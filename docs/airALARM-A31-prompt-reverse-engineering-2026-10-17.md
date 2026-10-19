# A31 Rakoit Prompt RE — airALARM findings (2026-10-17)

Evidence: **hardware tests** (explicitly labeled) + **static binary inspection** of original MIPS firmware. Do not treat binary inferences as acoustic proof.

## Purpose / baseline
Seek independent fixed audible alert MP3 volume while leaving radio/master zone volume unchanged. Preserve working airALARM v0.1.26; no NVRAM edits.
Hardware A31: firmware Rakoit 4.6.415156, test 192.168.0.35, MP3 served by ESP32 at http://192.168.0.42:8082/audio/a31_alert.mp3.
**Hardware confirmed:** URL API command playPromptUrl:http://192.168.0.42:8082/audio/a31_alert.mp3%2010 returns HTTP 200 OK, audible quieter MP3, resumes radio after; suffix 50 louder and 100 louder. **Master volume still affects absolute prompt loudness.** The complete 11-test matrix for master volume 80 and 50 is in [verified commands](./airALARM-verified-commands-2026-10-10.md).
Device export: MaxPromptVolume='50', Prompt='1'. Direct guessed commands for MaxPromptVolume/volumeprompt/voice_volume_prompt/mcu_volume_prompt/volume_prompt_url did not change setting; guessed setPlayerCmd variants reporting OK do not prove execution (even nonsense reports OK).

## Firmware files on operator Mac
- /Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/bin/rootApp (stripped MIPS32 rel2 ELF)
- /Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/bin/volumeprompt
- /Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/bin/smplayer
- /Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/lib/libmvmsg.so (exports volume_pormpt_direct; typo in exported name retained)
Tools: /opt/homebrew/bin/radare2; radare2 -q -e bin.relocs.apply=true -c 'aa; ...; q' FILE.

## rootApp MaxPromptVolume
rodata MaxPromptVolume at VA 0x0041c298; MaxPromptVolume= at VA 0x0041ccdc.
ReadGeneralConfig: WMUtil_Get_NVRAM -> fallback WMUtil_Get_GenConfig -> atoi -> shared memory g_wiimu_shm dereferenced structure offset 0x3D8, write instruction 0x0040782c.
offset 0x3D8 writes: 0x00403b4c, 0x0040782c; reads: 0x00403194 (StartupMusic), 0x004059f4 (MCUContextInit), 0x0040b480 (snprintf configuration export).
MCUContextInit nonzero 0x3D8 branch executes snprintf + WMUtil_Set_NVRAM (0x004054f4 through 0x0040551c); this alone is NOT sound output control.

## rootApp shared field 0x3BC
writes 0x00404848, 0x00405dbc, 0x00408208; reads 0x004031a0, 0x004059d8, 0x00405b54, 0x00405dac, 0x0040683c, 0x00415010, 0x0041597c. Matches on 0x3bc(sp) at 0x0040a878 and 0x0040adc4 are stack slots, NOT same shared-memory field.
0x00408208: loaded from NVRAM or general config via atoi. PostOldCompatible 0x00405da4–0x00405dbc sets field to 0x50 (decimal 80) if zero. 0x00404848: another config parse and NVRAM-save path.
Earlier interpretation labeled 0x3BC as startup_vol; **specific string-to-instruction mapping should be verified before marking that key name confirmed**. Certainly not yet proven to be current live radio volume.

## StartupMusic uses both fields
At 0x00403194 loads 0x3D8; at 0x004031a0 loads 0x3BC; conditional slt and branches. Calculates intermediary (MaxPromptVolume*100)/field_0x3BC at 0x004031b4–0x004031c0, but further xori 100 and movz processing at 0x004031c4–0x004031cc means raw ratio is not universally the final audio argument.
At 0x00403270 passes s1 as third argument a2; a1=1 at 0x00403288; calls imported volume_pormpt_direct through 0x00403284/0x0040328c.

