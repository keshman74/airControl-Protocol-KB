# 4STREAM 3.1.20.230912: AirPlay / Network / DLNA metadata and artwork

Source ID: **REV-4STREAM-AIRPLAY-ART-001**. Analysis date: 2026-10-25. Status throughout: **APK-VERIFIED / NOT-HW-VERIFIED**. This is static client implementation evidence. No APK code was executed, no binary was opened in a runtime, and no speaker/device request was sent.

## Artifact and scope

- Package: com.wifiaudio.Stream; version 3.1.20.230912 / 2023091217.
- APK SHA-256: 08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b.
- Scope: metadata and cover flow for AirPlay, generic Network/DLNA and the competing Internet Radio/TuneIn paths.
- Tooling: REA Android method inspection backed by JADX Headless MCP 0.7.1, plus an all-DEX dexlib2 reference and string-pool scan using the same frozen JADX MCP artifact.
- Existing hardware-confirmed facts and transport mappings are unchanged.

## Executive result

The 4STREAM client does **not** manufacture a device URL for AirPlay artwork. It expects albumArtURI to already be an absolute string beginning with http. A value such as /data/airplay_<hash>.jpg is rejected by NewPlayControlFragment.R2 before OkHttp is called and the default cover is shown. A full http:// or https:// URI is sent verbatim, including any explicit port. If the URI omits a port, normal URI defaults apply: HTTP 80 or HTTPS 443. Device security selects an OkHttp client implementation but does not rewrite this artwork URL.

No AirplayArtWorkData.jpeg fallback, /data/airplay_ builder, or other AirPlay artwork endpoint was found in the complete DEX string pool or in the reviewed URL-building path. This negative finding is bounded to the APK bytecode: a device may dynamically return an endpoint that the APK never stores as a literal.

## End-to-end path

~~~text
UPnP LastChange CurrentTrackMetaData
  or GetInfoEx TrackMetaData
  or GetMediaInfo CurrentURIMetaData
        |
        v
DeviceInfoExt.setDlnaTrackMetaData(String)
        |
        v
XmlAlbumInfo.a(String) parses DIDL-Lite / upnp:albumArtURI
        |
        v
DeviceInfoExt.albumInfo.albumArtURI + UI broadcasts
        |
        v
FragMenuContentCT.v1 selects NewPlayControlFragment for generic/AirPlay
        |
        v
NewPlayControlFragment.d4 -> S3 -> S2
        |
        +-- PlayMedium AIRPLAY/ROON -> R2 -> g.G(device).s(exact URL)
        |                                 -> OkHttp GET -> bytes
        |                                 -> BitmapFactory.decodeByteArray
        |                                 -> ImageView.setImageBitmap
        |
        +-- other generic source -> Glide (memory + SOURCE disk cache)
~~~

### Metadata ingress

There are three concrete application paths into the same setter:

| Path | Class and method | Stable DEX anchor | Behavior |
|---|---|---|---|
| periodic extended status | Lcom/wifiaudio/service/d$c1;->onSuccess(Ljava/util/Map;)V | classes2.dex: TrackMetaData const-string @ code unit 28; setDlnaTrackMetaData invokes @ 1074 and 1271 | Reads TrackSource, PlayMedium and TrackMetaData from GetInfoEx results. |
| AVTransport event | Lcom/wifiaudio/service/d$y0;->k(Lorg/teleal/cling/model/gena/a;)V | CurrentTrackMetaData const-string @ 85 and 415; setter invoke @ 504 | Parses LastChange, applies PlaybackStorageMedium and TrackSource, XML-unescapes CurrentTrackMetaData, then updates the model. |
| explicit media info | Lcom/wifiaudio/service/d$b;->onSuccess(Ljava/util/Map;)V | CurrentURIMetaData const-string @ 96; setter invoke @ 112 | Reads TrackSource, CurrentURI, PlayMedium and CurrentURIMetaData from GetMediaInfo. |

The controller anchors are Lcom/wifiaudio/service/m/c/a;->h(...)V for GetInfoEx and ->i(...)V for GetMediaInfo. Its GetMediaInfo callback class extends org.teleal.cling.support.avtransport.callback.GetMediaInfo.

The relevant event fragment is:

