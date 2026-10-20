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


## Third batch: A31_GAIN_DEEP_20261020_012845.zip (2026-10-20)
User uploaded and we inspected original static analysis bundle. All binaries SHA256 matched prior runs; no hardware commands or firmware modifications. Bundle contains `smplayer.txt`, `libmvmsg.txt`, `rootApp.txt`, `dither_table_raw.json` (404 bytes), `dither_coefficients.csv` (101 rows), and provider search.

### VERIFIED: original 101-point smplayer lookup table
Source is smplayer `.rodata`, VA `0x00408cb0`, 101 little-endian uint32 entries; main indexes as `table[100 - atoi(argv[2])]` and stores result in `self_dither_volume`. Complete machine-extracted values separately preserved at **[a31-smplayer-dither-coefficients-2026-10-20.csv](data/a31-smplayer-dither-coefficients-2026-10-20.csv)**.
Observed values (CLI level -> coeff/65536, approximate digital attenuation relative to full scale):
| CLI | uint32 coefficient | PCM factor | theoretical 20log10(factor) |
| ---: | ---: | ---: | ---: |
| 0 | 368 | 0.005615 | -45.0 dB |
| 10 | 4608 | 0.070313 | -23.1 dB |
| 30 | 9216 | 0.140625 | -17.0 dB |
| 50 | 14336 | 0.218750 | -13.2 dB |
| 70 | 19456 | 0.296875 | -10.5 dB |
| 80 | 36864 | 0.562500 | -5.0 dB |
| 100 | 65536 | 1.000000 | 0.0 dB |
All 101 coefficients are unique and strictly increasing. The curve rises much faster above roughly 70. **This is calculated PCM amplitude gain**, not measured SPL, and does not establish independence from downstream master/zone gain. Even level=0 maps to nonzero 368; do not assume mute. No safe out-of-range argument bounds verified.

### VERIFIED: custom ALSA mixer provider
`alsa_provider_search.txt` confirms original `system/workdir/lib/libasound.so.2.0.0` exports **`snd_pcm_mix_vol` at 0x00041e70** (`nm -D`: `00041e70 T snd_pcm_mix_vol`). In smplayer `CAudioProcessor.setAudioParams`, 0x00403bf4–0x00403c14 sets global `other_dither_volume` to 8192 and calls `snd_pcm_mix_vol(pcm_handle, 1, 8192, 65536)`.
Important correction: at 0x00403bfc `other_dither_volume` **address** is loaded and then **overwritten** at 0x00403c08, not read for the mixer call. Its initial or argv-defined value therefore may be discarded at this point. Extended ALSA API function semantics unknown pending its implementation disassembly.
Original smplayer digital frame scaling remains confirmed: `self_dither_volume` multiplication in `fcn.00402c80` (0x00402c98), post-scaling shift 16; frame sends PCM to ALSA `snd_pcm_writei`.

### Next package
Prepared **a31_mixer_deep_batch.sh** (tested with `bash -n` and end-to-end mock command invocation; **not yet run against original libasound on Mac**): read-only r2 disassembly of `snd_pcm_mix_vol` in `libasound.so.2.0.0`, smplayer setAudioParams, forceclose/release, gain setup. Reports plus ZIP automatically under `/Users/lab/AI/airALARM`, source bins remain under `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`. Run from project directory using `bash a31_mixer_deep_batch.sh`; upload ZIP. Continue preserving v0.1.26.

**Status: constant acoustic alert volume across master-zone levels remains UNSOLVED.**

## Fourth batch: A31_MIXER_DEEP_20261020_013500.zip (2026-10-20)
Operator supplied ZIP; unpacked and examined `libasound.txt` (149484 bytes), `smplayer.txt` (46915 bytes), `alsa_symbols.txt`, manifests and radare2 command scripts. Original SHA256: `libasound.so.2.0.0 = 3bff4704868e35833092cd77b5b0192431aa4e5fdfcd341d535154e96f211dac`; `smplayer = baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac`. Static analysis only.

