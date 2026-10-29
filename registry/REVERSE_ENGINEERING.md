# Reverse Engineering Registry

## REV-WIIM-HOME-001
Application: WiiM Home APK
Source tree: `/Users/lab/AI/WiiM-Home-decompiled/sources/`
Evidence: decompiled source extracts + hardware tests recorded in CHAT-AUDIT-02.

Key recovered areas:
- RenderingControl / StreamServicesCapability
- PlayQueue service and actions
- Qobuz capability/version negotiation
- Qobuz catalog/context URL construction
- Qobuz playback object pipeline
- SMB capability gating
- AVTransport callbacks
- classic Linkplay HTTP builders

Important classes/functions:
`np8`, `n42`, `wq7`, `kq`, `op8`, `i27`, `ec9`,
`QobuzPlayItem`, `LPPlayItem`, `LPPlayMusicList`,
`LPMSPlayData`, `LPPlayMediaData`.

Do not infer that capability name `AudioCast` means an AudioCast APK was decompiled.

## REV-4STREAM-001
4STREAM Android `com.wifiaudio.Stream` 3.1.20.230912 / 2023091217. APK SHA-256 `08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b`.
Status: **APK-VERIFIED / NOT-HW-VERIFIED**. [Canonical command/routing report](../protocols/linkplay-http-https/4STREAM-2026-10-24.md); [provenance](../evidence/reverse-engineering/4STREAM-2026-10-24.md); [machine observations](../evidence/reverse-engineering/4STREAM-2026-10-24-builders.csv).
Recovered broad family classification, explicit R328 gates, security/4443 selection, classic/MRM4 grouping, Single-vs-Master UPnP arguments, exact static-IP and timer formats, EQ and MCU frame. No device commands were executed.

## REV-IAUDIOCLOUD-001 — 2026-10-25

iAudioCloud 2.0.260728 (43), A33 native control audit: 141 declared opcode arrays, 109 bounded sender observations; no hardware actions. [Canonical report](../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md), [provenance](../evidence/reverse-engineering/IAUDIOCLOUD-2026-10-25.md), [records643–650](records/643-650.csv). Existing CMD-A33-SEEK, CMD-A33-PRESET-GET, CMD-A33-PRESET-ACTIVE and DISC-A33-001 are extended, not duplicated.


## REV-4STREAM-AIRPLAY-ART-001 — 2026-10-25

Focused 4STREAM 3.1.20.230912 metadata/artwork audit from UPnP AVTransport LastChange, GetInfoEx and GetMediaInfo through DIDL-Lite parsing to the playback ImageView. Status: **APK-VERIFIED / NOT-HW-VERIFIED**.

[Canonical report](../protocols/linkplay-http-https/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md), [provenance](../evidence/reverse-engineering/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md), [machine evidence](../evidence/reverse-engineering/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.json), [records 651–656](records/651-656.csv).

Key result: a relative AirPlay albumArtURI is not resolved by this APK; only a full http/https URI reaches the artwork GET. No AirplayArtWorkData.jpeg fallback or AirPlay stale-source guard was found. Existing hardware-confirmed facts are preserved.


## REV-WIIM-ROOMCORR-DSP-001 — 2026-10-29

WiiM Home 3.6.10.260924 native Room Correction DSP analysis of ARM64 `libwiimundk.so`. Status **APK-VERIFIED / NOT-HW-VERIFIED**. Entry points `time_align` (`0x148a2c`), `calrir_new` (`0x127a0c`), `apply_ir_windows` (`0x129a50`), `spl_sweep` (`0x13991c`); separately traced `tfplots_new` (`0x127e2c`) and RTA path `rta_method` (`0x13392c`) / `measured_test_rta` (`0x1348e0`).

[Report](../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-STATIC-3.6.10-2026-10-29.md) · [call graph](../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-CALLGRAPH-2026-10-29.md) · [argument/error table](../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-ARGUMENTS-ERRORS-2026-10-29.md) · [REA Evidence manifest](../evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-REA-EVIDENCE-MANIFEST-2026-10-29.md).

The RTA route is separate from `spl_sweep`; no sample-rate drift correction is demonstrated in the analyzed functions. Hardware facts remain untouched.
