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

### Hardware feedback and response handling — 2026-10-13
User confirmed A31 preset selection works and KNOB returns to Player. On A33 the selected preset begins playing, but KNOB reports PRESET FAILED and stays in Presets. Slot, installed version, HTTP status and response body were not supplied in that feedback; do not infer all slots or a precise network cause.
This proves the displayed failure does not necessarily represent a failed action on the tested A33.

v0.8.13 (3d6384a55a3fb218717a997dc5ccde191c7bd445) **IMPLEMENTED / HOST-TESTED; hardware fix unconfirmed**:
- Dedicated A33 choice classification uses HTTP status plus body. HTTP200 OK/Not/empty treated as accepted request; unknown-command and explicit plain Error/Failed/Unsupported/false rejected.
- Connection-lost(-5), read-timeout(-11), HTTP5xx treated as unconfirmed (may have acted); return to Player with CHECKING, query normal state, do not resend choice or auto-resume an uncertain selection.
- Accepted selection keeps the v0.8.12 delayed resume policy.
- Other connection errors/HTTP4xx stay rejected.
- Log slot, HTTP code, byte length and result only, not response data/secrets.
HTTP200 is request acceptance, not proof of the selected slot; a later state read is separate. Exact failure cause in user feedback remains unknown.

## QRY-WIIM-PRESET-LIST / CMD-WIIM-PRESET-PLAY — A97/A98 implementation
Status: **DOCUMENTED (official WiiM HTTP API v1.2) / IMPLEMENTED / HOST-TESTED; user hardware confirmation pending**.
Sources: https://www.wiimhome.com/pdf/HTTP%20API%20for%20WiiM%20Products.pdf sections 2.8.1-2.8.2; user reference https://cvdlinden.github.io/wiim-httpapi/tags/Presets.html.
These are WiiM product commands, not a guarantee for every product sharing an A97/A98 chip.

- List: HTTP/HTTPS /httpapi.asp?command=getPresetInfo.
- JSON preset_num is occupied count, not highest slot; preset_list rows contain number (1-based), name, url, source, picurl.
- Launch: MCUKeyShortClick:<1..12>. User reference also describes optional track suffix :<track>, 1-based; NOT implemented in KNOB here.
- Preserve original number in sparse lists. KNOB v0.8.14 parses only number/name, sorts by slot, skips invalid/duplicate/unnamed rows, accepts an empty valid list, and clears stale data on failed reads.
- For known A97/A98, use selected verified endpoint HTTP80 or HTTPS443 for list/launch. No speculative TCP8899 preset command and no automatic fallback from rejected getPresetInfo to a fabricated list.
- Read only on menu entry or Refresh; no background preset polling.
- A31 remains hardware-confirmed UPnP GetKeyMapping plus existing launch mechanism with 1..10 bound; its rejected getPresetInfo is NOT reintroduced.
- A33 remains getPresetListInfo / choicePreset with delayed resume and response policy.
Source: airKNOB experimental/multichip-v0.8.0 commit 2602c104e5b1ffa6acc79ec9f7172da663603274, version0.8.14.
Host tests compile the actual parser/filter against ArduinoJson6.21.6 and actual selection helper: sparse slots1/6/12, Cyrillic, sorted11/12, invalid/duplicate/type rejection and command routing isolation.

### A31 key-map MaxNumber=21 — hardware readback and KNOB parser correction, 2026-10-20

Status: **HARDWARE-CAPTURED structure / IMPLEMENTED parser fix / HOST-TESTED; firmware hardware retest pending**.

The user's current A31 at192.168.0.35 returns GetKeyMapping QueueContext with MaxNumber=21, Key0..Key21, populated Key1 Space Station Soma, Key2 DEF CON Radio, Key3 Suburbs of Goa, Key4 Synphaera Radio, and empty Key0/Key5..Key21. QueueContext contains an escaped KeyList and further-escaped DIDL Metadata. This is an additional confirmed variant; do not require MaxNumber=20 based on the older capture.

KNOB0.8.17 parseKeyPresets explicitly rejected maximum>20, before processing any key. The user's pasted MaxNumber21 therefore explains the captured HTTP200/10740-byte/xml_structure rejection. It does not explain the separate zero-byte http_or_body failure, which remains unresolved.

