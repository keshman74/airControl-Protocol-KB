# Media presets command view

## A33M native HTTPS/HTTP preset API — official V1.2, 19 Jan 2026

Transport follows the A33M API envelope:
- HTTP: `http://<ip>:8000/?Instruct=<params>`
- HTTPS: `https://<ip>:8443/?Instruct=<params>`

Status: **DOCUMENTED / OFFICIAL-A33M-V1.2**. Hardware-confirmed on A33 (2026-10-10): `choicePreset:1`, `choicePreset:2` select slots (the latter returned `Not` but switched); `getPresetListInfo` returns 12 entries. `setPlayerCmd:resume` starts playback after selecting slot 2. Remaining preset commands not yet hardware verified. See `tests/A33-PRESETS-HW-2026-10-10.md`.

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

## QRY-A31-UPNP-KEY-MAPPING — hardware readback 2026-10-13
**CONFIRMED on tested A31**: SSDP LOCATION -> :49152/description.xml advertises serviceType urn:schemas-wiimu-com:service:PlayQueue:1, controlURL /upnp/control/PlayQueue1.
SOAP GetKeyMapping has no input arguments and returns QueueContext XML with KeyList / Key0..Key20, MaxNumber, ListName, Metadata, Name, PicUrl, Source, Url.
User readback returned seven nonempty Name values, including Cyrillic. Names carry a suffix _#~YYYY-MM-DD HH:MM:SS in observed entries.
Key numbering, occupancy and relationship to MCU+KEY button indices are **NOT YET CONFIRMED**: first diagnostic printed names without their Key ancestors. Do not infer Key0=physical preset 1.
Evidence: [A31 key mapping](../../evidence/hardware-tests/A31-KEY-MAPPING-2026-10-13.md).

### Follow-up slot structure readback
User confirmed MaxNumber=20; Key0 has no name; Key1..Key7 respectively contain CLARK, THE SECOND BITE, SomaFM: Space Station Soma, SomaFM: DEF CON Radio, Hit FM Ukraine, Люкс ФМ Україна - Lux FM Ukraine, SomaFM: DEF CON Radio; Key8..Key20 have no names.
**CONFIRMED readback**, not proof that MCU+KEY supports every declared slot or a fresh playback test.
KNOB v0.8.11 implementation (a0d9649a6882b95a92f07c57e4842d8248597026): read on entering Presets or explicit Refresh; strip observed timestamp suffix; list nonempty names with original Key IDs, not compacted menu indices; Key0 excluded. A31/Linkplay launch commands above slot10 remain blocked pending evidence.
A33 uses getPresetListInfo / PresetNumber / PresetName, with filtered JSON parsing and choicePreset:<N> for selection. No automatic resume was added; previously observed A33 selection vs playback behavior remains relevant.
A97/A98 use the same PlayQueue read candidate, **not yet hardware validated for preset lists**. Fixed :49152 endpoint is verified on this A31; dynamic alternate-port discovery is not implemented in this version. A failed read shows READ FAILED and no fabricated titles.

## QRY-A31-PRESET-ARTWORK — confirmed readback 2026-10-13
Status: **CONFIRMED on tested A31; proposed UI priority not yet implemented**.
GetKeyMapping returns artwork via KeyN/PicUrl and optionally embedded Metadata/DIDL albumArtURI. These fields are independent; do not assume PicUrl is always a station logo, always a thumbnail or always current.
Observed:
- Key1 CLARK: PicUrl Qobuz /images/covers/37/51/0801061025137_600.jpg.
- Key2 THE SECOND BITE: PicUrl Qobuz /images/covers/jd/rt/kzlq5t2zsrtjd_600.jpg.
- Key3 Space Station Soma: metadata albumArtURI TuneIn s53125/images/logog.jpg; PicUrl same station /images/logoq.jpg. Query retained in actual response.
- Key4 DEF CON Radio: metadata albumArtURI TuneIn profiles s227824/images/logog.png; PicUrl TuneIn albums /gn/HTXMLDNHJ0g.jpg (different artwork source; album-vs-station interpretation is an inference from URL hosts).
- Key5 Hit FM Ukraine: metadata albumArtURI and PicUrl both profiles s6122/images/logog.png.
- Key6 Люкс ФМ Україна - Lux FM Ukraine: both profiles s55142/images/logog.png.
- Key7 DEF CON Radio: PicUrl profiles s227824/images/logog.png; no nested metadata artwork printed.
Current GetPositionInfo returned title Space Station Soma and albumArtURI profiles s53125/images/logog.jpg, matching Key3 metadata artwork.
This confirms stored artwork reading and one current-source comparison; it does **not** prove a Key3 playback command or a Key5 before/after switch (that test remains pending).

Design recommendation for airControl (NOT YET IMPLEMENTED):
- For radio preset tiles prefer stored metadata albumArtURI, then PicUrl when missing.
- For album/music presets use PicUrl when available; preserve other metadata rather than force radio logic on music.
- For Now Playing use current transport artwork; a saved preset image is only a provisional image for that selected preset, never proof of the current song/album cover.
- Missing/failed current artwork must not leave a previous unrelated album/station visible.
- Associate all artwork fields with original KeyN, not compacted display position.
- TuneIn thumbnails can use .jpg as well as .png: observed logoq.jpg is hardware readback. KNOB v0.8.10 currently rewrites only logog.png; JPG rewrite not implemented yet.

### Follow-up current metadata after Key5 selection — 2026-10-13
**CONFIRMED user readback**: after the requested manual selection of Key5, GetPositionInfo returned title Hit FM Ukraine and albumArtURI http://cdn-profiles.tunein.com/s6122/images/logog.png?t=636486210612100000. This matches stored Key5 Metadata/albumArtURI and PicUrl. Previous current readback was Space Station Soma (Key3).
Thus the current metadata source updated across this observed station change. The selection transport/native app used was not identified by this output; do not claim an MCU playback command was verified. No screenshot or KNOB artwork-display result was supplied in this test.

### A33 preset auto-start — KNOB v0.8.12
Status: **IMPLEMENTED / HOST-TESTED; KNOB hardware confirmation pending**.
Source commit: 674ad97b9764919bcedac0da300eed30ccbfdbf0 (airKNOB experimental/multichip-v0.8.0).
Uses the 2026-10-10 hardware-tested choicePreset -> 2s -> setPlayerCmd:resume sequence.
After selection, a nonblocking timer waits at least 2000ms; one getPlayerStatus query uses PlayStatus/status. If playing, skip resume. If paused/stopped, resume once. If unavailable/unrecognized, use the tested unconditional-resume fallback once; not a universal service guarantee.
Never repeat choicePreset on Not. A new preset, KNOB manual Play/Pause, source change or endpoint change cancels the timer. Zone mismatch/slave mode cancels; unsent volume takes priority; jobs expire 6000ms after due time rather than starting stale playback after a long outage.
No blocking delay(2000), no continuous preset polling, no A31/A97/A98 behavior change.
The 2026-10-13 user again reported A33 selection without playback. This confirms the symptom, not the new firmware fix.
