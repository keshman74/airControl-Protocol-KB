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


## Canonical machine-readable OpenAPI URL and menu labels (2026-10-20)

User supplied **direct official OpenAPI JSON**: https://api.ukrainealarm.com/swagger/v3/swagger.json . A live fetch succeeds; document reports `"openapi":"3.0.4"` and `"info.version":"3.0"`. Treat this as the machine-readable canonical Ukraine Alert API 3.0 specification; Swagger UI is https://api.ukrainealarm.com/swagger/index.html . Checked official operations `/api/v3/alerts`, `/api/v3/alerts/{regionId}`, `/api/v3/alerts/status`, `/api/v3/regions`, `/api/v3/webhook` methods POST/PATCH/DELETE. Source reference must not be interpreted as authorization to exceed unpublished rate limits.

**User-requested Ukrainian web UI renames for next version**:
- `Мережа ESP32 — Wi-Fi, DHCP / Static IP` → `Мережа — Wi-Fi, DHCP / Static IP`.
- `Голосові повідомлення — WAV та тест` → `Голосові повідомлення — файли та тест`.
- `Релейні виходи ESP32` → `Релейні виходи` (also section H3).

A source-only **`airALARM_v0.1.29_MENU_TEST.zip`** was generated from `airALARM_v0.1.28_POLL10_TEST` with precisely these four visible text substitutions and UI version label change. Diff verified, ZIP CRC and file count verified; API audio/relay implementation and network configuration untouched. **Not yet PlatformIO compiled or hardware verified**; previous 10-second test cadence remains experimental, not a certified provider API quota. This is an isolated UI patch, **not** completion of planned scheduler, Cloudflare WebHook, OTA or 1-second prompt timing. Working v0.1.28 hardware baseline remains as rollback.


## v0.1.29 hardware menu verified; v0.1.30 Schedule TEST CANDIDATE (2026-10-20)

**USER HARDWARE CONFIRMATION:** v0.1.29 renamed Ukrainian menu labels all display correctly on test ESP32, so this becomes the UI regression baseline. Do not infer production certification of 10s polling, security or WebHook from UI confirmation.

Generated **complete source ZIP** `airALARM_v0.1.30_SCHEDULE_TEST.zip` (source SHA256 and test matrix included as `STATIC_QA_REPORT.txt`) from original v0.1.29 MENU TEST. ZIP CRC and source structure confirmed. **NOT COMPILED WITH PLATFORMIO HERE; NOT HARDWARE TESTED.** Includes:
- `Хвилина мовчання — розклад повідомлень` separate web menu; four configurable slots, per-slot enabled, Monday–Sunday day bitmap, 24h HH:MM, selected zone or all enabled zones, dedicated local MP3 (A31 / separate HTTP server 8082) and WAV (A33) upload or external URL.
- NTP time via `configTzTime("EET-2EEST,M3.5.0/3,M10.5.0/4",...)` and `localtime_r` for Kyiv. No schedule before valid time, on active alarm, unconfirmed/stale API, error API, or if urgent audio queued. Strict API 200 within 30 seconds required. New scheduler slots default DISABLED.
- Persist last played civil minute in NVS per-slot (`slastN`) and globally (`sglob`) before playback; ignores late minute executions >12 seconds; no duplicate during DST fall-back/reboot; maximum one scheduled event per minute, conflict chooses first listed.
- Uses existing hardware-tested A31 volume snapshot/pause/prompt/timed-restore and A33 WAV download/play; does not modify original alarm audio files. A31 timeout range changes **5–55 to 1–55 seconds**, but setting value must remain longer than audio file or restoration may interrupt message.
- Scheduled-test button `POST /silence-test` using AJAX without leaving settings page, with all same safety gates. New POST `/silence-save`, `/silence-upload`; WAV HTTP `/audio/silN.wav`, MP3 HTTP `:8082/audio/silN.mp3`.
- The **65-second global type-audio gap remains for normal event transitions**, but urgent `action==0` alert ON events are picked before other queued events and bypass the gap. When an A31 scheduled Prompt is in progress, experimental override attempts `setPlayerCmd:stop`, then sends urgent `PromptEnable` and `playPromptUrl`, and extends the existing NVS volume-snapshot deadline through urgent playback. A33 receives new download/play attempt.
- **CRITICAL UNVERIFIED:** whether A31 native `setPlayerCmd:stop` actually terminates active URL Prompt and whether A33 plays urgently over an active WAV. These require controlled on-device test before any real emergency use. The firmware still serially handles network operations and does not guarantee immediate reaction within upstream polling/network delays. Real-time Cloudflare WebHook channel not yet integrated.
- **Other outstanding tasks**: authenticated local .bin OTA and signed/verified online release update, real official webhook signature validation, verified TLS trust instead of `setInsecure()`, provider quota for 10-second REST, proper alarm-on-boot semantics and tests for region hierarchy.
- Mac test build: `cd /Users/lab/AI/airALARM/airALARM_v0.1.30_SCHEDULE_TEST && ~/.platformio/penv/bin/pio run`. Flash ONLY test ESP32, no flash erase/uploadfs. Test local NTP time + scheduled short non-emergency MP3 at low master volume, restoration, AJAX test and simulated high priority interruption, inspect serial `[SILENCE]`/`[PRIORITY]` logs.

