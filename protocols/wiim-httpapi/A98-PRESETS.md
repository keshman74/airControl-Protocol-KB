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

## Reload_Button_GET experiment

**Status:** HARDWARE VERIFIED on A98, but **not a preset-slot enumeration API**.

Command:

`Reload_Button_GET`

Observed response:

```json
{"version":"1.0","buttons":[{"index":"play/pause","value":"play/pause"},{"index":"VolumeUp","value":"VolumeUp"},{"index":"VolumeDown","value":"VolumeDown"},{"index":"smartButton","value":"smartButton"},{"index":"factoryreset","value":"factoryreset"},{"index":"wpssetup","value":"wpssetup"},{"index":"btpair","value":"btpair"}]}
```

Conclusion: this query reports physical/control button assignments (play/pause, volume, smart button, factory reset, WPS, Bluetooth pairing). It does **not** expose the 12 preset-slot contents and therefore cannot be used to discover hidden saved input presets 7–9.

## Network preset status experiment — slot 3 Radio Record

**Status:** HARDWARE VERIFIED observation on A98

After `MCUKeyShortClick:3` (known preset 3 = Radio Record / newTuneIn), the device returned `OK`. Two seconds later `getPlayerStatus` showed:

- `mode = "10"`
- `vendor = "newTuneIn"`
- `status = "load"`
- `plicount = "0"`
- `plicurr = "0"`
- `Title` contained hex-encoded station metadata

`getStatusEx.preset_key` remained `"12"`, confirming again that this is the supported preset-key/slot count, not the active preset number.

No active preset-number field was observed in either `getPlayerStatus` or `getStatusEx`. For network/service presets, `mode=10` plus `vendor` identifies the playback/service context, but does not by itself identify which preset slot launched it.

## Native WiiM app active-preset observation

**Status:** USER/HARDWARE OBSERVED

The native WiiM app shows the full 12-slot preset screen, including media/service presets, saved input presets, and empty slots. Observed layout on the test A98:

1 Liked Music (YouTube Music); 2 A Hum Of Maybe (Qobuz); 3 Radio Record; 4 GREEN NOISE (Calm Radio); 5 Saffron and Smoke (YouTube Music); 6 NATURE RADIO SLEEP (WiiM Radio); 7 Optical In; 8 Line In; 9 Bluetooth; 10 Top Tracks (Deezer); 11 Empty; 12 Empty.

Crucially, the native app highlights the currently selected preset even when that preset was activated from **another controller/device**. Therefore the active preset state is available to the WiiM app through some device/state synchronization mechanism and is not merely local UI state from the app's own button press. This is strong evidence that an active-preset identifier/state exists outside the currently documented `getPlayerStatus` / `getStatusEx` fields observed so far.

Research implication: capture native-app traffic while the Presets screen is open, then activate different preset slots from another controller. Look for a poll, event, MQTT/state notification, or other API response whose value changes with the active preset number. This is higher-value than guessing undocumented commands.

## WiiM Home APK reverse-engineering: full key mapping / preset slots

**Status:** APK-REVERSE-ENGINEERED / HARDWARE TEST PENDING

Source inspected: WiiM Home Android 3.6.10.260924 (`com.linkplay.wiimhome`).

The native preset screen (`DeviceMuzo2PresetContentActivity`) registers with `LPDeviceObserverManager`. Its `updateMediaInfo(LPNotification)` refreshes the preset adapter when notifications of type `CURRENT_QUEUE_CHANGED` or `TRANSPORT_STATE_CHANGED` arrive. This explains how the Presets screen can react to state changes initiated by another controller; the exact active-slot derivation still needs hardware/traffic confirmation.

More importantly, the APK contains a separate **PlayQueue key-mapping API** used by the preset UI:

- UPnP service ID: `urn:wiimu-com:serviceId:PlayQueue`
- service type: `urn:schemas-wiimu-com:service:PlayQueue:1`
- control URL embedded for this device family: `/upnp/control/PlayQueue1`
- device description string: `:59152/description.xml`
- control endpoint string: `:59152/upnp/control/PlayQueue1`
- action: `GetKeyMapping`
- `GetKeyMapping` has one **out** argument: `QueueContext`
- action: `SetKeyMapping`
- `SetKeyMapping` has one **in** argument: `QueueContext`

The APK classes `LPPresetData` / `LPPresetList` expose `getKeyMapping`, `setKeyMapping`, `getIndex`, `setIndex`, and queue conversion via `KeyItem.covert2PresetList`. The preset-content flow calls the Linkplay DLNA provider path that executes `GetKeyMapping`.

This is currently the strongest candidate for retrieving the **complete 12 preset-key configuration**, including input presets omitted by HTTPS `getPresetInfo`. Do not mark the endpoint/response semantics hardware-verified until tested on the A98.

## A98 PlayQueue endpoint hardware confirmation

**Status:** HARDWARE VERIFIED endpoint discovery

On test A98 at `192.168.0.21`, HTTP GET to `http://192.168.0.21:59152/description.xml` returned the UPnP MediaRenderer description and explicitly advertised:

- `serviceType = urn:schemas-wiimu-com:service:PlayQueue:1`
- `serviceId = urn:wiimu-com:serviceId:PlayQueue`
- `SCPDURL = /upnp/PlayQueueSCPD.xml`
- `controlURL = /upnp/control/PlayQueue1`
- `eventSubURL = /upnp/event/PlayQueue1`

This independently confirms on hardware the PlayQueue service/port/control path found by APK reverse engineering. The `GetKeyMapping` action itself remains hardware-test pending until a SOAP request is executed.
