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
