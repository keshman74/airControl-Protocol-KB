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

## Real A31 auto-start route — validated from live boot scripts (2026-10-21)

Read-only evidence: [A31 flash and boot chain](STORAGE_LAYOUT_2026-10-21.md). `live.sh` mounts `/vendor`, executes `/home/user.sh`, and then runs `rootApp`. `user.sh` launches `daemonize /vendor/user/hdl -d 5 ...` when that file exists, otherwise stock `daemonize /home/bin/hdl`. **This is an override for an essential service, not a KNX hook; never put the KNX executable itself in `/vendor/user/hdl`.** `/vendor/user/user.sh` is deleted at each boot and is unsuitable.

A non-flashable offline design-only stage `A31_KNX_BOOT_INTEGRATION_STAGE_V1.zip` was prepared: proposed data layout in `/vendor/knx`, inert `hdl-wrapper.PREVIEW.txt` forwarding to stock `/home/bin/hdl`, read-only host checker and rollback plan. **No install, no hook activation, no flash writes or reboot conducted.** Confirm v0.11 mapping on real A31 from `/tmp` before any flash staging; then separately review wrapper compatibility, backup/recovery and request explicit permission.

## v0.11 live device table load — hardware-confirmed (2026-10-21)

User SSH output from physical A31 at `192.168.0.35` shows successful upload to `/tmp`, execution of `/tmp/knx-audio-v11 --map /tmp/knx-map.csv --show-map`, and **successful parsing of all 12 CSV records** (`MAP_TABLE mode=CSV rows=12 path=/tmp/knx-map.csv`). Confirmed mapping includes `3/1/6→MUTE(state)`, `3/1/0→VOL_UP(param=2)`, `3/1/1→VOL_DOWN(param=2)`, `3/0/0→PLAY_PAUSE`, `3/0/1→PLAY`, `3/0/2→PAUSE`, `3/0/4→NEXT`, `3/0/5→PREV`, `3/2/0..3→PRESET_1..4`, all four `press1`.

- `CONFIG_SOURCE=1.1.22`, `CONFIG_INTERFACE=192.168.0.35`, `CONFIG_FILE=LOADED`; `SAFETY max_volume=100 volume_step=2 volume_repeat_ms=90 button_debounce_ms=250`.
- The first transfer prompted one SSH `Permission denied` after an incorrect password attempt, but a retry succeeded. Final `--show-map` output verifies the binary and CSV were both accessible on the target.
- **Status: HARDWARE-CONFIRMED for CSV loading, parsing, mapping and printing only.** `--show-map` does **not** execute KNX→player commands. The table-driven `--run-all` path, persistence after reboot, and install/autostart remain unverified.
- No flash writes or boot-script changes were made by this test. Previous v0.10 KNX command behavior remains a separate hardware baseline. Recommended next single integration run (after stopping older active versions): `/tmp/knx-audio-v11 --map /tmp/knx-map.csv --run-all`; observe one mapped preset and one Mute action, then proceed to staged persistent install with explicit permission and safe rollback.

## v0.11 physical A31 command dispatch using CSV — 2026-10-21

User executed on real A31: `/tmp/knx-audio-v11 --map /tmp/knx-map.csv --run-all`, after `--show-map` had already demonstrated 12 parsed rows. **Status: HARDWARE-CONFIRMED for CSV-driven GroupAddress→action dispatch; Mute state effect readback confirmed; Preset 1 TCP sent but playback not yet explicitly reconfirmed for this v0.11 run.**

