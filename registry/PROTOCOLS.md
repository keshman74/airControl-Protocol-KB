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
