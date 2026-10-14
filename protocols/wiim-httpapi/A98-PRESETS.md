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

## GetKeyMapping — hardware verified complete key map

**Status:** HARDWARE VERIFIED on A98

SOAP action `GetKeyMapping` on `http://<device>:59152/upnp/control/PlayQueue1` returned `QueueContext` containing an XML `KeyList`.

Observed structure:

- `ListName = KeyMappingQueue`
- `MaxNumber = 21`
- keys are represented as `Key0` through `Key21`
- `Key1..Key12` correspond to the device's 12 user preset buttons/slots on the tested WiiM Pro/A98 UI; higher key records are present in the mapping structure but are not exposed as the 12 user preset buttons observed in the native app.

Observed key data:

| Key | Mapping returned by GetKeyMapping |
|---:|---|
| 0 | `RoutineId=Empty` |
| 1 | Liked Music; Source=YouTubeMusic; ContentType=songlist |
| 2 | A Hum Of Maybe; Source=Qobuz; ContentType=songlist |
| 3 | Radio Record; Source=newTuneIn; ContentType=station |
| 4 | GREEN NOISE; Source=CalmRadio; ContentType=station |
| 5 | Saffron and Smoke; Source=YouTubeMusic |
| 6 | NATURE RADIO SLEEP; Source=WiiMRadio; ContentType=radio |
| 7 | `RoutineId=ECA625C2-828F-4E7B-B7D3-4F05B2F002D8` |
| 8 | `RoutineId=D4C3F57E-71FB-442C-96F0-A079E5443E5E` |
| 9 | `RoutineId=089DB687-F75E-4550-BE35-5864D29A08BD` |
| 10 | Top Tracks; Source=Deezer2; ContentType=songlist |
| 11 | `RoutineId=Empty` |
| 12 | `RoutineId=Empty` |

Hardware/UI correlation already established separately: Key7 = Optical In, Key8 = Line In, Key9 = Bluetooth. Therefore saved input presets are represented in `GetKeyMapping` by non-empty `RoutineId` UUIDs rather than by `Name/Source/PicUrl` fields. `getPresetInfo` omits these routine-backed input slots, while `GetKeyMapping` exposes that they are occupied.

Media preset `Name` values contain a suffix in the observed form `_#~YYYY-MM-DD HH:MM:SS`; the native UI displays the name without this suffix. Artwork and source fields match the media preset information previously observed via `getPresetInfo`.

Important: `MaxNumber=21` is the maximum/key-map structure size returned by PlayQueue and must not be confused with `getStatusEx.preset_key=12`, which is the number of user preset buttons/slots exposed on this device.

## WiiM Home active-preset UI — APK correction and deeper trace

**Status:** APK-REVERSE-ENGINEERED; active-slot algorithm partially resolved

A deeper DEX trace corrects an earlier inference: the strings/methods `getPresetIndex` / `setPresetIndex` found in this WiiM Home build belong to `com.wifiaudio.feature.alarm.model.AlarmContextItem`. In `DeviceMuzo2PresetContentActivity`, `setPresetIndex` is used while building an alarm context (`PresetSongs`). It is **not evidence of a device API field carrying the currently active preset number**.

The Presets screen itself registers with `LPDeviceObserverManager`. Its `updateMediaInfo(LPNotification)` checks the notification UUID/type and refreshes the RecyclerView adapter for current-queue / transport-state changes. The adapter is obfuscated class `ct1`.

The adapter's bind path uses the current device/playback state rather than a directly observed `presetIndex` field. Relevant calls/inputs found in the binding logic include:

- `DeviceInfoExt.getDlnaPlayStatus()`
- preset `KeyItem.Source` and `KeyItem.Name`
- the routine repository / routine model
- audio-input resolution helpers; routine steps can be of type `AUDIOINPUT` and expose their input payload
- current audio-input item/name resolution

This strongly indicates that WiiM Home computes the visual "currently selected" state by correlating the current playback/input state with each KeyMapping item/routine, then rebinds the list when queue or transport notifications arrive. It does **not**, based on the code traced so far, simply read a public `activePresetIndex` value.