~~~java
if (mapA.containsKey("CurrentTrackDuration")
        || mapA.containsKey("CurrentTrackMetaData")) {
    String medium = mapA.get("PlaybackStorageMedium");
    String source = mapA.get("TrackSource");
    String metadata = mapA.get("CurrentTrackMetaData");
    if (medium != null) devInfoExt.setDlnaPlayMedium(medium);
    if (source != null) devInfoExt.setDlnaTrackSource(decode(source));
    if (metadata != null && !TextUtils.isEmpty(metadata.trim())) {
        devInfoExt.setDlnaTrackMetaData(xmlUnescape(metadata));
    }
}
~~~

GetPositionInfo is present as a library callback, but a complete reference-instruction scan found only its own class initialization and internal virtual call. No application instantiation/caller was found. Therefore this metadata/artwork path uses LastChange, GetInfoEx and GetMediaInfo, not GetPositionInfo. This is a complete-within-DEX direct-reference negative; reflection is outside that proof.

### DIDL-Lite and albumArtURI parsing

Generic Network/DLNA and AirPlay metadata reaches:

- Lorg/teleal/cling/c/a/a/z/e;->a(Ljava/lang/String;)Lcom/wifiaudio/model/AlbumInfo;
- DEX string anchors in classes3.dex: album-art regex @ 103, normalized replacement @ 105, opening-tag checks @ 352/360/376 and closing tag @ 366.
- Calls from DeviceInfoExt.setDlnaTrackMetaData at code units 212 and 284.

The parser normalizes an upnp:albumArtURI tag that carries attributes, extracts the element body, removes CDATA where present, decodes XML entities, and assigns the resulting string to AlbumInfo.albumArtURI. It does not resolve the string as a URI and does not join it to the device base URL.

Condensed decompilation:

~~~java
metadata = metadata.replaceAll(
    "<upnp:albumArtURI\\s*[\\w\\W]*>(.*)</upnp:albumArtURI>",
    "<upnp:albumArtURI>$1</upnp:albumArtURI>");
...
albumInfo.albumArtURI = decodeXml(
    between(metadata, "<upnp:albumArtURI>", "</upnp:albumArtURI>"));
~~~

A separate JSON parser in the same class reads the albumArtURI key. AirPlay does not have a dedicated parser branch: unless another source-specific condition matches, it uses this generic DIDL parser.

## AirPlay identification

Lcom/wifiaudio/model/DeviceInfoExt;->isAirPlay()Z, DEX prototype ()Z:

~~~java
public boolean isAirPlay() {
    String medium = this.dlnaPlayMedium;
    return medium != null
        && medium.trim().toUpperCase().equals(LP_AIRPLAY);
}
~~~

REA Evidence: ev_58a5b8366ab39e72bdf31ecd5a88f5cbfee3533f39fdb9b25917330102f712fb.

Thus recognition is based on the UPnP/GetInfoEx PlayMedium value AIRPLAY, not chip name, filename pattern, TrackSource, or album-art path.

## Model update and UI selection

DeviceInfoExt.setDlnaTrackMetaData selects source-specific parsers for Spotify, Alexa/Pandora, Douban, selected JSON sources, Rhapsody/AldiLife, Deezer, THIRD-DLNA and TuneIn; otherwise it uses the generic DIDL parser. It stores the parsed fields in the shared AlbumInfo, then calls setDlnaTrackURI and setDlnaAlbumArtURI.

- Exact method: Lcom/wifiaudio/model/DeviceInfoExt;->setDlnaTrackMetaData(Ljava/lang/String;)V.
- REA Evidence: ev_7b2c8fe0e339447bb0d19247afd3ff5f271b1d6f2e4434acf6864e9c87a77f3e.
- AlbumInfo.albumArtURI read/write anchors in this method include code units 578/664/700; setDlnaAlbumArtURI invoke @ 702.
- album cover update is emitted only when old title+artist differs from new title+artist; album info update is emitted after every accepted metadata reparse.

FragMenuContentCT.v1 routes IHeart, Alexa/Pandora, Spotify, TuneIn, LinkplayRadio and sleep/device sounds to dedicated fragments. Other sources use NewPlayControlFragment when config.a.g0 is true; it is initialized true in this APK and no reassignment was found in the static field-reference review. REA Evidence for v1: ev_65ff94a0cb04559d2bdc90730a174da8df8296a1ecd5ce79150b230ed4cd6404.

For the generic screen, the DEX path is:

- NewPlayControlFragment.d4() -> S3(DeviceInfoExt) @ code unit 359.
- S3 -> S2(albumInfo.albumArtURI) @ code units 22 or 129.
- S2 -> R2 for AIRPLAY or ROON @ code unit 224.
- AirPlay response callback NewPlayControlFragment$v.b(Object) decodes bytes with BitmapFactory.decodeByteArray @ code unit 12.
- NewPlayControlFragment$w.run() writes the bitmap with ImageView.setImageBitmap @ code unit 24.

