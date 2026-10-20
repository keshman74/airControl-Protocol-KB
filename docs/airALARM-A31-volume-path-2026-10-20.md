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


## Offline deep codec-volume investigation: 2026-10-20 03:58

Operator supplied `A31_CODEC_VOLUME_DEEP_20261020_035829.zip`; inspected its original radare2 outputs:
- `mv_ioguard` 32-bit MIPS ELF SHA256 `41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3`, report ~52.8 KB.
- `liblpml_alsa.so` SHA256 `1edfefb68a7be62f2dbcd9b11b2fad8cc6bd431127674c15cf99264806282a7a`, report ~10.9 KB.
- `a01controller` SHA256 `835d646bb83d3cf8d26c2ce1a3d115aaa323f781e0e2e102a62f8a42520a283b`, symbols ~148 KB.
This is **static binary evidence**, not live proof of acoustic gain behavior.

### Key confirmation: VolumeSetCodec performs TWO routes

`mv_ioguard` symbol `VolumeSetCodec` at VA `0x0040f0f0`, size 476. Code at `0x0040f118–0x0040f128` calls `MCUCommandSend(9,3, &volume_arg, 4)` (raw argument integer stored on caller stack, argument semantics/MCU frame not yet verified). This is an **explicit separate MCU channel**, rather than purely changing local software gain.

If `g_platform_opt.codec_dev` pointer at `g_platform_opt+4` is nonzero, subsequent `0x0040f140–0x0040f244` code locks `codec_mute_mutex`, opens configured codec-dev pathname using `open(path,O_RDWR)`, reads **40 bytes** into stack struct, modifies a state field, writes **40 bytes**, closes FD, unlocks. It logs `mv_ioguard set the volume(%d) g_wiimu_shm->volume(%d)`; second value is **`*(g_wiimu_shm + 0x3BC)`** (`0x0040f1b8`), thereby giving strong evidence that shared-memory offset `0x3BC` relates to zone volume. If state indicates a force-muted condition and requested volume becomes positive, sends another `MCUCommandSend(10,3,&zero,4)` after 20 ms at `0x0040f28c–0x0040f2a0`; **do not treat this as a harmless command to reproduce** or infer exact mute semantics from integers alone.

This strongly suggests dual volume handling via MCU control and codec driver state, but DOES NOT YET PROVE which of them affects physical final loudness nor what master-independent Prompt gain can be applied.

### Important negative: PromptCodec is a COUNTER, not amplitude setter

`PromptCodec` at VA `0x0040efc4` (size 300): locks the same mutex and opens the configured codec device, reads 40-byte state, manipulates field at stack offset `0x2c` (offset **0x0C** inside state struct at stack base `sp+0x20`): when arg1==1 increments, when arg1==-1 resets to zero, otherwise decrements if >0, then writes state back. Diagnostic `!!!!!!!!!!!!!!PromptCodec %d` references the resulting counter. **No arithmetic for a gain-setting value in this function.** It may activate codec behavior elsewhere when prompt flag/count changes, so this is not proof that codec hardware has no prompt-sensitive gain logic.

`MuteCodec` at VA `0x0040ee60`, size 356 likewise reads/writes a 40-byte state struct, updates a mute-like field and can send `MCUCommandSend(0x23,3,...)`. `PauseCodec` at `0x0040ed48` handles a pause-state field. The meaning of MCU IDs still needs command-send framing and receiver analysis.

### Controller and LPML software-gain paths

`Function_VolumeSet` `0x004068a0` and `Function_VolumeNotify` `0x00406ae8` update `g_vol_save` and send volume-related socket messages (`SocketClientReadWriteMsg`). These are event relay/reporting paths, not evidence of independent Prompt output gain.

`liblpml_alsa.so` `LPML_ALSA_fade` `0x00000cf8`, size 680, is **actual PCM sample-processing logic**, invoked by `LPML_snd_pcm_writei`. It calls helper `LPML_ALSA_helper_mute_flag_get`, `LPML_ALSA_helper_vol_get`, `LPML_ALSA_helper_selfVol_get`, `LPML_ALSA_helper_fade_flag_get`, and `LPML_ALSA_helper_fade_step_get`; implements volume/fade state updates, and reads/writes signed 16-bit PCM samples via `lh/sh` at `0x00000eb8–0x00000ee8` and `0x00000f08–0x00000f34`. Calls scaling helper at `0x00000bd0`. This is a *software/stream PCM path*, separate from MCU/codec control. Need dump the actual scaler and find its runtime users before claiming it affects native Prompt.

`a01controller` report provides symbols and ioctl / `wmrm_sound_write` cross-refs, but **does not identify a codec master gain setter** from this report.

