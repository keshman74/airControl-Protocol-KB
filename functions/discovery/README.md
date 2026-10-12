# Discovery
Goal: `Find airControl-compatible devices` → classify device → choose transport → load capabilities. Projects should consume this common model rather than hard-code a single chip family.


## Online-state truth
- `RULE-DISCOVERY-ONLINE-RESPONSE`: a persisted/remembered zone starts Offline/unknown. Mark it Online only after a real discovery or status response from the device. Cached/localStorage data is not online evidence.

## Confirmed fast discovery baseline

[Fast progressive zone discovery](../../registry/FAST_ZONE_DISCOVERY.md) is the v0.8.5 KNOB baseline, practically confirmed by the user on 2026-10-12: faster search, all expected zones found. Consume the shared algorithm with platform-appropriate resource limits. Keep packet receipt independent of API validation; show verified results immediately; allow bounded retries and cancellation. Preserve the Online-state rule above.
