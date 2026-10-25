# iAudioCloud 2.0.260728 — A33 native control audit

Status: **APK-VERIFIED / NOT-HW-VERIFIED**. This is shipped Android client behavior, not a new hardware test. Existing hardware evidence for A33 native presets and seek remains authoritative for its tested device/firmware. The app contains an explicit A33 Bluetooth branch, but its entire command inventory must not be assumed supported by every A33 product.

- Package: `com.cloudyx.multimediaplayer`, version `2.0.260728`, code `43`, min SDK 23, target SDK 36.
- XAPK SHA-256: `7c7111112c224d65584440e085c2832330efa431bf7b91ea32f8c343513e65b9`.
- Base APK SHA-256: `c2efb0d153fd1005b4819dc358922ae7972f7d1b646e11a41ec4725096b0cefb`.
- Four DEX files; 8,308 parsed classes. Nineteen split APKs contain no DEX. The ABI split contains `libandroidx.graphics.path.so`; it was inventoried, not disassembled.
- [141 opcode constants and 109 send-site observations](IAUDIOCLOUD-OPCODES-2026-10-25.md), [machine-readable send sites](../../evidence/reverse-engineering/IAUDIOCLOUD-SEND-SITES-2026-10-25.csv), [provenance](../../evidence/reverse-engineering/IAUDIOCLOUD-2026-10-25.md).

## Discovery and endpoint selection

`DevicesInteracter` listens for device announcements on UDP **53308**. `DeviceTmpModel` holds `host`, `port`, `net`, `product_type`. Its `getRealPort()I` returns **58803** when `port` is absent; otherwise it evaluates `Integer.decode("0x" + port) >> 2`. Thus announcement `16800` means **23040**, not decimal 16800. This directly corroborates the existing [native preset hardware report](COMMANDS.md).

`BaseDeviceModel` subsequently accepts status field `TCPport` as a decimal port string. Its defaults are control **58803**, file **58814**, USB **58815**; corresponding fields are `TCPport`, `TCPFilePortAndroid` (Gson alternate `TCPFilePort`), `TCPUsbPort`. `DeviceModel` connects to `getIp(), getPortReal()`; this audit does not replace a working discovered 23040 endpoint with the fallback. A client should preserve discovery/status provenance instead of hard-coding one port for all firmware.

`SocketUtils.tcp` uses a 5000 ms connect timeout. The device daemon later sets socket read timeout to zero. UDP bind failure handling may try higher local ports; that implementation detail does not establish that devices announce to those fallback ports.

## Exact outbound frame

Source: `DeviceModel.makeSendParams([BLjava/lang/String;)[B`, mirrored by `StringUtils.makeSendParams`.

| Offset | Size | Meaning |
|---|---:|---|
| 0 | 2 | `A3 BF` |
| 2 | 1 | Sequence byte |
| 3 | 2 | UTF-8 payload byte length, little endian |
| 5 | 2 | Command bytes in the order listed in the inventory |
| 7 | LEN | Payload bytes |
| 7+LEN | 1 | `FB` |

Total outbound size is `8 + LEN`. There is no checksum or appended NUL in these builders. A null String/empty string produces zero payload bytes; a String is sent literally, while the Object overload serializes through Gson (`JsonUtils.obj2StringHtmlFilter`). JSON map values that look numeric are often **strings**. Do not add JSON quotes around raw scalar payloads. Sequences wrap through Java byte arithmetic; DeviceModel owns a per-instance counter while StringUtils owns a separate static counter. The asynchronous senders do not prove a single synchronized request sequence or universal response correlation by SEQ.

The sender casts byte length to Java short without a bounds check. This proves the field encoding, not that all 65535-byte payloads work: receive code also uses signed short. Existing hardware-observed NUL-terminated response URLs remain valid; outgoing builders do not imply identical response termination.

### Seek: resolve the historical `4<seconds>` shorthand

`PlaybackControlAgreement.setMusicProgress` sends opcode **00 34** and raw decimal `i + ""`. For 30 the derived packet with sequence zero is:

```text
A3 BF 00 02 00 00 34 33 30 FB
```

