# Linkplay HTTP/HTTPS
A31/A97/A98 family transport and command catalog. HTTP/HTTPS choice is device capability dependent.

## Hardware transport map recovered from CHAT-AIRCONTROL-ORIGIN
- `RULE-LP-TRANSPORT-BY-HARDWARE`: A31 / UP2STREAM_PRO_V4 → HTTP :80; A97/R328 and A98/WiiM/Amlogic → HTTPS :443.
- A97/A98 desktop transport accepts the device's self-signed certificate; do not silently fall back to plain HTTP for those classified families.
- `RULE-LP-MR-ROLE-PARSING`: retain `master_ip` and `master_uuid`; a populated `master_ip` identifies a slave and resolves the real master.
