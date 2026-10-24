# Master Command Registry

Historical canonical record sequence before the 4STREAM increment: **1–634**. Current sequence endpoint: **642** (see the increment below; retained shard row counts differ).

- v0.4.8 baseline: records **1–204**
- saved-chat audit increment: records **205–214**
- current-chat/A33M V1.2 normalization: records **215–221**
- official Arylic A31 TCP API expansion: records **222–258**
- official Arylic A31 UART runtime API: records **259–316**
- A33M V1.2 full 36-page audit: record **317** (getEqSwitch; all other 62 API entries reuse existing canonical IDs)
- full `CHAT-AIRCONTROL-ORIGIN` audit: records **318–325** (transport/topology rules, A98 artwork, discovery truth, DLNA behavior, playback ownership, family separation, A31 UPnP seek hardware evidence)

- WiiM/Linkplay OpenAPI v1.2.0 full-source diff: records **326–634** (309 new source-documented commands; 36 existing command paths reused; generic Swagger helper excluded). A97/A98 applicability is candidate until hardware-tested.

The CSV shards under `registry/records/` are the lossless source table, while usable canonical views are distributed into device, protocol and function sections.

Vendor documentation is documentary evidence only. Commands are promoted to CAPTURED/CONFIRMED only by corresponding device/capture evidence.

Original record IDs and evidence statuses are preserved. Do not renumber IDs or silently promote evidence levels.

## 4STREAM APK source increment — 2026-10-24
Historical record sequence **635–642** adds eight source/routing records in [635-642.csv](records/635-642.csv); current sequence endpoint is **642**. The 142 source builder observations are not 142 new commands. Existing command IDs and hardware evidence remain unchanged.
The earlier 634 figure denotes the historical record sequence, not a deduplicated total over every retained shard (215-220.csv and 215-221.csv overlap historically). No historical rows are renumbered or removed here.
See [canonical 4STREAM report](../protocols/linkplay-http-https/4STREAM-2026-10-24.md).
