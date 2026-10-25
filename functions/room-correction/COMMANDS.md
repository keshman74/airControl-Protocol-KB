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
