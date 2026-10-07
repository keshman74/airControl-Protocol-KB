# Findings added from full audit of saved chat 300926

## TCP :8819
WiiM Home contains a concrete `Socket8819CommThread` implementation, so port 8819 is no longer merely an advertised unknown port.

### Framing
```text
offset 0   uint32 magic = 538482200
offset 4   uint32 payload_length
offset 8   uint32 0
offset 12  8 zero bytes
offset 20  UTF-8 payload
```

Immediately after connect, the app sends:

```json
{"action":"1888"}
```

It then reads response bytes and records connected/duration/size/speed. The audited source also shows a connectivity helper that falls back to TCP port `59152` if the requested port fails.

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
