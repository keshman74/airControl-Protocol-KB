# Volume command view

- `CMD-A31-VOLUME` [A31] `setPlayerCmd:vol:<0..100>` — **CONFIRMED**
- `QRY-A31-MCU-VOLUME` [A31] `MCU+VOL+GET&` — **CAPTURED**
- `QRY-A31-MCU-VOLUME-NATIVE` [A31] `MCU+VOL+GET` — **IMPLEMENTED / RESPONSE-KNOWN**
- `CMD-A31-MCU-VOLUME` [A31] `MCU+VOL+<NNN>` — **IMPLEMENTED/NEEDS-HW-EVIDENCE**
- `CMD-A31-HTTP-VOL-UP-REL` `setPlayerCmd:vol++`; `CMD-A31-HTTP-VOL-DOWN-REL` `setPlayerCmd:vol--` — **IMPLEMENTED / OBSERVED-IN-LOG**
- `CMD-LP-VOL-UP`, `CMD-LP-VOL-DOWN`, `CMD-LP-MAX-VOL` — **DOCUMENTED/IMPLEMENTED**
- `CMD-A33-VOLUME` [A33 TCP :1234] — **CONFIRMED**
- `CMD-ACS2-VOLUME`, `CMD-ACS2-VOL-UP`, `CMD-ACS2-VOL-DOWN`, `CMD-ACS2-MAX-VOLUME` — **DOCUMENTED**
- `QRY-UPNP-RC-GET-VOLUME` — **SCPD-DOCUMENTED / HARDWARE-ENDPOINT-VERIFIED**
- `CMD-UPNP-RC-SET-VOLUME` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**

## A97 RenderingControl execution evidence — 2026-10-20
- QRY-UPNP-RC-GET-VOLUME [tested A97 HTTP49152] — **HARDWARE-VERIFIED**, CurrentVolume94,12–23ms from Mac.
- CMD-UPNP-RC-SET-VOLUME [same A97] — **HARDWARE-VERIFIED SAME-LEVEL ACCEPTANCE/READBACK**, DesiredVolume94,15ms; follow-up94 in14ms. Changed-level output and other hardware remain unverified.
- KNOB0.8.23 implements this volume path with HTTPS fallback; full CI/build passed; KNOB hardware validation pending.
Canonical request, timing and limits: [A97-VOLUME.md](../../protocols/upnp/A97-VOLUME.md).
