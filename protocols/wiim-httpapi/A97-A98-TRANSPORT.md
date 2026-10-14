# A97 / A98 HTTP API transport

## Canonical transport rule

**Status:** PROJECT-CONFIRMED / REQUIRED IMPLEMENTATION RULE

For devices based on **A97 and A98**, access to the Linkplay/WiiM-style HTTP API must use **HTTPS**.

Canonical request form:

```text
https://{ip-address}/httpapi.asp?command={command}
```

Example for A98 at `192.168.0.21`:

```text
https://192.168.0.21/httpapi.asp?command=getPresetInfo
```

### TLS note

The WiiM/Linkplay API source documents HTTPS transport and notes that devices may use a self-signed certificate. Test clients such as `curl` may therefore require `-k` / `--insecure` for local-device testing.

### Implementation rule for airControl

- **A97:** use HTTPS for `/httpapi.asp?command=...`
- **A98:** use HTTPS for `/httpapi.asp?command=...`
- Do not silently substitute plain HTTP when implementing or testing A97/A98 commands.
- Command support remains model/firmware-specific and must still be hardware-verified separately.

Source API form supplied/confirmed for this project:
`https://{ip-address}/httpapi.asp?command={command}`

Related source audit: `OPENAPI-V1.2.0-COMPLETE.md`.
