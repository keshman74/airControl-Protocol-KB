# A97 Command View

- `CMD-LP-PLAY` — **playback** — `setPlayerCmd:play:<URL>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PLAYLIST` — **playback** — `setPlayerCmd:playlist:<songid>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PAUSE` — **playback** — `setPlayerCmd:pause` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-RESUME` — **playback** — `setPlayerCmd:resume` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-TOGGLE` — **playback** — `setPlayerCmd:onepause` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-PREV` — **playback** — `setPlayerCmd:prev` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-NEXT` — **playback** — `setPlayerCmd:next` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-POSITION` — **playback** — `setPlayerCmd:getplay:<seconds>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-SEEK` — **playback** — `setPlayerCmd:setplay:<seconds>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-STOP` — **playback** — `setPlayerCmd:stop` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-VOL-UP` — **volume** — `setPlayerCmd:RemoteVol++` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-VOL-DOWN` — **volume** — `setPlayerCmd:RemoteVol--` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-MAX-VOL` — **volume** — `setPlayerCmd:maximumVolume:<value>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-CHANNEL` — **playback** — `setChannel:<channel>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-LOOP` — **playback** — `setPlayerCmd:loopmode:<loopmode>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-REBOOT` — **system** — `reboot` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-FACTORY` — **system** — `factory` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-SHUTDOWN` — **system** — `shutdown` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-WIFI-STATE` — **network** — `wlanGetConnectState` — **DOCUMENTED/IMPLEMENTED**
- `QRY-LP-SCAN-APS` — **network** — `getScanAPs` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-CONNECT-AP` — **network** — `connectToAP:<wifiName>:<wifiPassword>` — **DOCUMENTED/IMPLEMENTED**
- `CMD-LP-MR-JOIN` — **multiroom** — `multiroom:JoinGroup:IP=<MASTER_IP>:uuid=<MASTER_UUID>` — **CONFIRMED-A97**
- `CMD-LP-MR-LEAVE` — **multiroom** — `multiroom:LeaveGroup` — **CONFIRMED-A97**
- `QRY-LP-MR-SLAVES` — **multiroom** — `multiroom:getSlaveList` — **DOCUMENTED**
- `CMD-LP-MR-UNGROUP` — **multiroom** — `multiroom:Ungroup` — **DOCUMENTED**
- `CMD-LP-MR-KICK` — **multiroom** — `multiroom:SlaveKickout:<ip>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-VOL` — **multiroom** — `multiroom:SlaveVolume:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-MUTE` — **multiroom** — `multiroom:SlaveMute:<...>` — **DOCUMENTED**
- `CMD-LP-MR-SLAVE-CHANNEL` — **multiroom** — `multiroom:SlaveChannel:<...>` — **DOCUMENTED**


## Origin-chat audit additions
- `RULE-LP-TRANSPORT-BY-HARDWARE` — A97/R328 uses Linkplay HTTPS :443 in the verified airControl transport map; plain HTTP tests are avoided for this classified family — **IMPLEMENTED / HARDWARE-OBSERVED**
- `RULE-LP-MR-ROLE-PARSING` — native group role is resolved from device topology using `master_ip` / `master_uuid` — **IMPLEMENTED / OBSERVED-IN-APP**


## WiiM HTTP API OpenAPI v1.2.0 candidate surface
Source: cvdlinden/wiim-httpapi OpenAPI v1.2.0. These entries are imported as **SOURCE-DOCUMENTED / NOT-HW-VERIFIED** for this chip family. The source itself warns that support varies by WiiM model, brand and firmware. Existing stronger hardware evidence remains authoritative. Full parameter/response audit: `protocols/wiim-httpapi/OPENAPI-V1.2.0-COMPLETE.md`.

