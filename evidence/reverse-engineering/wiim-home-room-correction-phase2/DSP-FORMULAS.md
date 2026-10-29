# WiiM Home Room Correction Phase 2 — DSP formulas

Status key: `BINARY-VERIFIED` means the operation/constant is directly present in the analyzed shipped ELF and supported by Ghidra pseudocode/assembly; `DECOMPILER-INFERRED` means semantic reconstruction from compiler-generated pseudocode; `SYNTHETIC-VERIFIED` applies only to the independent fixtures. All findings are `NOT-HW-VERIFIED`.

## Correlation and marker quality

### Fast normalized correlation (`fast_ncc`, 0x14a...; see `EVIDENCE.json`)

For each overlap, the first vector is mean-centered. The second vector's rolling energy is calculated without subtracting its local mean. The correlation is FFT-based, with normalization by the first vector energy and each second-window energy. A valid max absolute coefficient must be at least **0.1** (state +0x98 set by `init_state`, 0x149a48). This is a coarse candidate gate, not a quality guarantee. `BINARY-VERIFIED` for operations/constants, `DECOMPILER-INFERRED` for exact variable semantics.

### Peak-to-noise statistic (`crosscorr_peak_noise_std`)

For signal `x`, reference `r`, and sample rate `Fs`, compute linear correlation by FFT convolution of `x` and reversed `r`, length `N+M−1`. Select the earliest index attaining maximum absolute magnitude `p`. Let `W = int(window_ms*Fs/1000)`. The noise population comprises absolute correlation samples outside `[p−int(1.2W), p+W)`. Compute its population standard deviation `σ`. Accept when `abs(c[p])/(σ+1e−10) >= threshold`. The first-marker caller passes **threshold 12.0** and **window 20 ms**. Subsequent main-sweep check uses threshold **32.0**, window **60 ms**; sub path uses **180.0**, **300 ms**. These are caller/state-specific checks, not a conventional calibrated SNR in dB. `BINARY-VERIFIED` / `DECOMPILER-INFERRED`.

## `detect_ref_end` / `time_align`

`detect_ref_end` (0x14a818) works on 256-sample blocks, filters the reference/capture using the initialized IIR banks, obtains an analytic/Hilbert envelope, applies a Hann-like block weight `0.5*(1−cos(2πi/(L−1)))`, and accumulates weighted envelope-square divided by block length. The initial block average count is state +0x8c = 85; a 10-block parameter and 20.0 / 1.5 parameters also enter the detector. The detector has contiguous-run state. The returned location adjusts by an expression involving `int(param8*param2)`; parameter units and all run semantics remain `UNKNOWN`, so do not treat 1.5 as a verified milliseconds value. `DECOMPILER-INFERRED`.

`time_align` (0x148a2c) first checks marker presence through fast-NCC >=0.1 and marker peak/noise >=12 at 20 ms, then validates recovered main or sub sweep through filtered correlation, IR reconstruction/onset selection, mode-specific IR windowing, and a second peak/noise gate. Main alignment uses 15 Hz high-pass. Sub alignment uses a 500 Hz second-order low-pass followed by 15 Hz high-pass. The mode filters are separate from the preceding prompt detector's three-SOS IIR bank; the latter's exact cutoff response is unresolved. No explicit runner-up-peak ratio comparison was found in the inspected correlation helpers; the sidelobe/noise standard deviation can penalize competing peaks indirectly. No verified retry loop for ambiguity was identified.

Delay output is derived from the selected correlation/IR index using `((selectedIndex−Fs/2)/Fs)*1000 ms` in the existing analyzed path and is clamped to [−250, +2500] ms. Missing main/sub reconstructed sweep returns −3; prompt/NCC gate failure returns −2; other alignment failures return −1. Confirm branch-level details in `QUALITY-GATES.md`.

### Mode-specific IR window (`apply_ir_window_kp`, 0x14d1a4; window builder 0x150abc)

