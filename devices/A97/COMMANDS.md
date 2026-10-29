# A97 Command View

- `CMD-LP-PLAY` — **playback** — `setPlayerCmd:play:<URL>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PLAYLIST` — **playback** — `setPlayerCmd:playlist:<songid>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PAUSE` — **playback** — `setPlayerCmd:pause` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-RESUME` — **playback** — `setPlayerCmd:resume` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-TOGGLE` — **playback** — `setPlayerCmd:onepause` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PREV` — **playback** — `setPlayerCmd:prev` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-NEXT` — **playback** — `setPlayerCmd:next` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-POSITION` — **playback** — `setPlayerCmd:getplay:<seconds>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-SEEK` — **playback** — `setPlayerCmd:setplay:<seconds>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-STOP` — **playback** — `setPlayerCmd:stop` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-VOL-UP` — **volume** — `setPlayerCmd:RemoteVol++` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-VOL-DOWN` — **volume** — `setPlayerCmd:RemoteVol--` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-MAX-VOL` — **volume** — `setPlayerCmd:maximumVolume:<value>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-CHANNEL` — **playback** — `setChannel:<channel>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-LOOP` — **playback** — `setPlayerCmd:loopmode:<loopmode>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-REBOOT` — **system** — `reboot` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-FACTORY` — **system** — `factory` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-SHUTDOWN` — **system** — `shutdown` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-WIFI-STATE` — **network** — `wlanGetConnectState` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-SCAN-APS` — **network** — `getScanAPs` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-CONNECT-AP` — **network** — `connectToAP:<wifiName>:<wifiPassword>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-MR-JOIN` — **multiroom** — `multiroom:JoinGroup:IP=<MASTER_IP>:uuid=<MASTER_UUID>` — **CONFIRMED-A97**
- `CMD-LP-MR-LEAVE` — **multiroom** — `multiroom:LeaveGroup` — **CONFIRMED-A97**
- `QRY-LP-MR-SLAVES` — **multiroom** — `multiroom:getSlaveList` — **DOCUMENTED**
- `CMD-LP-MR-UNGROUP` — **multiroom** — `multiroom:Ungroup` — **DOCUMENTED**
- `CMD-LP-MR-KICK` — **multiroom** — `multiroom:SlaveKickout:<ip>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-VOL` — **multiroom** — `multiroom:SlaveVolume:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-MUTE` — **multiroom** — `multiroom:SlaveMute:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-CHANNEL` — **multiroom** — `multiroom:SlaveChannel:<...>` — **DOCUMENTED**


## A97 Non-HTTPS radio start fallback candidate — 2026-10-29

After airControl v5.0.10 static review, v5.0.11 adds a guarded fallback for the UPnP-only profile: if AVTransport `Play` fails after `SetAVTransportURI` has set radio metadata/artwork, send `MCU+PLY-PLA` over framed TCP/8899 and read transport state. This command is **PROTOCOL-DOCUMENTED / NOT-HW-VERIFIED** on A97/H50; the full source review and user symptom are recorded in [the evidence report](../../evidence/application-code/AIRCONTROL-A97-NONHTTPS-RADIO-PLAY-FALLBACK-2026-10-29.md). Keep existing A97 HTTPS facts unchanged.
