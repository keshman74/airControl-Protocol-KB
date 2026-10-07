# CHAT-AUDIT-04 — Full CHAT-AIRCONTROL-ORIGIN normalization

Source: **Приложение управления устройствами** (CHAT-AIRCONTROL-ORIGIN).

Purpose: full-chat pass against the canonical ledger as it stood at 317 records. Existing commands/protocols already represented in the KB were not duplicated. Only missing canonical knowledge or stronger evidence was normalized.

## New canonical records
- 318 `RULE-LP-TRANSPORT-BY-HARDWARE`
- 319 `RULE-LP-MR-ROLE-PARSING`
- 320 `QRY-A98-METAINFO-ARTWORK`
- 321 `RULE-DISCOVERY-ONLINE-RESPONSE`
- 322 `OBS-DLNA-QUEUE-NEXT-AUTONEXT`
- 323 `RULE-LOCAL-LIBRARY-PLAYBACK-OWNERSHIP`
- 324 `RULE-MULTIROOM-FAMILY-SEPARATION`
- 325 `TEST-A31-UPNP-SEEK-REL-TIME`

## Existing records reused, not duplicated
The chat repeats substantial material already canonical: A31 HTTP commands and rejected getMetaInfo/LineIn cases; A31 TCP :8899 and :8819 distinction; A33 ACS2 :8000/:8443; A33 TCP :1234 and native :23040 seek; Linkplay JoinGroup/LeaveGroup; A33 ACS2 multiroom commands; A33M/ACS2 command families; protocol/device architecture. These remain under their existing IDs.

## Evidence-strengthening
`CMD-UPNP-AVT-SEEK` is strengthened for **A31 REL_TIME** from APK-only evidence to **APK-VERIFIED + A31-HARDWARE-VERIFIED (REL_TIME)**, backed by record 325.

## Guardrails
- No exact wire command was invented for DLNA Auto-Next; only the observed functional behavior is recorded.
- A98 `getMetaInfo` success is not generalized to A31.
- A33 ↔ Linkplay cross-family multiroom remains unverified.
- App-state rules (online truth and local-library ownership) are explicitly labeled as application behavior, not vendor protocol commands.
