# WiiM local AutoEQ / biquad optimizer

## Boundary and confidence

`calculate_autoeq_biquads` (entry reported by Ghidra dossier at the build's function; see Evidence references in `EVIDENCE.json`) is a native local routine that opens target, sweep, and recorded audio paths, requires matching sample rates, enforces record/reference length constraints, calls the sweep analysis path in mode 3 with 695 points, then produces up to five PEQ entries. These facts are `BINARY-VERIFIED` / `DECOMPILER-INFERRED`, `NOT-HW-VERIFIED`.

The user-facing WiiM app also contains a separate cloud Room Correction path that uploads measurements and receives a `peq.json` result. No evidence in this analysis proves that the local native AutoEQ routine is the production solver for that user flow. The app-to-native JNI mapping for this routine remains `UNKNOWN`; JNI_OnLoad only stores the JavaVM and returns JNI 1.6 in the inspected function. Keep local native AutoEQ and cloud-produced profile as separate mechanisms.

## Model and parameter limits

- Filter family observed: peaking biquad.
- Maximum 5 filters; candidate centers 20–300 Hz.
- Gain bounds −6…+20 dB; Q bounds 0.1…6.
- Candidate peaks whose absolute curve magnitude is below 0.2 are skipped; final entries with |gain| <=0.2 dB are omitted; emitted values rounded to 0.01.
- The candidate extraction uses low-frequency forward/reverse filtering at 300 Hz and extrema selection; direction/zero-phase interpretation is decompiler-inferred.
- Initial gain is roughly half the detected extremum; Q is initialized from the width at half amplitude and clamped. This is a decompiler reconstruction, not a proven exact standard peak-picking method.

## Objective and coefficient construction

The objective evaluates the total cascade response from all filters at each input frequency, converts magnitude to dB with a 1e−10 floor, then minimizes mean squared error against the input error curve:

`J = (1/N) * sum((20*log10(max(abs(product(Hk(f))),1e-10)) - target_error[f])^2)`

The model hardcodes Fs=48,000 Hz. Biquad coefficients use the standard peaking-EQ form documented in `DSP-FORMULAS.md`. Optimizer budget is 500 epochs, finite-difference step 0.1, update step 0.1 for center/gain and 0.05 for Q. Termination conditions include objective <0.15, 10 consecutive objective changes <0.001, or epoch cap. Those stopping semantics are `DECOMPILER-INFERRED`.

## Implementation implications for airControl

This evidence supports writing an independent, transparent low-frequency peaking-filter optimizer with explicit target curve, bounds, deterministic initial conditions, stop conditions, and predicted-response output. It does **not** justify copying WiiM's optimizer as the cloud room-correction algorithm or inferring that it is enabled in the UI. The sign convention must be defined by airControl's own target-minus-measurement convention and tested with a known synthetic response before using these native formulas.