## URL handling, scheme and port

NewPlayControlFragment.S2 first rewrites only legacy Rhapsody/Napster hosts. That rule is unrelated to AirPlay. It suppresses a reload when the new string equals field l. For AIRPLAY or ROON it calls R2 instead of Glide.

~~~java
if (playMedium.equalsIgnoreCase("AIRPLAY")
        || playMedium.equalsIgnoreCase("ROON")) {
    R2(str, imageView);
} else {
    GlideMgtUtil.loadBitmap(...);
}
~~~

REA Evidence for S2: ev_d4b4bada27f3c8d8a4485b1bb4137690754ff1d2e076e4a5d9e5e52b9717ae7b.

R2 is decisive:

~~~java
private void R2(String str, ImageView imageView) {
    if (TextUtils.isEmpty(str) || !str.startsWith("http")) {
        setDefaultCover(imageView);
        return;
    }
    DeviceItem device = q0();
    if (device != null) {
        g.G(device).s(str, new v(imageView));
    }
}
~~~

REA Evidence for R2: ev_ba604e2f4c58196c5d1ecf8f3bbe79645c0c38bc3e70077c116f76f33a1062b9.

Consequences:

1. Both http:// and https:// pass because both begin with http.
2. A relative /data/airplay_<hash>.jpg fails the prefix test and is not transformed.
3. g.G(device) chooses an HTTP or HTTPS-capable client from device security, but g.s passes the supplied string to Request.Builder.url unchanged.
4. No port is added. An explicit port in the metadata URI is retained; otherwise the URI scheme determines the normal default, 80 for HTTP and 443 for HTTPS.
5. This artwork path is independent of the HTTPAPI :4443 routing described in the broader 4STREAM report.

The secure base client contains an optional interceptor that can force port 8443 and add retries only when config.a.N2 is true. In this APK N2 is initialized false; the complete field-reference scan found one SPUT in config.a.<clinit> and only SGET readers elsewhere. The interceptor is therefore inactive in the reviewed build, so it does not change the port or 404 behavior above.

HTTP construction:

~~~java
private void A(String str, Callback cb) {
    Request request = new Request.Builder().url(str).build();
    httpClient.newCall(request).enqueue(new j(cb));
}
~~~

REA Evidence: ev_b0856be179c6f6fd071d28a420e19aa8575fa6a3df68d3e76fbed609849dab7c. Client selection Evidence: ev_37c92353a07866e5f70950d9c81d0fe3812f814ffde77600d3588c0d80f9ce3c.

### The only host rewrite is not AirPlay

DeviceInfoExt contains one artwork host rewrite, but only when TrackSource equals Android_<id>_RemoteLocal. For an existing absolute http:// URL it replaces the original host with the phone IP and the embedded phone media-server port while preserving the path. This is local-phone playback support. It is not selected by PlayMedium AIRPLAY, does not accept a relative path, and must not be generalized into an AirPlay resolution rule.

## HTTP 404 and bitmap failure

The HTTP callback treats only 200–299 and 304 as success:

~~~java
private boolean K(int code) {
    return (code >= 200 && code < 300) || code == 304;
}
~~~

REA Evidence: ev_e368b8bf6319b382829364151b8383a0e9cc5406150ebee1a75c2bb401466ae9.

A 404 is delivered to NewPlayControlFragment$v.a(Exception), which immediately assigns the default cover. If a nominally successful response cannot be decoded, the posted UI runnable also chooses the default cover for a null bitmap.

There is no AirPlay-specific 404 retry, alternate endpoint, or stale-success restore in the reviewed path.

## Cache and previous-cover behavior

For AirPlay, S2 deliberately bypasses Glide. R2 uses an OkHttpClient built without an application Cache and decodes the response bytes directly. Therefore:

- no AirPlay bitmap memory/disk cache is configured by this path;
- the last URL string is retained in NewPlayControlFragment.l and an identical URL is not fetched again;
- the current ImageView bitmap naturally remains until another UI update occurs;
- when a different URL is requested and fails with 404 or decode failure, the default cover replaces the previous bitmap;
- metadata/history storage may retain albumArtURI as data, but it is not used here as a successful-image fallback.

For non-AirPlay generic sources, S2 configures Glide with skipMemoryCache(false) and DiskCacheStrategy.SOURCE. That cache behavior must not be attributed to AirPlay.

