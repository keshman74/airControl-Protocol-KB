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
