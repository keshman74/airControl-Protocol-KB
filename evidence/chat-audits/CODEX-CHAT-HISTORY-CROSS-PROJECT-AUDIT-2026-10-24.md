# Codex chat-history cross-project audit — 2026-10-24

Source artifact: user-supplied `codex-chat-history.zip`, exported 2026-10-22. Scope: overlapping research chats around A31, A33, A97 and A98 across airControl, airKNOB, KNX Gateway, airALARM and Integration.

## Evidence policy
Chat statements are provenance, not automatically CONFIRMED. Hardware outputs pasted by the user can promote a finding when the request/response and device context are explicit. Assistant proposals and implementation claims without a returned device result remain IMPLEMENTED/EXPERIMENTAL as appropriate.

## Recovered A33 EQ hardware evidence
From `airControl/2026-09-11_Приложение-управления-устройствами_6aa467fe.md`:

- `getEqType` returned `EQ type: 0111`.
- `getEqInfo:1` returned `{"Bass":"-2","Treble":"3"}`.
- `getEqInfo:2` returned a 10-band Flat graphic profile.
- `getEqInfo:3` returned `AutoRoomEQ` with ten PEQ entries containing `Index/Filter/Freq/Q/Gain`.
- `eqEnable:0001` and `eqEnable:0010` returned `OK` and were read back in `getStatusEx`.
- `eqEnable:0100` was observed in `getStatusEx` for Parametric EQ mode.
- Writing `setParameterEq` with `Custom:""` returned `Custom error`.
- Writing the same PEQ as a named profile with `Custom:"1"` returned `OK`; `getEqInfo:3` read back the new name `airCloudPEQ` and changed first band `305 Hz / Q 2.8 / Gain -1.7`.
- Important firmware behavior: although `Custom:"1"` was sent, readback returned `Custom:"0"`; therefore `Custom` is not a reliable user-profile flag on the tested A33 firmware.

These findings correct the prior KB gap where A33 PEQ was present mainly as DOCUMENTED ACS2 material.

## Recovered A33 Room EQ / Auto EQ implementation history
The same chat contains the original airCloudCTRL Room EQ development. This is an application-side algorithm, not a native A33 room-correction protocol:

- test signals: Pink Noise, White Noise, Sweep 20 Hz–20 kHz;
- microphone capture on the computer through Web Audio;
- live RTA and 5-second measurement;
- early Auto EQ generated unsafe repeated -9 dB bass cuts and was explicitly rejected as inaccurate;
- v0.3.0 changed the application algorithm to approximately 1/6-octave smoothing, level normalization, selection of significant regions, preference for cutting peaks, avoiding aggressive boost of deep nulls, minimum spacing between filters, max boost about +3 dB, max cut about -9 dB, and a Predicted-after-EQ curve;
- v0.3.1 exposed Raw / Smoothed / Normalized views and removed the earlier display clipping problem;
- the proposed target curves included Flat, House Curve and Custom;
- the calculated result was loaded into the device PEQ; A33 device-side application used `setParameterEq`.

Important correction: the archive does **not** preserve a formal DSP specification or exact source-level formula for the correction optimizer. The chat preserves design rules and observed behavior, not enough to claim a mathematically canonical algorithm. Before reusing it in a new release, inspect the actual source implementation.

## Recovered A98 EQ/PEQ hardware evidence
From the same origin chat:

- A98 10-band graphic EQ was reported working in airCloudCTRL v3.0.7.9 after using WiiM `EQGetBand/EQSetBand`.
- A98 EqNp/LV2 readback exposed ten active PEQ bands A–J with `mode/freq/q/gain`; K/L were returned disabled in the observed response.
- airCloudCTRL v3.0.7.11 used `EQGetLV2SourceBandEx / EQGetLV2BandEx` for reading and `EQSetLV2SourceBand` for per-source writing.
- Hardware tester confirmed that changing one PEQ band in airCloudCTRL also changed the value on the A98 device. This promotes the A98 EqNp read/write path beyond source-documentation for the tested device/firmware context.
- v3.0.7.14 reused the same application-side Room EQ measurement/calculation UI for A98 and loaded the result into A98 Parametric EQ. This is distinct from WiiM's native `RoomCorr*` API.

## WiiM native Room Correction distinction
The WiiM OpenAPI v1.2.0 import documents `RoomCorrGet`, `RoomCorrGetMode`, `RoomCorrSet`, `RoomCorrSetLR`, `RoomCorrSetMode`, and `setRoomCorrection`. The exported chats do not contain hardware execution of those native `RoomCorr*` commands. Do not conflate:
1. airControl's computer-side measurement/Auto-EQ algorithm feeding PEQ; and
2. WiiM native Room Correction API/state.

## A97 findings and limitation
The archive contains substantial A97 transport, discovery, PlayQueue/preset and HTTPS evidence. It also contains a hardware-discovered A97 zone using HTTPS :443 and A97 PlayQueue preset work. However, this audit did **not** find an explicit A97 hardware EQ/PEQ write/readback sequence comparable to the A33 and A98 evidence above. Therefore A97 EQ/Room Correction must remain isolated until direct hardware evidence is recovered or newly tested.

## Cross-project rule
A31, A97 and A98 are related Linkplay/WiiM families but their capabilities and transport details must be gated per device/firmware. A33 is a separate ACS2/native family. Shared UI and DSP math are allowed; protocol adapters and evidence status must remain separate.

## Source chat identities recovered from export
- CHAT-AIRCONTROL-ORIGIN: `airControl/2026-09-11_Приложение-управления-устройствами_6aa467fe.md`
- CHAT-AIRCONTROL-150926: `airControl/2026-09-15_Продолжение-разработки-airControl_6aa97e9d.md`
- CHAT-KNX-GATEWAY-160926: `KNX-Gateway/2026-09-16_Прошивка-KNX-HTTP-Gateway_6aab1694.md`
- CHAT-AIRKNOB-260926: `airKNOB/2026-09-26_KNOB-Управление-громкостью-ESP32_6ab8586b.md`
- CHAT-AIRCONTROL-300926: `airControl/2026-09-30_Продолжение-разработки-airControl-300926_6abd7450.md`
- CHAT-AIRCONTROL-041026: `airControl/2026-10-02_Продолжение-разработки-airControl-041026_6abef5ff.md`
- CHAT-KB-MERGE-061026: `airControl/2026-10-06_Git-Hub-Объединение-исследований-протокола_6ac55469.md`
- CHAT-A33-PRESETS: `airControl/2026-10-07_Команды-пресетов-A33_6ac62f6b.md`
- CHAT-AIRCONTROL-121026: `airControl/2026-10-12_Продолжение-разработки-airControl--121026_6acd6bbe.md`
- CHAT-A31-FIRMWARE-141026: `airControl/2026-10-14_Разбор-прошивки-A31_6acfd281.md`

The archive also includes Integration and airALARM conversations that cross-reference these device families; they are provenance sources but are not promoted to command truth unless they contain direct evidence.
