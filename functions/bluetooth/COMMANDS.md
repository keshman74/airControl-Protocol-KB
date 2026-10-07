# Bluetooth command view

- `CMD-ACS2-BT-DISCOVERY` [A33/ACS2] `setDiscoveryBluetooth:<Open|Close>` — **DOCUMENTED**
- `CMD-ACS2-BT-RESET` [A33/ACS2] `resetBluetoothPairing` — **DOCUMENTED**
- `CMD-ACS2-BT-CLEAR` [A33/ACS2] `clearBluetoothPairingList` — **DOCUMENTED**
- `QRY-ACS2-BT-NAME` [A33/ACS2] `getBluetoothName` — **DOCUMENTED**
- `CMD-ACS2-BT-NAME` [A33/ACS2] `modifyBluetoothName:<bleName>` — **DOCUMENTED**


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `CMD-WIIM-START-BT-DISCOVERY` — `startbtdiscovery:{n}` — Start Bluetooth device scan — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-BT-DISCOVERY-RESULT` — `getbtdiscoveryresult` — Get Bluetooth device scan result — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-CLEAR-BT-DISCOVERY-RESULT` — `clearbtdiscoveryresult` — Clear Bluetooth device scan result — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-BT-HISTORY` — `getbthistory` — Get paired Bluetooth devices — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-CONNECT-BT-A2DPSYNK` — `connectbta2dpsynk:{BT_MAC_ADDRESS}` — Connect to a Bluetooth device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-DISCONNECT-BT-A2DPSYNK` — `disconnectbta2dpsynk:{BT_MAC_ADDRESS}` — Disconnect from a Bluetooth device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-BT-PAIR-STATUS` — `getbtpairstatus` — Get Bluetooth pairing status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-CONNECTBTA2DPSOURCE` — `connectbta2dpsource:{str}` — Connect to a Bluetooth source device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-DELBTHISTORY` — `delbthistory:{str}` — Delete Bluetooth history — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-BTDISCONNECTALL` — `btdisconnectall` — Disconnect all Bluetooth devices — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GETBT-PAIR-DEV-STAT` — `getbtPairDevStat` — Get Bluetooth pair device status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GETBTSTATUS` — `getbtstatus` — Get Bluetooth status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STARTBTSERVER` — `startbtserver` — Start Bluetooth server — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STARTGETBT-PAIR-DEV-STAT` — `startgetbtPairDevStat` — Start getting Bluetooth pair device status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STOPBTDISCOVERY` — `stopbtdiscovery` — Stop Bluetooth discovery — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STOPBTSERVER` — `stopbtserver:{n}` — Stop Bluetooth server — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-BTAVKENTERPAIR` — `btavkenterpair` — Enter Bluetooth pairing mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-BLEHIDPAIR` — `blehidpair:{str}` — Pair with a BLE HID device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-BLEHIDREMOVEALL` — `blehidremoveall` — Remove all paired BLE HID devices — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-BTRECOVERY` — `btrecovery` — Recovery Bluetooth — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-BLE-HID-STATUS` — `getblehidstatus` — Get BLE HID status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-START-BLE-SCAN` — `startblescan:{n}` — Start BLE scan — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-BLE-DISCOVERY-RESULT` — `getblediscoveryresult` — Get BLE discovery result — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
