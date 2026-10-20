# A31 flash/mount inventory — hardware READ-ONLY, 2026-10-21

Source: user-provided `A31_STORAGE_LAYOUT_READONLY.txt`, read on *live* A31 device (`192.168.0.35`). `/proc/version`: Linux 2.6.36+, Linkplay Buildroot gcc 4.6.4, 2022-04-27. This is observed data, not an assumption based on a donor stock image.

## Confirmed live mounts

| Mount | Backing | FS | Mode | Persistence interpretation |
|---|---|---|---|---|
| `/` | `/dev/root` = `/dev/mtdblock6` per cmdline | squashfs | `ro` | RootFS image; do **not** write directly |
| `/mnt` | `/dev/mtdblock8` | jffs2 | `rw` | persistent *candidate* user storage, 512 KiB raw |
| `/vendor` | `/dev/mtdblock9` | jffs2 | `rw` | persistent *candidate* user storage, 2 MiB raw |
| `/tmp` | none | ramfs | `rw` | volatile |
| `/etc` | none | ramfs | `rw` | volatile |
| `/var` | none | ramfs | `rw` | volatile |
| `/media` | none | ramfs | `rw` | volatile |

Other visible virtual mounts: `/proc` proc, `/sys` sysfs, `/dev/pts` devpts; `/dev` populated via ramfs. `/system/workdir` exists with writable permission bits, but its filesystem is not reported as a separate persistent mount; **do not infer** that it is writable or persistent from `ls -ld` alone.

## MTD layout and cautions

```text
mtd0  0x01000000  ALL               (16 MiB)
mtd1  0x00030000  Bootloader        (192 KiB)
mtd2  0x00010000  Config            (64 KiB)
mtd3  0x00010000  Factory           (64 KiB)
mtd4  0x00200000  bkKernel         (2048 KiB)
mtd5  0x001e039f  Kernel
mtd6  0x0094fc61  RootFS
mtd7  0x00b30000  Kernel_RootFS    (11456 KiB aggregate)
mtd8  0x00080000  user             (512 KiB)  -> /mnt
mtd9  0x00200000  user2            (2048 KiB) -> /vendor
erasesize=0x10000 (64 KiB) on all listed MTD records
```

Boot cmdline: `console=ttyS1,57600n8 root=/dev/mtdblock6`. **Never write raw MTD partitions, kernel, bootloader, rootfs or firmware aggregate based only on this inventory**. Raw MTD sizes are not available filesystem free-space. The mount table establishes the existence of writable JFFS2, **not that any files currently placed there are safe to replace**, nor which boot script invokes them.

## Native KNX firmware integration proposal (not executed)

- **Candidate** location: `/vendor/knx/` containing MIPS ELF `knx-audio`, `knx-map.csv` and `knx-audio.conf`. This is tentative until actual `df`, `du`, directory inventory, and boot sequence are reviewed.
- In RAM load the 64-entry native KNX table at startup; persistent CSV and config remain on writable JFFS2.
- Leave tested Linkplay A31 transport, Mute, volume, TCP8899 presets untouched. Use a single native KNX process with explicit backoff/startup order; provide rollback path. No need to replace the stock audio application.
- Discover existing legitimate user/vendor boot hooks before selecting an autostart integration technique. Files under `/etc` are RAM-backed and may be recreated at each boot.
- Plan backup (file and full board/recovery strategy) and separate approval before **any** write to Flash/autostart. Current stage is exclusively read-only.
- Do **not** conclude that `/vendor` can hold the package until confirming free space/firmware scripts; raw size 2 MiB does not equal free space.

## Follow-up read-only evidence

Collect using `df -k /mnt /vendor`, `du -k /mnt /vendor`, `ls -la /mnt /vendor`, inspect (read-only) `/etc/inittab`, `/etc/init.d`, `/system/workdir` and known startup hooks. Mac-side helper `A31_FLASH_BOOT_AUDIT_READONLY.sh` produces `A31_FLASH_BOOT_AUDIT.txt` via SSH; it does not write to the player.

**Validation status:** physical layout confirmed; flash free space / safe install path / persistent service startup **NOT YET CONFIRMED**.

## Live read-only storage and boot audit — 2026-10-21

Operator supplied `A31_FLASH_BOOT_AUDIT.txt` collected on the actual A31 (`192.168.0.35`).

```text
/dev/mtdblock8  512 KiB total   216 KiB used   296 KiB free   42%  /mnt
/dev/mtdblock9 2048 KiB total   212 KiB used  1836 KiB free   10%  /vendor
```

- `/vendor/knx/` has sufficient **reported** free-space headroom for the ~46KiB native KNX v0.11 ELF plus config and mapping. This is a **candidate**, not a verified safe runtime/install path. Filesystem wear, 64KiB erase blocks, vendor ownership and possible wipe-on-update must be accounted for.
- `/mnt` currently holds `totalqueue.xml`, `qobuz_account.json`, `keymap.xml`. Preserve these player settings; do not overwrite or replace them.
- `/vendor` top-level directories: `wiimu`, `user`, `misc`, `data`; retain them. No `/vendor/bin`, `/vendor/etc` or `/vendor/init.d` exists in this live audit.
- `/etc/init.d` is a symlink to `/etc_ro/init.d`, but `NO_INIT_D_DIRECTORY` was returned by the probe (may be absent or a dangling symlink). `/etc/inittab`, `/etc/rcS`, `/etc/rc.local` are absent. These findings **do not rule out** other boot paths.
- `/system/workdir/` on the live device contains `live.sh`, `userrestore.sh`, `factory.sh`, `evn.sh`, `script/`, and `bin/`. Their **contents and invocation order were not inspected in this audit**. In a previously archived *different firmware image* (`RAKOIT_2024_all_scripts.txt`) `live.sh` invoked `/home/user.sh`, and the old `live.sh` contained automatic reformat logic for JFFS2 under some error conditions. **Do not assume the archived scripts match the current running 2022 A31 build**; verify on the physical device before selecting any hook.
- `/system/workdir` has writable Unix mode bits, but the provided mounts report root SquashFS read-only. Do not infer that it is a persistent writable location.
- **No writes to Flash, firmware, init scripts, or autostart were performed** in the audit.

Next read-only diagnostic: `A31_BOOT_CHAIN_READONLY.sh` retrieves exact live startup-file metadata and *selected* hook lines from `/etc_ro/rcS`, `/home/user.sh`, `/system/workdir/live.sh`, `/system/workdir/userrestore.sh`, `/system/workdir/evn.sh`, and `/sbin/lan.sh`. This is the final design input before proposing an installation method; avoid modifying existing boot scripts until a rollback/recovery plan exists. If no supported persistent hook exists, evaluate a controlled rootfs repack/stock OTA path rather than hijacking legacy `/vendor/user/hdl` or modifying unrelated services.
