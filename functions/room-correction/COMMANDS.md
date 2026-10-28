# Room correction


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-ROOM-CORR-GET` — `RoomCorrGet` — Get the current room correction settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-ROOM-CORR-GET-MODE` — `RoomCorrGetMode` — Get the current room correction mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET` — `RoomCorrSet:{str}` — Set the room correction settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET-LR` — `RoomCorrSetLR:{str}` — Set the room correction settings for left and right channels — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET-MODE` — `RoomCorrSetMode:{"Mode":"{str}"}` — Set the room correction mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ROOM-CORRECTION` — `setRoomCorrection:{"RC_Version":"{str}","Time":"{time}"}` — Set the room correction settings with version and time parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**


## airControl application-side Room EQ — recovered development history

**Status:** IMPLEMENTED/HARDWARE-OBSERVED as an airControl measurement-to-PEQ workflow; exact DSP source formula requires source-code recovery.

The original airControl development chat records a Room EQ implementation that is separate from WiiM's native `RoomCorr*` API:

`test signal -> speakers/room -> computer microphone -> RTA/measurement -> smoothing/normalization -> target comparison -> proposed PEQ -> device PEQ write`.

Recovered behavior:
- Pink Noise, White Noise and 20 Hz–20 kHz sweep test signals.
- Computer-side microphone capture; live RTA and a 5-second capture mode.
- Target concepts: Flat, House Curve and Custom.
- An early correction algorithm was rejected after it spent many filters at the `-9 dB` limit in the bass region.
- The v0.3.0 revision introduced approximately 1/6-octave smoothing, overall-level normalization, significant-region selection, spacing between filters, preference for cutting peaks, conservative handling of deep nulls, approximately `+3 dB` maximum boost and `-9 dB` maximum cut, plus a Predicted-after-EQ curve.
- v0.3.1 exposed Raw / Smoothed / Normalized views and removed the earlier graph clipping behavior.
- A33 output used its hardware-confirmed 10-band `setParameterEq` path.
- The same measurement/correction module was later exposed for A98 and its result could be loaded into the A98 EqNp/LV2 PEQ path.

**Important:** the chat export preserves the design rules and test observations, but not a complete canonical mathematical specification of the optimizer. Do not claim a Dirac/REW algorithm or exact formula from this evidence. Recover and audit the actual airControl source before porting or tuning the correction engine.

## Native WiiM Room Correction vs airControl Room EQ

Keep these mechanisms distinct:
- WiiM native: `RoomCorrGet/Set/SetLR/GetMode/SetMode/setRoomCorrection` — currently **SOURCE-DOCUMENTED / NOT-HW-VERIFIED** in this KB.
- airControl Room EQ: computer-side measurement/calculation feeding device PEQ — application implementation with hardware-observed A33/A98 output paths.

No A97 native RoomCorr or application Room EQ hardware test was found in the supplied Codex history during the 2026-10-24 audit.

Provenance: `evidence/chat-audits/CODEX-CHAT-HISTORY-CROSS-PROJECT-AUDIT-2026-10-24.md`.

## iAudioCloud APK evidence — 2026-10-25

Native RoomFit 04 40 requests sound with zero payload; 04 41 sends EqBand filter objects. Frequency/gain/Q are formatted strings; no hardware support, units or safe range is newly established.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).


## WiiM Home APK static implementation findings — 2026-10-28

**Status: APK-VERIFIED / NOT-HW-VERIFIED.** This section describes the Android app's measurement workflow, not device support for the documented `RoomCorr*` commands above.

- The app reads test-media paths and durations from `CloudRCConfig`, creates a Linkplay SDK media item with `AudioAnalysis`, and plays the configured URL on the device.
- The phone captures via Android `AudioRecord` or Oboe. Default recording config is mono PCM16 WAV at 48 kHz, 6500 ms; the measured sweep duration is config-driven.
- Local `libwiimundk.so` includes post-capture pink/sweep alignment, sample-rate validation, RTA and PEQ/biquad routines. The inspected sweep aligner rejects mismatched WAV rates. Continuous drift correction is not established.
- The app also uploads recordings and downloads a cloud task result archive. The local/cloud boundary for final EQ coefficients remains unknown.
- See the [full static report](../../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-3.6.10-2026-10-28.md) for class/method/address evidence, clock-domain limits, airControl design comparison, and proposed validation plan.

No hardware-confirmed command or device capability is changed by these APK findings.


### Embedded WiiM measurement resources

The base APK bundles fallback test WAVs: `room_correction_sweep-3.wav` (mono PCM16/48 kHz/6.5 s) and `refpink_-3dB.wav` (mono PCM16/48 kHz/42.96 s). `DataController.g0/P/i1` maps/copies these resources and checks the configured MD5 for remote refresh. These are APK fallback assets, not proof of current CDN versions. Exact source hashes and extracted files are listed in the [static report](../../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-3.6.10-2026-10-28.md#embedded-room-correction-fallback-files-extracted-from-the-base-apk). Status: **APK-VERIFIED / NOT-HW-VERIFIED**.