### IMPORTANT CORRECTION / refinement: `snd_pcm_mix_vol` is a dispatcher, not direct mixer gain arithmetic
At `libasound.so.2.0.0` VA `0x00041e70`, symbol size 156 bytes:
- `0x00041e8c–0x00041eb4`: assert PCM handle not null (`pcm.c` line 732 as reflected by assert immediate 0x2dc).
- `0x00041eb8`: load operations table from `pcm + 0xF4`; `0x00041ebc`: load callback pointer from `ops + 0x30`. If callback exists, `0x00041ee0` calls it indirectly, substituting the plugin/slave PCM handle as first argument (taken from `pcm + 0xFC`), while MIPS a1/a2/a3 still contain the passed arguments. If absent, descend to wrapped PCM at `pcm + 0x100`, look for its callback, and invoke if present. **Which PCM plugin/callback actually receives the call remains unknown.**
- After callback/skip, `0x00041ef4/0x00041ef8`: set flag value 1 at `pcm + 0x108` and wrapped PCM struct `*(pcm+0x100) + 0x108`; return zero. This wrapper performs **no explicit gain multiplication** itself.
- Therefore previous speculation that `snd_pcm_mix_vol(handle,1,8192,65536)` sets an independent output gain is **not supported by this wrapper**. It forwards parameters to a plugin callback; operational effect must be identified in plugin logic and live-device measurements.

### More clues from libasound and smplayer
- Symbols: `_snd_pcm_dmix_open` 0x0008140c, `snd_pcm_dmix_open` 0x00080bb4, `snd_pcm_dmix_writei` 0x0007f358.
- `.rodata` VA 0x000ae6a8 diagnostic text: `snd_pcm_dmix_writei alexa_flag = %d, pause_flag=%d, mute_flag=%d, mixer=%d, vol_min=%d, fixed_vol=%d\n`; suggests patched/extended DMIX mixing logic with flags, but the origin and actual use of each field is NOT YET ESTABLISHED.
- `smplayer` setAudioParams uses `snd_pcm_mix_vol(handle, 1, 8192, 65536)` at 0x00403c10; before this, overwrites global `other_dither_volume` with `0x2000` (8192) at 0x00403c08. Afterward calls `set_pcm_stream_info` at 0x00403c24.
- `smplayer` forceclose at 0x004032d8 and releaseProcessor at 0x00403648 invoke `snd_pcm_mix_vol` with a2=0,a3=0 before `snd_pcm_close`; full surrounding a1 and receiver callback have not been independently resolved.

### Next offline batch (created)
`a31_dmix_callback_batch.sh` was written and syntax-checked plus mock end-to-end smoke-tested (NOT on original Mac ELF). Defaults reports and zip under `/Users/lab/AI/airALARM`. Inspects `snd_pcm_dmix_writei`, `snd_pcm_dmix_open`, `_snd_pcm_dmix_open`, the mix notification string's xrefs and smplayer call sites. User should run `cd /Users/lab/AI/airALARM && bash a31_dmix_callback_batch.sh` after saving script there and upload ZIP.

**Status:** independent constant audible Prompt level across master-zone levels remains UNSOLVED. Preserve original A31 and working airALARM v0.1.26; do not modify NVRAM.


## Fifth offline bundle: A31_DMIX_CALLBACK_20261020_014011.zip (2026-10-20)
Original Mac batch report uploaded and inspected. Files: libasound.txt (88596 bytes), smplayer.txt (20297 bytes), stderr, manifest and radare2 command files. SHA256 of original libasound `3bff4704868e35833092cd77b5b0192431aa4e5fdfcd341d535154e96f211dac`; smplayer `baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac` (same as previous reports). Static analysis **only**; no A31 acoustic tests.

### CONFIRMED: DMIX samples and system pause/mute logic
- `snd_pcm_dmix_writei` VA `0x0007f358` (816 bytes): at `0x0007f368` accesses PCM private state; calls `snd_pause_flag_get` at `0x0007f3ac` and `snd_mute_flag_get` at `0x0007f3c8`; also uses `g_pause_local` and flags from private PCM data. Combines those values in branches around `0x0007f3f4–0x0007f468`.
- Branches near `0x0007f4f4–0x0007f5f0` load 16-bit samples (`lh`), call **`fcn.0007e70c`** at `0x0007f56c` and `0x0007f5dc`, and store transformed 16-bit samples back (`sh` at `0x0007f57c` and `0x0007f5ec`). This is **a second sample-processing stage inside patched libasound**, distinct from smplayer's self_dither_volume sample gain.
- Function eventually dispatches to `snd_pcm_mmap_writei` at `0x0007f680`. The exact mathematics of `fcn.0007e70c` and interpretation of the auxiliary mixer / min / fixed-volume values are **not yet recovered**.
- Diagnostics in the same function at `0x0007f62c` reference `snd_pcm_dmix_writei alexa_flag = %d, pause_flag=%d, mute_flag=%d, mixer=%d, vol_min=%d, fixed_vol=%d`. That proves those diagnostic labels are present, NOT the user-accessible ability to set fixed gain or route around master zone volume.
- `snd_pcm_dmix_open` VA `0x00080bb4` creates PCM and at `0x00080dcc–0x00080de4` installs the main PCM operations table at **VA 0x000c64a8** into PCM struct offset `0xF4` (via `0x00080dd4: sw v1,0xf4(v0)`). `snd_pcm_mix_vol` reads an operations table from `pcm+0xF4`, then its callback at `ops+0x30`. **Thus candidate callback slot for this DMIX operations table is VA 0x000c64d8**; its content has NOT yet been dumped, nor proven to be the receiver in the deployed `default` PCM chain. Flagging its location as static analysis target rather than claiming callback resolution.
- DMIX opener contains diagnostic text "dmix plugin can be only connected to hw plugin", showing its intended chained structure, but does **not** prove how A31's actual `default` PCM route is configured.

