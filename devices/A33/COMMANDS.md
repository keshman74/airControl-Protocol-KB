# A33 Command View

- `QRY-ACS2-STATUS` — **status** — `getStatusEx` — **DOCUMENTED**
- `CMD-ACS2-USB-PLAY` — **USB** — `playFromUsbDisk` — **DOCUMENTED**
- `QRY-ACS2-USB-LIST` — **USB** — `getUsbSongList` — **DOCUMENTED**
- `CMD-ACS2-USB-SELECT` — **USB** — `selectUsbTracks:<usbSongNum>` — **DOCUMENTED**
- `CMD-ACS2-SOURCE` — **source** — `setPlayerCmd:switchmode:<mode>` — **DOCUMENTED**
- `CMD-ACS2-BT-DISCOVERY` — **Bluetooth** — `setDiscoveryBluetooth:<Open|Close>` — **DOCUMENTED**
- `CMD-ACS2-BT-RESET` — **Bluetooth** — `resetBluetoothPairing` — **DOCUMENTED**
- `CMD-ACS2-BT-CLEAR` — **Bluetooth** — `clearBluetoothPairingList` — **DOCUMENTED**
- `QRY-ACS2-BT-NAME` — **Bluetooth** — `getBluetoothName` — **DOCUMENTED**
- `CMD-ACS2-BT-NAME` — **Bluetooth** — `modifyBluetoothName:<bleName>` — **DOCUMENTED**
- `QRY-ACS2-META` — **metadata** — `getMetaInfo` — **DOCUMENTED**
- `CMD-ACS2-MR-HOST` — **multiroom** — `multiroom:setHost` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-SLAVE` — **multiroom** — `multiroom:setSlave:<host_ip>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-DISCONNECT` — **multiroom** — `multiroom:disconnectSlave` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-BREAK` — **multiroom** — `multiroom:breakUp` — **DOCUMENTED/IMPLEMENTED**
- `QRY-ACS2-MR-INFO` — **multiroom** — `multiroom:getInformation` — **DOCUMENTED/IMPLEMENTED**
- `CMD-A33-PLAY` — **playback** — `{"cmd":"play"}` — **CONFIRMED**
- `CMD-A33-PAUSE` — **playback** — `{"cmd":"pause"}` — **CONFIRMED**
- `CMD-A33-NEXT` — **playback** — `{"cmd":"next"}` — **CONFIRMED**
- `CMD-A33-PREV` — **playback** — `{"cmd":"prev"}` — **CONFIRMED**
- `CMD-A33-VOLUME` — **volume** — `{"cmd":"volume","level":<N>}` — **CONFIRMED**
- `CMD-A33-MUTE-ON` — **mute** — `{"cmd":"mute","state":"on"}` — **CONFIRMED**
- `CMD-A33-SEEK` — **seek** — `A3 BF … [ASCII 4<seconds>] … FB` — **CONFIRMED**
- `EVT-A33-TUNEIN-CONTEXT` — **online service** — `StreamMediaName=tunein + metadata/context` — **CAPTURED**
- `EVT-A33-QOBUZ-CONTEXT` — **online service** — `StreamMediaName=qobuz + metadata/context` — **CAPTURED**
- `QRY-ACS2-PLAYER-STATUS` — **playback/status** — `getPlayerStatus` — **DOCUMENTED**
- `CMD-ACS2-PLAY-URL` — **playback** — `setPlayerCmd:play:<url>` — **DOCUMENTED**
- `CMD-ACS2-PLAYLIST` — **playback** — `setPlayerCmd:playlist:<songid>` — **DOCUMENTED**
- `CMD-ACS2-PAUSE` — **playback** — `setPlayerCmd:pause` — **DOCUMENTED**
- `CMD-ACS2-RESUME` — **playback** — `setPlayerCmd:resume` — **DOCUMENTED**
- `CMD-ACS2-TOGGLE` — **playback** — `setPlayerCmd:onepause` — **DOCUMENTED**
- `CMD-ACS2-PREV` — **playback** — `setPlayerCmd:prev` — **DOCUMENTED**
- `CMD-ACS2-NEXT` — **playback** — `setPlayerCmd:next` — **DOCUMENTED**
- `QRY-ACS2-POSITION` — **playback** — `setPlayerCmd:getplay:<seconds>` — **DOCUMENTED**
- `CMD-ACS2-SEEK-HTTP` — **playback** — `setPlayerCmd:setplay:<seconds>` — **DOCUMENTED**
- `CMD-ACS2-STOP` — **playback** — `setPlayerCmd:stop` — **DOCUMENTED**
- `CMD-ACS2-VOLUME` — **volume** — `setPlayerCmd:vol:<value>` — **DOCUMENTED**
- `CMD-ACS2-VOL-UP` — **volume** — `setPlayerCmd:RemoteVol++` — **DOCUMENTED**
- `CMD-ACS2-VOL-DOWN` — **volume** — `setPlayerCmd:RemoteVol--` — **DOCUMENTED**
- `CMD-ACS2-MUTE` — **mute** — `setPlayerCmd:mute:<mute>` — **DOCUMENTED**
- `CMD-ACS2-MAX-VOLUME` — **volume** — `setPlayerCmd:maximumVolume:<maximumVolume>` — **DOCUMENTED**
- `CMD-ACS2-CHANNEL` — **playback** — `setChannel:<channel>` — **DOCUMENTED**
- `CMD-ACS2-PROMPT-TONE` — **device** — `setPlayerCmd:prompttone:<prompt_tone>` — **DOCUMENTED**
- `CMD-ACS2-LOOP` — **playback** — `setPlayerCmd:loopmode:<loopmode>` — **DOCUMENTED**
- `CMD-ACS2-REBOOT` — **system** — `reboot` — **DOCUMENTED**
- `CMD-ACS2-FACTORY` — **system** — `factory` — **DOCUMENTED**
- `CMD-ACS2-SHUTDOWN` — **system** — `shutdown` — **DOCUMENTED**
- `CMD-ACS2-DEVICE-NAME` — **device** — `setPlayerCmd:devicename:<devicename>` — **DOCUMENTED**
- `QRY-ACS2-WIFI-STATE` — **network** — `wlanGetConnectState` — **DOCUMENTED**
- `QRY-ACS2-SCAN-APS` — **network** — `getScanAPs` — **DOCUMENTED**
- `CMD-ACS2-CONNECT-AP` — **network** — `connectToAP:wifiName:<name>:wifiPassword:<password>` — **DOCUMENTED**
- `CMD-ACS2-PROMPT-DOWNLOAD` — **prompt sound** — `downloadPromptSound:<audioFileName>` — **DOCUMENTED**
- `CMD-ACS2-PROMPT-PLAY` — **prompt sound** — `playPromptSound:<audioName>:<volume>` — **DOCUMENTED**
- `QRY-ACS2-PROMPT-SERVER` — **prompt sound** — `viewServerPromptSound` — **DOCUMENTED**
- `QRY-ACS2-PROMPT-DEVICE` — **prompt sound** — `viewDevicePromptSound` — **DOCUMENTED**
- `CMD-ACS2-PROMPT-DELETE` — **prompt sound** — `deleteSpecifiedAudio:<audioPath>` — **DOCUMENTED**
- `CMD-ACS2-STATIC-SWITCH` — **network** — `setNetIPSwitchState:<switch>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-STATIC-IP` — **network** — `setStaticIP:<staticIPInfo JSON>` — **DOCUMENTED/IMPLEMENTED**

## A33M preset API — official V1.2

- `CMD-A33M-PRESET-ADD` — `oneClickPreset:{"PresetNumber":"x","Overwrite":"yes|no"}` — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `CMD-A33M-PRESET-CHOICE` — `choicePreset:<1..12>` — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `CMD-A33M-PRESET-PREV` — `playPreviousPreset` — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `CMD-A33M-PRESET-NEXT` — `playNextPreset` — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `CMD-A33M-PRESET-MOVE` — `movePresetPosition:{"OldIndex":"x","NewIndex":"x"}` — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `CMD-A33M-PRESET-DELETE` — `deletePreset:<0..12>` (0 clears all) — **DOCUMENTED / NOT-YET-HW-VERIFIED**
- `QRY-A33M-PRESET-LIST` — `getPresetListInfo` — **DOCUMENTED / NOT-YET-HW-VERIFIED**

## A33M V1.2 full-manual audit
All **63/63** API entries in sections 3.1–3.13 are mapped in `protocols/acs2/A33M-V1.2-COMPLETE.md`. Previously missing canonical entry:
- `QRY-A33M-EQ-SWITCH` — `getEqSwitch` — **DOCUMENTED / OFFICIAL-A33M-V1.2 / NOT-YET-HW-VERIFIED**.
