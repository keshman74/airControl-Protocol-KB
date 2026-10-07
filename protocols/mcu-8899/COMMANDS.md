# mcu-8899 commands

## `QRY-A31-MCU-VOLUME`
- **Device:** A31
- **Function:** volume
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+VOL+GET&
```

**Notes:** Response AXX+VOL+NNN.

## `EVT-A31-MCU-VOLUME`
- **Device:** A31
- **Function:** volume event
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
AXX+VOL+NNN
```

**Notes:** Asynchronous/response volume state.

## `QRY-A31-MCU-VERSION`
- **Device:** A31
- **Function:** device info
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:VER&
```

**Notes:** MCU/RAKOIT query.

## `QRY-A31-MXV`
- **Device:** A31
- **Function:** maximum volume
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:MXV&
```

**Notes:** Maximum volume query.

## `CMD-A31-MXV`
- **Device:** A31
- **Function:** maximum volume
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED`

```text
MCU+PAS+RAKOIT:MXV:<30..100>&
```

**Notes:** Set + readback verification implemented.

## `QRY-A31-TREBLE`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:TRE&
```

**Notes:** Treble query.

## `CMD-A31-TREBLE`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CAPTURED/IMPLEMENTED`

```text
MCU+PAS+RAKOIT:TRE:<n>&
```

**Notes:** Treble state/set path.

## `QRY-A31-BALANCE`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:BAL&
```

**Notes:** Balance query.

## `CMD-A31-BALANCE`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CAPTURED/IMPLEMENTED`

```text
MCU+PAS+RAKOIT:BAL:<n>&
```

**Notes:** Balance range used by app -100..100.

## `CMD-A31-MID`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CAPTURED/IMPLEMENTED`

```text
MCU+PAS+RAKOIT:MID:<n>&
```

**Notes:** Mid parameter.

## `QRY-A31-EQ-PRESET`
- **Device:** A31
- **Function:** EQ preset
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:EQS&
```

**Notes:** Response EQS:n.

## `CMD-A31-EQ-PRESET`
- **Device:** A31
- **Function:** EQ preset
- **Transport:** TCP :8899
- **Status:** `CAPTURED/IMPLEMENTED`

```text
MCU+PAS+RAKOIT:EQS:<n>&
```

**Notes:** Preset select with readback in app.

## `QRY-A31-EQ-PRESET-LIST`
- **Device:** A31
- **Function:** EQ preset
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+RAKOIT:PEQ&
```

**Notes:** Observed Flat/Classical/Pop/Jazz/Rock/Vocal list.

## `QRY-A31-EQ-TONE`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED`

```text
MCU+PAS+EQGet&
```

**Notes:** Used to read bass/treble in airControl.

## `CMD-A31-VIRTUAL-BASS`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/VERIFIED-IN-APP`

```text
MCU+PAS+RAKOIT:VBS:<0|1>&
```

**Notes:** Set then readback path exists.

## `CMD-A31-VBI`
- **Device:** A31
- **Function:** EQ
- **Transport:** TCP :8899
- **Status:** `CONFIRMED-WRITE-ONLY`

```text
MCU+PAS+RAKOIT:VBI:<1..100>&
```

**Notes:** Device accepts set; VBI& gives no usable readback on tested firmware.

## `EVT-A31-PLAYBACK`
- **Device:** A31
- **Function:** playback event
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
AXX+SNG+INF{...}&
```

**Notes:** Asynchronous playback status/event.

## `QRY-A31-CFE`
- **Device:** A31
- **Function:** unknown
- **Transport:** TCP :8899
- **Status:** `EXPERIMENTAL`

```text
MCU+PAS+RAKOIT:CFE&
```

**Notes:** Observed; semantics unresolved.

## `QRY-A31-LST`
- **Device:** A31
- **Function:** unknown
- **Transport:** TCP :8899
- **Status:** `EXPERIMENTAL`

```text
MCU+PAS+RAKOIT:LST&
```

**Notes:** Observed; semantics unresolved.

## `CMD-A31-MCU-PAUSE`
- **Device:** A31
- **Function:** playback
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+PLY-PUS
```

**Notes:** airControl maps HTTP pause to this native TCP command with HTTP fallback.

