# WiiM Home PlayList XML builder

Status: **APK-VERIFIED / EXACT-BUILDER-RECOVERED**

Recovered from `tr6.java`.

Core structure:

```xml
<PlayList>
  <ListName>...</ListName>
  <ListInfo>
    <SourceName>...</SourceName>
    <SearchUrl>...</SearchUrl>
    <TrackNumber>...</TrackNumber>
    ...
  </ListInfo>
  <Tracks>
    <Track1>
      <Source>...</Source>
      <Id>...</Id>
      <URL>...</URL>
      ...
      <Metadata>...</Metadata>
    </Track1>
  </Tracks>
</PlayList>
```

For each `LPPlayItem`, the builder writes the media source, real track ID,
`getPlayUrl()`, service-specific `supplementXml()`, and generated metadata.
This is strong evidence that WiiM Home preserves service IDs/context alongside
the playable URL rather than reducing playback to a bare URL.
