# Discovery Registry

## A33 native UDP beacon — DISC-A33-001
Observed broadcast:
- destination: `255.255.255.255:53308`
- JSON fields: `product_type`, `net`, `host`, `port`, `eth0_mac`, `wlan0_mac`
- observed `product_type`: `EC04`
- observed advertised `port`: `16800`
- status: CAPTURED

Do not assume port 16800 is a control API until separately verified.

## A33 SSDP/UPnP
Observed:
- multicast `239.255.255.250:1900`
- `RenderingControl:1`
- `QPlay:1`
- device description on an HTTP port observed in capture

## A33 mDNS
Observed Spotify Connect advertisement: `_spotify-connect._tcp.local`.

## Global online rule
A persisted/saved device is not automatically Online. Online requires a real discovery or successful status response.

## Fast progressive zone discovery — DISC-FAST-ZONES-001

**CONFIRMED — overall practical result on KNOB v0.8.5, 2026-10-12.** User reports much faster discovery and all expected zones found in the tested LAN. No measured timings or per-chip inventory supplied.

Canonical algorithm, API routing, bounded ESP32 profile, desktop comparison, source references and evidence limits: [FAST_ZONE_DISCOVERY.md](FAST_ZONE_DISCOVERY.md).

Supporting rules: **RULE-DISCOVERY-NONBLOCKING-001** and **RULE-DISCOVERY-CANCEL-GENERATION-001** — IMPLEMENTED + HOST-TESTED. Continuously receive SSDP/LOCATION/NOTIFY and A33 IP hints, queue candidates, validate separately, emit verified zones immediately, bound retries and ignore stale results after cancellation. Cache entries remain hints, not Online evidence.

[Hardware/practical report](../evidence/hardware-tests/KNOB-DISCOVERY-v0.8.5-2026-10-12.md).

## A33 discovery port decoding — APK corroboration

`DeviceTmpModel.getRealPort()` in iAudioCloud 2.0.260728 decodes the announcement port as hexadecimal then shifts right 2 bits: `16800` -> `0x16800 >> 2` -> TCP23040. An absent announcement port falls back to58803. This resolves the earlier warning about the raw value16800: never use it directly as a decimal port. Later status `TCPport` is decimal. This corroborates existing native-preset hardware evidence, without proving one fixed port across all products. [Source audit](../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
