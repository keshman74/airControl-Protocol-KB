# Media presets command view

## A33M native HTTPS/HTTP preset API — official V1.2, 19 Jan 2026

Transport follows the A33M API envelope:
- HTTP: `http://<ip>:8000/?Instruct=<params>`
- HTTPS: `https://<ip>:8443/?Instruct=<params>`

Status for the seven commands below: **DOCUMENTED / OFFICIAL-A33M-V1.2 / NOT-YET-HW-VERIFIED**.

### CMD-A33M-PRESET-ADD — add/save current state to a preset
`oneClickPreset:<presetInfo>`

`presetInfo`:
```json
{"PresetNumber":"x","Overwrite":"xxx"}
```
- `PresetNumber=0`: automatically find an empty preset slot. If none exists, overwrite from the first slot only when `Overwrite=yes`.
- `PresetNumber=1..12`: target that explicit slot.
- `Overwrite=yes`: replace an occupied slot.
- `Overwrite=no`: do not replace an occupied slot.
Returns: `OK`, `FAIL`, `Format`, `Exceed`, `Error`.

### CMD-A33M-PRESET-CHOICE — play/select preset
`choicePreset:<presetNumber>`
- valid slot: `1..12`
- returns: `OK`, `Not` (slot empty), `Format`, `Exceed`, `Error`.

### CMD-A33M-PRESET-PREV
`playPreviousPreset`
Returns `OK`, `FAIL`, `Error`.

### CMD-A33M-PRESET-NEXT
`playNextPreset`
Returns `OK`, `FAIL`, `Error`.

### CMD-A33M-PRESET-MOVE
`movePresetPosition:<moveInfo>`

```json
{"OldIndex":"x","NewIndex":"x"}
```
Moves the preset from `OldIndex` to `NewIndex`. Official example: 5 → 2.
Returns `OK`, `FAIL`, `Error`.

### CMD-A33M-PRESET-DELETE
`deletePreset:<presetNumber>`
- `0`: clear the entire preset list.
- `1..12`: delete the specified slot.
Returns `OK`, `FAIL`, `Format`, `Exceed`, `Error`.

### QRY-A33M-PRESET-LIST
`getPresetListInfo`
Returns a **JSON response** on success; the V1.2 manual does not publish an example/schema for that JSON body. Do not invent its fields. Returns `Error` on API command error.

## Other preset/key mechanisms

- `CMD-A31-MCU-PRESET` — **media preset** — `MCU+KEY+<001..010>` — **IMPLEMENTED/NEEDS-HW-EVIDENCE**
- `QRY-UPNP-RC-LIST-PRESETS` — **list rendering presets** — `ListPresets(InstanceID) -> CurrentPresetNameList` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-RC-SELECT-PRESET` — **select rendering preset** — `SelectPreset(InstanceID, PresetName)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-SET-KEY-MAPPING` — **preset/key mapping** — `SetKeyMapping(QueueContext)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `QRY-UPNP-PQ-GET-KEY-MAPPING` — **preset/key mapping** — `GetKeyMapping() -> QueueContext` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**

Do not conflate A33M's 12-slot preset API with A31's MCU key/preset mechanism or UPnP RenderingControl presets.
