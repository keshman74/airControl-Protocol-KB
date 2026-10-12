# a33-native-23040 commands

## `CMD-A33-SEEK`
- **Device:** A33
- **Function:** seek
- **Transport:** TCP :23040 binary
- **Status:** `CONFIRMED`

```text
A3 BF … [ASCII 4<seconds>] … FB
```

**Notes:** Seek 30/60/90/120 sec observed; full intermediate framing must come from source/capture, never guessed.

## `EVT-A33-TUNEIN-CONTEXT`
- **Device:** A33
- **Function:** online service
- **Transport:** TCP :23040
- **Status:** `CAPTURED`

```text
StreamMediaName=tunein + metadata/context
```

**Notes:** TrackTitle/Url/Id/Image, TuneinUrl/Id, TrackContext/Path.

## `EVT-A33-QOBUZ-CONTEXT`
- **Device:** A33
- **Function:** online service
- **Transport:** TCP :23040
- **Status:** `CAPTURED`

```text
StreamMediaName=qobuz + metadata/context
```

**Notes:** TrackId/SongList/TrackContext/Path/SongPlay/duration/FormatId; redact Token.


## `CMD-A33-PRESET-GET`
- **Device:** A33 (hardware test: EC04)
- **Function:** retrieve native preset list
- **Transport:** TCP :23040 binary
- **Status:** `CONFIRMED / HARDWARE VERIFIED`
- **Command ID:** `03 76`
- **Payload:** empty

```text
TX: A3 BF 00 00 00 03 76 FB
RX command: 03 76
RX data: http://<device-ip>/preset_list.txt
```

**Framing:** `A3 BF | SEQ | LEN_LO LEN_HI | CMD1 CMD2 | DATA | FB`. The A33 response includes a NUL byte (`00`) after the URL before `FB`; the length field covers the URL plus this NUL. The returned HTTP JSON contains top-level `Presets`. Filled preset records include `PresetNumber`, `PresetName`, `Logo`, `StreamMediaName`, `MusicData`, etc.

**Discovery evidence:** A33 UDP announcement to port 53308 contained `"port":"16800"`; application decoding is hexadecimal value shifted right by 2: `0x16800 >> 2 = 23040`. TCP :23040 was then hardware-verified.

## `CMD-A33-PRESET-ACTIVE`
- **Device:** A33 (hardware test: EC04)
- **Function:** activate/start native preset
- **Transport:** TCP :23040 binary
- **Status:** `CONFIRMED / HARDWARE VERIFIED`
- **Command ID:** `03 70`
- **Payload:** compact UTF-8 JSON using the selected preset's `Logo`, not `PresetNumber`

```json
{"Logo":"<Logo from preset_list.txt>"}
```

Example hardware-verified request:

```text
PresetName: ABC Lounge Jazz
PresetNumber: 3
Logo: ZOMLX20261012234757

TX:
A3 BF 00 1E 00 03 70
{"Logo":"ZOMLX20261012234757"}
FB
```

The preset started playing successfully.

**Success correlation:** the A33 later emits command `03 70` carrying the same Logo:

```json
{"Logo":"ZOMLX20261012234757"}
```

Do not require a literal `OK` or `Yes` response. After the request, asynchronous state/event frames can arrive before the matching `03 70` response (observed examples: `00 06` Network, `03 74` MusicData, `00 47` DevVolume, `02 57`, `00 48` VolumeState, `00 60` track context, `00 10` loop mode). A controller must ignore unrelated intermediate frames and wait for `CMD 03 70` with the matching `Logo` before declaring preset activation success.

**Implementation note (KNOB/airControl):** treating the first received frame after `03 70` as the command response can produce a false `preset failed` even though playback starts. Match responses by command ID and Logo.
