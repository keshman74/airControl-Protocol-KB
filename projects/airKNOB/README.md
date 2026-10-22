# airControl KNOB / airKNOB — ESP32-S3

ID: `PRJ-AIRKNOB`. [Исходники](https://github.com/keshman74/airKNOB).

Проверенные в KB checkpoints: discovery 0.8.5; A31 MaxNumber21 fix 0.8.18; A98 menu restart fix 0.8.19; A97 presets 0.8.21; A98 качественное ускорение 0.8.22; A97 UPnP volume 0.8.23. Это разные испытания; они не доказывают одновременно полную стабильность последней версии. A98 eventing protocol подтверждён в desktop, KNOB port остаётся отдельно отмеченным host-tested candidate.

## Общие канонические исследования

- [Громкость, протокол и границы A97](../../protocols/upnp/A97-VOLUME.md) · [правила переноса](../../integration/A97-VOLUME-REUSE.md).
- [Уведомления, отдельная громкость и восстановление](../../functions/notifications/README.md).
- [Discovery](../../registry/FAST_ZONE_DISCOVERY.md).
- [Несколько контроллеров](../../functions/concurrent-control/README.md).
- [Пресеты](../../functions/media-presets/COMMANDS.md) · [A33 HTTP hardware](../../tests/A33-PRESETS-HW-2026-10-10.md) · [A33 native](../../protocols/a33-native-23040/COMMANDS.md).
- [Multiroom](../../functions/multiroom/README.md) · [runtime services](../../registry/STREAM_CAPABILITIES.md).
- [Native A31 KNX](../../devices/A31/NATIVE_KNX.md) · [mapping/install](../../devices/A31/KNX_MAPPING_TABLE.md).
- [Совместимость](../../registry/COMPATIBILITY.md) · [конфликты/следующие тесты](../../KB_CONFLICTS.md).

[Главный индекс](../../KB_MASTER_INDEX.md) · [Двусторонняя карта](../../KB_CROSS_PROJECT_MAP.md).

Ссылки обозначают зависимость/возможность повторного использования, не автоматическую синхронизацию исходников, реализацию или аппаратное подтверждение в этом проекте. BIN, Releases и OTA этим аудитом не меняются.
