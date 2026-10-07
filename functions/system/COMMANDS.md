# System command view

- Linkplay: `CMD-LP-REBOOT`, `CMD-LP-FACTORY`, `CMD-LP-SHUTDOWN` — **DOCUMENTED/IMPLEMENTED**.
- ACS2: `CMD-ACS2-REBOOT`, `CMD-ACS2-FACTORY`, `CMD-ACS2-SHUTDOWN` — **DOCUMENTED**.
- ACS2 prompt sound: `CMD-ACS2-PROMPT-TONE`, `CMD-ACS2-PROMPT-DOWNLOAD`, `CMD-ACS2-PROMPT-PLAY`, `QRY-ACS2-PROMPT-SERVER`, `QRY-ACS2-PROMPT-DEVICE`, `CMD-ACS2-PROMPT-DELETE` — **DOCUMENTED**.
- UPnP sync: `CMD-UPNP-RC-AIRPLAY-AUTOSYNC`, `CMD-UPNP-RC-AUTOSYNC-SUB` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**.


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `CMD-WIIM-SET-SHUTDOWN-TIMER` — `setShutdown:{sec}` — Shutdown — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-SHUTDOWN-TIMER` — `getShutdown` — Get the shutdown timer — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-LED-SWITCH` — `LED_SWITCH_SET:{n}` — Turn on/off status LED ("Status Light" option from app) — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-TOUCH-CONTROLS` — `Button_Enable_SET:{n}` — Turn on/off touch controls — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-BUTTON-ENABLE-GET` — `Button_Enable_GET` — Get button enable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-FIRMWARE-VERSION` — `getFirmwareVersion` — Get firmware version — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-DEVICE-NAME-CHANGEABLE` — `getDeviceNameChangeable` — Get device name changeable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-RESTORE-TO-DEFAULT` — `restoreToDefault` — Restoring the factory setting — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GETSYSLOG` — `getsyslog` — Get system log — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-HEX-DEVICE-NAME` — `setHexDeviceName:{str}` — Set hex device name — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-NO-SEND-MORE-DEVICE-EVENT` — `noSendMoreDeviceEvent:1` — Disable sending more device events — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-HW-ERROR-INFO` — `getHwErrorInfo` — Get hardware error information — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
