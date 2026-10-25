# iAudioCloud static evidence — 2026-10-25

[Canonical analysis](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md). [Opcode/source catalogue](../../protocols/a33-native-23040/IAUDIOCLOUD-OPCODES-2026-10-25.md).

Original supplied XAPK SHA256 `7c7111112c224d65584440e085c2832330efa431bf7b91ea32f8c343513e65b9`; base APK `c2efb0d153fd1005b4819dc358922ae7972f7d1b646e11a41ec4725096b0cefb`. [Split inventory](IAUDIOCLOUD-INVENTORY-2026-10-25.json).

REA 6.7.0, JADX Headless MCP 0.7.1, JAR SHA256 `6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75`, Java 27. Supplemental local static analysis used the same JAR's JADX and dexlib2 APIs, single decompiler worker, 4GiB heap; no app code executed. Decompiled Java aliases were cross-checked with original DEX descriptors and smali arrays. [Generated source hashes](IAUDIOCLOUD-SOURCE-HASHES-2026-10-25.json) identify local analysis products, not vendor source.

[Selected REA evidence projections](IAUDIOCLOUD-2026-10-25.json) retain IDs, normalized results and limitations; duplicate raw tool envelopes omitted:

- archive parent `ev_9b29ea5b540c13ac302a8d35b5be9163ca5423b4e763899460c51e127d45484d`;
- Android package parent `ev_ee0a1aee5500a96777227a0ab4c44f3fe456a0e519b8aaabf901fa9055bf34aa`;
- discovery port method `ev_f60319249805b2da525a81225e5251ee422be5fda1692c521b162db42dc84fca`;
- frame builder `ev_83f42bc8dcbe1fb8a229a8a454a518eff1b3d66172b966b0e05f65ce51f0ee18`;
- BLE frame method `ev_ad91d405f3ab9c65d23e753d34a7ebb15aeae09b6159ecfc1024aed630701d0e`.

All four DEX files were scanned for const-string method references. Selected decompilation covers agreement classes, device models, discovery/network utilities and provisioning callers; this is not a claim to review every application class. The 141 constants are exhaustive within DeviceModel initializer, not every possible app protocol; 109 send sites are bounded to 35 selected agreement classes plus DeviceModel. Request-field extraction is supplementary and can contain alternative branches and nested fields; the curated report explains reviewed schemas.

No hardware tests, app installation, traffic capture, signature/authenticity check or firmware operation. Static evidence must not promote previously untested commands to CONFIRMED. Original user archive was not modified. No APK, full proprietary source dump, account token or user credential is committed.
