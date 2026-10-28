# WiiM Home Room Audio Correction end-to-end mechanism

Status: **APK-VERIFIED / NOT-HW-VERIFIED**

## Artifact provenance

- XAPK: `WiiM Home_3.6.10.260924_apkcombo.com.xapk`
- Base package: `com.linkplay.wiimhome`
- Version: `3.6.10.260924`
- Version code: `2026092420`
- Base APK SHA-256: `99ebfac7f76ecb6c33b6988ab8ca11bb0833e22329e323f7299546cdc5da490a`
- Static analysis: JADX Headless 0.7.1 / REA
- APK was not executed; no device commands were sent.

## Functional pipeline

```
Room Correction entry/version gate
  -> fetch RC config
  -> select sweep/pink reference files and durations
  -> disable current EQ and RC
  -> set device RC mode MEASURE
  -> play reference sweep/pink audio
  -> phone AudioRecord/Oboe captures WAV/PCM
  -> validate level/SNR/duration
  -> upload recordings and metadata
  -> cloud taskId/result polling
  -> download result archive
  -> unpack PEQ/output files
  -> optional local file checks/plots
  -> build PEQ JSON payload
  -> apply EQBand profile to device
  -> set DynamicEQ/RC mode PLAYBACK
  -> verify/store profile
```

## Main classes

UI/state machine:

- `FragRCIntroduction`
- `FragRCSettings`
- `FragRCStepPreparation`
- `FragRCStepAudioCheck`
- `FragRCStepMeasure`
- `FragRCStepAnalyzing`
- `FragRCStepVerifyCorrection`
- `FragRCStepSaveEQLR`
- `FragRCStepSaveEQStereo`
- `FragRCProfileList`
- `FragRCFilterDetail`
- `FragRCSubMeasure`

Services:

- `RoomCorrectionManager`: cold-start/config/version state.
- `RCRepository`: RC status/config repository.
- `DataController`: download, upload, file processing, result handling, RC/EQ state.
- `RCEQManager`: disable/enable EQ, apply PEQ JSON, profiles and DynamicEQ mode.

Audio:

- `AudioRecorder`
- `OboeRecorderImpl`
- `RecordConfig`
- `FileUtil`

Models:

- `PeqData(freq, gain, q, mode)`
- `FrequencyResultData(frequency, raw, smoothed, target, error, equalization, parametric_eq, ...)`
- `DetectData`
- `ProfileData`
- `NameEQEntity`

## Step 1: config and capability

`RoomCorrectionManager.runColdStart` uses the current app version (`2026092420`), device ID, timeout and a report flag. It stores `last_rc_version` in `room_correction_prefs`.

`DataController.fetchRoomCorrectionConfigWithRetry...` obtains the RC configuration. The configuration supplies:

- sweep file;
- sweep duration;
- pink-noise reference files;
- pink durations;
- channel-specific reference data;
- minimum version/config values.

The APK does not hardcode one universal sweep duration; it reads it from `CloudRCConfig`.

## Step 2: preparation and disabling existing processing

Before measurement, the flow disables current EQ and Room Correction. `RCEQManager` contains separate success/failure paths for:

- “EQ off”;
- “RC off”.

The code logs `EQ 关闭成功!` and `RC 关闭成功!`.

This is required so the microphone captures the speaker/room response without the old correction profile active.

## Step 3: device measurement mode and reference playback

`DynamicEQStatus` contains at least:

- `MEASURE`
- `PLAYBACK`

`RCEQManager.v(DeviceItem, DynamicEQStatus, callback)` checks device/project support and delegates the device operation to `xt1.W1(deviceItem, statusCode, callback)`.

During measurement, the app requests a reference file from config and calls the DataController playback path. For subwoofer and channel variants the source is selected from:

- `room_correction.sweep_file`
- `room_correction_refpink_l`
- `room_correction_refpink_r`
- `room_correction_refpink`

## Step 4: phone microphone capture

`AudioRecorder` uses Android `AudioRecord` and an Oboe implementation. Captures are written to local WAV/PCM files.

Observed names include:

