# Additional MCU/PAS commands found in pasted WiiM Home decompilation

Status: **SOURCE-VERIFIED / NOT-HW-VERIFIED for A31**. The pasted source is from `WiiM-Home-decompiled`, not the previously hashed 4STREAM APK; do not attribute these commands to 4STREAM or A31 without artifact identity and runtime verification.

## Commands not currently present in the KB search

From `defpackage.q70` and `defpackage.rt5`:

- `MCU+PAS+EQSet:bass:<02d>&` — set bass, two-digit formatting.
- `MCU+PAS+EQSet:treble:<02d>&` — set treble, two-digit formatting.
- `MCU+PAS+EQGet&` — query EQ state.
- `MCU+PAS+EQ:mode:<mode>&` — set/query EQ mode; parser also recognizes `MCU+PAS+EQ:mode:`.
- `MCU+PAS+EQ:enable:<value>&` — EQ enable state; parser recognizes response.
- `MCU+PAS+HDMIGet&` — query HDMI setting.
- `MCU+PAS+HDMISet:<03d>&` — set HDMI value, three-digit formatting.

The decompiled response dispatcher also recognizes `MCU+PAS+EQ:bass:`, `MCU+PAS+EQ:treble:`, `MCU+PAS+EQ:enable:`, `MCU+PAS+EQ:mode:`, and `MCU+PAS+HDM+` responses. These are parser/dispatcher observations, not proof that an A31 accepts them.

## Additional generic PAS families in the pasted source

`rt5.java` recognizes `MCU+PAS+B`, `MCU+PAS+T`, `MCU+PAS+V`, `MCU+PAS+M`, `MCU+PAS+F`, `MCU+PAS+S`, and `MCU+PAS+W`, plus `MCU+PAS+GET&`. Their exact semantics and platform gates are not established by the pasted snippet alone.

## Database comparison

The existing KB contains related A31 `EQSet:treble`, `EQSet:bass`, `EQGet`, PEQ/EQS and UART EQ records, but did not contain the exact `EQ:mode`, `EQ:enable`, `HDMIGet`, or `HDMISet` strings found here. These are recorded separately to avoid promoting WiiM/Home behavior to A31 hardware facts.

## Required verification before A31 promotion

1. Record the exact source APK SHA-256/package/version.
2. Confirm the class belongs to the target application/platform.
3. Send only read-only queries through the correctly framed TCP/8899 API where supported.
4. Record A31 responses and update the device command status only with direct evidence.
