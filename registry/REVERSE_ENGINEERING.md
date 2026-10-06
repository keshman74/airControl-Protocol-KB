# Reverse Engineering Registry

## REV-WIIM-HOME-001

Application: WiiM Home APK  
Source tree used during research: `/Users/lab/AI/WiiM-Home-decompiled/sources/`

Recovered areas:
- RenderingControl / StreamServicesCapability
- PlayQueue SCPD and callbacks
- Qobuz capability/version negotiation
- Qobuz catalog/context URL construction
- Qobuz playback object pipeline
- SMB capability gating
- AVTransport callbacks
- classic Linkplay HTTP builders

Important classes: `np8`, `n42`, `wq7`, `kq`, `op8`, `i27`, `ec9`, `QobuzPlayItem`, `LPPlayItem`, `LPPlayMusicList`, `LPMSPlayData`, `LPPlayMediaData`.

Capability name `AudioCast` is not evidence that an AudioCast controller APK was decompiled.