### Targeted next offline batch

Prepared and syntax-checked `a31_codec_mcu_trace_batch.sh`; test run with mock radare2 sources produced a valid ZIP. It dumps `sym.MCUCommandSend`, `VolumeSetCodec`, `PromptCodec`, `MuteCodec`, `SendDataByI2S`, event parser section, `LPML_ALSA_fade`, scale helper `0x00000bd0`, and rootApp startup/state context. Reports and ZIP default to `/Users/lab/AI/airALARM`, original firmware input `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`. Execute on user's Mac `bash a31_codec_mcu_trace_batch.sh` and upload ZIP. **Original binary run pending**.

**Goal remains UNSOLVED:** fixed acoustic air alert volume independent of zone master volume. Preserve working airALARM v0.1.26, no NVRAM changes, no commands to MCU or codec.


## A31 MCU command framing, LPML Q16 processing (2026-10-20 04:04)

Operator supplied `A31_CODEC_MCU_TRACE_20261020_040432.zip`. Inspected original static radare2 reports: `mv_ioguard.txt` (1199 lines), `liblpml_alsa.txt` (279 lines), `rootApp.txt` (293 lines), README and manifest. All report stderr contains analysis INFO only, no command errors. Binary SHA256s match prior batches (`mv_ioguard 41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3`, `liblpml_alsa.so 1edfefb68a7be62f2dbcd9b11b2fad8cc6bd431127674c15cf99264806282a7a`, `rootApp 0314cbeb5961127bef4668317183f66e7b8cec7eeb1f323445c622dd20992a97`). **Entirely offline binary evidence, not a live hardware experiment.**

### Confirmed: MCUCommandSend is a dual-destination command formatter

- `mv_ioguard` `sym.MCUCommandSend` starts at `0x0040c8dc` (symbol size 3144 bytes); arguments `a0=command_id`, `a1=destination bitmask`, `a2=data pointer`, `a3=length`. MIPS prologue zeroes a `0x2000` (8192-byte) formatted-command buffer at `sp+0x20`; `0x0040c924–0x0040c950` checks `command_id < 50` and dispatches by a GP-relative **jump table**. `pdf` skipped the jump-table cases; therefore **the exact format for command ID 9 was NOT decoded by this batch**. Do not claim this is a raw UART byte command or a known wire format.
- At `0x0040d4bc–0x0040d50c`, after a nonempty formatted command is assembled, `destination bit0 (1)` invokes `*(g_mcu_opt+8)`, and `bit1 (2)` invokes `*(g_socket_opt+8)`; a1=`3` therefore requests BOTH paths when their callbacks are installed. These are callbacks, not yet proof of transport identity (UART/MCU and socket are inferred from names).
- `VolumeSetCodec` at `0x0040f118–0x0040f128` invokes `MCUCommandSend(9,3,&volume,4)`. Conditional secondary call after a 20ms delay: `MCUCommandSend(10,3,&zero,4)` at `0x0040f28c–0x0040f2a0`. The conditions relate to codec state/force-mute; **never reproduce these MCU calls on hardware without a controlled safety plan**.
- `MuteCodec` at `0x0040ef70–0x0040ef84` invokes `MCUCommandSend(0x23,3,formatted_text,0x40)`. Confirms the dispatcher handles both integer-like and formatted-text inputs, but each ID may serialize differently.
- `ParseCommonMCUEvent` invokes `MCUCommandSend(9,a1,&(g_wiimu_shm->field_0x3BC),4)` at `0x004171e0–0x004171f8`. This independently ties **command ID 9 to SHM offset 0x3BC (zone volume)**.
- `PromptCodec` at `0x0040efc4` only modifies a 40-byte codec-state struct's prompt-active counter `+0x0C` via read/write (increment arg1=1; reset arg1=-1; decrement other arg values while >0); it is not an amplitude setter in this function.

### Confirmed: SendDataByI2S is structured framed device I/O, NOT demonstrated PCM volume

`sym.SendDataByI2S` at `0x0040e528` pads payload to a 4-byte boundary, allocates `padded_size+20`, opens a device path stored in rodata (actual string **not decoded yet**), invokes `ioctl` requests `0xC0045005`, `0xC0045006`, `0xC0045002` with parameters (`16`, `2`, `0xAC44`) and writes a framed packet with markers including `0x20174564` and `0x45642017`. This may be a special device/MCU transfer routine but must not be used as evidence of audio PCM transmission or master gain. **No attempt to call it on the device.**

### Confirmed: LPML software PCM scaling

