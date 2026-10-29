# WiiM Room Correction native DSP call graph (static)\n\nStatus: **APK-VERIFIED / NOT-HW-VERIFIED**. Direct edges are resolved Ghidra call references; the dashed edge marks no resolved call from `spl_sweep` to `rta_method`.\n\n```mermaid\nflowchart TD
 subgraph SA["spl_sweep @ 0x13991c"]
  S["count gate; derive FFT/window/frequency grid"] --> C["calrir_new @ 0x127a0c"]
  C --> W["apply_ir_windows @ 0x129a50, alpha 0.25"]
  W -->|success| TF["tfplots_new @ 0x127e2c, windowed IR"]
  W -->|failure| TFR["tfplots_new @ 0x127e2c, raw IR fallback"]
  TF --> N["normalize all dB points to nearest 1 kHz"]
  TFR --> N
 end
 subgraph TA["time_align @ 0x148a2c"]
  A["WAV headers: same rate; recording 1x–3x"] --> B["bandpass and prompt/reference-end checks"]
  B --> P["mode filters + crosscorr_peak_noise_std @ 0x14a528"]
  P --> I["IR recovery / reconstruction checks"]
  I --> D["delay estimate; clamp [-250,+2500] ms"]
  B --> E2["prompt rejection: -2"]
  P --> E3["missing sweep: -3"]
  A --> E1["other invalid/error: -1"]
 end
 subgraph RT["Independent measured-test path"]
  M["measured_test_rta @ 0x1348e0"] --> R["rta_method @ 0x13392c"]
 end
 S -. "no resolved call edge" .-> R\n```\n\nSource report: [native DSP analysis](WIIM-HOME-ROOM-CORRECTION-DSP-STATIC-3.6.10-2026-10-29.md).