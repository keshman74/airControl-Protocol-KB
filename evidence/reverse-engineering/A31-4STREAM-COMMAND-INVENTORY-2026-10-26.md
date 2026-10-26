# A31 / 4STREAM command inventory

Status: **APK-VERIFIED / IMAGE-VERIFIED; NOT-HW-VERIFIED unless explicitly marked HW-VERIFIED**.

## Evidence

- Firmware: `a31rakoit-4.6.415156-b1-c3bddec5-20240816.bin`; extracted `home/bin/hdl`, SHA-256 `e627d10f72f494b1108212b5b3a46523c02865600948d7596d1c548805c595cd`.
- Live A31 at `192.168.0.192`, firmware `4.6.415156`, hardware `A31`: HTTP/UDP/TCP observations are **HW-VERIFIED** and recorded in `A31-RAKOIT-HDL-TCP-UDP-WIRE-2026-10-26.md`.
- 4STREAM APK SHA-256 `08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b`, package `com.wifiaudio.Stream`, version `3.1.20.230912`; JADX headless MCP 0.7.1. Static results below are **APK-VERIFIED**, not runtime proof.

## Firmware-visible network commands

### Local NETAPI (TCP/6666; JSON lines, CRLF)

The `hdl` API dispatch tables contain these `set` keys: `notify-usb-song`, `notify-url`, `usb-play`, `play-index`, `radio-play`, `play-control`, `play-mode`, `input`, `volume`, `treble`, `middle`, `bass`, `preset-play`.

The `get` table contains: `usb-disk`, `usb-playlists`, `usb-playlist`, `play-index`, `radio`, `play-mode`, `input`, `volume`, `treble`, `middle`, `bass`, `playlist`, `preset`, `name`, `device`.

Wire envelope emitted by `netapi_send_message`: {"key":"<key>","act":"set|get|info","val":<value>}\\r\\n. Worker accepts multiple JSON objects from a stream, grows a 4096-byte buffer, and rejects buffers over 128 KiB.

### Discovery / gateway transport

- UDP/6665: local discovery/HELLO service (`HELLO:<ip>:<model>` observed on A31).
- TCP/8888: WebSocket service created by `hdl` (static anchor `main` 0x004068f0–0x00406908).
- UDP/8585: gateway broadcast/monitor (static anchors `udp_broadcast` 0x0040e14c and `hdl_monitor_start` 0x0040f6b4). Broadcast payload is gateway discovery JSON.
- TCP/8586: gateway connection from `hdl_processing_start` (0x0040b0a8); framed as `Topic:%s\\r\\nLength:%d\\r\\n\\r\\n<body>\\r\\n`. Gateway body may be AES-128-CBC padded to 16 bytes; `Length` is ciphertext length.

Gateway topics/commands found in the image: `/user/`, `/custom/function/attribute/get`, `/custom/function/list/get_reply`, `/base/`, `/thing/property/down`, `/thing/property/up_reply`, `/thing/property/read`, `/thing/service/`, `/thing/topo/delete/notify`, `/vendor/user/hdl.cfg`, `all/custom/device/network_access/broadcast`, `all/custom/device/network_access/request_reply`, `all/custom/gateway/search`, `all/custom/gateway/broadcast_reply`, and service requests `MusicDeviceFind/down`, `MusicPlayerListGet/down`, `MusicPlayGroupListGet/down`, `MusicPlayListByGroupGet/down`.

## Firmware-visible UART / local IPC

- A31 status reports `uart_pass_port:8899` (**HW-VERIFIED** on 192.168.0.192).
- Firmware-side local MCU path uses the `lp_tcpapi_*` IPC helpers; the port is a local TCP pass-through, not a proven external UART electrical framing.
- Existing image strings and reports identify MCU command families (`SYS:`, `VOL:`, `MUT:`, `SRC:`, `NAM:`) and MCU/PLM control paths. Exact byte framing requires a UART capture; do not promote these families to hardware-confirmed commands.

## 4STREAM HTTP command strings (static APK)

The APK contains the Linkplay endpoint template `http://%s/httpapi.asp?command=...`. Exact command literals:

`getbtstatus`, `getbthistory`, `getbtpairstatus`, `getbtPairDevStat`, `getbtdiscoveryresult`, `startgetbtPairDevStat`, `clearbtdiscoveryresult`, `startbtdiscovery:%d`, `stopbtdiscovery`, `startbtserver:%d`, `stopbtserver:%d`, `connectbta2dpsynk:%s`, `disconnectbta2dpsynk:%s`, `wlanGetConnectState`, `getMvRomBurnPrecent`, `NotifyUpgradeType:firmware`, `EasyLinkResponseStop`.

The same APK embeds generic player command construction (`/httpapi.asp?command=`), and UPnP queue requests: `PlayQueue/CreateQueue,ip=<device>`, `PlayQueue/AppendTracksInQueueEx,ip=<device>`, and `PlayQueue/PlayQueueWithIndex,ip=<device>`.

## MCU/TCP helper classes in 4STREAM

JADX class anchors (APK-VERIFIED): `com.wifiaudio.utils.mcu.Socket8819CommThread` and `com.wifiaudio.utils.mcu.lumisound.SocketCommThread`. `Socket8819CommThread.<init>(String host,String peer,int port)` stores host/port; method `i()` executes `new Socket(this.h,this.i)`, applies a read timeout, then starts an inner reader with `new TCP8819Item()`. This proves a TCP MCU transport abstraction, but the actual A31 port and command bytes are supplied at runtime and are not constants in this class.

## Safety / confidence

No existing hardware-confirmed KB facts are changed by this inventory. Static APK strings and decompiled method bodies are not proof that every command is sent on A31/A97/A98. A97/A98-specific APK binaries were not present in the supplied filesystem inventory; their rows remain unverified until exact APKs are supplied.
