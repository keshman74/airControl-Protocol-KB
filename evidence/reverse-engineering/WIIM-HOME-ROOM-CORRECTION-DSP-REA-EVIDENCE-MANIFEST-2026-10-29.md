# REA Evidence manifest — WiiM Home native Room Correction DSP

**Status:** APK-VERIFIED / NOT-HW-VERIFIED.
**Artifact:** ARM64 ELF `libwiimundk.so`, SHA-256 `4e3159c5ed28490e7502692071da1e6bfeb1c2c592361492464f8fd74cd510ab`, BuildID `a68007e72b0db19a91b9a6b6761fa9c20647e427`.
**Tool:** REA MCP with Ghidra 12.1.4; image base `0x100000`.
**Full local REA bundle SHA-256:** `3b9d922591a45357de092887b2e340b78184587c74056eb700cc67d91235d2e5` (23,328,290 bytes; retained in local research folder and not duplicated into the repository).
**Canonical analysis:** [native DSP report](WIIM-HOME-ROOM-CORRECTION-DSP-STATIC-3.6.10-2026-10-29.md). Evidence IDs are exact REA record identifiers; all records share the target digest above. Data below is analysis evidence, not hardware proof.

| Evidence ID | Query | Address / subject |
|---|---|---|
| `ev_03f3a8e0a47f69e70d69a27d7b10f7ca61667106be77f41abdd1607234375ce3` | Function dossier | 0x149bf8 helper |
| `ev_08cf1baf4941e061eb14b43c32669860066d5b321cf6bd4e5a21137bc6cd7797` | Function dossier | 0x14d654 delay selector |
| `ev_219fc71ab495100d0d6fe1c7fc43fd734d0470f6ce0c7f41eb2c32720efda51e` | Function dossier | 0x129428 tukey_window |
| `ev_24fad8406618d68e0fe3000a812b141e91b406960d17da467a1e3842fa3de219` | Function dossier | 0x14cd24 low-pass helper |
| `ev_36a1acbbafcd1e03b483eb450f9005025ef5d2486cbb94a8715f969e856aaf5d` | Instruction listing | 0x13991c spl_sweep call setup |
| `ev_418502e59bca12e68feab056aa33c47b5dee5fb15b79e6eee3dfc95883e2512d` | Function dossier | 0x129944 half-window helper |
| `ev_4a2b09e9d0f5d3f1f183a125c9ae7fc92544ec59e5dc38a76b999896ea387e34` | Function dossier | 0x14a818 reference-end detection |
| `ev_5cdad1de588f90d106588e7a06e0444d2d07a1bf89edd88d036df19c5bbf4f4a` | Function dossier | 0x148a2c time_align |
| `ev_685ea6864011da16863f8e5c24db81fb41505200a323b830a7201164c6a9f456` | Function dossier | 0x14b260 Hilbert/envelope helper |
| `ev_6a0415b9ecaec57c6609c1701a850feca7241d74c0a766707610bd0a54a615ec` | Function dossier | 0x127a0c calrir_new |
| `ev_6a14f3141c25fae0c3283d35c3a9aff0239b304362dede65b5cb22edb8a632ab` | Function dossier | 0x14cc34 high-pass helper |
| `ev_925737ac5674e412afb23c3e601897e9a51f7327b5627bb34d968e3e2ccca083` | Function dossier | 0x14a528 cross-correlation peak/noise helper |
| `ev_989b5641357c48c5273b71d6c4fc1dcd5283967ca35185730b08ba6092545230` | Call graph | spl_sweep @ 0x13991c |
| `ev_a5bbafde556d5a5e76c512d563c533cc01157ded6d455f7221ded71b38744605` | Call graph | calrir_new @ 0x127a0c |
| `ev_ac81eda10a35068fe3e5aa034f7b0fab08a31db1dc069523b476506c123a6fea` | Function dossier | 0x14d38c IR reconstruction |
| `ev_b5c5289d306baf909fb43a622033c02e13e2cbfb2bbece4bd8e763f21b53320c` | Call graph | time_align @ 0x148a2c |
| `ev_ceb2f7def4213a53d598754c296889e0c6be7768dc3c73ff67f7f59800425d7b` | Function dossier | 0x1348e0 measured_test_rta |
| `ev_d28eb8907781be172f689052e63d26198c0f7f456eafdd33b39cc459a5e3d9fa` | Function dossier | 0x14d1a4 IR window/check helper |
| `ev_da3286d013bec03175a2acc6d490536e89c635fea62470553e00c4cf700b9b98` | Call graph | apply_ir_windows @ 0x129a50 |
| `ev_ea98712f898c6c8f4def48faf61d54bdec0a16baa1df2e593550b5272513071a` | Function dossier | 0x149f80 correlation helper |
| `ev_f07d97ea59f39adae14233b0407a24d4c532faec186d73e4e3957eb1177244d8` | Function dossier | 0x13991c spl_sweep |
| `ev_f3a92195374601b886d3d10cd3c189fff567fc4f6ac31ebdd68d2ebb1667f873` | Function dossier | 0x127e2c tfplots_new |
| `ev_f8fd0cf60509fb6ee77cd77ea671536192e94dc6a0a40e4ccfeecdec32ded331` | Function dossier | 0x129a50 apply_ir_windows |
| `ev_ff1b0085d02f253b69dacf3efa9b272f42f92e75422324664951395a36149ae0` | Function dossier | 0x13392c rta_method |

All 24 retained records are represented. No unresolved REA unknown records were returned for this session. Call graph coverage reports resolved Ghidra references; unresolved computed/indirect calls are still a limitation. The original XAPK/APK and native library are not included in the KB; the hashes bind the report to the analyzed artifacts.
