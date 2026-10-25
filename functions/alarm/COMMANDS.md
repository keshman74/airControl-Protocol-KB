# Alarm clock


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-SET-TIME-SYNC` — `timeSync:{YYYYMMDDHHMMSS}` — Get network time — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ALARM-CLOCK` — `setAlarmClock:{n}:{trig}:{op}:{time}:{day}:{url}` — Set Alarm — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-ALARM-CLOCK` — `getAlarmClock:{n}` —  — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STOP-ALARM-CLOCK` — `alarmStop` — Stop the current alarm — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**

## iAudioCloud APK evidence — 2026-10-25

Native alarm 02 30/32/33/34/35 and sleep/standby 03 40–43 have app-side schemas in the audit; timer units and firmware support remain unverified.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
