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

## WiiM Home Room Correction static audit — 2026-10-28/29
- [Canonical Room Correction function notes](functions/room-correction/COMMANDS.md)
- [End-to-end APK/native report](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-3.6.10-2026-10-28.md)
- [Native DSP reverse-engineering report](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-STATIC-3.6.10-2026-10-29.md)
- [Native DSP call graph](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-CALLGRAPH-2026-10-29.md)
- [Arguments and error codes](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-ARGUMENTS-ERRORS-2026-10-29.md)
- [REA Evidence manifest](evidence/reverse-engineering/WIIM-HOME-ROOM-CORRECTION-DSP-REA-EVIDENCE-MANIFEST-2026-10-29.md)

All static findings are **APK-VERIFIED / NOT-HW-VERIFIED**. Existing device hardware statuses remain unchanged.

## airControl A97/H50 radio playback correction — 2026-10-29
- [v5.0.11 fallback review and user-observed failure](evidence/application-code/AIRCONTROL-A97-NONHTTPS-RADIO-PLAY-FALLBACK-2026-10-29.md)
- [Arylic UPnP PlayQueue correction and v5.0.12 implementation](evidence/application-code/AIRCONTROL-A97-PLAYQUEUE-RADIO-CORRECTION-2026-10-29.md)
- [Canonical UPnP PlayQueue actions and Arylic radio QueueContext evidence](protocols/upnp/playqueue/COMMANDS.md)
- [H50 captured newTuneIn queue and 4STREAM custom URL route](evidence/captures/H50-PLAYQUEUE-NEW-TUNEIN-2026-10-30.md)
- [H50 RTL: SetAVTransportURI on 49152, successful WiiM Home Play on 59152](evidence/captures/H50-RTL-DUAL-UPNP-PLAY-2026-10-30.md)

The user's H50 rejected the direct `OnlineMusic` queue in v5.0.13 (`socket hang up`, state `STOPPED`, no native artwork). A separate 653-packet capture **HW-VERIFIES** that WiiM Home's `Play` over TCP/59152 started the RTL URI and artwork metadata previously set by airControl over TCP/49152. Port, `ControlSource`, and keep-alive differences are recorded; their individual necessity is not isolated. The user tested v5.0.14 RC1 and confirmed RTL audio starts without native-app Play and artwork appears there: **USER-HW-VERIFIED for RTL on this H50**; other stations/devices remain unverified. The v5.0.11 TCP `MCU+PLY-PLA` fallback did not start playback. Existing hardware-confirmed records remain unchanged.


## A31 Rakoit Silent + Native KNX V6E — 2026-10-30
- [Reproducible hardware-verified V6E image/build/boot evidence](evidence/hardware/A31-RAKOIT-SILENT-NATIVE-KNX-V6E-HW-VERIFIED-2026-10-30.md).
- [Canonical A31 Native KNX status and mappings](devices/A31/NATIVE_KNX.md).

**CONFIRMED on spare A31 192.168.0.29:** custom OTA boots with stock playback/SSH/HTTP; delayed boot supervisor autonomously starts v0.11 native KNX even after full power-cycle; MUTE ON/OFF (readback), volume +/−, presets 1–4, PLAY/PAUSE (physical observation). Single tested image SHA-256 `886b13056eb3bc721fffb5c78e921ccb87f6cc46796754ae2202756423aad431`; this is not mass-production certification. Preserve original OTA kernel, SquashFS device nodes, KNX ELF and known-good startup mechanism.

