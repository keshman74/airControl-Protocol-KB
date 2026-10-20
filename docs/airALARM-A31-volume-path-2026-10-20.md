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


## Original MCU wire-text formats extracted from mv_ioguard (2026-10-20 04:24)

Source: original uploaded `A31_MCU_FORMAT_20261020_042412.zip`; `reports/format_strings.txt` and `reports/rodata_hex.txt`. Binary SHA256 `41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3`, ELF 32-bit little-endian MIPS32 rel2. **OFFLINE STATIC CONFIRMATION ONLY — not hardware-tested commands**.

At `mv_ioguard` virtual addresses:
- `0x00425634`: literal `AXX+VOL+00%d\\n`; branch at `0x0040c9dc` for input less than 10 (signed negative also enters this branch; constrain usage to 0..100, do not say negative is rejected).
- `0x00425644`: literal `AXX+VOL+0%d\\n`; branch for integer >=10 and <100.
- `0x00425654`: literal `AXX+VOL+100\\n`; branch only for input exactly 100, otherwise no formatted VOL string emitted.
- `0x00425664`: `AXX+CHN+%03d\\n` (another command ID, not VOL).
- `0x00425674`: `AXX+EQS+%03d\\n`.
- `0x00425684`: `AXX+MUT+00%d\\n` (MCU command ID 10, with separate parameter pointer and >=4-byte payload).
- `0x00425694`: `AXX+PMT+002\\n`.
- `0x004256a4`: `AXX+PMT+001\\n`.
- `0x004256b4`: `AXX+PMT+000\\n`.

MIPS handler `0x0040cad8..0x0040cb48` dispatches input integer 2 => PMT+002; 1 => PMT+001; other => PMT+000. These values are **prompt command modes**, not demonstrated amplitudes, and need not represent a dedicated prompt gain level. Literal newline `0x0a` terminates strings before NUL. The above commands originate from the internal MCU formatter; **not HTTP API commands**, and no direct UART/MCU injection is authorized or advisable.

Prior binary analysis showed `VolumeSetCodec` calls `MCUCommandSend(9,3,&volume,4)`; the formatted text then passes to two callback paths selected by mask 3. Which active physical transport sends each callback is not fully demonstrated. The existence of separate `AXX+PMT` commands is a new lead for investigating alert ducking/mode, not evidence of master-independent alert loudness.

Runtime issue: `reports/format_strings.stderr.txt` emits radare2 hint `Relocs not applied`; raw rodata bytes and direct disassembly validate the literal formats regardless. Future calls may set `-e bin.relocs.apply=true` for symbol readability.

**NEXT FOCUS:** cross-reference call sites and dispatch ID (likely PMT modes, but verify) for `AXX+PMT` and compare with SHM MaxPromptVolume / the URL Prompt entry path. Stay offline/read-only, preserve airALARM v0.1.26; do not confuse fixed digital gain with fixed acoustic loudness.


## Next investigation: PMT mode event flow (2026-10-20)

From the **previously uploaded** original MCU routing jump-table CSV (static firmware analysis), dispatch **command ID 18** maps to handler `0x0040cad8` in `mv_ioguard.MCUCommandSend` (50 entries from VA `0x00428840`). Original earlier rodata extraction confirmed that this case selects `AXX+PMT+002\\n` for int 2, `AXX+PMT+001\\n` for int 1, and `AXX+PMT+000\\n` otherwise. **These are internal MCU commands, not documented HTTP API controls.** This is binary-confirmed string generation, not proof of MCU physical effect. `PromptCodec` is independently known to mutate local prompt-state counts and does not itself compute numeric gain. Actual downstream MCU response and alert-volume independence remain unknown.

Prepared **`a31_pmt_trace_batch.sh`** to search static code references to `MCUCommandSend` and `PromptCodec`, fully dump ID18 formatter, rootApp `StartupMusic`, `libmvmsg` prompt helpers, and `smplayer` start/end notices. Defaults to original firmware `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`; report and ZIP under `/Users/lab/AI/airALARM`. Tested with `bash -n` and end-to-end mocked radare2/ZIP workflow, **not yet executed on original firmware**. Mac run: `cd /Users/lab/AI/airALARM && bash a31_pmt_trace_batch.sh`. No SSH/device operations, NVRAM writes, audio play or volume changes.

Research objective remains UNSOLVED: fixed perceived alarm loudness independent of zone/master volume. Preserve airALARM v0.1.26.


## PMT notification call trace: user bundle 2026-10-20 04:32