- **Device information (1)**: `QRY-WIIM-GET-DEBUG-INFO`
- **Playback control (2)**: `CMD-WIIM-SET-PLAYER-CMD-HEX-PLAYLIST-URL`, `CMD-WIIM-SET-PLAYER-CMD-SEEK-POSITION`
- **Network (28)**: `QRY-WIIM-GET-STATIC-IP-INFO`, `CMD-WIIM-SET-WLAN-STATIC-IP`, `CMD-WIIM-SET-ETH-STATIC-IP`, `CMD-WIIM-SET-SSID`, `CMD-WIIM-SET-NETWORK`, `QRY-WIIM-GET-NETWORK-PREFER-DNS`, `QRY-WIIM-GET-WLAN-BAND-CONFIG`, `QRY-WIIM-GET-WLAN-ROAM-CONFIG`, `QRY-WIIM-GET-IPV6ENABLE`, `CMD-WIIM-SET-POWER-WIFI-DOWN`, `CMD-WIIM-WLAN-CONNECT-HIDE-AP`, `CMD-WIIM-WLAN-CONNECT-HIDE-AP-EX`, `QRY-WIIM-GET-NETWORK`, `QRY-WIIM-WLAN-GET-AP-LIST-EX`, `CMD-WIIM-SET-HIDE-SSID`, `CMD-WIIM-SET-NETWORK-EX-AES`, `CMD-WIIM-SET-WLAN-BAND-CONFIG`, `CMD-WIIM-SET-WLAN-CONNECT-DISABLE`, `CMD-WIIM-SET-WLAN-ROAM-CONFIG`, `CMD-WIIM-SET-NETWORK-PREFER-DNS`, `QRY-WIIM-WLAN-GET-AP-FULL-LIST`, `CMD-WIIM-WLAN-SWITCH-CONNECTED-AP`, `CMD-WIIM-SET-IPV6ENABLE`, `QRY-WIIM-GET-WLAN-CONNECT-DISABLE-STATUS`, `QRY-WIIM-GET-NETWORK-HEALTH`, `CMD-WIIM-WPSCANNEL`, `CMD-WIIM-WPSCLIENTMODE`, `CMD-WIIM-WPSSERVERMODE`
- **Equalizer (30)**: `CMD-WIIM-SET-EQON`, `CMD-WIIM-SET-EQOFF`, `QRY-WIIM-GET-EQSTAT`, `QRY-WIIM-GET-EQLIST`, `QRY-WIIM-GET-EQBAND`, `CMD-WIIM-LOAD-EQBY-NAME`, `CMD-WIIM-EQ-SET-BASS`, `CMD-WIIM-EQ-SET-TREBLE`, `CMD-WIIM-EQ-DISABLE`, `CMD-WIIM-EQ-SET-BAND`, `CMD-WIIM-EQ-SET-LV2BAND`, `CMD-WIIM-EQ-SET-LV2SOURCE-BAND`, `CMD-WIIM-EQV2DELETE`, `CMD-WIIM-EQV2RENAME`, `CMD-WIIM-EQ-CHANGE-SOURCE-FX`, `CMD-WIIM-EQ-CHANGE-FX`, `QRY-WIIM-EQ-GET-LV2BAND`, `QRY-WIIM-EQ-GET-LV2SOURCE-BAND`, `QRY-WIIM-EQ-GET-LV2SOURCE-BAND-EX`, `QRY-WIIM-EQV2GET-LIST`, `QRY-WIIM-EQV2GET-NEW-LIST`, `CMD-WIIM-EQV2LOAD`, `CMD-WIIM-EQV2SOURCE-LOAD`, `CMD-WIIM-EQ-SOURCE-OFF`, `CMD-WIIM-EQ-SET-CHANNEL-MODE`, `CMD-WIIM-EQ-SOURCE-SAVE`, `CMD-WIIM-EQ-SAVE`, `QRY-WIIM-EQ-GET-LV2BAND-EX`, `QRY-WIIM-EQ-GET-SOURCE-MODES`, `CMD-WIIM-EQ-SAVE-CUSTOM`
- **Device control (12)**: `CMD-WIIM-SET-SHUTDOWN-TIMER`, `QRY-WIIM-GET-SHUTDOWN-TIMER`, `CMD-WIIM-SET-LED-SWITCH`, `CMD-WIIM-SET-TOUCH-CONTROLS`, `QRY-WIIM-BUTTON-ENABLE-GET`, `QRY-WIIM-GET-FIRMWARE-VERSION`, `QRY-WIIM-GET-DEVICE-NAME-CHANGEABLE`, `CMD-WIIM-RESTORE-TO-DEFAULT`, `QRY-WIIM-GETSYSLOG`, `CMD-WIIM-SET-HEX-DEVICE-NAME`, `CMD-WIIM-NO-SEND-MORE-DEVICE-EVENT`, `QRY-WIIM-GET-HW-ERROR-INFO`
- **Alarm clock (4)**: `QRY-WIIM-SET-TIME-SYNC`, `CMD-WIIM-SET-ALARM-CLOCK`, `QRY-WIIM-GET-ALARM-CLOCK`, `CMD-WIIM-STOP-ALARM-CLOCK`
- **Presets (1)**: `QRY-WIIM-GET-PRESET-INFO`
- **Audio output control (8)**: `QRY-WIIM-GET-NEW-AUDIO-OUTPUT-HARDWARE-MODE`, `CMD-WIIM-SET-AUDIO-OUTPUT-HARDWARE-MODE`, `QRY-WIIM-GET-SPDIF-OUT-SWITCH-DELAY-MS`, `CMD-WIIM-SET-SPDIF-OUT-SWITCH-DELAY-MS`, `QRY-WIIM-GET-CHANNEL-BALANCE`, `CMD-WIIM-SET-CHANNEL-BALANCE`, `QRY-WIIM-GET-FADE-FEATURE`, `CMD-WIIM-SET-FADE-FEATURE`
- **Bluetooth (23)**: `CMD-WIIM-START-BT-DISCOVERY`, `QRY-WIIM-GET-BT-DISCOVERY-RESULT`, `CMD-WIIM-CLEAR-BT-DISCOVERY-RESULT`, `QRY-WIIM-GET-BT-HISTORY`, `CMD-WIIM-CONNECT-BT-A2DPSYNK`, `CMD-WIIM-DISCONNECT-BT-A2DPSYNK`, `QRY-WIIM-GET-BT-PAIR-STATUS`, `CMD-WIIM-CONNECTBTA2DPSOURCE`, `CMD-WIIM-DELBTHISTORY`, `CMD-WIIM-BTDISCONNECTALL`, `QRY-WIIM-GETBT-PAIR-DEV-STAT`, `QRY-WIIM-GETBTSTATUS`, `CMD-WIIM-STARTBTSERVER`, `CMD-WIIM-STARTGETBT-PAIR-DEV-STAT`, `CMD-WIIM-STOPBTDISCOVERY`, `CMD-WIIM-STOPBTSERVER`, `CMD-WIIM-BTAVKENTERPAIR`, `CMD-WIIM-BLEHIDPAIR`, `CMD-WIIM-BLEHIDREMOVEALL`, `CMD-WIIM-BTRECOVERY`, `QRY-WIIM-GET-BLE-HID-STATUS`, `CMD-WIIM-START-BLE-SCAN`, `QRY-WIIM-GET-BLE-DISCOVERY-RESULT`
- **Room correction (6)**: `QRY-WIIM-ROOM-CORR-GET`, `QRY-WIIM-ROOM-CORR-GET-MODE`, `CMD-WIIM-ROOM-CORR-SET`, `CMD-WIIM-ROOM-CORR-SET-LR`, `CMD-WIIM-ROOM-CORR-SET-MODE`, `CMD-WIIM-SET-ROOM-CORRECTION`
- **Alexa (11)**: `CMD-WIIM-ALEXA-ENABLE-BETA-ID`, `QRY-WIIM-GET-ALEXA-PROFILE`, `CMD-WIIM-ALEXA-LOG-OUT`, `QRY-WIIM-GET-ALEXA-COUNTRY`, `QRY-WIIM-ALEXA-LANGUAGE-LIST-GET`, `QRY-WIIM-ALEXA-GET-LANGUAGE`, `CMD-WIIM-SET-ALEXA-COUNTRY`, `CMD-WIIM-ALEXA-SET-LANGUAGE`, `QRY-WIIM-GET-AVS-DEV-INFO`, `QRY-WIIM-GET-AVS-MUSIC-HDENABLE`, `CMD-WIIM-SET-AVS-MUSIC-HDENABLE`
- **Amazon music (7)**: `CMD-WIIM-SET-AMAZON-ACCESS-TOKEN`, `CMD-WIIM-ENABLE-AMAZON-ATMOS`, `CMD-WIIM-ENABLE-AMAZON-HD`, `QRY-WIIM-GET-AMAZON-HD`, `QRY-WIIM-GET-AMAZON-CONFIG`, `CMD-WIIM-SET-AMAZON-MUSIC-PARAMS`, `CMD-WIIM-SET-PRIME-TOKEN`
- **Multiroom (20)**: `CMD-WIIM-MULTIROOM-SLAVE-MASK`, `CMD-WIIM-MULTIROOM-SLAVE-UN-MASK`, `CMD-WIIM-SET-PLAYER-CMD-SLAVE-VOLUME`, `CMD-WIIM-SET-PLAYER-CMD-SLAVE-MUTE`, `CMD-WIIM-SET-PLAYER-CMD-SLAVE-UNMUTE`, `CMD-WIIM-MULTIROOM-SLAVE-SET-DEVICE-NAME`, `QRY-WIIM-MULTIROOM-CONFIG-GET-REALTIME-CACHE-LIMIT`, `CMD-WIIM-MULTIROOM-CONFIG-SET-REALTIME-CACHE-LIMIT`, `CMD-WIIM-MULTIROOM-SLAVE-START-WPS`, `QRY-WIIM-MULTIROOM-GET-NAME-GROUP-LIST`, `CMD-WIIM-MULTIROOM-SLAVE-DEVICE-NAME`, `CMD-WIIM-MULTIROOM-SUBWOOFER-FORGET`, `CMD-WIIM-MULTIROOM-SUBWOOFER-GET-PAIR-INFO`, `CMD-WIIM-MULTIROOM-CONFIG-GET-LEADTIME`, `CMD-WIIM-MULTIROOM-SUBWOOFER-PAIR`, `CMD-WIIM-MULTIROOM-CONFIG-SET-LEADTIME`, `CMD-WIIM-SET-MRMSUB-LPF`, `QRY-WIIM-GET-SUB-LPF`, `CMD-WIIM-SET-SUB-LPF`, `QRY-WIIM-GET-MRMSUB-LPF`
- **Other (156)**: `QRY-WIIM-GET-REMOTE-VOLUME-STEP`, `CMD-WIIM-SET-REMOTE-VOLUME-STEP`, `QRY-WIIM-GET-MV-REMOTE-SILENCE-UPDATE-TIME`, `QRY-WIIM-GET-SPDIF-OUT-MAX-CAP`, `QRY-WIIM-GET-COAX-OUT-MAX-CAP`, `QRY-WIIM-GET-AUX-VOLTAGE-SUPPORT-LIST`, `CMD-WIIM-AUDIO-CAST-GET-SPEAKER-LIST`, `CMD-WIIM-AUDIO-CAST-SCAN-SPEAKER`, `CMD-WIIM-AUDIO-CAST-SPEAKER-GET-TRANSCODE-BUFFER-TIME`, `CMD-WIIM-AUDIO-CAST-SPEAKER-GET-TRANSCODE-PROFILE`, `CMD-WIIM-AUDIO-CAST-SPEAKER-SET-PASSWORD`, `CMD-WIIM-AUDIO-CAST-SPEAKER-SET-VOLUME`, `QRY-WIIM-GET-SOUND-CARD-MODE-SUPPORT-LIST`, `QRY-WIIM-GET-ACTIVE-SOUND-CARD-OUTPUT-MODE`, `CMD-WIIM-SET-LIGHT-OPERATION-BRIGHT-CONFIG`, `QRY-WIIM-GET-MV-REMOTE-UPDATE-START-CHECK`, `QRY-WIIM-GET-MV-REMOTE-UPDATE-START`, `QRY-WIIM-GET-MV-REMOTE-UPDATE-STATUS`, `QRY-WIIM-GET-MV-ROM-BURN-PRECENT`, `CMD-WIIM-EASY-LINK-RESPONSE-STOP`, `CMD-WIIM-NOTIFY-UPGRADE-TYPE-FIRMWARE`, `QRY-WIIM-GET-LMPFILTER-CAPABILITY`, `QRY-WIIM-GET-STREAM-SERVICE-CONFIG`, `CMD-WIIM-SET-HANDSHAKE-CODE`, `QRY-WIIM-GETSYSLOG-IP`, `QRY-WIIM-GET-STATUS-IP`, `QRY-WIIM-GET-WEATHER-INFO`, `CMD-WIIM-SET-ACCESS-PIN`, `CMD-WIIM-SET-LANGUAGE`, `CMD-WIIM-AUTO-PLAY-SET`, `QRY-WIIM-GET-MV-ROM-DOWNLOAD-STATUS`, `QRY-WIIM-GET-MV-ROM-DOWNLOAD-V2STATUS`, `CMD-WIIM-SET-HEX-GROUP-NAME`, `CMD-WIIM-SET-MV-REMOTE-SILENCE-OTATIME`, `QRY-WIIM-CHECK-ACCESS-PIN`, `CMD-WIIM-SET-WEATHER-LOCATION`, `CMD-WIIM-START-CHECK`, `QRY-WIIM-GETBATTERYVAL`, `QRY-WIIM-GET-ASR-STATUS`, `QRY-WIIM-GET-LPAUTH-CODE`, `CMD-WIIM-SET-TOKEN-PARAMS`, `CMD-WIIM-TALKSET-PROMPT`, `CMD-WIIM-TALKSET-ALARM-PRE-WAKE`, `CMD-WIIM-TALKSET-ALARM-TONE`, `CMD-WIIM-TALKSET-ALARM-TONE-PREVIEW`, `CMD-WIIM-TALKSET-ALARM-VOLUME`, `CMD-WIIM-TALKSET-ALARMCOMMON`, `CMD-WIIM-SET-SYNC-PLAY-EXTRA-DELAY`, `CMD-WIIM-SET-INITIAL-CONFIGURATION`, `QRY-WIIM-GET-UI-CONFIG`, `QRY-WIIM-GET-SPDIF-AUTO-SENSE-ENABLE`, `QRY-WIIM-GET-SPDIF-IN-NOISE-REMOVE`, `CMD-WIIM-PHONO-MODE-SWITCH-SET`, `CMD-WIIM-SET-PLAY-MODE-VOLUME-ENABLE`, `QRY-WIIM-GET-UI-WALLPAPER-LIST`, `CMD-WIIM-SET-PLAY-MODE-VOLUME-VALUE`, `CMD-WIIM-SET-POWER-MODE-TIME`, `QRY-WIIM-GET-BUTTON-VOLUME-STEP`, `CMD-WIIM-SET-BUTTON-VOLUME-STEP`, `QRY-WIIM-GET-AUX-AUTO-SENSE-ENABLE`, `CMD-WIIM-SET-UI-CONFIG`, `CMD-WIIM-SET-SPDIF-AUTO-SENSE-ENABLE`, `CMD-WIIM-SET-SPDIF-IN-NOISE-REMOVE`, `QRY-WIIM-GET-CHANNEL-MODE`, `QRY-WIIM-GET-AUTO-SENSE-ENABLE`, `CMD-WIIM-START-REBOOT-TIME`, `QRY-WIIM-LED-SWITCH-GET`, `QRY-WIIM-GET-MQARECEIVER-CAP`, `CMD-WIIM-RELOAD-BUTTON-GET`, `CMD-WIIM-SET-AUX-AUTO-SENSE-ENABLE`, `QRY-WIIM-GET-LOW-PRIORITY-PROMPT-DISABLE`, `QRY-WIIM-GET-SOFT-MUTE`, `QRY-WIIM-GET-LINE-IN-MAX-CAP`, `QRY-WIIM-GET-AUX-IN-MAX-CAP`, `QRY-WIIM-GET-UAC-OUT-MAX-CAP`, `QRY-WIIM-GET-HDMIAUTO-SENSE-ENABLE`, `CMD-WIIM-SET-CHANNEL-MODE`, `QRY-WIIM-GET-SYNC-PLAY-EXTRA-DELAY`, `QRY-WIIM-GET-LIGHT-OPERATION-BRIGHT-CONFIG`, `CMD-WIIM-SET-UI-WALLPAPER-LIST`, `QRY-WIIM-GET-MAIN-SUB-EXTRA-DELAY`, `CMD-WIIM-CAST-DISABLE`, `CMD-WIIM-CAST-DISABLE-USAGE-REPORT`, `CMD-WIIM-SET-AUTO-SENSE-ENABLE`, `QRY-WIIM-PHONO-MODE-SWITCH-GET`, `QRY-WIIM-GET-PLAY-MODE-VOLUME-ENABLE`, `CMD-WIIM-SET-VOLUME-CONTROL`, `QRY-WIIM-GET-PLAY-MODE-VOLUME-VALUE`, `CMD-WIIM-SET-MQARECEIVER-CAP`, `QRY-WIIM-GET-POWER-MODE-TIME`, `CMD-WIIM-SET-MAX-VOLUME`, `CMD-WIIM-ENABLE-CAST`, `CMD-WIIM-RELOAD-BUTTON-UPDATE`, `CMD-WIIM-ENABLE-CAST-USAGE-REPORT`, `CMD-WIIM-DISABLE-LOW-PRIORITY-PROMPT`, `CMD-WIIM-SET-SOFT-MUTE`, `CMD-WIIM-SET-HDMIAUTO-SENSE-ENABLE`, `CMD-WIIM-SET-SPDIF-OUT-MAX-CAP`, `CMD-WIIM-SET-COAX-OUT-MAX-CAP`, `CMD-WIIM-SET-LINE-IN-MAX-CAP`, `CMD-WIIM-SET-AUX-IN-MAX-CAP`, `CMD-WIIM-SET-UAC-OUT-MAX-CAP`, `CMD-WIIM-ENABLE-SYS-INFO`, `QRY-WIIM-GET-AIRPLAY-EXTRA-DELAY`, `QRY-WIIM-GET-CURRENT-WIRELESS-CONNECT`, `CMD-WIIM-SLAVE-ALERT-GET`, `CMD-WIIM-SLAVE-TALK-SET-ALARM-VOLUME`, `CMD-WIIM-SQUEEZELITE-AUTO-CONNECT-ENABLE`, `CMD-WIIM-SQUEEZELITE-CONNECT-SERVER`, `CMD-WIIM-SQUEEZELITE-DISCOVER`, `CMD-WIIM-SQUEEZELITE-GET-STATE`, `QRY-WIIM-GET-SETUP-ROUTER-INFO`, `CMD-WIIM-SET-SETUP-ROUTER-INFO`, `CMD-WIIM-ALERT-GET`, `CMD-WIIM-TVS-LOGOUT`, `QRY-WIIM-GET-TVS-STATE`, `QRY-WIIM-GET-TVS-DEV-INFO`, `CMD-WIIM-SET-TVSACCESS-TOKEN`, `CMD-WIIM-SET-TVSDEBUG-MODE`, `CMD-WIIM-SET-TVS-CLIENT-ID`, `CMD-WIIM-CREATE-ROUTINE`, `QRY-WIIM-GET-ALL-ROUTINES`, `QRY-WIIM-GET-ROUTINE-CAPABILITY`, `QRY-WIIM-GET-AUDIO-INPUT-CAPABILITY`, `QRY-WIIM-GET-AUDIO-OUT-MAX32BIT`, `CMD-WIIM-SET-AUDIO-OUT-MAX32BIT`, `QRY-WIIM-GET-AUDIO-OUTPUT-VRMS`, `QRY-WIIM-GET-AUDIO-OUTPUT-VRMS-SUPPORT-LIST`, `CMD-WIIM-SET-AUDIO-OUTPUT-VRMS`, `QRY-WIIM-GET-CBLSTATUS`, `QRY-WIIM-GET-CEC-POWER-CTRL`, `CMD-WIIM-SET-CEC-POWER-CTRL`, `QRY-WIIM-GET-CXDISH-PRECENT`, `QRY-WIIM-GET-DIGITAL-FILTER-TYPE-SUPPORT-LIST`, `QRY-WIIM-GET-DIGITAL-FILTER-TYPE`, `CMD-WIIM-SET-DIGITAL-FILTER-TYPE`, `QRY-WIIM-GET-OUTPUT-DIGITAL-FILTER-TYPE`, `QRY-WIIM-GET-OUTPUT-DIGITAL-FILTER-TYPE-SUPPORT-LIST`, `CMD-WIIM-SET-OUTPUT-DIGITAL-FILTER-TYPE`, `QRY-WIIM-GET-DIGITAL-INPUT-AUDIO-TYPE-SUPPORT`, `QRY-WIIM-GET-OUTPUT-VOLTAGE`, `CMD-WIIM-SET-OUTPUT-VOLTAGE`, `QRY-WIIM-GET-FEATURE-CAPABILITY`, `QRY-WIIM-GET-PLAY-MODE-GAIN-CONFIG`, `CMD-WIIM-SET-PLAY-MODE-GAIN-CONFIG`, `CMD-WIIM-MEDIASERVER-SCAN`, `CMD-WIIM-MEDIASERVER-UDISKUMOUNT`, `QRY-WIIM-GET-INPUT-MODE-SUPPORT-LIST`, `QRY-WIIM-GET-MODE-RENAME`, `CMD-WIIM-SET-MODE-RENAME`, `CMD-WIIM-SET-MUSIC-EXPLICIT`, `QRY-WIIM-GET-MV-REMOTE-UPDATE-DEVICE-OTA-INFO`, `CMD-WIIM-SET-TUNEIN-FAVORITE-STATE`, `CMD-WIIM-SET-TUNEIN-LOCATION`, `CMD-WIIM-SET-TUNEIN-TOKEN`, `CMD-WIIM-TIDAL-LOGIN`


