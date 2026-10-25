# Metadata command view

- `QRY-A31-METAINFO` [A31] `getMetaInfo` — **REJECTED** on tested A31 firmware.
- `QRY-ACS2-META` [ACS2] `getMetaInfo` — **DOCUMENTED**.
- `EVT-A31-PLAYBACK` `AXX+SNG+INF{...}&` — **CAPTURED**.
- `EVT-A33-TUNEIN-CONTEXT`, `EVT-A33-QOBUZ-CONTEXT` — **CAPTURED**.
- `QRY-UPNP-AVT-MEDIAINFO`, `QRY-UPNP-AVT-INFOEX` — **APK-VERIFIED**.
- `PROTO-UPNP-QUEUECONTEXT-XML`, `PROTO-WIIM-PLAYLIST-XML` preserve metadata/service context — **APK-VERIFIED / EXACT-BUILDER-RECOVERED**.


## 4STREAM AirPlay / Network / DLNA metadata — 2026-10-25

- LastChange CurrentTrackMetaData, GetInfoEx TrackMetaData and GetMediaInfo CurrentURIMetaData converge on DeviceInfoExt.setDlnaTrackMetaData.
- Generic DIDL-Lite parsing extracts upnp:albumArtURI without resolving a relative URI.
- AirPlay is identified by PlayMedium AIRPLAY and uses a direct OkHttp artwork loader; ordinary generic sources use Glide.
- LastChange can update immediately; otherwise GetInfoEx is scheduled every 5000 ms. The 1000 ms timer advances local progress only.
- No application caller of GetPositionInfo was found in the complete direct-reference scan.
- No explicit AirPlay-over-radio priority or stale-metadata guard was found.

Status: **APK-VERIFIED / NOT-HW-VERIFIED**. [Detailed report](../../protocols/linkplay-http-https/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md).