## libmvmsg.so volume_pormpt_direct
Found by nm -D of .so files. radare2 function sym.volume_pormpt_direct at 0x00005cdc, 644 bytes. MIPS argument handling: a0 audio-path pointer -> s0 (0x5d08), a1 mode -> s2 (0x5d0c), a2 numeric -> s3 (0x5d14). Checks path existence and fallbacks with snprintf, access(...,R_OK); conditional on s3 > 0 and s2 selects command templates near 0x5e84–0x5eec. Executes system(command) at 0x5f34–0x5f3c.
**RODATA strings confirmed by radare2 psz:**
    smplayer %s %d %s
    smplayer %s %s
    %s
    /vendor/misc/Voice-prompt/%s
    /system/workdir/misc/Voice-prompt/%s
    /system/workdir/misc/Voice-simple/%s
Therefore this helper invokes external smplayer, like URL playPromptUrl path. No evidence yet of independent hardware mixer or acoustic loudness decoupled from zone master volume. Exact argv semantics and difference of templates not yet established.

## Outstanding tasks
Inspect smplayer static strings for volume/mixer/alsa/gain/softvol, then argc/argv parsing and actual audio/mixing backend. User provided command but **has not supplied output yet**:
    BIN="/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/bin/smplayer"
    radare2 -q -e bin.relocs.apply=true -c 'aa; izz~volume; izz~mixer; izz~alsa; izz~gain; izz~softvol; q' "$BIN"
Investigate role of terminalPidbyName; verify mapping startup_vol to offset 0x3BC. No tests on hardware or modifications implied.

## Evidence classifications
Hardware VERIFIED: prompt URL + numeric suffix affects perceived sound; auto resume radio; sound still master-volume-dependent.
Static binary VERIFIED: stated strings, functions, shared-memory offsets, branching, command-line construction.
HYPOTHESES: smplayer parameter maps to gain; startup_vol name for offset 0x3BC pending direct reference confirmation; constant independent acoustic alert loudness remains UNSOLVED.

## Update: smplayer string inspection (2026-10-17)
Operator executed read-only radare2 `aa; izz~volume; izz~mixer; izz~alsa; izz~gain; izz~softvol` against original `/system/workdir/bin/smplayer`.
Strings found:
- `.dynstr` `self_dither_volume` at 0x004013fb, `other_dither_volume` at 0x004018ff — imported/dynamic symbol strings; no proof they control output amplitude.
- `.rodata` `GNOTIFY=volume_prompt_end` at 0x00408b84, `GNOTIFY=volume_prompt_start` at 0x00408c6c — evidence of start/end notification strings, but dispatch semantics and causal relation to radio restoration not yet proven.
- No strings matching mixer/alsa/gain/softvol in this exact `izz` search; absence does not rule out binary volume handling.
**Next:** inspect xrefs to two GNOTIFY strings and main/entrypoint argument parsing. Pending smplayer output backend; fixed acoustic loudness remains UNSOLVED.


## Update: smplayer GNOTIFY xrefs and main (2026-10-17)
Operator ran `radare2 -q -e bin.relocs.apply=true -c 'aaa; axt @ 0x00408b84; axt @ 0x00408c6c; afl~main; q' smplayer`.
- `main` identified at **0x00402760**, size **904 bytes** (25 basic blocks).
- **0x00402a00** in `main`: reference to string `GNOTIFY=volume_prompt_start` (rodata **0x00408c6c**).
- **0x00402aa0** in `main`: reference to string `GNOTIFY=volume_prompt_end` (rodata **0x00408b84**).
- Confirmed: both notification literals are referenced directly in smplayer's main; the destination mechanism and any link to radio pause/resume are **not established** until inspecting surrounding calls. Inspect `pd 24 @ 0x004029d0` and `pd 24 @ 0x00402a70`; examine argv parsing within main separately.


## Update: confirmed smplayer start/end notification transport (2026-10-17)
New read-only disassembly of original smplayer main at 0x004029d0 and 0x00402a70:
- At 0x004029f8, imported `SocketClientReadWriteMsg`; `0x00402a00` supplies second argument `GNOTIFY=volume_prompt_start`, `0x00402a08` invokes the function. First argument is a separate string (address from GP base); socket endpoint is **not yet decoded**.
- At `0x00402a14–0x00402a2c`, `CAudioProcessor.instance__` and start setup. Actual `start_char__int_` invocation lies just beyond this first snippet; inspect a wider slice before documenting its exact call location or args.
- At `0x00402a70–0x00402a84`, `CAudioProcessor.instance__` then `CAudioProcessor.waitFinish__`.
- At `0x00402a98`, imported `SocketClientReadWriteMsg`; `0x00402aa0` supplies `GNOTIFY=volume_prompt_end`, `0x00402aa8` invokes it.
- This establishes sequential socket notifications around audio processing/wait; **which receiver**, whether notification triggers radio pause/resume, and exact audio gain handling remain unverified. Correlation with hardware-resumed radio is not a proven causal link.