Operator uploaded `A31_PMT_TRACE_20261020_043252.zip`. Its read-only radare2 reports include `mv_pmt.txt`, `mv_callers.txt`, `root_prompt.txt`, `lib_prompt.txt`, `sm_prompt.txt`. All binaries' hashes match preceding original Rakoit archives (mv_ioguard SHA256 41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3; smplayer baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac).

**NEW static-binary-confirmed callsites**:
- `mv_ioguard.sym.cmdSocket_recive` invokes `sym.PromptCodec` at `0x00411c54`, `0x00411d0c`, `0x00411dc4`. These cross-references show **three paths from the socket message handler into PromptCodec**, but the current report does not dump enough caller context to accurately assign START, END or reset semantics per path; avoid inventing event names.
- `PromptCodec` at `0x0040efc4` still confirmed to modify the local codec prompt-active counter at struct offset +0x0C by read/write under mutex (arg1=1 increments, arg1=-1 zeroes, other inputs decrement if positive). It does not directly compute amplitude.
- `smplayer` literal notification strings `GNOTIFY=volume_prompt_start` (VA 0x00408c6c) and `GNOTIFY=volume_prompt_end` (VA 0x00408b84) are present and prior code analysis showed their send path. **A complete source-to-destination mapping to `cmdSocket_recive` branches is not yet shown by this bundle.**
- `MCUCommandSend` ID18 at 0x0040cad8 still maps values 0/1/2 to `AXX+PMT+000/001/002\\n`. **It is not established whether the three `PromptCodec` callsites also issue ID18**, nor what the MCU does when it receives PMT.
- `rootApp.StartupMusic` still uses conditional `MaxPromptVolume*100/zoneVolume` but only for startup prompt; the user-facing `playPromptUrl` path has not been proven to do the same.

**Next focused read-only batch**: `a31_pmt_callpath_batch.sh` created and `bash -n` checked. It dumps wide `cmdSocket_recive` disassembly near 0x00411a80–0x00411e30, PMT handler, smplayer prompt notices and URL string xrefs. Works only with extracted ELF files, creates ZIP under `/Users/lab/AI/airALARM`. It was not yet run on original Mac firmware. Preserve airALARM v0.1.26, do not send direct MCU commands.

**Status:** independent fixed acoustic Prompt volume remains UNSOLVED.


## Critical static finding: PromptCodec caller ALSO sends MCU PMT (2026-10-20 04:43)
Source: user-uploaded `A31_PMT_CALLPATH_20261020_044307.zip` containing original `mv_ioguard`, `smplayer` and `rootApp` radare2 dumps. **STATIC BINARY-CONFIRMED, NOT LIVE MCU CAPTURE.** Corrects the previous incomplete inference that `PromptCodec` calls might not link to MCU ID18: the socket receiver indeed directly sends ID18 after the PromptCodec calls.

**`mv_ioguard.cmdSocket_recive`**:
- compares incoming socket message (pointer s1) to a 27-byte string at VA `0x00426b78`. On match at `0x00411c50–0x00411c58`, calls `PromptCodec(1)`. If `SHM+0x3D0 != 2` and an auxiliary global flag is zero, writes zero to `SHM+0x3D0`, writes 1 to the auxiliary flag, then `MCUCommandSend(18, 3, &(SHM+0x3D0),4)` at `0x00411ca0` with value 0, yielding `AXX+PMT+000\\n`. If `SHM+0x3D0 == 2` and auxiliary flag is zero, sets auxiliary flag 1, prepares zero in a stack variable and likewise sends PMT 000 at `0x00411cd8`. **In these captured branches the sent value is 0, not 2.** The meaning of preexisting SHM+0x3D0==2 is not yet resolved.
- compares input to 25-byte string at `0x00426b94`; on match calls `PromptCodec(0)` at `0x00411d0c–0x00411d10`. If additional conditions are satisfied, sets `SHM+0x3D0=1`, auxiliary global flag 0, then `MCUCommandSend(18,3,SHM+0x3D0,4)` at `0x00411d58` (PMT 001). In the SHM+0x3D0==2 branch it prepares 1 on stack and sends PMT 001 at `0x00411d90`. Other branches exit without send.
- compares input to 26-byte string at `0x00426bb0`; on match calls `PromptCodec(-1)` at `0x00411dc4–0x00411dc8` and exits; no ID18 send directly in that captured branch.
- `MCUCommandSend` command ID 18 selects `AXX+PMT+002\\n` for argument int=2, `AXX+PMT+001\\n` for int=1, `AXX+PMT+000\\n` for other values. **The captured socket Prompt start/end branches send 0 and 1 respectively; no PMT 002 was observed in these branches**. Correct any earlier summary claiming start could send 002.
- Exact contents of the incoming socket strings at VA `0x00426b78`, `0x00426b94`, `0x00426bb0` must be extracted in next batch. Candidate matches to smplayer `GNOTIFY=volume_prompt_start/end` are still hypotheses pending literal address decoding.
- `rootApp` string `playPromptUrl` is present at VA `0x00420a78`, but report `axt @ 0x00420a78` returns no xrefs. Thus do **not** claim that the current report traces actual URL Prompt HTTP dispatch or MaxPromptVolume compensation.

