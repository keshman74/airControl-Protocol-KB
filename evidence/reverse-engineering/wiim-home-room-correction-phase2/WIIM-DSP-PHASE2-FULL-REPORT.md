# WiiM Home Room Correction — Deep DSP Research, Phase 2

**Artifact status:** `BINARY-VERIFIED` / `DECOMPILER-INFERRED` as marked per claim; all results are **NOT-HW-VERIFIED**. App-level use of local AutoEQ is partially `UNKNOWN`. This is static analysis plus independent synthetic fixtures. No device, firmware, EQ, or acoustic test was touched.

## Executive summary

Phase 2 closes several specific gaps and also narrows claims from the earlier analysis:

1. `time_align` uses a staged detector. It is not a single correlation threshold: a prompt NCC floor of **0.1**, a marker peak-to-correlation-noise ratio of **12** over a 20ms window, and later main/sub sweep checks (32/60ms and 180/300ms) are separate gates. The ratio is not dB SNR or coherence.
2. The mode-dependent alignment window has a directly recoverable edge-cosine formula. Its taper occupies 12.5% at each edge, with a flat center. Do not confuse it with the distinct `spl_sweep` response-extraction half-Tukey window reported in Phase 1.
3. Main alignment applies a 15Hz high-pass. Sub alignment applies a 500Hz second-order low-pass followed by 15Hz high-pass. `bandpass_2` contains three SOS sections per state bank, but its exact cutoff semantics remain unresolved.
4. The inspected path does not show resampling, ppm estimation, or time stretching. It expects compatible sample rates and rejects mismatch. This is a scoped absence finding, not a statement about all firmware/app code.
5. Mic correction in the local `auto_adjust_rc_freq_rta` route is normalized at nearest 1kHz and **subtracted** from the similarly normalized measured response. This is not proof that WiiM's cloud Room Correction uses this local calibration path.
6. `calculate_autoeq_biquads` exposes a local constrained peaking-EQ optimizer with a 48kHz model and an explicit mean-square objective. Its role as the app's production solver remains unproven; the user flow includes cloud-returned `peq.json`.
7. Synthetic fixtures passed, but the truncated-sweep fixture passes the early NCC threshold. This supports adding independent completeness and ambiguity checks in airControl v0.7.

## Scope and provenance

- App: WiiM Home 3.6.10.260924 APK; SHA-256 `99ebfac7f76ecb6c33b6988ab8ca11bb0833e22329e323f7299546cdc5da490a`.
- Source container XAPK SHA-256 `b2d474f4048d416b08deeae915cceb4b157b78a5778019d71e6084b92c9c5b9a`.
- Native ARM64 ELF: `libwiimundk.so`; SHA-256 `4e3159c5ed28490e7502692071da1e6bfeb1c2c592361492464f8fd74cd510ab`; ELF BuildID `a68007e72b0db19a91b9a6b6761fa9c20647e427`; Ghidra 12.1.4.
- Calibration input was read-only: `imm6-99-03503.txt`, SHA-256 `170036dbd1a7466c2a796259c31524fe612f42e4708bd169ddbd6216e73beaa9`; 256 parsed rows, 20–20000 Hz, −3.3…+0.8 dB.
- Prior baseline report and KB command docs were consulted. Existing Phase 1 findings are linked and not claimed as novel here.
- Evidence IDs and confidence metadata: `EVIDENCE.json`; full provider snapshot/source dossier remains under the parent research directory. Individual raw binaries and large snapshots are intentionally not proposed for the KB.

## A. Synchronization and delay

### Ordering

`time_align` at `0x148a2c` first conditions reference/capture through initialized IIR banks, checks for the prompt marker, locates its correlation peak and background statistic, then follows main or sub sweep processing. It reconstructs/validates sweep IR, selects an onset, applies the mode-specific window and performs a later correlation/noise test before converting/clamping delay. See the detailed formulas and function graph.

### Prompt and peak gates

`fast_ncc` uses mean-centered reference samples and rolling window energy from the second sequence, with FFT correlation. A candidate maximum absolute normalized coefficient must be >= **0.1**. This is a permissive early presence gate. `crosscorr_peak_noise_std` computes linear FFT correlation against reversed reference, selects the earliest maximum-absolute sample on ties, excludes an asymmetric interval around the peak from the absolute-correlation noise population, then compares peak magnitude to the population standard deviation plus epsilon.

