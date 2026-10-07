# A31 / Arylic UART API

Source: official Arylic UART API.

## Physical connection rules
- **115200 baud**
- **8 data bits**
- **no parity**
- **1 stop bit**
- **no flow control**
- UART messages sent by the host terminate with **semicolon `;`**
- three-character message identifiers; `:` separates parts
- messages may arrive without a query when state changes
- command without parameter normally queries state or performs direct control
- command with parameter normally changes state
- received messages normally contain the current state as parameter

## TCP evaluation bridge
Arylic states that most UART messages can also be evaluated over the TCP API on supported BP10XX platforms. Raw UART message is wrapped as:

`MCU+PAS+RAKOIT:{uart_message}&`

Example: UART `VOL:50` → TCP payload `MCU+PAS+RAKOIT:VOL:50&`.

This bridge is model/platform dependent and must not be confused with direct physical UART.

## Canonical commands
- `QRY-A31-UART-STA` — **device status** — `STA` → `STA:{states}` — states=current source,mute,volume,treble,bass,net,internet,playing,led,upgrading
- `CMD-A31-UART-SYS` — **system** — `SYS:{REBOOT|STANDBY|RESET}` → `(no documented response)` — STANDBY may not wake via UART on some models
- `QRY-A31-UART-WWW` — **internet** — `WWW` → `WWW:{0|1}` — also asynchronous on state change
- `CMD-A31-UART-NAM` — **device name** — `NAM[:{hextext}]` → `NAM:{hextext}` — UTF-8 text hex encoded
- `QRY-A31-UART-ETH` — **ethernet** — `ETH` → `ETH:{0|1}` — also asynchronous on state change
- `QRY-A31-UART-WIF` — **wifi** — `WIF` → `WIF:{0|1}` — also asynchronous on state change
- `CMD-A31-UART-WRS` — **wifi setup** — `WRS` → `(no documented response)` — enter Wi-Fi configuration mode
- `QRY-A31-UART-WSS` — **wifi RSSI** — `WSS` → `WSS:{rssi}` — proactive query
- `QRY-A31-UART-BSS` — **bluetooth RSSI** — `BSS` → `BSS:{rssi}` — not working on all models
- `QRY-A31-UART-IPA` — **IP address** — `IPA` → `IPA:{ip}` — also asynchronous on state change
- `QRY-A31-UART-TME` — **local time** — `TME` → `TME:{time}` — proactive query
- `CMD-A31-UART-COE` — **bluetooth PIN protection** — `COE[:{onoff}]` → `COE:{onoff}` — device reboots when executed
- `CMD-A31-UART-COD` — **bluetooth PIN** — `COD[:{pin}]` → `COD:{pin}` — default 0000
- `CMD-A31-UART-SRC` — **source** — `SRC[:{source}]` → `SRC:{source}` — NET/BT/USBDAC/LINE-IN/OPT/COAX/LINE-IN2/OPT2/COAX2/HDMI
- `CMD-A31-UART-POP` — **playback toggle** — `POP` → `(no documented response)` — network playback and Bluetooth
- `CMD-A31-UART-STP` — **stop** — `STP` → `(no documented response)` — network playback only
- `CMD-A31-UART-NXT` — **next** — `NXT` → `(no documented response)` — network playback and Bluetooth
- `CMD-A31-UART-PRE` — **previous** — `PRE` → `(no documented response)` — network playback and Bluetooth
- `CMD-A31-UART-PST` — **preset playback** — `PST:{preset}` → `(no documented response)` — start preset playlist
- `CMD-A31-UART-LPM` — **loop/shuffle** — `LPM[:{loopmode}]` → `LPM:{loopmode}` — REPEATALL/REPEATONE/REPEATSHUFFLE/SHUFFLE/SEQUENCE
- `CMD-A31-UART-BTC` — **bluetooth connection** — `BTC[:{onoff}]` → `(no documented response)` — disconnect/reconnect Bluetooth
- `QRY-A31-UART-PLA` — **playing state** — `PLA` → `PLA:{onoff}` — network playing state
- `QRY-A31-UART-CHN` — **multiroom channel** — `CHN` → `CHN:{S|L|R}` — query only; cannot set via API
- `QRY-A31-UART-MRM` — **multiroom mode** — `MRM` → `MRM:{S|M|N}` — slave/master/normal; query only
- `EVT-A31-UART-TIT` — **metadata title** — `TIT` → `TIT:{hextext}` — notification; documented not to work when sent in TCP
- `EVT-A31-UART-ART` — **metadata artist** — `ART` → `ART:{hextext}` — notification; documented not to work when sent in TCP
- `EVT-A31-UART-ALB` — **metadata album** — `ALB` → `ALB:{hextext}` — notification; documented not to work when sent in TCP
- `EVT-A31-UART-VND` — **metadata vendor** — `VND` → `VND:{vendor}` — spotify/qplay/dlna/airplay/upnp/phone/usb/tidal/napster/qobuz/amazon/tunein/iheart/vtuner/http/other; not TCP
- `EVT-A31-UART-ELP` — **elapsed/duration** — `ELP` → `ELP:{elapsed}/{duration}` — milliseconds; notification; not TCP
- `QRY-A31-UART-PLI` — **playlist info** — `PLI` → `PLI:{index}/{count}` — index starts at 1
- `CMD-A31-UART-APL` — **autoplay** — `APL[:{onoff}]` → `APL:{onoff}` — play last playlist on boot
- `CMD-A31-UART-AUD` — **audio output** — `AUD[:{onoff}]` → `AUD:{onoff}` — set/get audio output
- `CMD-A31-UART-VOL` — **volume** — `VOL[:{volume}]` → `VOL:{volume}` — set/get master volume
- `CMD-A31-UART-MUT` — **mute** — `MUT[:{onoff}]` → `MUT:{onoff}` — set/get mute
- `CMD-A31-UART-BAS` — **bass** — `BAS[:{tone}]` → `BAS:{tone}` — -10..10 dB
- `CMD-A31-UART-TRE` — **treble** — `TRE[:{tone}]` → `TRE:{tone}` — set/get treble
- `CMD-A31-UART-MID` — **mid** — `MID[:{tone}]` → `MID:{tone}` — set/get middle tone
- `CMD-A31-UART-VBS` — **virtual bass** — `VBS[:{onoff}]` → `VBS:{onoff}` — set/get virtual bass
- `CMD-A31-UART-BAL` — **balance** — `BAL[:{balance}]` → `BAL:{balance}` — -100..100; stereo only
- `CMD-A31-UART-VOF` — **fixed volume** — `VOF[:{volume}]` → `VOF:{volume}` — 0 disables; 1..100 fixed output
- `CMD-A31-UART-VOG` — **group volume** — `VOG[:{volume}]` → `VOG:{volume}` — grouped/multiroom playback volume
- `QRY-A31-UART-PEQ` — **EQ groups** — `PEQ` → `PEQ:{eqlist}` — index@name comma-separated
- `CMD-A31-UART-EQS` — **EQ group** — `EQS[:{eqidx}]` → `EQS:{eqidx}` — get/set EQ group
- `CMD-A31-UART-VST` — **volume step** — `VST[:{step}]` → `VST:{step}` — 0..10
- `CMD-A31-UART-EQE` — **EQ enable** — `EQE[:{onoff}]` → `EQE:{onoff}` — enable/disable EQ
- `CMD-A31-UART-CFE` — **crossfilter** — `CFE[:{onoff}]` → `CFE:{onoff}` — HPF stereo + LPF DAC-X
- `CMD-A31-UART-CFF` — **crossfilter frequency** — `CFF[:{cffreq}]` → `CFF:{cffreq}` — 50..300
- `QRY-A31-UART-VER` — **firmware/API version** — `VER` → `VER:{version}` — version-shortgit-APIlevel
- `CMD-A31-UART-LED` — **LED/display** — `LED[:{onoff}]` → `LED:{onoff}` — set/get
- `CMD-A31-UART-BEP` — **beep** — `BEP[:{onoff}]` → `BEP:{onoff}` — key press beep
- `CMD-A31-UART-PMT` — **prompt voice** — `PMT[:{onoff}]` → `PMT:{onoff}` — device reboots on command
- `CMD-A31-UART-DLY` — **auto-mute delay** — `DLY[:{mute_delay}]` → `DLY:{mute_delay}` — 0..32767
- `CMD-A31-UART-MXV` — **max volume** — `MXV[:{volume}]` → `MXV:{volume}` — 30..100
- `CMD-A31-UART-ASW` — **auto source switch** — `ASW[:{onoff}]` → `ASW:{onoff}` — return previous input when connection lost
- `CMD-A31-UART-POM` — **power-on source** — `POM[:{source}]` → `POM:{source}` — set/get power-on mode
- `CMD-A31-UART-VOS` — **multiroom volume sync** — `VOS:{onoff}` → `VOS:{onoff}` — sync master button/remote volume changes to slaves
- `QRY-A31-UART-LST` — **available sources** — `LST` → `LST:{sources}` — comma-separated supported sources
- `CMD-A31-UART-SOP` — **standby on power** — `SOP:{onoff}` → `SOP:{onoff}` — enter standby when power supplied

## Asynchronous feedback
The official API explicitly says state messages may be pushed without a preceding query. In particular WWW, ETH, WIF and IPA can be sent on state changes, while TIT/ART/ALB/VND/ELP are playback metadata/progress notifications.

## Scope
Commands have API-version levels in the vendor table and availability varies by firmware/model. Newly imported records are documentary evidence only until tested on our A31 hardware.
