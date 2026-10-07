# TCP :8819 correction/addendum

A second focused review of `wiim-tcp8819-protocol.txt` corrected and expanded the earlier CHAT-AUDIT-03 notes.

Canonical interpretation:
- :8819 is explicitly known to WiiM Home through `Socket8819CommThread` / `connectTCP8819`.
- The recovered exchange is a network throughput/connectivity diagnostic.
- Probe JSON is `{"action":"1888"}`.
- Socket timeout is 10000 ms; read target is 4096 bytes.
- Result fields are connected/duration/size/speed.
- DeviceReportNetStatus has a 20000 ms aggregate protection timeout.
- `us5.b()` fallback to 59152 is generic connectivity behavior and must not be described as protocol-level TCP8819 fallback.
- Header byte order remains unresolved because `vob.a()` and `mg0.f()` have not yet been decoded.
