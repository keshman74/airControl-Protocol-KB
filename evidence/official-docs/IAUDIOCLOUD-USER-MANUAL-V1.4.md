# iAudioCloud User Instruction Manual V1.4 — capability extraction

**Date:** 15 Jan 2026  
**Length:** 34 pages  
**Source:** user-supplied original PDF, recovered during chronological audit.

This manual is a **product/application capability source**, not a wire-protocol command specification. Capabilities below are therefore DOCUMENTED unless separate protocol/test evidence exists.

## Device provisioning and UI
- first-time Wi-Fi provisioning and adding further devices;
- device rename;
- local song push, volume control and source switching;
- playback UI exposes artwork, progress, volume and loop mode;
- playback queue/list can be opened and items deleted.

## Multiroom
The app supports synchronized playback groups. UI workflow: choose a master speaker, add other devices as slaves, submit the group. This independently corroborates the product-level Master/Slave model documented by the command API, but does not itself identify the underlying transport.

## Local library / favorites
- phone local songs and playlists can be pushed to the device;
- local playlists can be managed;
- Favorites applies to local My Music content;
- Tidal/Qobuz favorites remain service-native rather than the local Favorite store.

## Online services
The app exposes service entries including:
- Tidal
- TuneIn
- Qobuz
- Spotify
- Yandex
- YouTube
- vTuner
- QQ Music
- Music

Explicit in-app browse/push flows are documented for Tidal, Qobuz, TuneIn and vTuner. Presence in this UI is **not** proof that every device/chip supports every service; runtime capability detection remains authoritative.

## USB
When a supported device has a USB disk inserted, USB appears in Music services; its playlist can be browsed and selected tracks pushed to the device.

## Third-party renderer/connect protocols
Documented:
- DLNA (or Qplay) push from third-party players on the LAN;
- Spotify Connect;
- Qobuz Connect;
- AirPlay.

These are capability statements, not packet/API specifications.

## EQ
The application documents:
- Bass/Treble;
- Graphic/Preset EQ with 10 fixed bands and named custom saves;
- Parametric EQ with 10 bands, each exposing four adjustable parameters;
- Preset EQ and Parametric EQ are mutually exclusive and must not be enabled simultaneously.

This is an important behavior rule for airControl UI/state handling.

## Home Music Sharing
Two distinct sources are documented:

### Shared folder
A computer network share is added by UNC-style network path (example `\\computer name\music`). The app browses the shared folder and pushes selected tracks to the device.

### Media server
The app discovers/browses a media server on the LAN and pushes selected content to the device.

This corroborates the need for separate shared-folder/SMB-like and media-server/DLNA-UPnP library paths. The manual does not specify their low-level protocol implementation.

## Subwoofer behavior
- subwoofer is paired to a master and automatically reconnects/searches for its paired master in network mode;
- subwoofer may only be an extension/slave, never multiroom master;
- it cannot independently decode/play streaming music;
- no separate L/R channel setting;
- independent subwoofer EQ exists;
- after reboot, initial volume follows the physical knob position;
- disbanding group, network reconfiguration or factory reset can clear/unpair binding as described.

## Channel modes
UI semantics:
- LR = stereo;
- L = both device channels act as left;
- R = both device channels act as right.

## Advanced integration
The manual explicitly states the device supports remote control using HTTP and HTTPS commands for automated integration, including playback, volume and EQ, and points to an **“HTTPS API for A33M User Manual”** for command details.

This is a newly identified protocol-document dependency and should be recovered/audited separately if available.

## Timers
- timed playback / alarm clock;
- timed playback sources currently documented as Tidal, Qobuz, TuneIn and vTuner;
- timed playback requires powered-on device + Internet;
- sleep timer;
- timed standby.

## Presets
Preset playback can save/recall:
- songs;
- input sources;
- sound modes/EQ;
- loop mode and shuffle for song presets.

Preset slots can be overwritten, deleted and reordered. Empty/input-source preset slots may select hardware-supported inputs such as Network, AUX In, Bluetooth and USB Disk plus EQ settings.

## Firmware update
- app indicates new firmware/update progress;
- manual update through app;
- other supported methods named: Web, PC tools and USB drive;
- silent update window defaults/documentation to 04:00–06:00 local time;
- device must remain powered and online; unsuccessful silent update is retried in the configured daily window.

## Canonical implications
1. Add capability/service records without falsely converting them into low-level commands.
2. Preserve EQ mutual-exclusion behavior.
3. Preserve subwoofer role restrictions.
4. Model local shared folders separately from media-server discovery.
5. Treat service availability as per-device/runtime capability, not global.
6. Recover the referenced **HTTPS API for A33M User Manual** as a separate protocol source.
