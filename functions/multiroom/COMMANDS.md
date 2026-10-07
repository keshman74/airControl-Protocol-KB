# Multiroom command view

## ACS2 / CS2-ADAmp-ACAmp documented family

Official manual sequence and directionality:

1. `CMD-ACS2-MR-HOST` — `multiroom:setHost` — designate the future master **before adding slaves**.
2. `CMD-ACS2-MR-SLAVE` — `multiroom:setSlave:<host_ip>` — send to the prospective **slave**.
3. `CMD-ACS2-MR-DISCONNECT` — `multiroom:disconnectSlave` — send to the corresponding **slave** to leave the group.
4. `CMD-ACS2-MR-BREAK` — `multiroom:breakUp` — send to the corresponding **master** to break the group.
5. `QRY-ACS2-MR-INFO` — `multiroom:getInformation` — query current multiroom topology/status.

The official response model includes `HostIp`, `MyIp`, `SlaveSum`, device name, volume/mute/version and group data. `getPlayerStatus` distinguishes `standalone`, `master`, and `slave`.

**Evidence state:** DOCUMENTED by the official CS2/ADAmp/ACAmp manual. The first historical airCloudCTRL chat implemented this family in the application catalogue but contains no hardware invocation, so that chat does **not** promote these actions to CONFIRMED.

## Linkplay native multiroom

- `CMD-LP-MR-JOIN`, `CMD-LP-MR-LEAVE` — **CONFIRMED-A97** from later hardware tests.
- `QRY-LP-MR-SLAVES`, `CMD-LP-MR-UNGROUP`, `CMD-LP-MR-KICK`, `CMD-LP-MR-SLAVE-VOL`, `CMD-LP-MR-SLAVE-MUTE`, `CMD-LP-MR-SLAVE-CHANNEL` — **DOCUMENTED** unless a later per-command test record says otherwise.

Do not merge Linkplay native multiroom with the ACS2 command family merely because both implement Master/Slave grouping.

## UPnP RenderingControl candidates

- `QRY-UPNP-RC-SIMPLE-DEVICE-INFO`
- `QRY-UPNP-RC-CONTROL-DEVICE-INFO`
- `CMD-UPNP-RC-MULTIPLAY-SLAVE-MASK`

Status: **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**.


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `CMD-WIIM-MULTIROOM-SLAVE-MASK` — `multiroom:SlaveMask:{ip}` — Hide the IP address of a LinkPlay — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SLAVE-UN-MASK` — `multiroom:SlaveUnMask:{ip}` — Releasing a Multi-Room Mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-PLAYER-CMD-SLAVE-VOLUME` — `setPlayerCmd:slave_vol:{volume}` — General Volume Adjustment — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-PLAYER-CMD-SLAVE-MUTE` — `setPlayerCmd:slave_mute:mute` — General activation Mute — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-PLAYER-CMD-SLAVE-UNMUTE` — `setPlayerCmd:slave_mute:unmute` — General Mute Disabling — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SLAVE-SET-DEVICE-NAME` — `multiroom:SlaveSetDeviceName:{ip}:{s}` — Individual definition of the device Name — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-MULTIROOM-CONFIG-GET-REALTIME-CACHE-LIMIT` — `multiroom:ConfigGet:realtime_cache_limit` — Get the real-time cache limit — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-CONFIG-SET-REALTIME-CACHE-LIMIT` — `multiroom:ConfigSet:realtime_cache_limit:{value}` — Set the real-time cache limit — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SLAVE-START-WPS` — `multiroom:SlaveStartWPS:{ip}` — Start WPS on a LinkPlay device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-MULTIROOM-GET-NAME-GROUP-LIST` — `multiroom:getnamegrouplist` — Get the list of group names in multi-room mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SLAVE-DEVICE-NAME` — `multiroom:SlaveDeviceName:{ip}:{str}` — Multi-room get slave device name — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SUBWOOFER-FORGET` — `multiroom:subwooferForget:{"uuid":"{uuid}"}` — Multi-room subwoofer forget — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SUBWOOFER-GET-PAIR-INFO` — `multiroom:subwooferGetPairInfo` — Multi-room subwoofer get pair info — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-CONFIG-GET-LEADTIME` — `multiroom:ConfigGet:leadtime` — Multi-room get lead time — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-SUBWOOFER-PAIR` — `multiroom:subwooferPair:{str}` — Multi-room subwoofer pair — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-MULTIROOM-CONFIG-SET-LEADTIME` — `multiroom:ConfigSet:leadtime:{str}` — Multi-room set lead time — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-MRMSUB-LPF` — `setMRMSubLPF:{str}` — Set multiroom subwoofer LPF — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-SUB-LPF` — `getSubLPF` — Get subwoofer LPF — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-SUB-LPF` — `setSubLPF:{str}` — Set subwoofer LPF — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-MRMSUB-LPF` — `getMRMSubLPF:{str}` — Get multi-room sub LPF — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
