# airControl v5.0.12: A97/H50 radio playback via UPnP PlayQueue

**Status: SOURCE-IMPLEMENTED / ARYLIC-FORUM-DOCUMENTED / NOT-HW-VERIFIED.** No playback claim is made for the user's H50 until tested on the device.

## User-observed result

The user reports that v5.0.11 removed the red error banner but radio playback still did not start. v5.0.11 tried AVTransport `SetAVTransportURI` and `Play`, then sent framed TCP/8899 `MCU+PLY-PLA`. A successful TCP write was therefore not a valid playback confirmation and did not fix the reported H50 run.

## Arylic protocol evidence

Arylic staff's H50 guidance says TCP MCU commands cannot start a URL and points to UPnP `CreateQueue` followed by `PlayQueueWithIndex`. Their radio example sends a SOAP `CreateQueue` whose `QueueContext` contains a legacy Linkplay `<PlayList>` document with radio source fields and track URL/metadata, then invokes `PlayQueueWithIndex` with the same queue name and index 1. A separate H50 API answer says HTTPAPI is disabled for security while UPnP and TCP/8899 are available.

- [Arylic H50 MCU command discussion](https://forum.arylic.com/t/arylic-h50-mcu-command/5026)
- [Arylic H50 API discussion](https://forum.arylic.com/t/api-for-the-h50/3832/14)
- [Arylic radio PlayQueue example](https://forum.arylic.com/t/http-control-multiroom-tunein/241)

This is vendor-forum documentation, not a packet capture or proof that the user's firmware accepts the request or stream codec.

## v5.0.12 implementation

The UPnP-only radio route now:

1. Keeps the existing artwork proxy and metadata preparation.
2. Locates the device-advertised `urn:schemas-wiimu-com:service:PlayQueue:1` service and uses its discovered control URL and service URN.
3. Builds an Arylic Linkplay radio `<PlayList>` QueueContext with `Radio=1`, `SourceName=OnlineMusic`, one track, the selected URL and escaped DIDL-Lite metadata; the DIDL `res` advertises the selected audio MIME and the queue policy is 1.
4. Sends `CreateQueue`, then `PlayQueueWithIndex` with the same queue name and `Index=1`.
5. Reports SOAP faults by action and does not send `MCU+PLY-PLA` to start the URL.
6. Reads the advertised AVTransport state for diagnostics; state readback is reported separately from SOAP action acceptance.

The Arylic radio `<PlayList>` schema is distinct from the generic WiiM `<QueueContext><Name>…` schema. See the [canonical PlayQueue page](../../protocols/upnp/playqueue/COMMANDS.md).

## Scope, build, and limits

- No command was sent to the user's device during this code change.
- No firmware, device settings, stable v5.0.1 files, or existing hardware-confirmed KB facts were changed.
- v5.0.12 arm64 ZIP: `release/airControl-5.0.12-rc1-arm64.zip`.
- SHA-256: `7441dcbaf5f742d3fffad600ee9346255e02e95f1de1d83e4e8872aae623a67e`.
- Node syntax checks, `git diff --check`, Vite production build, Electron arm64 ZIP packaging, and `unzip -t` passed. No device playback test was run.
- PlayQueue support, accepted stream MIME/codec, audible playback, and native artwork on this specific H50 remain **NOT-HW-VERIFIED**.
- Isolated source folder: `/Users/lab/AI/airControl/airControl-v5.0.12/`.



## Follow-up 2026-10-30: v5.0.12 did not respond to radio selection

The user reports that v5.0.12 radio selection did not respond, while other airControl commands and the native app continued to control H50. The v5.0.12 direct-radio PlayQueue route is therefore **not a working H50 result** in this run. The code could send up to twelve sequential queue sequences for one click, each with network and state-read timeouts. Its DIDL layout also differed from Arylic's published direct URL radio example. These are identified client-side defects; without a v5.0.12 packet capture, the exact SOAP reply and causation of the user-visible delay remain unknown.

The existing WiiM Home PCAP on this H50 actually shows accepted `newTuneIn` queue traffic: `QueuePolicy=0`, `SourceName=newTuneIn`, `Radio=0`, `TrackNumber=0`, TuneIn `SearchUrl`, empty `Tracks`. It does not verify that H50 accepts the older Arylic direct URL `OnlineMusic` example. [Capture and APK evidence](../captures/H50-PLAYQUEUE-NEW-TUNEIN-2026-10-30.md).

v5.0.13-rc1 is an isolated candidate that sends one direct URL queue sequence per click, matches the vendor example's DIDL layout, and returns an explicit error if playback is not confirmed after two state reads. Its audible result remains **NOT-HW-VERIFIED**. Do not promote direct URL PlayQueue support from this source correction.

## Follow-up 2026-10-30: v5.0.13-rc1 failed on H50

The user tested v5.0.13-rc1 by selecting RTL. airControl reported `PlayQueueWithIndex: socket hang up; playback was not confirmed (stop)`. The selected station's artwork also did not appear in the native app; in earlier airControl versions the artwork did appear, although playback still required pressing Play in the native app. This is **USER-HW-OBSERVED** failure of the v5.0.13 direct URL `OnlineMusic` queue path on this H50. Do not present the old Arylic forum example as a verified working recipe for this firmware.

The existing WiiM Home PCAP shows a separate successful `newTuneIn` queue (`QueuePolicy=0`, `Radio=0`, `TrackNumber=0`, populated TuneIn `SearchUrl`, empty `Tracks`) with `PlayQueueWithIndex` HTTP 200 and subsequent `GetInfoEx` state `PLAYING`. This is **CAPTURE-OBSERVED** on the same H50. The differing source schema is the strongest lead; the capture does not establish a general Radio Browser URL route. Preserve the earlier `SetAVTransportURI` artwork behavior while investigating the exact start mechanism. No new command was sent to the device for this report.