KNOB0.8.18 accepts a bounded map maximum1..64 but iterates only Key1..Key20 to fit its20-entry storage. Original slot IDs and display-name timestamp cleanup are retained. Key21 support for display or launch is not implied. A31 launch remains bounded1..10 pending evidence.

Source: [3eeb389cca4e5360751a37a70a001bfcce725281](https://github.com/keshman74/airKNOB/commit/3eeb389cca4e5360751a37a70a001bfcce725281).
The actual parser regression test reconstructs the reported SOAP/KeyList/nested-Metadata shape and verifies the four original slot names; an all-populated21-key case verifies storage remains bounded20, and invalid MaxNumber65 is rejected. User serial/service tokens were not committed.
CI: [39479866247](https://github.com/keshman74/airKNOB/actions/runs/39479866247). Parser step passed; consult final workflow result for firmware build status.

Separate A98 KNOB restart remains unconfirmed as to cause.0.8.18 adds numeric ESP reset_reason and raw loop/worker stack high-water marks in /health. These values support diagnosis, not a claim that A98 restart is fixed. User-confirmed A33 preset behavior is preserved.

### KNOB0.8.20 — A97 preset menu integration

Status: **IMPLEMENTED / HARDWARE TEST PENDING on A97**. Source: https://github.com/keshman74/airKNOB/commit/1360ce68a2acf628b4d56b0820ada1d08ab4762c .
Build/tests: https://github.com/keshman74/airKNOB/actions/runs/39485073150 .

A97 uses the selected HTTP80/HTTPS443 endpoint for getPresetInfo and MCUKeyShortClick:N,1..12. Original sparse number values are preserved; empty/invalid rows are not converted to fabricated menu slots.

The deferred read from0.8.19 is generalized to both A97/A98: menu entry/Refresh requests one load; the main loop waits until the background worker is finished and drained, then loads outside the button handler. Pending volume, OTA and discovery defer work; menu/zone/chip changes cancel old work. A31/A33 retain their existing paths.

A97 /health reports actual preset HTTP status and received byte count plus http_or_body/json_parse/json_structure. wiim_presets_pending covers both chips; a98_presets_pending remains an A98-only alias.

Tests cover actual A97 list-loading branch with HTTP/HTTPS endpoint snapshots, Cyrillic and sparse slots3/12, transport failure, malformed JSON, invalid list structure, empty list, and existing1..12 launch routing. Deferred-reader tests exercise both chips and preserve A31/A33 isolation. Test/build success must be taken from the completed CI run, not inferred from this implementation note.

A98 PlayQueue+AVTransport+routines active-preset correlation remains A98-specific. It is not copied to A97 without device evidence; A97 external active-preset highlighting and hidden input-slot enumeration are not claimed by this update. API applicability is per product/firmware, not guaranteed by the chip name alone.

#### KNOB0.8.20 build verification
All26 regression suites and the ESP32-S3 build passed in run39485073150. Final test-source commit b9b0979b1465964d2f5ce13e44ce04e89cbbd3b5. The first run rejected an overly specific syntax-error assertion for a filtered non-object token; the revised test separately verifies truncated-JSON syntax failure and non-object rejection. No test or publication gate was skipped.
Published main OTA binary: 1343696 bytes, MD5 7cd914bc936684e129b2a93a4ae465ba. A97 hardware result is still pending.

## getPresetInfo — negative hardware result, 2026-10-20

Status: **HARDWARE-OBSERVED UNSUPPORTED on the tested A97-labelled device**.
Selected zone: Кухня,192.168.0.99, HTTPS443; device firmware/version was not supplied in this sample.
A direct curl -k HTTPS /httpapi.asp?command=getPresetInfo returned literal unknown command with HTTP200. KNOB0.8.20 health independently reported preset_http200, preset_bytes15, preset_error=http_or_body, and the user confirmed the list does not appear.

This negative result overrides the source-documented WiiM command candidate for this tested product/firmware. HTTP200 is not API success. Do not claim all A97 products support getPresetInfo merely because WiiM API documentation lists it. Launch MCUKeyShortClick:N has not been tested by this result.

Next read-only candidate: discover the advertised PlayQueue service through the device description/SCPD and, only if advertised, test GetKeyMapping. Do not assume A31 port49152, A98 port59152, returned mapping semantics, or A98 routine/active-state support for A97 until observed. The currently failing read used the correct selected HTTPS endpoint; switching blindly to HTTPS is not a fix.