This increment should NOT replace the proven airALARM v0.1.28 working acoustic baseline or v0.1.29 UI-tested source until compilation and targeted hardware verification. It is not certified for sole emergency public notification.


## v0.1.30 schedule candidate: actual Mac compiler failure and minimal FIX1 (2026-10-20)

User executed `~/.platformio/penv/bin/pio run` in `airALARM_v0.1.30_SCHEDULE_TEST`. **Build FAILED**, 11.19 sec, with fatal `src/main.cpp:116:79 error: cannot convert 'StringSumHelper' to 'const char*' in assignment` inside `mp3ServeTask`. It assigned `"/sil"+part+".mp3"` (Arduino String expression) into `const char* filePath`. Other output were nonfatal deprecation warnings `NetworkServer::available()` (renamed accept) and `NetworkUDP::flush()` (renamed clear).

**Produced FIX1 source ZIP**: `airALARM_v0.1.30_SCHEDULE_TEST_FIX1.zip`. Minimal surgical fix, hoisted existing `String dynamicFile;` to before both silN and tN audio path branches and changed scheduled MP3 branch to `dynamicFile="/sil"+part+".mp3"; filePath=dynamicFile.c_str();`. This pointer remains valid across LittleFS.exists/open (no intervening String modification for that path); same pattern already used for tN paths. Original source roundtrip comparison verified *only* the affected fragment changed. ZIP CRC passed, archive SHA256 `8dbbc7c99dd2630cae1ff04822b1407dad17dfca3e21792a665f7d875eda862f`, 12 files. README added. **Assistant environment does not have PlatformIO; FIX1 not yet compiled nor hardware verified.**

Mac command: `cd /Users/lab/AI/airALARM/airALARM_v0.1.30_SCHEDULE_TEST_FIX1 && ~/.platformio/penv/bin/pio run`. Preserve v0.1.28 hardware-working firmware and v0.1.29 menu UI-tested baseline, and do NOT flash FIX1 until Mac reports SUCCESS. All prior unresolved safety limitations (unverified urgent stopping A31 Prompt, fallback API quotas, insecure TLS etc.) still apply.

## v0.1.30 FIX1 boot failure diagnosed with serial log (2026-10-20 evening)

**User hardware bootloader-confirmed**: Mac USB 115200 logs show `esp_image: Image length 1325920 doesn't fit in partition length 1310720`, `OTA app partition slot 0 is not bootable`; slot 1 image at 0x150000 invalid magic (empty). `No bootable app partitions in the partition table`, reboot loop, HTTP 80/8082 not reachable. Image overflow is **15,200 bytes (~14.8 KiB)**. A PlatformIO `[SUCCESS]` build did not enforce boot-time target partition capacity. NOT a Wi-Fi/web server/HTML defect: application never starts. Repeated EN/Reset will not fix it.

**Safe recovery first**: stop serial monitor, reupload known good v0.1.29 MENU TEST via `pio run -t upload` on test board WITHOUT erase, uploadfs or factory.bin; check actual web UI and audio configs after recovery. Preserve NVS and LittleFS. Do not flash a new partition layout without explicit full flash-region map and backup; layout change risks erasing/reinterpreting NVS/audio files and affects OTA. The verified original v0.1.29 baseline is first rollback target.

**Engineering follow-up**: reduce compiled firmware code/data by comfortably >15,200 bytes (recommend >=32 KiB headroom), check output `firmware.bin` size against exact 0x140000 app partition (not just PlatformIO SUCCESS), and test reset boots after flashing. Compile tools not available in assistant environment, so no unverified size-fix should be claimed as successful. This issue blocks on-device v0.1.30 scheduler tests.

## FIX2 compiler regression and FIX3 (2026-10-20)

User compiled FIX2 on Mac and received linker failure `undefined reference to app_main` from ESP-IDF `libfreertos.a(app_startup.c.obj)` during `firmware.elf` link. The probable trigger is assistant-added `-flto` build flag conflicting with prebuilt pioarduino/Arduino ESP32 libraries. Created `airALARM_FIX3.zip` (folder `airALARM_v0.1.30_SCHEDULE_TEST_FIX3`), removing only `-flto` while preserving full `src/main.cpp` and size gate. ZIP checked (`unzip -t` clean); **not compiled on Mac yet**, and firmware size not known. Run `pio run -t clean` then `pio run`, do not upload unless compiler success and >=32KiB partition headroom. Tested v0.1.29 remains device rollback.

## FIX3 -> FIX4: SCons size-check callback error (2026-10-20)

User reports FIX3 successfully linked ESP32 firmware image, but PlatformIO post-action errored: `TypeError: verify_firmware_size() got an unexpected keyword argument 'env'`. This is an incorrect callback signature in the assistant-added extra script, not a compile/link error. Original function used `def verify_firmware_size(source, target, environment)`; SCons calls with keyword arguments `target`, `source`, `env`. FIX4 uses `def verify_firmware_size(target, source, env)` and keeps original `src/main.cpp` byte-identical to FIX3. ZIP created and CRC checked: `airALARM_FIX4.zip`, SHA256 `dec425fa7fe470fb70aac58b7fa0a6b121c8a08be693217f316d5a8f12f1ae58`. The Python file passes py_compile. Actual Mac firmware size / successful post-check NOT YET VERIFIED. Limit 0x140000 with 0x8000 spare => firmware.bin <=1,277,952 bytes. Do not flash if FAIL. Test ESP32 is running recovered known-good v0.1.29.
