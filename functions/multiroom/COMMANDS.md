# Multiroom command view

- `CMD-LP-MR-JOIN` [A31/A97/A98] `multiroom:JoinGroup:IP=<MASTER_IP>:uuid=<MASTER_UUID>` — **CONFIRMED-A97**
- `CMD-LP-MR-LEAVE` [A31/A97/A98] `multiroom:LeaveGroup` — **CONFIRMED-A97**
- `QRY-LP-MR-SLAVES` [A31/A97/A98] `multiroom:getSlaveList` — **DOCUMENTED**
- `CMD-LP-MR-UNGROUP` [A31/A97/A98] `multiroom:Ungroup` — **DOCUMENTED**
- `CMD-LP-MR-KICK` [A31/A97/A98] `multiroom:SlaveKickout:<ip>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-VOL` [A31/A97/A98] `multiroom:SlaveVolume:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-MUTE` [A31/A97/A98] `multiroom:SlaveMute:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-CHANNEL` [A31/A97/A98] `multiroom:SlaveChannel:<...>` — **DOCUMENTED**
- `CMD-ACS2-MR-HOST` [A33] `multiroom:setHost` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-SLAVE` [A33] `multiroom:setSlave:<host_ip>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-DISCONNECT` [A33] `multiroom:disconnectSlave` — **DOCUMENTED/IMPLEMENTED**
- `CMD-ACS2-MR-BREAK` [A33] `multiroom:breakUp` — **DOCUMENTED/IMPLEMENTED**
- `QRY-ACS2-MR-INFO` [A33] `multiroom:getInformation` — **DOCUMENTED/IMPLEMENTED**
