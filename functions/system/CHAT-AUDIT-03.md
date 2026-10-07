# Additional system/device commands recovered from WiiM Home

- `CMD-LP-SET-TIMEZONE-EX` — `setTimezoneEx:<offset>:<dstFlag>:<timezoneId>` — **APK-VERIFIED / NOT-HW-VERIFIED**
- `CMD-LP-SET-MV-REMOTE-SILENCE-UPDATE-TIME` — `setMvRemoteSilenceUpdateTime:<value>` — **CALL-SITE-VERIFIED / NOT-HW-VERIFIED**
- `OBS-LP-GET-UPDATE-SERVER` — response handler confirmed; exact request builder string not recovered in this pass.
- `OBS-LP-SET-UPDATE-SERVER` — success response handler confirmed; exact request builder string not recovered in this pass.
- `OBS-LP-GET-SLEEP-TIMER` — raw response handler confirmed; exact request builder string not recovered in this pass.

For update-server handling, WiiM Home checks returned text for `fwupdate.wiimu.com:8020` and replaces it with `s000.linkplay.com:8020`.
