# KNOB RAM and screenshot capture — v0.8.16

Status: IMPLEMENTED / HOST-TESTED; hardware validation pending.
Source: airKNOB experimental/multichip-v0.8.0 commit 5b7c230aed211172544ec881c46bda3f7fb151ae.

## Symptom and evidence
2026-10-20 user reported KNOB slowdown and web screenshot response Not enough free RAM. Firmware v0.8.15 requires a largest free block >=116000 bytes and a 240×240 RGB565 sprite for screenshot. Normal Player drawScreen also repeatedly attempts the same full sprite.
240×240×2=115200 bytes is a contiguous allocation. Total free heap alone is not sufficient evidence it can be allocated.
No hardware heap measurement or confirmed memory leak is available from this report; slowdown may have additional causes.

## Change
Player redraw and screenshots use a temporary reusable 240×16 RGB565 sprite: 7680 bytes, 15 times smaller. Coordinates are translated/clipped by DisplayRouter. The volume arc only computes rows in the current band.
Allocate once per frame/screenshot, reuse for15 bands, free afterward, including disconnect handling. No reduction in RGB565 color depth.
Screenshot remains a 240×240 24-bit BMP, bottom-up rows, 172854-byte payload. Screenshot regeneration does not repaint the physical LCD.
No settings erase, filesystem format, factory reset, or speculative heap cleanup.

## Diagnostic endpoint
KNOB HTTP GET /health returns firmware, uptime_s, free_heap, min_free_heap, largest_free_block (internal8-bit), psram_total, psram_free, capture_buffer_bytes.
This reads ESP memory state only and sends no query to the player. Values are bytes except uptime seconds.
Use before/after a screenshot and over time to distinguish low total heap, fragmentation, PSRAM availability and reset uptime. Do not infer these from screenshot refusal alone.

## Tests and limits
Host test compiles actual DisplayRouter and handleScreenshot with a bounded sprite mock and compares a reference scene across band boundaries, image cropping, BMP row order/length/colors and disconnect cleanup. Old full-screen allocation is rejected by the test harness.
Hardware LCD speed/flicker and long-running memory stability still require testing. Screenshot serving is synchronous for the requested image; this change does not make every network operation asynchronous.
