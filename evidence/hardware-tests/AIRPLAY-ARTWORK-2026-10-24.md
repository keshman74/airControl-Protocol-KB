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

## airControl5.0.0 targeted fix — 2026-10-24
User identified the active local project as /Users/lab/AI/airControl/airControl-v5.0.0.
Implemented AirPlayArtworkTLS-v1 in airControl branch feature/v5.0.x-active-presets-a98:
https://github.com/keshman74/airControl/commit/2fceb06544620192443f1458248dc3bc2fb3f094
Package version remains5.0.0; this patch identifier distinguishes the fix without replacing the complete local application.

The Electron artwork resolver is extracted to electron/artwork-fetch.cjs. Four metadata/UPnP artwork call sites pass selected target.ip through IPC. Certificate verification is relaxed only for HTTPS /data/AirplayArtWorkData.jpeg on the exact selected player's RFC1918 IPv4. Public CDN/other-host/other-path requests retain normal verification. The selected-IP context is retained across redirects, and the rule is re-evaluated at every hop. No global TLS disable is introduced. Existing image/jpeg fallback already handles this confirmed missing Content-Type case.

Actual local HTTPS tests use a self-signed certificate: baseline resolver request fails, selected-player patched request succeeds, exact image bytes/data URL and missing Content-Type fallback verified. Other selected-IP mismatch, public/other-path certificate rejection, same-player and external redirects, timeout and normal HTTP paths tested.
Installer was applied to a canonical5.0.0 fixture; backup and repeat-install detection verified; wrong-version refusal leaves files unchanged. node --check passed patched Electron main. Full Vite/Electron GUI build was not run; an attempted JSX parser check was unavailable in this environment. Four call-site changes only add the selected-IP argument; no JSX structure was changed.
The ZIP patch includes the module, guarded standard-library Python installer, test and README; installer modifies only the verified old fetcher and four call sites, preserving other local edits and saving backups.

Status: IMPLEMENTED / NODE HTTPS-TESTED / INSTALLER-TESTED. Mac AirPlay hardware verification in airControl after applying the patch remains pending. A98 KNOB is already hardware-confirmed working; separate A31 image-source issue remains unresolved.


## airControl5.0.0 AirPlay cover stability follow-up — 2026-10-24
After the AirPlayArtworkTLS-v1 patch, the user reported the cover flashed briefly but did not remain visible in airControl. This symptom suggests the first image fetch/render may succeed and a later refresh may substitute a failed raw URL. It does not by itself prove the exact failing request because the desktop log was not captured.

Source-level fix AirPlayArtworkStability-v1 was added to feature/v5.0.x-active-presets-a98:
https://github.com/keshman74/airControl/commit/ff3ae4a351c19443006af98f7888705a4cf3191e

The Linkplay parser filters the raw /data/AirplayArtWorkData.jpeg URL only when its host equals the selected device IP. That self-signed player-local URL must first be fetched by Electron and represented as a data: URL; it must not fall through to Chromium on a transient resolver miss. A failed fetch for the same media keeps the previous successfully resolved data URL. When the media title changes and no new artwork is resolved, the previous art is cleared to avoid showing the old album. Other local routes and public CDN URLs are unaffected.

Validation: parser tests passed for transient failure retaining last-good artwork, raw player URL rejection, clearing stale artwork on new track, and replacing the old data URL with a newly resolved image. The guarded installer applied successfully to the full source parser fixture, was idempotent on a repeated run, and saves a backup. This validates parsing/installer logic only. The user has not yet confirmed this second patch on the A98 hardware; the full Electron/Vite build has not run in this environment. KNOB0.8.23 continues to be user-confirmed working for AirPlay cover on A98; A31 path issue remains separate.