`34` is the second command byte (also ASCII `4`), not an extra character prepended to the payload. This completes the source-side framing for existing `CMD-A33-SEEK`; the displayed example is derived, not a newly captured packet. The integer unit matches existing seek hardware evidence; this static sender alone does not establish seek bounds.

## Playback, volume and sources

| Bytes | Payload / behavior | Source |
|---|---|---|
| `00 00` | Empty: request device information | DeviceModel.getDeviceInfo / sendGetDeviceInfo paths |
| `00 05` | Empty heartbeat | DeviceModel heartbeat sender |
| `00 32` | Raw `plays` or `pause` | PlaybackControlAgreement.sendPlay |
| `00 33` | `{"index":"+1" or "-1","SongPlay":"null"}` | PlaybackControlAgreement.sendChangeMusicCMD |
| `00 34` | Raw decimal position | PlaybackControlAgreement.setMusicProgress |
| `00 10` | `Shuffle`: `yes`/`no`; `Repeat`: caller string, constants include `Loopno`, `Loopyes`, `Single` | PlaybackControlAgreement.setPlayModeCMD / Type |
| `00 40` | Legacy volume: `VolumeState:"null"`, `DevVolumeL`, `DevVolumeR` string values | VolumeAgreement.sendVolumeCMDOld |
| `00 47` | `{"DevVolume":"<integer>"}` | VolumeAgreement.sendVolumeCMDNew |
| `00 40` | Legacy mute: `VolumeState:"mute"`/`"active"`, current L/R values | VolumeAgreement.sendMuteCMD |
| `00 48` | `{"VolumeState":"mute" or "unmute"}` | VolumeAgreement.sendMuteCMDNew |
| `00 49` | `{"DevVolumeChannel":"<caller value>"}` | VolumeAgreement.setChannel |
| `00 06` | Raw input mode string | DeviceModel mode sender |
| `00 01` | Raw name | DeviceModel rename sender |
| `00 02`, `00 03` | Empty factory reset / reboot requests | DeviceModel; not executed |

Volume selection parses the **second dot-separated firmware version component**: >=33 chooses `00 47`, otherwise `00 40`. Empty/insufficient version strings do not take either send branch; this is not general semantic-version comparison. `DeviceModel.sendVolume` clamps to device maximum, default 100 when the maximum is zero. `DeviceModel.setMute` calls **both** legacy and new mute senders asynchronously; no fixed order is established.

Input constants preserve spaces/case: `Network`, `Bluetooth`, `Line In`, `Line2 In`, `Aux In`, `Aux2 In`, `AUX In`, `AUX2 In`, `Optical In`, `Optical2 In`, `Coaxial In`, `Coaxial2 In`, `HDMI ARC`, `USB Disk`, `USB Device`, `PHONO In`, plus `ANY`, `STANDBY`, `WIFI`. Constants are not a per-device supported-mode list. Use returned capabilities and do not silently normalize to ACS2's other documented spellings.

TuneIn resume has a special path: under the app's Network/TuneIn/non-USB/non-AirPlay2 conditions it calls playTuneIn again instead of sending `00 32`. Therefore the generic raw play command does not describe every UI play action.

## Presets

Reuses `CMD-A33-PRESET-GET` and `CMD-A33-PRESET-ACTIVE`, already hardware-verified separately.

| Bytes | Request |
|---|---|
| `03 76` | Empty payload; response string is treated as an HTTP URL, fetched and parsed as top-level `Presets` |
| `03 70` | `{"Logo":"<preset identifier>"}` activate |
| `03 71` | Serialized PresetModel add |
| `03 73` | Serialized PresetModel edit |
| `03 72` | `{"Logo":"<preset identifier>"}` delete |
| `03 75` | `{"OldIndex":"...","NewIndex":"..."}` move |

`PresetModel` declares EqData, EqType, InputMode, Logo, LoopMode, MusicData, PresetName, PresetNumber, SetSleepTime, StreamMediaName, Volume. Serialization depends on populated fields; the model is not a guarantee all fields are required. `PresetAgreement` treats PresetName `Empty` specially and parses EqData for populated slots. Response handling uses Logo as identity. Keep artwork separate (`MusicData.TrackImage` in existing hardware evidence).