## AudioCast interoperability candidate
WiiM-source AudioCast commands are candidate functionality for A97. User observation from the native WiiM app indicates AudioCast is presented as audio transmission to compatible UPnP/DLNA devices. The OpenAPI does not itself identify the target protocol, and A97 hardware support is not yet verified. Preserve this as a test candidate for possible DLNA/UPnP bridging to otherwise incompatible multiroom families (including A33), not as confirmed compatibility.

## getPresetInfo — negative hardware result, 2026-10-20

Status: **HARDWARE-OBSERVED UNSUPPORTED on the tested A97-labelled device**.
Selected zone: Кухня,192.168.0.99, HTTPS443; device firmware/version was not supplied in this sample.
A direct curl -k HTTPS /httpapi.asp?command=getPresetInfo returned literal unknown command with HTTP200. KNOB0.8.20 health independently reported preset_http200, preset_bytes15, preset_error=http_or_body, and the user confirmed the list does not appear.

This negative result overrides the source-documented WiiM command candidate for this tested product/firmware. HTTP200 is not API success. Do not claim all A97 products support getPresetInfo merely because WiiM API documentation lists it. Launch MCUKeyShortClick:N has not been tested by this result.

Next read-only candidate: discover the advertised PlayQueue service through the device description/SCPD and, only if advertised, test GetKeyMapping. Do not assume A31 port49152, A98 port59152, returned mapping semantics, or A98 routine/active-state support for A97 until observed. The currently failing read used the correct selected HTTPS endpoint; switching blindly to HTTPS is not a fix.


