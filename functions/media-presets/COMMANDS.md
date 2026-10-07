# Media presets command view

- `CMD-A31-MCU-PRESET` — **media preset** — `MCU+KEY+<001..010>` — **IMPLEMENTED/NEEDS-HW-EVIDENCE**
- `QRY-UPNP-RC-LIST-PRESETS` — **list rendering presets** — `ListPresets(InstanceID) -> CurrentPresetNameList` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-RC-SELECT-PRESET` — **select rendering preset** — `SelectPreset(InstanceID, PresetName)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `CMD-UPNP-PQ-SET-KEY-MAPPING` — **preset/key mapping** — `SetKeyMapping(QueueContext)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
- `QRY-UPNP-PQ-GET-KEY-MAPPING` — **preset/key mapping** — `GetKeyMapping() -> QueueContext` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**