### Next focused static batch
`a31_dmix_trace_batch.sh` written; `bash -n` and mock end-to-end ZIP test passed; NOT run against original Rakoit binaries in this session. It dumps:
1. `pxw` operations table VA 0x000c64a8 and callback slot VA 0x000c64d8;
2. `fcn.0007e70c` disassembly and xrefs;
3. DMIX writer / helper calls and original smplayer ALSA caller.
Operator should save it in `/Users/lab/AI/airALARM` and run `bash a31_dmix_trace_batch.sh`; outputs ZIP in **that same project directory**. Do NOT change v0.1.26, NVRAM or A31 volume.

**Interpretation boundary:** confirmed second ALSA PCM sample-processing path; independent fixed audible Prompt volume remains UNSOLVED.


## Sixth offline bundle: A31_DMIX_TRACE_20261020_014854.zip (2026-10-20)
User supplied ZIP and its content was inspected. Files: `libasound.txt` (58,556 bytes), `smplayer.txt` (15,893 bytes), manifest and r2 command files. Original SHA256 unchanged from fifth bundle: libasound `3bff4704868e35833092cd77b5b0192431aa4e5fdfcd341d535154e96f211dac`, smplayer `baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac`. Read-only static analysis; not a new hardware test.

### Confirmed: DMIX ops callback slot resolves to 0x0007e880
- `snd_pcm_dmix_open` sets PCM `ops` pointer to VA `0x000c64a8` via instruction `0x00080dd4: sw v1,0xf4(v0)`.
- Read-only `pxw` reports at VA `0x000c64d8` (ops+0x30) the function pointer `0x0007e880`. Subsequent words at `0x000c64dc` and `0x000c64e0` are `0x0007fa30`, `0x0007ead8`.
- `snd_pcm_mix_vol` is an indirect dispatcher: `0x00041eb8` obtains `ops`, `0x00041ebc` reads `ops+0x30`, then `0x00041ee0` dispatches the callback, possibly using a wrapped PCM if the immediate one lacks the callback. Thus **0x0007e880 is the candidate concrete DMIX mix-volume callback**. Its disassembly has **not yet been captured**; do not claim its arithmetic or input parameter meaning until confirmed. Nor is actual A31 `default` PCM plugin chain yet established.

### Confirmed: additional Q16-style gain/dither stage
- `fcn.0007e70c` is 92 bytes, called twice from `snd_pcm_dmix_writei` at `0x0007f56c` and `0x0007f5dc`. It begins with `mul v0,a1,a0` (multiply sample and coefficient), compares coefficient to `0x10000`, and performs additional conditional low-gain sample correction / state update when it is below that value (`0x0007e724–0x0007e75c`). Function returns `sra v0,v0,16` at `0x0007e764` in delay slot of `jr ra`. Approximate idealized output `sample * coefficient / 65536`; integer overflow, signedness, bias/dither, and input clipping can make exact output differ.
- `snd_pcm_dmix_writei` reads 16-bit input samples (`lh`), calls this gain helper, and writes 16-bit samples (`sh` at `0x0007f57c`, `0x0007f5ec`). It also processes pause/mute flags. This confirms a second digital sample amplitude stage in patched ALSA code, following smplayer's own `self_dither_volume` handling. It does **not** prove hardware-independent acoustic volume.

### Next targeted static analysis bundle
Actual script `a31_dmix_ops_batch.sh` authored and verified with `bash -n` and mock end-to-end report ZIP run. After operator downloads to `/Users/lab/AI/airALARM`, runs `bash a31_dmix_ops_batch.sh`: dumps `0x0007e880` with `af/pdf`, adjacent callbacks `0x0007fa30` and `0x0007ead8`, xrefs, actual mix dispatch and smplayer callsites. Lists candidate ALSA config filenames from *extracted firmware only*. Defaults report + ZIP to `/Users/lab/AI/airALARM`; script does not connect to A31 or alter original binaries. **Not yet run on user's genuine libasound.**

