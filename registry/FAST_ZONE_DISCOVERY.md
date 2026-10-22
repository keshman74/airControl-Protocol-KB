# Fast progressive zone discovery

Canonical IDs: **DISC-FAST-ZONES-001**, **RULE-DISCOVERY-NONBLOCKING-001**, **RULE-DISCOVERY-CANCEL-GENERATION-001**.

## Evidence and scope

**DISC-FAST-ZONES-001 — CONFIRMED (overall practical result on KNOB v0.8.5).**

On 2026-10-12 the user reported: «так гораздо быстрее ищутся и находятся все зоны!» and explicitly requested promotion of the method into airControl-Protocol-KB.

This confirms faster discovery and successful discovery of all expected zones in the user's tested LAN. No numerical duration, repeated-run count, complete device list or per-chip firmware inventory was supplied. Do not convert this aggregate confirmation into independent hardware proof for every chip, every discovery path, or every command. Prior KNOB versions intermittently missed zones, including the zone called Office; the final report does not separately enumerate IP addresses.

**RULE-DISCOVERY-NONBLOCKING-001 — IMPLEMENTED + HOST-TESTED.**
**RULE-DISCOVERY-CANCEL-GENERATION-001 — IMPLEMENTED + HOST-TESTED.**

Component details below are established by pinned source and automated tests. Their combined practical outcome is confirmed by the user. No packet capture was supplied for this specific verification.

Hardware report: [KNOB v0.8.5, 2026-10-12](../evidence/hardware-tests/KNOB-DISCOVERY-v0.8.5-2026-10-12.md).

## Reusable algorithm

1. Start an on-demand discovery session with a new generation ID and a snapshot of local IPv4 settings.
2. Continuously collect SSDP responses, LOCATION addresses, multicast NOTIFY and A33 UDP beacon candidates; enqueue local IP hints without making HTTP/TLS calls in the receive/UI loop.
3. Seed the queue with the selected and previously verified IP addresses. A cache entry is only a hint: validate the real device again before treating it as found/Online.
4. Run network validation separately. Use a bounded nonblocking TCP candidate sweep of known API ports. Verify candidates with a real getStatusEx request, parsed device identity and the appropriate API family.
5. Transfer plain result records back to the UI owner through a bounded queue. Show each successfully validated zone immediately, without waiting for the full sweep.
6. Suppress duplicate verified candidates. Retry unsuccessful validation within a finite budget; a first failure must not permanently exclude the host from the current session.
7. Permit selection and cancellation during discovery. Increment the generation and reject any late result belonging to the old session.
8. Close discovery sockets at completion/cancellation, persist verified IP hints, and put the worker to sleep until the next explicit search.

Do not replace this method with a serial blocking scan or HTTP validation inside SSDP packet handling. Do not stop the fallback sweep just because the first zone was found.

## Discovery mechanisms

| Mechanism | Packet / address | Candidate extraction |
|---|---|---|
| Active SSDP | UDP 239.255.255.250:1900, M-SEARCH | Both datagram sender IPv4 and IPv4 host from LOCATION |
| Passive SSDP | Temporary multicast listener on 239.255.255.250:1900 | NOTIFY sender and LOCATION |
| A33 native beacon | UDP :53308 | Sender as an IP hint, followed by API verification |
| API-port sweep | Current IPv4 /24, additionally subnet-filtered | Open 80/443/8000/8443, followed by getStatusEx |
| Known-IP cache | Previously verified local addresses | Prioritized fresh API checks, never assumed Online |

SSDP targets used by KNOB: ssdp:all, upnp:rootdevice and urn:schemas-upnp-org:device:MediaRenderer:1. Each burst uses:

```http
M-SEARCH * HTTP/1.1
HOST: 239.255.255.250:1900
MAN: "ssdp:discover"
MX: 1
ST: <target>

```

The A33 beacon's advertised encoded native port is not treated as an HTTP API port. This discovery implementation uses the beacon for an IP hint; it does not invent a Linkplay UDP/UDPX request.

## Candidate API verification

| Family | Known control endpoint |
|---|---|
| A31 / Linkplay HTTP | http://<ip>:80/httpapi.asp?command=getStatusEx |
| A97/A98 / Linkplay HTTPS | https://<ip>:443/httpapi.asp?command=getStatusEx |
| A33 / ACS2 HTTP | http://<ip>:8000/?Instruct=getStatusEx |
| A33 / ACS2 HTTPS | https://<ip>:8443/?Instruct=getStatusEx |

An open port or SSDP packet alone is not sufficient. Require a successful API response and valid device status JSON. Prefer the port already observed open. Chip identification and transport selection are distinct: valid Linkplay identity with uuid plus DeviceName/project/hardware at the Linkplay API can be retained as LINKPLAY when the exact hardware label is unknown. Do not assume A31-specific TCP/DSP capabilities for that generic profile.