At the first marker the call arguments resolve to ratio **12.0** and window **20ms**. The later main path passes **32.0 / 60ms**; the sub path passes **180.0 / 300ms**. These ratios are dimensionless. They should not be described as SNR dB or coherence. Complete formula appears in `DSP-FORMULAS.md`.

### Reference prompt / Hilbert envelope

`detect_ref_end` at `0x14a818` operates on 256-sample blocks. The call path includes Hilbert/analytic-envelope helpers at `0x1501f0` and `0x1502e8`, a cosine/Hann-type block taper, weighted envelope-square accumulation, and contiguous-run tracking. State initialization includes block count 85, another count 10, and floating parameters 20.0, 1.5, 0.065, 0.45, 0.065. The exact semantic units and all interaction of those state fields are not fully reconstructible from this optimized pseudocode; the 1.5 value is not asserted to be milliseconds. The first correlation checks are independent evidence of the prompt gate.

### Filters and main/sub verification

- Main: 15Hz high-pass.
- Sub: 500Hz second-order low-pass then 15Hz high-pass.
- Initial prompt conditioning also calls `bandpass_2`, which stores three SOS sections per bank. Its exact filter-edge frequencies cannot be reliably inferred from the available state semantics.
- Main/sub validation uses distinct noise-ratio thresholds and windows, plus IR recovery. `apply_ir_window_kp` uses 125ms left / 800ms right for main and 12.5ms left / 800ms right for sub, with a 262144 sample IR bound.

### Delay and failure codes

The inspected delay selection path converts an index as `((selectedIndex−Fs/2)/Fs)*1000` ms, then clamps to [−250,+2500] ms. The alignment path returns `-2` on prompt/NCC gate failure; `-3` when required main/sub reconstructed sweep is missing; other failures use `-1`. Do not assign more detailed subcodes without the relevant branch evidence.

### Drift

Within `time_align`, `detect_ref_end`, the correlation helpers, and their inspected callees, no resampler, interpolation-based sample-rate correction, ppm fit, time stretcher, or insert/drop-sample loop was identified. The path checks sample-rate compatibility. It does not follow that all app or cloud code lacks drift correction. Drift remains **UNKNOWN outside the analyzed native path**.

## B. IR windows and response calculation

The alignment helper's window equation and bounds are in `DSP-FORMULAS.md`. The endpoint taper is a half-cosine down to zero, flat through the middle, with 12.5% of the window at each end. The algorithm builds separate side windows and applies them around onset after crop-bound clamping.

This resolves the previously ambiguous formula for `apply_ir_window_kp`, not every internal detail of `calrir_new` nor the distinct `apply_ir_windows` response-analysis function. Phase 1 report remains authoritative for already verified FFT deconvolution, response extraction and function parameters. Residual exact denominator floor/regularization and low-level IFFT scaling must be retained as unknown unless the Phase 1 evidence directly proves them; no claim is added here.

`rta_method` is observed to use a 65536-point real FFT and a logarithmic frequency grid with adjacent center ratio about 1.0072216 (`10^(0.3/96)`). `auto_adjust_rc_freq_rta` evaluates a separate 695-point grid `20*1.01^i`. These are distinct grids in different routines. Do not merge them into one presumed final EQ grid.

## C. Calibration

The parser accepts frequency/dB pairs (space/comma/tab/newline delimiters), stores up to 2000 rows and needs at least two usable points. The selected range is inclusive 20–20000Hz; correction values clamp to ±16dB. The correction and measured response are interpolated in log-frequency and each normalized at its nearest 1kHz sample. The correction is subtracted from normalized measurement. Exact file suffix alternatives and extrapolation edge-policy names remain unknown; endpoint behavior should be inspected before claiming a particular extension rule.

The supplied iMM-6 curve is syntactically within the parser's range, but this does not establish the mic's measurement chain, serial-specific calibration validity, orientation, host gain, or whether it is appropriate for another external microphone. It also does not prove cloud Room Correction consumes this file.

## D. Quality, SNR, coherence

