# A33M HTTPS API V1.2 — full 36-page audit

Source: **HTTPS API for A33M User Manual V1.2**, dated 19 Jan 2026, 36 pages.

Audit coverage: pages 1–36; API sections 3.1 through 3.13. All 63 documented API entries were checked against the canonical KB.

Result:
- 62 commands/queries already had canonical IDs and were enriched with exact parameters, ranges, responses, JSON fields and behavioral rules.
- 1 missing query was added: `QRY-A33M-EQ-SWITCH` / `getEqSwitch` (record 317).
- Preset list response remains intentionally schema-unknown because the official manual says only “JSON response” and provides no body example.
- Source availability and features are kept hardware-dependent where the manual says so.
- Documentary evidence does not promote commands to hardware CONFIRMED.
