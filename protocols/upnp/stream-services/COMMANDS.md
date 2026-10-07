# UPnP Stream Services — CHAT-AUDIT-01

## StreamServicesCapability

```text
StreamServicesCapability(InstanceID, AppVersion)
    -> StreamCapability
```

Recovered behavior from the saved research chat:
WiiM Home queries the device capability and uses `StreamCapability` to determine
available stream/service support. The chat specifically notes Samba as capability-dependent.

Status: `SOURCE-CONFIRMED / NOT-HW-VERIFIED`

## Rule
Do not infer streaming-service capability only from A31/A97/A98/A33 chip/model name.
Query/capture the actual device capability where supported.