The HTTP ACS2 choicePreset/getPresetListInfo interface remains distinct. [Existing HTTP preset tests](../../tests/A33-PRESETS-HW-2026-10-10.md) found that `choicePreset:2` could return `Not` while selecting the slot, and resume after two seconds started playback. Do not overwrite that result with a generic success/error assumption from this APK.

## Multiroom, timers, network and auxiliary control

| Bytes | Request schema / meaning | Source class |
|---|---|---|
| `00 50` | `StreamSource:"pipe"`, `Host`, `Slave` array | MultiRoomAgreement |
| `00 52` | Empty multiroom status request | MultiRoomAgreement |
| `02 30`, `02 33` | Alarm add/edit: SetTime, RepeatWeek (empty becomes `0`), MusicData (null becomes `default`), Volume, TimeOut, StreamMediaName (default `default`), Switch, Logo | AlarmAgreement |
| `02 32` | Raw caller string for alarm deletion | AlarmAgreement |
| `02 34`, `02 35` | Empty alarm list / support requests | AlarmAgreement |
| `03 40`, `03 41` | JSON SetSleepTime + SleepCountdown / empty get | SleepAgreement |
| `03 42`, `03 43` | JSON SetStandbyTime + StandbyCountdown / empty get | StandbyAgreement |
| `00 04` | Raw standby state string (the unused local Status map is not sent) | StandbyAgreement |
| `03 85`, `03 86` | Set static IP / empty get | IpSetAgreement |
| `03 90` | `{"EnableDisNet":"true"}` | DeviceInfoAgreement |
| `04 10`, `04 11` | `{"AmplifierTrigger":"<caller string>"}` / empty get | TriggerSwitchAgreement |
| `04 20`, `04 21` | CustomizationSubject from project name, RingtoneSwitch, Enable `1` / empty get | DeviceInfoAgreement |
| `04 30` | Empty Bluetooth-reset request | DeviceInfoAgreement |

For `00 50`, a nonempty group list and host produce Host=host IP and Slave=[host IP, other group IPs]. A host without list produces Host=its stored host and Slave=[its IP]. No host produces Host=`0`, Slave=[`0`]. Preserve the target device and this branch logic; do not substitute Linkplay JoinGroup.

Static-IP payload always includes `StaticIpStatus:"1"`. Depending on selected interface it adds **EStaticIp/EStaticNetmask/EStaticGateway/EStaticDns** or **WStaticIp/WStaticNetmask/WStaticGateway/WStaticDns**. This sender is not evidence for a disable-static-IP payload. Timer units/ranges and trigger polarity are not established by these generic string senders.

## Media and firmware paths

The inventory includes native requests for USB `00 82/83`, local media `00 90/92`, HTTP URL `01 31`, TuneIn `00 60`, vTuner `02 00`, Tidal `00 20`, Qobuz `01 40`, shared media `02 20/21` and `02 80/82`. Service request maps are in the send-site catalogue, with source methods. They include identifiers, metadata and sometimes account Token parameters; only field names and variable expressions are retained, never live account values. These are native socket payloads, not an assertion that equivalent names work on TCP1234 or HTTP ACS2.

Firmware request `01 50` has no payload; `01 51` carries A33M_OTA=`yes` when the caller int is zero, otherwise `no`, MCU_OTA is `yes` only when that same integer is one, otherwise `no`. `01 52` is also used by SilentUpgradeAgreement with a SilentUpgrade field. `01 53` is used by `SilentUpgradeAgreement.sendGetSilentUpgrade` with a map containing a null-key/null-value entry; this audit does not infer a universal version query or exact wire JSON from the constant name OTA_VERSION. The generic field extractor omits that null-key assignment. OTA behavior was inspected statically; no firmware was downloaded or installed. A command name such as OTA_RESULT alone does not determine its direction or one universal schema.

## A33 Bluetooth provisioning

Source: DevicesInteracter.makeSendDataBLE, bleHandshake, bleSetNetWifi; byte constants cross-checked in smali.

