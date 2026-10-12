# Hardware/practical verification: KNOB fast discovery

- Date: 2026-10-12 (Europe/Kiev).
- Project: airControl KNOB / airKNOB.
- Version: v0.8.5, ONX2424G013 ESP32-S3.
- Canonical finding: DISC-FAST-ZONES-001 — CONFIRMED (overall observed behavior).
- Source/tested build: [source commit](https://github.com/keshman74/airKNOB/commit/efeccb316fb041da5872c48ace92db60429e85ef), [CI run](https://github.com/keshman74/airKNOB/actions/runs/38297173264).
- User report, verbatim: «так гораздо быстрее ищутся и находятся все зоны! Сохрани в нашу базу данных airControl-Protocol-KB методы быстрого поиска зон».
- Observed outcome: search is qualitatively much faster; all expected zones are found in the tested LAN.
- Context: earlier releases intermittently missed zones; desktop airControl found zones quickly.
- Not supplied: quantitative timings, total/device-by-device inventory, repetition count, individual player firmware versions or a packet capture.
- Scope: confirms the integrated discovery method on the user's KNOB/LAN. It does not independently verify every chip/transport, isolate which SSDP path discovered a particular zone, or validate playback/EQ/multiroom commands.
- Related implementation/host-test rules: RULE-DISCOVERY-NONBLOCKING-001 and RULE-DISCOVERY-CANCEL-GENERATION-001.
- Technical definition: [canonical method](../../registry/FAST_ZONE_DISCOVERY.md), [discovery registry](../../registry/DISCOVERY.md).

Preserve this behavior as a KNOB discovery baseline; future changes need regression checks on the user's real inventory.
