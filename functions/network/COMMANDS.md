# Network command view

- `QRY-A31-STATIC-IP` [A31] `getStaticIP` — **CONFIRMED**
- `CMD-A31-DHCP` [A31] `setDhcp:wifi` — **CONFIRMED**
- `CMD-A31-STATIC-IP` [A31] `setStaticIP:{"type":"wifi","ip":"<IP>","mask":"<MASK>","gateway":"<GW>","dns":"<DNS>"}` — **CONFIRMED**
- `QRY-LP-WIFI-STATE` [A31/A97/A98] `wlanGetConnectState` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-SCAN-APS` [A31/A97/A98] `getScanAPs` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-CONNECT-AP` [A31/A97/A98] `connectToAP:<wifiName>:<wifiPassword>` — **DOCUMENTED/IMPLEMENTED**
