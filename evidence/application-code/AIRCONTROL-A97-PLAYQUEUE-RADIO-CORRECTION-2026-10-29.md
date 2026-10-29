# A97/H50 Non-HTTPS radio: use PlayQueue, not MCU play

**Status:** Arylic-forum-protocol documented; airControl change implemented in v5.0.12-rc1; **NOT-HW-VERIFIED** on this user's H50/A97. The user tested v5.0.11 and reported: the red error disappeared, but playback still did not start.

## The correction

The H50 firmware's HTTPAPI is disabled for security. This does not mean that all device control is unavailable: the vendor UPnP services and framed TCP/8899 channel are separate interfaces. For starting a new stream URL, however, Arylic support says a TCP/8899 MCU command cannot do it. Their documented approach is a PlayQueue SOAP sequence:

1. Send `CreateQueue` to the advertised PlayQueue service.
2. Put one radio item in an Arylic Linkplay `<PlayList>` QueueContext. Its fields include `ListName`, `ListInfo/Radio=1`, `SourceName=OnlineMusic`, and `Tracks/Track1` with `URL`, `Source`, and DIDL-Lite `Metadata`.
3. Pass `QueuePolicy=1`.
4. Send `PlayQueueWithIndex` with the same `QueueName` and one-based `Index=1`.

The DIDL-Lite metadata includes the station title, artist, album, stream URL, and artwork URL. The queue context itself is passed as escaped XML inside the SOAP argument; the DIDL-Lite in `Metadata` is escaped as text inside the PlayList XML.

This Arylic radio `<PlayList>` format is distinct from the generic WiiM `<QueueContext><Name>...<Tracks>...</Tracks></QueueContext>` builder documented at [QUEUECONTEXT_XML.md](../../protocols/upnp/QUEUECONTEXT_XML.md). Do not substitute one schema for the other.

## Why the v5.0.11 fix was wrong

v5.0.11 sent `MCU+PLY-PLA` after AVTransport URI/metadata setup. Arylic states that TCP commands cannot initiate playback from a supplied URL. The user's real-device result confirms that this fallback only removed the UI error; it did not start the stream. A successful TCP write is not evidence of audible playback.

## v5.0.12 implementation

airControl v5.0.12-rc1 replaces the UPnP-only radio AVTransport `SetAVTransportURI` + `Play` path with the vendor PlayQueue flow above. It uses the PlayQueue control URL and service type discovered from SSDP/description.xml, checks SOAP faults, and reads AVTransport state after the queue action. It does not send HTTPAPI/HTTPS or TCP play commands for this route. API-enabled routes remain on their prior flow.

## Evidence limits

- The user confirms v5.0.11 failed to start playback; this is hardware evidence for that failed implementation only.
- The PlayQueue sequence and wire-level field structure are documented by Arylic forum posts. They are not a packet capture from this device.
- v5.0.12-rc1 playback and native artwork remain **NOT-HW-VERIFIED** pending the user's test.
- Do not change existing A97 HTTPS hardware-confirmed records; the non-HTTPS behavior is a separate transport profile.

## References

- Arylic, [API for the H50](https://forum.arylic.com/t/api-for-the-h50/3832) — HTTPAPI disabled for security; UPnP and TCP/8899 remain available.
- Arylic, [H50 MCU command discussion](https://forum.arylic.com/t/arylic-h50-mcu-command/5026) — TCP cannot execute URL playback; use UPnP PlayQueue.
- Arylic, [HTTP control multiroom & tunein](https://forum.arylic.com/t/http-control-multiroom-tunein/241) — `CreateQueue` radio context followed by `PlayQueueWithIndex`.
- Canonical command details: [UPnP PlayQueue](../../protocols/upnp/playqueue/COMMANDS.md), [A97 commands](../../devices/A97/COMMANDS.md).