Exact excerpt:
```text
MAP_TABLE mode=CSV rows=12 path=/tmp/knx-map.csv
PROBE_LOOPBACK_RC=0 mute=0
API_OK endpoint=127.0.0.1 original_mute=0
ACTIVE_INSTANCE_GUARD_OK port=43997
MODE=RUN_ALL audio_writes=MUTE_VOLUME_TRANSPORT_PRESETS
JOIN_OK group=224.0.23.12:3671 on 192.168.0.35
KNX_EVENT 1 src=1.1.22 ga=3/2/0 action=PRESET_1 value=1 param=1
PRESET_TCP_SEND_RC=0 slot=1
PRESET_TRANSMITTED playback_not_readback_verified
ACTION_PRESET_TRANSMITTED_UNACKNOWLEDGED
KNX_EVENT 2 src=1.1.22 ga=3/1/6 action=MUTE value=1 param=0
HTTP_MUTE_WRITE_RC=0 requested=1
READBACK_RC=0 actual=1 expected=1
READBACK_MATCH
ACTION_READBACK_VERIFIED
KNX_EVENT 3 src=1.1.22 ga=3/1/6 action=MUTE value=0 param=0
HTTP_MUTE_WRITE_RC=0 requested=0
READBACK_RC=0 actual=0 expected=0
READBACK_MATCH
ACTION_READBACK_VERIFIED
```

The transcript stops without showing Ctrl+C or elapsed runtime; make no claim about process exit, multi-hour stability or persistence. Prior v0.10 and v0.9 presets 1/2 were independently confirmed by operator observation, but those observations cannot substitute for a new physical playback report in v0.11.

**Next architecture milestone:** package and stage `/vendor/knx/{knx-audio,knx-map.csv,knx-audio.conf}` with backups and verify the executable+CSV on persistent mount, only with explicit device-write approval. Native boot path `/home/user.sh` uses `/vendor/user/hdl` as the **replacement** for stock essential `/home/bin/hdl`, not a generic hook. Do not activate `/vendor/user/hdl` or touch stock service without separately agreed recovery and rollback mechanism. Also note boot's possible /vendor format on error or FORCE_FORMAT_FLAG.

## First persistent data install — staged, NOT YET RUN (2026-10-21)

After physical `v0.11 --map /tmp/knx-map.csv --run-all` confirmed table-driven Mute ON/OFF with readback and Preset1 TCP transmission, the operator explicitly **authorized writing exactly the native binary, map CSV and config to `/vendor/knx` on A31 `192.168.0.35`**. Autostart, hdl, flash images, system scripts and reboot were **not authorized**.

Package `A31_KNX_VENDOR_INSTALL_V1.zip` was prepared and verified offline, but **the operator has not yet executed it**. Its contents include immutable v0.11 MIPS32 LE static ELF, one Mac installer, a temporary remote install script, read-only verifier, checksum list and Russian README.

First install only, deliberate fail-closed path:
1. Mac SSH reads **current live tested** `/tmp/knx-audio.conf` and `/tmp/knx-map.csv` from A31 to a private Mac `backup-YYYYMMDD-HHMMSS` directory; uses the v0.11 executable.
2. Mac streams these three files plus a remote helper as a `tar` stream to a uniquely named **RAM** staging directory.
3. Remote helper checks admin UID0, `/dev/mtdblock9 /vendor jffs2 rw` mount, **≥512 KiB free**, nonempty inputs, and that `/vendor/knx` does not already exist. It runs `--show-map` from RAM before any persistent write.
4. If all checks pass, it stages exactly three files under a uniquely named `/vendor/.knx-firstinstall-<pid>` directory, `chmod 700` binary/dir, `chmod 600` mapping/config, then **renames the directory** to `/vendor/knx` within the same JFFS2 filesystem.
5. Runs `--show-map` from installed paths; Mac reads all three back and confirms exact byte matches using `cmp`.

No modification of `/vendor/user/hdl`, `/home/user.sh`, `live.sh`, `rcS`, stock audio player, raw MTD, or activation of autostart. On installation error or missing tar/SSH capability, stop and inspect logs; **do not run ad-hoc flash commands**. Read-only verification command is shipped as `VERIFY_INSTALLED.sh`. Until a real installation log is returned, persistent installation is **UNVERIFIED / NOT CLAIMED COMPLETE**.

Next milestone after successful install is to inspect installed persistent files and separately design/review a reversible startup shim. The established boot hook **overrides** essential `hdl`, so it must never be activated without a separate risk assessment, board recovery and explicit approval.

## First install attempt blocked by missing BusyBox tar — v1.1 repair (2026-10-21)

