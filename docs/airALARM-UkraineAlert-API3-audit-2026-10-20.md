# airALARM — аудит Ukraine Alert API 3.0 и рекомендации (20.10.2026)

> **Статус:** изучение источников и исходника airALARM v0.1.28, **не** аппаратная проверка новых методов, не подтверждение работы облачного сервиса. Основная нормативная база проекта: [Ukraine Alert API Swagger v3.0](https://api.ukrainealarm.com/swagger/index.html) и локально предоставленный снимок OpenAPI (`Ukraine-Alert-API.txt`). Для управления акустикой — [airControl Protocol KB](https://github.com/keshman74/airControl-Protocol-KB). Аппаратно рабочая v0.1.28 сохраняется как baseline.

## Источники: подтверждённое и оговорки

1. Пользовательский OpenAPI 3.0.4, `info.version: 3.0`, `info.contact: Stfalcon/support@stfalcon.com`, `securitySchemes.Token`: `apiKey`, заголовок `Authorization`, без обязательного префикса Bearer. Ключ предоставляется после регистрации. Не добавлять префикс без указания поставщика.
2. [Официальная страница получения API-ключа](https://api.ukrainealarm.com/) содержит форму заявки. [Публичный договор оферты](https://api.ukrainealarm.com/contract.pdf) (2023): п.1.1.6 определяет «Запит» как успешный HTTP-вызов **или полученный WebHook**; п.1.1.8 описывает публичный сервис с уникальным публичным IP (для Cloudflare Workers это требует уточнения у поставщика), п.4.1 требует согласования заявки, п.4.4–4.5 ограничивает использование; п.5.1 на дату текста обозначает API услугу бесплатной; п.7.3–7.4 не гарантирует своевременность/доступность уведомлений и исключает гарантию пригодности для критического оповещения. Условия могут меняться, проверять действующую редакцию.
3. [Официальная организация UkraineAlarm на GitHub](https://github.com/UkraineAlarm) содержит сгенерированные клиенты [JS](https://github.com/UkraineAlarm/UkraineAlarm-javascript), [Python](https://github.com/UkraineAlarm/UkraineAlarm-python), C#, Kotlin и т.д.; они подтверждают операции Token/alerts/status/webhook, но не содержат гарантированного расписания опросов.
4. [Пример от Stfalcon](https://github.com/stfalcon-studio/ukrainealarm-python-client) имеет `time_delay: 60` секунд. Это **пример конфигурации**, НЕ документированное ограничение API и НЕ доказательство допустимости 10 секунд.
5. [Официальный Linux-клиент](https://www.ukrainealarm.com/linux-app) способен запускать пользовательский shell-скрипт на события тревоги/отбоя через `exec_command = true` и `custom_script`. Это **отдельная x86-64 Linux-интеграция**, не встроенный WebSocket/SSE интерфейс API для ESP32. Полезен как эталон сценариев и семантики оповещений.
6. [Cloudflare Durable Objects WebSocket](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) поддерживает server-side WSS и Hibernation API; это отдельный transport **между нашей облачной платформой и ESP32**, а не прямой push-канал Ukraine Alert API.

## Полный перечень endpoints в предоставленной OpenAPI 3.0

| HTTP endpoint | Назначение и модель |
|---|---|
| `GET /api/v3/alerts` | Список `AlertRegionModel[]` активных тревог |
| `GET /api/v3/alerts/{regionId}` | `AlertRegionModel[]` для области/района/громады; `regionId` в path — **string** |
| `GET /api/v3/alerts/status` | `AlertModification{lastActionIndex: int64}`: проверить необходимость обновления полного состояния |
| `GET /api/v3/regions` | `RegionsViewModel{states: RegionViewModel[]}`, рекурсивный список территорий и `regionChildIds` (объявление типа, содержащего массив `RegionViewModel`) |
| `GET /api/v3/alerts/regionHistory?regionId=...` | `RegionAlarmsHistory`; описание — последние 25 тревог, НЕ источник push |
| `GET /api/v3/alerts/dateHistory?date=YYYYMMDD` | `AlertDurationResponse[]`; история |
| `GET /api/v3/geo-data` | `GeaDataResultModel` с air/artillery/urban-fights геоданными, не нужен для текущей текстовой зоны |
| `GET /api/v3/geo-data/all` | Данные для гео-контекста, не обязательны для базовой логики тревоги |
| `POST /api/v3/geo-data/check-coordinates` | `CoordinatesByRegionModel{latitude,longitude,regionId}` → `isInRegion`; опциональное уточнение принадлежности точки |
| `POST /api/v3/webhook` | Регистрация callback, тело `{ "webHookUrl": "https://..." }` |
| `PATCH /api/v3/webhook` | Обновление callback URL |
| `DELETE /api/v3/webhook` | Отмена подписки |

**ВАЖНО:** `GET /api/v3/alerts/status` *не возвращает статус тревоги региона*. Имя endpoint обманчиво. `lastActionIndex` — глобальная метка изменений (точная область действия не специфицирована, так что не считать гарантированно региональной). При изменении проверять реальные данные `GET /alerts/{regionId}`; при неизменном индексе состояние обычно можно сохранить, **но обязательно** периодически сверять полноценный snapshot и сверять сразу после reconnection/boot для защиты от рассинхронизации. Частые изменения по всей Украине могут приводить к дополнительному запросу на каждом цикле.

## Модели и семантика

- `AlertRegionModel`: `regionId:string`, `regionType` (State / District / Community / CityOrVillage / CityDistrict / Null), `regionName`, `lastUpdate`, `activeAlerts: Alert[]|null`.
- `Alert`: `regionId:string`, `regionType`, `type:AlertType`, `lastUpdate`, `activeAlertLevels: AlertLevelWithReason[]|null`. Alert may apply at parent/child scope; verify real responses before inheritance logic.
- `AlertType`: `UNKNOWN`, `AIR`, `ARTILLERY`, `URBAN_FIGHTS`, `CHEMICAL`, `NUCLEAR`, `INFO`, `CUSTOM`. **Never collapse UNKNOWN/INFO/CUSTOM to AIR**. More than one type may be active concurrently.
- `AlertLevel`: `Red`/`Yellow`; `AlertLevelWithReason` contains `alertLevel`, `reason`, `createdAt`. A change of reason or severity while type remains active can matter to alert playback and web display even if boolean typeActive is unchanged.
- `WebHookMessageModel`: `status:string|null`, `regionId:int32`, `alarmType:string|null`, `createdAt`, `alertLevel:string|null`, `reason:string|null`, `activeAlertLevels[]`. Unlike REST `regionId:string`, webhook `regionId` is declared **int32**. Normalise before comparing. Values of `status` are NOT enumerated in the provided model: do not assume literal START/END, isActive, etc., without provider docs/live signed sample.
- WebHook registration model only has `webHookUrl`, and no per-region subscription filter is documented; filter by region/type in our cloud relay, but confirm callback registration cardinality and global-vs-regional event scope with provider.
- Authentication to **call API** uses `Authorization: <api-key>`, NOT automatically the authenticity check for **callbacks from API to us**.

## WebHook documentation gap — must close before production

OpenAPI operations `/api/v3/webhook` explicitly link:
- `https://api.ukrainealarm.com/webhook-signature-validation.html`
- `https://api.ukrainealarm.com/webhook-message-model.html`

Both could **not** be retrieved by available web lookup (2026-10-20). Therefore UNKNOWN: actual signature header/key derivation, accepted clock skew, exact start/stop `status` values, ordering/duplication/retry policy, callback timeout, subscriptions per key. **DO NOT use generic HMAC-SHA256 implementations copied from unrelated providers.** Request documents or signed non-production sample from support@stfalcon.com. A shared secret in a private callback URL can be an added barrier but does not replace official signature verification or snapshot reconciliation.

## API request rate — no verified 10-sec allowance

The OpenAPI supplied does NOT state a numeric request limit. Stfalcon example `time_delay:60` is not a protocol rule. A 10-second request cadence is **6/minute = 8,640/day per always-on ESP32**. At scale across zones/devices under one key load escalates. If polling `status` every 10s, extra `/alerts/{regionId}` calls when index changes can add requests. Implement 429 `Retry-After`/backoff, jitter across devices, direct API recheck after network restore; request a written **approved rate and key/account limits** from Stfalcon. Do not borrow rate limit numbers from alerts.in.ua or Hosting Ukraine — they are different services.

## airALARM v0.1.28: concrete source audit

Inspected local complete `/mnt/data/airALARM_v0.1.28/src/main.cpp` (hardware-working baseline):
1. `POLL_MS=30000` and `pollApi` requests `GET /api/v3/alerts/{regionId}` each cycle. Experimental POLL10 variant changes cadence; neither current version uses `/alerts/status` index or WebHook yet.
2. `pollApi` uses `WiFiClientSecure::setInsecure()` — **TLS certificate is not verified**, unacceptable on public Internet for safety alert commands. Replace with verified CA trust before field release. WebUI and OTA credentials need their own security assessment.
3. Parses `AlertRegionModel[]` as first item only (`root[0]`), requires exact selected `regionId`, treats `activeAlerts` JSON as array. Before changing regional coverage, record real shapes for state/district/community and ancestor-level alerts. Invalid/empty/null responses must not automatically clear a true alarm without verified authoritative reconciliation.
4. Distinguishes 8 `AlertType` values; stores `Red/Yellow` and `reason`. **But** audio events are queued solely on typeActive boolean changes; subsequent severity/reason modifications during active alert do not automatically enqueue an updated audio announcement. Severity escalation policy must be explicit.
5. On first valid API response after boot, `stateInitialized` becomes true but **does not enqueue alert announcement** even when already active. User needs explicit configurable startup/reconnect recovery behavior to avoid silently missing an in-progress active alert; avoid replay storms by persisting last processed event identity, timestamps, and boot baseline policy.
6. `TYPE_AUDIO_GAP_MS=65000` blocks event queue, and `dispatchTypeQueue` is FIFO. User requires urgent alarm > scheduled «Хвилина мовчання», no waiting 65 seconds. Implement separate priority path + cancellation + idempotency, test A31 prompt cancellation and A33 behavior before claiming audio preemption.
7. Next web UI needs active/source/age and connection status `PUSH CONNECTED / POLLING / STALE`, last confirmed snapshot, timestamps and type badges, with local SSE/WebSocket or controlled lightweight refresh.

## Recommended production evolution (not yet implemented)

- **Primary:** Stfalcon official WebHook → publicly reachable **Cloudflare Worker** validating **provider-specific** signature + payload, region and type; resilient state store (Durable Object); event log with nonce/id, monotonic timestamp and dedupe; WSS broadcast to authenticated ESP32 clients (outbound connection from local Wi-Fi).
- **Fallback:** authorized, rate-limited direct ESP32 REST GET `/alerts/status` every 10s *only if permitted by provider and configured conditions*; fetch full regional snapshot when changed and periodically even when unchanged; immediately on boot/reconnect. When cloud push healthy, run less frequent reconciliation to minimize API requests.
- **Alert logic:** compare typed active level sets and `createdAt/lastUpdate`; preserve priority and old Master-volume return sequence for hardware-confirmed A31; do not let scheduler block prompt. Full alarm event should atomically update relays, web UI and queue with clear status FRESH/STALE. Do not suppress boot alert by default without a documented user policy.
- **Cloudflare specifics:** Durable Objects Hibernation WebSockets saves compute during idle; cloud pricing/free usage and key/registration policy must be tested. Provider's public service unique-IP definition should be checked against shared Anycast IP for workers.
- **Legal/safety:** contract says API provided AS IS; airALARM should be supplemental, not sole life-safety infrastructure unless separately designed, tested and approved. Require power/network fault telemetry and operator-visible stale indication.

## Questions for Stfalcon support (ask without disclosing private API key)

1. Is a 10-second GET `/alerts/status` allowed per API key? What requests/minute/day and aggregate key/device limits apply? Is `lastActionIndex` national/global or regional, and monotonic through service restarts?
2. Please provide working `webhook-signature-validation.html` and `webhook-message-model.html`, header names, signature verification example, sample genuine signed payload for start, end and severity update. What are retry and timeout guarantees?
3. Is WebHook one callback per token? Are events sent for all Ukraine or filterable by region? Does `status` have defined enums? Any ordering guarantee? How should duplicates be handled?
4. Is Cloudflare Workers callback URL on shared global IP acceptable under the offer's «публічний сервіс ... унікальна IP адреса» definition? Is optional domain/registration requirement?
5. Are there recommended publication latency/availability targets or status feed alternatives for embedded devices? Is the official Linux client's transport accessible as a public API?
