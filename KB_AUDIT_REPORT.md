# airControl KB — полный отчёт доступного аудита

Дата: 22 октября 2026. Исходный snapshot main: `193feb477a898142ff9172254f5c24df63324927`. Начальный источник: [предварительный отчёт](evidence/KB-CONSISTENCY-AUDIT-2026-10-22.md). Изменения подготовлены только в отдельной ветке для PR; main/firmware/OTA не изменяются.

## Покрытие и метод

В дереве исходного snapshot **165 файлов**: 163 UTF-8 файла получены через GitHub connector; два WAV проинвентаризированы, не интерпретировались как протокольное доказательство. Полный git checkout совпал с тем же commit. Просканированы все тексты, CSV-поля и ID; отчёты, source audits и приоритетные hardware follow-ups сопоставлены по контексту. Инвентаризация выходного дерева, байты и SHA256 доступны в [inventory](registry/audit/inventory.json).

Все 640 исторических CSV-строк обработаны; **639 уникальных ID**. В каталоге каждому ID доступны исходные строки, legacy status, консервативная классификация, device/protocol/mechanism, technical views и все упоминания. Дополнительные контекстные document-only записи помечены отдельно: они не прибавляются к историческому CSV итогу. [Каталог](registry/audit/catalog.json), [полный occurrence index](registry/audit/occurrences.md).

Это завершённый аудит доступной структуры и согласованности KB, **не новая аппаратная валидация 639 функций**. Машинная обработка всех файлов не означает повторный независимый reverse engineering каждой импортированной команды. Доказательства, имеющиеся только в внешних ZIP, PDF, исходниках приложений или Mac-каталогах, не были заново получены/выполнены. Для части старых строк первичный provenance остаётся неполным; это не скрыто общим статусом «проверено».

## Найдено и исправлено

1. Реальная коллизия ID `RULE-TCP-CONNECTIVITY-FALLBACK-59152`: одинаковый generic helper из двух этапов. Обе строки сохранены; generated identity одна. Диапазоны имён 215–220/215–221 не являются конфликтом содержания. Итоги и исторический MANIFEST пояснены.
2. Разведены canonical views и aliases source/sources, online-service/online-services, presets/media-presets; дополнительные tokens и A33 service context не потеряны. `integration/` и `integrations/` имеют разные роли, обе сохранены.
3. Исправлена трассировка 10 CSV ID, не имевших именованных technical views: TCP8819 details, secure status routing и MoveTracksInQueue теперь имеют явные ссылки/определения.
4. Шесть статусов дополнены независимыми qualifier/source/context полями. CAPTURED, IMPLEMENTED, host-tested и «подтверждён статический разбор» не превращены в аппаратную проверку. Исторические CSV не переписаны.
5. A97 SOAP volume и KNOB0.8.23 качественное ускорение доступны всем проектам. Сохранены HTTPS fallback и model boundaries. Mac SOAP15ms не выдан за ESP32 latency или measured speedup относительно TLS.
6. A33 presets: DOCUMENTED PDF schema unknown не отменяет наблюдаемую hardware schema; Not может сопровождать выбор. Нативные03 76/03 70 и корреляция Logo отделены от ACS2 choice/list.
7. A97 getPresetInfo REJECTED и A98 CONFIRMED представлены как два контекста одной команды. A97 preset read/display/launch follow-up не остаётся «pending» в актуальной сводке.
8. A33 HTTPS8443 Prompt подтверждение добавлено к обзорным страницам. Успешная первая загрузка и повторный400 Exist не смешаны с отсутствием поддержки.
9. airALARM: различены software gain, временный master и ещё не решённая физическая независимость. Сохранены WAV Failed, OK без volume effect, wrong-IP correction, ~2s radio leakage, static/live distinctions и invalid grep V1.
10. Handoff уточнён конкретным более полным источником: explicit user baseline0.1.29 + source SHA; 1.4 source candidate. Это решение по качеству и содержимому доказательства, не просто по поздней дате.
11. A31 native KNX persistent file install не назван autostart/whole firmware flash. CSV/Mute, v0.9 volume и v0.10 slots1/2 сохранены в пределах соответствующих тестов.
12. Реестр [24 вопросов/конфликтов](KB_CONFLICTS.md) сохраняет rationale, источники и тесты; [карта проектов](KB_CROSS_PROJECT_MAP.md) отличает внедрение от возможности переноса.

## Автоматические проверки

[CLI и инструкции](tools/kb/README.md); GitHub Actions запускает тот же offline audit и unit tests. Проверяются ID/CSV/обязательные поля, дубли с точным исключением, ссылки/anchors, наличие technical views, source existence и статусы контекстных решений, противоречия одного точного контекста, freshness generated outputs. Отчёт [findings](registry/audit/findings.json) сохраняет предупреждения.

Первичный проход: одна повторная ID, десять ID без technical view, одно пустое optional notes; реально неработающих inline Markdown path links исходного дерева не обнаружено. Пустой notes допустим и не заполнялся выдуманным ответом. **330 уникальных legacy ID не имеют explicit Source в исходной строке**; остальные309 из community OpenAPI имеют Source. Ссылка на technical view/чат-аудит помогает навигации, но не выдаётся за найденный первичный capture. Дефицит provenance остаётся открытым KB-C23.

Свободные формулировки и семантические конфликты требуют ручного анализа. Проверка не гарантирует существование внешнего ZIP/URL и не проверяет полноту каждого vendor API. Community OpenAPI не назван official hardware proof; A97/A98 imports остаются кандидатами.

## Что сохранено

Все исходные файлы и CSV-строки, старые version milestones, отрицательные/неполные испытания, source qualifiers и ограничения. Для изменённых обзоров применены пояснения и адресные follow-ups; для V1 SUPERSEDED относится только к invalid grep-разделам. Исходные WAV и shell для аудио не менялись. Не производились команды устройствам, flash edits, OTA/Release публикации или изменения других репозиториев.

## Нерешённое и следующий шаг

- A31 физическая независимость alert уровня, точное окончание MP3, восстановление после network loss/reboot и политика чужого изменения master.
- A31 TCP multi-client limit, same-IP behavior, реальный wire rate против configured repeat90ms.
- Firmware inventory A97/A98/A33; A97 sustained/fallback/events и тест :59152 SetVolume; перенос на desktop/mobile отдельно.
- A33 все preset slots/прочие записи/автовоспроизведение; A98 KNOB eventing end-to-end.
- Повторные discovery scans с точным inventory и offline/cache/cancellation, KNX multi-zone нагрузки.
- A31 autostart/power-cycle проверяется отдельно; текущее состояние hook stock.
- airALARM archive1.4/installed build, provider polling quotas, webhook signature, исходный repo и недостающие первичные источники.

Полные решения и вопросы владельцу — [KB_CONFLICTS](KB_CONFLICTS.md). Эти вопросы не блокировали независимые документальные этапы. Merge PR — только после проверки владельцем.
