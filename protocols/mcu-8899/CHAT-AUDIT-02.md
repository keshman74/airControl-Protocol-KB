# CHAT-AUDIT-02 — A31 :8899 volume path

Recovered implementation path:

```text
relative KNX +/- request
    -> if volume unknown: MCU+VOL+GET
    -> wait for AXX+VOL
    -> calculate target 0..100
    -> MCU+VOL+NNN
```

Example: `MCU+VOL+065`.

The source also rate-limits command transmission and uses an optimistic
last-transmitted target to avoid stale-feedback jumps during rapid presses.

Evidence level:
- exact gateway implementation: IMPLEMENTED
- `AXX+VOL` response family: previously CAPTURED
- final rapid-press/0/100 behavior: not promoted to CONFIRMED by this chat alone