Status: fixed acoustic Prompt volume independent of zone master output remains UNSOLVED. Preserve airALARM v0.1.26 and A31 NVRAM.


## Seventh offline bundle: A31_DMIX_OPS_20261020_015752.zip (2026-10-20)
Operator uploaded report bundle; inspected `libasound.txt`, `smplayer.txt`, `alsa_config_paths.txt` and recorded SHA256. libasound and smplayer checksums match earlier bundles; this is read-only static analysis, **not a live-device test**.

### CONFIRMED: concrete DMIX mix_vol callback setter at 0x0007e880
The 16-word table at libasound VA `0x000c64a8` contains function pointer `0x0007e880` at `+0x30` (`0x000c64d8`). Direct disassembly:
```asm
0x0007e880  lw v0, 0x104(a0)    ; PCM private context
0x0007e884  beqz a1, 0x7e8a0
0x0007e888  lw v0, 0xac(v0)     ; private mixer-state pointer (delay slot)
0x0007e88c  addiu v1, zero, 1
0x0007e890  sw v1, 0(v0)        ; state enabled
0x0007e894  sw a2, 8(v0)        ; numeric threshold/min (exact semantics beyond state use unproven)
0x0007e898  jr ra
0x0007e89c  sw a3, 0xc(v0)      ; numeric fixed/max (delay slot)
0x0007e8a0  sw zero, 0(v0)      ; disabled branch
0x0007e8a4  sw zero, 8(v0)
0x0007e8a8  sw zero, 0xc(v0)
0x0007e8ac  jr ra
```
Thus `snd_pcm_mix_vol` **dispatches to a configuration setter**, NOT an autonomous gain amplifier or master-volume override. The callback retains `(enabled, a2, a3)` in PCM private state. The setter contains no PCM multiplication and returns without calculated amplitude.
`smplayer` invokes `snd_pcm_mix_vol(pcm_handle,1,0x2000,0x10000)` during `CAudioProcessor.setAudioParams` (`0x00403bf4–0x00403c14`), and invokes `(pcm_handle,0,0,0)` at forceclose (`0x004032d0–0x004032dc`) and releaseProcessor (`0x00403640–0x00403648`). The flag is therefore enabled for playback and cleared on teardown.

### CONFIRMED: DMIX write actually reads configured mixer-state
`snd_pcm_dmix_writei` at `0x0007f358` obtains `private=*(pcm+0x104)`, then `s6=*(private+0xac)` at `0x0007f3a8`; this is the **same mixer-state pointer** set by callback. Reads `*(s6+0)` as flag at `0x0007f3f4`, `*(s6+8)` at `0x0007f488`, and `*(s6+0xc)` at `0x0007f498`, branching and updating gain intermediate before passing PCM samples through `fcn.0007e70c` (Q16 scaling). It also evaluates global pause/mute flags. Thus callback parameters participate in actual PCM gain/attenuation algorithm, but real acoustic dependence on downstream master zone volume **remains untested and unknown**.
More specific: the callback's a2=8192 and a3=65536 are used as configured numeric lower/upper boundaries by branches. The global PCM gain variable seen in radare2 GP-addressed code at around `0x0007f468–0x0007f560` appears to be further adjusted depending on flags. Precise state evolution needs analysis; *do not describe this as a fixed-volume override*.

### Firmware configuration candidates (filename verification only)
The report's `alsa_config_paths.txt` identifies:
- `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/lib/alsa/alsa.conf`
- `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED/system/workdir/lib/alsa/pcm/dmix.conf`
Their **contents were not included**; no proof yet that ALSA `default` on live A31 routes via this DMIX ops table. Next prioritize inspecting actual config, plugin routing and any remaining master volume stage before claiming fixed acoustic loudness.

### Next phase, strictly offline
Prepare a combined batch collecting config file contents, `snd_pcm_dmix_writei` complete control flow, `snd_pcm_dmix_open` callback install and `smplayer` playback/cleanup sites, plus search other volume-control components. Output reports + ZIP under `/Users/lab/AI/airALARM`. Do not modify firmware or NVRAM. **Open goal:** fixed perceived alert loudness independent of master zone volume.