```
room_correction_sweep-3.wav
record_L
record_R
record_C
record_pink_L
record_pink_R
record_pink_C
record
record_temp
```

`FragRCStepMeasure` supports left/right/center and repeated measurement passes. It checks recording status, timeout, level and SNR. Error classification uses `FftType` values such as DB_HIGH, DB_LOW, SNR and LENGTH_ERROR.

## Step 5: upload and cloud analysis

`FragRCStepAnalyzing` uploads recorded material through `DataController`. The upload path uses:

- `AutoEQUploadRequest`
- `UploadResponse`
- `S3KeyInfo`
- `UrlMode`
- returned `taskId`

The app then polls/downloads the result. The result may be an archive; the code explicitly extracts it and looks for an output key. The APK contains no complete local replacement for the cloud optimization algorithm.

## Step 6: result representation

The result is represented as frequency/target/error data plus PEQ filters.

`FrequencyResultData` fields:

```
frequency
raw
smoothed
target
error
error_smoothed
equalization
equalized_raw
equalized_smoothed
parametric_eq
first_result
```

`PeqData` fields:

```
freq: double
gain: double
q: double
mode: int
```

This is parametric EQ, not the 10-band integer Eq10HP slider model.

## Step 7: result files

The apply stage reads:

- `peq.json` for mono;
- `peq_L.json` and `peq_R.json` for stereo;
- `peq_L.json`, `peq_R.json`, `peq_C.json` for multi-channel mode.

The JSON contains at least:

```json
{
  "pluginURI": "...",
  "EQBand": [...]
}
```

Each EQ band carries the PEQ parameters represented by the app as frequency/gain/Q/mode.

## Step 8: apply commands/wrappers

The exact device transport is hidden behind obfuscated `xt1` methods, but the payload construction is visible in `RCEQManager`.

Mono method `w(...)` builds:

```json
{
  "EQLevel": 2,
  "pluginURI": "...",
  "EQBand": [...],
  "UpdateAt": "<unix-ms>",
  "rc_output": "<output identifier>"
}
```

Stereo method `x(...)` builds:

```json
{
  "EQLevel": 2,
  "pluginURI": "...",
  "EQBandL": [...],
  "EQBandR": [...],
  "UpdateAt": "<unix-ms>",
  "rc_output": "<output identifier>"
}
```

Multi-channel method `y(...)` builds:

```json
{
  "EQLevel": 2,
  "pluginURI": "...",
  "channelMode": "multi",
  "EQBandL": [...],
  "EQBandR": [...],
  "EQBandC": [...],
  "UpdateAt": "<unix-ms>",
  "rc_output": "<output identifier>"
}
```

Dispatchers:

- mono/multi apply: `xt1.U1(device, json, callback)`
- stereo apply: `xt1.V1(device, json, callback)`
- DynamicEQ state: `xt1.W1(device, statusCode, callback)`

These are app-level wrappers; this APK evidence does not by itself reveal the final HTTP/TCP/UART wire command emitted by `xt1`.

## Step 9: playback mode and verification

After applying results the app switches the device to:

```
DynamicEQStatus.PLAYBACK
```

The app also has status/profile paths through `RCEQManager.o`, `EQRequest` and `RCRepository`. Profiles are represented by `NameEQEntity` and `ProfileData`.

The result/profile can be displayed in `FragRCFilterDetail`, which parses PEQ values into `PeqData`.

## Important limits

**APK-VERIFIED**

- end-to-end state machine and class responsibilities;
- microphone capture and file naming;
- cloud upload/task/result workflow;
- PEQ model fields;
- mono/stereo/multi JSON payload shapes;
- EQ/RC disable before measurement;
- DynamicEQ MEASURE/PLAYBACK states;
- device apply dispatchers `xt1.U1/V1/W1`.

**NOT ESTABLISHED**

- exact cloud fitting algorithm;
- exact sweep sample rate/window/FFT implementation;
- exact target-curve formula;
- exact PEQ filter-count limits;
- exact device wire commands behind `xt1`;
- whether `rc_output` is a file, profile ID or firmware selector on every device;
- whether all processing is cloud-side for every hardware generation.

## Minimal analogue design for airControl

