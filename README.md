# airControl Protocol Knowledge Base

Canonical protocol knowledge base for **airControl**, **airKNOB**, **KNX → airScope / airCloud Gateway** and future integrations.

Baseline imported from research snapshot **v0.4.8-CHAT-AUDIT-02-PLAYQUEUE-SCPD**.

## Current baseline

- 204 protocol registry records
- A31 / A97 / A98 / A33 device families
- Linkplay HTTP/HTTPS
- MCU TCP :8899
- ACS2 HTTP :8000 / HTTPS :8443
- A33 JSON TCP :1234
- A33 native TCP :23040
- UPnP AVTransport / RenderingControl / PlayQueue
- online-service research: TuneIn, Qobuz, Spotify, TIDAL, Deezer, vTuner, YouTube Music
- WiiM Home reverse engineering

## Evidence status

Never silently promote evidence.

- CONFIRMED — hardware tested
- CAPTURED — observed on wire
- DOCUMENTED — official documentation/source
- IMPLEMENTED — present in project source
- SOURCE-CONFIRMED / NOT-HW-VERIFIED — recovered from application/decompiled source
- EXPERIMENTAL — under investigation
- REJECTED — tested and known not to work in the stated context

## Rule

Every newly discovered command, response, port, protocol behavior, device compatibility result or reverse-engineering finding must be added here with its evidence status. Negative findings are preserved.

See `INDEX.md`, `registry/`, `devices/`, `protocols/`, `functions/`, `services/`, `evidence/` and `integrations/`.