## A97 PlayQueue preset read — confirmed 2026-10-20
**HARDWARE CONFIRMED on tested A97 Кухня192.168.0.99:** GetKeyMapping succeeds over HTTP on both49152 and59152,3538-byte responses, MaxNumber21, six named Key1..Key6 records. HTTPS443 getPresetInfo is rejected as unknown command. The initial read experiment did not test launch. Subsequent KNOB0.8.21 testing confirmed that preset names display and selections start playback using HTTPS443 `MCUKeyShortClick:N`; user confirmation: «работает! Прессеты отображаются и запускаются!». Individual tested slots were not enumerated. Active-slot tracking remains unverified. Canonical response details, request and limits: [A97-PRESETS.md](../../protocols/upnp/playqueue/A97-PRESETS.md).

## A97 RenderingControl volume — tested 2026-10-20
On Кухня192.168.0.99, HTTP49152 /upnp/control/rendercontrol1:
- GetVolume(InstanceID0,ChannelMaster) succeeds;12/23/15ms from Mac,CurrentVolume94.
- SetVolume(InstanceID0,ChannelMaster,DesiredVolume94) succeeds in15ms, matching GetVolume readback94 in14ms. Status: HARDWARE-VERIFIED SAME-LEVEL ACCEPTANCE, not a changed-level/audible test.
- Event endpoint is advertised but volume event subscription/payload is not tested here.
KNOB0.8.23 uses this route for encoder volume with paced HTTPS fallback; build/tests passed, KNOB hardware speed validation pending. Other /httpapi.asp commands remain HTTPS443.
Canonical: [A97-VOLUME.md](../../protocols/upnp/A97-VOLUME.md).

