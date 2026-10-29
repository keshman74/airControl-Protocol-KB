# A31 Rakoit Silent + Native KNX v0.11 — V6E hardware-verified build and reproducibility

Date: 2026-10-30 (operator confirmation, following 2026-10-29 build).
Status: **CONFIRMED on one spare A31**, with the limitations below. Preserve this checkpoint; do not modify the tested binary in place.

## Device and boundaries

- Spare physical A31: `192.168.0.29`, device `Office 29`, Rakoit firmware `4.6.415156`, build `a31rakoit`, project `UP2STREAM_PRO_V4`. SSH `admin@192.168.0.29:24678`.
- Main A31 `192.168.0.35` **not flashed** in these V6D/V6E tests.
- Tool used for physical OTA: **LinkPlay Debug Tool For Custom v1.5.9** in Windows. This is the confirmed operator update path for the spare unit; do not substitute raw MTD writes.
- Source OTA: `a31rakoit-4.6.415156-b1-c3bddec5-20240816.bin`, SHA-256 `0f4de8352091b7d688a4040e57cacc230c4bfa789454269c2546b2aaa4565ffa`. Original kernel retained.

## Reproducible build mechanism — V6E

macOS project directory `/Users/lab/AI/A31_Firmware`. Linux Lima VM `a31-build`; writable Linux workspace `/home/lab.guest/A31_Firmware`. The Mac shared directory is read-only from Lima: copy sources into Linux HOME before building.

Local inputs:
- `RAKOIT_BASE_2024/rootfs.squashfs`: original Rakoit rootfs;
- `RAKOIT_SILENT_ROOTFS_STAGE14`: silent voice-prompt stage;
- `A31_KNX_SOURCE_V011`: native KNX MIPS32 little-endian static ELF/config/CSV/wrapper;
- original OTA `a31rakoit-4.6.415156-b1-c3bddec5-20240816.bin`.

Retained builder:
- `A31_UNIVERSAL_BUILD_V6E_DELAYED_BOOT.zip` unpacked inside the project directory;
- `A31_UNIVERSAL_BUILD_V6E_DELAYED_BOOT/INSTALL_AND_BUILD_ON_MAC.sh`;
- installer saves previous builder as `A31_UNIVERSAL_BUILD_V6_BACKUP_<timestamp>`, installs V6E hook/build logic and invokes Lima build.
- invocation:
```bash
cd "/Users/lab/AI/A31_Firmware"
unzip -o A31_UNIVERSAL_BUILD_V6E_DELAYED_BOOT.zip
bash A31_UNIVERSAL_BUILD_V6E_DELAYED_BOOT/INSTALL_AND_BUILD_ON_MAC.sh
```

Builder reconstructs squashfs **in Linux, not macOS**, preserving Unix ownership and 68 device nodes. Base format: SquashFS 4.0, xz, 524288-byte blocks. It retains the original OTA kernel; packs custom rootfs into structural OTA with validated header/data CRC. Source-diff allowlist must pass; no other stock boot chain changes are authorized.

V6E tested build ID: `A31-Rakoit-4.6.415156-Silent-KNX-V6E-20261029-215907`.
- RootFS bytes: `6852608`; SHA-256: `5e54cd4b598812df148a4528c686bd14632d35ba2e4b435cfac0c9498f538dfd`.
- OTA output filename: `A31-Rakoit-4.6.415156-Silent-KNX-V6E-20261029-215907-NOT-FLASHABLE.bin`.
- OTA SHA-256: **`886b13056eb3bc721fffb5c78e921ccb87f6cc46796754ae2202756423aad431`**.
- Lima output: `/home/lab.guest/A31_Firmware/A31_UNIVERSAL_BUILD_V6_OUTPUT/<BUILD_ID>/<OTA_FILENAME>`.
- Project release folder: `/Users/lab/AI/A31_Firmware/Firmware Relise/` (operator-chosen exact spelling). Transfer via `limactl shell a31-build -- cat "<Lima OTA path>" > "Firmware Relise/<OTA_FILENAME>"` then `shasum -a 256`. Actual Mac-side digest matched the above.
- Builder log: `BUILD_V6_PASS`, `OTA_KERNEL_PRESERVED=PASS`, `OTA_CRC=PASS`, `PACKED_BOOT_CHAIN_AND_KNX=PASS`, `ROOTFS_DEVICES_68=PASS`, `ROOTFS_OWNERSHIP=PASS`, `SOURCE_DIFF_ALLOWLIST=PASS`, `V6E_DELAYED_BOOT_HOOK=PASS`, `V6D_KNX_BINARY_PRESERVED=PASS`.
- Builder emitted `FLASH_READY=FALSE`, `BOOT_HARDWARE_VERIFIED=FALSE`, file suffix `NOT-FLASHABLE` **before** physical tests; these are conservative build-time labels, not a post-test denial. Do not silently rewrite the file or claim certification for other units.

### Boot integration (critical regression guard)

