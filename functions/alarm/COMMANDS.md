# Alarm clock


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-SET-TIME-SYNC` — `timeSync:{YYYYMMDDHHMMSS}` — Get network time — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ALARM-CLOCK` — `setAlarmClock:{n}:{trig}:{op}:{time}:{day}:{url}` — Set Alarm — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-ALARM-CLOCK` — `getAlarmClock:{n}` —  — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-STOP-ALARM-CLOCK` — `alarmStop` — Stop the current alarm — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
