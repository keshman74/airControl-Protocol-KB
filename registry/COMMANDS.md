# Master Command Registry

Current canonical ledger: **634 records**.

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
