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