## `CMD-A31-MCU-PLAY`
- **Device:** A31
- **Function:** playback
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+PLY-PLA
```

**Notes:** airControl maps resume/play to this native TCP command with HTTP fallback.

## `CMD-A31-MCU-NEXT`
- **Device:** A31
- **Function:** playback
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+PLY+NXT
```

**Notes:** Native fast path in airControl; preserve HTTP fallback.

## `CMD-A31-MCU-PREV`
- **Device:** A31
- **Function:** playback
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+PLY+PRV
```

**Notes:** Native fast path in airControl; preserve HTTP fallback.

## `CMD-A31-MCU-VOLUME`
- **Device:** A31
- **Function:** volume
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+VOL+<NNN>
```

**Notes:** airControl pads 0..100 to three digits.

## `CMD-A31-MCU-MUTE`
- **Device:** A31
- **Function:** mute
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+MUT+00<0|1>
```

**Notes:** Native fast path in airControl.

## `CMD-A31-MCU-PRESET`
- **Device:** A31
- **Function:** media preset
- **Transport:** TCP :8899
- **Status:** `IMPLEMENTED/NEEDS-HW-EVIDENCE`

```text
MCU+KEY+<001..010>
```

**Notes:** Translation of MCUKeyShortClick:1..10 in airControl.

## `EVT-A31-EQ-TREBLE`
- **Device:** A31
- **Function:** EQ event
- **Transport:** TCP :8899
- **Status:** `CAPTURED`

```text
MCU+PAS+EQ:treble:<NN>&
```

**Notes:** Observed after TRE change in saved A31 capture.


# Official Arylic TCP API additions
Source: Arylic TCP API documentation. Status below is **DOCUMENTED / OFFICIAL-ARYLIC-TCP-API** unless an older record already has stronger hardware/capture evidence.

Transport rules: persistent bidirectional TCP socket on **8899**; at least **200 ms** between commands; documentation states **one connection per client IP**. Packet = 4-byte header `18 96 18 20` + 4-byte little-endian payload length + 4-byte little-endian byte-sum checksum + 8 zero bytes + payload. Payloads longer than 11 bytes normally end in `&`.

## `QRY-A31-TCP-DEVICE-BASIC`
- **Function:** device info
- **Command/mechanism:** `MCU+DEV+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+DEV+INF<semicolon fields>&

## `QRY-A31-TCP-DEVICE-INFO`
- **Function:** device info
- **Command/mechanism:** `MCU+INF+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+INF+INF{JSON}&; same broad data family as HTTP getStatusEx

## `QRY-A31-TCP-INTERNET`
- **Function:** network
- **Command/mechanism:** `MCU+WWW+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+WWW+000|001; device also sends state changes actively

## `QRY-A31-TCP-USB`
- **Function:** USB
- **Command/mechanism:** `MCU+USB+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+USB+000|001; device also sends state changes actively

## `QRY-A31-TCP-MUTE`
- **Function:** mute
- **Command/mechanism:** `MCU+MUT+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+MUT+000|001

## `CMD-A31-TCP-NAME`
- **Function:** device
- **Command/mechanism:** `MCU+NAM+SET<name>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+NAM+SET<name>&

## `CMD-A31-TCP-REBOOT-WIFI`
- **Function:** system
- **Command/mechanism:** `MCU+DEV+RST&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Reboots Wi-Fi module; TCP connection drops

## `CMD-A31-TCP-FACTORY`
- **Function:** system
- **Command/mechanism:** `MCU+FACTORY`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Factory reset; TCP connection drops

## `CMD-A31-TCP-PLAY-TOGGLE`
- **Function:** playback
- **Command/mechanism:** `MCU+PLY+PUS`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Playback status response AXX+PLY+...

## `CMD-A31-TCP-STOP`
- **Function:** playback
- **Command/mechanism:** `MCU+PLY-STP`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Playback status response AXX+PLY+...

## `CMD-A31-TCP-LAST-PLAYLIST`
- **Function:** playback
- **Command/mechanism:** `MCU+PLY+PUQ`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Start last playlist if playback was previously started in app

## `CMD-A31-TCP-PLAYMODE`
- **Function:** playback mode
- **Command/mechanism:** `MCU+PLP+<000..004>`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+PLP+NNN; 000 repeat all, 001 repeat one, 002 repeat all+shuffle, 003 shuffle, 004 sequence

