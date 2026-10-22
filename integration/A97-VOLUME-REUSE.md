# A97 fast volume — cross-project implementation rule
Decision date:2026-10-21. Explicit user request after hardware-confirming KNOB0.8.23: retain the faster approach for other projects, including airControl desktop and the future mobile app.

## Canonical protocol and verified baseline
[A97-VOLUME.md](../protocols/upnp/A97-VOLUME.md) is the canonical request/evidence record.
On tested A97 Кухня192.168.0.99:
- HTTP UPnP RenderingControl :49152 /upnp/control/rendercontrol1.
- SOAP SetVolume with InstanceID0, ChannelMaster and DesiredVolume.
- Terminal GetVolume12–23ms, same-level SetVolume15ms, readback14ms.
- KNOB0.8.23 volume control is now user/hardware-confirmed noticeably faster.
These measurements/observations are distinct. Do not claim15ms KNOB or phone latency, a measured speedup ratio, long-term stability, or all A97 firmware compatibility.

## Required approach when implementing A97 volume elsewhere
1. Route absolute volume through RenderingControl SetVolume on a compatible A97. Resolve the advertised service endpoint when available; port49152 is hardware-exercised on the tested unit. Port59152 is advertised but its volume actions were not tested in this experiment.
2. Keep transport behind the project's device adapter, exposing a common setVolume(zone,level) operation. Desktop and mobile adapters must account for their own runtime networking constraints; working ESP32 connectivity does not by itself establish browser/WebView/phone support.
3. Store one latest absolute0..100 target. Run at most one volume job for that zone; turns/slider movement replace unsent intermediate values. Old completions must not overwrite new UI targets. Handle zone/generation changes and cancellation.
4. Do not add GetVolume or full player-status requests before/after every slider step. Update feedback through separately validated events or existing bounded polling. RenderingControl volume event delivery/payload remains unverified for this A97.
5. Pace sends and retry/capability failures. KNOB's verified implementation baseline is a120ms minimum dispatch interval and30s suppression after a failed SOAP attempt, scoped to IP/zone generation. Do not copy timing values to other platforms without considering their measured behavior.
6. Validate complete SetVolumeResponse and reject SOAP Fault even with HTTP200. Fall back to the selected existing HTTPS absolute-volume command on incompatibility/error; preserve bounds and avoid an unbounded retry queue.
7. Keep Linkplay /httpapi.asp commands, confirmed presets and other controls on their selected HTTPS443 endpoint. This UPnP exception does not authorize globally substituting plain HTTP or A31 TCP.
8. Preserve each other chip's confirmed route: A31/A33 and A98 must not automatically inherit the A97 SOAP implementation without their own evidence and validation.

## Rollout state
| Project | State |
|---|---|
| airControl KNOB0.8.23 | Implemented; CI/build passed; user confirms A97 control is noticeably faster |
| airControl desktop | Required approach for future integration; not claimed implemented by this record |
| airControl mobile | Required approach for future integration; not claimed implemented or hardware-tested |
| Other project controllers/gateways | Reuse protocol and scheduling design with compatible-device detection, fallback and project-specific validation |

Before marking each new integration hardware-verified, check volume changes and reversals, last-target behavior, external-controller synchronization, zone switching and error fallback. Preserve the distinction between protocol evidence, implementation tests and user hardware confirmation.


## Использующие проекты / навигация

[airControl](../projects/airControl/README.md) · [airALARM](../projects/airALARM/README.md) · [KNX Gate](../projects/knx-gate/README.md) · [airKNOB](../projects/airKNOB/README.md).
Состояние переноса, проверки и применимости: [KB_CROSS_PROJECT_MAP](../KB_CROSS_PROJECT_MAP.md). Наличие ссылки не означает реализацию или аппаратное подтверждение в каждом проекте.
