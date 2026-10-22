# Compatibility Matrix

| Capability | A31 | A97 | A98 | A33 |
|---|---|---|---|---|
| Basic player control | CONFIRMED | PARTIAL | PARTIAL | CONFIRMED |
| Volume / mute | CONFIRMED | PARTIAL | PARTIAL | CONFIRMED |
| EQ | MCU :8899 confirmed/implemented | UNKNOWN | separate HTTP EQ implemented; verify per command | UNKNOWN |
| USB | CONFIRMED | no USB on test hardware | no USB on test hardware | DOCUMENTED/needs hardware test |
| Native Multiroom | CONFIRMED | CONFIRMED | family support; verify device-specific | ACS2 separate architecture |
| Online TuneIn | observed in ecosystem | — | — | CONFIRMED/CAPTURED |
| Online Qobuz | artwork/playback evidence | — | artwork confirmed | CONFIRMED/CAPTURED |
| Spotify Connect | — | — | — | ADVERTISED |
| Discovery | Linkplay discovery/status | Linkplay | Linkplay | UDP + SSDP + mDNS captured |


## Scoped corrections — 2026-10-22

Старая матрица выше — обзор, не исчерпывающая command-by-command проверка. Приоритет имеют следующие адресные результаты; firmware, если не указан в источнике, unknown.

| Возможность | A31 | A97 | A98 | A33 |
|---|---|---|---|---|
| RenderingControl SetVolume | не перенесено из A97 | CONFIRMED tested HTTP49152/KNOB0.8.23 | не перенесено из A97 | не перенесено из A97 |
| getPresetInfo HTTPS | REJECTED в preset research | REJECTED tested Кухня | CONFIRMED tested .21 | другой API |
| List/launch presets | GetKeyMapping; native KNX slots1/2 CONFIRMED | GetKeyMapping49152/59152 + HTTPS launch CONFIRMED | HTTPS + events desktop CONFIRMED | HTTP choice1/2/list и native03 76/03 70 CONFIRMED |
| HTTPS8443 Prompt | не ACS2 | не ACS2 | не ACS2 | CONFIRMED tested prompttone/download/play |
| Отдельный alert уровень | software gain/temporary master tested; physical independence unknown | не установлено | не установлено | WAV :10 tested; full independence matrix unknown |
| Native KNX persistent files | CONFIRMED install; autostart unknown | не установлено | не установлено | не установлено |

Источники: [A97 volume](../protocols/upnp/A97-VOLUME.md), [A97 presets](../protocols/upnp/playqueue/A97-PRESETS.md), [A98 presets](../protocols/wiim-httpapi/A98-PRESETS.md), [A33 HTTP](../tests/A33-PRESETS-HW-2026-10-10.md), [A33 native](../protocols/a33-native-23040/COMMANDS.md), [notifications](../functions/notifications/README.md), [A31 install](../devices/A31/KNX_MAPPING_TABLE.md).

Машинные уточнения: [KB_DECISIONS.json](KB_DECISIONS.json). CONFIRMED для одного endpoint/действия не повышает всё семейство. PARTIAL/UNKNOWN — полнота покрытия, а не замена шести статусов доказательств.
