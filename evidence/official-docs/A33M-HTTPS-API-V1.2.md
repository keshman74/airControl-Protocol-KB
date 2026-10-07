# HTTPS API for A33M — User Manual V1.2

**Date:** 19 Jan 2026  
**Length:** 36 pages  
**Source:** user-supplied official PDF `LATEST_HTTPS_API.pdf`.

## Transport
Official A33M envelope:
- HTTP `http://<ip>:8000/?Instruct=<params>`
- HTTPS `https://<ip>:8443/?Instruct=<params>`
Responses are JSON or text.

## Command surface
The manual documents device/status, network, playback, volume/mute/channel, device control, USB, source switching, Bluetooth, metadata, multiroom, prompt sounds, static IP, EQ and a new explicit **Preset control** section.

Compared with the earlier CS2/ADAmp/ACAmp manual already in this KB, the most important newly recovered surface for airControl is the seven-command A33M preset API:
- `oneClickPreset:<presetInfo>`
- `choicePreset:<presetNumber>`
- `playPreviousPreset`
- `playNextPreset`
- `movePresetPosition:<moveInfo>`
- `deletePreset:<presetNumber>`
- `getPresetListInfo`

See `functions/media-presets/COMMANDS.md` for exact parameters and responses.

## Important A33M details
- 12 preset positions are exposed by this API.
- `oneClickPreset` can auto-select a free position with PresetNumber 0.
- PresetNumber 0 in `deletePreset` means clear the entire preset list.
- Presets can be reordered using OldIndex/NewIndex.
- The list query returns JSON, but this manual provides no JSON example/schema.
- Source switching is hardware-dependent; documented strings include Network, Bluetooth, USB Disk, Line In, Line2 In, Optical In, Optical2 In, HDMI ARC, PHONO In, AUX In, Coaxial In.
- `getStatusEx` explicitly exposes MultiroomType/MultiroomStatus/Host and the manual defines host/slave/none plus busy/free semantics.
- Mute in group play also sets slave mute state.
- EQ adds `getEqSwitch` and explicitly states preset EQ and parameter EQ cannot be simultaneously active.

## Evidence rule
All entries sourced only from this PDF are **DOCUMENTED / OFFICIAL-A33M-V1.2**. Hardware status must be promoted only after a real A33/A33M request/response test or packet capture.
