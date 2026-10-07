# ACS2 API

Two API transports are documented:

```text
HTTP  http://<DEVICE_IP>:8000/?Instruct=<params>
HTTPS https://<DEVICE_IP>:8443/?Instruct=<params>
```

Responses may be JSON or text. Port 8000 has been used on the tested A33; 8443 is a documented alternative and must not be omitted from the model.

See `COMMANDS.md` for recovered commands.
