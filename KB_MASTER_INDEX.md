# airControl KB — главный индекс

Единая точка входа для четырёх проектов. Технические определения остаются на страницах протоколов/функций; свидетельства — в исходных отчётах. Этот файл заменяет роль прежнего INDEX как входной точки, не создаёт второго реестра команд.

- [Карта проектов и общих исследований](KB_CROSS_PROJECT_MAP.md)
- [Конфликты и решения](KB_CONFLICTS.md)
- [Полный отчёт и границы аудита](KB_AUDIT_REPORT.md)
- [Журнал изменений](KB_CHANGELOG.md) · [Инструкции AI](AGENTS.md)
- [Тематический индекс](INDEX.md) · [Источники чатов](CHATS.md)
- [Совместимость](registry/COMPATIBILITY.md) · [Политика доказательств](registry/EVIDENCE_POLICY.md)
- [Реестр команд](registry/COMMANDS.md) · [Контекстные решения](registry/KB_DECISIONS.json)
- [Все ID и упоминания](registry/audit/occurrences.md) · [Машинный каталог](registry/audit/catalog.json) · [Диагностика](registry/audit/findings.json) · [Инвентаризация и хеши](registry/audit/inventory.json)

## Проекты

| Проект | Страница |
|---|---|
| airControl desktop и будущее mobile | [airControl](projects/airControl/README.md) |
| airALARM ESP32 | [airALARM](projects/airALARM/README.md) |
| airScope / airCloud KNX Gate | [KNX Gate](projects/knx-gate/README.md) |
| airControl KNOB / airKNOB ESP32-S3 | [airKNOB](projects/airKNOB/README.md) |

## Приоритетные исследования

| Тема | Канонический источник | Граница подтверждения |
|---|---|---|
| Быстрая громкость | [A97 RenderingControl](protocols/upnp/A97-VOLUME.md), [перенос](integration/A97-VOLUME-REUSE.md) | A97 KNOB 0.8.23 работает; Mac 12–23 ms ≠ ESP32 latency |
| Уведомления и восстановление | [Общая функция](functions/notifications/README.md) | Различать цифровой gain, временный master и независимый физический выход |
| Discovery | [Метод](registry/FAST_ZONE_DISCOVERY.md), [наблюдения](registry/DISCOVERY.md) | KNOB 0.8.5 aggregate confirmation, не все прошивки |
| Несколько контроллеров | [Совместная работа](functions/concurrent-control/README.md) | Предел параллельных TCP-клиентов не установлен |
| Пресеты | [Общая функция](functions/media-presets/COMMANDS.md) | A31/A97/A98/A33 используют разные read/launch/event routes |
| A33 HTTP и TCP presets | [ACS2](protocols/acs2/A33M-V1.2-COMPLETE.md), [тест HTTP](tests/A33-PRESETS-HW-2026-10-10.md), [native](protocols/a33-native-23040/COMMANDS.md) | Not может сопровождать выбор; native Logo не artwork |
| KNX и зоны | [A31 native](devices/A31/NATIVE_KNX.md), [CSV mapping](devices/A31/KNX_MAPPING_TABLE.md) | Native A31 ≠ ESP32 gateway; autostart не активирован |
| Multiroom | [Правила](functions/multiroom/README.md) | A33 ACS2 и Linkplay разделены |
| Сервисы | [Runtime capabilities](registry/STREAM_CAPABILITIES.md), [услуги](registry/SERVICES.md) | Реклама сервиса ≠ API управления |
| OTA | [Границы](projects/airALARM/README.md), [KNOB checkpoints](integration/) | Только ссылки и статусы; OTA не изменялся |

## Устройства и протоколы

[A31](devices/A31/README.md) · [A97](devices/A97/README.md) · [A98](devices/A98/README.md) · [A33](devices/A33/README.md).

[Linkplay HTTP/S](protocols/linkplay-http-https/COMMANDS.md) · [A31 TCP 8899](protocols/mcu-8899/COMMANDS.md) · [UART](protocols/uart/COMMANDS.md) · [диагностика 8819](protocols/communication-8819/COMMANDS.md) · [UPnP](protocols/upnp/COMMANDS.md) · [ACS2](protocols/acs2/COMMANDS.md) · [A33 JSON 1234](protocols/a33-json-1234/COMMANDS.md) · [A33 native 23040](protocols/a33-native-23040/COMMANDS.md).
