> **Частично SUPERSEDED:** пустые maps/FD/filter результаты из-за неподдерживаемого grep -E недействительны. [V2](airALARM-A31-live-audio-v2-2026-10-20.md) реально выполнен и заменяет только эти разделы; остальные V1 наблюдения сохранены. См. [общую функцию](../functions/notifications/README.md).

# A31 live audio SSH diagnostics — 2026-10-20

Source: user-provided A31_LIVE_AUDIO_20261020_033238.zip. Evidence is hardware-observed unless explicitly qualified. The session was read-only.

## Confirmed
- Device Linux 2.6.36+, ALSA 1.0.23. Audio card index 0 named mtk_snd (noop), playback PCM 00-00.
- Runtime /tmp/alsa/asoundrc includes dmixer.conf and defines default -> plug -> asymed -> dmixer. Runtime dmixer.conf specifies dmix on hw:0,0 at 44100 Hz, 16-bit, two channels, period 2048, buffer 16384.
- Kernel PCM hw_params: MMAP_INTERLEAVED, S16_LE, 44100 Hz, 2 channels, period 2048, buffer 16384. Status reports RUNNING and owner_pid 12963, but PID 12963 does not appear in the following process snapshot. Hardware counters delay=-12617728, avail=12634112, hw_ptr=12617728, appl_ptr=0 are anomalous and require interpretation; do not treat them as a latency measurement.
- Process snapshot includes rootApp PID 676, volumeprompt 773, wmrmplayer 880, a01controller 807. PIDs change on restart.
- Earlier separate operator observation showed wmrmplayer had /dev/pcmC0D0p open; do not treat the current archive as a reconfirmation of that handle.

## Critical test failure
The first version of the live audio diagnostic script used remote grep -E, unsupported by BusyBox 1.12.1. stderr repeatedly reported invalid option E. Consequently empty results for audio library mappings, per-process file handles, kernel module matches and config-hook filtering are INVALID TESTS, not negative findings. The SSH session itself completed and emitted the end marker.

## Correction
Prepared a31_live_audio_batch_v2.sh, read-only, one SSH session, stores ZIP under /Users/lab/AI/airALARM. All remote filters use BusyBox-supported grep -e; remote script avoids whoami, id, tr and uname. It collects per-process maps, audio FDs, process metadata and a second PCM snapshot. Bash syntax checked, BusyBox grep -e tested and mock SSH + ZIP workflow passed. Device run is pending.

## Interpretation
The runtime ALSA configuration and PCM params agree with the proposed dmixer route, but actual Prompt-time use and the location of downstream master-zone attenuation remain unverified. Do not claim independent fixed acoustic alert volume. No airALARM v0.1.26, NVRAM or volume changes were performed.
