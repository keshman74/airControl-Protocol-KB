# v0.4.2 Audit Report

## Result
- v0.4.1 records: 96
- Missing records added: 41
- v0.4.2 total: 137

## Main omissions found
### 1. A31 native MCU fast-control path
The application source contains native TCP :8899 translations that were absent from the KB:
- `MCU+PLY-PUS`
- `MCU+PLY-PLA`
- `MCU+PLY+NXT`
- `MCU+PLY+PRV`
- `MCU+VOL+NNN`
- `MCU+MUT+00x`
- `MCU+KEY+001..010`

These are marked `IMPLEMENTED/NEEDS-HW-EVIDENCE` unless a separate capture/test proves the exact outgoing command.

### 2. ACS2 playback duplication was intentional and necessary
ACS2 officially documents many strings also known from Linkplay (`setPlayerCmd:*`). They now have their own `CMD-ACS2-*` records because identical text does not mean identical protocol/evidence.

### 3. ACS2 Prompt Sound + Static IP
Prompt-sound operations and static-IP controls were missing from v0.4.1 and are now present.

### 4. A31 EQ event
Captured `MCU+PAS+EQ:treble:<NN>&` was missing and is now recorded.

## Conflicts / aliases requiring care
- ACS2 `getEqType` manual has a visible typo `getEqTypet` in one request line while Params says `getEqType`; canonical command remains `getEqType`.
- ACS2 Prompt Play has OCR/manual text corruption in one preview. Canonical entry follows the application API catalog and remains DOCUMENTED until verified.
- `setPlayerCmd:setplay:<seconds>` (ACS2 HTTP/S) and A33 native TCP :23040 seek are distinct mechanisms.
- A31 `setStaticIP` JSON shape differs from ACS2 static-IP JSON shape. Do not merge.
- A31/A97/A98 native Linkplay Multiroom and A33 ACS2 Multiroom remain separate families.

## Evidence gaps intentionally NOT invented
- Physical A31 UART baud/data/parity/stop/voltage.
- Exact command protocol on TCP :8819.
- Direct hardware proof for every A31 MCU fast-control command.
- Cross-chip A33 ↔ A31/A97/A98 grouping.
- Full intermediate bytes of A33 TCP :23040 framing when not available from a source.