Next static inspection: `pd 48 @ 0x00402760` (argc/argv handling at start of main) and `pd 32 @ 0x00402a10` (audio start/wait flow). Do not change hardware or firmware v0.1.26.


## Update: smplayer argv and CAudioProcessor.start (2026-10-17)
User's read-only disassembly `pd 48 @ 0x00402760; pd 32 @ 0x00402a10`:
- smplayer `main` at 0x00402760 retains `argv` in `s1` (0x00402798), `argc` in `s3` (0x0040279c), and loads `argv[1]` into `s0` (0x004027a4, delay slot of WiimuContextGet).
- `0x004027ac` passes `argv[1]` as path to `stat`, and `0x004027c8` saves it as `file_name`; no argument-null/argc validation is proven by this fragment.
- At `0x00402a14–0x00402a34` calls `CAudioProcessor.instance__` and `CAudioProcessor.start_char__int_`, passing `a1=s0` (path) and `a2=s4` (integer). **Where s4 comes from is still unknown**; do not yet claim it equals CLI gain or an independent channel setting.
- `0x00402a38` branches on nonzero return to `waitFinish` path; zero return enters log/error path at `0x00402a40–0x00402a64` and returns without the normal wait/completion notification (requires wider control-flow audit).
- At `0x00402a70–0x00402a84` calls `CAudioProcessor.waitFinish` after accepted `start`.
Next: inspect main middle `pd 100 @ 0x00402800` to find s4 assignment/argv parsing, then `pdf @ method.CAudioProcessor.start_char__int_` to identify integer semantics. The device and airALARM v0.1.26 remain untouched.


## Update: smplayer CLI integer processing and lookup table (2026-10-20)
Static disassembly supplied by operator for `main` range `0x00402800–0x0040298c`. **Confirmed code behavior**:
- `0x004028b4`: branch on `argc < 3`, delay slot initializes `s4=0`. For argc >= 3, `0x004028c0–0x004028c4` does `atoi(argv[2])`.
- `0x004028c8–0x004028ec`: computes `index = 100 - atoi(argv[2])`, uses four-byte table entry `table[index]`, stores entry into global `self_dither_volume`. Table base from PIC gp pointer offset `-0x7350`; numeric content/units and bounds unknown.
- At argc==3 `0x004028f4` branches to `0x00402ae0` (not inspected yet). **Do not assume** this branch always enters the same audio playback path as argc>=4.
- For argc>=4 `0x004028fc–0x00402908`: `atoi(argv[3])` then `s4 = (atoi(argv[3]) == 1) ? 1 : 0`. `s4` reaches `CAudioProcessor.start_char__int_` as its integer argument at `0x00402a34`.
- For argc>=5 `0x00402918–0x0040293c`: computes `100 - atoi(argv[4])`, uses same coefficient table and stores result in `other_dither_volume`. Subsequent checks test argc==5.
- The existing hardware-tested `playPromptUrl:URL%20N` takes an apparent two-token CLI form, but the exact rootApp shell string, argv handling and `argc==3` special branch still need comparison before mapping every case.
- Strong indication numerical CLI args select software gain/dither lookup coefficients. **Not yet proof** of absolute independence from master/zone volume, table units, mixer interaction, or valid range checks. In this visible code, table index is not explicitly clamped; **do not test out-of-range values**.

Next priority: `pd 45 @ 0x00402ad0` for special argc==3 path, `pdf @ method.CAudioProcessor.start_char__int_`, and xrefs to `obj.self_dither_volume` and `obj.other_dither_volume` to find application to PCM signal. Preserve airALARM v0.1.26.