### Batch tooling added after seventh bundle
Created **`a31_audio_route_batch.sh`** (bash syntax-checked, smoke-tested with a mock radare2 and test ALSA config fixture; **not yet executed on original extracted firmware**). It batches read-only `libasound` DMIX writer, Q16 helper, mixer callback, `snd_pcm_mix_vol` dispatch and `smplayer` audio setup; additionally copies exact ALSA config candidates `alsa.conf`, `dmix.conf`, `pcm.conf`, `asound.conf`, `default.conf`, `hw.conf`, `plug.conf`, `softvol.conf`, `.asoundrc` from **original extracted firmware only**. It records text matches to `default/dmix/hw/slave/softvol` to establish a possible PCM configuration route. ZIP & reports default under `/Users/lab/AI/airALARM`, source ELF files remain unchanged. Run from project directory: `bash a31_audio_route_batch.sh`; upload ZIP. This is not an alternative to verifying the live device's effective audio route.


## Eighth offline bundle: A31_AUDIO_ROUTE_20261020_020954.zip (2026-10-20)

User uploaded read-only batch ZIP. Contents include original extracted firmware ALSA configs `system/workdir/lib/alsa/alsa.conf`, `system/workdir/lib/alsa/pcm/default.conf`, and `system/workdir/lib/alsa/pcm/dmix.conf` together with radare2 disassembly. Original SHA256 still unchanged: libasound `3bff4704868e35833092cd77b5b0192431aa4e5fdfcd341d535154e96f211dac`, smplayer `baec063cdba06156ef399d0792ba76ab8009bfba9d38aadf1fdb9925a313f1ac`. The archive is STATIC evidence, not running-device verification.

### IMPORTANT: default PCM is NOT necessarily DMIX
- `smplayer`'s `CAudioProcessor.setAudioParams` calls `snd_pcm_open(..., "default", ...)` at VA `0x00403960–0x00403974`.
- Extracted `pcm/default.conf` defines `pcm.!default` as `type empty`, `slave.pcm` resolving `cards.<card-driver>.pcm.default:CARD=$CARD` if present, and **fallback** `type plug` with `slave.pcm { type hw; card $CARD }` if no card-specific definition is found. The fallback is **plug -> hw**, not explicit `dmix`.
- Separate `pcm/dmix.conf` defines `pcm.!dmix` as `type dmix`, `slave.pcm { type hw; card $CARD; device $DEV; subdevice $SUBDEV }`. Its mere presence proves the plugin is available but does NOT show `default` uses it.
- `alsa.conf` declares `pcm.default cards.pcm.default`, `pcm.dmix cards.pcm.dmix`; DMIX defaults include `48000` Hz and `S16_LE`, but neither is proof of the active Prompt stream. Its `@hooks` load **`/etc/asound.conf`** and **`/tmp/alsa/asoundrc`** (errors ignored), so device-time overrides can change the final route.
- The collected bundle does not contain these live override files or card-specific `cards/<driver>.conf` configurations; **effective live-device PCM chain unresolved**.
- Radare2 `smplayer.stderr.txt` contains an irrelevant failure to resolve requested `method.CAudioProcessor.decode_audio` name; already-supported direct `snd_pcm_open("default")` is visible. `libasound.stderr.txt` similarly contains a failed disassembly of unnamed `0x0007e880`; the callback is already resolved and disassembled in seventh bundle. Do not treat those missing command dumps as contradictory evidence.
- `snd_pcm_dmix_writei` 0x0007f358: retains earlier confirmed mix-state updates, pause/mute checks, and sample-scaling via `fcn.0007e70c`. Its implementation alone cannot establish that it is called in a deployed audio chain.

### Revised inference / next experiment
Until the runtime `default` PCM config and downstream master-volume location are known, the hypothesized DMIX route for Prompt and any independent gain benefit are **UNVERIFIED**. Prior findings about callback and PCM math remain valid **conditionally when this plugin is in the chain**.

A read-only collection script `a31_alsa_route_inventory.sh` was prepared and tested (`bash -n` plus end-to-end test with a synthetic extracted firmware tree). It searches under the extracted firmware only for card-specific `*.conf` ALSA definitions, other `asound.conf` files and audio route references in startup scripts, copying only relevant configs into ZIP under `/Users/lab/AI/airALARM`. Command: `cd /Users/lab/AI/airALARM && bash a31_alsa_route_inventory.sh`. This script DOES NOT connect to the A31 or modify original binaries or working airALARM v0.1.26. No claim yet that archived configs equal those deployed on running A31.

**Open goal:** fixed acoustic Alert/Prompt loudness regardless of master-zone volume is not demonstrated.


## Ninth offline bundle: A31_ALSA_ROUTE_20261020_022956.zip (2026-10-20)
User uploaded and inspected ZIP; contains 68 copied firmware ALSA configuration files, config inventory and search matches (89 eligible text files searched). **Static extracted firmware evidence only; not proof of live loading.** Critical new files `system/workdir/lib/alsa/asoundrc`, `dmixer.conf`, `dmixer_48k.conf`. Existing 8th-batch observation about generic `pcm/default.conf` fallback remains accurate but **the firmware contains a likely custom override that changes the expected default playback chain**.

