# Online services command view

- `QRY-UPNP-STREAM-CAPABILITY` — **stream services capability** — `StreamServicesCapability(InstanceID, AppVersion)` — **SOURCE-CONFIRMED / NOT-HW-VERIFIED**
- `QRY-UPNP-STREAM-CAPABILITY-EXACT` — **service capability** — `StreamServicesCapability(InstanceID=0, AppVersion=BuildConfig.VERSION_NAME) -> StreamCapability` — **APK-VERIFIED + HARDWARE-VERIFIED**
- `CMD-UPNP-PQ-STREAM-SET-QUALITY` — **online stream quality** — `StreamSetQuality(source, quality)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `QRY-UPNP-PQ-STREAM-GET-QUALITY` — **online stream quality** — `StreamGetQuality(source) -> quality` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-SET-RATING` — **online track rating** — `SetRating(Source, TrackID, Rating)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `QRY-UPNP-PQ-GET-ONLINE` — **online queue fetch** — `GetQueueOnline(QueueName, QueueID, QueueType, Queuelimit, QueueAutoInsert) -> QueueContext` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `QRY-UPNP-PQ-SEARCH-ONLINE` — **online queue search** — `SearchQueueOnline(QueueName, SearchKey, Queuelimit) -> QueueContext` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-SET-QUEUE-RECORD` — **online queue record/favorite** — `SetQueueRecord(QueueName, QueueID, Action)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-SET-SONGS-RECORD` — **online song record/favorite** — `SetSongsRecord(QueueName, SongID, Action)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-USER-REGISTER` — **online account register** — `UserRegister(QueueName, UserName, PassWord) -> Result` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-USER-LOGIN` — **online account login** — `UserLogin(AccountSource, Version, UserName, PassWord, SavePass, Code, CodeVerifier, Token, Proxy) -> Result` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-USER-LOGOUT` — **online account logout** — `UserLogout(AccountSource) -> Result` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
