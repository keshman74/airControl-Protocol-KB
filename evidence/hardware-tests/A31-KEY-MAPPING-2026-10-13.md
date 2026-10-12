# A31 GetKeyMapping readback — 2026-10-13
User ran read-only SSDP/service-description/SCPD discovery and SOAP GetKeyMapping on their A31. Local IP omitted.
Advertised service: urn:schemas-wiimu-com:service:PlayQueue:1.
Control endpoint: HTTP port 49152, /upnp/control/PlayQueue1.
SCPD showed no input arguments. Parsed QueueContext tag set:
Key0..Key20, KeyList, ListName, MaxNumber, Metadata, Name, PicUrl, Source, Url.
Names read: CLARK; THE SECOND BITE; SomaFM: Space Station Soma; SomaFM: DEF CON Radio; Hit FM Ukraine; Люкс ФМ Україна - Lux FM Ukraine; SomaFM: DEF CON Radio. Each observed Name had an _#~ timestamp suffix.
Scope: successful reading on one tested A31; not a playback test or proof for A97/A98/A33. Numeric slot association remains open because initial diagnostic flattened names.
No raw Metadata/URL/token fields stored.
Canonical entry: [media presets](../../functions/media-presets/COMMANDS.md).
