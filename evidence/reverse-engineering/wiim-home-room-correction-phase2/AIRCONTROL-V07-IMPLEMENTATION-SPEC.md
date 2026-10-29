# airControl Room Correction Engine v0.7 — evidence-based implementation spec

This is a proposal for our own engine, not a WiiM clone. It uses directly recoverable algorithms where useful and marks independent design choices explicitly. Do not deploy to devices or set EQ from this research report.

## Measurement ingress and input checks

1. Preserve raw microphone WAV and metadata immutably; validate PCM format, channel count, sample rate, nonzero level, clipping fraction, duration, and expected prompt markers.
2. Reject sample-rate mismatch unless an explicitly designed resampler path is enabled. WiiM's inspected path rejects mismatch; it does not provide a recovered drift-compensation mechanism.
3. Detect prompt marker with block envelope and normalized correlation; report NCC, peak/noise score, chosen lag, and ambiguity (best-vs-runner-up) separately. WiiM evidence provides candidate thresholds NCC 0.1, marker ratio 12 at 20ms, but these values require calibration to our prompt/recording chain before adoption.
4. Require a minimum recovered sweep fraction and independent main/sub checks. The Phase 2 synthetic result demonstrates why the NCC floor alone is insufficient.
5. Explicitly measure clock drift from repeated known markers if recording supports them. Any fitted ppm correction is our own extension and must be validated with independent sample-rate fixtures; never label it WiiM-derived.

## IR recovery and response extraction

1. Implement deconvolution from known sweep with double-precision FFT, explicit denominator floor/regularization, documented IFFT normalization, and peak/onset quality diagnostics. The exact proprietary `calrir_new` denominator treatment and several low-level normalization details remain incompletely established; expose them as choices in v0.7.
2. Preserve the complete IR and window metadata. For a WiiM-aligned comparison mode only, implement the verified onset crop extents and cosine edge taper from `DSP-FORMULAS.md`, and name it `wiim_observed_alignment_window`; do not conflate with `spl_sweep`'s separate response window.
3. Compute response on a defined log-frequency grid, with explicit aggregation/smoothing and 1 kHz normalization. The `rta_method` 65536 FFT/log-band grid is a useful observed reference, but exact final smoothing and all low-level `tfplots_new` semantics are not fully established.
4. Apply microphone calibration by log-frequency interpolation and 1 kHz-relative subtraction only after confirming the calibration file's sign and measurement-chain convention. Keep raw, calibrated, and normalized curves in output.

## AutoEQ solver

1. Define a target curve and allowable correction region separately; identify the error sign convention in API names (`target_minus_measurement_db`).
2. Start with constrained peaking biquads. The WiiM native local routine offers a useful observed envelope: max five filters, center 20–300 Hz, gain −6…+20 dB, Q 0.1…6, model at 48 kHz. Treat these as reference limits, not mandatory product choices.
3. Minimize explicit weighted squared error with regularization on filter count, boost, Q, and adjacent center crowding. Those regularizers are our design extensions.
4. Produce predicted response, residual, convergence status, and warnings for uncorrectable nulls/low-SNR bins. Validate coefficient serialization and predicted/filtered frequency response against independent analytic cases.
5. Keep analysis/local preview separate from device write. Any hardware command path must be a separate, reviewed feature, with user action and rollback.

## Suggested acceptance suite

- Deterministic known delay/echo and distinct reflection fixtures.
- FIR response comparison against direct frequency response.
- Noise and clipping sweeps; cutoff values derived from recorded input distributions, not imported blindly from WiiM.
- Equal/near-equal peak ambiguity and truncated-prompt fixtures.
- Synthetic ppm drift tests at ±25/50/100 ppm; tests must fail if expected drift is silently ignored.
- Calibration sign test using known response and known calibration perturbation.
- Biquad coefficient magnitude/phase checks and end-to-end predicted-response check.

Synthetic tests in this directory currently cover only delay/NCC, DFT response identity, drift-estimator observability, low-NCC noise, equal peaks, truncation, and missing marker. They are scaffolding, not complete v0.7 conformance tests.
