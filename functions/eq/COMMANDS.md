# Eq command view

- `QRY-A31-TREBLE` [A31] `MCU+PAS+RAKOIT:TRE&` — **CAPTURED**
- `CMD-A31-TREBLE` [A31] `MCU+PAS+RAKOIT:TRE:<n>&` — **CAPTURED/IMPLEMENTED**
- `QRY-A31-BALANCE` [A31] `MCU+PAS+RAKOIT:BAL&` — **CAPTURED**
- `CMD-A31-BALANCE` [A31] `MCU+PAS+RAKOIT:BAL:<n>&` — **CAPTURED/IMPLEMENTED**
- `CMD-A31-MID` [A31] `MCU+PAS+RAKOIT:MID:<n>&` — **CAPTURED/IMPLEMENTED**
- `QRY-A31-EQ-TONE` [A31] `MCU+PAS+EQGet&` — **IMPLEMENTED**
- `CMD-A31-VIRTUAL-BASS` [A31] `MCU+PAS+RAKOIT:VBS:<0|1>&` — **IMPLEMENTED/VERIFIED-IN-APP**
- `CMD-A31-VBI` [A31] `MCU+PAS+RAKOIT:VBI:<1..100>&` — **CONFIRMED-WRITE-ONLY**
- `QRY-ACS2-EQ-TYPE` [ACS2 devices] `getEqType` — **DOCUMENTED**
- `CMD-ACS2-EQ-ENABLE` [ACS2 devices] `eqEnable:<eqSwitch>` — **DOCUMENTED**
- `CMD-ACS2-EQ-HILO` [ACS2 devices] `setEqHighAndLowFrequencies:{"Bass":"-5..5","Treble":"-5..5"}` — **DOCUMENTED**
- `CMD-ACS2-EQ-PRESET` [ACS2 devices] `setPresetEq:<presetInfo JSON>` — **DOCUMENTED**
- `CMD-ACS2-EQ-PARAM` [ACS2 devices] `setParameterEq:<parametInfo JSON>` — **DOCUMENTED**
- `QRY-ACS2-EQ-INFO` [ACS2 devices] `getEqInfo:<eqType>` — **DOCUMENTED**
- `CMD-ACS2-EQ-ADD` [ACS2 devices] `addCustomEqInfo:<addEqInfo JSON>` — **DOCUMENTED**
- `CMD-ACS2-EQ-DELETE` [ACS2 devices] `delCustomEqInfo:<delEqInfo JSON>` — **DOCUMENTED**
