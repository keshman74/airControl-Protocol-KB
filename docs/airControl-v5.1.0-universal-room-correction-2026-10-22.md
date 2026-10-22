# airControl v5.1.0 — Universal Room Correction (design and A97 research)

Status: DESIGN APPROVED BY USER / NOT HARDWARE VERIFIED. Date: 2026-10-22.

## Requirement
Desktop computer measures room acoustics and calculates correction. The selected playback device applies DSP locally and should retain correction independently of airControl. Four adapters: A33, A97 (first priority), A98 (second), A31 (limited-capability fallback). Common measurement and correction engine; device-specific capability detection and command adapters. Show predicted difference between target and realizable response. Do not regress current EQ or Multiroom.

## Canonical evidence review
- A97 is Allwinner R328, HTTPS :443 in the verified transport map; current compatibility matrix marks A97 EQ **UNKNOWN**. Do not assume WiiM API commands work on A97.
- The WiiM OpenAPI v1.2.0 import lists EQGetStat, EQGetBand, EQGetLV2Band, EQSetBand, EQSetLV2Band, EQSave, EQSave:Custom and room-correction commands. These are **SOURCE-DOCUMENTED / NOT-HW-VERIFIED** for A97/A98.
- A98 separate HTTP EQ implementation exists in the airControl source snapshot, but persistence and Room Correction require device tests.
- A31 MCU :8899 tone/preset controls are implemented/confirmed in prior work; no claim of full PEQ support.

## A97 validation sequence (non-destructive first)
1. Identify device, firmware, transport and current EQ state.
2. Probe read-only EQGetStat, EQGetList, EQGetBand, EQGetLV2Band and RoomCorrectionGet variants **only after confirming endpoint syntax from KB**. Record HTTP status, body, firmware, timings, and errors; distinguish unsupported from network failure.
3. Backup existing settings and confirm restore route before any write.
4. Test a small, reversible filter only with explicit user authorization; read back, measure actual response, and test persistence after reboot separately.
5. Promote each command to CONFIRMED only with hardware evidence and firmware context.

## Architecture contract
MeasurementEngine -> CorrectionEngine -> DeviceDSPAdapter (capabilities, readSnapshot, preview, apply, readBack, save, restore). Require safe gain/preamp and headroom handling, measurement quality checks, rollback, and no writes on unsupported devices.

## Next action
Obtain A97 IP/firmware and read-only probe results, then map actual filter schema and storage semantics. This file is a research/design record, not a claim of working hardware correction.
