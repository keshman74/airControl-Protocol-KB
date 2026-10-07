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