### Confirmed file content: custom override defines default → dmix
`system/workdir/lib/alsa/asoundrc` (327 bytes; SHA256 `d7f13942de02113c5f7f88b2818c469d9e4346311958eabcd3b9980da1fefdaf`):
```
</tmp/alsa/dmixer.conf>

pcm.mv_audio { type hw; card 0; device 0 }
pcm_slave.mv_rate { pcm mv_audio; rate 44100 }
pcm.rate_convert { type rate; slave mv_rate }
pcm.asymed { type asym; playback.pcm "dmixer"; capture.pcm "hw:0,0" }
pcm.!default { type plug; slave.pcm "asymed" }
ctl.dmixer { type hw; card 0 }
```
The leading `<...>` line is an ALSA **configuration include** referencing absolute runtime path `/tmp/alsa/dmixer.conf`, not a shell redirection. `pcm.!default` would supersede the generic library default if this file is effectively loaded. Its playback path points via `plug`, `asym`, `dmixer` to PCM card 0 device 0. `rate_convert` and `mv_rate` exist but are not directly referenced by `pcm.!default` in this file; avoid falsely asserting they're in default playback chain.

`system/workdir/lib/alsa/dmixer.conf` (177 bytes; SHA256 `eab66e789146370c2fdf330f12dc87f7d26eeeca3b94bf0443227d2fed29b8ee`):
```
pcm.dmixer {
  type dmix
  ipc_key 1024
  slave { pcm "hw:0,0"; rate 44100; format S16_LE; period_size 2048; buffer_size 16384 }
  bindings { 0 0; 1 1 }
}
```
`system/workdir/lib/alsa/dmixer_48k.conf` (162 bytes; SHA256 `efc4f510a9540bd257137363f8976c63440df5a411f5fb418f3047ab3c04ab38`) defines same DMIX chain at **48000 Hz**. Which runtime file is active is unknown.

### Environment setup recovered from script matches
`system/workdir/evn.sh` (in search results but not copied into ninth archive) contains:
```sh
export ALSA_CONFIG_DIR=/tmp/alsa/
export ALSA_CONFIG_PATH=$ALSA_CONFIG_DIR/alsa.conf
```
Combined with `alsa.conf`'s `@hooks` loading `/tmp/alsa/asoundrc`, this provides a **plausible intended boot-time route**: create `/tmp/alsa` tree, install `alsa.conf`, `asoundrc` plus chosen `dmixer.conf`, export paths and start smplayer. However **the actual initialization/copy commands are not in this report**, and no evidence of live process environment or active ALSA PCM chain was collected. Do not promote intended config to hardware-confirmed route.

### Implications for independent alert loudness
The extended ALSA DMIX plugin likely has a mixer-state callback activated by `snd_pcm_mix_vol` during Prompt, and if this config is active, DMIX will process samples before `hw:0,0`. However a later volume control (e.g. codec mixer/master) could still reduce both prompt and radio. Independent **constant audible** alert loudness relative to zone master remains UNVERIFIED / UNSOLVED.

### Tenth offline batch prepared
Created `a31_alsa_boot_audit.sh` to inspect source firmware for startup/initialization shell/RC files and binary strings mentioning `ALSA_CONFIG_PATH`, `asoundrc`, `dmixer.conf`, `/tmp/alsa`, and audio setup. It also copies the key ALSA configs plus relevant scripts to a ZIP. The script was verified with `bash -n` and an end-to-end synthetic test that detected a test boot setup script. **It has not yet run against the user’s original firmware.** Defaults output to `/Users/lab/AI/airALARM/A31_ALSA_BOOT_<timestamp>.zip`; source extracted firmware at `/Users/lab/AI/A31_Firmware/RAKOIT_EXTRACTED`. Operator: `cd /Users/lab/AI/airALARM && bash a31_alsa_boot_audit.sh`. Read-only and does not contact live A31 or alter airALARM v0.1.26.


## Tenth offline bundle: A31_ALSA_BOOT_20261020_023634.zip (2026-10-20)
User supplied ZIP; verified original contents include `relevant_scripts/system/workdir/live.sh` (3383 bytes), `evn.sh` (950 bytes), `alsa.conf`, `asoundrc`, `dmixer.conf`, `dmixer_48k.conf` and script search reports; scan reports 7 matching scripts/80 binaries. Read-only STATIC firmware analysis only.

