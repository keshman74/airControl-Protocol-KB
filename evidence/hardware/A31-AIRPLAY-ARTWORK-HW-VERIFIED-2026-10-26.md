# A31 AirPlay artwork — hardware verification and implementation rule

Date: **2026-10-26**  
Status: **HW-VERIFIED**  
Device family: **Linkplay A31 / airScope**  
Related static analysis: `protocols/linkplay-http-https/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md`

## Hardware-confirmed result

During active AirPlay playback on the tested A31, UPnP AVTransport `GetPositionInfo` on port `49152` returned DIDL metadata containing a **root-relative** `upnp:albumArtURI`.

Two observed examples:

- `Air` — Bicep, soarr: `/data/airplay_f67a80954965fd2f79a144f41d4bbe38.jpg`
- `Williamsburg` — Apparat: `/data/airplay_3dc11f6bacaf2037be977bbcf2ccc5a1.jpg`

The second path was fetched successfully from the device HTTP origin:

```text
http://<device-ip>/data/airplay_3dc11f6bacaf2037be977bbcf2ccc5a1.jpg
HTTP 200
Content-Type: image/jpeg
180224 bytes
JPEG 512x512
```

The first observed AirPlay artwork was also hardware-tested as HTTP 200 / `image/jpeg` / 180224 bytes / JPEG 512x512 while active. The same exact URL could later return HTTP 404 while still present/stale in metadata, so these artwork objects are transient and must not be assumed permanent.

## Critical port/origin rule

**Port 49152 is the UPnP control endpoint, not the origin for A31 AirPlay artwork.**

A client must **not** transform:

```text
/data/airplay_<32hex>.jpg
```

into:

```text
http://<device-ip>:49152/data/airplay_<32hex>.jpg
```

For the tested A31, the correct artwork origin is the normal device HTTP origin:

```text
http://<device-ip>/data/airplay_<32hex>.jpg
```

(default HTTP port 80).

Recommended implementation: preserve the root-relative `albumArtURI` from DIDL metadata, then resolve it against the selected device's normal HTTP origin. Do not infer the artwork port from the UPnP SOAP/control port.

## airControl v5.0.0 bug and fix

The Electron `linkplayUpnpPositionInfo()` implementation previously did:

```js
let art = xmlTag(meta, "albumArtURI");
if (art && art.startsWith("/")) art = `http://${host}:49152${art}`;
```

This was the cause of missing A31 AirPlay covers.

The verified fix is to preserve the URI:

```js
const art = xmlTag(meta, "albumArtURI");
```

and let the artwork resolver join supported device-local relative paths to the selected device origin.

After this change, hardware testing confirmed the real AirPlay album cover appears both in the A31 zone card and in airControl **Now Playing**. Tested visible track after the fix: `Recalibration` — Apparat, album `A Hum Of Maybe`, source `AirPlay`.

## Rule for airControl KNOB / ESP32

For KNOB implementations using A31 AirPlay metadata:

1. Read `upnp:albumArtURI` from the current metadata.
2. If it is an absolute `http://` or `https://` URL, use it as supplied.
3. If it matches a root-relative A31 device artwork path such as `/data/airplay_<32hex>.jpg`, fetch it from the A31's normal device HTTP origin, e.g. `http://<A31-IP>/data/airplay_<hash>.jpg`.
4. **Do not use port 49152 for the JPEG fetch.** Port 49152 remains the UPnP SOAP/control service.
5. Treat HTTP 404 as potentially transient/stale metadata. A later metadata update may provide a new hash/path.
6. Do not allow remembered Internet Radio artwork to override a successfully resolved native AirPlay cover.

## Evidence classification

- Root-relative A31 AirPlay `/data/airplay_<32hex>.jpg`: **HW-VERIFIED**
- JPEG served from normal A31 HTTP origin / port 80: **HW-VERIFIED**
- HTTP 200, `image/jpeg`, 180224 bytes, 512x512: **HW-VERIFIED**
- Same artwork URL can later become 404/stale: **HW-VERIFIED**
- airControl fix (do not prepend `:49152`; resolve against device origin): **HW-VERIFIED in UI**
- Native 4STREAM behavior remains separately classified as **APK-VERIFIED / NOT-HW-VERIFIED** in its source document.
