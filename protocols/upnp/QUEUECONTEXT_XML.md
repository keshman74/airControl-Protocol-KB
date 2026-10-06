# QueueContext XML

Exact generic builder recovered from WiiM Home `i27.java`.

```xml
<QueueContext>
  <Name>...</Name>
  <Source>...</Source>
  <CurrentIndex>...</CurrentIndex>
  <HeadData><Item>...</Item></HeadData>
  <Tracks>
    <Track index="0">
      <Title>...</Title><Artist>...</Artist><Album>...</Album>
      <Url>...</Url><Image>...</Image>
    </Track>
  </Tracks>
  <TailData><Item>...</Item></TailData>
</QueueContext>
```

HeadData/TailData are optional. Text is XML-escaped.