The alignment path chooses left duration 125 ms (main) or 12.5 ms (sub), right duration 800 ms. The code computes left sample count `L=int(Fs*left_ms/1000)` and right count `R=int(Fs*800/1000)`, clips the crop around the detected onset to the 262144-sample IR buffer, and multiplies separate left/right windows.

The window builder initializes a length-`N` array to 1. For normalized index `u=i/(N−1)`, it changes only the outer 12.5%:

```
w(u) = (1 + cos(π(8u−1))) / 2,   0 <= u < 0.125
w(u) = 1,                         0.125 <= u <= 0.875
w(u) = (1 + cos(π(8u−7))) / 2,   0.875 < u <= 1
```

The left side copies the first `R` requested entries; the right side copies from offset `R` in the generated window. These are edge half-cosine tapers with a flat middle. This is **not evidence of a generic Tukey alpha=0.25**: the tapers occupy 12.5% per edge (25% combined), and apply to the aligner's separately sized left/right segments. `BINARY-VERIFIED` for formula/indices; `DECOMPILER-INFERRED` for naming/semantic interpretation.

Do not conflate this path with `spl_sweep` response-extraction windowing (documented in the Phase 1 report as 125 ms pre-onset, 800 ms post-onset, half-Tukey α=.25). They have different callers and evidence.

## Calibration curve application

`get_calibration_data_new` selects entries with `20 <= f <= 20000 Hz`, clamps correction to [−16,+16] dB, and requires at least two points. `auto_adjust_rc_freq_rta` builds `f_i=20*1.01^i` (695 points) and interpolates in log10-frequency. With mic calibration `C(f)` and measured response `R(f)`, both are normalized at nearest 1 kHz sample and calibration is **subtracted**:

```
Rcorr(f) = (R(f) − R(1 kHz)) − (C(f) − C(1 kHz))
```

This establishes the sign in this local analysis path. It does not establish that this calibration curve is applied to WiiM's cloud-produced room-correction profile. `BINARY-VERIFIED`/`DECOMPILER-INFERRED`; not hardware verified.

## `rta_method`

Uses a 65536-point real FFT and a logarithmic frequency-band grid with adjacent center ratio `10^(0.3/96) ≈ 1.0072216` (approximately 1/24-octave spacing); centers follow `1000*10^(0.3*k/96)` up to indexing convention. The input WAV length gate is a disjoint duration predicate: length exceeds max(65535,13*Fs), and either is <=30*Fs or lies in (42*Fs,60*Fs]. Do not infer why those durations are accepted. `BINARY-VERIFIED` for FFT/grid constants and predicate; exact downstream band aggregation semantics remain only as decompiler-resolved as indicated in `EVIDENCE.json`.

## AutoEQ objective and peaking biquad

The separately exposed local `calculate_autoeq_biquads` path uses at most five peaking filters, centers 20–300 Hz, gain [−6,+20] dB, Q [0.1,6]. The objective helper computes mean squared error over the supplied frequency samples:

```
J(θ) = (1/N) Σi (20 log10(max(|Πk Hk(fi;θk)|, 1e−10)) − ei)^2
```

The objective's sample rate is fixed at 48 kHz. Here `e_i` is the supplied target error curve. Each peaking biquad is formed with `A=10^(G/40)`, `ω=2πfc/48000`, `α=sin(ω)/(2Q)`, and `D=1+α/A`:

```
b0=(1+Aα)/D; b1=−2cos(ω)/D; b2=(1−Aα)/D
a0=1; a1=−2cos(ω)/D; a2=(1−α/A)/D
```

The optimizer runs up to 500 epochs, finite-differences parameters with step 0.1, updates fc/gain by 0.1 and Q by 0.05; stop conditions include MSE <0.15, 10 consecutive changes <0.001, or 500 epochs. Candidate extrema with absolute magnitude <0.2 are skipped; output filters with |gain|<=0.2 are omitted and output values rounded to 0.01. Exact stopping/parameter ordering should be rechecked against the referenced function evidence before implementing a byte-for-byte compatible clone. This local routine's use as the app's production solver is `UNKNOWN`.
