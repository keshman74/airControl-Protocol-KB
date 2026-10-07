# WiiM Home QueueContext XML — exact recovered builder

Status: **APK-VERIFIED / EXACT-BUILDER-RECOVERED**

Recovered from decompiled `i27.java`.

```xml
<QueueContext>
  <Name>...</Name>
  <Source>...</Source>
  <CurrentIndex>...</CurrentIndex>
  <HeadData>
    <Item>...</Item>
  </HeadData>
  <Tracks>
    <Track index="0">
      <Title>...</Title>
      <Artist>...</Artist>
      <Album>...</Album>
      <Url>...</Url>
      <Image>...</Image>
    </Track>
  </Tracks>
  <TailData>
    <Item>...</Item>
  </TailData>
</QueueContext>
```

`HeadData` and `TailData` are emitted only when non-empty.
Each track comes from `LPMetadataPlayItem`.
The builder XML-escapes textual values.

This resolves the previously open question of the generic `QueueContext`
serialization format. It does **not by itself** prove every service-specific
Qobuz HeadData/TailData value or the exact final live Qobuz invocation on each
hardware generation.
