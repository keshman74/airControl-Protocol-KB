# a33-json-1234 commands

## `CMD-A33-PLAY`
- **Device:** A33
- **Function:** playback
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"play"}
```

**Notes:** Hardware-confirmed.

## `CMD-A33-PAUSE`
- **Device:** A33
- **Function:** playback
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"pause"}
```

**Notes:** Hardware-confirmed.

## `CMD-A33-NEXT`
- **Device:** A33
- **Function:** playback
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"next"}
```

**Notes:** Hardware-confirmed.

## `CMD-A33-PREV`
- **Device:** A33
- **Function:** playback
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"prev"}
```

**Notes:** Hardware-confirmed.

## `CMD-A33-VOLUME`
- **Device:** A33
- **Function:** volume
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"volume","level":<N>}
```

**Notes:** Hardware-confirmed.

## `CMD-A33-MUTE-ON`
- **Device:** A33
- **Function:** mute
- **Transport:** TCP :1234 JSON
- **Status:** `CONFIRMED`

```text
{"cmd":"mute","state":"on"}
```

**Notes:** Hardware-confirmed.
