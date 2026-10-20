# KNOB v0.8.22 — A97/A98 volume responsiveness

## Problem and resulting behavior
A97/A98 encoder volume previously waited for a new HTTPS connection and response in the UI loop. A31/A33 already use their separately verified TCP paths.

A97/A98 HTTPS absolute-volume sends now use the existing single background worker. The UI draws the encoder target immediately. One request may be in flight; all further turns replace one latest target. Completion of an older target cannot clear or delay a newer value. Requests are limited to one dispatch per120ms while turning; no extra idle poll frequency is introduced.

The worker retains one HTTPS connection for volume and getPlayerStatus when the server permits HTTP/1.1 keep-alive. It honours server closure and closes on errors, zone/IP/port/epoch changes, before artwork/other chip work, or after1500ms without another job. It never automatically replays a failed HTTP request. The existing bounded UI retry always uses the current absolute target.

The worker retains snapshot/epoch isolation across zone switches and OTA. A successful volume acknowledgement does not overwrite displayed volume with the old sent target, nor become stranded by unrelated artwork/control epoch changes.

## Preserved behavior / scope
- A31 TCP8899 and A33 TCP1234 volume paths unchanged.
- A97 confirmed PlayQueue listing and HTTPS MCUKeyShortClick launch unchanged.
- A98 PlayQueue/AVTransport subscriptions, getAllRoutines and preset correlation unchanged.
- Status fallback remains4s and group/artwork polling intervals are unchanged.
- Foreground menu/transport HTTP paths are unchanged. This release moves encoder volume to the worker; it does not claim every menu operation is asynchronous or every foreground request shares the retained worker socket.
- No A97 event capability or new RenderingControl event parsing is assumed.
- Host tests mock the network adapter; keep-alive support and speedup require measurements on the actual A97/A98.

## Diagnostics
/health:
- background_job: volume / artwork / status
- wiim_volume_sends: worker volume attempts since boot
- wiim_volume_last_ms, wiim_volume_max_ms: duration of volume requests, including TLS when needed
- wiim_https_requests: retained-worker HTTPS request attempts (volume and player status)
- wiim_https_reused: successful requests started on an already connected worker socket

Counters aggregate across zones until reboot, not per-device metrics.

## Validation
New host tests execute the actual volume dispatch/run/commit code and retained HTTPS adapter. They cover latest-target coalescing, old-zone rejection, unrelated epoch changes, bounded failure retries, artwork cancellation, offline/OTA/task allocation cases, A31/A33 route preservation, host/port/epoch session isolation, server close, errors/incomplete bodies/API rejection and absence of automatic replay.
Existing regression suites and PlatformIO build run in GitHub Actions.

Hardware baseline: user reported improved A31 and good A33 control/feedback before this change. A97/A98 optimization is implemented for hardware comparison; no measured speedup is claimed yet.

## Build result
All host regression steps and the ESP32-S3 PlatformIO build passed:
https://github.com/keshman74/airKNOB/actions/runs/39492189870
Source: https://github.com/keshman74/airKNOB/commit/cfdde6ffbbdbf971a7806d5e5505c089fb2d043c
Main OTA manifest verified at0.8.22.
Binary:https://raw.githubusercontent.com/keshman74/airKNOB/main/firmware/airControl-KNOB-v0.8.22.bin
Size:1348464 bytes; MD5:185eac7b006d2f15700770641e8039b2.

## User report before this optimization — 2026-10-20
The user reported that A31 control and feedback were noticeably faster after the previous optimization, and that A33 behaved well. This is a qualitative user hardware observation without timings or a newly supplied exact firmware identification. Preserve those working paths.
A97/A98 changes in0.8.22 remain IMPLEMENTED / HOST-TESTED / BUILD-PASSED, HARDWARE VERIFICATION PENDING.

## Implementation references
Arduino-ESP32 2.0.17 HTTPClient keep-alive, end/disconnect and response framing:
https://github.com/espressif/arduino-esp32/blob/2.0.17/libraries/HTTPClient/src/HTTPClient.cpp
These source semantics do not prove that either tested player supports persistent HTTPS sessions.

## User hardware comparison after 0.8.22 — 2026-10-20
User report in the KNOB development conversation: «на а98 заметно стало быстрее а на а97 еще притормаживает крутилка громкости».

- A98: qualitative hardware confirmation of noticeably faster control after the 0.8.22 update in this test sequence. No latency numbers or health trace supplied; this does not independently prove HTTPS keep-alive support or long-term stability.
- A97: encoder volume still lags; treat as an unresolved responsiveness issue. Do not mark A97 speed optimization hardware-verified successful.
- Need a health snapshot before/after turning with the A97 selected, including firmware, zone_chip, wiim_volume_sends, wiim_volume_last_ms/max_ms, wiim_https_requests/reused, background job/state and memory. Counters are boot-wide, so compare deltas with the same zone selected rather than attributing totals across multiple chips.
- Root cause remains unproven: separate request/TLS duration from worker contention or UI/rendering symptoms before further transport changes. Do not switch A97 to A31 TCP or plain HTTP on the basis of this report.

## A97 health comparison — firmware0.8.22, 2026-10-20
KNOB192.168.0.41; selected A97 zone192.168.0.99; zone_epoch3 in both samples.
| Field | Before | After |
|---|---:|---:|
| uptime_s | 388 | 411 |
| wiim_volume_sends | 68 | 82 |
| wiim_volume_last_ms | 1305 | 1221 |
| wiim_volume_max_ms | 1346 | 1346 |
| wiim_https_requests | 162 | 178 |
| wiim_https_reused | 46 | 46 |
| free_heap | 87920 | 84212 |
| min_free_heap | 37888 | 37888 |
| largest_free_block | 65524 | 65524 |

Both snapshots: background_poll2/background_job=status, loop stack watermark1600, worker watermark3112, reset_reason3. No reboot is shown between the samples (uptime increases). No memory leak is established by these two heap values.

Over23 seconds:14 volume attempts,16 worker HTTPS attempts,0 additional successful requests on an already-connected worker socket. The earlier46 reused successes are boot-wide and cannot be attributed to A97. Last completed volume attempts took1.305s and1.221s; the1.346s maximum is boot-wide. Attempt counters are not successful player-application acknowledgements.

Conclusion: the measured volume-request duration is sufficient to explain slow command delivery despite asynchronous UI dispatch. No successful socket reuse was recorded in this interval. This does not isolate TLS-handshake time from server response/body/network time or prove the server always forbids keep-alive.

Next evidence needed: inspect the A97-advertised RenderingControl SCPD and time GetVolume over its advertised UPnP HTTP endpoint. The KB currently marks SetVolume as SCPD-documented, not per-action hardware verified. Do not change /httpapi.asp to plain HTTP or use A31 TCP as an assumed substitute. GetVolume diagnostic is read-only; SetVolume and event payload compatibility require separate confirmation before firmware integration.