A compatible implementation should separate these modules:

1. Config/capability service.
2. Device state controller (EQ off, RC off, measurement, playback).
3. Reference audio playback.
4. Microphone recorder with WAV/PCM output.
5. Validation (SNR, level, duration, clipping).
6. Channel/session manager (mono, L/R, optional center/sub).
7. Local or server-side frequency analysis.
8. Target-curve and smoothing stage.
9. PEQ solver producing `freq/gain/Q/mode`.
10. Profile serializer using `EQBand` JSON.
11. Device apply layer with mono/stereo/multi payloads.
12. Verification and rollback.

For airControl, do not treat this as a replacement for Eq10HP raw values. WiiM’s correction result is a parametric-EQ profile applied through a separate RC path.

## Additional static findings — signal delivery, native DSP, and synchronization (2026-10-28)

This addendum qualifies the broad cloud-processing wording above: the APK contains substantial local validation, alignment, RTA and PEQ-related DSP as well as a cloud upload/result stage. The exact partition of final coefficient optimization remains unresolved.

### Stimulus generation and playback

`DataController.P0(MeasureType, DeviceItem, callback)` selects remote `pink_file`/sweep paths from `CloudRCConfig`. `R0` concatenates the configured result domain and path; `T0` formats that URL with numeric substitutions 16 and 48, creates an `LPPlayItem.trackUrl`, sets media source `AudioAnalysis`, and submits it through the Linkplay SDK playback path. Evidence: `ev_4e1dd8288f7c2479000dfaf07a72858315b28d238855dad54855be81812b3660`, `ev_e431a8a90662e9b5f8a904408ea01a953418475ffc169f81d0783dd2fe3e66d2`, `ev_918dad2ed5a1c3cc974d5ddf04f89ae7348363df6f218ae9bba714de9ff2b889`.

**Verified:** configured remote media URLs are handed to the device as playback items; duration comes from cloud config, not one universal hard-coded sweep. The nested base APK contains Room Correction WAV resources under `res/raw`; they are not direct top-level entries of the outer XAPK ZIP.

**Unknown:** waveform samples/type, media rate/bit depth, amplitude/fades, sync-marker layout, generation timing, and LAN fetch protocol. The URL substitutions 16/48 have no proven semantics. This is evidence of configured file-URL playback, not handset real-time synthesis.

### Capture, effects, and buffering

`RecordConfig.<init>` defaults to WAV, Android mono input config `0x10`, PCM16 encoding `2`, 48 kHz (`0xbb80`), duration 6500 ms (`0x1964`). `FragRCStepMeasure.m1` overrides duration with cloud-config values, adds a wait margin, and assigns channel/position filenames. Evidence: `ev_91fb6b7cc095b98f148034f1ca7336750d0b2063056dfb80e6c77b5b620c2af5`, `ev_ed54e40ace82513b73ae60aa3034f8d0875bb72c5ad0badbc55ad19d1235258c`.

`AudioRecorder.t()` checks `RECORD_AUDIO`, creates Android `AudioRecord`, and applies a selected input using `setPreferredDevice` (`ev_aa5a562a45a610589e37e43a5836c09a372af4d2e212b3bd76d05661e1cc93e0`). `AudioRecorder.z(sessionId)` attempts to disable AEC, AGC and NoiseSuppressor and reports any still-enabled effect (`ev_dc8ae715d0c7b2e20346d8a42b4489d7bbafdd8c8c8bca8dc1561ba4fd1f8d25`); this cannot guarantee vendor audio-HAL compliance.

`OboeRecorderImpl.b` calls JNI `nativeStartRecording(path, rate, config, nativeWriteToFile)` (`ev_b248146ac94da5f8a9680c8f379593a8e168b660b62b48fad6f43f0681e43ed3`). Java `onOboeData(byte[])` buffers into fixed-size byte chunks; if an incoming block exceeds remaining capacity it resets its buffered index, potentially discarding queued bytes without an explicit loss counter (`ev_a7e12aeb405c10532a3579edf541d4ab28db2fe98f0a05fef499b3a64506c228`).

