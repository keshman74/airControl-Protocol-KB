# Source audit — project origin chat + official CS2/ADAmp/ACAmp API

## Provenance

Historical chat: **«Приложение управления устройствами»**, started 11 Sep 2026. This is the first airCloudCTRL/airControl development chat supplied for chronological audit.

User's initial source set:
- CLOUDYX product page for the target audio module family.
- FilmoScope Lab LLC, **“HTTPS API for CS2, ADAmp.70, ACAmp-60/100 — User Manual”**, update 2025-08-26, 31 pages.
- Pascal Audio software page as UI/UX reference only (not a device-control protocol).
- Attachment **“airCloud App .pdf”**, described by the user as the phone-app user manual. The saved HTML preserves the attachment card/name but not the PDF bytes; it must be audited separately if/when the PDF itself is accessible.

## What this chat establishes

The initial application requirement was to expose the documented device functions through a desktop UI while hiding raw API commands behind an abstraction layer. Functional groups identified from the official API were: device/status, network, playback, volume/mute/channel, source, Bluetooth, EQ, multiroom, USB, prompt sounds and system/device management.

The first generated airCloudCTRL v0.1 implemented/catalogued the documented HTTP/HTTPS command surface and an Electron transport, but the chat contains **no device command/response hardware test**. The only executed test in this historical chat is application startup via npm/Vite/Electron.

Therefore protocol records sourced only from this stage are **DOCUMENTED**, not CONFIRMED.

## Official transport

The manual documents both forms:

```text
HTTP  http://<device-ip>:8000/?Instruct=<params>
HTTPS https://<device-ip>:8443/?Instruct=<params>
```

Responses may be JSON or text.

## Official command families recovered from the manual

### Network
- `wlanGetConnectState`
- `getScanAPs`
- `connectToAP:wifiName:<name>:wifiPassword:<password>`
- `setNetIPSwitchState:<switch>`
- `setStaticIP:<staticIPInfo JSON>`

### Playback / volume / channel
- `getPlayerStatus`
- `setPlayerCmd:play:<url>`
- `setPlayerCmd:playlist:<songid>`
- `setPlayerCmd:pause`
- `setPlayerCmd:resume`
- `setPlayerCmd:onepause`
- `setPlayerCmd:prev`
- `setPlayerCmd:next`
- `setPlayerCmd:getplay:<seconds>`
- `setPlayerCmd:setplay:<seconds>`
- `setPlayerCmd:stop`
- `setPlayerCmd:vol:<value>`
- `setPlayerCmd:RemoteVol++`
- `setPlayerCmd:RemoteVol--`
- `setPlayerCmd:mute:<0|1>`
- `setPlayerCmd:maximumVolume:<value>`
- `setChannel:<rl|rr|ll>`
- `setPlayerCmd:prompttone:<Enable|Disable>`
- `setPlayerCmd:loopmode:<1..5>`

### Status / metadata
- `getStatusEx`
- `getMetaInfo`

The manual's getStatusEx example includes device/network/volume/source/playback fields and `MultiroomStatus` / `Host`. The getMetaInfo example includes Title, Artist, Album, Picture, Schedule, Totlen and PlaySource; its published example uses `PlaySource: tidal`.

### Multiroom
- `multiroom:setHost` — designate the master before adding slaves.
- `multiroom:setSlave:<host_ip>` — send to the prospective slave.
- `multiroom:disconnectSlave` — send to the corresponding slave; slave leaves its group.
- `multiroom:breakUp` — send to the corresponding master; breaks the group.
- `multiroom:getInformation` — returns group topology/status fields.

Important: this ACS2-style multiroom family is kept separate from later Linkplay native multiroom research and tests.

### USB / sources
- `playFromUsbDisk`
- `getUsbSongList`
- `selectUsbTracks:<usbSongNum>`
- `setPlayerCmd:switchmode:<mode>`

Documented source strings: Network, Bluetooth, LineIn, USBDisk, OpticalIn, HDMIARC, RCAIn, RCA2 In, PHONO In.

### Bluetooth
- `setDiscoveryBluetooth:<Open|Close>`
- `resetBluetoothPairing`
- `clearBluetoothPairingList`
- `getBluetoothName`
- `modifyBluetoothName:<bleName>`

### Prompt sounds
- `downloadPromptSound:<audioFileName>`
- `playPromptSound:<audioName>:<volume>`
- `viewServerPromptSound`
- `viewDevicePromptSound`
- `deleteSpecifiedAudio:<audioPath>`

### EQ
- `getEqType`
- `eqEnable:<eqSwitch>`
- `setEqHighAndLowFrequencies:<JSON>`
- `setPresetEq:<JSON>`
- `setParameterEq:<JSON>`
- `getEqInfo:<eqType>`
- `addCustomEqInfo:<JSON>`
- `delCustomEqInfo:<JSON>`

Documented EQ mode values: 0000 off; 0001 high/low; 0010 preset; 0011 high/low+preset; 0100 parameter; 0101 parameter+high/low. Bass/Treble range -5..5. Preset bands -12..12. Parametric EQ supports up to 10 points, filters PK/LS/HS/LP/HP/OFF, frequency 20..24000 Hz, Q 0..30, gain -12..12 dB.

### System / device
- `reboot`
- `factory`
- `shutdown`
- `setPlayerCmd:devicename:<name>`

## Verification state for this historical chat

- Official API syntax and documented semantics: **DOCUMENTED**.
- airCloudCTRL v0.1 API catalogue/transport implementation: **IMPLEMENTED (historical)**.
- Device command execution in this chat: **NOT TESTED**.
- Desktop development environment startup: **TESTED**, Vite 6.4.3 served on localhost:5173 and Electron launched.
- Later hardware confirmations must be linked from later chat/test evidence rather than retroactively promoted here.
