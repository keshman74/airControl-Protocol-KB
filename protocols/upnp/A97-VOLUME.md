# A97 RenderingControl volume — 2026-10-20

Status: **HARDWARE-VERIFIED GetVolume and KNOB0.8.23 volume control with user-confirmed responsiveness improvement on the tested A97**.
Device: Кухня,192.168.0.99, classified A97. Exact player firmware/project not supplied in this experiment.

## Advertised endpoints
The namespace-tolerant description diagnostic returned HTTP200,3125 bytes, five service declarations on each of49152 and59152.
RenderingControl service:
`urn:schemas-upnp-org:service:RenderingControl:1`

On each port P:
- `http://192.168.0.99:P/upnp/control/rendercontrol1`
- SCPD `http://192.168.0.99:P/upnp/rendercontrolSCPD.xml`
- event `http://192.168.0.99:P/upnp/event/rendercontrol1`

The action experiment below used **port49152 only**. Advertisement on59152 does not itself confirm action execution there.

## Actual SCPD inputs and successful requests
- GetVolume: InstanceID, Channel.
- SetVolume: InstanceID, Channel, DesiredVolume.
- Tested InstanceID0, ChannelMaster, DesiredVolume94.

HTTP POST controlURL, Content-Type text/xml; charset=utf-8.
SOAPAction for reads:
`"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"`
SOAPAction for writes:
`"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"`

SetVolume request used:
```xml
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><u:SetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1"><InstanceID>0</InstanceID><Channel>Master</Channel><DesiredVolume>94</DesiredVolume></u:SetVolume></s:Body></s:Envelope>
```

GetVolume uses the same envelope with GetVolume, InstanceID0 and ChannelMaster, omitting DesiredVolume. Readback field CurrentVolume.

## User terminal result — Mac to A97
| Operation | Time | Returned/sent level |
|---|---:|---:|
| GetVolume1 | 12ms | 94 |
| GetVolume2 | 23ms | 94 |
| GetVolume3 | 15ms | 94 |
| SetVolume | 15ms | 94 |
| GetVolume readback | 14ms | 94 |

The script validated expected SOAP action-response elements, rejected SOAP Fault, and printed Проверка уровня: OK.
Thus the service read succeeds and same-level SetVolume is accepted with matching readback. This terminal experiment did not change the level; subsequent KNOB0.8.23 volume-control confirmation is recorded below. Do not promote this to all A97 products/firmware or claim ESP32 request latency15ms.

## Integration rules
- Use this separate HTTP UPnP channel for A97 volume, retaining selected HTTPS443 for the Linkplay /httpapi.asp API and confirmed preset launches.
- A97 current known compatible path is HTTP49152 RenderingControl. Do not use A31 TCP or globally downgrade HTTPS based on this evidence.
- Keep only the latest absolute0..100 target and serialize sends. No GetVolume/readback round-trip is required for each encoder step.
- Accept complete valid SetVolumeResponse only, reject Fault even under HTTP200.
- A compatibility fallback may use the existing absolute HTTPS volume command; repeated failed SOAP probes must be paced/cached per zone.
- EventSubURL advertisement alone does not establish successful subscription or volume NOTIFY payload parsing.
- This evidence supports an implementation candidate for other controllers/projects, but each integration must preserve model-specific fallback and undergo its own hardware test.

## KNOB implementation
0.8.23 uses the existing background volume worker for A97 SOAP SetVolume, retaining latest-target coalescing and120ms dispatch minimum. SOAP failure falls back to HTTPS and suppresses new SOAP attempts for30s for that IP/zone generation. A98, A31/A33, preset commands and active-state logic remain unchanged.
Source: https://github.com/keshman74/airKNOB/commit/2e1d6a081c2d6decf53537e2b55ffb8f8092ff89
Build/test run: https://github.com/keshman74/airKNOB/actions/runs/39497192418
Status: IMPLEMENTED / HOST-TESTED / BUILD-PASSED. All CI steps passed and main OTA0.8.23 is published. Binary:https://raw.githubusercontent.com/keshman74/airKNOB/main/firmware/airControl-KNOB-v0.8.23.bin; 1352544 bytes; MD58f21b45befc034e4e46924babbc5823a. KNOB0.8.23 volume control and qualitative responsiveness improvement are user/hardware-confirmed on the tested A97 (follow-up2026-10-21).

Related baseline evidence: [KNOB0.8.22 optimization](../../integration/KNOB-WIIM-OPTIMIZATION-v0.8.22.md).

## KNOB hardware confirmation and cross-project rule — 2026-10-21
After0.8.23 was published with A97 RenderingControl volume, the user confirmed: «да так гораздо быстрее!» and explicitly asked to retain this approach for other projects, including airControl desktop and its future mobile version.

Promote the tested A97 KNOB volume-control path to **USER/HARDWARE-VERIFIED WORKING WITH NOTICEABLE SPEED IMPROVEMENT**. This is qualitative feedback; no new /health timing, exact improvement ratio, tested-volume range or long-duration stability measurement was supplied. The earlier15ms is still the Mac SOAP measurement, not a measured KNOB command time.

Project reuse decision: for a compatible A97, prefer the separate RenderingControl SetVolume path with HTTPS fallback, latest-target coalescing and paced per-zone failure handling. Preserve HTTPS for other Linkplay commands. Apply this design to future airControl desktop/mobile and other project integrations; those integrations are planned, not already implemented or hardware-verified by this KNOB result.

Reusable implementation requirements and evidence boundaries: [A97 volume reuse rule](../../integration/A97-VOLUME-REUSE.md).