Native `OboeAudioRecorder::startRecording` (`libwiimundk.so + 0x1471ec`) attempts the AAudio Unprocessed preset, falls back to Oboe default, checks input direction, optionally opens a WAV writer, and logs actual final sample rate (`ev_e311395c4347d50fb43f2d571a8f25492ca2b39e2f3a74b19cf9e69da552799b`). `onAudioReady` (`0x1479c8`) writes callback bytes and/or forwards data to Java (`ev_cb6fa41bde415d1727c7e1e33fab1ab10ab105cfea4cf858b05f84342f7b6a8a`). No capture timestamp is visibly forwarded there.

### Local native alignment and DSP

`libwiimundk.so` is stripped ARM64, SHA-256 `4e3159c5ed28490e7502692071da1e6bfeb1c2c592361492464f8fd74cd510ab`. Ghidra 12.1.4 addresses are in its analysis image (base `0x100000`); pseudocode is decompiler output.

| Function | Address | Decompiled behavior / evidence |
|---|---:|---|
| `align_pink` | `0x143514` | Reads reference and recording WAVs, validates rates/length/level, detects clipping, correlation-delay failure and excessive delay. `ev_678658814adc09264c67efc5149f5b90d168f4fde98b67ed114138dc5455f45c` |
| `time_align` | `0x148a2c` | Reads sweep and recording WAVs; rejects unequal sample rates; recovers main/sub sweeps and IR windows; invokes correlation/noise, coherence and reference-end routines; emits delay in ms and checks prompt score and delay limit. Has integer `delay method` input. `ev_62a55e23795a86c7a165eb434e188ee023b4eceb331ccb864cc6bc4fc6ec240e` |
| `spl_sweep` | `0x13991c` | Requires record length from 1× to 3× reference; uses `calrir_new`, `apply_ir_windows`, `tfplots_new`. `ev_725c08af508c02c95164a05a3dd4f8b9d1dec4f062a94edfc2055fc383e5278e` |
| `process_group_sweep` | `0x139f1c` | Reads multiple WAVs, checks sample rate/length, calls `spl_sweep` and accumulates arrays. `ev_9e3bbdd280c4088c68a6d8039053aef861cf280c05b43aa3667ea299d3e08455` |
| `measured_test_rta` | `0x1348e0` | Calls `rta_method`, reads target/calibration data, validates response ranges, computes preference score and writes JSON. `ev_0e5eb97319e9f4ed5b4d949144877e9a0094b04638bd0aa1168dcd1f4ebecb52` |
| `auto_adjust_rc_freq_rta` | `0x1368c8` | Calls `rta_method` and `eq_frequency_bounds` using calibration-aware inputs. `ev_e96246d95e23319d2a1f9f5955be5b197f95fbc61778322dd04d40f2c31b356c` |
| `calculate_autoeq_biquads` | `0x152cd4` | Reads target/sweep/record data, calls `spl_sweep`, generates EQ frequencies and optimizes multiple PEQs/biquads. `ev_4b6e8ece3d3d67023060fdd20cc5dbd559b493a413b90611fbfe27fa2fe97503` |

JNI wrappers include `WiimuNDK.timeAlign` (`0x11c094`, `ev_e0749704062156d85c09bd7f70f9a6629b3d8ccbf8bc4c5595d979c14dcfc4f6`), `measuredTestRta` (`0x11baf0`, `ev_b8edb193e0d741ff1c579aca08bf29291922956447ebf7207704c7fcb9aaf1fc`), `measureTest` (`0x11a7a0`, `ev_e6b98cb0586e2a0e11e31406b56803f83a6006e81bc16927dfa5597562481e08`) and `alignPink` (`0x11ac94`, `ev_2290572be4fc4aef18cc323c04184a7fdf18a9442222245fbb04ade486700c98`). These establish local file/array DSP entry points; no evident playback timestamp is an argument.

