# A97 presets — hardware readback, 2026-10-20

Canonical ID: QRY-A97-UPNP-KEY-MAPPING.
Status: **HARDWARE CONFIRMED READ on the tested device**.

## Device and rejected HTTP API
- Zone: Кухня; IP192.168.0.99; classified A97 by KNOB and identified as A97 by the user.
- Normal selected command endpoint: HTTPS443, /httpapi.asp.
- Exact device hardware/project/firmware strings were not supplied in this capture.
- HTTPS getPresetInfo returned literal unknown command, HTTP200. KNOB0.8.20 independently captured15 response bytes and displayed no preset list.
- This is a confirmed negative result for this product/firmware, not a claim about every A97 product. Do not interpret HTTP200 as API success.

## Advertised PlayQueue and successful read
The user's diagnostic read description.xml, located the PlayQueue service, checked its SCPD for GetKeyMapping, then performed the read-only SOAP call.

Service type:
urn:schemas-wiimu-com:service:PlayQueue:1

Both endpoints successfully returned3538-byte SOAP responses:
- http://192.168.0.99:49152/upnp/control/PlayQueue1
- http://192.168.0.99:59152/upnp/control/PlayQueue1

SOAPAction:
"urn:schemas-wiimu-com:service:PlayQueue:1#GetKeyMapping"

Request body:
```xml
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><u:GetKeyMapping xmlns:u="urn:schemas-wiimu-com:service:PlayQueue:1"/></s:Body></s:Envelope>
```

The diagnostic extracted QueueContext/KeyList, printed MaxNumber21 and the same six named records from each endpoint. Matching printed fields and response lengths do not establish full byte-for-byte identity of the responses or prove that the two ports share one server instance.

## Observed named records
| Key | Stored Name without display-only timestamp suffix |
|---|---|
| Key1 | Nashe Radio Ukraine |
| Key2 | Hit FM Ukraine |
| Key3 | Luv 107.1 |
| Key4 | http://luxwash.co.ua/hvilina/playlist.m3u |
| Key5 | luxlviv |
| Key6 | Local Radio |

Full observed Name suffixes:
- Key1: _#~2026-07-14 02:03:17
- Key2: _#~2026-07-14 02:03:48
- Key3: _#~2026-06-29 15:57:15

Key4 was printed as a URL-valued Name; retain it as the returned label rather than inventing a station name. The remaining displayed names had no printed timestamp suffix.

MaxNumber21 describes the returned mapping capacity/structure; it is not the count of these six named records. Preserve original KeyN identifiers. The diagnostic printed nonempty Name fields only: it does not prove that all other keys are empty in every field, nor exclude routine-backed input presets. Do not infer Key0 -> preset1 or renumber sparse records.

## Integration rules and limits
- For this tested A97, read the list through the confirmed PlayQueue GetKeyMapping path; getPresetInfo must not remain the sole list mechanism.
- The successful read is HTTP SOAP on the UPnP ports, separate from the selected HTTPS443 command endpoint. Do not change normal device control globally to plain HTTP because PlayQueue uses it.
- Read on explicit menu entry/Refresh, serialize with background player requests and retain bounded response/array handling.
- Timestamp removal is a display operation; preserve original key identities.
- This experiment did not launch a preset. HTTPS MCUKeyShortClick:N remains a documented candidate until separately hardware-tested on this A97. No A31 TCP preset command is proven by this readback.
- A98 PlayQueue/AVTransport/getAllRoutines active-preset correlation is not established for A97 by this experiment.
- Hardware verification of the corresponding future KNOB list integration remains pending; this record confirms the direct terminal read, not a firmware fix.

Provenance: user terminal output in the airControl KNOB development conversation on2026-10-20, following the read-only advertised-service/SCPD diagnostic. No service tokens, serials or raw media metadata are included here.
