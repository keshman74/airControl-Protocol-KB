# Artwork

Seed page. Add commands through the registry and link evidence here.

## Confirmed compatibility
- `QRY-A98-METAINFO-ARTWORK`: on A98, `getMetaInfo` artwork through the Electron resolver is confirmed working in airControl.
- Do not generalize this to A31: `QRY-A31-METAINFO` remains REJECTED on the tested A31 firmware.

## AirPlay open issue — 2026-10-24
User reports native-app cover visible, KNOB/airControl cover missing while text metadata works. Device/profile and artwork path diagnosis pending. External player-local AirPlay artwork path is a test candidate, not yet hardware-confirmed for this setup. See [evidence and diagnostic plan](../../evidence/hardware-tests/AIRPLAY-ARTWORK-2026-10-24.md).

## A98 AirPlay cover flicker follow-up — 2026-10-24
The user reports the cover briefly flashes in airControl5.0.0 but does not remain visible after the TLS resolver patch. Source review found that a transient resolver miss could leave the raw self-signed player URL in metadata; renderer parsing could then expose it to Chromium, while poll updates could repeatedly replace a valid data URL. Implemented AirPlayArtworkStability-v1 in the same feature branch to filter this exact selected-player endpoint and retain last-good decoded artwork for the same track. See [evidence and validation status](../../evidence/hardware-tests/AIRPLAY-ARTWORK-2026-10-24.md#aircontrol500-airplay-cover-stability-follow-up---2026-10-24).
