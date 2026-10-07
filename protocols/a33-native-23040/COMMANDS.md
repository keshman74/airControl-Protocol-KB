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
