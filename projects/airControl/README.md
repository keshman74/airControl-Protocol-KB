# airControl — desktop / будущее mobile

ID: `PRJ-AIRCONTROL`. [Исходники](https://github.com/keshman74/airControl).

Подтверждённые контрольные точки: v5.0.0 A33 native presets и macOS ARM64 DMG; A98 active preset eventing с внешнего WiiM Home. Windows installer и mobile этим не проверены. A97 UPnP volume — требование будущего переноса, не выполненная desktop/mobile интеграция.

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
