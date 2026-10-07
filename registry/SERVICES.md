# Online Services Registry

| ID | Service | Device | Evidence | Control |
|---|---|---|---|---|
| SVC-TUNEIN | TuneIn | A33 | service + metadata/context captured on TCP :23040 | PARTIAL |
| SVC-QOBUZ | Qobuz | A33 | service + metadata/context/queue captured on TCP :23040 | PARTIAL |
| SVC-SPOTIFY | Spotify Connect | A33 | `_spotify-connect._tcp.local` advertised by mDNS | API UNKNOWN |
| SVC-TIDAL | TIDAL | A33/ACS2 | official `getMetaInfo` example reports `PlaySource: tidal`; Tidal Connect also observed in saved ecosystem capture | DOCUMENTED / CAPTURED-ECOSYSTEM; A33 hardware control API not yet confirmed |
| SVC-DEEZER | Deezer | A33 | insufficient evidence | UNKNOWN |
| SVC-VTUNER | vTuner | A33 | application code anticipates it; capture required | PARTIAL |
| SVC-YOUTUBE-MUSIC | YouTube Music | A33 | no confirmed native evidence yet | UNKNOWN |

## Sensitive fields
Qobuz captures may contain `Token` / `user_auth_token`. Store field names only; redact values.

## CHAT-AUDIT-02 hardware capability additions
Runtime `StreamServicesCapability` is authoritative for service exposure.
Hardware-captured matrices for A31/A97/A98 are in `STREAM_CAPABILITIES.md`.
Notably, A98 advertised SpotifyConnect, TidalConnect, QobuzConnect, Samba,
YouTubeMusic and AudioCast while A31/A97 exposed smaller service sets.
These are capability responses, not proof of a common control API for each service.
