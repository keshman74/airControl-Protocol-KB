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
- Native KNX→Mute and volume control are hardware-confirmed on the tested A31 as of v0.9 (details below). Transport commands were accepted by the local HTTP API, but playback effects were not read back. Presets 1 and 2 are hardware-confirmed via physical playback switching in v0.9, with operator confirmation; presets 3–10, sources, reboot persistence, permanent service/autostart, unattended long-duration operation, alternate interfaces and other chips are **UNVERIFIED**.
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

## Native KNX v0.9 — partial hardware confirmation (2026-10-20)

Build artifact `A31_KNX_NATIVE_V09.zip`: static MIPS32 LE ELF with C/assembly source, runtime configuration and host tests. **CONFIRMED on physical A31 only for the functions explicitly evidenced below; other functions remain UNVERIFIED.**

- New opt-in `--run-all` mode: continuous UDP KNX receiving; fixed sender filter `1.1.22` and configurable KNX GA mapping.
- Transports via **local** Linkplay HTTP API: `setPlayerCmd:onepause`, `resume`, `pause`, `next`, `prev` (from existing KB; no rediscovery). Mute has readback and volume uses getPlayerStatus read/absolute set/readback with step 2.
- Native presets via official framed **TCP :8899**: binary header `18 96 18 20`, little-endian payload length and byte sum, 8 reserved zero bytes, `MCU+KEY+001..010`. Default mapped KNX GA `3/2/0..3` (slots 1–4), other slots only after explicit GA configuration. Presets **1 and 2 are confirmed to change playback** by the operator's direct observation of the physical device during the v0.9 test; the log itself records TCP transmission but does not include native MCU acknowledgement or readback. Presets 3–10 remain unverified. At least 200ms is enforced between preset commands.
- Optional source AUX and USB use previously CONFIRMED A31 HTTP switchmode forms, but KNX source mappings default OFF.
- Only KNX value 1 triggers button actions; value 0 is a release. Mute treats both 0 and 1 as states. Repeat button telegrams within 350ms are suppressed.
- Local command mode remains temporary-only under `/tmp`; no flash/autostart. Previous hardware-confirmed v0.7 remains the rollback baseline.

Suggested single end-to-end integration run: after copying the ELF and config into `/tmp`, manually execute `--run-all` and press the existing KNX transport/volume/Mute/preset buttons. Verify observed behavior in the player rather than retesting each underlying HTTP API from scratch.

### Physical device log: v0.9 `--run-all` (2026-10-20)

- Platform: A31 Wi-Fi interface `apcli0`, IP `192.168.0.35`, source filter `1.1.22`. Config loaded; multicast `224.0.23.12:3671` JOIN_OK.
- `33` accepted KNX events during >420s elapsed runtime, with HEARTBEAT at 60s intervals until 420s; SSH session stopped manually with Ctrl+C. **CONFIRMED** extended interactive run (not a long-term soak test, not auto-start or reboot persistence).
- **Mute GA `3/1/6`: CONFIRMED.** 11 accepted mute events: 1 correctly skipped unchanged OFF state, 10 state-changing HTTP writes; all 10 state-changing writes had `READBACK_MATCH`.
- **Volume GA `3/1/0`, `3/1/1`: CONFIRMED.** 12 accepted volume commands (4 down, 8 up), each followed by `VOLUME_READBACK_MATCH` after HTTP set and player status read. The reported volume traveled 91 → 83 → 99. **Risk:** uncontrolled button repetition raised volume to 99%; add an explicit maximum level, preferably user-configurable. Logs included several `DEBOUNCE_SKIPPED`; tune repeat/debounce to not lose intentional holds.
- **Transport GA `3/0/0`, `3/0/1`, `3/0/2`, `3/0/4`, `3/0/5`: API ACCEPTED only, NOT PLAYBACK-STATE-VERIFIED.** 10 events logged with `HTTP_ACTION_RC=0` and `HTTP_ACCEPTED_NOT_STATE_VERIFIED`: 2 PlayPause, 2 Play, 2 Pause, 2 Next, 2 Prev. Do not imply that playback transition was independently confirmed by this log.
- **Presets GA `3/2/0..3`: NOT TESTED** in this trace (no PRESET events). Preset 5–10 KNX addresses OFF. Native TCP :8899 preset launch integration requires separate device evidence. **Sources AUX/USB: NOT TESTED** (groups OFF).
- Runtime's `HEARTBEAT verified=25` is not a pure readback count: it includes actions merely dispatched/accepted. Use distinct counters for `received`, `write_sent`, `readback_confirmed`, `http_accepted_without_readback`, and `skipped` in future releases.