For routine-backed input slots (the hardware-verified Key7/8/9 mappings), the APK resolves the non-empty `RoutineId` through its routine repository and can inspect an `AUDIOINPUT` step. This explains how the native UI can label/highlight Optical In / Line In / Bluetooth even though `GetKeyMapping` itself returns only RoutineId UUIDs for those keys.

Further work: determine the exact media-preset matching fields used by adapter `ct1`, and inspect the UPnP event payload(s) feeding `CURRENT_QUEUE_CHANGED` / `TRANSPORT_STATE_CHANGED`. Do not document a standalone active-preset-number command unless hardware/API evidence is found.

### WiiM APK: Routine repository behind input preset UUIDs

**Status:** APK-REVERSE-ENGINEERED / HARDWARE TEST PENDING

Further inspection of WiiM Home 3.6.10.260924 shows a dedicated `RoutineRepository` in the preset feature. The APK contains methods/logging for `getAllRoutines`, `getRoutineCapability`, `createRoutine`, and `updateRoutine`, including command-building strings such as `getAllRoutines:`, `command=createRoutine:`, and `command=updateRoutine:`.

This repository is the next candidate for resolving the non-empty `RoutineId` UUIDs returned by `GetKeyMapping` for input-backed preset slots (hardware-correlated Key7 Optical, Key8 Line In, Key9 Bluetooth). The exact transport/request syntax for `getAllRoutines` is not yet hardware verified; treat it as APK evidence only until tested.

## getAllRoutines — hardware verified input-preset resolver

**Status:** HARDWARE VERIFIED on A98 (`192.168.0.21`)

Read-only HTTPS command:

`https://<device>/httpapi.asp?command=getAllRoutines`

returned a JSON object with `routines`. On the tested A98 it exactly resolved the three non-empty `RoutineId` UUIDs from PlayQueue `GetKeyMapping`:

| Preset index | Routine ID | name | step type | payload.input |
|---:|---|---|---|---|
| 7 | `ECA625C2-828F-4E7B-B7D3-4F05B2F002D8` | Optical In | `audioInput` | `optical` |
| 8 | `D4C3F57E-71FB-442C-96F0-A079E5443E5E` | Line In | `audioInput` | `line-in` |
| 9 | `089DB687-F75E-4550-BE35-5864D29A08BD` | Bluetooth | `audioInput` | `bluetooth` |

Each returned routine also contains `index`, and it matched the preset key number (7/8/9). Therefore the complete input-preset UI can be reconstructed dynamically without hard-coding slot meanings:

1. Read `GetKeyMapping` via PlayQueue.
2. For a key with non-empty/non-`Empty` `RoutineId`, read HTTPS `getAllRoutines`.
3. Match `KeyN.RoutineId == routine.id` (and the observed `routine.index == N`).
4. Use `routine.name` as the display label and `steps[].payload.input` as the machine-readable input identifier.

This closes the previously missing mapping for routine-backed input presets on the tested A98.

## PlayQueue GetCurrentQueueInfo experiment

**Status:** HARDWARE VERIFIED negative result on A98

After activating known preset 3 (Radio Record / newTuneIn), `getPlayerStatus` again showed `mode=10`, `vendor=newTuneIn`, `status=load`, with no active preset index. A SOAP call to PlayQueue action `GetCurrentQueueInfo` at `http://<device>:59152/upnp/control/PlayQueue1` returned UPnP error **401 / invalid action**. Therefore `GetCurrentQueueInfo` is not a supported PlayQueue action on this tested A98 and must not be used/documented as an available command. The next action names should be taken directly from the device's `/upnp/PlayQueueSCPD.xml` rather than guessed.

## A98 PlayQueue SCPD action inventory — hardware verified

**Status:** HARDWARE VERIFIED from device `/upnp/PlayQueueSCPD.xml`

