# WiiM Home Room Correction native DSP — static reverse engineering

**Status: APK-VERIFIED / NOT-HW-VERIFIED.** Static ARM64 code evidence only; no device execution.
**Target:** WiiM Home 3.6.10.260924, `libwiimundk.so`; SHA-256 `4e3159c5ed28490e7502692071da1e6bfeb1c2c592361492464f8fd74cd510ab`; ELF BuildID `a68007e72b0db19a91b9a6b6761fa9c20647e427`.
**Tool:** Ghidra 12.1.4 through REA MCP. Ghidra image base is `0x100000`; addresses below are image addresses, not file offsets.
**Prior canonical end-to-end report:** [WiiM Home Room Correction 3.6.10](WIIM-HOME-ROOM-CORRECTION-3.6.10-2026-10-28.md). This report deepens the native DSP subset.

REA query Evidence IDs and source hashes are indexed in [REA Evidence manifest](WIIM-HOME-ROOM-CORRECTION-DSP-REA-EVIDENCE-MANIFEST-2026-10-29.md). The full 23 MB REA bundle is retained locally; its SHA-256 is recorded in the manifest. The binary is stripped, and mixed FP/integer ARM64 parameters are imperfectly rendered by the decompiler. Use callsite instructions for ABI argument setup. REA call graphs include resolved call references; computed/indirect calls can remain unknown.

[Call graph](WIIM-HOME-ROOM-CORRECTION-DSP-CALLGRAPH-2026-10-29.md) · [Arguments and errors](WIIM-HOME-ROOM-CORRECTION-DSP-ARGUMENTS-ERRORS-2026-10-29.md) · [REA Evidence manifest](WIIM-HOME-ROOM-CORRECTION-DSP-REA-EVIDENCE-MANIFEST-2026-10-29.md)\n\n## Conclusions

- `time_align` requires equal WAV header sample rates and recording duration in [1×, 3×] reference duration. It does not resample. On success it computes delay and clamps to [-250, +2500] ms. Evidence `ev_5cdad1de588f90d106588e7a06e0444d2d07a1bf89edd88d036df19c5bbf4f4a`.
- `calrir_new` computes frequency-domain `Y/X`, inverse FFTs, divides by FFT length, copies a selected IR prefix and peak-normalizes it. Evidence `ev_6a0415b9ecaec57c6609c1701a850feca7241d74c0a766707610bd0a54a615ec`.
- `apply_ir_windows` crops around the largest absolute IR sample and applies left/right half-Tukey tapers. It does not independently detect or reject reflections. Evidence `ev_f8fd0cf60509fb6ee77cd77ea671536192e94dc6a0a40e4ccfeecdec32ded331`.
- `spl_sweep` derives 125 ms left / 800 ms right extents, uses a 262144-sample IR and calls `tfplots_new`. It normalizes response to the nearest 1 kHz point. Evidence `ev_f07d97ea59f39adae14233b0407a24d4c532faec186d73e4e3957eb1177244d8`.
- `rta_method` is not called by `spl_sweep`; it belongs to separate `measured_test_rta` flow at `0x1348e0`. Call graph `ev_989b5641357c48c5273b71d6c4fc1dcd5283967ca35185730b08ba6092545230`; wrapper `ev_ceb2f7def4213a53d598754c296889e0c6be7768dc3c73ff67f7f59800425d7b`.
- No sample-rate drift estimator/resampler is demonstrated in these functions. This is scoped absence, not a global claim about every app module.

## 1. `time_align` — `0x148a2c`

The function opens reference and recording WAV files, reads 44-byte headers, compares sample-rate fields at offset `+0x18`, and reads data-byte counts at `+0x28`; 16-bit sample count is `(bytes+1)/2`. Recording count must be >= reference and <= 3× reference. Samples are converted from signed 16-bit to float by division by 32768. DSP state is initialized from the shared rate (`0x149a48`). No resampling occurs before DSP.

Observed chain: `bandpass_2` both signals → reference/prompt end detection (`0x14a818`) and correlation/coherence (`0x14ce08`) → mode-specific filters and `crosscorr_peak_noise_std` (`0x14a528`) → IR-window recovery/check (`0x14d1a4`, `calrir_new`, reconstruction `0x14d38c`) → delay selection (`0x14d654`). Prompt missing/weak returns `-2`; missing main/sub sweep returns `-3`; other failures return `-1`.

Mode-dependent observed correlation inputs: call setup contains float pair 32.0 and integer 60 in the main route; the alternate sub route uses float pair 180.0 and integer 300. Both modes include a 15 Hz high-pass stage (constant `0x41700000`). The `0x14d1a4` threshold argument is 125.0 for mode zero, 12.5 otherwise. These are supplied constants; helper argument units/meaning are not fully documented by the binary.

Delay formula: `((found_index - sample_rate/2)/sample_rate)*1000` ms. Above +2500 clamps to +2500; below -250 clamps to -250 and still returns success.

## 2. `calrir_new` — `0x127a0c`