Inside rootfs:
- `/usr/share/a31-knx/knx-audio`, `knx-audio.conf`, `knx-map.csv`, `hdl-wrapper-v5.sh`, `boot-hook.sh`.
- `/home/user.sh` invokes `/bin/sh /usr/share/a31-knx/boot-hook.sh` if executable.
- Preserve original stock `hdl` via `daemonize /home/bin/hdl`. Existing vendor override `/vendor/user/hdl` has priority; on spare, that legacy shim was renamed to `/vendor/user/hdl.disabled-v6d` *after an individually MD5-verified backup*, so RootFS hook is authoritative.
- Native KNX CLI (hardware-confirmed): `./knx-audio --config /usr/share/a31-knx/knx-audio.conf --map /usr/share/a31-knx/knx-map.csv --run-all`.
- **V6D failure mode:** hook attempted KNX before local Linkplay HTTP API was ready; first boot log `PROBE_LOOPBACK_RC=-146`, `PROBE_A31_IP_RC=-128`, `API_PROBE_FAILED abort no audio writes`. When manually run after boot, *the identical* native binary showed `API_OK`, `JOIN_OK`, and KNX MUTE succeeded. Do not reinstate early one-shot launch or orphaned lock.
- **V6E fix:** background supervisor, approximately 20-second initial delay, bounded retries (up to 12 attempts with 5-second intervals), duplicate-instance prevention and lock cleanup on worker/supervisor end. Preserve this boot readiness/retry behavior, KNX binary and mappings unless subsequently hardware-verified otherwise.
- Journal: `/tmp/a31-rootfs-knx-boot.log`; processes: `ps | grep "[k]nx-audio"`. BusyBox 1.12.1 `grep` does **not** accept `-E`; do not infer absence of a process from that failed command.

## Hardware proof — V6E

After actual OTA and restart, operator supplied:
```text
ps: 1012 admin 204 S knx-audio
V6E_SUPERVISOR_STARTED
V6E_KNX_ATTEMPT=1
PROBE_LOOPBACK_RC=0 mute=0
API_OK endpoint=127.0.0.1 original_mute=0
ACTIVE_INSTANCE_GUARD_OK port=43997
MODE=RUN_ALL audio_writes=MUTE_VOLUME_TRANSPORT_PRESETS
JOIN_OK group=224.0.23.12:3671 on 192.168.0.29
KNX_EVENT 1 src=1.1.22 ga=3/1/6 action=MUTE value=1 param=0
HTTP_MUTE_WRITE_RC=0 requested=1
READBACK_RC=0 actual=1 expected=1
READBACK_MATCH
ACTION_READBACK_VERIFIED
KNX_EVENT 2 src=1.1.22 ga=3/1/6 action=MUTE value=0 param=0
HTTP_MUTE_WRITE_RC=0 requested=0
READBACK_RC=0 actual=0 expected=0
READBACK_MATCH
ACTION_READBACK_VERIFIED
KNX_EVENT 3 src=1.1.22 ga=3/0/0 action=PLAY_PAUSE value=1 param=0
HTTP_ACTION_RC=0 action=PLAY_PAUSE
HTTP_ACCEPTED_NOT_STATE_VERIFIED
```
Trace included more PLAY_PAUSE sends and additional MUTE readback matches; heartbeat error count was 0. Note: PlayPause log proves API acceptance only. **Operator independently confirmed actual PLAY/PAUSE effect**, and independently confirmed physical volume +/- and Presets 1–4 playback. Operator also confirmed **KNX autonomously starts again after complete power-off / power-on, without SSH or manually launching a process**. Radio playback, SSH and Linkplay HTTP status were observed working after flashing. Thus V6E is the **hardware-verified checkpoint** for this exact device and image.

Default KNX addresses:
- `3/1/6` MUTE (state 0/1);
- `3/1/0` VOL+, `3/1/1` VOL-;
- `3/0/0` PLAY_PAUSE;
- `3/2/0`, `3/2/1`, `3/2/2`, `3/2/3` Presets 1–4.
- KNX source filter `1.1.22`; source groups AUX/USB disabled.
- Physical evidence for custom standalone PLAY, PAUSE, NEXT, PREV commands in **V6E** is not asserted by this confirmation.

## Preservation rules and limits

1. **Do not overwrite or delete the tested V6E image or its matching SHA.** Keep a unique build ID/date for each modified firmware.
2. For future changes, preserve Rakoit original kernel, squashfs metadata (especially device nodes), stock `hdl`, duplicate-instance guard, delay/retries, native ELF and CSV mappings, unless a new physical test explicitly supersedes them.
3. Do **not** generalize this proof to main A31, alternate A31 revisions, A97/A98/A33, factory OTA, unsigned image acceptance on every unit, production recovery or mass release.
4. Existing rollback/source artifacts, full flash backups and old stage evidence remain separate. A flash backup by itself does not prove independent brick recovery without UART.
5. Longer soak, failure/recovery under network/KNX router outage, and regression testing across other devices remain open.

Evidence: operator-provided Mac build/transfer logs, SSH process/boot logs, physical MUTE & transport/preset/volume tests, and power-cycle confirmation in A31 Firmware project conversation on 2026-10-29/30.
