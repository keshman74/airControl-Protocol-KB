# H50 PlayQueue traffic and 4STREAM URL playback route — 2026-10-30

**Evidence status:** CAPTURE-OBSERVED for the recorded H50 UPnP request/response bytes; APK-VERIFIED for the 4STREAM static call chain; **NOT-HW-VERIFIED for direct Radio Browser URL playback**. This report does not infer that an accepted SOAP action produced audible audio.

## Inputs

- Existing capture: `/private/tmp/wiim-a97.pcap`, SHA-256 `71aaebfc2987d0bd99e47e75d0191ea9eb7c6f528acb9a87b69d3947ffa03fb4`, recorded 2026-10-29. Read offline with `tcpdump -nn -A -r`; no packet was sent during this analysis.
- 4STREAM APK: `/Users/lab/AI/4STREAM.apk`, SHA-256 `08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b`, package `com.wifiaudio.Stream` version `3.1.20.230912`. Inspected statically through REA/JADX 0.7.1; no APK execution.
- User observation on 2026-10-30: v5.0.12 radio selection in airControl did not respond; other airControl commands and the native app still controlled H50. This establishes a radio-path regression, not the exact H50 SOAP reply.

## Captured H50 PlayQueue sequence

The recorded Mac `192.168.0.104` sent these actions to H50 `192.168.0.100:59152/upnp/control/PlayQueue1`:

| Local time 2026-10-29 | Request | Response |
|---|---|---|
| 14:18:23.893 | `CreateQueue`, SOAPAction `urn:schemas-wiimu-com:service:PlayQueue:1#CreateQueue`, 1108-byte body | 14:18:23.903, HTTP 200 with `CreateQueueResponse` |
| 14:18:23.906 | `PlayQueueWithIndex`, same service, `QueueName=Kiss FM Ukraine`, `Index=1` | 14:18:23.923, HTTP 200 with `PlayQueueWithIndexResponse` |

The `CreateQueue` body has `QueuePolicy=0`. Its XML-escaped `QueueContext` decodes to this shape (the device serial in `SearchUrl` is intentionally omitted):

```xml
<PlayList>
  <ListName>Kiss FM Ukraine</ListName>
  <ListInfo>
    <SourceName>newTuneIn</SourceName>
    <TrackNumber>0</TrackNumber>
    <SearchUrl>http://api.radiotime.com/profiles/s104870/media?...</SearchUrl>
    <Radio>0</Radio>
    <PicUrl>http://cdn-profiles.tunein.com/s104870/images/logoq.png?...</PicUrl>
    <ContentType>radio</ContentType>
    <Quality>0</Quality>
    <Login_username></Login_username>
    <CurrentPage>1</CurrentPage>
    <TotalPages>1</TotalPages>
  </ListInfo>
  <Tracks></Tracks>
</PlayList>
```

The `SearchUrl` in the packet includes a TuneIn profile path, a partner ID, `latlon`, version, and a device serial. The `QueueContext` string escapes its ampersands a second time in SOAP. The response proves the H50 accepted this particular `newTuneIn` queue shape. The capture did not isolate audible playback or prove the queue was created because of a specific UI click.

This differs materially from Arylic's older [direct URL radio example](https://forum.arylic.com/t/http-control-multiroom-tunein/241), which uses `SourceName=OnlineMusic`, `Radio=1`, `TrackNumber=1`, one `Track1/URL` plus escaped DIDL-Lite `Metadata`, and `QueuePolicy=1`. The recorded acceptance of `newTuneIn` **must not be promoted to proof that this firmware accepts the direct URL schema**.

## 4STREAM APK custom URL path

Focused JADX method evidence:

| Method | Static finding | REA Evidence |
|---|---|---|
| `FragCustomRadioTuneIn.w2(TuneCustomRadioItem)` | Passes the item's `link` to `com.wifiaudio.action.e.A0`. | `ev_0745ea3a9152c7bd5515682afe27be2c4d753b4d45fe5c9fd8822ca8a67ce5b1` |
| `com.wifiaudio.action.e.A0(DeviceItem,String,...)` | Calls `action.s.a.U(device, Uri.encode(link))` and sends the result through `utils.e1.g.G(device).s(...)`. | `ev_a0217ee0a1aa483942d30fc302bde007dc022e0ca21bb614344bf51241781215` |
| `action.s.b.U(DeviceInfoParam,String)` | Builds `g.E(deviceInfoParam) + "setPlayerCmd:play:" + encoded URL`. | `ev_5b1315bb75089722f3425b22a7af1168fb585ed06d42318a1f8bfaa8e607e9c5` |
| `utils.e1.g.E(DeviceInfoParam)` | Selects `http://IP/httpapi.asp?command=`, `https://IP/httpapi.asp?command=`, or HTTPS port 4443 according to the device's security and gc4a flag. | `ev_492245e37f35612e4e662191fe5c84d59408b9b2e3ff859cdf21c975da7f9f` |
| `utils.e1.g.G(DeviceItem)`, `utils.e1.e.g0/f0` | Selects a secure client for security 3.x, and its newer certificate/password route names `certificate_new` and `WiimuNDK.securityPwd1()`. | `ev_eca3e9117eb67da7ca015c74cddf248b6ab7600cb48774027f7adebe130551ad`, `ev_a99b98aafea041ce947e4bde2f5a83d89b33e58a2fc8c74f05eac36b50326f1d`, `ev_7b7839b0726d85c2df37553f5bf5e0911616f6b57db33ecc6fc661889be6b550` |

This is a static path for 4STREAM's **custom radio link** in the analyzed 2023 APK. It does not prove that the user's current phone installation uses the same version or that every Internet Radio provider uses this path. It does explain why native 4STREAM playback is not evidence that the direct UPnP `OnlineMusic` PlayList works on H50.

The canonical [H50 fallback profile](../../devices/A97-NON-HTTPS.md) already records that this device advertises `security=https/2.0`, `security_version=3.0`, and TLS/443 while plain HTTP/80 is refused. “A97 Non HTTPS” names airControl's fallback profile when its own HTTPS request cannot complete; it is not a claim that HTTPS is absent from H50 firmware.

## airControl consequence

v5.0.12 used a generic direct-radio `OnlineMusic` queue on H50 and could repeat `CreateQueue`/ `PlayQueueWithIndex` for up to twelve alternate URLs per click. Its DIDL also differed from Arylic's direct URL example. v5.0.13 limits each click to one queue sequence, restores the example's vendor-specific DIDL layout, and reports unconfirmed playback. These are **SOURCE-IMPLEMENTED / NOT-HW-VERIFIED** corrections. The exact H50 direct URL playback route remains unresolved until a matching current-device capture or hardware test establishes it.
