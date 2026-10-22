# Protocol Registry

| ID | Device(s) | Transport | Purpose | Status |
|---|---|---|---|---|
| PROTO-LINKPLAY-HTTP | A31 | HTTP :80 | player/status/network/source | CONFIRMED |
| PROTO-LINKPLAY-HTTPS | A97/A98 | HTTPS | Linkplay API | CONFIRMED/PARTIAL |
| PROTO-MCU-8899 | A31 | TCP :8899 | MCU state, EQ, events | CAPTURED/IMPLEMENTED |
| PROTO-COMM-8819 | Linkplay/WiiM; per-device support to test | TCP :8819 | diagnostic/network throughput-connectivity probe; dedicated WiiM Home channel | APK-VERIFIED / NOT-HW-VERIFIED |
| PROTO-ACS2-HTTP | A33 | HTTP :8000 | `/?Instruct=params` | CONFIRMED |
| PROTO-ACS2-HTTPS | A33 | HTTPS :8443 | `/?Instruct=params` | DOCUMENTED |
| PROTO-A33-JSON-1234 | A33 | TCP :1234 | bidirectional JSON state/control | CONFIRMED |
| PROTO-A33-NATIVE-23040 | A33 | TCP :23040 | native commands, seek, service context/metadata | CONFIRMED/CAPTURED |
| PROTO-UPNP | A31/A33 observed | SSDP/UPnP | discovery/rendering | PARTIAL |

| PROTO-WIIM-HTTPAPI | WiiM/Linkplay; A97/A98 candidates | HTTPS :443 | `/httpapi.asp?command=<command>`; self-signed TLS on WiiM | SOURCE-DOCUMENTED / A97-A98 NOT-HW-VERIFIED |


## Scoped follow-up

- PROTO-ACS2-HTTPS: конкретные A33 Prompt-команды HTTPS8443 аппаратно проверены: [test](../docs/airALARM-verified-commands-2026-10-10.md). Общая командная совместимость не доказана.
- RenderingControl A97 HTTP49152 SetVolume/GetVolume: [CONFIRMED scoped](../protocols/upnp/A97-VOLUME.md). Объявление 59152 само по себе не подтверждает SetVolume.
- [Карта потребителей](../KB_CROSS_PROJECT_MAP.md).
