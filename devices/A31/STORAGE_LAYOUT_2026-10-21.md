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