Recovered args: `param_1=X` real reference samples; `param_2=Y` recorded samples; `param_3` unused; `param_4=N` FFT length; `param_5` N-sample IFFT buffer; `param_6` output IR; `param_7=L` number of output samples.

It allocates KISS real forward/inverse FFT state, computes X and Y, then for each positive-frequency bin computes:
`Re=(Yr*Xr+Yi*Xi)/(Xr²+Xi²)`
`Im=(Yi*Xr-Yr*Xi)/(Xr²+Xi²)`
i.e. `Y*conj(X)/|X|² = Y/X` when the denominator is nonzero. For a zero denominator it writes sentinel bit pattern `0x2edbe6ff` into components (not literal zero). It inverse transforms to param_5, divides N samples by N, copies first L to param_6, then divides that prefix by its maximum absolute value if nonzero. Allocation failure logs and returns -1; success 0.

At caller `spl_sweep` instruction range `0x139b34–0x139b50`: x0 reference copy, x1 record copy, x2 reference count (unused), x3 FFT length, x4 IFFT output, x5 IR output, x6=262144 samples. This is disassembly-derived because the decompiler omitted args in its call expression.

## 3. `apply_ir_windows` — `0x129a50`

Requires left+right lengths equal total window length; mismatch returns 1. It finds the earliest maximum-absolute-value sample in the supplied IR. Start=peak-left length; if negative, shifts IR right with memmove, zero-pads front and re-finds peak/start. End=min(peak+right length, input count); calculated crop must equal requested length. It generates left/right half windows via `generate_half_tukey_window` at `0x129944`, backed by `tukey_window` at `0x129428`, then multiplies the selected IR into output.

For 0<alpha<1 the full Tukey window is unity in the center and raised-cosine at both edges. With normalized index x=i/(N-(sideFlag!=0)), left edge (x<alpha/2) is `0.5*(1+cos(pi*(2*x/alpha-1)))`; right edge (x>1-alpha/2) is `0.5*(1+cos(pi*(2*x/alpha-2/alpha+1)))`. Alpha<=0 or >=1 is an error. Alpha>=1 also writes a Hann-like curve before returning failure. `spl_sweep` supplies alpha=0.25. Peak-centering may be intended to anchor the impulse/direct arrival, but the code does not label direct/reflected paths; that semantic is inference only.

## 4. `spl_sweep` — `0x13991c`

Input count gate: record must be nonzero and in [reference, 3×reference], else -1. It derives:
- `Nfft=next_power_of_two(record_count)`;
- `left=floor(rate*125/1000)`;
- `right=floor(rate*800/1000)`;
- window length = left+right; work length = next power of two of that sum;
- geometric point count = integer `ln(rate/2)/0.009950321410848074`.

It copies inputs, calls `calrir_new`, then calls `apply_ir_windows` at `0x139b84–0x139bc0` (alpha .25; IR length 0x40000). If windowing returns nonzero, the next call uses raw/unwindowed IR; otherwise the windowed IR. Then `tfplots_new` (`0x127e2c`, evidence `ev_f3a92195374601b886d3d10cd3c189fff567fc4f6ac31ebdd68d2ebb1667f873`) FFTs IR, calculates magnitude per bin, groups FFT bins around geometric center frequencies, computes RMS magnitude per band, smooths either response or power (positive smoothing parameter uses a raised-cosine convolution), then computes `20*log10(value+1e-10)`. Finally, the nearest frequency to 1000 Hz is selected and its response is subtracted from every output point. `spl_sweep` returns 0 or -1.

At the ARM64 callsite, observed FP registers include s0=1.0, s2 with bits 0x3f8147ae (~1.01), s3=20.0 and s4=20000.0; integer setup includes w3=100, the forwarded mode/control, lengths and output buffers. Because the recovered prototype is mixed/poorly typed, only the constants and raw register setup are asserted here; do not assign all of these registers semantic labels from the decompiler signature. The called function itself constructs a geometric grid from its f0/ratio parameters and computes band RMS/dB. See [argument/error table](WIIM-HOME-ROOM-CORRECTION-DSP-ARGUMENTS-ERRORS-2026-10-29.md).

### RTA is separate

`rta_method` at `0x13392c` allocates a 65536-point KISS real FFT and log-band/smoothing buffers. It is called from `measured_test_rta` (`0x1348e0`), which builds the 20 Hz × 1.01 frequency grid and handles target/calibration curves. It is not a parameter/callee of `spl_sweep`; do not combine the two into one algorithm.

## 5. Drift compensation

**Not proven in analyzed path.** `time_align` rejects unequal nominal WAV rates and processes at one rate; `spl_sweep` accepts one sample rate. No explicit rate-ratio estimator, ppm drift loop, or resampler is visible in these function bodies and traced callees. It remains possible another module handles drift; static evidence here cannot exclude it globally.

## Evidence grades / limitations

**Direct/high:** entry points, gates, constants, equations in pseudocode/assembly, return branches and resolved call edges. **Derived:** unit conversions, window-duration arithmetic, relative 1 kHz response. **Unknown:** helper units, whether another application subsystem compensates clock drift, runtime/hardware/acoustic behavior. APK-only; NOT-HW-VERIFIED.