User executed the `A31_KNX_VENDOR_INSTALL_V1/INSTALL_TO_A31.sh` first-install flow on Mac against lab A31 `192.168.0.35:24678`. Step 1 succeeded, retrieving existing `/tmp/knx-audio.conf` and `/tmp/knx-map.csv` into a Mac backup:

```text
MAC_BACKUP=/Users/lab/AI/A31_Firmware/A31_KNX_VENDOR_INSTALL_V1/backup-20261021-025505
Step 2: RAM-only stage, validation and first-install to /vendor/knx...
sh: tar: not found
```

Root cause: stock BusyBox A31 lacks `tar`. The previous Mac installer streamed a tar archive that the A31 was supposed to extract **under /tmp**, so the failure occurred **before** running `REMOTE_INSTALL.sh` or performing its three-file JFFS2 write. **The log does NOT establish that files were installed to /vendor/knx.** Prior /tmp temp cleanup is separate; do not claim the destination is empty until a read-only check confirms it.

Fixed artifact **`A31_KNX_VENDOR_INSTALL_V1_1.zip`** is staged offline:
- Same ELF as v1, SHA256 `7c7743c43e0b9869eb67c8209f83c8bbed862c683203efe72f15bb2ae4fcd884`; no changes to KNX mapping engine or protocol.
- On Mac, back up live tested config/map again, then make remote RAM staging folder. Transfer ELF, config, map and helper one by one via `ssh -T ... 'cat > /tmp/<unique>/name'` — known to work on this BusyBox build.
- Continue unchanged fail-closed `REMOTE_INSTALL.sh`: require root, JFFS2 RW `/vendor`, >=512 KiB free, absent `/vendor/knx`, successful `--show-map` from RAM; only then write 3 files to uniquely named staging directory and rename it to `/vendor/knx`.
- Replace tar-based readback with three `ssh cat` reads into temporary Mac folder, compare with `cmp`.
- Mac ZIP integrity test, `bash -n` and `sh -n` pass; **not run on physical device yet**. Stage v1.1 only within operator-approved `/vendor/knx` scope: no changes to `hdl`, boot, RootFS, raw MTD, autostart, or reboot.
- Avoid rerunning first-install blindly if destination exists: inspect outcome and seek explicit instruction for updates/rollback.

Outcome is **installer v1 failed early; backup confirmed; install not yet confirmed.** Await new v1.1 installation log with `INSTALL_OK` plus 3 `BYTE_MATCH` lines.

## Vendor install v1.1 halted on absent `id`; corrected in v1.2 (2026-10-21)

Operator's lab A31 SSH installer log:
```text
PREFLIGHT_OK
MAC_BACKUP=/Users/lab/AI/A31_Firmware/A31_KNX_VENDOR_INSTALL_V1_1/backup-20261021-030141-52242
RAM_SENT knx-audio
RAM_SENT knx-map.csv
RAM_SENT knx-audio.conf
RAM_SENT REMOTE_INSTALL.sh
/tmp/a31-knx-firstinstall-20261021-030141-52242/REMOTE_INSTALL.sh: line 15: id: not found
ERROR: remote session must run as root (admin UID 0).
INSTALL_STOPPED (code=11).
```
The error arises because stock BusyBox has **no external `id` binary**. It is NOT evidence that the admin account lacks root privileges. The remote script exited at line 15, before any JFFS2 staging/copy; **no installed `/vendor/knx` has been confirmed**, and the next install still fails closed if destination already exists. SSH transfer to /tmp was successful and Mac backups were created.