- Service `0000AB00-0000-1000-8000-00805F9B34FB`; command/write AB01; command notify AB02; data AB03; data notify AB04 (same UUID suffix).
- Frame: `EC CE | command:1 | payload length LE16 | payload | terminator`.
- When the model's firmwareVersion equals `a33` ignoring case, terminator is **26**; other branch uses **FB**. The selector is a model string, not independent hardware identification.
- A33 handshake command `00` has bytes `A1 A1 AA BB CC DD 7C`; resulting frame: `EC CE 00 07 00 A1 A1 AA BB CC DD 7C 26`. The app logs `7C` as crc but hard-codes it; no general checksum algorithm is established.
- Notifications are enabled before writing the handshake when AB02 exists.
- Wi-Fi command `01` carries JSON `essid` and `passwd`, each hex encoding the UTF-8 input. Hex encoding itself is not encryption; BLE link security was not evaluated. No user credentials were collected or transmitted.
- Generic handshake contains client identity/version fields; its identity version differs from package version. The generic key value is omitted from published evidence.

## Receive handling and implementation limits

`DaemonRunnable` accumulates chunks and `bytesToResult` splits on byte FB; `ResultModel.fromByte` reads command at bytes 5–6, signed-short length at 3–4 and payload at 7. `DeviceUtils.getResultOnce` also relies on start/end markers. This is observed application code, **not** proof of robust stream framing. The code does not establish correct handling for every fragmented/coalesced sequence or arbitrary binary payload. A reconstruction should buffer by validated header and declared byte length, retain incomplete tails, and dispatch unsolicited messages separately; that is an analyst recommendation, not a hardware-tested algorithm here.

The receive dispatcher branches on opcode and ignores empty result data. It handles events as well as responses; no universal one-request/one-response contract or strict SEQ matching was found in the inspected dispatcher. Existing native preset response correlation by opcode plus Logo should be preserved.

## Coverage and remaining checks

Answered from static evidence: package identity/composition; discovery port decoding; request framing; 141 initializer constants; 109 selected send sites; playback/volume, presets, multiroom, timer/network control; EQ/RoomFit/subwoofer; A33 provisioning. See the following detailed EQ section.

Not performed: APK signature verification, installation/execution, device traffic capture, hardware command tests, native graphics-library disassembly, cloud-service validation. Whole-DEX const-string searching did not establish ACS2 `Instruct=` or `getStatusEx` builders; that bounded negative result does not prove every possible dynamically formed HTTP/JSON path absent. Existing TCP1234 and ACS2 hardware/documentary knowledge remains separate. Capability support and valid ranges must be established per device/firmware.

Suggested future device checks: read-only discovery/status first; compare announced and status ports; confirm new/old volume branch; observe mute ordering; verify EQ and RoomFit capability/ranges; capture fragmented/interleaved native responses. Reset, network, provisioning and OTA commands were not exercised.

## EQ, RoomFit, subwoofer and volume detail (hex bytes in actual array order)

| ID | Method/source | Outgoing payload |
|---|---|---|
|02 50|DeviceModel.handleResult EQ_TYPE_SYNC branch, 1372|Receive branch discards getData(); no sending method established here. Do not confuse with sendTypeSync.|
|02 51|EQAgreement.sendVolumeSync / lambda$sendVolumeSync$1|JSON {"Bass":"<integer>","Treble":"<integer>"}|
|02 52|EQAgreement.sendSet / sendCustomSet|JSON {"Custom":"0" or "1","Name":"...","EqBand":["<integer>",...]}: preset=0, custom=1|
|02 53|EQAgreement.sendSetParam|JSON {"Custom":"1","Name":"...","EqBand":[filter,...]}|
|02 54|EQAgreement.sendTypeSync|Raw caller string, not JSON-quoted string; exact selector set not established in these files|
|02 54|SubwooferAgreement.sendGetFreq|Object integer 4 serialized as scalar JSON `4`|
|02 55|EQAgreement.sendUpdataCustom|JSON {"Type":"2","Name":"...","EqBand":["<integer>",...]}|
|02 55|EQAgreement.sendUpdateParam|JSON {"Type":"3","Name":"...","EqBand":[filter,...]}|
|02 56|EQAgreement.sendCustomMove|JSON {"Type":"<caller string>","Name":"..."}; method name suggests removal and constant is EQ_CUSTOM_REMOVE|
|02 57|EQAgreement.sendEQOffNo|Raw caller string; enabled/disabled literal mapping not established here|
|02 58|EQAgreement.sendUpdataName|JSON {"OldName":"...","NewName":"...","Type":"<caller string>"}|
|02 59|SubwooferAgreement.sendFreqSync|JSON {"FreqValue":model value,"FreqMax":model max,"FreqMin":model min}; despite INFO_GET name this method sends frequency settings|
|03 20|SubwooferAgreement.sendPhase|JSON {"PhaseSwitch":"<integer>"}; DeviceModel.setSubwooferPhase maps boolean true->1, false->0|
|03 21|SubwooferAgreement.reset|Empty map JSON `{}`|
|04 40|RoomFitAgreement.sendPlaySound|No payload (null String), not JSON null|
|04 41|RoomFitAgreement.sendFilterInfo|JSON {"EqBand":[filter,...]}|
|00 40|VolumeAgreement.sendVolumeCMDOld|JSON {"VolumeState":"null","DevVolumeL":"...","DevVolumeR":"..."}; null is literal string|
|00 40|VolumeAgreement.sendMuteCMD|JSON {"VolumeState":"mute" or "active","DevVolumeL":"<current L>","DevVolumeR":"<current R>"}|
|00 47|VolumeAgreement.sendVolumeCMDNew|JSON {"DevVolume":"<integer>"}|
|00 48|VolumeAgreement.sendMuteCMDNew|JSON {"VolumeState":"mute" or "unmute"}|
|00 49|VolumeAgreement.setChannel|JSON {"DevVolumeChannel":"<caller string>"}|

