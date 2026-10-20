# A97 presets — hardware readback, 2026-10-20

Canonical ID: QRY-A97-UPNP-KEY-MAPPING.
Status: **HARDWARE CONFIRMED READ, KNOB DISPLAY AND PRESET LAUNCH on the tested device**.

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
- The initial terminal experiment only read presets. The subsequent KNOB0.8.21 hardware test confirmed display and launch (see confirmation below): the implemented launch path is HTTPS443 /httpapi.asp?command=MCUKeyShortClick:N. No A31 TCP preset command is established by these tests.
- A98 PlayQueue/AVTransport/getAllRoutines active-preset correlation is not established for A97 by this experiment.
- KNOB0.8.21 list display and preset launch are now hardware-confirmed on this tested A97. This does not establish support for every A97 product/firmware.

Provenance: user terminal output in the airControl KNOB development conversation on2026-10-20, following the read-only advertised-service/SCPD diagnostic. No service tokens, serials or raw media metadata are included here.


## KNOB implementation checkpoint — 0.8.21
- Implemented in airKNOB main, source commit 56b3224fecb0aceace7e3d00e1ceea2e7b8c6eca (including the preceding feature commit).
- A97 list read tries HTTP SOAP GetKeyMapping on port49152, then59152. A valid empty mapping is accepted. getPresetInfo remains only a final compatibility fallback when both SOAP reads fail.
- Original KeyN identities are retained; the A97 menu exposes supported slots1–12, with bounded response/storage handling and serialized deferred reads. /health reports preset_source and preset_port.
- Existing A31, A33 and A98 paths are preserved; regression tests cover their separate read routes. A97 host tests cover both SOAP ports, fallback, malformed replies, empty/error handling and original slot limits.
- GitHub Actions build and tests passed: https://github.com/keshman74/airKNOB/actions/runs/39488634901
- Published OTA version:0.8.21; binary https://raw.githubusercontent.com/keshman74/airKNOB/main/firmware/airControl-KNOB-v0.8.21.bin (1344976 bytes; MD5 afbe7a1cab3cffcfe4632b25e28986e9).
- Subsequent user hardware confirmation validates firmware list display and preset launch on the tested A97; see below.

## Hardware confirmation — KNOB0.8.21, 2026-10-20
The user confirmed after the published0.8.21 update: «работает! Прессеты отображаются и запускаются!».

- Tested setup: A97 zone Кухня,192.168.0.99; KNOB192.168.0.41, firmware0.8.21 in the current test sequence.
- Confirmed outcome: preset names appear in the KNOB menu and selecting a preset starts playback.
- Successful integrated scheme: read using PlayQueue GetKeyMapping over HTTP UPnP; launch using the unchanged selected HTTPS443 HTTP API command MCUKeyShortClick:N, preserving the original KeyN slot number.
- Launch request form: `https://192.168.0.99/httpapi.asp?command=MCUKeyShortClick:N` (N is the original supported preset slot).
- The user did not enumerate individual tested slots, supply a new packet trace, or report per-command timings. Do not claim every slot1–12 was tested or infer exact response text.
- Active-preset tracking for changes from other controllers and A98-style routine/input correlation remain unverified for A97.
- This confirmation supersedes the earlier pending status for KNOB list integration and launch, while retaining the negative getPresetInfo result.
