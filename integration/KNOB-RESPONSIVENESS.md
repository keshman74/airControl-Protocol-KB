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

## Hardware regression report — 2026-10-20, v0.8.17

Status: USER-OBSERVED / HEALTH-CAPTURED. Root causes and firmware fixes are not yet verified.

KNOB address for this test: 192.168.0.41.

- A33: user reports preset menu/operation normal. Preserve this behavior; this is not a claim that every A33 function is validated.
- A31 at 192.168.0.35: Presets presents Refresh rather than populated entries. First health sample: HTTP200, preset_bytes0, preset_error=http_or_body, uptime6825. Later: HTTP200, preset_bytes10740, preset_error=xml_structure, uptime6908. Thus both body-read failure and parser rejection were captured; the actual 10740-byte XML has not been supplied. Do not assert a MaxNumber, namespace or encoding cause without that payload.
- A98 at 192.168.0.21: before failure, health showed HTTP200, preset_bytes4340, preset_error empty, uptime6930, zone_epoch3. Next sample: uptime2, zone_epoch0, HTTP-1/body0. This confirms that KNOB restarted around the reported preset-menu failure. It does not prove that the player rebooted, that polling overload caused it, or that low heap alone caused it.
- Before A98 restart: free_heap87920, min_free_heap74956, largest_free_block73716, psram_free8307731. After restart: free_heap106024, min_free_heap105912, largest_free_block94196. These are observations, not a confirmed memory leak.
- Missing evidence: A31 GetKeyMapping response structure; KNOB reset reason/serial panic or watchdog log for the A98 restart. Static inspection shows synchronous preset reads can overlap the periodic background worker; causality remains unverified.

Promotion to the main OTA channel earlier that day was at the user's request. Build/host-test success must not be represented as hardware regression clearance. Do not label the A31/A98 preset issues fixed until hardware retesting.

## Hardware follow-up and A98 menu hardening — 2026-10-20

- User confirmed A31 presets fixed after installing0.8.18. Promote the A31 MaxNumber21 parser fix to **USER/HARDWARE-VERIFIED on the tested A31**, while preserving the separate prior body-read failure as an unconfirmed intermittent issue.
- On A98 selected192.168.0.21,0.8.18 health after another restart showed uptime3, reset_reason4, loop_stack_watermark_raw3808, worker_stack_watermark_raw4012, free_heap108072, min_free_heap104696, largest_free_block98292.
- **Reset-code correction:** ESP-IDF4.4.7 defines ESP_RST_PANIC as4 and ESP_RST_INT_WDT as5. The assistant initially called4 an interrupt watchdog, then corrected that statement after checking the source. Treat this capture as panic/exception, not a proven watchdog, low-RAM or stack-overflow diagnosis. Source: https://github.com/espressif/esp-idf/blob/v4.4.7/components/esp_system/include/esp_system.h .
- Stack high-water marks in this response belong to the new boot; they do not describe stack usage at the prior panic.

### KNOB0.8.19 implemented changes — hardware confirmation pending

Source: https://github.com/keshman74/airKNOB/commit/11603ff19371d03bbb4895e8657a6b5ecbc08a52 .
A98 menu entry/Refresh schedules a one-shot read. The UI loop executes it after the button handler returns and after any background status/artwork job completes and is drained. Pending reads block new periodic jobs and A98 maintenance. Menu/zone/chip changes cancel obsolete work; OTA, discovery and pending volume defer it. Failed attempts pace metadata retry. A persistent UI-only scratch Model replaces the temporary12-key model on the loop-task stack; mapping() resets it before each load.
A31 and A33 retain existing preset-read paths, including the hardware-confirmed A31 fix.

Actual deferred-reader host regression passed: no overlapping network read while worker busy, single execution, cancellation, OTA/reboot/volume/scan gates, retry pacing, and A31/A33 isolation. The complete build/test result is tracked at https://github.com/keshman74/airKNOB/actions/runs/39482167685 .
These changes remove concrete overlap/stack-depth risks; they do not establish the observed panic's root cause or prove a hardware fix. If reproduced, obtain serial exception/Backtrace plus post-boot /health. Do not disable watchdogs or erase settings as a substitute for evidence.

## User hardware confirmation — KNOB0.8.19, 2026-10-20

After receiving0.8.19 for the A98 preset-menu restart, the user replied “исправили!” (“fixed”). Mark the previously reported A98 preset-menu restart as **USER/HARDWARE-VERIFIED RESOLVED on the tested device in this retest**. The exact internal panic cause remains unproven; no serial backtrace was supplied. Do not generalize this short retest to long-running stability or every A98 firmware.

Confirmed checkpoints to preserve: A31 preset list fixed in0.8.18 (MaxNumber21 variant); A98 preset-menu restart resolved in0.8.19 with deferred, serialized preset loading and reduced loop stack use; A33 preset behavior previously reported normal. A97 has no new hardware result in this exchange.
