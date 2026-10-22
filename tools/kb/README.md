# Повторяемый аудит KB

Python 3, только стандартная библиотека, без сети и доступа к устройствам.

```bash
python tools/kb/audit.py --write
python tools/kb/audit.py --check
python -m unittest discover -s tools/kb -p 'test_*.py'
```

Генерирует inventory с SHA256, каталог каждого CSV ID + контекстные document-only записи, все ID→упоминания и findings. Исторические CSV не переписывает. Режим --check блокирует новые дубли ID (кроме одной точной хешированной коллизии), повреждённый CSV/пустые обязательные поля, отсутствие технического view, внутренние Markdown ссылки/anchors, неизвестные статусы контекстных решений, источники несуществующих claim, несовместимые CONFIRMED/REJECTED одного точного контекста и устаревшие generated outputs.

330 legacy ID без отдельного поля Source показываются предупреждениями, а не скрываются. Они имеют technical views, но это не подтверждение первичного provenance. Пустое notes допустимо. Найденные одинаковые device+protocol+mechanism с разными ID — кандидаты на ручное сравнение, не автоматический merge.

Семантическое противоречие свободного текста/старой Markdown-матрицы полностью автоматически не определяется. Проверка совместимости применима к структурированным `contextual_evidence` в [KB_DECISIONS](../../registry/KB_DECISIONS.json); старые таблицы сверены вручную в [KB_CONFLICTS](../../KB_CONFLICTS.md). Глобальная лексическая замена статусов запрещена. Remote URL, наличие внешнего ZIP и действительность ссылок на Mac не проверяются offline. Inventory исключает собственные generated files и .git, поэтому outputs детерминированы.

[Главный индекс](../../KB_MASTER_INDEX.md).
