> Продолжение V1; следующий [volume-path audit](airALARM-A31-volume-path-2026-10-20.md) уже содержит последующие выполненные batches. Формулировки «next/pending» ниже относятся к моменту записи, не ко всей цепочке. [Сводка и потребители](../functions/notifications/README.md).

# airALARM A31: live audio batch V2 — 2026-10-20

Source: user-provided original `A31_LIVE_AUDIO_V2_20261020_034559.zip`. Executed from Mac against user's Rakoit A31 at `192.168.0.35` through a read-only SSH session. Hardware evidence from `a31_live_audio_v2.txt` and `ssh_stderr.txt`, not from offline code alone. No user credentials, SSH process environment or device secrets archived.

## Verification of diagnostic tooling

The V2 `remote_readonly.sh` replaces unsupported BusyBox `grep -E` with multiple `grep -e`. `ssh_stderr.txt` contains only OpenSSH's post-quantum KEX warning; no BusyBox grep errors. Output includes `READ_ONLY_BATCH_V2_COMPLETE`. Sections covering process maps and file descriptors were actually populated and are interpretable (unlike V1's corresponding empty sections).

## Live PCM and audio route

- Runtime `/tmp/alsa/asoundrc` points `default → plug → asymed → dmixer`, and live `dmixer.conf` specifies `dmix → hw:0,0`, rate `44100`, `S16_LE`, stereo, 2048 frames/period, 16384 frames/buffer.
- `/proc/asound/cards`: card 0 `mtk_snd`, label `noop`. `/proc/asound/pcm`: `00-00: mtk pcm noop-0`, one playback and capture.
- PCM hw_params in live capture: `MMAP_INTERLEAVED, S16_LE, 2 channels, 44100 Hz, period_size 2048, buffer_size 16384`. Status says `RUNNING`.
- Kernel PCM `status` reports `owner_pid: 12963`, which is **absent** from both collected `ps` snapshots; hardware PCM status also reports large negative delay, huge positive avail and `appl_ptr=0`. These data are anomalous / possibly driver-specific or stale; do not infer which active process controls the stream from that owner value.
- Existence of live config strongly supports expected DMIX route; process `smplayer` was not captured during a Prompt and its effective inherited `ALSA_CONFIG_PATH` was not checked. Master-independent loudness remains unproven.

## HIGH-VALUE HARDWARE DISCOVERY: mv_ioguard holds codec and serial nodes

Live `ps` and `/proc/<pid>/fd`:
- `mv_ioguard`, PID 711, parent `rootApp` (PID 676), maps `libmvmsg.so`. Open FDs: **`/dev/nop_codec` and `/dev/ttyS0`** (plus `/dev/null`). These are actual live handles and now high-priority clues for tracking common master-zone attenuation / external codec controls. **Cannot conclude** that the process actually writes volume to either device or what commands it uses.
- `wmrmplayer`, PID 880, parent `rootApp`, maps `libasound.so.2.0.0`, `libmad.so.0.2.1`, `libmvmsg.so`. Open FDs: **14 → /dev/pcmC0D0p**, **13 → /dev/timer**. Also maps a shared device-backed memory region `30062000-30072000 rw-s ... /dev/pcmC0D0p`; matches ALSA MMAP playback behavior.
- `a01controller`, PID 807, parent `rootApp`, maps `libasound.so.2.0.0`, `liblpml_alsa.so`, `libmad.so.0.2.1`, `libmvmsg.so`. Live FDs include `/dev/plock` and `/dev/urandom`; **no matching direct PCM device FD observed in that snapshot**. Its mapped libasound alone is not evidence of active PCM playback.
- `volumeprompt`, PID 773, parent 1, maps `libmvmsg.so`; no direct PCM FD visible at time of capture. This does not disprove its role in command routing.
- `rootApp`, PID 676, maps `libmvmsg.so`, no direct PCM FD visible.
- `intercom`, `airplay`, `imuzop`, `imuzop_dec` map ALSA or audio codec-related shared libraries but did not show PCM FDs in the snapshot. Loading a library is not proof of current playback.
- `/dev/snd` is symlink to `/dev`; actual character nodes include `pcmC0D0p`, `pcmC0D0c`, `mixer`, `audio`, `dsp`, `controlC0`, `vdsp`.

## Next research step

The critical unknown is **where the master-zone gain is applied** after software Prompt amplitude scaling, and whether it can safely be compensated without disturbing radio volume.

Created `a31_volume_path_batch.sh` (Bash syntax validated and smoke-tested with fake SSH + ZIP) to inventory **read-only** live `/dev/nop_codec`, `/dev/ttyS0`, `/proc/misc`, `/proc/devices`, relevant process FDs/maps and PCM, plus static string/import references from extracted `mv_ioguard`, `wmrmplayer`, `a01controller`, `rootApp`, `liblpml_alsa.so`, `libasound.so`. It writes report + ZIP under `/Users/lab/AI/airALARM`. The operator must download and execute it on Mac: `cd /Users/lab/AI/airALARM && bash a31_volume_path_batch.sh`. The script is **not** yet run on original A31 for this batch. No code changes to airALARM v0.1.26, master volume or NVRAM.

Status: **static firmware finding + hardware evidence of codec handle; not a proven independent acoustic Alert-volume implementation**.
