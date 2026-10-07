# linkplay-http-https commands

## `QRY-A31-STATUS-EX`
- **Device:** A31
- **Function:** status
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
getStatusEx
```

**Notes:** Extended device status; exposes uart_pass_port=8899 and communication_port=8819 on tested A31.

## `QRY-A31-PLAYER-STATUS`
- **Device:** A31
- **Function:** playback/status
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
getPlayerStatus
```

**Notes:** status/mode/vol/mute plus hex metadata on tested A31.

## `QRY-A31-METAINFO`
- **Device:** A31
- **Function:** metadata
- **Transport:** HTTP :80
- **Status:** `REJECTED`

```text
getMetaInfo
```

**Notes:** Returned unknown command on tested A31 firmware; do not generalize to A98/A33.

## `CMD-A31-VOLUME`
- **Device:** A31
- **Function:** volume
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:vol:<0..100>
```

**Notes:** Example vol:15 -> Current volume:15%.

## `CMD-A31-MUTE-ON`
- **Device:** A31
- **Function:** mute
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:mute:1
```

**Notes:** Hardware-tested.

## `CMD-A31-MUTE-OFF`
- **Device:** A31
- **Function:** mute
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:mute:0
```

**Notes:** Hardware-tested.

## `CMD-A31-SOURCE-AUX`
- **Device:** A31
- **Function:** source
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:switchmode:AUX%20In
```

**Notes:** Activates AUX In.

## `CMD-A31-SOURCE-USB`
- **Device:** A31
- **Function:** source
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:switchmode:USB%20Disk
```

**Notes:** Activates USB Disk.

## `CMD-A31-SOURCE-LINEIN-AUX`
- **Device:** A31
- **Function:** source
- **Transport:** HTTP :80
- **Status:** `REJECTED`

```text
setPlayerCmd:switchmode:LineIn
```

**Notes:** Did not activate AUX on tested A31.

## `CMD-A31-PLAY-URL`
- **Device:** A31
- **Function:** playback
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setPlayerCmd:play:<URL>
```

**Notes:** Local HTTP MP3 playback confirmed.

## `QRY-A31-USB-LIST`
- **Device:** A31
- **Function:** USB
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
getLocalPlayList
```

**Notes:** JSON locallist; file is HEX -> UTF-8 /media/sda1/...

## `QRY-A31-STATIC-IP`
- **Device:** A31
- **Function:** network
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
getStaticIP
```

**Notes:** Observed wifi=0 Static, wifi=1 DHCP, eth=-1 unavailable.

## `CMD-A31-DHCP`
- **Device:** A31
- **Function:** network
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setDhcp:wifi
```

**Notes:** Response OK.

## `CMD-A31-STATIC-IP`
- **Device:** A31
- **Function:** network
- **Transport:** HTTP :80
- **Status:** `CONFIRMED`

```text
setStaticIP:{"type":"wifi","ip":"<IP>","mask":"<MASK>","gateway":"<GW>","dns":"<DNS>"}
```

**Notes:** JSON command tested; response OK.

## `CMD-LP-PLAY`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:play:<URL>
```

**Notes:** Hardware confirmation exists on A31 for URL playback.

## `CMD-LP-PLAYLIST`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:playlist:<songid>
```

**Notes:** Per-device verification required.

## `CMD-LP-PAUSE`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:pause
```

**Notes:** Per-device evidence required.

## `CMD-LP-RESUME`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:resume
```

**Notes:** Per-device evidence required.

## `CMD-LP-TOGGLE`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:onepause
```

**Notes:** Per-device evidence required.

## `CMD-LP-PREV`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:prev
```

**Notes:** Per-device evidence required.

## `CMD-LP-NEXT`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:next
```

**Notes:** Per-device evidence required.

## `QRY-LP-POSITION`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:getplay:<seconds>
```

**Notes:** Position query form in app command catalog.

## `CMD-LP-SEEK`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:setplay:<seconds>
```

**Notes:** Per-device verification required.

## `CMD-LP-STOP`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:stop
```

**Notes:** Per-device verification required.

## `CMD-LP-VOL-UP`
- **Device:** A31/A97/A98
- **Function:** volume
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:RemoteVol++
```

**Notes:** Per-device verification required.

## `CMD-LP-VOL-DOWN`
- **Device:** A31/A97/A98
- **Function:** volume
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:RemoteVol--
```

**Notes:** Per-device verification required.

## `CMD-LP-MAX-VOL`
- **Device:** A31/A97/A98
- **Function:** volume
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:maximumVolume:<value>
```

**Notes:** Separate from A31 MCU MXV.

## `CMD-LP-CHANNEL`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setChannel:<channel>
```

**Notes:** Stereo/left/right.

## `CMD-LP-LOOP`
- **Device:** A31/A97/A98
- **Function:** playback
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
setPlayerCmd:loopmode:<loopmode>
```

**Notes:** Loop mode.

## `CMD-LP-REBOOT`
- **Device:** A31/A97/A98
- **Function:** system
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
reboot
```

**Notes:** Do not mark hardware-confirmed globally.

## `CMD-LP-FACTORY`
- **Device:** A31/A97/A98
- **Function:** system
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
factory
```

**Notes:** Destructive; hardware evidence not assumed.

## `CMD-LP-SHUTDOWN`
- **Device:** A31/A97/A98
- **Function:** system
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
shutdown
```

**Notes:** Per-device support may vary.

## `QRY-LP-WIFI-STATE`
- **Device:** A31/A97/A98
- **Function:** network
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
wlanGetConnectState
```

**Notes:** Network state.

## `QRY-LP-SCAN-APS`
- **Device:** A31/A97/A98
- **Function:** network
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
getScanAPs
```

**Notes:** Scan Wi-Fi.

## `CMD-LP-CONNECT-AP`
- **Device:** A31/A97/A98
- **Function:** network
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED/IMPLEMENTED`

```text
connectToAP:<wifiName>:<wifiPassword>
```

**Notes:** Credential-bearing; never store real password.

## `CMD-LP-MR-JOIN`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `CONFIRMED-A97`

```text
multiroom:JoinGroup:IP=<MASTER_IP>:uuid=<MASTER_UUID>
```

**Notes:** Hardware-tested on A97; do not claim A31-specific test.

## `CMD-LP-MR-LEAVE`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `CONFIRMED-A97`

```text
multiroom:LeaveGroup
```

**Notes:** Hardware-tested on A97.

## `QRY-LP-MR-SLAVES`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:getSlaveList
```

**Notes:** Native Linkplay multiroom.

## `CMD-LP-MR-UNGROUP`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:Ungroup
```

**Notes:** Native Linkplay multiroom.

## `CMD-LP-MR-KICK`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:SlaveKickout:<ip>
```

**Notes:** Verify exact syntax before CONFIRMED.

## `CMD-LP-MR-SLAVE-VOL`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:SlaveVolume:<...>
```

**Notes:** Exact parameterization requires source-specific entry.

## `CMD-LP-MR-SLAVE-MUTE`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:SlaveMute:<...>
```

**Notes:** Exact parameterization requires source-specific entry.

## `CMD-LP-MR-SLAVE-CHANNEL`
- **Device:** A31/A97/A98
- **Function:** multiroom
- **Transport:** HTTP/S
- **Status:** `DOCUMENTED`

```text
multiroom:SlaveChannel:<...>
```

**Notes:** Exact parameterization requires source-specific entry.
