# Findings added from full audit of saved chat 300926

## TCP :8819
WiiM Home contains a concrete `Socket8819CommThread` implementation, so port 8819 is no longer merely an advertised unknown port.

### Framing
```text
offset 0   encoded 32-bit field derived from decimal magic 538482200
offset 4   encoded 32-bit field derived from payload_length
offset 8   encoded 32-bit field derived from 0
offset 12  8 zero bytes
offset 20  UTF-8 payload
```

Immediately after connect, the app sends:

```json
{"action":"1888"}
```

It then reads response bytes and records connected/duration/size/speed. Byte order/literal header bytes remain unresolved until `vob.a()` and `mg0.f()` are decoded. A separate generic connectivity helper tests TCP port `59152` if an arbitrary requested port fails; this is NOT proven to be an :8819 protocol fallback.

Status: **APK-VERIFIED / NOT-HW-VERIFIED**.

## Linkplay secure status transport
Recovered exact `getStatusEx` transport selection:

```text
http://<ip>/httpapi.asp?command=getStatusEx
https://<ip>/httpapi.asp?command=getStatusEx
https://<ip>:4443/httpapi.asp?command=getStatusEx   # bHasgc4aVer
```

This must remain separate from ACS2 `:8000/:8443 ?Instruct=` transport.

## New PlayQueue action
```text
MoveTracksInQueue(QueueName, IndexList, ToIndex)
```

Recovered exact callback class from WiiM Home. Status: **APK-VERIFIED / NOT-HW-ACTION-VERIFIED**.
