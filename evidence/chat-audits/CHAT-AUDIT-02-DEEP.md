# CHAT-AUDIT-02 — DEEP RE-AUDIT

Primary saved chat:
`Продолжение разработки airControl 041026.html`

This supersedes the shallow first CHAT-AUDIT-02 pass.

## Method
- inspected the saved HTML as a complete byte/text source, not only semantic-search hits;
- recovered references to research outputs and attached text/log files;
- re-read the WiiM Home research notebook and source extracts available in Library;
- separated APK/source evidence from real-device evidence;
- preserved negative/regression evidence rather than normalizing it away.

## Decompiled application identified
### WiiM Home
Decompiled source tree used in the research:
`/Users/lab/AI/WiiM-Home-decompiled/sources/`

Recovered classes/files referenced by the research include:
- `np8.java` — PlayQueue dispatcher/callback path
- `n42.java` — DLNA/UPnP service provider path
- `wq7.java` — QueueContext/BrowseQueue handling
- `kq.java` — AppendTracksInQueueEx
- `op8.java` — PlayQueueWithIndex
- `i27.java` — QueueContext XML builder (`<QueueContext><Name>...`)
- `ec9` — Qobuz API URL builder
- `QobuzPlayItem`, `LPPlayItem`, `LPPlayMusicList`, `LPMSPlayData`, `LPPlayMediaData`

No second decompiled controller application is asserted by this audit unless separately evidenced.

## StreamServicesCapability
WiiM Home:
`zv9.m(device, retries, callback)`
-> `n42.f1.c(device)`
-> RenderingControl
-> `StreamServicesCapability`
-> `StreamCapability`

Arguments:
- InstanceID = 0
- AppVersion = BuildConfig.VERSION_NAME
- recovered dependency VERSION_NAME = 1.0

Service helper map:
- `n42.f1.a(device)` -> AVTransport
- `n42.f1.b(device)` -> `urn:wiimu-com:serviceId:PlayQueue`
- `n42.f1.c(device)` -> RenderingControl

Hardware endpoints captured on tested A31/A97/A98:
- RenderingControl: `urn:schemas-upnp-org:service:RenderingControl:1`
- controlURL: `/upnp/control/rendercontrol1`
- PlayQueue serviceId: `urn:wiimu-com:serviceId:PlayQueue`
- controlURL: `/upnp/control/PlayQueue1`

## Hardware StreamCapability matrix

### A31
StreamCapability version 1.0.
Advertised: Prime 1.1, Tidal 2.1, newTuneIn 1.1, Rhapsody 1.0,
Deezer 1.1, Qobuz 1.2, iHeartRadio 1.0, vTuner 1.1.
Not advertised in captured response: Samba, Plex, SpotifyConnect,
TidalConnect, QobuzConnect, Roon, Squeezelite, YouTubeMusic.

### A97
StreamCapability version 1.2.
Advertised: Prime 1.4 SD; Tidal 2.2 LOW/HIGH/LOSSLESS; newTuneIn 1.1;
Rhapsody 1.0; soundmachine 1.1; Deezer 1.1; Qobuz 1.6 qualities 5/6/7/27;
iHeartRadio 1.0; Pandora 1.0; vTuner 1.1; CalmRadio 1.1 64/128/192/320;
SoundCloud 1.0.
Samba not advertised.

### A98
StreamCapability version 1.6.
Advertised services include Prime 1.4 SD/HD/UHD; Tidal 2.3 including HI_RES;
newTuneIn 1.2; Rhapsody 1.1; SoundMachine 1.2; Deezer2 1.1;
Qobuz 2.2; iHeart/iHeartRadio; Pandora2; vTuner; CalmRadio; SoundCloud;
Plex; KKBOX; RadioParadise2; HotMix; WiiMRadio; SpotifyConnect;
TidalConnect; AVS_MRM; Squeezelite; Roon; Soundtrack; QobuzConnect;
AudioCast; Samba; YouTubeMusic.

Important: `AudioCast 1.0` here is a returned capability/service name.
It is NOT evidence that an AudioCast controller APK was decompiled.

## Qobuz negotiation
Hardware values:
- A31 Qobuz 1.2
- A97 Qobuz 1.6
- A98 Qobuz 2.2

APK feature gates:
- >=1.5 Play Next
- >=1.6 + StreamCapability >=1.2 Play Last
- >=1.8 new OAuth login flow
- >=1.9 new Artist behavior
- >=2.0 + flag ReplayGain
- >=2.1 Weekly Queue
- >=2.2 Qobuz Radio

## Qobuz API/context routes recovered from ec9
- `/artist/page?artist_id=<id>`
- `/album/get?album_id=<id>&offset=<n>&limit=50`
- `/playlist/get?playlist_id=<id>&extra=tracks&offset=<n>&limit=50`
- `/radio/artist?artist_id=<id>`
- `/radio/album?album_id=<id>`
- `/radio/track?track_id=<id>`

These are catalog/context API routes, NOT proven direct audio stream URLs.