Package **`A31_KNX_VENDOR_INSTALL_V1_2.zip`** fixes the deployer only:
- `REMOTE_INSTALL.sh` reads the real UID from `/proc/self/status` with POSIX shell builtin `read`, preserving UID0 enforcement without `id`.
- Replaces `df ... | awk` with shell built-in parsing of `df -k /vendor` to avoid the possibly absent `awk`; requires numeric available KiB and >=512 KiB free.
- Verifies availability of `chmod`, `cp`, `mv`, `sync`, `ls`, `mkdir`, `rm` before the first persistent write.
- The KNX v0.11 MIPS executable remains **byte-for-byte unchanged**, SHA256 `7c7743c43e0b9869eb67c8209f83c8bbed862c683203efe72f15bb2ae4fcd884`.
- Local `sh -n`, `bash -n`, file hashes, ZIP test passed; unit-simulated UID parser read 0 and simulated A31 `df` output parsed 1836 KiB. **NOT YET RUN ON PHYSICAL A31.**
- Same authorized scope: only create three files under `/vendor/knx`, no changes to essential `hdl`, /vendor/user/hdl, boot scripts, raw flash or autostart.

Mac next command: `bash A31_KNX_VENDOR_INSTALL_V1_2/INSTALL_TO_A31.sh`. Expected `PERSISTENT_PREFLIGHT_OK`, `INSTALL_OK`, three `BYTE_MATCH`, `SUCCESS`. Stop on error and review the log; never blindly delete the persistent destination.

## Installer v1.2: false-negative BusyBox utility lookup; v1.3 RAM-operation preflight (2026-10-21)

Operator ran approved installer v1.2 against A31 `192.168.0.35:24678`. Existing destination preflight succeeded and all four staged files were uploaded to RAM; Mac backup captured at `/Users/lab/AI/A31_Firmware/A31_KNX_VENDOR_INSTALL_V1_2/backup-20261021-031250-52417`. Remote helper stopped **before any new /vendor writes**:
```text
PREFLIGHT_OK
RAM_SENT knx-audio
RAM_SENT knx-map.csv
RAM_SENT knx-audio.conf
RAM_SENT REMOTE_INSTALL.sh
ERROR: BusyBox utility not found: chmod; no flash writes.
INSTALL_STOPPED (code=20).
```

This message was produced by the installer's `command -v chmod` probe. Since this A31 had previously executed `chmod` successfully, this is evidence of an unreliable utility-discovery check **not proof that chmod itself is absent**. Exact cause (shell builtin support vs PATH) has not been experimentally isolated; do not make a stronger claim.

**Corrected package: `A31_KNX_VENDOR_INSTALL_V1_3.zip`.** Replaces the preflight use of `command -v` with **actual filesystem-operation tests entirely under the unique RAM stage**: `mkdir`, `cp`, `chmod`, `mv`, `ls`, `rm`, `rmdir`, `sync`. If any fails, helper stops before creating anything in `/vendor`. Preserves explicit UID check from `/proc/self/status`, JFFS2 RW validation, >=512KiB free, table `--show-map`, first-install no-overwrite policy, staged JFFS2 directory rename and 3 byte-by-byte Mac `cmp` verifications. Native v0.11 ELF unchanged (SHA-256 `7c7743c43e0b9869eb67c8209f83c8bbed862c683203efe72f15bb2ae4fcd884`). No changes to `hdl`, `/vendor/user/hdl`, init scripts, RootFS, raw MTD or autostart.

Offline tests: `busybox ash -n` remote helper, `bash -n` Mac installer, zip integrity/hashes all pass; simulated **end-to-end remote helper** under BusyBox `ash` using isolated mock mount/df/ELF succeeded writing exactly three files, and repeated run exited with code 13 refusing overwrite. **Physical A31 v1.3 installation NOT YET CONFIRMED.** User can run `bash A31_KNX_VENDOR_INSTALL_V1_3/INSTALL_TO_A31.sh` after unpacking. Wait for `INSTALL_OK`, 3 `BYTE_MATCH` lines and `SUCCESS` before marking deployed.

## v0.11 permanent vendor install — HARDWARE-CONFIRMED (2026-10-21)

**Installed successfully on physical A31 at 192.168.0.35** with Mac installer `A31_KNX_VENDOR_INSTALL_V1_3/INSTALL_TO_A31.sh`. This is a permanent-file installation, **not autostart or a whole-firmware flash**. The live log reports:

