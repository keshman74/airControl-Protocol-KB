# airControl v5.0.11: A97/H50 UPnP radio start fallback

**Evidence status:** User-observed symptom + static airControl code review. TCP play command is protocol-documented, but this change is **NOT-HW-VERIFIED** on A97/H50. No device command or network capture was issued by this research.

## Observed behavior

The user reports that on the A97 non-HTTPS path, choosing a station updates metadata and artwork in the native player, but the stream remains stopped until Play is pressed in the native application. airControl reports `socket hang up`. In the same report, radio works on the other chip paths. The screenshot identifies an H50-labelled UI tile; the exact hardware identity is not independently verified by this screenshot.

## Source finding

In airControl v5.0.10, the `device.upnpOnly` radio route sends UPnP AVTransport `SetAVTransportURI` with DIDL-Lite metadata/art and then AVTransport `Play` (`src/main.jsx:2542-2582`, `electron/main.cjs:1747-1783`). A socket-reset response is checked against transport state and SOAP Play may be retried. If it still fails, that route returns an error and does not use another play transport.

The A97/H50 UPnP fallback profile documents the Linkplay/Arylic framed TCP/8899 payload `MCU+PLY-PLA` as a playback command, but explicitly does not mark it as H50 write-confirmed. The command is therefore a suitable guarded fallback candidate after an unsuccessful UPnP Play, not a proven device-specific fix.

## v5.0.11 change

For the UPnP-only radio path only:

1. Keep sending metadata/artwork through the discovered AVTransport endpoint.
2. Keep the existing SOAP Play attempt and socket-reset handling.
3. If SOAP Play ultimately fails, send one framed `MCU+PLY-PLA` request over TCP/8899 with no reply expected.
4. Query UPnP transport status after the send and return the fallback transport/state details to airControl.
5. API-enabled A31/A97/A98 routes remain unchanged.

The UI now treats a successful TCP send as an accepted playback request so it will not discard the selected station or immediately move to another stream candidate. `transportStateConfirmed` distinguishes a state readback from a send-only acceptance.

## Evidence boundaries

- User observation establishes the symptom and the native-app Play workaround, not the exact wire command.
- Static code review confirms the v5.0.10 fallback gap described above.
- `MCU+PLY-PLA` is documented in the KB's MCU command view as implemented/needs hardware evidence.
- The v5.0.11 change has not been exercised against an A97/H50 device. Do not label the result fixed or hardware-confirmed until the user tests playback and the native app state.
- The source changes do not modify hardware settings or other chip/API radio paths.

## Canonical references

- [A97 command view](../../devices/A97/COMMANDS.md) — playback support and fallback status.
- [MCU TCP :8899 command view](../../protocols/mcu-8899/COMMANDS.md)
- airControl implementation: `/Users/lab/AI/airControl/airControl-v5.0.11/`


## Follow-up correction — user test invalidates the v5.0.11 fallback, 2026-10-29

The user reports that v5.0.11 removed the red error banner but **radio playback still did not start**. This means the earlier TCP/8899 fallback's “accepted send” was not sufficient to start the URL stream on the user's H50. The source report above records the original implementation and is retained for provenance; its proposed fallback must not be described as a fix.

Arylic staff's H50 guidance explicitly says a URL cannot be started by TCP MCU alone and directs clients to UPnP `CreateQueue` and `PlayQueueWithIndex`. The corrected v5.0.12 candidate replaces the SetAVTransportURI/TCP-play route for UPnP-only radio with the Arylic PlayQueue flow. Details and source links: [corrected PlayQueue report](AIRCONTROL-A97-PLAYQUEUE-RADIO-CORRECTION-2026-10-29.md).

**Evidence status:** user-confirmed failure of the v5.0.11 fallback; Arylic forum-documented protocol guidance; v5.0.12 source implemented. v5.0.12 playback remains **NOT-HW-VERIFIED** until the user tests it on the H50.