This table records implemented discovery routing; independent per-chip HTTP/HTTPS and command evidence remains in the existing device/protocol registries.

## KNOB v0.8.5 implementation profile

| Parameter | Source value |
|---|---|
| API validation workers | 1 FreeRTOS task, 12 KiB stack |
| Nonblocking TCP probe slots | At most 4, 180 ms connect deadline |
| Ports | 80, 443, 8000, 8443 |
| Socket budget | Close probe sockets before HTTP/TLS validation |
| API read timeout in discovery | 600 ms; HTTP connect timeout 350 ms; TLS handshake setting 2 s |
| Host validation budget | At most 2 validation jobs per host; deferred retry 700 ms |
| Internal port-80 retry | Up to 2 GET attempts within each validation job; distinguish this from the job budget |
| Queues | 32 candidate jobs, 24 plain result records |
| SSDP bursts | 3 bursts, spaced 800 ms apart |
| Minimum receive window | 6500 ms |
| Overall worker deadline | 60000 ms, checked between operations; an in-flight request may finish later |
| Web result refresh | 500 ms while searching |
| Cache | Verified IP hints saved at stop/completion and checked again next time |
| Idle behavior | Task notification sleep, no periodic network scan |
| Main UI ownership | Worker does not manipulate the LCD, menu, Preferences or zone array |

The full sweep is still a /24 implementation. These limits are an ESP32 profile, not universal protocol requirements or measured discovery duration. Do not copy desktop concurrency limits blindly to constrained hardware.

During a search KNOB pauses automatic cover/status polling and screenshot servicing; explicit volume/button control remains available. A user-triggered control request may still take its normal transport time. Cancellation is logically immediate; it does not forcibly kill an HTTP/TLS call already in progress.

## Desktop airControl comparison

Current progressive desktop implementation runs SSDP and /24 probing concurrently, emits validated devices immediately, scans up to 96 addresses concurrently with four port probes per address, uses a 110 ms TCP probe timeout and a 600 ms status-validation timeout. It extracts both sender and LOCATION addresses.

The historical DISCOVERY_V4.1.1.md note describes an older fallback-only approach. The current electron/main.cjs implementation is the reference for progressive discovery. The reusable rule is independent receipt, bounded validation and immediate results, rather than identical worker counts.

## Regression tests and acceptance

Automated checks cover:
- actual endpoint detector: supported transports, preferred port, generic Linkplay profile, invalid status rejection and stale generation;
- actual SSDP LOCATION parser: response/NOTIFY, header case, explicit ports, invalid URLs;
- scheduling ledger: duplicates, verified hosts, bounded retry, restart, full subnet and timer wrap;
- actual worker code under deterministic socket/FreeRTOS mocks: main enqueue during a delayed API call, stale-result rejection, restart, four live probe sockets and cleanup;
- web selection while scanning and stop control;
- retained encoder, OTA and versioned-firmware checks.

Host mocks verify logic, not ESP32 radio timing. For future ports/releases, test repeated scans against a known device inventory, cancellation/restart, cached-offline devices, simultaneous native-app control, audio continuity, memory/socket use and cold/warm network caches. Preserve the v0.8.5 user-confirmed behavior as the KNOB discovery baseline.

## Immutable source references

- [KNOB v0.8.5 main.cpp](https://github.com/keshman74/airKNOB/blob/efeccb316fb041da5872c48ace92db60429e85ef/src/main.cpp)
- [KNOB retry/deduplication ledger](https://github.com/keshman74/airKNOB/blob/efeccb316fb041da5872c48ace92db60429e85ef/src/discovery_scheduler.h)
- [KNOB worker regression test](https://github.com/keshman74/airKNOB/blob/efeccb316fb041da5872c48ace92db60429e85ef/tests/worker.test.py)
- [Successful build and checks](https://github.com/keshman74/airKNOB/actions/runs/38297173264)
- [Desktop progressive discovery reference](https://github.com/keshman74/airControl/blob/16f8436a2ad9364c0457cf75ce066f452b5d8dec/electron/main.cjs)


## Использующие проекты / навигация

[airControl](../projects/airControl/README.md) · [airALARM](../projects/airALARM/README.md) · [KNX Gate](../projects/knx-gate/README.md) · [airKNOB](../projects/airKNOB/README.md).
Состояние переноса, проверки и применимости: [KB_CROSS_PROJECT_MAP](../KB_CROSS_PROJECT_MAP.md). Наличие ссылки не означает реализацию или аппаратное подтверждение в каждом проекте.