Evidence excerpts:

```text
JOIN_OK group=224.0.23.12:3671 on 192.168.0.35
KNX_EVENT 12 src=1.1.22 ga=3/1/1 action=VOL_DOWN value=1
VOL_BEFORE=91 REQUEST=89
HTTP_VOLUME_WRITE_RC=0 target=89
VOL_READBACK_RC=0 actual=89 expected=89
VOLUME_READBACK_MATCH
KNX_EVENT 30 src=1.1.22 ga=3/0/1 action=PLAY value=1
HTTP_ACTION_RC=0 action=PLAY
HTTP_ACCEPTED_NOT_STATE_VERIFIED
HEARTBEAT seconds=420 accepted=25 verified=25
```

The native program ran in temporary `/tmp` only; no firmware or permanent startup modifications have been performed. The later operator confirmation of preset playback (see next section) completes the requested preset-button test. Do not needlessly re-test established Linkplay HTTP commands.


### Physical device follow-up — native preset transmission via TCP :8899 (2026-10-20)

**HARDWARE-CONFIRMED PLAYBACK CHANGE FOR SLOTS 1–2 (operator observed); LOG TRANSMIT-ONLY**: A31 v0.9 `--run-all` accepted 11 KNX events and reported the following four native preset transmissions:
```text
KNX_EVENT 5 src=1.1.22 ga=3/2/0 action=PRESET_1 value=1
PRESET_TCP_SEND_RC=0 slot=1
PRESET_TRANSMITTED playback_not_readback_verified
KNX_EVENT 6 src=1.1.22 ga=3/2/1 action=PRESET_2 value=1
PRESET_TCP_SEND_RC=0 slot=2
PRESET_TRANSMITTED playback_not_readback_verified
KNX_EVENT 7 src=1.1.22 ga=3/2/1 action=PRESET_2 value=1
PRESET_TCP_SEND_RC=0 slot=2
PRESET_TRANSMITTED playback_not_readback_verified
KNX_EVENT 8 src=1.1.22 ga=3/2/0 action=PRESET_1 value=1
PRESET_TCP_SEND_RC=0 slot=1
PRESET_TRANSMITTED playback_not_readback_verified
```
The TCP send returning zero is not a positive A31 MCU acknowledgement. No state readback or independent native MCU acknowledgement is included in this log. **Following this trace, the operator explicitly confirmed that KNX preset buttons 1 and 2 switched between their respective stored presets and started playback on the actual A31. Therefore the end-to-end KNX→TCP8899→preset playback behavior is CONFIRMED for slots 1 and 2, by operator observation, while the trace alone remains transmit-only.** TCP :8899 on-loopback connection and write **succeeded** to the extent that the caller reported no error, but no RX packet is shown.

The same follow-up includes 2 Mute state transitions with `READBACK_MATCH`; 3 volume-down operations with `VOLUME_READBACK_MATCH` (90→88→86→84); and two `PLAY_PAUSE` commands with HTTP acceptance only. The final reported volume is **84%**, so an appropriate maximum-volume clamp remains an outstanding safety requirement. `HEARTBEAT accepted=7 verified=7` **overcounts** actual state-verified actions, because preset and transport dispatches are included in the current verified counter.

This trace ended manually with Ctrl+C; no persistence or unattended soak-time claims follow from it.


### Operator confirmation — presets 1 and 2 really switched and played (2026-10-20)

Operator answer after reviewing the above log: **«да переключались»**, explicitly confirming that physical A31 changed between KNX-triggered Preset 1 (`3/2/0`) and Preset 2 (`3/2/1`) and played the selected presets. **Status: CONFIRMED on physical device for these two KNX→A31 native TCP 8899 preset paths.** This evidence is direct operator observation, not a readback field or MCU acknowledgement; keep those categories distinct.

Next engineering work: configurable max volume below 100 (previous tests reached 99%), hold/repeat behavior, split `verified` vs `accepted` statistics, service lifecycle reliability and *only then* consider persistent startup after a separate safety review. Presets 3–10 are not claimed as hardware-tested through KNX here.
