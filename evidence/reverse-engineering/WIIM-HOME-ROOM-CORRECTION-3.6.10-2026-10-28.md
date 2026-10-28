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
