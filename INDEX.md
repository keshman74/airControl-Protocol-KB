# INDEX

Canonical knowledge is organized by **device**, **protocol**, and **function**. Audit files are evidence/provenance only; no technical finding may exist only in an audit index.

## Devices
- [A31](devices/A31/README.md) · [commands](devices/A31/COMMANDS.md) · [native KNX (hardware confirmed)](devices/A31/NATIVE_KNX.md)
- [A97](devices/A97/README.md) · [commands](devices/A97/COMMANDS.md)
- [A98](devices/A98/README.md) · [commands](devices/A98/COMMANDS.md)
- [A33](devices/A33/README.md) · [commands](devices/A33/COMMANDS.md)

## Canonical registries
- [Commands](registry/COMMANDS.md)
- [Devices](registry/DEVICES.md)
- [Protocols](registry/PROTOCOLS.md)
- [Services](registry/SERVICES.md)
- [Discovery](registry/DISCOVERY.md)
- [Fast progressive zone discovery](registry/FAST_ZONE_DISCOVERY.md) — KNOB v0.8.5 user-confirmed baseline
- [Compatibility](registry/COMPATIBILITY.md)
- [Stream capabilities](registry/STREAM_CAPABILITIES.md)
- [KNOB artwork preparation and limits](registry/KNOB_ARTWORK.md)
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

## KNOB integration
- [Responsiveness, background work and resource use](integration/KNOB-RESPONSIVENESS.md) — v0.8.17, host-tested and build-passed; hardware validation pending.
- [RAM and screenshot capture](integration/KNOB-RAM-CAPTURE.md)
- [A98 preset integration](integration/KNOB-A98-PRESETS.md)

## 4STREAM APK research — 2026-10-24
- [Canonical A31/A97/A98 command and routing audit](protocols/linkplay-http-https/4STREAM-2026-10-24.md)
- [142 source builder expressions](protocols/linkplay-http-https/4STREAM-BUILDERS-2026-10-24.md)
- [Provenance and retained evidence](evidence/reverse-engineering/4STREAM-2026-10-24.md)
- [Eight source/routing records, sequence 635–642](registry/records/635-642.csv)
Static evidence only; device hardware statuses are unchanged.

## iAudioCloud A33 native audit — 2026-10-25

- [Detailed native command analysis](protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md)
- [141 opcode constants and 109 send-site observations](protocols/a33-native-23040/IAUDIOCLOUD-OPCODES-2026-10-25.md)
- [Evidence and reproducibility](evidence/reverse-engineering/IAUDIOCLOUD-2026-10-25.md)

Discovery, framing, presets, EQ/RoomFit/subwoofer and firmware-dependent volume; APK evidence only. Existing hardware confirmation is retained separately.


## 4STREAM AirPlay metadata/artwork audit — 2026-10-25

- [Canonical metadata-to-ImageView report](protocols/linkplay-http-https/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md)
- [Provenance and reproduction selectors](evidence/reverse-engineering/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md)
- [REA and DEX evidence](evidence/reverse-engineering/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.json)
- [Six aggregate source/rule records, sequence 651–656](registry/records/651-656.csv)

Static evidence: AirPlay is recognized from PlayMedium; relative /data artwork is not expanded; full HTTP/S artwork URLs are fetched verbatim. Status **APK-VERIFIED / NOT-HW-VERIFIED**. Existing hardware-confirmed facts are unchanged.


## WiiM Home Room Correction static audit — 2026-10-28
- [Canonical Room Correction function notes](functions/room-correction/COMMANDS.md#wiim-home-apk-static-implementation-findings-2026-10-28)
- [APK/native reverse-engineering report](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-3.6.10-2026-10-28.md)

Static evidence only. Status **APK-VERIFIED / NOT-HW-VERIFIED**; existing device hardware statuses are unchanged.