**Implication:** PCM prompt state and MCU PMT notification are coupled at the runtime socket event layer. This is NOT evidence PMT gives independent output amplitude or that it is safe to call on its own. The acoustic fixed-alert-volume requirement remains UNSOLVED.

Next investigation: extract exactly three incoming notification strings, cross-check their payload and senders; separately inspect how `playPromptUrl` reaches `smplayer`. Do NOT send low-level MCU commands or modify airALARM v0.1.26.


## PMT event strings definitively resolved from firmware (2026-10-20 04:49)

Uploaded bundle `A31_PMT_EVENT_STRINGS_20261020_044925.zip`, inspected original `mv_ioguard.txt`, `sm.txt`, `root.txt`, r2 command files, manifest. Confirmed original ELF SHA256 hashes unchanged: mv_ioguard 41b127e2dee1ce98d99e6d493a198a4dea7afbee5bc4de2e1deb04b8316f79f3; smplayer baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac; rootApp 0314cbeb5961127bef4668317183f66e7b8cec7eeb1f323445c622dd20992a97.

**STATIC BINARY CONFIRMED:**
- mv_ioguard incoming socket notification literal at 0x00426b78: `GNOTIFY=volume_prompt_start`, corresponding to `cmdSocket_recive` call `PromptCodec(1)` at 0x00411c54 and conditional `MCUCommandSend(18,3,...)` sending **PMT 000**.
- Literal at 0x00426b94: `GNOTIFY=volume_prompt_end`, corresponding to `PromptCodec(0)` at 0x00411d0c and conditional MCU **PMT 001**.
- Literal at 0x00426bb0: `GNOTIFY=volume_prompt_init`, corresponding to `PromptCodec(-1)` at 0x00411dc4, local reset; no MCU PMT send confirmed in that branch.
- `smplayer` contains exact `GNOTIFY=volume_prompt_start` and `GNOTIFY=volume_prompt_end` strings, with send-path in main established previously. This is compelling binary-level source/receiver string match; actual packets between processes have **not** been live-captured.
- rootApp `playPromptUrl` is present at VA 0x00420a78; `axt @ 0x00420a78` yielded no references in current radare2 analysis. Therefore URL Prompt HTTP parser → smplayer startup → volume argument chain is **not fully traced**. Lack of xref is not evidence of unsupported API; URL Prompt works in earlier hardware tests.

**Important correction:** In previously captured start/end handler branches, PMT start sends 0 and end sends 1 when conditions allow. Do NOT claim PMT 002 is sent at start from these branches. Meaning of PMT 002 on MCU and analog output remains unknown. PMT is **mode signaling, not proven separate gain**. Fixed acoustic airALARM loudness across master-zone volume levels is still UNSOLVED.

Prepared next offline script `a31_prompt_url_trace_batch.sh` (bash syntax verified, actual operator execution pending) for consolidated rootApp HTTP command parser, smplayer and notification receiver analysis; output ZIP under `/Users/lab/AI/airALARM`. No live device control, firmware modification or NVRAM changes.


## RootApp URL Prompt entrypoint identified, 2026-10-20 04:54

User uploaded original `A31_PROMPT_URL_TRACE_20261020_045428.zip`; extracted and examined `root.txt`, `mv.txt`, `lib.txt` and command scripts. Read-only static analysis.

**Confirmed new linkage:** `rootApp` string `playPromptUrl` at VA `0x00420a78` has a **real code xref from `sym.GoaheadCmdParsethread` at `0x0040fbd4`** (`addiu a1,a1,str.playPromptUrl`). Earlier bundles without a fully analyzed parser returned an empty xref; absence was a tooling limitation, now corrected. `rootApp` adjacent .rodata literals `smplayer` VA `0x00420a88` and `smplayer %s &\\n` VA `0x00420a94`; proximity suggests but does **not yet prove** the URL Prompt branch uses this exact shell formatting or what gain it passes.