## AirPlay versus Internet Radio, TuneIn and DLNA

The distinction exists at two layers:

1. DeviceInfoExt.setDlnaTrackMetaData chooses a parser from current TrackSource and PlayMedium. TuneIn and other services can have dedicated parsers; ordinary DLNA and AirPlay use generic DIDL parsing.
2. FragMenuContentCT.v1 selects dedicated playback fragments for TuneIn, LinkplayRadio, Spotify, Alexa/Pandora and IHeart. AirPlay remains on the generic new playback fragment, where the AIRPLAY medium selects the direct-byte artwork loader.

There is no explicit metadata generation number, source ownership token, AIRPLAY priority check, or stale-callback rejection around setDlnaTrackMetaData. GetInfoEx, GetMediaInfo and LastChange event callbacks all update the same DeviceInfoExt fields. The callbacks set TrackSource/PlayMedium before metadata in their normal flow, but static code does **not** prove that a late result from a previous radio request cannot overwrite newer AirPlay state. The defensible conclusion is arrival-order shared-state behavior, not a guarantee of AirPlay precedence. Runtime reproduction is required to determine whether service scheduling prevents that race in practice.

## Fallback endpoint search

A complete string-pool scan covered classes.dex, classes2.dex and classes3.dex and included the requested terms and case variants.

| Term | Result relevant to AirPlay artwork |
|---|---|
| AirplayArtWorkData.jpeg | 0 matches |
| /data/airplay_ | 0 matches |
| airplay_ | 6 matches, all AirPlay UI/localization identifiers; no artwork path |
| /data/ | 41 matches, class descriptors or unrelated data paths such as /data/sys.log; no AirPlay cover |
| artwork | 3 generic cloud-model accessor names |
| albumArt / cover | many generic model/UI/cache strings; no AirPlay fallback builder |
| jpg / jpeg | generic MIME/format/service templates; no AirplayArtWorkData endpoint |

No fallback to /data/AirplayArtWorkData.jpeg or another synthesized endpoint is implemented in the reviewed DEX path.

## Update cadence on AirPlay track change

Lcom/wifiaudio/service/d;->V0()V starts two timers:

~~~java
getInfoExTimer.scheduleAtFixedRate(getInfoExTask, 0L, 5000L);
progressTimer.scheduleAtFixedRate(progressTask, 0L, 1000L);
~~~

REA Evidence: ev_17738e9f536688e231c277854a75b05a0f2033dbf4bbb3b9dc44a1091a9d06d1.

The 5-second task is the gated GetInfoEx status/metadata poll. The 1-second task is local playback-progress maintenance, not an artwork poll. AVTransport LastChange events can update metadata immediately. Therefore a track change is processed:

- immediately when a usable LastChange event arrives; or
- on the next eligible GetInfoEx cycle, with a worst-case nominal interval of about 5 seconds before gating/network delays.

Artwork is requested when S2 receives a URL string different from its remembered value. It is not independently polled. If successive tracks reuse the identical URL, the same-URL suppression prevents a new AirPlay download.

## Direct answers

1. **AirPlay recognition:** PlayMedium, trimmed and uppercased, equals AIRPLAY.
2. **Relative albumArtURI:** it is not expanded. /data/airplay_<hash>.jpg is rejected and the default cover is shown.
3. **Scheme and port:** full http or https URI is used verbatim; explicit port retained, otherwise normal 80/443 default. No AirPlay-specific port is appended.
4. **HTTP 404:** error callback, then default cover. No fallback endpoint.
5. **Previous cover cache:** no AirPlay Glide/OkHttp application cache; only same-URL request suppression and transient current ImageView state. A failed new URL replaces the image with default.
6. **Source separation / overwrite:** parser and playback-fragment selection distinguish services, but the shared model has no explicit AirPlay priority or stale-result guard; late radio metadata is not statically prevented from overwriting.
7. **Fallback:** no AirplayArtWorkData.jpeg, /data/airplay_ builder or alternate AirPlay endpoint found.
8. **Frequency:** event-driven immediately when LastChange works, otherwise the next gated 5-second GetInfoEx cycle; artwork only on a distinct URL.

## Evidence boundary

DEX code-unit anchors are offsets within a method instruction stream, not file offsets or runtime addresses. Generated Java names can be aliases; the class descriptors and method prototypes above are stable for this APK. Static reference scanning does not cover reflection, dynamically downloaded code, firmware-generated strings, or runtime device behavior. Hardware verification, live packet capture, HTTP response observation and timing measurements were not performed.