## KNOB0.8.23 volume hardware confirmation — 2026-10-21
User confirms A97 volume control is noticeably faster after switching to RenderingControl SetVolume. Status: USER/HARDWARE-VERIFIED WORKING on the tested device; numerical ESP32 latency and long-duration stability not measured. Preserve this as the preferred compatible-A97 volume approach for future airControl desktop/mobile and other integrations, with paced HTTPS fallback. Those future integrations are not yet confirmed. See [canonical evidence](../../protocols/upnp/A97-VOLUME.md) and [reuse rule](../../integration/A97-VOLUME-REUSE.md).

## 4STREAM APK evidence — 2026-10-24
**APK-VERIFIED / NOT-HW-VERIFIED**. The APK explicitly checks ALLWINNER-R328 for quiet-update and optional 5-GHz UI paths; it does not label those checks A97. Existing getPresetInfo rejection and hardware-tested RenderingControl Master volume remain authoritative.
[Command formats, chip conditions and limitations](../../protocols/linkplay-http-https/4STREAM-2026-10-24.md); [142 central builder observations](../../protocols/linkplay-http-https/4STREAM-BUILDERS-2026-10-24.md). New source/routing records 635–642 supplement existing IDs without changing their hardware status.


## A97 10-band EQ hardware confirmation — 2026-10-26
**HARDWARE-VERIFIED on tested A97:** ALLWINNER-R328, project `a97_rakoit`, firmware `Linkplay.4.6.437434`, HTTPS :443, test address 192.168.0.105.