### SIGNIFICANT NEW CONFIRMATION: startup copies ALSA config to the exact runtime path
In `system/workdir/live.sh`, these excerpts appear in this order:

```sh
. /sbin/config.sh
. /sbin/global.sh
. ./evn.sh
...
cp /system/workdir/lib/alsa /tmp/ -fr
...
rootApp 2>&1 | lplogd 1024 /tmp/sys_app.log 1 &
```

In `system/workdir/evn.sh`, invoked before the copy/rootApp startup:

```sh
export ALSA_CONFIG_DIR=/tmp/alsa/
export ALSA_CONFIG_PATH=$ALSA_CONFIG_DIR/alsa.conf
```

The copied `alsa.conf` defines `@hooks` loading `/etc/asound.conf` and `/tmp/alsa/asoundrc` (`errors false`). The latter exists in firmware, has a leading config include `</tmp/alsa/dmixer.conf>`, and defines `pcm.!default` as `type plug; slave.pcm "asymed"`, `pcm.asymed` as playback `"dmixer"`, capture `"hw:0,0"`. `dmixer.conf` defines `pcm.dmixer` as `type dmix` on `hw:0,0`, `rate 44100`, `format S16_LE`. Hence the **intended startup playback chain** when `live.sh` executes and this config is not subsequently overridden:
`smplayer snd_pcm_open("default") → plug → asymed → dmixer (dmix) → hw:0,0`.

This closes the previously unresolved question of **how copied firmware ALSA configs reach the /tmp/alsa runtime path**. It strongly supports practical use of the earlier discovered dmix callback, beyond mere existence of an unused config. It is still not a capture of the effective running A31 chain: `/sbin/config.sh`, `/sbin/global.sh`, `/etc/asound.conf`, later overrides, process environment, and possible alternate boot paths are not verified. Do not call the actual running-device routing hardware-confirmed.

### Additional observation
`logs/binary_string_matches.txt` detected `snd_pcm_mix_vol` also in `system/workdir/bin/intercom`, in addition to previously analyzed `smplayer`. No evidence yet that intercom is relevant to Prompt or changes master-volume control.

### Interpretation boundary
The independently controlled digital sample gain and DMIX stateful mixer logic are now sufficiently understood as **static binary + intended boot configuration**. The original user goal—fixed acoustic alert volume across zone master levels—**remains UNSOLVED**. Next higher-value task: investigate where the **shared downstream master volume** is applied and/or inspect live ALSA config/process state read-only; do not modify volume, NVRAM, firmware or working airALARM v0.1.26.


## First live A31 SSH evidence: 2026-10-20 — active /tmp/alsa/asoundrc confirmed
**HARDWARE-VERIFIED ON A31** `192.168.0.35`, Rakoit `4.6.415156` (as operator identifies target): operator successfully logged in via SSH on TCP 24678 as `admin` (authorization worked; do not store credentials/secrets here). Shell banner: `BusyBox v1.12.1 () built-in shell (ash)`. Minimal environment: `whoami` and `tr` binaries unavailable, so commands relying on these failed. These failures are not evidence of ALSA or SSH malfunction.

Operator ran `cat /tmp/alsa/asoundrc` over the real SSH session. **Live file content**:
```conf
</tmp/alsa/dmixer.conf>

pcm.mv_audio {
  type hw
  card 0
  device 0
}
pcm_slave.mv_rate {
  pcm mv_audio
  rate 44100
}
pcm.rate_convert {
  type rate
  slave mv_rate
}
pcm.asymed {
  type asym
  playback.pcm "dmixer"
  capture.pcm "hw:0,0"
}
pcm.!default {
  type plug
  slave.pcm "asymed"
}
ctl.dmixer {
  type hw
  card 0
}
```

**Interpretation:** Live `/tmp/alsa/asoundrc` is present and agrees with the extracted firmware asoundrc. This **hardware-confirms the custom runtime config file**, and supports the *configured* default playback chain `default → plug → asymed → dmixer` (and, assuming the included dmixer.conf matches the extracted firmware, `dmixer → hw:0,0`). **Do not yet call it proven that the active smplayer process loads this config**; its process environment and effective PCM chain were not read, nor was live `/tmp/alsa/dmixer.conf` displayed yet. The prior on-disk `live.sh` copying ALSA configs aligns with the observed result.

