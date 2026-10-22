# airALARM — ESP32

ID: `PRJ-AIRALARM`. Репозиторий исходников airALARM пока не установлен по содержимому KB; не выдумывать ссылку.

Текущая документальная rollback-точка: v0.1.29_MENU_TEST по явному решению пользователя в API3 audit. 1.4 WiFi — source test candidate; не объявлять стабильной по имени архива. Исходный handoff предварителен. Поведение A31 временного master и A33 WAV описано в общей функции уведомлений. Длительная проверка восстановления, конфликт ручной громкости и независимый физический gain остаются открытыми. API3 webhook signature/rate policy не установлены; 120 s — восстановленная договорённость кандидатов 0.1.31/32, не подтверждённая квота провайдера. Проверка ZIP/сборок вне KB этим аудитом не выполнялась.

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
