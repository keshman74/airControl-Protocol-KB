# Журнал изменений airControl KB

## 22 октября 2026 — согласование базы, отдельная review-ветка

Основание: main `193feb477a898142ff9172254f5c24df63324927`, предварительный consistency audit сохранён.

- Главный индекс, четыре проектные страницы, двусторонняя карта потребителей, AGENTS и единая политика шести статусов.
- 640 строк/639 уникальных ID вместо ошибочного текущего итога634. Исторические CSV полностью сохранены; одна коллизия ID разрешена как одна сущность с двумя исходными строками и хешированной оговоркой.
- Уточнены A97 UPnP volume, A97 rejected/A98 confirmed getPresetInfo, A97 presets0.8.21, A33 HTTP/native presets, A33 HTTPS Prompt, airALARM rollback0.1.29 vs 1.4 candidate, A31 persistent install vs autostart.
- Канонические views sources, online-services, media-presets дополнены; старые alias-файлы и строки сохранены.
- Общие функции notifications и concurrent-control связывают проекты с исследованием, сохраняют отрицательные результаты и открытые вопросы.
- Добавлены структурированные контекстные уточнения, поиск всех ID/упоминаний, inventory/hash и отчёт диагностик. CSV не стал «автоматически CONFIRMED».
- Offline CLI, meaningful regression tests и CI для повторного аудита. Ограничения первичного provenance и семантической автоматики явно описаны.
- Ни один исходный файл не удалён; firmware/BIN/audio assets/OTA tools, GitHub Releases и другие репозитории не изменялись. PR не объединяется автоматически.
