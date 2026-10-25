# Discovery command view

Discovery is mechanism-oriented rather than a command-only API. Canonical mechanisms are maintained in `registry/DISCOVERY.md` and `registry/TRANSPORT_DETECTION.md`.

- `QRY-UPNP-STREAM-CAPABILITY-EXACT` — runtime capability discovery after UPnP device/service discovery — **APK-VERIFIED + HARDWARE-VERIFIED**
- `PROTO-UPNP-PLAYQUEUE-ENDPOINT` — discover PlayQueue service/controlURL from device description — **APK-VERIFIED + HARDWARE-VERIFIED**

- `DISC-FAST-ZONES-001` — [fast progressive zone discovery](../../registry/FAST_ZONE_DISCOVERY.md) — **CONFIRMED on KNOB v0.8.5 (overall user-reported result)**.
- `RULE-DISCOVERY-NONBLOCKING-001` — separate continuous receipt from bounded network validation; emit results progressively — **IMPLEMENTED + HOST-TESTED**.
- `RULE-DISCOVERY-CANCEL-GENERATION-001` — generation IDs reject late results after stop/restart; select while scanning — **IMPLEMENTED + HOST-TESTED**.

## iAudioCloud APK evidence — 2026-10-25

UDP53308 announcement port is hexadecimal shifted right two bits: 16800 ->23040. Empty port fallback is58803. Status TCPport is parsed as a decimal string; preserve these distinct representations.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
