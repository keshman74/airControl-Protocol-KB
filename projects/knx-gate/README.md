# airScope / airCloud KNX Gate

ID: `PRJ-KNX-GATEWAY`. [Исходники](https://github.com/keshman74/airScope-airCloud-KNX-Gate).

ESP32 KNX→HTTP/HTTPS и native KNX на Linux A31 — разные реализации. Native A31 v0.9 volume, v0.10 presets 1/2 и v0.11 CSV/Mute не означают проверку соответствующей функции ESP32 gateway. Сохранять A31 TCP/HTTP fallback, направление VOL+/− и отдельный ACS2 A33. Ошибка SEARCH ZONES vs RESCAN из внешнего проекта не считается исправленной этим аудитом: в KB нет достаточного сопоставленного теста новой версии.

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
