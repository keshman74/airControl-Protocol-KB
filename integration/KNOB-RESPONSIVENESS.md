# KNOB responsiveness and resource use — v0.8.17

Status: IMPLEMENTED / HOST-TESTED / BUILD-PASSED. Hardware validation of v0.8.17 is pending.

Source: https://github.com/keshman74/airKNOB/commit/17d8363c6fb80663b6c4a49a40ccc81637d1dcb4

Canonical A98 protocol remains [A98-PRESETS.md](../protocols/wiim-httpapi/A98-PRESETS.md). This integration change does not replace device protocol evidence.


## Evidence and scope

Baseline: 0.8.16, experimental/multichip-v0.8.0. User measured 140496 bytes free internal heap, 86004-byte largest block, and 8365395 bytes free PSRAM. These numbers alone do not establish a leak or reboot. The A31 at 192.168.0.35 returned GetKeyMapping HTTP 200 in 27 ms, 3432 bytes; MaxNumber 20 and one populated Key1. The raw XML was not supplied. The cause of the panel's READ FAILED is therefore not yet proven.

## Implemented

- One background worker handles periodic status/group polling and artwork download/decode. It never draws the display. Results are committed by the UI task only if their zone and operation generations still match. Cover pixels use a staging buffer; canceled/obsolete results never replace current artwork.
- Encoder events are drained in order with bounds applied per event, then rendered once. Volume commands retain coalescing and pacing; no request is emitted for every stale intermediate value.
- Main UI loop handles input before web and maintenance work. Background work starts only after interaction/network quiet periods. A33 playback and group status share getStatusEx. Existing event-first TCP/GENA behavior is retained.
- HTTP body size and receive checks reject truncated/oversized data and parse chunk framing via HTTPClient. Body writes have a time budget, in addition to socket timeouts; this is not a hard preemptive deadline for the entire HTTP transaction.
- A33 TCP reconnect clears partial JSON; malformed A31 volume events are ignored; loading/unknown playback state does not become a false pause. Explicit FAIL/Format/Exceed responses are rejected; documented A33 Not/empty selection semantics remain.
- A31 KeyList extraction accepts XML namespaces; sparse slot IDs remain intact. Preset diagnostics are exposed in /health. A98 PlayQueue/AVTransport/GetKeyMapping/routines matching remains unchanged.
- Volume arc geometry is cached in 57600 bytes of PSRAM, with a computed fallback if allocation is unavailable. Rendering is clipped to screenshot strips. The background worker requires an 8192-byte stack.
- OTA validates filename, nonempty size and declared byte count; errors are displayed instead of silently waiting. Zone polling in the browser pauses during upload.

## Validation

Host regression tests cover encoder reversal/clamping/menu input, complete/incomplete bounded HTTP bodies, all 240×240 arc pixels at every volume, stale background results, artwork URL fallbacks/cancel, sparse presets, A98 routines/events, A33 resume guards, discovery, screenshot strips and web upload behavior. Firmware compilation is a separate CI gate. See the workflow linked to this source commit for the actual result.

## Remaining limits and hardware checks

- Test on A31/A33/A97/A98: rotate during a slow artwork download, switch zones while a response is pending, change source/preset from another controller, upload through a desktop and phone browser.
- Check A31 presets; if READ FAILED remains, capture /health immediately and provide the saved raw GetKeyMapping XML privately.
- Initial unknown-device detection, explicit menu operations, preset reads and GENA subscription maintenance still have bounded synchronous calls; not every network action is asynchronous.
- Artwork limits remain 350 KB and 2048 pixels per dimension; unsupported PNG formats are not newly supported.
- No hardware latency measurements or full hardware validation are claimed. Stable main and its online update channel are unchanged.

## User-provided v0.8.16 observation

The user supplied a working BMP screenshot showing the Presets READ FAILED state and a /health response with uptime 991 seconds, min_free_heap 88320, psram_total 8385799, capture_buffer_bytes 7680. Thus screenshot capture was demonstrated in that instance, but long-term memory stability and the preset failure cause were not established.

## Build verification

All 25 host regression test suites passed, and ESP32-S3 PlatformIO build/publish succeeded in [GitHub Actions run 39416413210](https://github.com/keshman74/airKNOB/actions/runs/39416413210).
Firmware: airControl-KNOB-v0.8.17.bin; 1342832 bytes; MD5 99efec4f7b097ceda9ecf551317a6c33.
Linker reports static RAM 171928/327680 bytes (52.5%) and flash 1342465/3342336 bytes (40.2%); these are not runtime heap measurements. Dependency macro/attribute warnings remain; the build succeeded.