`libmvmsg.so` still confirms shared helper `volume_pormpt_direct` calls smplayer with formats `smplayer %s %d %s` and `smplayer %s %s`. `mv_ioguard` confirms receiving `GNOTIFY=volume_prompt_start/end/init` and passing start/end to MCU mode PMT 000/001 under conditions. Their integration with actual URL Prompt needs parser block disassembly.

**Next targeted offline bundle prepared**: `a31_prompt_http_handler_batch.sh` analyzes `rootApp` `0x0040fae0..0x0040fd20`, the `playPromptUrl` xref, adjacent strings and `system/popen` callsites. This read-only script needs operator execution against extracted Rakoit rootApp on Mac. Output ZIP under `/Users/lab/AI/airALARM`; no direct A31 commands. Script syntax checked with `bash -n`; radare2 run pending.

**Open question:** whether `playPromptUrl` invokes smplayer with direct percentage parameter or inherited zone-volume compensation. Fixed audible alert loudness independent of zone volume remains UNSOLVED.


## HTTP Prompt handler branch disassembled (2026-10-20 04:57)

Source: uploaded original `A31_PROMPT_HTTP_HANDLER_20261020_045715.zip`, including `rootApp` r2 disassembly of `sym.GoaheadCmdParsethread`. **STATIC BINARY VERIFIED**, not a runtime trace of a specific request.

- At `0x0040fbc8–0x0040fbe0`, `strncmp(input,"playPromptUrl",13)` selects this HTTP command branch. Code sets `s2=input+14` at `0x0040fc00`.
- `0x0040fc08–0x0040fc18` calls `strstr(s2,<literal VA 0x0041baec>)`. Exact needle **NOT YET decoded**. This branch's success is required to reach player-spawn code.
- `0x0040fc20–0x0040fc30` loads field `g_wiimu_shm+0x3C8` and tests `<40` (`slti v0,v0,0x28`). Semantics of field 0x3C8 **UNKNOWN**; do not call it current master volume or priority mode without confirmation.
- On allowed path, `terminalPidbyName("smplayer")` at `0x0040fc40`, `snprintf(buf,0x3ff,"smplayer %s &",s2)` at `0x0040fc60`, and `system(buf)` at `0x0040fc70`. The invoked shell command therefore incorporates raw argument substring `s2`. It does not append a separately computed gain number in this branch, but the supplied substring can itself include a CLI gain argument.
- On rejected path, execution writes a short error/response via `UnixSocketServer_write`; the literal has not been fully decoded. The recognized branch returns a 2-byte response after system() at `0x0040fc88`. **Never assert that all playPromptUrl invocations work for every URL string**.
- Separate hardware tests previously showed some `playPromptUrl:<url>%20<number>` forms do play with software gain and radio resumes; this static analysis clarifies one possible parser path, but actual string value at 0x0041baec must be resolved first.
- The exact format literal at `0x00420a94` reads `smplayer %s &`; `smplayer` literal at `0x00420a88`, command literal `playPromptUrl` at `0x00420a78`.

Prepared `a31_prompt_http_conditions_batch.sh` (syntax checked with bash -n, device run pending) to extract the `strstr` needle VA 0x0041baec, command bytes and surrounding branch, report under `/Users/lab/AI/airALARM`. It reads only original firmware `rootApp`; no SSH, audio playback or device writes. **Alert independent of master volume remains UNSOLVED.**


## HTTP handler acceptance condition resolved (2026-10-20 05:07)
User uploaded `A31_PROMPT_HTTP_CONDITIONS_20261020_050723.zip`. Offline rootApp SHA256 `0314cbeb5961127bef4668317183f66e7b8cec7eeb1f323445c622dd20992a97` unchanged. Original r2 text confirms:
- `rootApp.GoaheadCmdParsethread`, `strncmp(input,"playPromptUrl",13)` at 0x0040fbd8; `s2=input+14` at 0x0040fc00.
- `strstr(s2, "mp3")` at 0x0040fc10, with **needle literal exactly `mp3` at VA 0x0041baec**. This is substring matching, not an extension/MIME validation. No case-insensitive handling demonstrated.
- If match is non-NULL, `g_wiimu_shm->field_0x3C8 < 40` check (`slti v0,v0,0x28` at 0x0040fc2c). This is a signed comparison; if false, reject branch at 0x0040fca0. **Field purpose unknown** and must not be described as current zone volume. Threshold is *not* a gain value.
- If both pass: `terminalPidbyName("smplayer")`, `snprintf(...,"smplayer %s &", s2)`, `system(...)`, then short socket OK response. This handler does not calculate MaxPromptVolume-based gain or synthesize an extra gain parameter. Caller supplies arguments including any numeric suffix, while smplayer's argv[2] adjusts Q16 PCM amplitude as previously decoded.
- `ps @ 0x0041baec` returns `mp3`, backed by raw hex `6d 70 33 00`. Adjacent literal `linkplay_bonjour` is unrelated.
- Not all HTTP playPromptUrl strings necessarily reach smplayer (two guards); don't generalize from hardware success with one mp3 URL.
- `axt @ obj.g_wiimu_shm` not sufficient to find all readers of offset 0x3C8; next step is targeted static references to the specific field and writers, plus cross-checking downstream codec gain.

