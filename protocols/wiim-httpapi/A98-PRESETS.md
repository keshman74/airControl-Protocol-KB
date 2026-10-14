# A98 presets — hardware verification

## Test device

- Chip/platform: **A98**
- Test IP: `192.168.0.21`
- Transport: **HTTPS**
- Endpoint form: `https://<device-ip>/httpapi.asp?command=<command>`
- TLS test client: `curl -k` (device/local certificate handling)

## `getPresetInfo`

**Canonical ID:** `QRY-WIIM-GET-PRESET-INFO`

**Status:** **HARDWARE VERIFIED on A98**

Request:

```text
https://192.168.0.21/httpapi.asp?command=getPresetInfo
```

Observed response structure:

```json
{
  "preset_num": 7,
  "preset_list": [
    {
      "number": 1,
      "name": "Liked Music",
      "url": "unknow",
      "source": "YouTubeMusic",
      "picurl": "https://www.gstatic.com/youtube/media/ytm/images/pbg/liked-songs-delhi-1200.png"
    }
  ]
}
```

Observed field semantics:

- `preset_num` — number of populated presets returned; observed `7`.
- `preset_list` — array of populated preset entries.
- `number` — preset slot number. `getPresetInfo` returned media/service presets in slots **1, 2, 3, 4, 5, 6, 10**. Hardware observation additionally confirms that slots **7, 8, 9 are occupied by saved input presets** (Optical, Line In, Bluetooth respectively), even though they were not present in this `getPresetInfo` response.
- `name` — display name.
- `url` — observed as literal `"unknow"` for all tested entries; do not depend on it as a playable URL.
- `source` — service/source identifier.
- `picurl` — artwork/logo URL; observed both HTTPS and HTTP artwork URLs.

Observed sources in this hardware response:

- `YouTubeMusic`
- `Qobuz`
- `newTuneIn`
- `CalmRadio`
- `WiiMRadio`
- `Deezer2`

### airControl implementation notes

- Use `number` as the preset slot identifier.
- Use `name` as the UI label.
- Use `picurl` for preset artwork.
- Preserve `source` for service identification.
- Do not assume `getPresetInfo` enumerates every occupied preset slot. On the tested A98, slots **7=Optical, 8=Line In, 9=Bluetooth** are occupied input presets but were omitted from the returned `preset_list`.
- Treat `preset_num` as the count represented by the returned preset list, not as the total number of occupied hardware preset slots and not as the highest slot number. Observed `preset_num=7`, while slots 7–9 are separately occupied inputs and slot 10 is returned as a media preset.
- Mixed-content artwork is possible because `picurl` may be HTTP even though the device API transport is HTTPS.

## Preset activation

Source documentation defines:

```text
MCUKeyShortClick:{n}
```

for preset slots 1–12, and:

```text
MCUKeyShortClick:{n}:{t}
```

for preset + track number.

**A98 activation status:** **HARDWARE VERIFIED**.

On the test A98 (`192.168.0.21`), `MCUKeyShortClick:3` successfully started preset slot 3 (`Radio Record`, source `newTuneIn`). This confirms preset activation by the `number` returned from `getPresetInfo`.

Hardware-verified example:

```text
https://192.168.0.21/httpapi.asp?command=MCUKeyShortClick:3
```

Observed result: preset 3 started playback successfully.

Input-preset activation is also **HARDWARE VERIFIED** for slot 7. On the test A98, `MCUKeyShortClick:7` switched the device to the saved **Optical** input preset successfully.

This confirms that the same `MCUKeyShortClick:{n}` mechanism can activate both a media/service preset (verified slot 3, Radio Record) and a saved input preset (verified slot 7, Optical). Slots 8 (Line In) and 9 (Bluetooth) are known occupied input presets but have not yet been individually activation-tested in this record.

## Hidden input preset identification experiment

**Status:** HARDWARE VERIFIED observation on A98

After activating slot 7 with `MCUKeyShortClick:7`, the device switched to the saved **Optical** input and returned:

- `getPlayerStatus.mode = "43"`
- `status = "play"`
- `Title/Artist/Album = "556E6B6E6F776E"` (hex for `Unknown`)
- `getStatusEx.preset_key = "12"` — on this A98 this indicates the device supports **12 preset keys/slots**, not the currently active preset
- `getStatusEx.security = "https/2.0"`
- `getStatusEx.public_https_version = "1.0"`
- firmware observed: `Linkplay.4.8.827634`
- project: `WiiM_Pro_with_gc4a`
- hardware field: `AmlogicA113`

The useful discriminator for the active source is therefore currently `getPlayerStatus.mode`; `getStatusEx` does not directly label the active input as Optical in this observation. Do **not** interpret `preset_key = "12"` as the active preset number: it denotes the device's **12 available preset buttons/slots**. Slot 7 was active while the field remained `"12"`.

Further hardware tests completed:

| Preset slot | Saved input | `getPlayerStatus.mode` | Activation response | Player status |
|---|---|---:|---|---|
| 7 | Optical | `43` | `OK` | `play` |
| 8 | Line In | `40` | `OK` | `play` |
| 9 | Bluetooth | `41` | `OK` | `stop` in the observed test |

Thus the tested A98 input-mode mapping is **40 = Line In, 41 = Bluetooth, 43 = Optical**. All three saved input slots 7–9 are hardware-verified to activate successfully through the same `MCUKeyShortClick:{n}` command, despite being omitted from `getPresetInfo`.

For Bluetooth, `status="stop"` after switching does not mean the preset activation failed: the device returned `OK` and switched to Bluetooth; no Bluetooth media playback was active at the moment of the status query.
