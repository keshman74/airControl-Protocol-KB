# Research Chat Registry

This registry links research conversations to the canonical KB. A chat is **provenance/evidence**, never a parallel command database.

## Rule
When a research chat discovers or tests something:
1. assign/update the canonical `CMD/QRY/EVT/PROTO/RULE/TEST/CAP/REV` record;
2. update device/protocol/function/service views;
3. record request/response or capture evidence;
4. link that canonical ID back to its `CHAT-*` source here and in `evidence/chat-audits/`;
5. promote evidence status only to the level actually proven.

## Linked chats

| Chat ID | Conversation / source | Primary scope | Canonical objects / areas |
|---|---|---|---|
| CHAT-AIRCONTROL-ORIGIN | **Приложение управления устройствами** (started 2026-09-11) | Original airCloudCTRL/airControl requirements; CLOUDYX; CS2/ADAmp/ACAmp official API; iAudioCloud app manual; initial architecture; later hardware/application recovery notes | `PROTO-ACS2-HTTP`, `PROTO-ACS2-HTTPS`; ACS2 playback/network/EQ/USB/Bluetooth/Multiroom families; records 318–325 from full-chat audit: Linkplay transport/topology rules, A98 artwork, discovery online truth, DLNA queue behavior, local-library ownership, multiroom family separation, A31 UPnP REL_TIME seek evidence. See `CHAT-AUDIT-04-ORIGIN-FULL.md`. |
| CHAT-AIRCONTROL-300926 | **Продолжение разработки airControl 300926** | WiiM Home reverse engineering, UPnP/PlayQueue, Qobuz, SMB/Samba, transport research, TCP :8819, network/status paths | `QRY-UPNP-STREAM-CAPABILITY`, PlayQueue records, TCP8819 records, QueueContext/PlayList XML, StreamCapability, Qobuz capability gates, network/status reverse engineering. Evidence split across CHAT-AUDIT-01/03 and later normalized audits. |
| CHAT-AIRCONTROL-041026 | **Продолжение разработки airControl 041026** | A31 gateway/native volume behavior; further WiiM/UPnP audit; PlayQueue/RenderingControl SCPD; services/capabilities | `CMD-A31-HTTP-VOL-UP-REL`, `CMD-A31-HTTP-VOL-DOWN-REL`, `QRY-A31-MCU-VOLUME-NATIVE`; PlayQueue/RenderingControl/StreamCapability canonical records and reverse-engineering evidence. |
| CHAT-A33-PRESETS | **A33/A33M preset research/test chat** — existing dedicated research conversation; exact conversation URL/ID to be recorded when recovered from its saved chat/export | A33M native 12-slot Preset API and subsequent hardware tests | `CMD-A33M-PRESET-ADD`, `CMD-A33M-PRESET-CHOICE`, `CMD-A33M-PRESET-PREV`, `CMD-A33M-PRESET-NEXT`, `CMD-A33M-PRESET-MOVE`, `CMD-A33M-PRESET-DELETE`, `QRY-A33M-PRESET-LIST`. Current source status: official-document DOCUMENTED; hardware tests belong here and will promote individual records. |
| CHAT-A33-NATIVE | A33 native protocol research (conversation identity to be recovered from chronological audit) | TCP :1234 control/state; TCP :23040 native framing/seek/service context | `CMD-A33-PLAY`, `CMD-A33-PAUSE`, `CMD-A33-NEXT`, `CMD-A33-PREV`, `CMD-A33-VOLUME`, `CMD-A33-MUTE-ON`, `CMD-A33-SEEK`, A33 TuneIn/Qobuz context events. |
| CHAT-A31-MCU | A31 native/gateway research (conversation identity to be recovered from chronological audit) | TCP :8899 MCU control/state/EQ/volume and HTTP fallback | `PROTO-MCU-8899`, `MCU+VOL+NNN`, `MCU+VOL+GET`, playback/mute/key commands, AXX responses/events. |
| CHAT-WIIM-PLAYQUEUE | WiiM Home/PlayQueue research; currently provenance overlaps CHAT-AIRCONTROL-300926/041026 | PlayQueue SCPD, QueueContext, local/media-server playback, Qobuz queue execution | `PROTO-UPNP-PLAYQUEUE-ENDPOINT`, Create/Replace/Append/Browse/Delete/Backup/PlayQueueWithIndex/AppendTracksInQueueEx and related SCPD actions. |
| CHAT-TCP8819 | TCP :8819 focused research; currently provenance overlaps CHAT-AIRCONTROL-300926 | WiiM Home network diagnostic/performance channel | `PROTO-TCP8819-DIAGNOSTIC`, framing, `{"action":"1888"}`, measurement/result behavior, generic 59152 connectivity rule. |

| PRJ-KNX-LINKPLAY-GATE | **KNX to LinkPlay Gate** — ChatGPT Project: https://chatgpt.com/g/g-p-6aab13e5b4888191ad6f6648251277cb-knx-to-linkplay-gate/project | KNX→Linkplay/airScope/airCloud gateway research and implementation; mapping KNX group events to device-control protocols; A31/A97/A98/A33 integration | Links gateway implementation/tests to canonical Linkplay HTTP/HTTPS, MCU :8899, ACS2/A33, discovery, playback, volume, mute, sources, presets and multiroom records. Individual chats inside this project should receive their own `CHAT-*` entries as they are audited. |

| CHAT-SHARE-6AC59E5A | Shared ChatGPT conversation — https://chatgpt.com/share/6ac59e5a-ab1c-83eb-87d8-a010d7763d0a | Research/evidence source; exact title and protocol scope pending content recovery/audit | Link preserved now. Canonical IDs will be attached after the conversation content is recovered and audited; no technical claims are inferred from the URL alone. |

| CHAT-CURRENT-KB-INTEGRATION | **Current airControl-Protocol-KB integration conversation** (2026-10-07) | KB normalization, chat/project provenance linking, A33M V1.2 preset extraction, TCP :8819 correction | Records 215–221; A33M preset family; correction of generic TCP 59152 rule; KB provenance policy. Hardware preset testing intentionally deferred to the dedicated A33 preset research chat. |

## Project containers

A ChatGPT Project is a provenance container, not a technical record. Its child research chats are linked individually to canonical IDs when audited. `PRJ-KNX-LINKPLAY-GATE` is the first explicitly linked project container.

## Identity policy
Never invent a ChatGPT conversation URL or UUID. If an exact URL/ID is present in a saved HTML/export, record it. Otherwise keep the descriptive chat identity and mark URL/ID recovery pending.

## Bidirectional-link policy
Every future hardware test should carry:
- canonical record ID;
- `CHAT-*` source;
- device/chip/model and firmware when known;
- transport/port;
- exact request;
- exact response/capture;
- result/status;
- date/evidence artifact.

This makes both directions navigable: **chat → canonical records** and **canonical record → chat/evidence**.
