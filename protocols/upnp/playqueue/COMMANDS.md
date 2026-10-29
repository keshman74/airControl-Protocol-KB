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


## Arylic Linkplay internet radio queue — forum documented, 2026-10-29

**Status: ARYLIC-FORUM-DOCUMENTED / NOT-HW-VERIFIED on the user's H50/A97.** This is a distinct schema from the WiiM PlayQueue generic `<QueueContext><Name>…` form in [QUEUECONTEXT_XML.md](../QUEUECONTEXT_XML.md). Do not merge the two formats.

Arylic staff's H50 guidance says URL playback is started with UPnP PlayQueue, not by sending a URL over TCP/MCU. Their radio example uses the advertised `urn:schemas-wiimu-com:service:PlayQueue:1` endpoint and the following sequence:

1. `CreateQueue(QueueContext, QueuePolicy)`
   - `QueueContext` is an XML-escaped Linkplay legacy `<PlayList>` document.
   - The playlist contains `ListInfo/Radio=1`, `SourceName=OnlineMusic`, `TrackNumber=1`, and `Tracks/Track1/URL`, `Source`, `Metadata`.
   - `Metadata` contains escaped DIDL-Lite for the radio item.
   - Arylic's example uses `QueuePolicy=1`.
2. `PlayQueueWithIndex(QueueName, Index=1)`, using the same queue name declared in the `PlayList`.

The control URL must be taken from the device's UPnP description; do not assume a fixed port/path. Use cleartext HTTP SOAP where the device advertises an HTTP control endpoint. This evidence does not establish exact firmware compatibility, accepted stream codecs/MIME types, or successful playback on every H50/A97.

Sources:
- [Arylic H50 MCU command discussion](https://forum.arylic.com/t/arylic-h50-mcu-command/5026) — Arylic staff says TCP MCU cannot start a URL and points to UPnP CreateQueue/PlayQueueWithIndex.
- [Arylic H50 API discussion](https://forum.arylic.com/t/api-for-the-h50/3832/14) — HTTPAPI disabled for security; UPnP and TCP/8899 remain available.
- [Arylic radio PlayQueue example](https://forum.arylic.com/t/http-control-multiroom-tunein/241) — SOAP action/argument example and legacy radio PlayList QueueContext.

The user's latest report says v5.0.11's `MCU+PLY-PLA` fallback removed the red error but did not start playback. This is direct evidence that the prior fallback was insufficient in that run, not proof of PlayQueue success. v5.0.12 implementation is documented separately and remains NOT-HW-VERIFIED pending user playback confirmation.


## H50 `newTuneIn` queue — captured acceptance 2026-10-29

**CAPTURE-OBSERVED HTTP 200 responses on the tested H50** for `CreateQueue` and `PlayQueueWithIndex` using the `newTuneIn` schema below. This observation does **not** verify audible playback or the separate direct-URL `OnlineMusic` schema above.

Existing `/private/tmp/wiim-a97.pcap` (SHA-256 `71aaebfc2987d0bd99e47e75d0191ea9eb7c6f528acb9a87b69d3947ffa03fb4`) records requests to `192.168.0.100:59152/upnp/control/PlayQueue1` at 14:18:23 local. `CreateQueue` used `QueuePolicy=0`; its escaped `PlayList` had `ListName=Kiss FM Ukraine`, `SourceName=newTuneIn`, `TrackNumber=0`, `SearchUrl` pointing to a TuneIn profile media endpoint, `Radio=0`, `ContentType=radio`, `PicUrl`, and empty `Tracks`. `PlayQueueWithIndex` used the same name and `Index=1`. Both returned HTTP 200 SOAP action responses.

See [packet-level evidence and 4STREAM static URL path](../../evidence/captures/H50-PLAYQUEUE-NEW-TUNEIN-2026-10-30.md). Keep this specific observed queue distinct from the older Arylic direct-stream example (`OnlineMusic`, `Radio=1`, one `Track1/URL`, `QueuePolicy=1`).

## H50 direct-URL queue limitation and alternate AVTransport Play (2026-10-30)

The user's H50 returned `socket hang up` for v5.0.13 `OnlineMusic` `PlayQueueWithIndex`, remained `STOPPED`, and did not show station artwork. This is a negative hardware observation, so the older Arylic forum direct-URL queue example is **not H50-verified**. A 653-packet Mac/H50 capture then showed a working different path: airControl `SetAVTransportURI` to TCP/49152 supplied RTL URI and DIDL artwork; WiiM Home sent `AVTransport#Play` to TCP/59152 with `<ControlSource>WiiMApp</ControlSource>` and `Connection: keep-alive`; the H50 returned HTTP 200 and entered `PLAYING`. The causal contribution of port, control-source field and keep-alive is not isolated. [Full capture report](../../../evidence/captures/H50-RTL-DUAL-UPNP-PLAY-2026-10-30.md).
