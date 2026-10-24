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
- CMD-UPNP-RC-SET-VOLUME [same A97] — **HARDWARE-VERIFIED SAME-LEVEL ACCEPTANCE/READBACK**, DesiredVolume94,15ms; follow-up94 in14ms. The terminal test itself did not change the level; subsequent KNOB0.8.23 volume control and noticeable speed improvement were confirmed by the user on2026-10-21. Other hardware remains unverified.
- KNOB0.8.23 implements this volume path with HTTPS fallback; full CI/build passed; KNOB A97 volume control and qualitative speed improvement user/hardware-confirmed on2026-10-21.
Canonical request, timing and limits: [A97-VOLUME.md](../../protocols/upnp/A97-VOLUME.md).

## Reuse decision — 2026-10-21
Use the hardware-confirmed A97 RenderingControl volume design in future airControl desktop/mobile and other project implementations, with paced HTTPS fallback and latest-target coalescing. These other integrations are planned, not completed. See [cross-project rule](../../integration/A97-VOLUME-REUSE.md).

## 4STREAM APK evidence — 2026-10-24
**APK-VERIFIED / NOT-HW-VERIFIED**. RULE-4STREAM-RC-CHANNELS; setMaxVolume and setVolumeControl are separate HTTP configuration builders. Preserve hardware-tested A97 volume behavior.
[Exact formats and source selectors](../../protocols/linkplay-http-https/4STREAM-2026-10-24.md#upnp-recovered-argument-differences).
