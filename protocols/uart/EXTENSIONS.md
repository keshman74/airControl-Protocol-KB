# Arylic UART default configuration and multi-zone extensions

These are documented in the same UART API but are separated from the normal A31 runtime command list because applicability is product/platform dependent.

## 4-zone RS232 models
For MA400/HA400/M400/H400:
- `ZON:{logiczoneid}:{msg};` redirects a UART message to a zone; response is redirected in the same form.
- `IDS[:{zoneid}:{logiczoneid}];` queries/sets logical zone IDs, range 1..127.
These are **not generic A31 single-zone commands**.

## Default configuration
Use `DEF:{sub-api};`. Documented sub-APIs:
- LTP — LED driving method (UND/RGB/PIN; model-limited)
- NAM — default device name
- FXN — restore default name on factory reset
- VOL — default volume
- VBS — default virtual bass
- PMT — default prompt voice
- VOS — default volume sync
- BEP — default beep
- MDL — model name
- VST — default volume step
- SAV — save settings; must be sent last
- SEN — enable/disable supported source modes
- POM — default power-on source
- MXV — default max volume
- COE/COD — default Bluetooth PIN protection/code
- LAP — default autoplay

Important vendor rule: after default configuration, factory reset is required to verify/apply as documented; SEN has special save/reset behavior.
