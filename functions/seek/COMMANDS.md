# Seek command view

- `CMD-A33-SEEK` [A33] `A3 BF … [ASCII 4<seconds>] … FB` — **CONFIRMED**

- `TEST-A31-UPNP-SEEK-REL-TIME` — **A31 / UPnP AVTransport** — `Seek(Unit=REL_TIME)` — **HARDWARE-VERIFIED**

## iAudioCloud APK evidence — 2026-10-25

Existing CMD-A33-SEEK is clarified by APK source: bytes 00 34 followed by raw decimal position, with LE16 payload byte length. Derived seek30 frame at seq0: A3 BF 00 02 00 00 34 33 30 FB. No new hardware capture.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