**Original objective STILL OPEN:** software PCM Prompt gain is master-zone-dependent in prior live tests, not demonstrated fixed acoustic level. Do not change baseline airALARM v0.1.26 or any device gain/NVRAM.


## PROMPT_GATE bundle 2026-10-20 05:12 — no writer identified yet

User uploaded `A31_PROMPT_GATE_20261020_051234.zip`; archive contains `rootApp.txt` (75,461 bytes), `mv_ioguard.txt` (37,330 bytes), their radare2 scripts and stderr. Source hashes match prior validated extracts. **Static code evidence only**.

- The rootApp `playPromptUrl` branch at `0x0040fc20–0x0040fc30` **reconfirms** load from `g_wiimu_shm + 0x3C8` (`lw v0,0x3c8(v0)`) and signed `slti v0,v0,0x28` (value <40). It also reconfirms the `strstr(s2,"mp3")` gate and `snprintf("smplayer %s &", s2)` call. This repeats already verified facts, not a new semantic interpretation.
- The report dumps `ReadGeneralConfig`, `MCUContextInit`, `StartupMusic` and sections of `mv_ioguard`. In these dumps there is **no established writer of offset 0x3C8** and no evidence tying it to master volume, Prompt gain or a timing parameter. The report is not an exhaustive scan, so writer absence in shown samples is **not proof that no writer exists**.
- Earlier interpretation of `SHM+0x3BC` as zone volume and `SHM+0x3D8` as MaxPromptVolume is preserved; do not conflate those fields with unknown `0x3C8`.
- Next static scan `a31_shm_field_scan.sh` (Bash syntax checked, **not run on operator's original binaries**) searches executable MIPS32 ELF segments in rootApp/mv_ioguard/a01controller/wmrmplayer for load/store opcodes using immediates 0x3BC/0x3C8/0x3D0/0x3D8 and emits contextual radare2 dumps, matches CSV and ZIP in `/Users/lab/AI/airALARM`. It excludes SP-relative references; false positives in unrelated structs remain possible. This will help locate actual writes but cannot automatically establish which base pointers are g_wiimu_shm. No device connection or firmware write.
- Fixed acoustic alarm volume independent of zone master remains UNSOLVED.


## SHM field scan: M_MODE discovery (2026-10-20 16:05)
User uploaded `A31_SHM_FIELD_SCAN_20261020_160549.zip`. Read-only MIPS32 executable ELF scan of `rootApp`, `mv_ioguard`, `a01controller`, `wmrmplayer` found 114 immediate-displacement load/store matches in four fields. Distribution: rootApp 28, mv_ioguard 12, a01controller 70, wmrmplayer 4. These are **instruction matches, not 114 proven references to shared memory**; base-pointer verification is essential, especially in a01controller.

**MAJOR STATIC FINDING: field 0x3C8 is M_MODE (player operating mode), not zone volume.**
- `a01controller.sym.Get_M_MODE` at 0x0041a170 returns `lh v0,0x3c8(v0)` at 0x0041a188, with base loaded from `g_wiimu_shm` at 0x0041a17c–0x0041a180. This reads the low signed 16 bits of M_MODE.
- `a01controller.sym.Set_M_MODE` at 0x0041a18c takes an integer mode argument, and near 0x0041a4a8–0x0041a4bc it loads `g_wiimu_shm` and writes `sw s0,0x3c8(v0)` in the delay slot of `process_unlock` call. The stored value is the function's incoming mode (`s0 = a0` at 0x0041a1b8). Subsequent read of the same word at 0x0041a4d0. Thus this is an explicit writer. Another candidate `a01controller.CNodeMan_Init` writer at 0x0041fe4c needs register ancestry verification.
- `rootApp.GoaheadCmdParsethread` at 0x0040fc28 `lw 0x3c8` and at 0x0040fc2c signed `slti 0x28` means `playPromptUrl` is gated on **operating mode value <40**, not the main-zone volume. The earlier condition for `strstr("mp3")` still applies.
- `rootApp` has another field read `0x0040b2f8` during status/config report string formatting, potentially enabling the textual name of 0x3C8 by examining adjacent rodata format string in a focused batch.
- `rootApp SHM+0x3BC` remains zone-volume field, and `SHM+0x3D8` remains MaxPromptVolume. No reason to conflate these with M_MODE.
- Scan detects unrelated matching offsets in large binary as possible false positives, and scanner explicitly excludes SP-relative operations; therefore completeness is not guaranteed.

**Next targeted offline batch:** created `a31_m_mode_batch.sh` with `radare2` disassembly of full `Get_M_MODE`, `Set_M_MODE`, their xrefs, `CNodeMan_Init` and rootApp guard/status code. `bash -n` syntax checked; **not executed against original user's binaries**. Inputs are original Rakoit extracted firmware at `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`, outputs ZIP under `/Users/lab/AI/airALARM`. User can run `bash a31_m_mode_batch.sh`. This script is read-only and makes no network/device calls.

**Research goal still unsolved:** independent fixed acoustic alert loudness under variable master zone volume. Preserve airALARM v0.1.26.


## Offline M_MODE deep batch 2026-10-20 16:17

Source: operator uploaded `A31_M_MODE_20261020_161720.zip`; extracted original `a01controller.txt` (~56 KB), `rootApp.txt`, `mv_ioguard.txt`, manifests/radare2 scripts. This is STATIC ELF evidence, not a hardware M_MODE test.

- `a01controller.Get_M_MODE` at 0x0041a170 reads signed **16-bit** `lh v0,0x3c8(v0)` from `g_wiimu_shm` at 0x0041a188. `Set_M_MODE` at 0x0041a18c stores incoming mode (`s0=a0` at 0x0041a1b8) as full 32-bit `sw s0,0x3c8(v0)` at 0x0041a4bc, in MIPS delay slot of `process_unlock`.
- `CNodeMan_Init` initializes same shared-memory mode to signed **-1** at 0x0041fe4c: `sw v1,0x3c8(v0)` where v1=-1, g_wiimu_shm pointer loaded 0x0041fe1c–0x0041fe28. This confirms the previously suspected initialization write.
- `Set_M_MODE` first calls `AudioCaptureBypassLoad`. At 0x0041a1c8–0x0041a210 it computes `mode-40` and tests `(unsigned)(mode-40)<20`, i.e. **mode in 40..59 inclusive**; then conditionally starts audio capture when entering that range and stops it otherwise based on `IsAudioCaptureStart`. Exact individual mode enum labels remain unknown.
- Its further logic examines g_wiimu_shm+0x3dc and other conditions, dispatches socket messages, runs `process_lock/process_unlock`, updates SHM+0xfa0 to -1, and stores M_MODE. Also uses comparisons to 0, 1, and 99 in later branch; do not infer their public enum labels from these tests alone.
- Callers of `Set_M_MODE` include `CStandaloneNode_SwitchModeToStorage`, `CStandaloneNode_SwitchDAC`, `CStandaloneNode_SwitchSourceMode`, `CStandaloneNode_parse_avs_play`, `CStandaloneNode_parseCmd_rmc`, `ParseRenderCmd`, `evtSocket_thread`, `show_song_info_from_Udisk`; Get_M_MODE is used widely in playback/status paths.
- `rootApp.GoaheadCmdParsethread` HTTP `playPromptUrl` still tests **signed M_MODE < 40** at 0x0040fc28–0x0040fc30. IMPORTANT subtlety: initialization value -1 is **less than 40**, so `M_MODE<40` alone is not proof of an actively playing supported mode or specific source. HTTP branch additionally requires 'mp3' substring. This is a gating rule, NOT an independent alert-volume solution.
- `rootApp` also reads same field for status text at 0x0040b2f8; no enum mapping recovered from this report.
- No gain changes, device SSH commands, or changes to working airALARM v0.1.26 were performed.

**Open problem:** fixed acoustic Prompt loudness regardless of master-volume setting remains unsolved; next highest-value research should avoid overfocus on M_MODE enum and instead trace URL Prompt relative to downstream master gain / codec state or seek noninvasive recordings at different zone levels.
