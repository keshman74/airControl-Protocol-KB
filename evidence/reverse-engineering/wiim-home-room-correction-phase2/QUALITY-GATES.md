# Quality gates, errors, and limits

All thresholds below are from the analyzed WiiM Home 3.6.10.260924 ARM64 `libwiimundk.so` image. Status: `BINARY-VERIFIED` for literal constants/call arguments, `DECOMPILER-INFERRED` for reconstructed branch meaning; all `NOT-HW-VERIFIED`.

| Stage | Observed check | Threshold / units | Outcome |
|---|---|---|---|
| Input compatibility | reference/capture sample-rate match and length/range checks in alignment path | exact branches in `time_align` dossier; sample-rate mismatch is rejected | `-1` general failure path (exact subtype should not be inferred) |
| Prompt candidate | `fast_ncc` | maximum normalized absolute coefficient >= **0.1** | failure returns `-2` |
| Prompt integrity | `crosscorr_peak_noise_std` | peak / std(abs-correlation sidelobes) >= **12.0**, window **20 ms** | marker rejected otherwise |
| Main sweep | filtered correlation plus IR recovery/onset | high-pass **15 Hz**; peak/noise >= **32**, window **60 ms** | missing recovered sweep can return `-3`; later failure `-1` |
| Sub sweep | 500 Hz low-pass then 15 Hz high-pass; IR recovery/onset | peak/noise >= **180**, window **300 ms** | missing recovered sweep can return `-3`; later failure `-1` |
| Delay output | selected index transform | `((index−Fs/2)/Fs)*1000`, clamp [−250,+2500] ms | selected delay or error |
| Calibration points | frequency range and dB clamp | inclusive 20–20000 Hz; clamp ±16 dB; >=2 rows | fewer than two returns −1 |
| RTA input | WAV sample count | `n > max(65535,13*Fs)` and (`n <= 30*Fs` or `42*Fs < n <= 60*Fs`) | invalid duration path returns failure |

`crosscorr_peak_noise_std` details: linear FFT correlation, earliest absolute maximum on ties; noise samples are absolute correlation magnitudes excluding `[peak−int(1.2W), peak+W)`, where `W=int(window_ms*Fs/1000)`. The ratio uses `std + 1e−10`. This is a relative peak-vs-correlation-background score, **not dB SNR** and not coherence.

### Not evidenced in the inspected path

- No explicit coherence computation was identified in the time-alignment or RTA functions inspected.
- No explicit clipping detector/ADC overload threshold was recovered in this Phase 2 scope.
- The pre-roll noise is handled indirectly by marker envelope/correlation checks; no absolute noise-floor calibration was found.
- No explicit retry loop based on a runner-up / best-peak ratio was found in the correlation helpers inspected. Cross-correlation standard deviation can reduce acceptance when many large sidelobes exist, but does not establish a specific ambiguity ratio.
- A partial sweep can exceed the fast-NCC floor: the synthetic truncated fixture retained 2300/4096 samples and measured 0.751744 versus 0.1. This only shows that the early NCC gate is permissive for that fixture; later IR reconstruction and main/sub checks may reject it.
- Independent sample-clock drift compensation is not established. Equal sample rates are expected/rejected when unequal; no resampling, ppm estimator, time stretcher, or record-end marker correction was found in the scoped call path. This is not a global claim about all WiiM code.

## Synthetic fixture results

Command: `python3 tests/synthetic_phase2.py` (stdlib only; deterministic seeded fixtures; no hardware, no playback, no firmware changes).

| Fixture | Result | What it demonstrates |
|---|---|---|
| 211-sample delay + weaker reflection | PASS; exact 211 samples; NCC 0.963704 | Basic known-delay correlation fixture |
| Periodic FIR response DFT identity | PASS; MAE 0 dB | DFT fixture mathematics, not `tfplots_new` equivalence |
| ±25/50/100 ppm synthetic drift | PASS; exact estimator values | Drift is observable in this separate synthetic estimator; **not** evidence WiiM compensates it |
| 20:1 noise RMS-to-signal fixture | PASS; NCC 0.024425 < 0.1 | Low-NCC rejection under this generated condition |
| Two separated equal peaks | PASS; both NCC 0.999998 | Harness detects ambiguity; no WiiM runner-up ratio was found |
| Truncated sweep padded to valid length ratio | PASS as a test; NCC 0.751744 passes 0.1 | Early NCC alone does not reject this truncated fixture |
| Missing marker deterministic noise | PASS; maximum NCC 0.094968 < 0.1 | NCC rejection for this fixture; detector itself not emulated |

These are **synthetic fixture outcomes**, not validation of the proprietary full alignment implementation. The harness deliberately separates expected fixture behavior from claims about the binary.
