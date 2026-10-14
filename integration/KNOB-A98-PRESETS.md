# KNOB A98 preset integration — v0.8.15

Canonical protocol: [A98-PRESETS.md](../protocols/wiim-httpapi/A98-PRESETS.md).
Source: https://github.com/keshman74/airKNOB/tree/a12f4507f4f32e1136cb1498df1e000acd7322cd
Status: IMPLEMENTED / HOST-TESTED, hardware test on KNOB pending.

## List
A98 uses HTTP :59152 PlayQueue GetKeyMapping, retaining full timestamped Name for identity and stripping timestamp only for UI labels.
Key1..Key12 are user slots; MaxNumber21 and higher map records are not user-slot counts.
Nonempty RoutineId is joined to HTTPS/selected-endpoint getAllRoutines by id; when index is present it must agree with KeyN.
Routine name labels the slot; audioInput steps[].payload.input identifies the source. No fixed Key7/8/9 meanings.
Unresolved UUIDs remain labelled Routine N and are not assigned a guessed input.
Empty keys are omitted. A97 keeps getPresetInfo; A31/A33 paths remain separate.

## Active state
Only selected A98 has PlayQueue and AVTransport subscriptions on :59152.
- CurretPlayListName exactly matches a full media KeyN.Name; MusicSource and CurrentIndex are not slot IDs.
- AVTransport CurrentTrackURI / AVTransportURI / PlaybackStorageMedium are normalized for optical, line-in, bluetooth and matched to routine input.
- Transport-state-only STOPPED/PAUSED_PLAYBACK retains input identity.
- PlayQueue TrackNums0 does not resurrect the previous media key after an input change.
- Positive media state can replace an input; positive input replaces stale media.
- Duplicate identities are ambiguous and show no active marker.
- Known getPlayerStatus mode40/41/43 is an input fallback while AVTransport subscription is unavailable.
- Active item is marked with * in Presets. Encoder focus stays independent; external selection does not move the user's menu focus.
- New identities invalidate an old artwork download/cover; downloads reject a result from an earlier artwork epoch.

## Transport and load
Callback listener: KNOB TCP8081, HTTP NOTIFY; WiFiServer is used because Arduino WebServer does not parse NOTIFY.
One incremental client, max2048-byte headers and16384-byte body, bounded per-loop read2048 bytes, stalled client timeout2s.
Only selected player IP, current epoch path and matching SID accepted; duplicate/old SEQ rejected, wrap handled. HTTP200 ACK on accepted complete frames.
Subscriptions requested for600s, renewed at half returned lease; failure retries30s. No rapid retry loop.
Old-zone subscriptions are unsubscribed with bounded timeouts; old epoch notifications rejected.
Model queried on initial A98 setup and menu entry/Refresh, not on each event. Routine data is JSON-filtered; raw responses/secrets are not logged.
Subscription/model maintenance yields to volume, OTA and discovery. Notifications also serviced between artwork chunks.
Endpoint59152 is the hardware-confirmed A98 endpoint; dynamic alternate-port/service-description discovery is not part of this version.
Initial/renewal HTTP operations are synchronous and bounded; this is not a promise of zero UI blocking. Typical external selection is event-driven after subscriptions are established.

## Validation
Host tests compile actual Model/NOTIFY parser, actual callback receiver, actual subscription manager and actual routine loader with ArduinoJson.
Cases: exact timestamp identities, same service/different presets, dynamic routine slots, Cyrillic, media/input cross-type transitions, stale queue, STOPPED-only notifications, mismatched routine index, invalid XML, payload bounds, SID/IP/epoch/SEQ checks, truncated frames, subscription renewal/retry and volume priority.
Required hardware checks: select media1 then5 from WiiM Home; select each configured input, observe stop-without-media for Bluetooth; input->media and media->input; menu marker follows without Refresh; check own KNOB selection still works; change zone/reboot and verify reconnect.
Do not claim all A98 devices or firmware versions work from this checkpoint alone.