Read commands confirmed:
- `EQGetStat` -> `{"EQStat":"On"}`.
- `EQGetList` -> stock profiles plus user/custom names; exact observed list included `Custom`, `рр`, `124`, `1`.
- `EQGetBand` -> `status=OK`, 10 bands at 31, 63, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz. Device reports `EQ_support=Eq10HP_ver_1.0` in `getStatusEx`.

Write command confirmed:
- `EQSetBand:{"EQBand":[{"index":N,"param_name":"<band label>","value":V}]}` -> `{"status":"OK"}`.
- Safe changed-value/readback test on index 0 / `00. 31 Hz`: 41 -> 42 was accepted and immediately visible via `EQGetBand`; restore 42 -> 41 was accepted and read back as 41. Other nine band values remained unchanged.
- Writing a band clears the returned preset `Name` from `Custom` to an empty string in the observed session. Preserve this behavior in clients; do not assume a named preset remains selected after direct band editing.

Negative probe (same hardware/firmware): the tested forms `EQGetLV2Band:Eq10HP`, `EQGetLV2Band:http://eq10q`, `EQGetLV2SourceBand:wifi`, `EQGetLV2SourceBandEx:wifi`, `EQv2GetList:0`, and `EQv2GetNewList:0` all returned `{"status":"Failed"}`. This does **not** prove LV2/PEQ is absent; only these exact parameterizations are hardware-observed failing.

