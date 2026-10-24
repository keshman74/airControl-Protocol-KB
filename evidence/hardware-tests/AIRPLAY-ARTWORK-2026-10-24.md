# AirPlay artwork missing in KNOB and airControl — 2026-10-24

Status: USER-REPORTED OPEN ISSUE; device/chip/firmware and current AirPlay source app not yet supplied.

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
