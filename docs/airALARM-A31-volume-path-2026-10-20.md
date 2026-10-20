# airALARM A31 — live codec/volume path audit, 2026-10-20

Source bundle: `A31_VOLUME_PATH_20261020_035157.zip`, uploaded by operator after read-only SSH + extracted-firmware scan. Device identified in project as A31 Rakoit 4.6.415156 at `192.168.0.35`. Origin of each assertion is identified below. No commands to change audio level, firmware, NVRAM, or playback were run.

## Live-device verified evidence

- `/proc/devices` registers a distinct character device named `nop_codec` with **major 246**, and device node `/dev/nop_codec` is **246:0** (`crw-r--r--`).
- `/dev/ttyS0` is **4:64**, and is distinct from `/dev/nop_codec`.
- `mv_ioguard` PID **711**, parent `rootApp` PID **676**, has FD **5 → /dev/nop_codec** and FD **3 → /dev/ttyS0**. This is a strong candidate to investigate for external codec and master-volume control, but **does not prove that volume is written on these channels or the meaning of any ioctl request**.
- `wmrmplayer` PID **880** has FD **14 → /dev/pcmC0D0p**; live `/proc/880/maps` additionally maps `/dev/pcmC0D0p`. `libasound.so.2.0.0`, `libmvmsg.so`, and `libmad.so.0.2.1` are loaded into it. Indicates active use of ALSA/MMAP playback interface; **not a demonstrated master gain controller**.
- `a01controller` PID **807** maps `libasound.so.2.0.0`, `liblpml_alsa.so`, `libmad.so.0.2.1` and `libmvmsg.so`, but had no direct PCM FD in this snapshot. `volumeprompt` PID **773** loads `libmvmsg.so` and had no direct PCM FD. Absence of a particular FD at an instant is not absence of functionality.
- `/proc/asound/card0/pcm0p/sub0/hw_params`: `MMAP_INTERLEAVED`, `S16_LE`, `44100 Hz`, `2 channels`, `period_size=2048`, `buffer_size=16384`. PCM state `RUNNING`. `owner_pid=12963` remained in status, but PID not visible in the `ps` snapshot. ALSA delay/avail values were anomalous; avoid interpreting them as accurate latency. Hardware PCM `mtk_snd` is labeled `noop`; codec path may be vendor-specific.
- Registration entries `i2s_config` (221), `i2s0` (234), `alsa` (116), `sound` (14) also appear in `/proc/devices`. These show driver interfaces are available, not how zone volume is applied.
- `ssh_stderr.txt` contains only the OpenSSH post-quantum algorithm warning. No permission or BusyBox matching errors in this run.

## Static evidence from ORIGINAL firmware files, not live function tracing

`mv_ioguard` is 32-bit MIPS32 rel2 ELF. SHA256: `41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3`.

Its strings/symbol-name scan includes all these exact names:
- `VolumeSetCodec`, `MuteCodec`, `PauseCodec`, `PromptCodec`;
- `Function_VolumeSet`, `Function_VolumeNotify`, `Function_MuteSet`, `Function_VolumeUp`, `Function_VolumeDown`;
- `g_force_muted`, `g_codec_mcu_mute`, `codec_check_mute_thread`;
- `setPlayerCmd:vol++`, `setPlayerCmd:vol--`, `GNOTIFY=VOLUMECHANGE`, `GNOTIFY=volume_prompt_start`, `GNOTIFY=volume_prompt_end`;
- `/dev/nop_codec`, `/dev/ttyS0`;
- diagnostic `mv_ioguard set the volume(%d) g_wiimu_shm->volume(%d)`, `!!!!!!!!!!!!!!PromptCodec %d`, `mv_ioguard set the startup volume as %d`, ` max prompt volume %s`.
Dynamic imports include `ioctl`, `open`, `read`, `write`, plus `volume_pormpt_direct` and `volume_pormpt_action`. **Combined live FDs and these static symbols are strong leads, but actual call sites / ioctl numbers and order are NOT YET analyzed.** Do not claim confirmed control of master volume or independent Prompt volume from symbol names alone.

Additional static sources:
- `liblpml_alsa.so` has symbols/names `LPML_ALSA_helper_selfVol_get`, `LPML_ALSA_helper_vol_get`, `LPML_ALSA_helper_mute_flag_get`, `LPML_ALSA_helper_fade_flag_get`, `LPML_ALSA_helper_fade_step_get`, `LPML_ALSA_fade`. These may be involved in stream software gain. Exact semantics and users unverified.
- `wmrmplayer` has `audio_alsa_init`, `audio_alsa_play`, `snd_pcm_writei`, and multiroom volume-sync related strings. This is evidence of playback and syncing code, **not of master-zone hardware gain**.
- `a01controller` imports `snd_pcm_writei`, `snd_pcm_open`, `wmrm_sound_write`, `ioctl`, and Prompt helpers. Requires focused callsite analysis.

## Next batch and intended interpretation boundary

Generated **`a31_codec_volume_deep_batch.sh`** as a read-only Mac/radare2 bundle to disassemble `VolumeSetCodec`, `MuteCodec`, `PromptCodec`, `Function_VolumeSet`, `Function_VolumeNotify`, relevant `ioctl` and `open` cross-references; plus `liblpml_alsa.so` gain helper functions and `a01controller` ioctl callsites. Reports and ZIP default under **`/Users/lab/AI/airALARM`**; source extracted firmware under **`/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`**. Tested with `bash -n` and end-to-end mock `radare2`/ZIP invocation, **NOT run on original Rakoit binaries**. Operator: download into project directory and execute `bash a31_codec_volume_deep_batch.sh`, send ZIP. Some `sym.X` lookups may be missing in stripped binaries; inspect `*_symbols.txt` and stderr before treating absence as a negative finding.

**Goal status:** fixed audible airALARM Prompt loudness independent of zone master level still **UNSOLVED**. Preserve working airALARM v0.1.26, device volume, and NVRAM.
