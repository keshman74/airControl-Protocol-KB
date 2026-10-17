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