## Qobuz playback object chain
`Qobuz API`
-> `QobuzPlayItem`
-> `LPPlayMusicList`
-> `LPMSPlayData`
-> `wp6.F()`
-> `eh6.d()`
-> `LPPlayMediaData`
-> `n42.m0()`
-> device network playback

The model carries real Qobuz track ID separately from service/search context.
Do not reduce this architecture to `FLAC URL -> renderer`.

## PlayQueue actions recovered
- CreateQueue(QueueContext)
- ReplaceQueue(QueueContext)
- AppendTracksInQueue(QueueContext)
- AppendTracksInQueueEx(QueueContext, optional Action, Direction, StartIndex, Play)
- PlayQueueWithIndex(QueueName, Index)
- BrowseQueue(QueueName) -> QueueContext
- DeleteQueue(QueueName)
- BackUpQueue(QueueContext)
- GetQueueIndex(QueueName) -> CurrentIndex, PreloadingIndex, CurrentPage, TrackNums

The PlayQueue service endpoint is hardware-verified on tested devices.
Individual actions remain APK/source verified unless a direct device invocation
and response is separately captured.

## AVTransport family recovered from WiiM Home
- Play
- Pause
- Previous
- Next
- Seek
- GetMediaInfo
- GetInfoEx

These coexist with Linkplay HTTP, RenderingControl, PlayQueue and native MCU/TCP.
Do not collapse them into one transport family.

## SMB rule
WiiM Home contains SMB code/classes, but actual device support is capability-driven:
- A98: Samba 1.0 advertised
- A97: Samba not advertised
- A31: Samba not advertised

## A31 / airScope log evidence re-read
Recovered real traffic includes:
- `MCU+VOL+GET`
- response `AXX+VOL+012`
- `MCU+VOL+002` -> `AXX+VOL+002`
- `MCU+VOL+000` -> `AXX+VOL+000`
- `MCU+VOL+010` -> `AXX+VOL+010`
- continuing absolute values through `MCU+VOL+065` -> `AXX+VOL+065`
- `AXX+MUT+001`, `AXX+MUT+000`
- `AXX+SIL+001`, `AXX+SIL+000`
- `AXX+SNG+INF{...}` asynchronous playback event

This materially upgrades confidence in the no-ampersand gateway form
`MCU+VOL+GET` and absolute `MCU+VOL+NNN` behavior.

Historical HTTP regression evidence:
an older gateway build mapped VOL_UP to `setPlayerCmd:vol--` and VOL_DOWN
to URL-encoded `setPlayerCmd:vol++`. Device status/logs showed this mapping
was reversed relative to intended UI semantics. Canonical mapping remains:
VOL+ -> vol++; VOL- -> vol--.

## Remaining research point
Exact final Qobuz QueueContext XML and the final `n42.m0()` path remain the
main unfinished reverse-engineering target. Do not invent the missing fields.

## Second attachment sweep: exact XML builders recovered
A later full-file sweep of the very large `wiim-queuecontext-xml-final.txt`
(145,634 lines) recovered the previously missing exact generic QueueContext
serializer in `i27.java`.

It serializes Name, Source, CurrentIndex, optional HeadData, Tracks with
Title/Artist/Album/Url/Image, optional TailData, then closes QueueContext.

The same source dump also recovered `tr6.java` playlist serialization with
ListName/ListInfo/SourceName/SearchUrl/TrackNumber and per-track Source/Id/URL/
service-specific supplementXml/Metadata.

Therefore the earlier statement that the generic QueueContext XML was still
unknown is superseded. What remains unresolved is the exact service-specific
Qobuz values and final live invocation path on each device generation.

## Third sweep — additional protocol families recovered

A further attachment/source-dump pass found two important areas missed earlier:

1. WiiM Home `ylb.java` has a dedicated PlayQueue `SetMediaServerInfo` path to
   `http://<device>:59152/upnp/control/PlayQueue1`. It supplies controller name,
   UUID, IP and `media_port`. This is directly relevant to airControl serving
   local media to a renderer.

2. The recovered RenderingControl SCPD contains a much larger action set than
   StreamServicesCapability: volume/mute/channel/EQ, rendering presets,
   multiroom device information/slave mask, alarm queues, device naming and
   AirPlay sync actions. These are now inventoried with SCPD-level status and
   are not falsely promoted to per-action hardware confirmation.

## Fourth sweep — full PlayQueue SCPD recovered

`wiim-playback-map.txt` contains the embedded PlayQueue SCPD (`vt1.java`).
This exposed a substantially larger protocol surface than the earlier
CreateQueue/PlayQueueWithIndex/AppendTracksInQueueEx subset.

Added 20 new command/query records, including BrowseQueueEx,
ReplaceQueue, DeleteQueue, BackUpQueue, queue loop/policy, RemoveTracksInQueue,
online queue search/fetch, stream quality, rating, key mapping and account
login/logout/register actions.

This is particularly important for the online-services research because
GetQueueOnline/SearchQueueOnline/UserLogin demonstrate that the PlayQueue
service is not merely a local playlist container.
