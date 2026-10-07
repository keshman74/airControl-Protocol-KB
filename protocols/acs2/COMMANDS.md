# acs2 commands

## `QRY-ACS2-STATUS`
- **Device:** A33/ACS2
- **Function:** status
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getStatusEx
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-USB-PLAY`
- **Device:** A33/ACS2
- **Function:** USB
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
playFromUsbDisk
```

**Notes:** OK / Not / Error.

## `QRY-ACS2-USB-LIST`
- **Device:** A33/ACS2
- **Function:** USB
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getUsbSongList
```

**Notes:** JSON numbered /udisk paths.

## `CMD-ACS2-USB-SELECT`
- **Device:** A33/ACS2
- **Function:** USB
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
selectUsbTracks:<usbSongNum>
```

**Notes:** OK / Format / Not found / Not / Error.

## `CMD-ACS2-SOURCE`
- **Device:** A33/ACS2
- **Function:** source
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:switchmode:<mode>
```

**Notes:** Modes documented: Network, Bluetooth, LineIn, USBDisk, OpticalIn, HDMIARC, RCAIn, RCA2 In, PHONO In.

## `CMD-ACS2-BT-DISCOVERY`
- **Device:** A33/ACS2
- **Function:** Bluetooth
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setDiscoveryBluetooth:<Open|Close>
```

**Notes:** Bluetooth visibility.

## `CMD-ACS2-BT-RESET`
- **Device:** A33/ACS2
- **Function:** Bluetooth
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
resetBluetoothPairing
```

**Notes:** Reset pairing.

## `CMD-ACS2-BT-CLEAR`
- **Device:** A33/ACS2
- **Function:** Bluetooth
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
clearBluetoothPairingList
```

**Notes:** Reset + clear pairing list.

## `QRY-ACS2-BT-NAME`
- **Device:** A33/ACS2
- **Function:** Bluetooth
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getBluetoothName
```

**Notes:** JSON status response.

## `CMD-ACS2-BT-NAME`
- **Device:** A33/ACS2
- **Function:** Bluetooth
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
modifyBluetoothName:<bleName>
```

**Notes:** Change Bluetooth name.

## `QRY-ACS2-META`
- **Device:** A33/ACS2
- **Function:** metadata
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getMetaInfo
```

**Notes:** Official example includes Title/Artist/Album/Picture/Schedule/Totlen/PlaySource.

## `CMD-ACS2-MR-HOST`
- **Device:** A33
- **Function:** multiroom
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
multiroom:setHost
```

**Notes:** Separate from Linkplay native multiroom.

## `CMD-ACS2-MR-SLAVE`
- **Device:** A33
- **Function:** multiroom
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
multiroom:setSlave:<host_ip>
```

**Notes:** Send to slave.

## `CMD-ACS2-MR-DISCONNECT`
- **Device:** A33
- **Function:** multiroom
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
multiroom:disconnectSlave
```

**Notes:** A33 ACS2.

## `CMD-ACS2-MR-BREAK`
- **Device:** A33
- **Function:** multiroom
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
multiroom:breakUp
```

**Notes:** A33 ACS2.

## `QRY-ACS2-MR-INFO`
- **Device:** A33
- **Function:** multiroom
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
multiroom:getInformation
```

**Notes:** A33 ACS2.

## `QRY-ACS2-EQ-TYPE`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getEqType
```

**Notes:** Official API.

## `CMD-ACS2-EQ-ENABLE`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
eqEnable:<eqSwitch>
```

**Notes:** Official API.

## `CMD-ACS2-EQ-HILO`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setEqHighAndLowFrequencies:{"Bass":"-5..5","Treble":"-5..5"}
```

**Notes:** OK/FAIL/Bass error/Treble error/Error.

## `CMD-ACS2-EQ-PRESET`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPresetEq:<presetInfo JSON>
```

**Notes:** 10-band -12..12.

## `CMD-ACS2-EQ-PARAM`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setParameterEq:<parametInfo JSON>
```

**Notes:** Up to 10 points; filters PK/LS/HS/LP/HP/OFF.

## `QRY-ACS2-EQ-INFO`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getEqInfo:<eqType>
```

**Notes:** Types 1,2,3,22,33 documented.

## `CMD-ACS2-EQ-ADD`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
addCustomEqInfo:<addEqInfo JSON>
```

**Notes:** Custom preset/parameter EQ.

## `CMD-ACS2-EQ-DELETE`
- **Device:** ACS2 devices
- **Function:** EQ
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
delCustomEqInfo:<delEqInfo JSON>
```

