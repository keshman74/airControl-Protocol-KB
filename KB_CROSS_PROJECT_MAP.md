# Межпроектная карта airControl KB

Один технический источник на тему; проектные страницы содержат только ссылки, состояние переноса и отличия.

| Проект | Страница | Исходники / состояние |
|---|---|---|
| PRJ-AIRCONTROL | [desktop/mobile](projects/airControl/README.md) | desktop существует; mobile планируется |
| PRJ-AIRALARM | [ESP32 alerts](projects/airALARM/README.md) | исходный repo не установлен; rollback 0.1.29 по документу |
| PRJ-KNX-GATEWAY | [KNX Gate](projects/knx-gate/README.md) | ESP32 gateway; отдельно native A31 |
| PRJ-AIRKNOB | [KNOB](projects/airKNOB/README.md) | ESP32-S3 |

## Исследование → использующие проекты

Обозначения: **H** — конкретный интегрированный результат аппаратно проверен (см. источник и контекст); **I** — реализация/host tests без полной аппаратной проверки; **R** — повторное использование/перенос, не реализация; **D** — документальная зависимость.

| Каноническое исследование | airControl | airALARM | KNX Gate | airKNOB |
|---|---|---|---|---|
| [A97 volume + fallback](protocols/upnp/A97-VOLUME.md) | R desktop/mobile | R | R | H 0.8.23 |
| [A98 HTTPS optimization](integration/KNOB-WIIM-OPTIMIZATION-v0.8.22.md) | R | R | R | H qualitative 0.8.22 |
| [Уведомления / restore](functions/notifications/README.md) | R | H A31/A33 в указанных тестах | R | R |
| [Progressive discovery](registry/FAST_ZONE_DISCOVERY.md) | I source reference | R; собственный UI/поиск проверялся отдельно | R | H aggregate 0.8.5 |
| [Несколько контроллеров](functions/concurrent-control/README.md) | H A98 preset highlight; предел клиентов unknown | R restore conflict | D | D |
| [A33 HTTP presets](tests/A33-PRESETS-HW-2026-10-10.md) | R | R | R; scheduling recommendation | I, отдельные feedback в функции |
| [A33 native presets](protocols/a33-native-23040/COMMANDS.md) | H v5.0.0 | R | R | R; не переносить desktop confirmation |
| [A97 presets](protocols/upnp/playqueue/A97-PRESETS.md) | R | R | R | H 0.8.21 |
| [A98 active preset events](protocols/wiim-httpapi/A98-PRESETS.md) | H v5.0.x | R | R | I 0.8.15 |
| [A31 native KNX](devices/A31/NATIVE_KNX.md) | D | D | D, отдельный native runtime | D |
| [Multiroom](functions/multiroom/README.md) | H scoped Linkplay; ACS2 separate | D | D | D |
| [Online service capabilities](registry/STREAM_CAPABILITIES.md) | D/runtime | D/runtime | D/runtime | D/runtime |
| [Firmware/OTA checkpoints](projects/airALARM/README.md) | own packaging | 1.4 candidate | own mechanism | own checkpoints |

Обратные ссылки добавлены в общие страницы и проектные разделы. Старые каталоги `integration/` (технические заметки) и `integrations/` (подключение проектов/чатов) сохраняются с разными ролями. [projects/README](projects/README.md) и [integrations/PROJECTS](integrations/PROJECTS.md) ссылаются сюда вместо ведения второй проектной матрицы. Реестр конкретных чатов — [CHATS.md](CHATS.md).
