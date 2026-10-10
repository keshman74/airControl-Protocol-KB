# airALARM — аппаратно проверенные команды (2026-10-10)

Источники: ACS2 API / airControl-Protocol-KB, Ukraine Alert API 3.0. Только фактически проверенные результаты помечены «подтверждено».

## A33 — ACS2 HTTPS :8443 (192.168.0.31)
- Подтверждено: `GET https://<ip>:8443/?Instruct=setPlayerCmd:prompttone:Enable` → HTTP 200 `OK`.
- Подтверждено: `GET https://<ip>:8443/?Instruct=downloadPromptSound:https://keshman74.github.io/airControl-Protocol-KB/assets/airALARM/airalarm_alert.wav` → HTTP 200 `OK` при первой загрузке; повторно HTTP 400 `Exist`.
- Подтверждено: `GET https://<ip>:8443/?Instruct=playPromptSound:airalarm_alert.wav:10` → HTTP 200 `OK`. Пользователь слышал украинское сообщение при 10%, радио возобновлялось после него.
- Подтверждено в airALARM: `prompttone:Enable` → `downloadPromptSound` (400 Exist) → `playPromptSound` (200 OK). HTTP 200 не гарантирует акустического воспроизведения в каждом испытании.
- Проверено: `curl -G --data-urlencode` для `Instruct` вызывал 400 Error; в рабочем URL двоеточия не кодировались.
- Громкость 10–100 указана в используемой ACS2 документации, весь диапазон аппаратно не проверен.

## A31 — Linkplay HTTP (192.168.0.35)
- Подтверждено: `GET http://<ip>/httpapi.asp?command=PromptEnable` → `OK`; `prompt_status` в `getStatusEx` меняется 0→1.
- НЕ подтверждено: `playPromptUrl:<url>` — в тестах `Failed`.
- Подтверждено с ограничением: `setPlayerCmd:play:<http-url>` запускает WAV, но прерывает радио без восстановления.

## Ukraine Alert API 3.0
- Подтверждено: `GET /api/v3/alerts/31` с действительным ключом → HTTP 200, JSON `regionId:31`, `activeAlerts:[]` в момент теста.
- Подтверждено: HTTP 401 возможен при проблемах авторизации. Ошибки API и устаревшие данные не означают «отбой».

## UI и обнаружение
- Подтверждено пользователем: airALARM v0.1.9 сохраняет страницу при тесте звука и показывает онлайн/офлайн; на скриншоте 4/7 зон онлайн, 192.168.0.103 офлайн.
- НЕ проверено на железе: airALARM v0.1.10 — удаление зон, проверка каждые 60 с, критический статус после трёх неудач, уведомление в UI. TCP-доступность не гарантирует поддержку протокола.