```text
PREFLIGHT_OK
RAM_SENT knx-audio
RAM_SENT knx-map.csv
RAM_SENT knx-audio.conf
RAM_SENT REMOTE_INSTALL.sh
/tmp/a31-knx-firstinstall-20261021-031854-52532/REMOTE_INSTALL.sh: line 80: rmdir: not found
PERSISTENT_PREFLIGHT_OK uid=0 available_kib=1836 tools=RAM_TESTED
MAP_TABLE mode=CSV rows=12 path=/tmp/a31-knx-firstinstall-20261021-031854-52532/knx-map.csv
INSTALL: /vendor/knx created. Checking installed file paths (read-only)...
MAP_TABLE mode=CSV rows=12 path=/vendor/knx/knx-map.csv
CONFIG_FILE=LOADED
SAFETY max_volume=100 volume_step=2 volume_repeat_ms=90 button_debounce_ms=250
-rwx------ 1 0 0 45564 knx-audio
-rw------- 1 0 0   442 knx-audio.conf
-rw------- 1 0 0   590 knx-map.csv
/dev/mtdblock9 2048 232 1816 11% /vendor
INSTALL_OK (persistent files only; no service/hdl changes; no autostart)
BYTE_MATCH knx-audio
BYTE_MATCH knx-map.csv
BYTE_MATCH knx-audio.conf
SUCCESS: three files installed in /vendor/knx.
NO AUTOSTART. NO HDL CHANGES. NO REBOOT.
```

Mac backup: `/Users/lab/AI/A31_Firmware/A31_KNX_VENDOR_INSTALL_V1_3/backup-20261021-031854-52532`. Preserve for recovery.

**Evidence classification:** JFFS2 files written and byte-verified; CSV and config parsed from **installed persistent paths**. Persistence after an actual power cycle has not been physically tested; RAM-driven v0.11 KNX dispatch with actual Mute readback was already confirmed separately in the preceding milestone. New persistent-path active playback is not independently exercised here.

**Non-fatal flaw:** remote BusyBox lacks `rmdir`; the installer emitted a warning while cleaning an isolated **RAM-only** tool-test directory at remote helper line 80, but proceeded to a successful byte-verified install. Future installer versions should replace `rmdir` in RAM-stage cleanup with a carefully scoped supported method; **do not rerun a first-install script** merely to fix the warning.

**Next phase (NOT AUTHORIZED YET):** offline design a reversible autostart mechanism. The only identified live hook, `/vendor/user/hdl`, replaces an essential `/home/bin/hdl` invocation; it is **not** a generic startup script hook. Do not write a shim to it or alter stock player, boot scripts, RootFS, raw MTD or reboot without separate recovery planning and authorization.

## KNX Autostart Stage v1 — prepared offline; NOT ACTIVATED (2026-10-21)

After first physical installation of the three permanent v0.11 files under `/vendor/knx`, the operator requested continuation of the autostart work. Offline stage package `A31_KNX_AUTOSTART_STAGE_V1.zip` has been created, including `hdl-wrapper.sh`, `TEST_OFFLINE.sh`, `VERIFY_A31_READONLY.sh`, `README_RU.md`.

Proposed wrapper (NOT deployed) uses a background subshell: wait 20s, honour `/vendor/knx/disabled`, verify binary/CSV/config, run `knx-audio --config /vendor/knx/knx-audio.conf --map /vendor/knx/knx-map.csv --run-all`, log to volatile `/tmp/knx-boot.log`; foreground path unconditionally `exec /home/bin/hdl "$@"`. This preserves stock HDL process semantics in principle but is **not real-device validated with the bundled `daemonize`**. The `/vendor/user/hdl` hook replaces essential hdl; do not activate it without independent recovery access and dedicated device-side compatibility checks.

Three offline mock tests passed: normal both-service start; `disabled` prevents KNX and starts hdl; missing CSV prevents KNX and starts hdl. ZIP integrity test passed. The stage also includes a **read-only** SSH audit of currently installed files, any existing override, running processes and vendor free space. No hook written, no daemonize changed, no device restart, no MTD/rootfs modifications. Activation remains pending a distinct approval and recovery plan.
