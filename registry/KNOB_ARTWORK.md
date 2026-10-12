# Artwork preparation for airControl KNOB

## RULE-KNOB-ARTWORK-PREP-001 — Adopted preparation rule
Status: **DESIGN RULE / NOT YET IMPLEMENTED**. Adopted by the user on 2026-10-13 (Europe/Kyiv).

When airControl serves a radio cover to a KNOB panel, provide a separately cached reduced variant:
- Target canvas: **152 × 152 pixels**, preserving aspect ratio; center/letterbox rather than stretch.
- Format: non-interlaced **8-bit-per-channel PNG**, or **baseline JPEG**.
- Preserve the original cover for desktop/mobile display. The KNOB variant must not replace or degrade the original.
- Reuse the generated variant for the same source content; do not resize or download again on every status poll.
- The compressed result must remain comfortably below the KNOB byte limit; check actual encoded size.
- Endpoint shape/query parameter is not specified yet. KNOB and server must agree on variant selection before shipping.
- This preparation must not add player-control requests. Fetching the image is a separate media-server operation.

This reduces network transfer, RAM requirements and decoder work. No measured latency improvement or successful hardware test of the proposed variant is claimed.

## Current KNOB constraints
Source: airKNOB experimental/multichip-v0.8.0, v0.8.9.
Status: **IMPLEMENTED / SOURCE-VERIFIED**.
- Maximum compressed download: **350 × 1024 = 358400 bytes**.
- Maximum original PNG/JPEG dimensions: **2048 × 2048**.
- Interlaced PNG rejected.
- Covers are currently downloaded into RAM before decoding. A file smaller than the maximum is not guaranteed to fit the available contiguous heap.
- Rendered artwork region is **76 × 76**.
- v0.8.9 accounts for JPEGDEC progressive DC output at ceil(original/8). This is thumbnail decoding, not full progressive reconstruction.
- 16-bit-per-channel PNG compatibility is **NOT established** by these user tests; do not label it unsupported or confirmed supported without decoder/hardware evidence.

## User observations — A98
Status: **CONFIRMED user readback / bounded scope**.
Device reported: A98 / AmlogicA113 / Linkplay.4.8.827634. KNOB v0.8.9 reported as improving covers, with remaining missing examples.
The user downloaded the following images on their Mac and reported their absence on KNOB:

| Example | Bytes | Dimensions | Encoding | Exceeded source limit |
|---|---:|---|---|---|
| The Sound Of Silence — Disturbed | 422312 | 600 × 600 | PNG RGB, 8-bit/channel, non-interlaced | Compressed bytes |
| SomaFM Space Station Soma (320k MP3) | 751774 | 400 × 400 | PNG RGB, 16-bit/channel, non-interlaced | Compressed bytes |
| IBIZA CHILLOUT LOUNGE | 96571 | 2500 × 2500 | PNG RGB, 8-bit/channel, non-interlaced | Dimensions |

All three downloads returned HTTP 200 on the Mac. The last two URLs were served by airControl's local HTTP radio-cover endpoint, port **17890**, path **/radio-cover/<cover-id>**.
These observations plus the source limits explain why the current firmware rejects these examples. Mac HTTP 200 does not prove a successful ESP32 download. The findings do not establish behavior for every cover, chip or server.

## Direct external artwork
The Disturbed URL comes from publicfile.linkplay.com, rather than airControl's local cover server. Local variant generation alone does not fix direct external URLs from a native phone application.
A separate constrained-memory approach is required for those large images. Temporary flash-file decoding is a **candidate**, not implemented/validated here; do not increase RAM allocation blindly or format existing storage.

## Related behavior
If artwork is missing, rejected or fails to decode, do not show a prior station/album cover as current. Empty artist metadata must clear the previous artist.
A transient OFFLINE indicator is a separate issue; none of these image tests proves a panel/player restart.

Evidence: [user test record](../evidence/hardware-tests/KNOB-ARTWORK-LIMITS-2026-10-13.md).
