# Discovery
Goal: `Find airControl-compatible devices` → classify device → choose transport → load capabilities. Projects should consume this common model rather than hard-code a single chip family.


## Online-state truth
- `RULE-DISCOVERY-ONLINE-RESPONSE`: a persisted/remembered zone starts Offline/unknown. Mark it Online only after a real discovery or status response from the device. Cached/localStorage data is not online evidence.
