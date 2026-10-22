# UPnP PlayQueue — CHAT-AUDIT-01

## Evidence status
Recovered from the saved airControl research chat and its discussion of decompiled WiiM Home sources.
These actions are **not yet hardware-confirmed for A33/A97/A98**.

## CreateQueue
`PlayQueue/CreateQueue(QueueContext)`

Recovered call chain:

```text
LPPlayMediaData
  -> getPlayData()
  -> np8.k(String, Device, callback)
  -> PlayQueue service
  -> CreateQueue
  -> QueueContext = prepared XML string
```

Observed WiiM Home success log marker:

```text
command=PlayQueue/CreateQueue
```

Status: `PARTIAL / SOURCE-CONFIRMED / NOT-HW-VERIFIED`

Unknowns intentionally preserved:
- exact QueueContext XML schema
- Qobuz ID/token/URL representation
- exact SOAP endpoint/service URN
- response payload
- A33/A97/A98 support

## PlayQueueWithIndex
`PlayQueueWithIndex(...)`

Found in the recovered Qobuz -> queue -> PlayQueue execution chain.
Exact arguments were not established in this chat copy.

Status: `SOURCE-CONFIRMED / NOT-HW-VERIFIED`

## AppendTracksInQueueEx
`AppendTracksInQueueEx(QueueContext, Action, StartIndex, Direction, Play)`

Known parameter names:
- QueueContext
- Action
- StartIndex
- Direction
- Play

Status: `SOURCE-CONFIRMED / NOT-HW-VERIFIED`

Do not invent parameter value domains or device compatibility until captured/tested.


## GetKeyMapping — A97 hardware-confirmed read
The tested A97 supports advertised GetKeyMapping on both HTTP49152 and59152. See [A97 presets readback and limits](A97-PRESETS.md). This confirmation is specific to GetKeyMapping; it does not promote the other actions above to hardware-confirmed status.


## CMD-UPNP-PQ-MOVE-TRACKS

`MoveTracksInQueue(QueueName, IndexList, ToIndex)` — APK-VERIFIED / NOT-HW-ACTION-VERIFIED. [Recovered callback](../../communication-8819/CHAT-AUDIT-03.md). Не является подтверждением исполнения на всех A31/A97/A98.