Filter objects for 02 53, parametric 02 55 and 04 41: `{"Index":"<zero-based list index>","Filter":"<model type>","Freq":"<one decimal>","Gain":"<one decimal>","Q":"<two decimals>"}`. Null list elements skipped but index remains original index. Null list yields empty array. No isOff exclusion, min/max validation or band-count limit in these senders. String.format has no explicit Locale. Do not conflate with EqUtils.formatFiltersToMapList: that helper excludes isOff and uses `Type` rather than `Filter`, numeric rather than string values, and does not establish these socket payloads.

## Version and range behavior

VolumeAgreement.sendVolumeCMD (line 67): requires nonempty version and at least two dot-separated components. Parses **second component** as integer; >=33 selects 00 47, otherwise 00 40. This is not general semantic-version comparison, and malformed numeric component is not caught locally. DeviceModel.sendVolume (line 2085) clamps to [0, getVolumeMax()], default max=100 when getVolumeMax()==0. It updates L/R according to stereo/left/right and old command preserves opposite channel; new command sends single requested value.

DeviceModel.setMute (2137) calls both legacy sendMuteCMD and new sendMuteCMDNew every time, with no firmware branching. Each dispatches an independent thread, so no fixed wire order proven. setMuteGroup iterates slaves when nonempty, otherwise self.

No fixed bass/treble, graphic band, parametric Freq/Gain/Q or subwoofer frequency bounds established in these files. Subwoofer ranges arrive as FreqMin/FreqMax and should not be invented.

## Responses and caveats

- EQAgreement.setEqType expects `preset_EQ` array. Array-valued EqBand takes graphic branch; otherwise getEqParametricEQ parses its string as array. That parser reads `Mode` (default `PK`) rather than outgoing `Filter`; preserve the mismatch, do not silently normalize.
- EQAgreement.setEqParams reads Custom, Name, EqBand; filter uses Index, Filter, Freq, Gain, Q (default frequency 1000, gain 0, Q about 0.707). Rejects text error / EQ disable. Graphic 02 52 handler in DeviceModel similarly handles error / EQ disable before JSON parsing.
- 02 51 response reads Bass and Treble; Treble tolerates floating numeric text and truncates to int.
- 02 57 response stores raw data into EqEnable.
- SubwooferAgreement.setInfo reads FreqMin, FreqMax, FreqValue only when subwoofer model exists; recognizes `EQ disable` text. setSwitch reads PhaseSwitch.
- VolumeAgreement.refreshVolume expects DevVolumeL/DevVolumeR/VolumeState; refreshVolumeNew sets both L/R from DevVolume. setMute maps received unmute to internal active.
- BaseDeviceModel reads EqType, EqEnable, Subwoofer from device status (lines 433-440). Presence alone does not prove particular hardware support.
- No gain units, phase-angle degrees, max band count or device-chip compatibility proven. Static application-side schemas only.
