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
