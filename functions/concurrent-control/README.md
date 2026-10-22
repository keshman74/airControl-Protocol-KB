# Совместная работа нескольких контроллеров

Использующие проекты: [airControl](../../projects/airControl/README.md), [airALARM](../../projects/airALARM/README.md), [airKNOB](../../projects/airKNOB/README.md), [KNX Gate](../../projects/knx-gate/README.md).

Требование: родное приложение, desktop, KNOB и автоматика управляют устройствами без обязательного координатора. KB не устанавливает измеренное максимальное число параллельных TCP-соединений A31.

| Канал | Доказательство | Ограничение |
|---|---|---|
| A31 TCP 8899 | [Официальный источник](../../evidence/official-docs/ARYLIC-TCP-API.md): одна связь на client IP, интервал минимум 200 ms | DOCUMENTED; это не лимит «один клиент вообще», не результат нагрузочного теста разных IP |
| A31 volume/events | [Состояние/last target](../../registry/BEHAVIOR_RULES.md), [native KNX](../../devices/A31/NATIVE_KNX.md) | KNX repeat 90 ms в config не доказывает соблюдение 200 ms на wire; требуется capture |
| A97 UPnP volume | [Проверка](../../protocols/upnp/A97-VOLUME.md) | Один background job на зону, coalescing; RenderingControl NOTIFY не проверен |
| A98 external preset changes | [Реальный airControl/WiiM Home тест](../../protocols/wiim-httpapi/A98-PRESETS.md) | Подтверждена синхронизация выделения пресета; не предел throughput/числа клиентов |
| A33 persistent TCP | [Native parser](../../protocols/a33-native-23040/COMMANDS.md) | Ответ 03 70 сопоставлять по Logo; промежуточные события не считать ответом |
| A31 alert restore | [Решение](../notifications/README.md) | Старый snapshot может затереть ручное изменение; политика ещё требует решения |

Повторяемый аппаратный тест: зафиксировать product/firmware и IP каждого клиента, 1/2/3/4 клиента с разных IP и отдельно с одного IP; каждый 90 s, затем длительная сессия. Собирать disconnect/reconnect, фактический wire interval, p50/p95/max ACK/feedback, ошибки, целевую/фактическую громкость, пропуски KNX, непрерывность аудио. Раздельно сравнить HTTP, TCP и UPnP одинаковыми абсолютными целями; не складывать время Mac SOAP с KNOB HTTPS в «коэффициент ускорения».

[Конфликты и тесты](../../KB_CONFLICTS.md) · [Карта связей](../../KB_CROSS_PROJECT_MAP.md)
