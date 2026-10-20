# A31 — native KNXnet/IP receiver (hardware-confirmed)

## Status and scope

**CONFIRMED on physical Rakoit/Linkplay A31** in the 2026-10-20 test session. The native program runs as a standalone **MIPS32 little-endian static ELF** launched manually from `/tmp`. This is **not** an official A31 firmware feature or a persistent firmware modification.

- Lab firmware: `4.6.415156`; Wi-Fi interface: `apcli0`.
- KNXnet/IP routing multicast: `224.0.23.12:3671` over UDP, using `IP_ADD_MEMBERSHIP`.
- Tested KNX source individual address: `1.1.22`, group address: `3/1/6` (binary 1-bit Mute).
- Internal player API: HTTP to `127.0.0.1:80/httpapi.asp?command=...`; status: `getPlayerStatus`; write: `setPlayerCmd:mute:0` / `setPlayerCmd:mute:1`.
- No external Mac/ESP32 KNX-to-HTTP gateway is required while the native program is running.

## Hardware evidence — v0.6 passive receiver

```text
GET_SOCKET_TYPE_RC=0 SOCKET_TYPE=1 EXPECTED_DGRAM=1
JOIN_DIRECT_RC=0
JOIN_OK
KNX_ACCEPT 1 mute=1
KNX_ACCEPT 2 mute=0
DONE accepted=2 no_audio_writes=1
KNX_EXIT_CODE=0
```

**Important implementation finding:** on Linux MIPS, `SOCK_DGRAM=1` and `SOCK_STREAM=2`. Earlier v0.1–v0.5 used the wrong socket type, causing `setsockopt(IP_ADD_MEMBERSHIP)` failures (`-71`). The v0.6 change fixed the failure. Do not revert.

## Hardware evidence — v0.7 controlled Mute with readback

```text
PROBE_LOOPBACK_RC=0 mute=0
API_OK endpoint=127.0.0.1 original_mute=0
PROBE_DONE no_audio_writes=1
KNX_EXIT_CODE=0

JOIN_OK
KNX_ACCEPT 1 mute=0
HTTP_MUTE_WRITE_RC=0 requested=0
READBACK_RC=0 actual=0 expected=0
READBACK_MATCH
CONTROL_VERIFIED
KNX_ACCEPT 2 mute=1
HTTP_MUTE_WRITE_RC=0 requested=1
READBACK_RC=0 actual=1 expected=1
READBACK_MATCH
CONTROL_VERIFIED
DONE accepted=2 verified=2
KNX_EXIT_CODE=0
```

**CONFIRMED**: A31 accepts both KNX group write values, issues the corresponding local HTTP Mute command and verifies the resulting `mute` field using `getPlayerStatus`. Observed 2/2 readback matches. In this session the accepted order was **OFF, then ON**, so the final state was `mute=1`. This does not imply a polarity inversion; event order follows actual input.

## Operating modes / limitations

- `--listen-only`: receive and decode, no audio writes (**CONFIRMED v0.6**).
- `--probe-api`: read loopback API, no audio writes (**CONFIRMED v0.7**).
- `--control-mute`: bounded two-event Mute control with readback (**CONFIRMED v0.7**).
- Only a manual process in volatile `/tmp`; no autostart, permanent install, or firmware flashing was performed.
- No hardware evidence yet for persistent service, operation across a reboot, multicasting on different network interfaces, continuous long-term operation, or KNX control of volume, sources, presets, transport, A97, A98 or A33. These are **UNVERIFIED**.
- Scope distinction: the confirmed *KNX control integration* applies to this A31 device. It does not change existing device/API command statuses for other platforms.

Provenance: physical-device SSH log supplied by project operator, 2026-10-20; binaries `A31_KNX_NATIVE_V06`, `A31_KNX_NATIVE_V07` verified through hardware tests.

## Experimental next step — v0.8 (HOST-BUILT, NOT HARDWARE-CONFIRMED)

v0.8 was compiled as a MIPS32 LE static ELF and passed **offline** KNX decoding, group/source parsing, configuration and Linkplay HTTP response-parser tests. Artifact: `A31_KNX_NATIVE_V08.zip`, with C/assembly sources, a `/tmp/knx-audio.conf` example and Russian instructions. **Do not mark v0.8 features CONFIRMED until A31 logs are supplied.**

- New **read-only** `--monitor-10m` and indefinite `--monitor` modes; 60-second heartbeat, safe UDP reconnect after 300 seconds idle.
- Runtime configurable KNX sender, A31 interface IPv4 and named group addresses: Mute `3/1/6`, Volume Up `3/1/0`, Volume Down `3/1/1`, PlayPause `3/0/0`, Play `3/0/1`, Pause `3/0/2`, Next `3/0/4`, Previous `3/0/5`, Presets1–4 `3/2/0..3` (defaults). Invalid or conflicting mappings abort before network activity. Only sender `1.1.22` is accepted by default.
- Play/pause, next/previous, source switching and presets are **decoded as observations only**, with **no audio writes**; hardware execution is future work.
- Active `--run-mute` is **opt-in** and retains strict getPlayerStatus readback and stop after 3 consecutive failures, but **long-running operation is unverified**. Previous `--control-mute` two-event bounded mode remains available.
- Experimental `--control-volume` (two KNX button presses) / `--run-volume`: read `getPlayerStatus.vol`, step ±2, issue `setPlayerCmd:vol:<n>`, verify vol readback. **A31 KNX→volume path not yet hardware-tested.**
- No autostart, flash writes, daemon installation, other-chip support, or automatic DHCP address migration. The device should only run one instance of this program per KNX listener test.
