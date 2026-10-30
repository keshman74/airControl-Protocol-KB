# H50 radio: dual UPnP endpoint Play capture (2026-10-30)

**Evidence:** USER-HW-OBSERVED packet capture / APP-CODE-CORRELATED. The H50 was at `192.168.0.106` during this session (previously `192.168.0.100`). Capture: `/private/tmp/h50-rtl-play-106.pcap`, SHA-256 `19aff509a01806774d8423feede4dc5de42e1f0c88860b5be42c215dffb5265a`, 653 packets. The Mac was `192.168.0.104`. Stream URL path tokens and artwork hashes are omitted here.

## Chronological evidence

| Step | Wire evidence | Outcome |
|---|---|---|
| airControl v5.0.11 selects RTL | `POST /upnp/control/rendertransport1` to H50 TCP/49152, `AVTransport#SetAVTransportURI`. DIDL has RTL title, an `upnp:albumArtURI` pointing to airControl's local `/radio-cover/...` proxy and an HLS `TrackURI`. | H50 returns HTTP 200. WiiM Home's later `GetInfoEx` on TCP/59152 reads the same RTL URI and metadata while transport is `STOPPED`. This proves the two endpoints see shared player state. |
| airControl Play | `AVTransport#Play` to TCP/49152, `<InstanceID>0</InstanceID><Speed>1</Speed>`, `Connection: close`, no `ControlSource`. The client sends TCP FIN immediately after the request body. | No successful Play response is visible; subsequent transport state is `STOPPED`. v5.0.11 also attempted `MCU+PLY-PLA` on TCP/8899 without reaching playback. |
| WiiM Home Play on the same loaded RTL URI | `POST /upnp/control/rendertransport1` to TCP/59152 at 01:46:41.833, `AVTransport#Play`, `Connection: keep-alive`, body `<InstanceID>0</InstanceID><Speed>1</Speed><ControlSource>WiiMApp</ControlSource>`. | H50 returns HTTP 200 `PlayResponse` at 01:46:41.840. Later state changes through `TRANSITIONING` to `PLAYING`. Audible output was not independently documented by the PCAP. |

The capture demonstrates a **working Play request over TCP/59152 after airControl's SetAVTransportURI over TCP/49152**. It does not isolate whether the different port, `ControlSource`, keep-alive, or their combination is required. A correct implementation should mirror the captured working request, resolve/verify the TCP/59152 AVTransport service before use, and confirm `PLAYING` by readback. It should preserve `SetAVTransportURI` for the previously observed native-app artwork behavior. The direct `OnlineMusic` PlayQueue attempt in v5.0.13 failed with socket hang up and `STOPPED`, and its artwork did not appear; it must not be considered a verified H50 radio path.

This capture contains no proof that the same dual-endpoint behavior applies to every A97 firmware. No firmware or device settings were changed by the analysis. A v5.0.14 source candidate mirrors the observed sequence. Its RTL result is recorded below.


## airControl v5.0.14 RC1 user hardware result

After the capture-based change, the user tested v5.0.14 RC1 on the H50 and answered that **both RTL sound and its artwork work**. The test question specifically asked whether audio starts without pressing Play in WiiM Home and whether the artwork appears there. This is **USER-HW-VERIFIED for RTL on this H50**. It is independent of the earlier WiiM Home PCAP; no v5.0.14 packet capture was supplied. The release ZIP SHA-256 is `46df441571713a59f338966d8d366e3de1c58041e5c64e23f7de0b6d6029b431`; local source commit `e31e65c`. The capture and user result still do not isolate whether port 59152, `ControlSource`, keep-alive, or their combination is required. The user subsequently reported that **all radio stations and artwork they checked work** in v5.0.14 RC1. This extends **USER-HW-VERIFIED** to the tested H50 stations/covers, but their names and count were not recorded; it does not establish exhaustive directory or codec coverage. Other devices remain **NOT-HW-VERIFIED** for this release.

## Related evidence

- [H50 accepted newTuneIn queue](H50-PLAYQUEUE-NEW-TUNEIN-2026-10-30.md)
- [A97 command view](../../devices/A97/COMMANDS.md)
- [airControl PlayQueue attempts](../application-code/AIRCONTROL-A97-PLAYQUEUE-RADIO-CORRECTION-2026-10-29.md)