**Notes:** Type 2 preset / 3 parameter.

## `QRY-ACS2-PLAYER-STATUS`
- **Device:** A33/ACS2
- **Function:** playback/status
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getPlayerStatus
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PLAY-URL`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:play:<url>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PLAYLIST`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:playlist:<songid>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PAUSE`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:pause
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-RESUME`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:resume
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-TOGGLE`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:onepause
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PREV`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:prev
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-NEXT`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:next
```

**Notes:** Official ACS2 API.

## `QRY-ACS2-POSITION`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:getplay:<seconds>
```

**Notes:** Official ACS2 API; source support restrictions documented.

## `CMD-ACS2-SEEK-HTTP`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:setplay:<seconds>
```

**Notes:** Official ACS2 API; distinct from native TCP :23040 seek.

## `CMD-ACS2-STOP`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:stop
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-VOLUME`
- **Device:** A33/ACS2
- **Function:** volume
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:vol:<value>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-VOL-UP`
- **Device:** A33/ACS2
- **Function:** volume
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:RemoteVol++
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-VOL-DOWN`
- **Device:** A33/ACS2
- **Function:** volume
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:RemoteVol--
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-MUTE`
- **Device:** A33/ACS2
- **Function:** mute
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:mute:<mute>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-MAX-VOLUME`
- **Device:** A33/ACS2
- **Function:** volume
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:maximumVolume:<maximumVolume>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-CHANNEL`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setChannel:<channel>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PROMPT-TONE`
- **Device:** A33/ACS2
- **Function:** device
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:prompttone:<prompt_tone>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-LOOP`
- **Device:** A33/ACS2
- **Function:** playback
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:loopmode:<loopmode>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-REBOOT`
- **Device:** A33/ACS2
- **Function:** system
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
reboot
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-FACTORY`
- **Device:** A33/ACS2
- **Function:** system
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
factory
```

**Notes:** Official ACS2 API; destructive.

## `CMD-ACS2-SHUTDOWN`
- **Device:** A33/ACS2
- **Function:** system
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
shutdown
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-DEVICE-NAME`
- **Device:** A33/ACS2
- **Function:** device
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
setPlayerCmd:devicename:<devicename>
```

**Notes:** Official ACS2 API.

## `QRY-ACS2-WIFI-STATE`
- **Device:** A33/ACS2
- **Function:** network
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
wlanGetConnectState
```

**Notes:** Official ACS2 API.

## `QRY-ACS2-SCAN-APS`
- **Device:** A33/ACS2
- **Function:** network
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
getScanAPs
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-CONNECT-AP`
- **Device:** A33/ACS2
- **Function:** network
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
connectToAP:wifiName:<name>:wifiPassword:<password>
```

**Notes:** Never store real credentials.

## `CMD-ACS2-PROMPT-DOWNLOAD`
- **Device:** A33/ACS2
- **Function:** prompt sound
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
downloadPromptSound:<audioFileName>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PROMPT-PLAY`
- **Device:** A33/ACS2
- **Function:** prompt sound
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
playPromptSound:<audioName>:<volume>
```

**Notes:** Official/API-console spelling normalized from application catalog; verify manual parameter spelling before CONFIRMED.

## `QRY-ACS2-PROMPT-SERVER`
- **Device:** A33/ACS2
- **Function:** prompt sound
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
viewServerPromptSound
```

**Notes:** Official ACS2 API.

## `QRY-ACS2-PROMPT-DEVICE`
- **Device:** A33/ACS2
- **Function:** prompt sound
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
viewDevicePromptSound
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-PROMPT-DELETE`
- **Device:** A33/ACS2
- **Function:** prompt sound
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED`

```text
deleteSpecifiedAudio:<audioPath>
```

**Notes:** Official ACS2 API.

## `CMD-ACS2-STATIC-SWITCH`
- **Device:** A33/ACS2
- **Function:** network
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setNetIPSwitchState:<switch>
```

**Notes:** Official API; airControl uses Disable / W_Enable / E_Enable variants in current code.

## `CMD-ACS2-STATIC-IP`
- **Device:** A33/ACS2
- **Function:** network
- **Transport:** HTTP :8000 or HTTPS :8443
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setStaticIP:<staticIPInfo JSON>
```

**Notes:** Fields W/E StaticIp/Netmask/Gateway documented.