## Update: argc==3 and CAudioProcessor.start (2026-10-20)
Source: user's radare2 output `pd 24 @ 0x00402ad0; pdf @ method.CAudioProcessor.start_char__int_` on original smplayer.
- `0x00402ae0: b 0x402980` with delay slot `0x00402ae4: move s4, zero`. When `argc==3` (two tokens after executable: audio file + numeric arg), main explicitly resets s4 to zero before common processing. **The argv[2]-derived self_dither_volume lookup/write already occurred** earlier (0x004028bc–0x004028ec).
- C++ method `CAudioProcessor::start(char*,int)` at **0x004030b4**, disassembly 320 bytes; stores `a2` (integer passed by main from s4) to instance **offset 0xE8** at `0x004030f8`, stores duplicated file path pointer into offset 0xE4 at 0x004030fc. Thus `s4` is a separate start *mode/flag* field, **not identical to argv[2]-derived gain table coefficient**.
- At `0x00403100`, calls `CAudioProcessor.ParseFileType`; at `0x0040315c`, calls `pthread_create` with `CAudioProcessor.decodeThread(void*)` at **0x00404718**. Then waits briefly on a condition variable and returns 1. Audio output logic is in decodeThread or functions it invokes, rather than shown in start itself.
- Caution: lack of observed CLI input range validation around table indexing; only inspect files and use prior hardware-tested values 10..100 if necessary. Independent absolute Prompt loudness still UNSOLVED.
- Next: batch static analysis of smplayer main, decodeThread and global gain xrefs, libmvmsg command builder, rootApp settings/call sites.

## Batch automation of static research — 2026-10-20
The accompanying downloadable helper `a31_re_batch.sh` was created and syntax-checked; tested its orchestration against mock radare2 and mock ELF paths (NOT yet executed against real extracted firmware in this chat). Usage on operator Mac: `bash ~/Downloads/a31_re_batch.sh`. Optional positional args: `[RAKOIT_EXTRACTED_DIR] [OUTPUT_DIR]`. Defaults to `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED` and a timestamped directory inside `~/AI/A31_Firmware/A31_RE_REPORTS/`.
It runs **read-only** radare2 batches against `smplayer`, `libmvmsg.so`, `rootApp`, collecting main argument parsing, `CAudioProcessor.start`, first 160 instructions of decodeThread, `self_dither_volume`/`other_dither_volume` xrefs, original volume_pormpt_direct, MaxPromptVolume and shared-memory accesses. Produces `smplayer.txt`, `libmvmsg.txt`, `rootApp.txt`, `manifest.txt`, `README.md`, reproducible `r2_commands/*.r2` and a `.zip` ready for review. It performs no device-side experiments, HTTP calls, firmware flash or NVRAM writes.
Remaining research: trace coefficient table into PCM/audio backend; check if master output volume is multiplied afterward. Preserve airALARM v0.1.26.

## Batch report received 2026-10-20 00:33 local
User executed script successfully on Mac; uploaded `A31_RE_BATCH_20261020_003338.zip`; all three r2 jobs completed: smplayer 742 lines, libmvmsg 193 lines, rootApp 347 lines. Static-only; A31 and v0.1.26 untouched. Original SHA256 manifest:
- smplayer: `baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac`
- libmvmsg.so: `59e57f72f35a4ccb9a6bd5b0011ae34fcbd8343c03a8a672c670ac5e805828e3`
- rootApp: `0314cbeb5961127bef4668317183f66e7b8cec7eeb1f323445c622dd20992a97`
**New static evidence from cross-references:**
- `self_dither_volume`: assigned in `main` at `0x004028ec`; independently **read** in `fcn.00402c80` at `0x00402c8c` / `0x00402c94`.
- `other_dither_volume`: assigned in `main` at `0x0040293c`; **read and written** by `CAudioProcessor.setAudioParams(int,unsigned int,unsigned short)` at `0x00403bfc` and `0x00403c08` respectively. Further disassembly required to explain use/overwrite.
- `CAudioProcessor.decodeThread(void*)` at `0x00404718` calls `CAudioProcessor.decode_audio()` at `0x00404740`, which is the next relevant playback processing path. Audio frame function present as `CAudioProcessor.playAudioFrame(mad_pcm*)` at `0x00403cf8`. The present batch did NOT yet dump complete `decode_audio` / `playAudioFrame` / `fcn.00402c80`.
- **Do not infer** gain independence from shared/master volume from presence of self/other dither coefficients.

