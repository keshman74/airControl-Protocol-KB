# A31 Native KNX — Editable Group Address Mapping Table

## Status and provenance
- **Version:** native KNX v0.11 (2026-10-21); MIPS32 little-endian static ELF, offline build/tests pass. **NOT YET HARDWARE-TESTED** on physical A31.
- Proven baseline: v0.10 hardware-confirmed KNX receive/Mute/transport dispatch, presets 1 and 2 playback (operator observed); v0.9 volume changes with readback. See [NATIVE_KNX.md](NATIVE_KNX.md).
- v0.11 did not alter the proven HTTP player implementation, Mute/readback implementation, local TCP8899 preset format, or the KNX decoder. Only config-to-action mapping, CLI and monitoring metadata changed.

## In-memory table + eventual persistence

```text
KNX 224.0.23.12:3671 -> KNX DPT1 GroupValueWrite
   -> u16 source filter (1.1.22 in lab)
   -> mapping[64] RAM entries { ga:u16, action:u8, trigger:u8, arg:u8 }
   -> A31 local HTTP 127.0.0.1:80 or framed TCP 8899
```

The table is loaded from an external UTF-8 CSV on process startup, not compiled into the binary. Editing group addresses does not require recompiling or reflashing ELF. For permanent settings, the CSV and network config must be saved to a **verified writable, persistent A31 partition**; this partition has **not yet been identified** on the live device. `/tmp` is temporary, not persistent. The current program is a reader only: no flash writes, web configuration backend, or autostart.

## CSV schema V1: GA,ACTION,PARAM,TRIGGER

Examples:
```csv
# KNX_MAP_SCHEMA=1
3/1/6,mute,0,state
3/1/0,volume_up,2,press1
3/1/1,volume_down,2,press1
3/0/0,playpause,0,press1
3/2/0,preset,1,press1
3/2/1,preset,2,press1
```

- `GA`: KNX three-level group address `0..31/0..7/0..255`; unique across all active rows.
- `ACTION`: `mute`, `volume_up`, `volume_down`, `playpause`, `play`, `pause`, `next`, `previous`, `preset`, `source_aux`, `source_usb`.
- `PARAM`: `1..10` for `preset` (slot) and for `volume_up/down` (percentage points per KNX command); `0` for other actions.
- `TRIGGER`: `state` required for Mute (bit 0=off, 1=on); `press1`, `press0`, `both` for button actions.
- Limit: **64 rows**, maximum CSV bytes **8191**, DPT 1 GroupValueWrite only. No DPT5 absolute-volume or feedback KNX TX in v0.11. Malformed / duplicate / incompatible row aborts startup before sending player commands.
- KNX source and local interface are separate settings in `knx-audio.conf`: `source=1.1.22`, `interface_ip=192.168.0.35`. KNX-only `max_volume=100` (configurable), `volume_step=2`, `volume_repeat_ms=90`, `button_debounce_ms=250` remain defaults.
- On A31 after manually copying CSV and ELF to /tmp: `/tmp/knx-audio-v11 --map /tmp/knx-map.csv --show-map` validates and prints the table. `--run-all` enables actual playback changes; never run multiple active versions.
- Compatibility: omitting `--map` uses the established v0.10 `action=GA` legacy mapping; no implicit fallback when an explicitly supplied table is missing.

## Commissioning UI roadmap

The offline bundle includes an HTML/JS table editor and Python CLI CSV editor. Both currently operate on the Mac and **do not write to the player**. Future embedded A31 interface: authenticated LAN-only configuration endpoint, server-side duplicate/range/schema validation, backup, atomic write to confirmed persistent mount, explicit reload/restart with rollback and audit; avoid unauthenticated web writes and unbounded flash write frequency.

## Firmware image safety gate

`FIRMWARE_OVERLAY_STAGE` is a non-bootable/non-flashable placement candidate. Before any stock firmware repack/OTA: fetch **read-only** mount/partition data from the actual A31, verify firmware provenance and storage space, secure recovery/backups and test a spare unit. Never use donor Youyishi `wifiaudio` startup scripts on Rakoit; they initialize other audio stacks and may disrupt playback.

**Evidence:** v0.11 source, host test executable, static ELF, schema and editor included in `A31_KNX_NATIVE_V11.zip`; physical A31 v0.11 test PENDING.

## Live flash inventory — 2026-10-21

The actual A31 has two writable JFFS2 mounts: `/mnt` on mtd8 (512 KiB raw) and `/vendor` on mtd9 (2 MiB raw); root SquashFS is read-only and `/tmp`, `/etc`, `/var` are ramfs. `/vendor/knx/` is a **candidate** persistent location, not an approved write target until free space and vendor file responsibilities are reviewed. See [read-only A31 storage evidence](STORAGE_LAYOUT_2026-10-21.md). No flash writes, service installation or autostart yet.