Room-correction implication: direct 10-band read/write is now a confirmed A97 control surface suitable for a first room-correction implementation. The mapping of raw `value` units to dB is **not yet hardware-confirmed** and must be measured before treating values as acoustic gain in dB.


### A97 EQLoad:Flat and neutral raw value — hardware confirmation 2026-10-26
On the same tested A97 (ALLWINNER-R328 / a97_rakoit / Linkplay.4.6.437434 / HTTPS :443), `EQLoad:Flat` returned `status=OK`, `EQStat=On`, `Name=Flat`, and all ten EQ bands at raw `value=50`. A subsequent `EQGetBand` returned the same state. The prior ten-band values were then restored individually with the already verified `EQSetBand`; every write returned `status=OK` and final readback matched the original vector exactly: [41,29,35,38,46,50,54,62,69,79].

This hardware-verifies `EQLoad:Flat` and establishes raw 50 as the **neutral/Flat center value** for this Eq10HP implementation. Do not yet label raw 50 as numerically 0 dB or infer raw-unit-to-dB scaling until that conversion is separately established. Direct `EQSetBand` restore leaves `Name` empty, consistent with direct manual-band editing observed above.


### A97 factory booster/reducer EQ vectors — hardware confirmation 2026-10-26
Same tested A97 (ALLWINNER-R328 / a97_rakoit / Linkplay.4.6.437434 / HTTPS :443). `EQLoad:<name>` and immediate `EQGetBand` produced matching factory vectors:
- Bass Booster: [73,67,65,59,55,50,50,50,50,50]
- Treble Booster: [50,50,50,50,50,55,59,65,67,73]
- Bass Reducer: [27,33,35,39,45,50,50,50,50,50]
- Treble Reducer: [50,50,50,50,50,45,39,35,33,27]
Flat center is 50. The booster/reducer vectors are symmetric around 50 except the observed 250 Hz bass pair is 59/39 (offsets +9/-11), so do not assume exact mathematical symmetry for every factory preset coefficient. After testing, the prior custom vector [41,29,35,38,46,50,54,62,69,79] was restored via `EQSetBand` and verified by `EQGetBand`.

