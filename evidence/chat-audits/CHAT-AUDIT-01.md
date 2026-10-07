# CHAT-AUDIT-01

Source: `Продолжение разработки airControl 300926.htm`
Source type: saved ChatGPT research conversation.

## Newly recovered KB objects
- `QRY-UPNP-STREAM-CAPABILITY`
- `CMD-UPNP-PQ-CREATE`
- `CMD-UPNP-PQ-PLAY-INDEX`
- `CMD-UPNP-PQ-APPEND-EX`

## Important source-derived findings
1. WiiM Home invokes `StreamServicesCapability` with `InstanceID` and `AppVersion`
   and receives `StreamCapability`.
2. Recovered CreateQueue chain:
   `LPPlayMediaData -> getPlayData() -> np8.k(...) -> PlayQueue -> CreateQueue`.
3. `QueueContext` is already a prepared XML string when handed to CreateQueue.
4. WiiM Home logs `command=PlayQueue/CreateQueue` on success.
5. The same PlayQueue research exposed `AppendTracksInQueueEx` parameters:
   `QueueContext`, `Action`, `StartIndex`, `Direction`, `Play`.
6. `PlayQueueWithIndex(...)` appears in the Qobuz queue execution chain.

## Evidence boundary
The saved chat explicitly treats `PlayQueue/CreateQueue` as PARTIAL:
the command and QueueContext parameter are established from WiiM Home analysis,
but QueueContext format and A33 hardware operation were not yet confirmed.

The chat copy also indicates that earlier messages were not fully present.
Therefore this audit does not claim completeness for research predating the visible archive.