`DataController.Y0` calls `WiimuNDK.checkVideoIsValid`, parses `DetectData`, and can request retries for SNR/length/coherence results (`ev_bd517bf1bf9b1500dde87e8c542b4b384cb0d3772df362b39e49b1c418e09881`). Record directory uploads go through `DataController.p1` (`ev_8314beecd17eb8189eb9c16847f717d486420ad2eb4177baa6d07cd37c12ce62`); the cloud task/output-archive path remains present. Thus local validation/alignment/measurement and cloud analysis both exist; final coefficient-calculation ownership remains unresolved.

### Independent clock domains: evidence-based conclusion

- **SOURCE-VERIFIED:** post-capture acoustic/data alignment uses WAV references/recordings; pink and sweep paths have correlation-based alignment and quality checks.
- **SOURCE-VERIFIED:** sweep alignment rejects unequal reference/capture sample rates. Oboe logs actual opened rate; a request for 48 kHz does not prove AudioRecord produced that rate.
- **INFERRED:** prompt/main/sub-sweep markers or coded regions exist because native code reports missing prompt tone, main/sub sweep, recovered sweep check and prompt score. Exact structure/frequencies remain unknown.
- **UNKNOWN:** continuous drift tracking, playback/capture timestamps, sample insertion/deletion, async resampling, periodic markers and end-to-end dropout accounting. The inspected aligner processes completed files; it does not establish continuous drift compensation. Absence in these functions does not prove absence elsewhere.
- **SOURCE-VERIFIED:** error categories include clipping, level, rate/length, low prompt score, delay limit and SNR/coherence. Complete retry policy is not mapped.

### airControl comparison and implementation direction

The A33 prototype in `airControl-v5.0.0/docs/A33_ROOM_CORRECTION.md` serves desktop test media, captures with browser `getUserMedia`, uses a browser analyser/local preview PEQ and requires explicit apply. Its notes identify missing mic calibration, acoustic alignment/deconvolution and multi-position averaging. This differs from WiiM Home and is not end-to-end hardware verified.

| Area | WiiM Home | airControl prototype | Recommendation |
|---|---|---|---|
| Stimulus | Configured remote media URL passed to Linkplay SDK | Desktop test-media server | Device-specific playback adapters; confirm actual transport/readiness with a sanitized trace. |
| Capture | Android AudioRecord/Oboe WAV | Browser analyser/getUserMedia | Native CoreAudio (macOS) and WASAPI (Windows) measurement capture; preserve actual rate and monotonic sample frames. |
| Alignment | Saved-WAV correlation, sweep/IR windows and delay checks | No acoustic alignment/deconvolution | Matched-filter offset plus marker-pair drift slope; never use UI start time for sample-zero. |
| Clock domains | Offline alignment; live drift correction unproven | No independent-clock timeline model | Separate fixed latency and drift; resample only within measured limits, otherwise reject; preserve every discontinuity. |
| Quality | Clip/level/rate/length/SNR/coherence/prompt checks | Basic status/RTA | Add continuity, SNR/coherence, alignment confidence, drift and repeatability checks. |
| EQ | Native profile JSON and cloud output path | Local PEQ preview, explicit apply | Retain preview/apply, backend-specific bounds, readback and rollback. |

Desktop engine specification: (1) native CoreAudio/WASAPI capture with device selection, actual rate, monotonic frames, gap/overrun counters and lossless raw storage; (2) deterministic versioned sweep/coded-noise references with exact hash, onset and repeated markers; (3) isolated A31/A97/A98/A33 playback adapters; (4) matched-filter onset plus marker slope to estimate offset and clock ratio; (5) sweep deconvolution/IR, documented window and FFT; Welch cross/auto spectra for noise; (6) mic calibration identity/units/sign, and no absolute SPL claim without sensitivity; (7) quality gate for gaps, clipping, SNR/coherence, alignment/drift and repeatability; (8) explicit preview/apply, preserved prior EQ, device readback and rollback.

### Proposed validation plan (not run)

