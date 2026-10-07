# TCP :8819 — canonical protocol record

## Status
**APK-VERIFIED / NOT-HW-VERIFIED**

WiiM Home contains a dedicated class `com.wifiaudio.shared.mcu.Socket8819CommThread` and explicitly connects to device TCP port `8819`. The recovered code proves a diagnostic/network-measurement role. It does **not** yet prove Play/Pause/Volume/Source/EQ control over this port.

## Connection
- Target: `<device-ip>:8819`
- Java socket read timeout: **10000 ms**
- Higher-level `DeviceReportNetStatus` protection timeout: **20000 ms**
- Code names: `Socket8819CommThread`, `connectTCP8819`
- Result object: `TCP8819Item`

## Probe payload
Immediately after connection the app sends:

```json
{"action":"1888"}
```

The value `1888` is a **JSON string**.

## Framing
```text
offset 0..3    encoded uint32 magic derived from decimal 538482200
offset 4..7    encoded uint32 payload length
offset 8..11   encoded uint32 zero
offset 12..19  8 zero bytes
offset 20...   payload bytes (Java String.getBytes(); JSON text)
```

Source path:
`Socket8819CommThread.j(String)`

Important: the decompiled builder passes the integer fields through `vob.a(...)` and writes them using `mg0.f(...)`. Until those helpers are decoded, the KB must **not** assert byte order or literal four-byte magic representation.

The sender writes exactly `20 + payload.length` bytes using `DataOutputStream.write(...)` and calls `flush()`.

## Response / measurement behavior
After sending the probe, WiiM Home opens a `DataInputStream` and accumulates bytes from the device.

Recovered thresholds:
- measurement target: **4096 bytes**
- socket/measurement timeout: **10000 ms**

It calculates:

```text
speed = received_bytes / elapsed_seconds
```

and stores:
- `connected`
- `duration`
- `size`
- `speed`

in `TCP8819Item`.

This supports classifying the recovered `action:"1888"` exchange as a **network throughput/connectivity diagnostic probe**.

## DeviceReportNetStatus context
The higher-level network-status reporter runs several checks in parallel, including:
- DLNA `GetControlDeviceInfo`
- TCP :8819 measurement
- cloud device status

and then combines them into `CustomDeviceInfo`. Its overall timeout protection is **20000 ms**.

## Port 59152 — corrected interpretation
The helper `us5.b(ip, requestedPort)`:
1. checks the requested TCP port with a **5000 ms** connect timeout;
2. if it fails, checks TCP **59152** with the same timeout.

This is a **generic TCP-connectivity helper**. It is **not evidence that the TCP :8819 protocol itself switches or falls back to 59152**. Keep this rule separate from the 8819 wire protocol.

## What is not proven
- No recovered evidence here proves Play/Pause/Volume/Mute/Source/EQ commands on :8819.
- No exact semantic response body for `action:"1888"` is decoded; this code measures received byte count/time.
- A31/A97/A98 per-device hardware support still requires direct testing.
- Byte order of the three 32-bit header fields remains unresolved until `vob.a` and `mg0.f` are decoded.
