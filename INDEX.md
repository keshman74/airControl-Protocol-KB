# INDEX

Canonical knowledge is organized by **device**, **protocol**, and **function**. Audit files are evidence/provenance only; no technical finding may exist only in an audit index.

## Devices
- [A31](devices/A31/README.md) · [commands](devices/A31/COMMANDS.md)
- [A97](devices/A97/README.md) · [commands](devices/A97/COMMANDS.md)
- [A98](devices/A98/README.md) · [commands](devices/A98/COMMANDS.md)
- [A33](devices/A33/README.md) · [commands](devices/A33/COMMANDS.md)

## Canonical registries
- [Commands](registry/COMMANDS.md)
- [Devices](registry/DEVICES.md)
- [Protocols](registry/PROTOCOLS.md)
- [Services](registry/SERVICES.md)
- [Discovery](registry/DISCOVERY.md)
- [Compatibility](registry/COMPATIBILITY.md)
- [Stream capabilities](registry/STREAM_CAPABILITIES.md)
- [Behavior rules](registry/BEHAVIOR_RULES.md)
- [Transport detection](registry/TRANSPORT_DETECTION.md)
- [Reverse engineering](registry/REVERSE_ENGINEERING.md)

## Protocols
- [Linkplay HTTP/HTTPS](protocols/linkplay-http-https/COMMANDS.md)
- [MCU TCP :8899](protocols/mcu-8899/COMMANDS.md)
- [Communication :8819](protocols/communication-8819/COMMANDS.md)
- [ACS2](protocols/acs2/COMMANDS.md)
- [A33 JSON :1234](protocols/a33-json-1234/COMMANDS.md)
- [A33 native :23040](protocols/a33-native-23040/COMMANDS.md)
- [UPnP canonical view](protocols/upnp/COMMANDS.md)
- [PlayQueue](protocols/upnp/playqueue/COMMANDS.md)
- [RenderingControl SCPD](protocols/upnp/RENDERINGCONTROL_SCPD.md)
- [QueueContext XML](protocols/upnp/QUEUECONTEXT_XML.md)
- [WiiM PlayList XML](protocols/upnp/PLAYLIST_XML.md)
- [Remote media server registration](protocols/upnp/PLAYQUEUE_REMOTE_MEDIA_SERVER.md)

## Functions
Playback · Volume · Mute · Sources · EQ · USB · Bluetooth · Metadata · Media Presets · Multiroom · Network · Discovery · Online Services · Device Info · System

Canonical function files are under `functions/*/COMMANDS.md`.

## Research chats
- [Research chat registry](CHATS.md) — bidirectional provenance map from research conversations to canonical records.
- [Chat-to-KB workflow](evidence/chat-audits/README.md)

## Evidence
`evidence/` contains proof and provenance only: hardware tests, captures, official docs, application code, reverse engineering and chat audits. Audit files are **not** a parallel technical index.

## Baseline
v0.4.8 contains **204 canonical records**. Original lossless CSV shards remain under `registry/records/` as an audit-safe baseline.

## Latest normalized audit
- CHAT-AUDIT-03 findings are already promoted into the canonical protocol/function/device structure. Provenance: `evidence/chat-audits/CHAT-AUDIT-03-300926.md`.