- Synthetic incrementing samples: detect dropped/duplicated frames and verify exact saved sample count/duration.
- Inject callback stalls and PTS gaps; require explicit counters/rejection, never silent time stretching.
- Measure playback latency/jitter electrically and acoustically; separate fixed delay from room delay.
- Simulate independent clocks at ±25/50/100 ppm for 60–180 s; validate drift slope and post-correction residual.
- Test acoustic alignment with known offsets, reverb, low SNR, ambiguous peaks, clipping, truncated sweep and absent marker.
- Verify stimulus sample count, spectrum, crest factor, onset/fades, distortion and hash.
- Repeat one mic/speaker position 3–5 times and compare transfer curves.
- Test calibration sign/units/extrapolation; compare with calibrated analyzer.
- Test EQ stability, limits, serialization, readback and rollback on mocks before device writes.

All findings remain **APK-VERIFIED / NOT-HW-VERIFIED**. No device hardware status was changed. Unknowns include exact stimulus bytes, device fetch protocol, full cloud/local coefficient split, and clock-drift correction in any uninspected code path.


### Existing airControl capture symptom to use as a regression case

The user-provided AVFoundation experiment recorded 115 PTS discontinuities in 10 seconds, totaling 58,880 samples (1.227 s). Applying `aresample=async=1000:first_pts=0` produced the requested 55.000 s file but still showed deep 1 kHz signal dips of roughly 44–46 dB. These are airControl capture observations, not WiiM behavior; causation is not established and cannot be assigned to A97. Treat this as a required regression fixture: retain original PTS/frame diagnostics, expose every discontinuity, and verify that duration normalization has not masked signal loss.

### Embedded Room Correction fallback files extracted from the base APK

The base APK has these `res/raw` resources; `DataController.g0(String)` maps the app's runtime filenames to their raw resource IDs, and `DataController.P(File, String)` copies the mapped resource to the app's Room Correction cache when the file is missing. `yo9.a.p()` resolves that cache as `<app-private-base>/config/`, so runtime fallback paths are `<app-private-base>/config/room_correction_sweep-3.wav` and `<app-private-base>/config/refpink_-3dB.wav`. `DataController.i1(...)` then compares the configured/server MD5 and determines whether a remote refresh is needed. Evidence: `ev_c314b7b15426b2e9210aab504c219852eee728642910777051a7c5cdb7824f73`, `ev_66c4da75aa8643128fb12cc9ae341b8243927257767d9bad97cf74fa5707f0cd`, `ev_9947f6dea4a6987789f82e273ea031e3cd576c59f47e63dd086c64623e891968`.

| Runtime fallback name | APK resource entry | Format / duration | Extracted SHA-256 | Extracted MD5 |
|---|---|---|---|---|
| `room_correction_sweep-3.wav` | `res/raw/room_correction_sweep_3.wav` | mono PCM16, 48 kHz, 6.500 s | `61064aff234e6cc83dcf58033c1db86682eec0e9e3fa2b7834a9f0671bab1a8e` | `c625a28e75ae16159ca22a6b353f33a6` |
| `refpink_-3dB.wav` | `res/raw/refpink__3db.wav` | mono PCM16, 48 kHz, 42.960 s | `abb6769e99d7156d5472c4899015a1a200e6cbc3f1e682bcf700a95024e6992d` | `bcedfd477a7f7512c0da1fc69e388399` |
| auxiliary `mmpsilence.wav` | `res/raw/mmpsilence.wav` | mono PCM16, 8 kHz, 0.18575 s | `2af9f700506e672316c91ed21c8d36bc5375af88e8d35303dd045e199464b5ea` | `4946e7f71c31b1d194f6604914703d15` |

Byte-extracted copies and a ZIP bundle are available locally under `/Users/lab/AI/WiiM-RC-test-assets/` and `/Users/lab/AI/WiiM-RC-test-assets.zip` (ZIP SHA-256 `bb5b096885eb5da40be06dcba0471f0d9526162487a534c4a161c9b4d67ad1ca`). The names of the two measurement WAVs are normalized to the app's runtime fallback names; resource bytes are unchanged. The pink WAV is approximately 42.96 s, while its model/config can report a different active pink duration; do not assume the entire file is always played.

The app's current remote paths and current live cloud versions are **not** embedded as fixed URLs: `CloudRCConfig.Result` supplies `domain`, file paths, and MD5 values at runtime. Without that response, only the embedded fallback copies can be identified and extracted; no claim is made that they are byte-identical to current CDN files.
