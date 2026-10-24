# AirPlay artwork missing in KNOB and airControl — 2026-10-24

Status: USER-REPORTED OPEN ISSUE; selected player subsequently identified as A31 at192.168.0.35, KNOB0.8.23; player firmware and current AirPlay source app not supplied in this capture.

User reports AirPlay artwork is visible in the native player application, while KNOB and airControl display only text metadata. This establishes that the native app can display an image for this session; it does not establish where that app obtains it or a universal AirPlay/codec limitation.

Source inspection: airKNOB main at2acb61ba2bfdfdc60f0f1fe823edf087c737eb98 (0.8.23) uses getMetaInfo for non-A31 profiles, then AVTransport GetPositionInfo artwork fallback. SOAP extraction checks TrackMetaData,CurrentTrackMetaData,AVTransportURIMetaData. The inspected airControl main Electron resolver likewise extracts albumArtURI via GetPositionInfo and accepts HTTP(S) artwork. The installed desktop version was not identified; these source observations alone do not establish its exact failing branch.

## External candidate, not confirmed on user's devices
A directly published WiiM Amp/Linkplay5.2.823846 debug log contains getMetaInfo artwork URL:
https://<player>/data/AirplayArtWorkData.jpeg?cache=<track-identity>
Source: https://github.com/mjcumming/wiim/issues/260 (external user's log; not an official cross-model API guarantee).
The core path /data/AirplayArtWorkData.jpeg is a candidate to test on compatible Linkplay devices using their selected HTTP(S) origin. Do not apply it to A33 without native evidence, or silently downgrade A97/A98 HTTPS.

## Next diagnostic and implementation requirements
Read the KNOB selected-zone health/profile, current player state/mode, getMetaInfo artwork fields and test the specific player-local AirPlay JPEG candidate. Inspect actual image Content-Type, bytes/signature and accessibility before integration.
A static AirPlay artwork URL may change content between tracks: if verified, any implementation must key/invalidate its cache by playback identity rather than URL alone. Do not keep a previous track's cover after identity changes or add image downloads to every volume event.
Fix/adaptation must be considered in both KNOB and airControl (and shared future mobile adapter). No firmware/app fix or successful retrieval on user's AirPlay device is claimed by this note.

## A31 terminal readback — 2026-10-24
KNOB0.8.23 selected A31,http://192.168.0.35:80.
getPlayerStatus returned mode1,statusplay, with hex title/artist/album. Decoded title Gas; artist Bicep, Lauren Duffus, soarr; album Gas / Ultra / Equarium.
getMetaInfo produced JSONDecodeError at the first character. The diagnostic did not preserve its raw response/status, so this capture alone does not identify the actual non-JSON response.
GET http://192.168.0.35:80/data/AirplayArtWorkData.jpeg returned HTTP404 Site or Page Not Found.
Thus the externally observed WiiM file path is not available at the tested A31 origin/path in this session. Do not add it as a presumed A31 fix or infer all AirPlay artwork is absent from the device.

Native application cover visibility remains user-confirmed, while KNOB and airControl show text only. The native app's image source is still unproven (player-local, event metadata, application cache or online lookup are possibilities).
Next bounded read-only test: inspect the actual AVTransport SCPD inputs and read advertised GetPositionInfo/GetMediaInfo/GetInfoEx actions, preserving returned metadata/URLs. Existing KNOB code uses GetPositionInfo only, so another advertised metadata response could identify a missing resolver path. No fix is claimed yet.

## A98 terminal result and scope correction — 2026-10-24
User tested A98 at192.168.0.21 with AirPlay:
- getPlayerStatus mode1,statusplay,Title Ultra,artist Bicep/Eartheater/Saskia,album Gas / Ultra / Equarium.
- getMetaInfo returns metaData.albumArtURI=https://192.168.0.21/data/AirplayArtWorkData.jpeg.
- GET that URL: HTTP200, Content-Type absent, Content-Length180224, first bytes JPEG true, PNG false. Only a32-byte prefix was read; no full-file dimensions/decoder inspection was performed.
- User then clarified: **A98 AirPlay artwork DOES display on KNOB0.8.23, but DOES NOT display in airControl**. Promote A98 KNOB AirPlay artwork to USER/HARDWARE-VERIFIED WORKING in this session. Do not continue treating it as a missing-cover KNOB regression.
- The separate A31 AirPlay missing-artwork issue and404 path result remain unresolved.

Source review: KNOB0.8.23 decodes image format using bytes, so absent Content-Type is not an established rejection cause. The size180224 is below its350KiB compressed-image limit; dimensions were not supplied.
The inspected airControl main4.4.54 and feature/v5.0.x-active-presets-a98 version5.0.0 share fetchArtworkDataUrl. Its HTTPS image request lacks the rejectUnauthorized:false setting used by local player control requests. This is a concrete source inconsistency and plausible cause for player-local self-signed HTTPS artwork failure; no installed-app TLS error trace was supplied. MIME fallback already defaults to image/jpeg, so absence of Content-Type alone is not established as its cause either.
Installed desktop version/project path still needs identification: GitHub main and feature package versions do not establish which local desktop source the user runs. Scope a fix to the selected player's local HTTPS artwork certificate handling, keep public CDN certificate checks and per-track cache identity, and validate against the actual desktop version before claiming the issue fixed.
