# DEV-A33
Separate architecture from A31/A97/A98.

Known transports:
- ACS2 HTTP `:8000/?Instruct=params` — used on test device.
- ACS2 HTTPS `:8443/?Instruct=params` — documented alternative.
- TCP :1234 — bidirectional JSON state/control.
- TCP :23040 — native binary protocol; seek plus service context/metadata captured.
- UDP broadcast :53308 — discovery beacon captured.
- SSDP/UPnP and mDNS advertisements captured.

Do not substitute Linkplay JoinGroup/LeaveGroup for ACS2 multiroom without testing.