- `LPML_snd_pcm_writei` `0x00000ab8` invokes `LPML_ALSA_fade` on its PCM buffer and then actual `snd_pcm_writei` (`0x00000b0c`). 
- `LPML_ALSA_fade` `0x00000cf8` examines helper getters for mute, overall volume, self volume, fade status and fade step; iterates over signed 16-bit samples, passes them to scaler `fcn.00000bd0` and writes transformed 16-bit samples back at `0x00000ee8` or `0x00000f34`.
- `fcn.00000bd0` multiplies sample by coefficient at `0x00000be0`, applies conditional quantization/dither below `0x10000`, then `sra v0,v0,16` at `0x00000c28`: Q16-style digital gain. This is independent of smplayer's other coefficient-stage, but **its use by running native URL Prompt has NOT been demonstrated**. The runtime owner/path matters.

### Particularly relevant: rootApp STARTUP prompt compensation formula

`rootApp` `sym.StartupMusic` reads `MaxPromptVolume` at `SHM+0x3D8` and zone volume at `SHM+0x3BC`. At `0x004031a0–0x004031c4` it conditionally computes `MaxPromptVolume*100/zoneVolume` and passes a derived `s1` value to `volume_pormpt_direct(...,1,s1)` at `0x00403284`. If zone volume is below MaxPromptVolume or MaxPromptVolume is zero, `s1` remains zero; the branch for a quotient of 100 also special-cases zero. This shows **some Rakoit startup prompts account for zone gain**, but does **NOT** establish the behavior of `playPromptUrl` or a supported way to get fixed audible alert volume.

### Next focused static batch

Prepared `a31_mcu_routing_batch.sh` to extract 50-entry GP-relative command dispatch table of `MCUCommandSend` at `0x00428840` and automatically disassemble cases `9`, `10`, `35` after validating target addresses stay within `0x0040c8dc..0x0040d524`. Also dumps startup ratio and LPML scale for context. Uses radare2 + python3; stores reports and ZIP in `/Users/lab/AI/airALARM`, original extracted binaries read-only. `bash -n` and mocked radare2 table decoder, ZIP complete run passed. **Not yet run against genuine MIPS binaries.** Operator should download into project directory and run `bash a31_mcu_routing_batch.sh`.

**Status:** master-independent fixed acoustic volume for airALARM remains UNSOLVED; no NVRAM or firmware changes.


## MCU routing table batch: 2026-10-20 04:17

Operator supplied `A31_MCU_ROUTING_20261020_041758.zip`. Read-only static analysis of original `mv_ioguard` SHA256 `41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3`; no live MCU or device writes.

The GP-relative dispatch table at ELF VA `0x00428840` decoded successfully as **50 entries indexed command_id 0–49**. All 50 targets reside in `MCUCommandSend` function `0x0040c8dc..0x0040d524`. Important targets: ID 9 => `0x0040c9dc`; ID 10 => `0x0040caa4`; ID 11 => `0x0040ca5c`; ID 12 => `0x0040ca80`; ID 35 (0x23) => `0x0040d1e0`. Several entries intentionally route to common final dispatch at `0x0040d4bc`. Full table retained in user-supplied archive CSV `reports/jump_table_decoded.csv`.

**Confirmed ID 9 formatting:** handler loads input integer through `lw a3,(s0)`, splits cases `value < 10` (format-string VA `0x00425634`), `10 <= value < 100` (VA `0x00425644`), and `value == 100` (literal VA `0x00425654`). Other values >100 are not accepted by the third branch; **negative values** would enter first branch, so do not state that the handler rejects negatives. Both formatted branches use `snprintf`, exact strings NOT YET EXTRACTED. ID 10 invokes `snprintf` with input integer and format VA `0x00425684`; ID 35 does `strncpy(output,input,0x1fff)` then common send path. The header/payload of the serial/wire protocol remains UNKNOWN until these strings are extracted. Do not assume safe or correct to issue raw ID 9/10 commands to A31.

**Prior conclusions unchanged:** `VolumeSetCodec` dispatches ID 9 to callback mask 3; `PromptCodec` handles prompt counter and has no gain arithmetic itself; `rootApp.StartupMusic` contains conditional quotient `MaxPromptVolume*100/zoneVolume` for startup prompt, not confirmed for URL Prompt. Master-independent constant acoustic alert loudness remains UNSOLVED.

Next static batch `a31_mcu_format_batch.sh` was generated and validated with `bash -n` (not yet run against original firmware). It reads the inferred string addresses `0x00425634/44/54/64/74/84` using radare2 `ps`, grabs hex bytes for cross-check, and dumps case blocks, saving ZIP under `/Users/lab/AI/airALARM`. User should download script there and run `bash a31_mcu_format_batch.sh`.
