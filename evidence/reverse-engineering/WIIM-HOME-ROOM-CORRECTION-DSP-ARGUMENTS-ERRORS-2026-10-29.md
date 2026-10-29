# WiiM native DSP arguments and error codes

Addresses are Ghidra image addresses. Evidence records are in [rea-evidence.json](WIIM-HOME-ROOM-CORRECTION-DSP-REA-EVIDENCE-MANIFEST-2026-10-29.md). Ghidra types for mixed FP/integer arguments are imperfect; use instruction callsites.

## Argument mapping

| Function | Arguments and observed use |
|---|---|
| `time_align` `0x148a2c` | (reference WAV path, recording WAV path, mode selector, output float delay-ms pointer) |
| `calrir_new` `0x127a0c` | (reference X, recording Y, unused value, FFT length N, N-sample IFFT destination, output IR, copied/normalized prefix length L) |
| `apply_ir_windows` `0x129a50` | (alpha, IR input, windowed output, left/right window buffers and scratch arguments, IR count, total/left/right lengths). At caller: alpha .25, IR count 0x40000; extents derived from 125 ms and 800 ms. Full register/stack call setup: 0x139b84–0x139bc0. |
| `spl_sweep` `0x13991c` | (reference pointer/count, record pointer/count, sample rate, opaque mode/control forwarded to TF, frequency output, response output, output point count) |
| `tfplots_new` `0x127e2c` | (start frequency, IR pointer, geometric ratio, rate/range args, mode, work buffers, smoothing/range/output arrays). Callsite FP registers include s0=1.0, s2 bits 0x3f8147ae (~1.01), s3=20.0, s4=20000.0; integer setup includes w3=100, mode/control and output pointers. Mixed-ABI parameter mapping is not fully reliable in the recovered prototype, so these are raw observed values, not all semantic assignments. |
| `rta_method` `0x13392c` | file path, smoothing/control integer, opaque context, two output arrays, count/control; invoked by measured-test wrapper, not spl_sweep. |

## Status/error summary

| Function | Return | Observed condition |
|---|---:|---|
| time_align | 0 | aligned delay written, possibly clamped |
| | -1 | file/header/init/allocation/rate/duration/filter/correlation/IR helper failure |
| | -2 | prompt missing or score too low |
| | -3 | main/sub sweep not detected |
| calrir_new | 0 / -1 | success / allocation failure |
| apply_ir_windows | 0 / 1 | success / length, crop, or half-window generation failure |
| spl_sweep | 0 / -1 | success / invalid length, allocation, calrir or tfplots failure |
| tfplots_new | 0 / -1 | success / allocation, smoothing, or zero-window-sum failure |
| rta_method | 0 / -1 | success / file, allocation, input/range or processing failure |

## time_align diagnostics

| Address/callsite | String |
|---|---|
| 0x148df0 | WAV header allocation failed. |
| 0x148e20 vicinity | Failed to open sweep file. |
| 0x148e4c | Failed to open record file. |
| 0x148e64 | Sample rates do not match. |
| 0x148e70 | Invalid record file. |
| 0x148e7c | init_state failed. |
| 0x148f30 / 0x149048 | bandpass_2 sweep/record failed. |
| 0x1491b8 | detect_ref_end failed. |
| 0x1491c4 / 0x149220 | prompt tone score too low / No prompt tone. |
| 0x149300 | correlation_coherence_ref failed. |
| 0x1494e4 | crosscorr_peak_noise_std failed. |
| 0x14950c | calrir_new failed. |
| 0x149684 | apply_ir_window_kp failed. |
| 0x14975c | record window reconstruction failed. |
| 0x149784 / 0x1497ac / 0x1497d4 | lowpass sub / highpass main / highpass sub record-window failure. |
| 0x149854 / 0x149874 | sweep not recovered by IR window / No main or sub sweep. |

