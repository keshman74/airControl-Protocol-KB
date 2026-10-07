# CHAT-AUDIT-02

Source: `Продолжение разработки airControl 041026(1).html`

## New command records
- `CMD-A31-HTTP-VOL-UP-REL`
- `CMD-A31-HTTP-VOL-DOWN-REL`
- `QRY-A31-MCU-VOLUME-NATIVE`

## Recovered A31 volume behavior

### Native TCP absolute volume
The gateway code builds:
`MCU+VOL+%03d`

Example discussed in the chat:
`MCU+VOL+065` = set volume to 65%.

For relative KNX control the gateway:
1. requests current volume with `MCU+VOL+GET` if volume is unknown;
2. waits for `AXX+VOL...`;
3. calculates an absolute target;
4. clamps target to 0..100;
5. sends `MCU+VOL+NNN`.

### Corrected HTTP fallback mapping
Final intended mapping recovered from the chat:

```text
VOL+  -> TCP +5 / HTTP setPlayerCmd:vol++
VOL-  -> TCP -5 / HTTP setPlayerCmd:vol--
```

URL encoded plus command:
`setPlayerCmd:vol%2b%2b`

The chat contains evidence that an earlier gateway build had these HTTP
fallback actions reversed. That old mapping is historical/regression evidence,
not the canonical behavior.

### Rapid-volume behavior
The implementation accumulates pending relative changes and respects
`MIN_COMMAND_INTERVAL_MS` before sending another TCP command.

A stale-state bug near 0% was identified: a second fast command could be
calculated from an old `AXX+VOL` value. The proposed/final code introduces an
optimistic local volume target after successful `MCU+VOL+NNN` transmission,
while a later `AXX+VOL` remains the authoritative device confirmation.

The saved chat shows successful compilation of this change, but does not
contain sufficient final hardware-test evidence to mark the complete rapid
0/100-boundary behavior CONFIRMED.

## Existing records reconfirmed, not duplicated
- A33 TCP :1234 play/pause/next/prev/volume/mute.
- A33 TCP :23040 native seek.
- UPnP PlayQueue `CreateQueue(QueueContext)`.
- `PlayQueueWithIndex(...)`.
- PlayQueue findings remain NOT-HW-VERIFIED for A33/A97/A98 in this chat.

## Important ambiguity
The existing KB contains a captured query variant `MCU+VOL+GET&`.
This chat's gateway source sends `MCU+VOL+GET`.
Do not silently merge them. A fresh wire capture should determine whether
the trailing `&` is part of the MCU payload in one protocol mode or an older
representation.
