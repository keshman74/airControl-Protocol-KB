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