## Output location requirement (user, 2026-10-20)
All next airALARM/A31 research report archives and report directories default under `/Users/lab/AI/airALARM` rather than `/Users/lab/AI/A31_Firmware/A31_RE_REPORTS`. An updated `a31_re_batch.sh` sets `OUT="${2:-$HOME/AI/airALARM/A31_RE_BATCH_$STAMP}"`, while the source binaries continue to be read from `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`. The script syntax was checked with `bash -n`. It also includes extra dumps for `fcn.00402c80`, `CAudioProcessor.setAudioParams`, `scale`, `playAudioFrame` and `decode_audio`. Operator must replace local script before next run.

## Batch analysis #2: A31_RE_BATCH_20261020_011946.zip (2026-10-20)
Operator successfully ran the updated read-only script on Mac. Reports generated in user-requested directory `/Users/lab/AI/airALARM/A31_RE_BATCH_20261020_011946`, ZIP `/Users/lab/AI/airALARM/A31_RE_BATCH_20261020_011946.zip`. Uploaded and inspected: `smplayer.txt` 1478 lines, `libmvmsg.txt` 193, `rootApp.txt` 347; original binary SHA256 unchanged vs prior batch. This is **static reverse engineering**, not a new live-device test.

### Definitive digital gain processing path in smplayer
- `main`: parse `atoi(argv[2])`, calculate 0..100-derived lookup `table[100 - value]` (0x004028c0–0x004028e4), write coefficient to `self_dither_volume` (0x004028ec). No verified bounds checking immediately before table indexing; **never issue out-of-range values**.
- `fcn.00402c80` at 0x00402c80: loads `self_dither_volume` at 0x00402c8c/0x00402c94, multiplies incoming sample by it (`mul` at **0x00402c98**), applies a conditional low-coefficient dither/noise-shaping branch if coefficient less than `0x10000` (0x00402c9c–0x00402cd8), then arithmetic shift by **16 bits** (0x00402ce0). This resembles Q16 fixed-point amplitude scaling; exact table values, dB curve and dynamic range remain unmeasured.
- `CAudioProcessor.playAudioFrame(mad_pcm*)` at 0x00403cf8: calls `CAudioProcessor.scale(int)` on libmad samples (0x00403e68), then calls `fcn.00402c80` **0x00403e84** and stores resulting 16-bit PCM (0x00403e90); channel-specific equivalent calls around 0x00403ee4. Calls `snd_pcm_writei` at **0x00403db0** to write PCM to ALSA.
- `CAudioProcessor.decode_audio()` at **0x004044cc** opens ALSA PCM **`default`** via `snd_pcm_open` (0x004045a4–0x004045b8), initializes libmad and calls `playAudioFrame` at 0x00404640 or 0x004046a4. Thread wrapper `decodeThread` calls `decode_audio`.
- Thus numeric suffix influences digital PCM amplitude **before ALSA**. Actual analog acoustic output can still be affected by master/zone gain downstream; this report does **not** show a master-independent path.

### Additional ALSA mixing path requiring research
- `CAudioProcessor.setAudioParams` at **0x004038fc** configures ALSA hw/sw params. At 0x00403960–0x00403974 it may open PCM `default`; at 0x00403bfc loads **address** of `other_dither_volume`, at **0x00403c08** sets its value to `0x2000` (8192). This is a **write**, not evidence its prior value is used in that function. An earlier quick summary described it as 'read'; corrected here.
- At **0x00403c10**, calls imported nonstandard/extended `snd_pcm_mix_vol` with `a0=pcm_handle`, `a1=1`, `a2=0x2000` (8192), `a3=0x10000` (65536). Exact semantics of this custom API are currently unknown; do not assert it provides independent analog/hardware gain.
- There is also `set_pcm_stream_info` call at 0x00403c24, and `switch_mode_get_silence` around 0x00403c7c. These may interact with prompt vs main stream mixing; no causal proof yet.

### Further offline batch: script provided
New targeted `a31_gain_deep_batch.sh` (syntax checked with `bash -n`; **not run on operator firmware yet**) creates outputs under `/Users/lab/AI/airALARM`, dumps table (101 4-byte entries from VA `0x00408cb0` inferred from root table base at 0x004028dc), attempts to export coefficients to CSV, dumps PCM/silence routines, and searches libs for `snd_pcm_mix_vol` provider. Command on operator Mac after downloading into project directory: `cd /Users/lab/AI/airALARM && bash a31_gain_deep_batch.sh`.
Need verify table address/format and ALSA exported provider from new batch; tool output is authoritative. No device interactions or firmware changes; working airALARM v0.1.26 remains baseline.
