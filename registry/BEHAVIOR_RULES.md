# Behavior Rules

## RULE-DISCOVERY-ONLINE-001
Saved configuration means previously known, not currently online. Online requires a live response.

## RULE-EVIDENCE-001
Do not promote a command to CONFIRMED from documentation or code alone.

## RULE-REGRESSION-001
Do not replace a hardware-confirmed implementation with EXPERIMENTAL behavior without an explicit test.

## RULE-SECURITY-001
Never commit real auth tokens, passwords, cookies, API session credentials or private identifiers. Use `<REDACTED>`.

## RULE-CROSS-CHIP-MULTIROOM-001
Do not treat A33 ACS2 multiroom as interchangeable with Linkplay A31/A97/A98 JoinGroup/LeaveGroup. Cross-chip grouping remains unconfirmed until tested.

## RULE-STREAM-CAPABILITY-001
Streaming/service support must not be inferred only from device chip/model.
Where available, use the device's `StreamServicesCapability` / `StreamCapability`
mechanism or hardware evidence before declaring a service supported.

## RULE-A31-VOLUME-001 — Relative volume mapping
Canonical airScope mapping:
- VOL+ => TCP target +5; HTTP fallback `setPlayerCmd:vol++`
- VOL- => TCP target -5; HTTP fallback `setPlayerCmd:vol--`

An earlier reversed HTTP mapping is a known regression and must not be restored.

## RULE-A31-VOLUME-002 — Relative TCP volume state
When current volume is unknown, query it and wait for `AXX+VOL`.
For rapid relative changes, calculate from the last successfully transmitted
absolute target rather than stale feedback, while treating subsequent
`AXX+VOL` as authoritative confirmation.

## RULE-A31-TCP-RATE-001
The gateway source explicitly rate-limits native TCP commands using
`MIN_COMMAND_INTERVAL_MS`. CHAT-AUDIT-02 does not establish the numeric value,
so the KB must not invent one from this chat alone.