## `QRY-A31-TCP-PLAYMODE`
- **Function:** playback mode
- **Command/mechanism:** `MCU+PLP+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+PLP+NNN

## `CMD-A31-TCP-PRESET-NEXT`
- **Function:** media preset
- **Command/mechanism:** `MCU+KEY+NXT`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Play next preset playlist

## `CMD-A31-TCP-PRESET-PREV`
- **Function:** media preset
- **Command/mechanism:** `MCU+KEY+PRE`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Play previous preset playlist

## `CMD-A31-TCP-PRESET-SAVE`
- **Function:** media preset
- **Command/mechanism:** `MCU+PRE+<001..010>`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Example response AXX+PRE+FF2; only sources supporting presets

## `QRY-A31-TCP-INPUT`
- **Function:** source/status
- **Command/mechanism:** `MCU+PLM+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+PLM+NNN; documented source-code map

## `QRY-A31-TCP-PROGRESS`
- **Function:** metadata/status
- **Command/mechanism:** `MCU+SONGGET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+SNG+INF{curpos,totlen,status,loop}&

## `QRY-A31-TCP-MEDIA`
- **Function:** metadata
- **Command/mechanism:** `MCU+MEA+GET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+MEA+DAT{title,artist,album,vendor,skiplimit}&; text fields hex encoded

## `QRY-A31-TCP-NOWPLAYING`
- **Function:** metadata/status
- **Command/mechanism:** `MCU+PINFGET`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+PLY+INF{type,ch,mode,loop,eq,status,curpos,offset_pts,totlen,Title,Artist,Album,alarmflag,plicount,plicurr,vol,mute}&

## `EVT-A31-TCP-SPOTIFY`
- **Function:** online service/status
- **Command/mechanism:** `(active event)`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AXX+SPY+000|001; Spotify stopped/started

## `CMD-A31-TCP-EQ-TONE`
- **Function:** EQ
- **Command/mechanism:** `MCU+PAS+EQSet:<treble|bass>:<0..10>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** MCU+PAS+EQ:<type>:<value>&; 0..10 maps app -5..+5

## `QRY-A31-TCP-AP8064-BOARD`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:GetBoard&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** MCU+PAS+Rakoit:Board:<board>&

## `QRY-A31-TCP-AP8064-COMMIT`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:GetCommit&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `QRY-A31-TCP-AP8064-PROMPT`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:GetPrompt&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-PROMPT`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:SetPrompt:<0|1>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `QRY-A31-TCP-AP8064-API`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:GetAPIVer&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-SENDKEY`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:SendKey:<key>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `QRY-A31-TCP-AP8064-MAXVOL`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:MaxVolume:Get&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-MAXVOL`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:MaxVolume:<mxv>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-VB-INT`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:VB:INT:<value>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Virtual Bass intensity; AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-VB-ENH`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:VB:ENH:<value>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Virtual Bass enhance; AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-VB-TOGGLE`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:VB:SWI&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Toggle Virtual Bass; AP8064 base-board dependent

## `QRY-A31-TCP-AP8064-VB`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:VB:Get&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Get Virtual Bass on/off; AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-VB`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:VB:<en>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** Set Virtual Bass on/off; AP8064 base-board dependent

## `CMD-A31-TCP-AP8064-LED`
- **Function:** passthrough/AP8064
- **Command/mechanism:** `MCU+PAS+Rakoit:LED:<en>&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** LED on/off; AP8064 base-board dependent

## `QRY-A31-TCP-BP10XX-VOL`
- **Function:** passthrough/BP10XX
- **Command/mechanism:** `MCU+PAS+RAKOIT:VOL&`
- **Status:** `DOCUMENTED / OFFICIAL-ARYLIC-TCP-API / NOT-YET-HW-VERIFIED`
- **Response/notes:** MCU+PAS+RAKOIT:VOL:<value>&; BP10XX base-board dependent

## Existing records strengthened by official documentation
The official TCP API also documents existing canonical records for absolute volume `MCU+VOL+NNN`, volume query `MCU+VOL+GET`, mute `MCU+MUT+000|001`, pause `MCU+PLY-PUS`, resume `MCU+PLY-PLA`, next `MCU+PLY+NXT`, previous `MCU+PLY+PRV`, numbered presets `MCU+KEY+001..010`, and `MCU+PAS+EQGet&`. Preserve any stronger CAPTURED/IMPLEMENTED/CONFIRMED status already present.
