# EQ command view

- A31 MCU: `QRY-A31-TREBLE`, `CMD-A31-TREBLE`, `QRY-A31-BALANCE`, `CMD-A31-BALANCE`, `CMD-A31-MID`, `QRY-A31-EQ-PRESET`, `CMD-A31-EQ-PRESET`, `QRY-A31-EQ-PRESET-LIST`, `QRY-A31-EQ-TONE`, `CMD-A31-VIRTUAL-BASS`, `CMD-A31-VBI`, `EVT-A31-EQ-TREBLE`.
- ACS2: `QRY-ACS2-EQ-TYPE`, `CMD-ACS2-EQ-ENABLE`, `CMD-ACS2-EQ-HILO`, `CMD-ACS2-EQ-PRESET`, `CMD-ACS2-EQ-PARAM`, `QRY-ACS2-EQ-INFO`, `CMD-ACS2-EQ-ADD`, `CMD-ACS2-EQ-DELETE` — **DOCUMENTED**.
- UPnP RenderingControl: `QRY-UPNP-RC-GET-EQ`, `CMD-UPNP-RC-SET-EQ` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**.

- `QRY-A33M-EQ-SWITCH` [A33M] `getEqSwitch` — current EQ switch; **DOCUMENTED / OFFICIAL-A33M-V1.2 / NOT-YET-HW-VERIFIED**.


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `CMD-WIIM-SET-EQON` — `EQOn` — Turn on the EQ — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-EQOFF` — `EQOff` — Turn off the EQ setting — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-EQSTAT` — `EQGetStat` — Check if the EQ is ON or OFF — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-EQLIST` — `EQGetList` — Check all the possible EQ settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-EQBAND` — `EQGetBand` — Get the current EQ band — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-LOAD-EQBY-NAME` — `EQLoad:{name}` — Set the specific EQ with name — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-BASS` — `EQSet:Bass:{n}` — Set Bass level — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-TREBLE` — `EQSet:Treble:{n}` — Set Treble level — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-DISABLE` — `EQDisable` — Equalizer disable — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-BAND` — `EQSetBand:{"EQBand":[{"index":{n1},"param_name":{str},"value":{n2}}]}` — Set (a specific) band of the 10-band EQ — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-LV2BAND` — `EQSetLV2Band:{str}` — Set LV2 band — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-LV2SOURCE-BAND` — `EQSetLV2SourceBand:{str}` — Set LV2 source band — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQV2DELETE` — `EQv2Delete:{str}` — Delete EQ v2 settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQV2RENAME` — `EQv2Rename:{str}` — Rename EQ v2 settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-CHANGE-SOURCE-FX` — `EQChangeSourceFX:{str}` — Change source FX — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-CHANGE-FX` — `EQChangeFX:{str}` — Change FX — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQ-GET-LV2BAND` — `EQGetLV2Band:{pluginURI}` — Get LV2 band — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQ-GET-LV2SOURCE-BAND` — `EQGetLV2SourceBand:{str}` — Get LV2 source band — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQ-GET-LV2SOURCE-BAND-EX` — `EQGetLV2SourceBandEx:{str}` — Get LV2 source band with extra parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQV2GET-LIST` — `EQv2GetList:{str}` — Get EQ v2 list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQV2GET-NEW-LIST` — `EQv2GetNewList:{str}` — Get new EQ v2 list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQV2LOAD` — `EQv2Load:{str}` — Load EQ v2 settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQV2SOURCE-LOAD` — `EQv2SourceLoad:{str}` — Source load EQ v2 settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SOURCE-OFF` — `EQSourceOff:{str}` — Turn off EQ source — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SET-CHANNEL-MODE` — `EQSetChannelMode:{str}` — Set channel mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SOURCE-SAVE` — `EQSourceSave:{str}` — Save EQ source settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SAVE` — `EQSave:{str}` — Save EQ settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQ-GET-LV2BAND-EX` — `EQGetLV2BandEx:{pluginURI}` — Get LV2 band with extra parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-EQ-GET-SOURCE-MODES` — `EQGetSourceModes` — Get the EQ source modes — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-EQ-SAVE-CUSTOM` — `EQSave:Custom` — Save the current EQ setting as "Custom" — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**


## Recovered hardware evidence from Codex chat-history audit (2026-10-24)

### A33 / ACS2 — hardware confirmed
Recovered from the original airControl development chat:
- `getEqType` → `EQ type: 0111`.
- `getEqInfo:1` → Bass/Treble object.
- `getEqInfo:2` → 10-band Graphic EQ object.
- `getEqInfo:3` → 10-band Parametric EQ object (`Index/Filter/Freq/Q/Gain`), observed profile `AutoRoomEQ`.
- `eqEnable:0001` and `eqEnable:0010` returned `OK` with `getStatusEx` readback; `0100` was observed as Parametric EQ mode.
- `setParameterEq:{...}` is **HW-CONFIRMED** for writing a named 10-band PEQ profile on the tested A33/CS-8 path. A write using `Custom:"1"` returned `OK` and `getEqInfo:3` read back the changed band and profile name.
- Firmware quirk: `Custom:"1"` was normalized to `Custom:"0"` on readback; do not use `Custom` alone as a reliable user-profile flag.
- Attempting to write the system `AutoRoomEQ` object with `Custom:""` returned `Custom error`.

### A98 / WiiM — hardware confirmed application path
Recovered from the original airControl development chat:
- 10-band Graphic EQ read/write via `EQGetBand/EQSetBand` was reported working on hardware.
- EqNp/LV2 exposed ten active bands A–J with `mode/freq/q/gain`; K/L were observed disabled in the captured response.
- A per-band PEQ write through the airControl implementation using `EQSetLV2SourceBand` was confirmed by the tester to change the value on the physical A98; read path used `EQGetLV2SourceBandEx / EQGetLV2BandEx`.
- Scope warning: this hardware evidence applies to the tested A98 path. It does not automatically promote every WiiM LV2/EQv2 command in the OpenAPI import.

### A97
The supplied Codex chat-history contains A97 HTTPS/discovery/PlayQueue evidence, but this audit found no explicit A97 EQ/PEQ hardware write + readback sequence. Keep A97 EQ capability isolated until directly verified.

Provenance: `evidence/chat-audits/CODEX-CHAT-HISTORY-CROSS-PROJECT-AUDIT-2026-10-24.md`.

## 4STREAM APK evidence — 2026-10-24
**APK-VERIFIED / NOT-HW-VERIFIED**. HTTP EQ/EQv2 and MCU+PAS+EQSet families are separate. Width formats are not range validation, and OEM controls are not universal chip capabilities.
[Exact formats and source selectors](../../protocols/linkplay-http-https/4STREAM-2026-10-24.md#eq-and-mcu-control).

## iAudioCloud APK evidence — 2026-10-25

Native EQ 02 51–58, subwoofer 02 59 / 03 20 / 03 21, exact JSON/filter string serialization and device-dependent ranges. sendTypeSync uses 02 54; 02 50 is a receive-side observation.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
