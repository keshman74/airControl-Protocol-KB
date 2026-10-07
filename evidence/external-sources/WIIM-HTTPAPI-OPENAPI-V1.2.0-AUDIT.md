# WiiM HTTP API OpenAPI v1.2.0 — canonical import audit

Source repository: cvdlinden/wiim-httpapi
Source file: openapi.json
Source blob SHA: 5a1e68e149fee8e45ba80e4d8797d5521650e20c
Source status: community-maintained / work in progress; based on WiiM Products HTTP API v1.2 plus additional sources.

## Coverage
- 346 OpenAPI paths inspected.
- 1 path (/{command}) is a Swagger generic testing helper and was not promoted as a device command.
- 345 real command paths compared against the canonical 325-record ledger.
- 36 matched existing canonical knowledge and were not duplicated.
- 309 were absent and became records 326–634.

## Evidence policy
All newly imported commands are SOURCE-DOCUMENTED / NOT-HW-VERIFIED for A97/A98. Deprecated source endpoints retain DEPRECATED. No source-only command was promoted to CONFIRMED. Existing stronger statuses remain authoritative.

## Distribution
- lossless new-record shard: registry/records/326-634.csv
- full command-by-command source audit: protocols/wiim-httpapi/OPENAPI-V1.2.0-COMPLETE.md
- device candidate views: devices/A97/COMMANDS.md and devices/A98/COMMANDS.md
- function views: device-info, playback, network, eq, system, alarm, presets, audio-output, bluetooth, room-correction, alexa, amazon-music, multiroom, wiim-extended.

## Important source caveat
The source explicitly states that commands may depend on device/model/brand/firmware and that non-WiiM Linkplay products such as Arylic may or may not implement them. Therefore A97/A98 membership here is a test candidate map, not proof of support.