**Next read-only BusyBox-compatible diagnostic** from the same SSH shell:
```sh
id
cat /tmp/alsa/dmixer.conf
cat /proc/asound/cards
cat /proc/asound/pcm
ps
echo "SSH_ALSA_CONFIG_PATH=$ALSA_CONFIG_PATH"
```
`echo $ALSA_CONFIG_PATH` only reveals this SSH shell's own environment; it does not prove rootApp/smplayer inherited identical variables. If files/commands absent, errors are expected and non-destructive. Avoid editing `/tmp/alsa`, master volume, NVRAM, or airALARM v0.1.26.

**Open goal remains** Prompt audible alert loudness independent from zone master volume; no proof yet of bypass or successful master-independent amplitude path.


## Live A31 SSH follow-up — PCM hardware and process inventory (2026-10-20)

**HARDWARE-VERIFIED on `192.168.0.35:24678`:** A31 BusyBox v1.12.1 shell successfully read both custom runtime ALSA config files:
- `/tmp/alsa/asoundrc` has the previously documented `pcm.!default {type plug; slave.pcm "asymed"}`, `pcm.asymed` playback `"dmixer"`, and includes `</tmp/alsa/dmixer.conf>`.
- `/tmp/alsa/dmixer.conf` content:
```conf
pcm.dmixer {
 type dmix
 ipc_key 1024
 slave {
  pcm "hw:0,0"
  rate 44100
  format S16_LE
  period_size 2048
  buffer_size 16384
 }
 bindings {
  0 0
  1 1
 }
}
```
- `cat /proc/asound/cards`: `0 [mtksnd]: noop - mtk_snd`; `mtk_snd (noop)`. **Caution:** driver label includes `noop`; do not assume native DAC/analog master mixer is directly represented by this PCM interface or physically downstream hardware mapping.
- `cat /proc/asound/pcm`: `00-00: mtk pcm noop-0 : : playback 1 : capture 1`.
- `ps` (user field `admin`) lists running `rootApp` PID 676, `volumeprompt` PID 773, `hdl` PID 678, `mv_ioguard` PID 711, `a01controller` PID 807, `wmrmplayer` PID 880, `intercom` PID 806, `dropbear` PID 672, plus supporting services. No standalone `smplayer` present in the *snapshot*; absence in one snapshot does not prove it is never executed (Prompt was not reported active).
- `id`, `whoami`, `tr` commands were `not found` in shell (BusyBox 1.12.1 limited applets/links). `echo "SSH_ALSA_CONFIG_PATH=$ALSA_CONFIG_PATH"` returned `SSH_ALSA_CONFIG_PATH=`, thus **interactive SSH shell** variable empty; this says nothing about `rootApp` / spawned `smplayer` environment (different launch ancestry).
- Confirms **on-device installed config** `default → plug → asymed → dmixer (dmix) → hw:0,0` for processes that load it. Still NOT demonstrated that `smplayer` actually inherits `ALSA_CONFIG_PATH` and uses this config, nor how the master-zone volume is implemented.
- Additional semantic caution: `mtk_snd (noop)` might front a vendor-specific audio path; investigate before claiming end-to-end physical PCM ownership or bypassing shared gain.

**Safe next read-only checks:** `busybox --list` to identify `tr`/other applets; `grep -E 'libasound|alsa' /proc/676/maps` and equivalent for `volumeprompt`/player processes; if `busybox tr` supported, *only show filtered ALSA_CONFIG_* process env values*, not entire `/proc/<pid>/environ` as it could contain secrets. No device write or master-volume adjustment.

The hardware-level independent acoustic alert-loudness requirement **remains UNSOLVED**. Keep airALARM v0.1.26 baseline, no NVRAM changes.

## Live SSH process file descriptors — wmrmplayer (2026-10-20)
**HARDWARE VERIFIED, read-only** from user-provided output on A31 `192.168.0.35` via SSH. `ls -l /proc/880/fd | grep '/dev/'` for `wmrmplayer` PID 880 shows:
```
lrwx------ 1 0 0 64 14 -> /dev/pcmC0D0p
lr-x------ 1 0 0 64 13 -> /dev/timer
lr-x------ 1 0 0 64 0 -> /dev/null
```
Interpretation: `wmrmplayer` has the ALSA playback PCM node `/dev/pcmC0D0p` open (FD 14); timer and null FDs also open. This is direct hardware/process evidence of a PCM playback handle, but **not proof that this process applies master-zone volume**, nor that it is the only process that opens the device, nor that all Prompt playback routes through it. PID is ephemeral and may change across reboots. User provided only PLAYER AUDIO DEVICES segment, not the other requested maps/FD results. For next step, ask for limited read-only observations of the ALSA-related maps and rootApp FDs, and current `ps`, without changing volume or NVRAM. The goal of fixed acoustic Prompt loudness independent of zone master remains UNSOLVED.
