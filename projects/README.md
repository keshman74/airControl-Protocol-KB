> Актуальные проектные страницы и двусторонняя матрица: [KB_CROSS_PROJECT_MAP](../KB_CROSS_PROJECT_MAP.md). [airControl](airControl/README.md) · [airALARM](airALARM/README.md) · [KNX Gate](knx-gate/README.md) · [airKNOB](airKNOB/README.md). Таблицы ниже сохранены как предварительная карта.

# airControl KB — единая карта проектов и перекрёстных исследований

**Статус:** навигационный индекс. Канонические протоколы, команды и доказательства остаются в существующих `devices/`, `protocols/`, `functions/`, `registry/`, `evidence/`. Не дублируйте их в проектных папках.

## Проекты
| Проект | Исходный код | Документация и общие исследования |
|---|---|---|
| airControl (desktop) | [keshman74/airControl](https://github.com/keshman74/airControl) | [Интеграции](../integrations/PROJECTS.md), [протоколы](../protocols/) |
| airALARM (ESP32) | Репозиторий исходников ещё не установлен | [Передача контекста](../docs/airALARM_PROJECT_HANDOFF.md), [A31](../devices/A31/), [Linkplay HTTP](../protocols/linkplay-http-https/COMMANDS.md) |
| KNX Gate (ESP32) | [keshman74/airScope-airCloud-KNX-Gate](https://github.com/keshman74/airScope-airCloud-KNX-Gate) | [Интеграции](../integrations/PROJECTS.md), [протоколы](../protocols/) |
| airKNOB (ESP32-S3) | [keshman74/airKNOB](https://github.com/keshman74/airKNOB) | [Быстрый поиск зон](../registry/FAST_ZONE_DISCOVERY.md), [отзывчивость](../integration/KNOB-RESPONSIVENESS.md) |

## Общие темы: одно исследование — несколько проектов
| Исследование | Канонический источник | Где применяется |
|---|---|---|
| Громкость, mute и звуковые сообщения | [A31 commands](../devices/A31/COMMANDS.md), [функции](../functions/), [airALARM handoff](../docs/airALARM_PROJECT_HANDOFF.md) | airALARM, airKNOB, airControl, KNX Gate |
| Обнаружение зон | [Discovery](../registry/DISCOVERY.md), [fast discovery](../registry/FAST_ZONE_DISCOVERY.md) | airControl, airKNOB, KNX Gate |
| A31/A97/A98/A33 команды | [Совместимость](../registry/COMPATIBILITY.md), [устройства](../devices/), [протоколы](../protocols/) | Все проекты |
| KNX управление | [A31 native KNX](../devices/A31/NATIVE_KNX.md), [интеграции](../integrations/PROJECTS.md) | KNX Gate, airControl |
| Проверенные результаты | [Evidence](../evidence/), [чат-реестр](../CHATS.md) | Все проекты |

## Правило пополнения KB
1. Каждое новое наблюдение записывать в `evidence/` с датой, устройством, прошивкой, командой, результатом и статусом проверки.
2. Подтверждённую команду/функцию фиксировать **один раз** в канонической странице `functions/`, `protocols/` или `devices/`, добавляя ссылку на evidence.
3. Проектные документы содержат ссылки на общие записи и только проектно-специфичные отличия.
4. Обновлять этот индекс и [главный INDEX](../INDEX.md) при добавлении новой темы.
5. Codex перед изменением любого проекта проверяет [INDEX](../INDEX.md), [COMPATIBILITY](../registry/COMPATIBILITY.md) и связанные исследования. Статусы CONFIRMED / DOCUMENTED / EXPERIMENTAL не смешивать.

**Важное ограничение:** ссылки делают знания доступными, но не означают автоматическую синхронизацию всех репозиториев и контекста ChatGPT. Для автоматического индексирования нужен отдельный процесс проверки ссылок и обновления индексов.