Concrete gates are tabulated in `QUALITY-GATES.md`. Found: sample-rate/length compatibility, normalized correlation, peak-vs-correlation-background checks, reconstructed IR/main/sub verification, and duration constraints in RTA ingestion. Not found in the inspected scope: explicit coherence metric, calibrated dB SNR, absolute pre-roll noise floor, explicit clipping detector, or a best-vs-runner-up ambiguity ratio. These remain unknown, not absent globally.

The user-noted higher A33 pre-roll noise cannot be judged solely by the 12.0 marker correlation ratio. That ratio is local to correlation magnitude and sidelobe standard deviation; no absolute dB floor was recovered. v0.7 should log the pre-roll RMS/peak and clipping fraction as its own diagnostics and set thresholds from actual recordings, not transplant WiiM values blindly.

## E. AutoEQ and app boundary

The native local routine and objective are documented in `AUTOEQ-OPTIMIZER.md`. Key reusable facts are the peaking biquad coefficient equations, 48kHz model, parameter bounds, filter count and stopping budget. Candidate selection details and optimizer stopping semantics have decompiler uncertainty.

The app has a separate cloud path: measurement upload/task and returned `peq.json`, documented in the existing Phase 1 app report. The JNI_OnLoad function analyzed only saves JavaVM and reports JNI 1.6; no registration linking the local optimizer to app Room Correction was observed. Consequently:

- Local optimizer existence: `BINARY-VERIFIED`.
- Local objective/coefficient interpretation: `DECOMPILER-INFERRED`.
- Direct app Room Correction invocation of this optimizer: `UNKNOWN`.
- Cloud solver internal math: `UNKNOWN`.

## F. Synthetic evaluation

All fixtures in `tests/synthetic_phase2.py` pass. Full parameter/output table is in `QUALITY-GATES.md`; JSON console output is reproducible by rerunning the script. It is stdlib-only and tests isolated properties, not an end-to-end proprietary clone. Particularly actionable result: a truncated sweep with 2300/4096 samples yields NCC 0.751744, above the 0.1 gate. The early NCC test alone is not a completeness test.

## G. Comparison with airControl v0.5/v0.6

Existing scripts are offline analysis utilities, not device control and not PEQ production implementations. v0.5 uses reference hash guards, banded STFT active-vs-pre-roll diagnostic (not coherent SNR), and a single 500–2000Hz/near-1k normalization; it has no mic calibration. v0.6 adds local section correlation/repeatability checks and regularized spectral inversion `power + peak*1e−5`; it still does not estimate clock drift or produce calibrated PEQ. The WiiM path differs by staged prompt detection, peak/noise ratio gates, main/sub filter paths, IR recovery/onset and multiple distinct frequency grids. Full comparison references are retained in the local workspace docs/scripts; no v0.5/v0.6 source was edited.

## H. What is usable for airControl v0.7

Directly implementable after independent unit tests: the documented peaking-biquad equations and explicit objective model; log-frequency interpolation/calibration subtraction with a sign test; diagnostic NCC and peak-vs-background statistics; mode-specific 500Hz/15Hz filters if our sub/main semantics justify them; and the observed alignment window as an optional compatibility mode.

Do not copy uncalibrated thresholds as product defaults. Do not call the synthetic drift estimator WiiM behavior. Keep unknowns explicit: exact prompt block parameter meanings, bandpass cutoff response, all onset-selection details, a complete final `tfplots_new` smoothing/edge rule, the calibration suffix/extrapolation variants, app-to-local-AutoEQ JNI binding, cloud optimization, actual device sample-clock behavior, and hardware playback results.

## I. KB proposal and history

New proposed KB addition: this Phase 2 evidence report plus formulas, quality gates, AutoEQ boundary, and v0.7 implementation spec. It refines Phase 1, rather than overwriting it. Status labels should remain `APK/BINARY-VERIFIED / NOT-HW-VERIFIED`, with inference and unknown fields per claim. Separate KB PR is being prepared against canonical base commit `cc77e7e5da9f9139ff177e261003ae7b8e64a95b`; no direct main branch write.

## Files

- `FUNCTIONS-AND-CALLGRAPH.md`
- `DSP-FORMULAS.md`
- `QUALITY-GATES.md`
- `AUTOEQ-OPTIMIZER.md`
- `AIRCONTROL-V07-IMPLEMENTATION-SPEC.md`
- `EVIDENCE.json`
- `tests/synthetic_phase2.py`