These observations hardware-verify `EQLoad:Bass Booster`, `EQLoad:Treble Booster`, `EQLoad:Bass Reducer`, and `EQLoad:Treble Reducer` on this firmware. They still do not establish raw-unit-to-dB conversion; factory preset raw values alone are insufficient to claim a dB scale.


### A97 Eq10HP raw value vs native-app dB observations — 2026-10-26
**HARDWARE/UI-OBSERVED on the same tested A97.** With the native EQ UI open, direct `EQSetBand` writes to index 0 (31 Hz) produced these displayed gain values:
- raw 25 -> -6.0 dB
- raw 40 -> -2.6 dB
- raw 50 -> 0.0 dB (also confirmed by factory Flat)
- raw 60 -> +2.2 dB
- raw 75 -> +6.0 dB

Therefore the raw scale must not be modeled as a single symmetric linear coefficient around 50: equal raw offsets of +/-10 produced +2.2/-2.6 dB in the native UI. Endpoints +/-25 both display +/-6.0 dB. These are observed mapping points, not yet a complete conversion formula. Preserve exact observed points and derive/interpolate only after additional measurements if needed.


## A97/H50 non-HTTPS radio playback correction — 2026-10-29

The v5.0.11 implementation sent framed TCP/8899 `MCU+PLY-PLA` after AVTransport `Play` failed. The user reports the error banner disappeared but playback still did not begin. That implementation is therefore **NOT A WORKING FIX in the reported run** and must not be treated as evidence that TCP/8899 can start an arbitrary radio URL.

Arylic's H50 guidance says URL playback uses UPnP PlayQueue: `CreateQueue` with a radio `PlayList` QueueContext, followed by `PlayQueueWithIndex` for the same queue. See [canonical PlayQueue details](../../protocols/upnp/playqueue/COMMANDS.md) and the [v5.0.12 implementation report](../../evidence/application-code/AIRCONTROL-A97-PLAYQUEUE-RADIO-CORRECTION-2026-10-29.md).

Status: **ARYLIC-FORUM-DOCUMENTED / SOURCE-IMPLEMENTED / NOT-HW-VERIFIED** on the user's H50. Do not change existing HTTPS-confirmed A97 command facts.


## H50 PlayQueue capture and direct URL limitation — 2026-10-30

On the tested H50 `192.168.0.100`, the existing WiiM Home PCAP records `CreateQueue` and `PlayQueueWithIndex` over HTTP/59152 with HTTP 200 SOAP responses. The accepted context is **`newTuneIn` with a TuneIn SearchUrl and no Track URL**, not Arylic's separate published `OnlineMusic` direct-URL example. Status: **CAPTURE-OBSERVED ACTION ACCEPTANCE** for that exact TuneIn shape; audible playback and arbitrary direct URL queue support remain unverified. [Detailed packet and APK evidence](../../evidence/captures/H50-PLAYQUEUE-NEW-TUNEIN-2026-10-30.md).

The user reports that airControl v5.0.12 did not respond when selecting radio, while its other H50 commands and the native app worked. v5.0.12's repeated direct-URL queue attempts and divergent DIDL are source-observed defects; v5.0.13 corrects those client behaviors but remains **NOT-HW-VERIFIED**. The H50 separately advertises HTTPS security 3.0, and 4STREAM's analyzed custom-radio path builds `setPlayerCmd:play:<encoded-url>` through its secure HTTP API client. Do not infer that this device's firmware lacks HTTPS merely from airControl's fallback profile. Existing HTTPS-tested A97 facts are unchanged.

## H50 RTL radio: two UPnP AVTransport endpoints (2026-10-30)

A 653-packet capture on the user's H50 at `192.168.0.106` shows airControl's `SetAVTransportURI` to TCP/49152 accepted RTL URI and DIDL artwork metadata. Its `Play` to 49152 did not start playback. WiiM Home then sent `AVTransport#Play` to TCP/59152 with `Connection: keep-alive` and `<ControlSource>WiiMApp</ControlSource>`; the H50 returned HTTP 200 and subsequently reported `PLAYING`. This is **HW-CAPTURE-VERIFIED** for that device/session. The individual necessity of port, control-source field, and keep-alive is not isolated; v5.0.14 RC1 implements the combination, and the user confirmed RTL sound starts without WiiM Home Play while RTL artwork appears in WiiM Home: **USER-HW-VERIFIED for RTL on this H50**. The user later reported that all H50 stations and covers they checked work in v5.0.14 RC1; the station list/count were not recorded, so exhaustive catalog and codec coverage remain unverified. Other devices remain unverified. [Packet report](../../evidence/captures/H50-RTL-DUAL-UPNP-PLAY-2026-10-30.md).