The tested A98 advertises these PlayQueue actions: `CreateQueue`, `ReplaceQueue`, `DeleteQueue`, `BackUpQueue`, `AppendQueue`, `BrowseQueue`, `BrowseQueueEx`, `SetQueueLoopMode`, `GetQueueLoopMode`, `SetQueuePolicy`, `PlayQueueWithIndex`, `AppendTracksInQueue`, `RemoveTracksInQueue`, `MoveTracksInQueue`, `AppendTracksInQueueEx`, `SetKeyMapping`, `GetKeyMapping`, `GetQueueOnline`, `SearchQueueOnline`, `SetQueueRecord`, `SetSongsRecord`, `UserRegister`, `UserLogin`, `UserLogout`, `GetUserInfo`, `GetUserAccountHistory`, `SetUserFavorites`, `GetUserFavorites`, `GetQueueIndex`, `SetSpotifyPreset`, `DeleteActionQueue`, `GetBasicUserInfo`, `TakePlayControl`, and `SetRating`.

There is no advertised `GetCurrentQueueInfo` action, matching the hardware 401 invalid-action result. There is also no explicit advertised `GetActivePreset`/active-preset-index action. `GetQueueIndex` requires an input `QueueName` and returns `CurrentIndex`, `PreloadingIndex`, `CurrentPage`, and `TrackNums`; these are queue-track indices, not established preset-slot indices. `BrowseQueue` likewise requires a QueueName. Do not infer an active preset number from these actions without additional evidence.

## GetKeyMapping active-state comparison — hardware verified negative result

**Status:** HARDWARE VERIFIED on A98

A controlled comparison was performed after activating presets 1, 3, and 7 via `MCUKeyShortClick:N`. After each activation, both `getPlayerStatus` and PlayQueue `GetKeyMapping` were read.

Observed:
- preset 3: `getPlayerStatus mode=10, vendor=newTuneIn, status=load`
- preset 7: `getPlayerStatus mode=43, vendor="", status=play`
- `GetKeyMapping` remained structurally/content-identical across the captured preset 1 / 3 / 7 reads: same `ListName=KeyMappingQueue`, `MaxNumber=21`, media key metadata, RoutineIds for keys 7/8/9, and empty keys.

Conclusion: `GetKeyMapping` is configuration/key-assignment state, not active-preset state. It does not mark the currently active key in these observations. Active highlighting in WiiM Home must therefore be derived from other current playback/input state and/or event state.

Caution on the preset-1 sample: immediately after `MCUKeyShortClick:1`, the sampled `getPlayerStatus` still showed `vendor=newTuneIn`, `status=stop`, and the previous Radio Record title. This snapshot should not be used as evidence that preset 1 failed or that YouTubeMusic maps to newTuneIn; it may represent transitional/asynchronous state. A longer/timed poll is needed for reliable media-preset matching.

## Media preset transition timing — hardware verified (Preset 1 / YouTubeMusic)

**Status:** HARDWARE VERIFIED on A98

After `MCUKeyShortClick:1` for known Key1 = Liked Music / YouTubeMusic, repeated `getPlayerStatus` polling showed an asynchronous transition:

- initial samples: `mode=10`, empty `vendor`, `status=stop`, empty Title/Artist/Album
- subsequent sample: `vendor=YouTubeMusic`, `status=load`, with new title metadata
- later samples: `vendor=YouTubeMusic`, `status=play`, increasing `curpos/offset_pts`, stable nonzero `totlen`

Thus an immediate status read after `MCUKeyShortClick:N` is not reliable for identifying a media preset. The device clears/transitions current playback state before the target service becomes visible. Implementations should wait/poll until playback state stabilizes rather than interpreting the first response.

For this known preset, stable `getPlayerStatus.vendor=YouTubeMusic` matches `GetKeyMapping Key1.Source=YouTubeMusic`, but Source/vendor alone is **not sufficient to uniquely identify a preset slot** because multiple keys may share a service (e.g. more than one YouTubeMusic preset). No active preset number is exposed by this observation.
