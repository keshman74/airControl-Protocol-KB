# Compatibility Matrix

| Capability | A31 | A97 | A98 | A33 |
|---|---|---|---|---|
| Basic player control | CONFIRMED | PARTIAL | PARTIAL | CONFIRMED |
| Volume / mute | CONFIRMED | PARTIAL | PARTIAL | CONFIRMED |
| EQ | MCU :8899 confirmed/implemented | UNKNOWN | separate HTTP EQ implemented; verify per command | UNKNOWN |
| USB | CONFIRMED | no USB on test hardware | no USB on test hardware | DOCUMENTED/needs hardware test |
| Native Multiroom | CONFIRMED | CONFIRMED | family support; verify device-specific | ACS2 separate architecture |
| Online TuneIn | observed in ecosystem | — | — | CONFIRMED/CAPTURED |
| Online Qobuz | artwork/playback evidence | — | artwork confirmed | CONFIRMED/CAPTURED |
| Spotify Connect | — | — | — | ADVERTISED |
| Discovery | Linkplay discovery/status | Linkplay | Linkplay | UDP + SSDP + mDNS captured |

## 4STREAM static scope — 2026-10-24
REV-4STREAM-001 adds client-code evidence, not new confirmed cells. A31 is explicitly legacy; R328 has explicit gates; isA98 covers every non-A28/non-A31 hardware string. Feature flags, project identity, security and wmrm_version affect routing. [Conditional matrix and exact formats](../protocols/linkplay-http-https/4STREAM-2026-10-24.md). Existing hardware negatives are preserved.
