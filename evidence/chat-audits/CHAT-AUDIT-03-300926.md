# CHAT-AUDIT-03 — saved chat 300926

Source: `Продолжение разработки airControl 300926.html`

This audit was performed line-by-line against the saved HTML plus protocol-research attachments available from the same conversation/library.

## New canonical findings promoted
- PlayQueue `MoveTracksInQueue(QueueName, IndexList, ToIndex)`
- concrete TCP :8819 framing and probe payload `{"action":"1888"}`
- TCP connectivity fallback to port 59152
- exact WiiM Home `getStatusEx` transport selection including HTTPS :4443 branch
- `setTimezoneEx:<offset>:<dstFlag>:<timezoneId>`
- `setMvRemoteSilenceUpdateTime:<value>`
- update-server response behavior and sleep-timer response handler

## Evidence rule
Where the source exposed only a response handler or function/log name but not the exact request builder string, the KB uses an `OBS-*` record and does not invent the request syntax.

## Attachments reviewed for this increment
- `wiim-playqueue-soap-actions.txt`
- `wiim-tcp8819-protocol.txt`
- `wiim-getstatusex-transport.txt`
- `wiim-http-core.txt`
- `wiim-upnp-actions-core.txt`

The chat itself documents the research scope around WiiM Home, PlayQueue, Qobuz, SMB/Samba, HTTP/HTTPS, TCP 8819 and capability discovery. The saved page is the named source chat. 
