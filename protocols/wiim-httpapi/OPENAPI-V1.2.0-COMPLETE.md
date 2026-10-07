# WiiM / Linkplay HTTP API — OpenAPI v1.2.0 complete audit

Source snapshot: `cvdlinden/wiim-httpapi` `openapi.json` blob `5a1e68e149fee8e45ba80e4d8797d5521650e20c`.

Transport described by source: `HTTPS GET https://<device>/httpapi.asp?command=<command>`. WiiM devices use a self-signed certificate. Source explicitly warns that commands may be model-, brand-, or firmware-specific. Therefore this import is **SOURCE-DOCUMENTED / NOT-HW-VERIFIED for A97/A98** unless a pre-existing canonical record already has stronger evidence.

OpenAPI paths audited: **346 including generic test path; 345 real command paths**. Existing canonical matches reused: **36**. New canonical records: **309** (records 326–634). Generic `/{command}` is a Swagger testing helper, not a device command, and is not assigned a command record.


## Device information

### `getStatusEx`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get device information
- **operationId:** `getStatusEx`
- **Responses:** `200` → `#/components/schemas/DeviceStatus`

### `getDebugInfo`
- **Status:** QRY-WIIM-GET-DEBUG-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get device debug information
- **operationId:** `getDebugInfo`
- **Responses:** `200` → `#/components/schemas/DeviceDebugInfo`


## Track metadata

### `getMetaInfo`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get Current Track Metadata
- **operationId:** `getMetaInfo`
- **Responses:** `200` → `#/components/schemas/TrackMetadata`


## Playback control

### `getPlayerStatus`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get the playback status
- **operationId:** `getPlayerStatus`
- **Responses:** `200` → `#/components/schemas/PlayerStatus`

### `setPlayerCmd:hex_playlist:url:{index}`
- **Status:** CMD-WIIM-SET-PLAYER-CMD-HEX-PLAYLIST-URL · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Play a specific track from a playlist by URL and index
- **operationId:** `setPlayerCmdHexPlaylistUrl`
- **Parameters:** `index` (path, required, string)
- **Responses:** `200` (Successful response)

### `setPlayerCmd:pause`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Pause
- **operationId:** `setPlayerCmdPause`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:resume`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Resume
- **operationId:** `setPlayerCmdResume`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:onepause`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Toggle pause/play
- **operationId:** `setPlayerCmdOnePause`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:play:{url}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Play audio URL
- **operationId:** `setPlayerCmdPlayUrl`
- **Parameters:** `url` (path, required, string, default="http://as-hls-ww-live.akamaized.net/pool_01505109/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8")
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:playlist:{url}:{index}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Play audio playlist
- **operationId:** `setPlayerCmdPlaylistUrl`
- **Parameters:** `index` (path, required, string); `url` (path, required, string, default="https://gist.githubusercontent.com/bpsib/67089b959e4fa898af69fea59ad74bc3/raw/685789e28187c0a15da978b51d436a140d5ea207/BBC-Radio-HLS.m3u")
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:prev`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Previous
- **operationId:** `setPlayerCmdPrev`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:next`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Next
- **operationId:** `setPlayerCmdNext`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:seek:position`
- **Status:** CMD-WIIM-SET-PLAYER-CMD-SEEK-POSITION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Seek
- **operationId:** `setPlayerCmdSeekPosition`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:stop`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Stop
- **operationId:** `setPlayerCmdStop`
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:vol:{value}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Set volume
- **operationId:** `setPlayerCmdVol`
- **Parameters:** `value` (path, required, integer)
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:mute:{n}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Mute
- **operationId:** `setPlayerCmdMute`
- **Parameters:** `n` (path, required, integer, enum=[0,1], default=1)
- **Responses:** `200` → `#/components/responses/StringOK`

### `setPlayerCmd:loopmode:{n}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Loop mode set
- **operationId:** `setPlayerCmdLoopmode`
- **Parameters:** `n` (path, required, integer, enum=[-1,0,1,2,3,4,5], default=4)
- **Responses:** `200` → `#/components/responses/StringOK`


## Network

### `getStaticIpInfo`
- **Status:** QRY-WIIM-GET-STATIC-IP-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the static IP information
- **operationId:** `getStaticIpInfo`
- **Responses:** `200` → `#/components/schemas/StaticIpInfo`

### `getStaticIP`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Query networking status
- **operationId:** `getStaticIP`
- **Responses:** `200` → `string`

### `wlanGetConnectState`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get the connection status
- **operationId:** `wlanGetConnectState`
- **Responses:** `200` → `string`

### `setWlanStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}`
- **Status:** CMD-WIIM-SET-WLAN-STATIC-IP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set static WLAN network config
- **operationId:** `setWlanStaticIp`
- **Parameters:** `IpAddress` (path, required, string); `GatewayIp` (path, required, string); `DnsServerIp` (path, required, string)
- **Responses:** `200` → `#/components/responses/StringOK`

### `setEthStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}`
- **Status:** CMD-WIIM-SET-ETH-STATIC-IP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set static Ethernet network config
- **operationId:** `setEthStaticIp`
- **Parameters:** `IpAddress` (path, required, string); `GatewayIp` (path, required, string); `DnsServerIp` (path, required, string)
- **Responses:** `200` → `#/components/responses/StringOK`

### `setSSID:{value}`
- **Status:** CMD-WIIM-SET-SSID · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Change the SSID name of the device
- **operationId:** `setSSID`
- **Parameters:** `value` (path, required, string)
- **Responses:** `200` (Successful response)

### `setNetwork:{n}:{password}`
- **Status:** CMD-WIIM-SET-NETWORK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Setting the password WIFI
- **operationId:** `setNetwork`
- **Parameters:** `n` (path, required, integer, enum=[0,1]); `password` (path, required, string)
- **Responses:** `200` (Successful response)

### `getNetworkPreferDNS`
- **Status:** QRY-WIIM-GET-NETWORK-PREFER-DNS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the preferred DNS server
- **operationId:** `getNetworkPreferDNS`
- **Responses:** `200` (Successful response)

### `getWlanBandConfig`
- **Status:** QRY-WIIM-GET-WLAN-BAND-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the WLAN band configuration
- **operationId:** `getWlanBandConfig`
- **Responses:** `200` (Successful response)

### `getWlanRoamConfig`
- **Status:** QRY-WIIM-GET-WLAN-ROAM-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the WLAN roaming configuration
- **operationId:** `getWlanRoamConfig`
- **Responses:** `200` (Successful response)

### `getIPV6Enable`
- **Status:** QRY-WIIM-GET-IPV6ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get IPV6 enable status
- **operationId:** `getIPV6Enable`
- **Responses:** `200` (Successful response)

### `setPowerWifiDown`
- **Status:** CMD-WIIM-SET-POWER-WIFI-DOWN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Stop WIFI signal
- **operationId:** `setPowerWifiDown`
- **Responses:** `200` (Successful response)

### `wlanConnectHideAp:{str}`
- **Status:** CMD-WIIM-WLAN-CONNECT-HIDE-AP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WLAN connect to hidden AP
- **operationId:** `wlanConnectHideAp`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `wlanConnectHideApEx:{str1}:{str2}:{str3}`
- **Status:** CMD-WIIM-WLAN-CONNECT-HIDE-AP-EX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WLAN connect to hidden AP with extra parameters
- **operationId:** `wlanConnectHideApEx`
- **Parameters:** `str1` (path, required, string); `str2` (path, required, string); `str3` (path, required, string)
- **Responses:** `200` (Successful response)

### `getNetwork`
- **Status:** QRY-WIIM-GET-NETWORK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the network configuration
- **operationId:** `getNetwork`
- **Responses:** `200` (Successful response)

### `wlanGetApListEx`
- **Status:** QRY-WIIM-WLAN-GET-AP-LIST-EX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get WLAN AP list
- **operationId:** `wlanGetApListEx`
- **Responses:** `200` → `object`

### `setHideSSID:{str}`
- **Status:** CMD-WIIM-SET-HIDE-SSID · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set hide SSID
- **operationId:** `setHideSSID`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setNetworkExAES:{n}:{password}`
- **Status:** CMD-WIIM-SET-NETWORK-EX-AES · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set network with AES encryption
- **operationId:** `setNetworkExAES`
- **Parameters:** `n` (path, required, integer, enum=[0,1]); `password` (path, required, string)
- **Responses:** `200` (Successful response)

### `setWlanBandConfig:{str}`
- **Status:** CMD-WIIM-SET-WLAN-BAND-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set WLAN band configuration
- **operationId:** `setWlanBandConfig`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setWlanConnectDisable:{str}`
- **Status:** CMD-WIIM-SET-WLAN-CONNECT-DISABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set WLAN connect disable
- **operationId:** `setWlanConnectDisable`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setWlanRoamConfig:{str}`
- **Status:** CMD-WIIM-SET-WLAN-ROAM-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set WLAN roam configuration
- **operationId:** `setWlanRoamConfig`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setNetworkPreferDNS:{str}`
- **Status:** CMD-WIIM-SET-NETWORK-PREFER-DNS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set network preferred DNS
- **operationId:** `setNetworkPreferDNS`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `wlanGetApFullList`
- **Status:** QRY-WIIM-WLAN-GET-AP-FULL-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get WLAN AP list
- **operationId:** `wlanGetApFullList`
- **Responses:** `200` (Successful response)

### `wlanSwitchConnectedAp:ssid={ssid}:bssid={bssid}`
- **Status:** CMD-WIIM-WLAN-SWITCH-CONNECTED-AP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Wlan switch connected AP
- **operationId:** `wlanSwitchConnectedAp`
- **Parameters:** `ssid` (path, required, string); `bssid` (path, required, string)
- **Responses:** `200` (Successful response)

### `setIPV6Enable:{str}`
- **Status:** CMD-WIIM-SET-IPV6ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set IPv6 enable
- **operationId:** `setIPV6Enable`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getWlanConnectDisableStatus`
- **Status:** QRY-WIIM-GET-WLAN-CONNECT-DISABLE-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get WLAN connect disable status
- **operationId:** `getWlanConnectDisableStatus`
- **Responses:** `200` (Successful response)

### `getNetworkHealth`
- **Status:** QRY-WIIM-GET-NETWORK-HEALTH · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get network health status
- **operationId:** `getNetworkHealth`
- **Responses:** `200` → `object`

### `wpscannel`
- **Status:** CMD-WIIM-WPSCANNEL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WPS Channel
- **operationId:** `wpscannel`
- **Responses:** `200` → `string`

### `wpsclientmode`
- **Status:** CMD-WIIM-WPSCLIENTMODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WPS Client Mode
- **operationId:** `wpsclientmode`
- **Responses:** `200` → `string`

### `wpsservermode`
- **Status:** CMD-WIIM-WPSSERVERMODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WPS Server Mode
- **operationId:** `wpsservermode`
- **Responses:** `200` → `string`


## Equalizer

### `EQOn`
- **Status:** CMD-WIIM-SET-EQON · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Turn on the EQ
- **operationId:** `setEQOn`
- **Responses:** `200` → `object`

### `EQOff`
- **Status:** CMD-WIIM-SET-EQOFF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Turn off the EQ setting
- **operationId:** `setEQOff`
- **Responses:** `200` → `object`

### `EQGetStat`
- **Status:** QRY-WIIM-GET-EQSTAT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Check if the EQ is ON or OFF
- **operationId:** `getEQStat`
- **Responses:** `200` → `object`

### `EQGetList`
- **Status:** QRY-WIIM-GET-EQLIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Check all the possible EQ settings
- **operationId:** `getEQList`
- **Responses:** `200` (Default response)

### `EQGetBand`
- **Status:** QRY-WIIM-GET-EQBAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the current EQ band
- **operationId:** `getEQBand`
- **Responses:** `200` (Default response)

### `EQLoad:{name}`
- **Status:** CMD-WIIM-LOAD-EQBY-NAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the specific EQ with name
- **operationId:** `loadEQByName`
- **Parameters:** `name` (path, required, string, enum=["Flat","Acoustic","Bass Booster","Bass Reducer","Classical","Dance","Deep","Electronic","Hip-Hop","Jazz","Latin","Loudness","Lounge","Piano","Pop","R&B","Rock","Small Speakers","Spoken Word","Treble Booster","Treble Reducer","Vocal Booster"])
- **Responses:** `200` → `object`

### `EQSet:Bass:{n}`
- **Status:** CMD-WIIM-EQ-SET-BASS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Bass level
- **operationId:** `eqSetBass`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `EQSet:Treble:{n}`
- **Status:** CMD-WIIM-EQ-SET-TREBLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Treble level
- **operationId:** `eqSetTreble`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `EQEnable`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Equalizer enable
- **operationId:** `eqEnable`
- **Responses:** `200` (Successful response)

### `EQDisable`
- **Status:** CMD-WIIM-EQ-DISABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Equalizer disable
- **operationId:** `eqDisable`
- **Responses:** `200` (Successful response)

### `EQSetBand:{"EQBand":[{"index":{n1},"param_name":{str},"value":{n2}}]}`
- **Status:** CMD-WIIM-EQ-SET-BAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set (a specific) band of the 10-band EQ
- **operationId:** `eqSetBand`
- **Parameters:** `n1` (path, required, integer); `str` (path, required, string); `n2` (path, required, integer)
- **Responses:** `200` (Successful response)

### `EQSetLV2Band:{str}`
- **Status:** CMD-WIIM-EQ-SET-LV2BAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set LV2 band
- **operationId:** `eqSetLV2Band`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQSetLV2SourceBand:{str}`
- **Status:** CMD-WIIM-EQ-SET-LV2SOURCE-BAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set LV2 source band
- **operationId:** `eqSetLV2SourceBand`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2Delete:{str}`
- **Status:** CMD-WIIM-EQV2DELETE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Delete EQ v2 settings
- **operationId:** `eqv2Delete`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2Rename:{str}`
- **Status:** CMD-WIIM-EQV2RENAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Rename EQ v2 settings
- **operationId:** `eqv2Rename`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQChangeSourceFX:{str}`
- **Status:** CMD-WIIM-EQ-CHANGE-SOURCE-FX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Change source FX
- **operationId:** `eqChangeSourceFX`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQChangeFX:{str}`
- **Status:** CMD-WIIM-EQ-CHANGE-FX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Change FX
- **operationId:** `eqChangeFX`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQGetLV2Band:{pluginURI}`
- **Status:** QRY-WIIM-EQ-GET-LV2BAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LV2 band
- **operationId:** `eqGetLV2Band`
- **Parameters:** `pluginURI` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQGetLV2SourceBand:{str}`
- **Status:** QRY-WIIM-EQ-GET-LV2SOURCE-BAND · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LV2 source band
- **operationId:** `eqGetLV2SourceBand`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQGetLV2SourceBandEx:{str}`
- **Status:** QRY-WIIM-EQ-GET-LV2SOURCE-BAND-EX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LV2 source band with extra parameters
- **operationId:** `eqGetLV2SourceBandEx`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2GetList:{str}`
- **Status:** QRY-WIIM-EQV2GET-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get EQ v2 list
- **operationId:** `eqv2GetList`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2GetNewList:{str}`
- **Status:** QRY-WIIM-EQV2GET-NEW-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get new EQ v2 list
- **operationId:** `eqv2GetNewList`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2Load:{str}`
- **Status:** CMD-WIIM-EQV2LOAD · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Load EQ v2 settings
- **operationId:** `eqv2Load`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQv2SourceLoad:{str}`
- **Status:** CMD-WIIM-EQV2SOURCE-LOAD · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Source load EQ v2 settings
- **operationId:** `eqv2SourceLoad`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQSourceOff:{str}`
- **Status:** CMD-WIIM-EQ-SOURCE-OFF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Turn off EQ source
- **operationId:** `eqSourceOff`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQSetChannelMode:{str}`
- **Status:** CMD-WIIM-EQ-SET-CHANNEL-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set channel mode
- **operationId:** `eqSetChannelMode`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQSourceSave:{str}`
- **Status:** CMD-WIIM-EQ-SOURCE-SAVE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Save EQ source settings
- **operationId:** `eqSourceSave`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQSave:{str}`
- **Status:** CMD-WIIM-EQ-SAVE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Save EQ settings
- **operationId:** `eqSave`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQGetLV2BandEx:{pluginURI}`
- **Status:** QRY-WIIM-EQ-GET-LV2BAND-EX · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LV2 band with extra parameters
- **operationId:** `eqGetLV2BandEx`
- **Parameters:** `pluginURI` (path, required, string)
- **Responses:** `200` (Successful response)

### `EQGetSourceModes`
- **Status:** QRY-WIIM-EQ-GET-SOURCE-MODES · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the EQ source modes
- **operationId:** `eqGetSourceModes`
- **Responses:** `200` → `array`

### `EQSave:Custom`
- **Status:** CMD-WIIM-EQ-SAVE-CUSTOM · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Save the current EQ setting as "Custom"
- **operationId:** `eqSaveCustom`
- **Responses:** `200` (Successful response)


## Device control

### `reboot`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Reboot
- **operationId:** `rebootDevice`
- **Responses:** `200` → `object`

### `setShutdown:{sec}`
- **Status:** CMD-WIIM-SET-SHUTDOWN-TIMER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Shutdown
- **operationId:** `setShutdownTimer`
- **Parameters:** `sec` (path, required, string, default="0")
- **Responses:** `200` → `object`

### `getShutdown`
- **Status:** QRY-WIIM-GET-SHUTDOWN-TIMER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the shutdown timer
- **operationId:** `getShutdownTimer`
- **Responses:** `200` → `integer`

### `LED_SWITCH_SET:{n}`
- **Status:** CMD-WIIM-SET-LED-SWITCH · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Turn on/off status LED ("Status Light" option from app)
- **operationId:** `setLedSwitch`
- **Parameters:** `n` (path, required, integer, enum=[0,1], default=1)
- **Responses:** `200` → `#/components/responses/StringOK`

### `Button_Enable_SET:{n}`
- **Status:** CMD-WIIM-SET-TOUCH-CONTROLS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Turn on/off touch controls
- **operationId:** `setTouchControls`
- **Parameters:** `n` (path, required, integer, enum=[0,1], default=1)
- **Responses:** `200` → `#/components/responses/StringOK`

### `Button_Enable_GET`
- **Status:** QRY-WIIM-BUTTON-ENABLE-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get button enable status
- **operationId:** `buttonEnableGet`
- **Responses:** `200` (Successful response)

### `getFirmwareVersion`
- **Status:** QRY-WIIM-GET-FIRMWARE-VERSION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get firmware version
- **operationId:** `getFirmwareVersion`
- **Responses:** `200` (Successful response)

### `getDeviceNameChangeable`
- **Status:** QRY-WIIM-GET-DEVICE-NAME-CHANGEABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get device name changeable status
- **operationId:** `getDeviceNameChangeable`
- **Responses:** `200` (Successful response)

### `restoreToDefault`
- **Status:** CMD-WIIM-RESTORE-TO-DEFAULT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Restoring the factory setting
- **operationId:** `restoreToDefault`
- **Responses:** `200` (Successful response)

### `setDeviceName:{name}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Setting the name of device
- **operationId:** `setDeviceName`
- **Parameters:** `name` (path, required, string)
- **Responses:** `200` (Successful response)

### `getsyslog`
- **Status:** QRY-WIIM-GETSYSLOG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get system log
- **operationId:** `getsyslog`
- **Responses:** `200` (Successful response)

### `setHexDeviceName:{str}`
- **Status:** CMD-WIIM-SET-HEX-DEVICE-NAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set hex device name
- **operationId:** `setHexDeviceName`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `noSendMoreDeviceEvent:1`
- **Status:** CMD-WIIM-NO-SEND-MORE-DEVICE-EVENT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disable sending more device events
- **operationId:** `noSendMoreDeviceEvent`
- **Responses:** `200` (Successful response)

### `getHwErrorInfo`
- **Status:** QRY-WIIM-GET-HW-ERROR-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get hardware error information
- **operationId:** `getHwErrorInfo`
- **Responses:** `200` → `object`


## Alarm clock

### `timeSync:{YYYYMMDDHHMMSS}`
- **Status:** QRY-WIIM-SET-TIME-SYNC · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get network time
- **operationId:** `setTimeSync`
- **Parameters:** `YYYYMMDDHHMMSS` (path, required, string)
- **Responses:** `200` (Default response)

### `setAlarmClock:{n}:{trig}:{op}:{time}:{day}:{url}`
- **Status:** CMD-WIIM-SET-ALARM-CLOCK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Alarm
- **operationId:** `setAlarmClock`
- **Parameters:** `n` (path, required, integer, enum=[0,1,2]); `trig` (path, required, integer, enum=[0,1,2,3,4,5]); `op` (path, required, integer, enum=[0,1,2]); `time` (path, required, string); `day` (path, required, string); `url` (path, required, string)
- **Responses:** `200` (Default response)

### `getAlarmClock:{n}`
- **Status:** QRY-WIIM-GET-ALARM-CLOCK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Not specified
- **operationId:** `getAlarmClock`
- **Parameters:** `n` (path, required, integer, enum=[0,1,2], default=0)
- **Responses:** `200` → `object`

### `alarmStop`
- **Status:** CMD-WIIM-STOP-ALARM-CLOCK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Stop the current alarm
- **operationId:** `stopAlarmClock`
- **Responses:** `200` (Default response)


## Source input switch

### `setPlayerCmd:switchmode:{mode}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Switch the source input
- **operationId:** `setPlayerCmdSwitchMode`
- **Parameters:** `mode` (path, required, string, enum=["line-in","bluetooth","optical","udisk","wifi","HDMI"])
- **Responses:** `200` (Default response)


## Presets

### `MCUKeyShortClick:{n}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Play preset with preset number
- **operationId:** `getMCUKeyShortClick`
- **Parameters:** `n` (path, required, integer, enum=[1,2,3,4,5,6,7,8,9,10,11,12], default=1)
- **Responses:** `200` → `#/components/responses/StringOK`

### `MCUKeyShortClick:{n}:{t}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Play preset with preset number and track number
- **operationId:** `getMCUKeyShortClickTrack`
- **Parameters:** `n` (path, required, integer, enum=[1,2,3,4,5,6,7,8,9,10,11,12], default=1); `t` (path, required, integer, default=1)
- **Responses:** `200` → `#/components/responses/StringOK`

### `getPresetInfo`
- **Status:** QRY-WIIM-GET-PRESET-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Preset List
- **operationId:** `getPresetInfo`
- **Responses:** `200` → `#/components/schemas/PresetList`


## Audio output control

### `getNewAudioOutputHardwareMode`
- **Status:** QRY-WIIM-GET-NEW-AUDIO-OUTPUT-HARDWARE-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get audio output mode
- **operationId:** `getNewAudioOutputHardwareMode`
- **Responses:** `200` → `object`

### `setAudioOutputHardwareMode:{n}`
- **Status:** CMD-WIIM-SET-AUDIO-OUTPUT-HARDWARE-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set audio output mode
- **operationId:** `setAudioOutputHardwareMode`
- **Parameters:** `n` (path, required, integer, enum=[1,2,3])
- **Responses:** `200` → `#/components/responses/StringOK`

### `getSpdifOutSwitchDelayMs`
- **Status:** QRY-WIIM-GET-SPDIF-OUT-SWITCH-DELAY-MS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get SPDIF sample rate switch latency
- **operationId:** `getSpdifOutSwitchDelayMs`
- **Responses:** `200` → `integer`

### `setSpdifOutSwitchDelayMs:{Delay}`
- **Status:** CMD-WIIM-SET-SPDIF-OUT-SWITCH-DELAY-MS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set SPDIF sample rate switch latency
- **operationId:** `setSpdifOutSwitchDelayMs`
- **Parameters:** `Delay` (path, required, integer)
- **Responses:** `200` → `#/components/responses/StringOK`

### `getChannelBalance`
- **Status:** QRY-WIIM-GET-CHANNEL-BALANCE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get left/right channel balance
- **operationId:** `getChannelBalance`
- **Responses:** `200` → `string`

### `setChannelBalance:{n}`
- **Status:** CMD-WIIM-SET-CHANNEL-BALANCE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set left/right channel balance
- **operationId:** `setChannelBalance`
- **Parameters:** `n` (path, required, number)
- **Responses:** `200` → `string`

### `GetFadeFeature`
- **Status:** QRY-WIIM-GET-FADE-FEATURE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get fade in/out feature status
- **operationId:** `getFadeFeature`
- **Responses:** `200` → `object`

### `SetFadeFeature:{n}`
- **Status:** CMD-WIIM-SET-FADE-FEATURE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set fade in/out feature
- **operationId:** `setFadeFeature`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)


## Bluetooth

### `startbtdiscovery:{n}`
- **Status:** CMD-WIIM-START-BT-DISCOVERY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start Bluetooth device scan
- **operationId:** `startBtDiscovery`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` → `#/components/responses/StringOK`

### `getbtdiscoveryresult`
- **Status:** QRY-WIIM-GET-BT-DISCOVERY-RESULT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Bluetooth device scan result
- **operationId:** `getBtDiscoveryResult`
- **Responses:** `200` → `#/components/schemas/BluetoothDeviceList`

### `clearbtdiscoveryresult`
- **Status:** CMD-WIIM-CLEAR-BT-DISCOVERY-RESULT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Clear Bluetooth device scan result
- **operationId:** `clearBtDiscoveryResult`
- **Responses:** `200` → `#/components/responses/StringOK`

### `getbthistory`
- **Status:** QRY-WIIM-GET-BT-HISTORY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get paired Bluetooth devices
- **operationId:** `getBtHistory`
- **Responses:** `200` → `#/components/schemas/BluetoothDeviceList`

### `connectbta2dpsynk:{BT_MAC_ADDRESS}`
- **Status:** CMD-WIIM-CONNECT-BT-A2DPSYNK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Connect to a Bluetooth device
- **operationId:** `connectBtA2dpsynk`
- **Parameters:** `undefined` (?, optional)
- **Responses:** `200` → `string`

### `disconnectbta2dpsynk:{BT_MAC_ADDRESS}`
- **Status:** CMD-WIIM-DISCONNECT-BT-A2DPSYNK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disconnect from a Bluetooth device
- **operationId:** `disconnectBtA2dpsynk`
- **Parameters:** `undefined` (?, optional)
- **Responses:** `200` → `#/components/responses/StringOK`

### `getbtpairstatus`
- **Status:** QRY-WIIM-GET-BT-PAIR-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Bluetooth pairing status
- **operationId:** `getBtPairStatus`
- **Responses:** `200` → `object`

### `connectbta2dpsource:{str}`
- **Status:** CMD-WIIM-CONNECTBTA2DPSOURCE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Connect to a Bluetooth source device
- **operationId:** `connectbta2dpsource`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `delbthistory:{str}`
- **Status:** CMD-WIIM-DELBTHISTORY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Delete Bluetooth history
- **operationId:** `delbthistory`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `btdisconnectall`
- **Status:** CMD-WIIM-BTDISCONNECTALL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disconnect all Bluetooth devices
- **operationId:** `btdisconnectall`
- **Responses:** `200` (Successful response)

### `getbtPairDevStat`
- **Status:** QRY-WIIM-GETBT-PAIR-DEV-STAT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Bluetooth pair device status
- **operationId:** `getbtPairDevStat`
- **Responses:** `200` (Successful response)

### `getbtstatus`
- **Status:** QRY-WIIM-GETBTSTATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Bluetooth status
- **operationId:** `getbtstatus`
- **Responses:** `200` (Successful response)

### `startbtserver`
- **Status:** CMD-WIIM-STARTBTSERVER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start Bluetooth server
- **operationId:** `startbtserver`
- **Responses:** `200` (Successful response)

### `startgetbtPairDevStat`
- **Status:** CMD-WIIM-STARTGETBT-PAIR-DEV-STAT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start getting Bluetooth pair device status
- **operationId:** `startgetbtPairDevStat`
- **Responses:** `200` (Successful response)

### `stopbtdiscovery`
- **Status:** CMD-WIIM-STOPBTDISCOVERY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Stop Bluetooth discovery
- **operationId:** `stopbtdiscovery`
- **Responses:** `200` (Successful response)

### `stopbtserver:{n}`
- **Status:** CMD-WIIM-STOPBTSERVER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Stop Bluetooth server
- **operationId:** `stopbtserver`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `btavkenterpair`
- **Status:** CMD-WIIM-BTAVKENTERPAIR · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enter Bluetooth pairing mode
- **operationId:** `btavkenterpair`
- **Responses:** `200` (Successful response)

### `blehidpair:{str}`
- **Status:** CMD-WIIM-BLEHIDPAIR · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Pair with a BLE HID device
- **operationId:** `blehidpair`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `blehidremoveall`
- **Status:** CMD-WIIM-BLEHIDREMOVEALL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Remove all paired BLE HID devices
- **operationId:** `blehidremoveall`
- **Responses:** `200` (Successful response)

### `btrecovery`
- **Status:** CMD-WIIM-BTRECOVERY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Recovery Bluetooth
- **operationId:** `btrecovery`
- **Responses:** `200` (Successful response)

### `getblehidstatus`
- **Status:** QRY-WIIM-GET-BLE-HID-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get BLE HID status
- **operationId:** `getBleHidStatus`
- **Responses:** `200` (Successful response)

### `startblescan:{n}`
- **Status:** CMD-WIIM-START-BLE-SCAN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start BLE scan
- **operationId:** `startBleScan`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getblediscoveryresult`
- **Status:** QRY-WIIM-GET-BLE-DISCOVERY-RESULT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get BLE discovery result
- **operationId:** `getBleDiscoveryResult`
- **Responses:** `200` (Successful response)


## Room correction

### `RoomCorrGet`
- **Status:** QRY-WIIM-ROOM-CORR-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the current room correction settings
- **operationId:** `roomCorrGet`
- **Responses:** `200` → `object`

### `RoomCorrGetMode`
- **Status:** QRY-WIIM-ROOM-CORR-GET-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the current room correction mode
- **operationId:** `roomCorrGetMode`
- **Responses:** `200` (Successful response)

### `RoomCorrSet:{str}`
- **Status:** CMD-WIIM-ROOM-CORR-SET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the room correction settings
- **operationId:** `roomCorrSet`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `RoomCorrSetLR:{str}`
- **Status:** CMD-WIIM-ROOM-CORR-SET-LR · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the room correction settings for left and right channels
- **operationId:** `roomCorrSetLR`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `RoomCorrSetMode:{"Mode":"{str}"}`
- **Status:** CMD-WIIM-ROOM-CORR-SET-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the room correction mode
- **operationId:** `roomCorrSetMode`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setRoomCorrection:{"RC_Version":"{str}","Time":"{time}"}`
- **Status:** CMD-WIIM-SET-ROOM-CORRECTION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the room correction settings with version and time parameters
- **operationId:** `setRoomCorrection`
- **Parameters:** `str` (path, required, string); `time` (path, required, string)
- **Responses:** `200` (Successful response)


## Alexa

### `alexaEnableBetaId:{n}`
- **Status:** CMD-WIIM-ALEXA-ENABLE-BETA-ID · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable Alexa Beta ID
- **operationId:** `alexaEnableBetaId`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getAlexaProfile`
- **Status:** QRY-WIIM-GET-ALEXA-PROFILE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Profile
- **operationId:** `getAlexaProfile`
- **Responses:** `200` (Successful response)

### `alexaLogOut`
- **Status:** CMD-WIIM-ALEXA-LOG-OUT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Log out of Alexa
- **operationId:** `alexaLogOut`
- **Responses:** `200` (Successful response)

### `getAlexaCountry`
- **Status:** QRY-WIIM-GET-ALEXA-COUNTRY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Country
- **operationId:** `getAlexaCountry`
- **Responses:** `200` (Successful response)

### `alexaLanguageListGet`
- **Status:** QRY-WIIM-ALEXA-LANGUAGE-LIST-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Language List
- **operationId:** `alexaLanguageListGet`
- **Responses:** `200` (Successful response)

### `alexaGetLanguage`
- **Status:** QRY-WIIM-ALEXA-GET-LANGUAGE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Language
- **operationId:** `alexaGetLanguage`
- **Responses:** `200` (Successful response)

### `setAlexaCountry:{str}`
- **Status:** CMD-WIIM-SET-ALEXA-COUNTRY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Alexa Country
- **operationId:** `setAlexaCountry`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `alexaSetLanguage:{str}`
- **Status:** CMD-WIIM-ALEXA-SET-LANGUAGE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Alexa Language
- **operationId:** `alexaSetLanguage`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getAvsDevInfo`
- **Status:** QRY-WIIM-GET-AVS-DEV-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Voice Service Device Info
- **operationId:** `getAvsDevInfo`
- **Responses:** `200` (Successful response)

### `getAvsMusicHDEnable`
- **Status:** QRY-WIIM-GET-AVS-MUSIC-HDENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Alexa Voice Service Music HD enable status
- **operationId:** `getAvsMusicHDEnable`
- **Responses:** `200` (Successful response)

### `setAvsMusicHDEnable:{str}`
- **Status:** CMD-WIIM-SET-AVS-MUSIC-HDENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Alexa Voice Service Music HD enable
- **operationId:** `setAvsMusicHDEnable`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)


## Amazon music

### `setAmazonAccessToken:{str}:{str2}`
- **Status:** CMD-WIIM-SET-AMAZON-ACCESS-TOKEN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Amazon access token
- **operationId:** `setAmazonAccessToken`
- **Parameters:** `str` (path, required, string); `str2` (path, required, string)
- **Responses:** `200` (Successful response)

### `EnableAmazonAtmos:{n}`
- **Status:** CMD-WIIM-ENABLE-AMAZON-ATMOS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable Amazon Atmos
- **operationId:** `enableAmazonAtmos`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `EnableAmazonHD:{n}`
- **Status:** CMD-WIIM-ENABLE-AMAZON-HD · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable Amazon HD
- **operationId:** `enableAmazonHD`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `GetAmazonHD`
- **Status:** QRY-WIIM-GET-AMAZON-HD · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Amazon HD status
- **operationId:** `getAmazonHD`
- **Responses:** `200` (Successful response)

### `getAmazonConfig`
- **Status:** QRY-WIIM-GET-AMAZON-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Amazon Music configuration
- **operationId:** `getAmazonConfig`
- **Responses:** `200` (Successful response)

### `setAmazonMusicParams:code={str1}:redirect_uri={str2}:client_id={str3}:code_verifier={str4}`
- **Status:** CMD-WIIM-SET-AMAZON-MUSIC-PARAMS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Amazon Music parameters
- **operationId:** `setAmazonMusicParams`
- **Parameters:** `str1` (path, required, string); `str2` (path, required, string); `str3` (path, required, string); `str4` (path, required, string)
- **Responses:** `200` (Successful response)

### `setPrimeToken:username={str1}:token={str2}:refreshToken={str3}:expires_in={n}`
- **Status:** CMD-WIIM-SET-PRIME-TOKEN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set Amazon Prime token
- **operationId:** `setPrimeToken`
- **Parameters:** `str1` (path, required, string); `str2` (path, required, string); `str3` (path, required, string); `n` (path, required, integer)
- **Responses:** `200` (Successful response)


## Multiroom

### `multiroom:getSlaveList`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get a list of LinkPlay available
- **operationId:** `multiroomGetSlaveList`
- **Responses:** `200` (Successful response)

### `multiroom:SlaveKickout:{ip}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Removing a LinkPlay from the multi-room
- **operationId:** `multiroomSlaveKickout`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveMask:{ip}`
- **Status:** CMD-WIIM-MULTIROOM-SLAVE-MASK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Hide the IP address of a LinkPlay
- **operationId:** `multiroomSlaveMask`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveUnMask:{ip}`
- **Status:** CMD-WIIM-MULTIROOM-SLAVE-UN-MASK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Releasing a Multi-Room Mode
- **operationId:** `multiroomSlaveUnMask`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveVolume:{ip}:{volume}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Individual volume adjustment
- **operationId:** `multiroomSlaveVolume`
- **Parameters:** `ip` (path, required, string); `volume` (path, required, integer)
- **Responses:** `200` (Successful response)

### `setPlayerCmd:slave_vol:{volume}`
- **Status:** CMD-WIIM-SET-PLAYER-CMD-SLAVE-VOLUME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** General Volume Adjustment
- **operationId:** `setPlayerCmdSlaveVolume`
- **Parameters:** `volume` (path, required, integer)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveMute:{ip}:{mute}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Individual muting
- **operationId:** `multiroomSlaveMute`
- **Parameters:** `ip` (path, required, string); `mute` (path, required, integer, enum=[0,1])
- **Responses:** `200` (Successful response)

### `setPlayerCmd:slave_mute:mute`
- **Status:** CMD-WIIM-SET-PLAYER-CMD-SLAVE-MUTE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** General activation Mute
- **operationId:** `setPlayerCmdSlaveMute`
- **Responses:** `200` (Successful response)

### `setPlayerCmd:slave_mute:unmute`
- **Status:** CMD-WIIM-SET-PLAYER-CMD-SLAVE-UNMUTE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** General Mute Disabling
- **operationId:** `setPlayerCmdSlaveUnmute`
- **Responses:** `200` (Successful response)

### `multiroom:SlaveChannel:{ip}:{channel}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Individual management of the audio signal Right / left
- **operationId:** `multiroomSlaveChannel`
- **Parameters:** `ip` (path, required, string); `channel` (path, required, integer, enum=[0,1])
- **Responses:** `200` (Successful response)

### `setPlayerCmd:{slave_channel}:{channel}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Overal management of the audio signal Right / left
- **operationId:** `setPlayerCmdSlaveChannel`
- **Parameters:** `slave_channel` (path, required, string); `channel` (path, required, integer, enum=[0,1])
- **Responses:** `200` (Successful response)

### `multiroom:SlaveSetDeviceName:{ip}:{s}`
- **Status:** CMD-WIIM-MULTIROOM-SLAVE-SET-DEVICE-NAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Individual definition of the device Name
- **operationId:** `multiroomSlaveSetDeviceName`
- **Parameters:** `ip` (path, required, string); `s` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:Ungroup`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Disabling Multi-Room
- **operationId:** `multiroomUngroup`
- **Responses:** `200` (Successful response)

### `multiroom:ConfigGet:realtime_cache_limit`
- **Status:** QRY-WIIM-MULTIROOM-CONFIG-GET-REALTIME-CACHE-LIMIT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the real-time cache limit
- **operationId:** `multiroomConfigGetRealtimeCacheLimit`
- **Responses:** `200` (Successful response)

### `multiroom:ConfigSet:realtime_cache_limit:{value}`
- **Status:** CMD-WIIM-MULTIROOM-CONFIG-SET-REALTIME-CACHE-LIMIT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the real-time cache limit
- **operationId:** `multiroomConfigSetRealtimeCacheLimit`
- **Parameters:** `value` (path, required, integer)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveStartWPS:{ip}`
- **Status:** CMD-WIIM-MULTIROOM-SLAVE-START-WPS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start WPS on a LinkPlay device
- **operationId:** `multiroomSlaveStartWPS`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:getnamegrouplist`
- **Status:** QRY-WIIM-MULTIROOM-GET-NAME-GROUP-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the list of group names in multi-room mode
- **operationId:** `multiroomGetNameGroupList`
- **Responses:** `200` → `object`

### `multiroom:LeaveGroup`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Leaving the multi-room mode
- **operationId:** `multiroomLeaveGroup`
- **Responses:** `200` (Successful response)

### `multiroom:JoinGroup:IP={IP}:uuid={uuid}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Joining a multi-room group
- **operationId:** `multiroomJoinGroup`
- **Parameters:** `IP` (path, required, string); `uuid` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:SlaveDeviceName:{ip}:{str}`
- **Status:** CMD-WIIM-MULTIROOM-SLAVE-DEVICE-NAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room get slave device name
- **operationId:** `multiroomSlaveDeviceName`
- **Parameters:** `ip` (path, required, string); `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:subwooferForget:{"uuid":"{uuid}"}`
- **Status:** CMD-WIIM-MULTIROOM-SUBWOOFER-FORGET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room subwoofer forget
- **operationId:** `multiroomSubwooferForget`
- **Parameters:** `uuid` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:subwooferGetPairInfo`
- **Status:** CMD-WIIM-MULTIROOM-SUBWOOFER-GET-PAIR-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room subwoofer get pair info
- **operationId:** `multiroomSubwooferGetPairInfo`
- **Responses:** `200` (Successful response)

### `multiroom:ConfigGet:leadtime`
- **Status:** CMD-WIIM-MULTIROOM-CONFIG-GET-LEADTIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room get lead time
- **operationId:** `multiroomConfigGetLeadtime`
- **Responses:** `200` (Successful response)

### `multiroom:subwooferPair:{str}`
- **Status:** CMD-WIIM-MULTIROOM-SUBWOOFER-PAIR · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room subwoofer pair
- **operationId:** `multiroomSubwooferPair`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `multiroom:ConfigSet:leadtime:{str}`
- **Status:** CMD-WIIM-MULTIROOM-CONFIG-SET-LEADTIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Multi-room set lead time
- **operationId:** `multiroomConfigSetLeadtime`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setMRMSubLPF:{str}`
- **Status:** CMD-WIIM-SET-MRMSUB-LPF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set multiroom subwoofer LPF
- **operationId:** `setMRMSubLPF`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getSubLPF`
- **Status:** QRY-WIIM-GET-SUB-LPF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get subwoofer LPF
- **operationId:** `getSubLPF`
- **Responses:** `200` (Successful response)

### `setSubLPF:{str}`
- **Status:** CMD-WIIM-SET-SUB-LPF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set subwoofer LPF
- **operationId:** `setSubLPF`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getMRMSubLPF:{str}`
- **Status:** QRY-WIIM-GET-MRMSUB-LPF · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get multi-room sub LPF
- **operationId:** `getMRMSubLPF`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)


## Other

### `get_remote_volume_step`
- **Status:** QRY-WIIM-GET-REMOTE-VOLUME-STEP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the remote volume step
- **operationId:** `getRemoteVolumeStep`
- **Responses:** `200` → `object`

### `set_remote_volume_step:{n}`
- **Status:** CMD-WIIM-SET-REMOTE-VOLUME-STEP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the remote volume step
- **operationId:** `setRemoteVolumeStep`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getMvRemoteSilenceUpdateTime`
- **Status:** QRY-WIIM-GET-MV-REMOTE-SILENCE-UPDATE-TIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the MV remote silence update time
- **operationId:** `getMvRemoteSilenceUpdateTime`
- **Responses:** `200` → `object`

### `getSpdifOutMaxCap`
- **Status:** QRY-WIIM-GET-SPDIF-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get SPDIF output maximum capabilities
- **operationId:** `getSpdifOutMaxCap`
- **Responses:** `200` (Successful response)

### `getCoaxOutMaxCap`
- **Status:** QRY-WIIM-GET-COAX-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the maximum capabilities of the coaxial output
- **operationId:** `getCoaxOutMaxCap`
- **Responses:** `200` → `string`

### `getAuxVoltageSupportList`
- **Status:** QRY-WIIM-GET-AUX-VOLTAGE-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get auxiliary voltage support list
- **operationId:** `getAuxVoltageSupportList`
- **Responses:** `200` (Successful response)

### `audio_cast:get_speaker_list`
- **Status:** CMD-WIIM-AUDIO-CAST-GET-SPEAKER-LIST · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast get speaker list
- **operationId:** `audioCastGetSpeakerList`
- **Responses:** `200` (Successful response)

### `audio_cast:scan_speaker`
- **Status:** CMD-WIIM-AUDIO-CAST-SCAN-SPEAKER · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast scan speaker
- **operationId:** `audioCastScanSpeaker`
- **Responses:** `200` (Successful response)

### `audio_cast:speaker_get_transcode_buffer_time`
- **Status:** CMD-WIIM-AUDIO-CAST-SPEAKER-GET-TRANSCODE-BUFFER-TIME · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast get speaker transcode buffer time
- **operationId:** `audioCastSpeakerGetTranscodeBufferTime`
- **Responses:** `200` (Successful response)

### `audio_cast:speaker_get_transcode_profile`
- **Status:** CMD-WIIM-AUDIO-CAST-SPEAKER-GET-TRANSCODE-PROFILE · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast get speaker transcode profile
- **operationId:** `audioCastSpeakerGetTranscodeProfile`
- **Responses:** `200` (Successful response)

### `audio_cast:speaker_set_password:{str1}:{str2}`
- **Status:** CMD-WIIM-AUDIO-CAST-SPEAKER-SET-PASSWORD · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast set speaker password
- **operationId:** `audioCastSpeakerSetPassword`
- **Parameters:** `str1` (path, required, string); `str2` (path, required, string)
- **Responses:** `200` (Successful response)

### `audio_cast:speaker_set_volume:{str}:{volume}`
- **Status:** CMD-WIIM-AUDIO-CAST-SPEAKER-SET-VOLUME · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Audio Cast set speaker volume
- **operationId:** `audioCastSpeakerSetVolume`
- **Parameters:** `str` (path, required, string); `volume` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getSoundCardModeSupportList`
- **Status:** QRY-WIIM-GET-SOUND-CARD-MODE-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get sound card mode support list
- **operationId:** `getSoundCardModeSupportList`
- **Responses:** `200` (Successful response)

### `getActiveSoundCardOutputMode`
- **Status:** QRY-WIIM-GET-ACTIVE-SOUND-CARD-OUTPUT-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the active sound card output mode
- **operationId:** `getActiveSoundCardOutputMode`
- **Responses:** `200` → `object`

### `setLightOperationBrightConfig:{"auto_sense_enable":{s},"default_bright":{b},"disable":{d}}`
- **Status:** CMD-WIIM-SET-LIGHT-OPERATION-BRIGHT-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** WiiM Ultra enable/disable LCD
- **operationId:** `setLightOperationBrightConfig`
- **Parameters:** `s` (path, required, integer, default=0); `b` (path, required, integer, default=1); `d` (path, required, integer, enum=[0,1], default=1)
- **Responses:** `200` (Successful response)

### `getMvRemoteUpdateStartCheck`
- **Status:** QRY-WIIM-GET-MV-REMOTE-UPDATE-START-CHECK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Search for firmware updates available (check for updates)
- **operationId:** `getMvRemoteUpdateStartCheck`
- **Responses:** `200` → `string`

### `getMvRemoteUpdateStart`
- **Status:** QRY-WIIM-GET-MV-REMOTE-UPDATE-START · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start firmware update
- **operationId:** `getMvRemoteUpdateStart`
- **Responses:** `200` → `string`

### `getMvRemoteUpdateStatus`
- **Status:** QRY-WIIM-GET-MV-REMOTE-UPDATE-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Status of the update process
- **operationId:** `getMvRemoteUpdateStatus`
- **Responses:** `200` → `string`

### `getMvRomBurnPrecent`
- **Status:** QRY-WIIM-GET-MV-ROM-BURN-PRECENT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Status of the update process
- **operationId:** `getMvRomBurnPrecent`
- **Responses:** `200` → `object`

### `EasyLinkResponseStop`
- **Status:** CMD-WIIM-EASY-LINK-RESPONSE-STOP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** EasyLink response stop
- **operationId:** `easyLinkResponseStop`
- **Responses:** `200` (Successful response)

### `NotifyUpgradeType:firmware`
- **Status:** CMD-WIIM-NOTIFY-UPGRADE-TYPE-FIRMWARE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Notify upgrade type firmware
- **operationId:** `notifyUpgradeTypeFirmware`
- **Responses:** `200` (Successful response)

### `getLMPFilterCapability`
- **Status:** QRY-WIIM-GET-LMPFILTER-CAPABILITY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LMP filter capability
- **operationId:** `getLMPFilterCapability`
- **Responses:** `200` → `object`

### `getStreamServiceConfig:{source}`
- **Status:** QRY-WIIM-GET-STREAM-SERVICE-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get stream service config for a specific source
- **operationId:** `getStreamServiceConfig`
- **Parameters:** `source` (path, required, string)
- **Responses:** `200` (Successful response)

### `setHandshakeCode:{str}`
- **Status:** CMD-WIIM-SET-HANDSHAKE-CODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set handshake code
- **operationId:** `setHandshakeCode`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getsyslog:ip:{str}`
- **Status:** QRY-WIIM-GETSYSLOG-IP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get system log for a specific IP address
- **operationId:** `getsyslogIp`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getStatus:ip:{str}`
- **Status:** QRY-WIIM-GET-STATUS-IP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the device status
- **operationId:** `getStatusIp`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `GetUpdateServer`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get update server
- **operationId:** `getUpdateServer`
- **Responses:** `200` (Successful response)

### `getWeatherInfo`
- **Status:** QRY-WIIM-GET-WEATHER-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get weather info
- **operationId:** `getWeatherInfo`
- **Responses:** `200` (Successful response)

### `setAccessPIN:{"PIN":"{str}"}`
- **Status:** CMD-WIIM-SET-ACCESS-PIN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set access PIN
- **operationId:** `setAccessPIN`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setLanguage:{str}`
- **Status:** CMD-WIIM-SET-LANGUAGE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set language
- **operationId:** `setLanguage`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `AutoPlaySet`
- **Status:** CMD-WIIM-AUTO-PLAY-SET · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Auto play setting
- **operationId:** `autoPlaySet`
- **Responses:** `200` (Successful response)

### `getMvRomDownloadStatus`
- **Status:** QRY-WIIM-GET-MV-ROM-DOWNLOAD-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get MV ROM download status
- **operationId:** `getMvRomDownloadStatus`
- **Responses:** `200` → `object`

### `getMvRomDownloadV2Status`
- **Status:** QRY-WIIM-GET-MV-ROM-DOWNLOAD-V2STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get MV ROM download status V2
- **operationId:** `getMvRomDownloadV2Status`
- **Responses:** `200` → `object`

### `setHexGroupName:{str}`
- **Status:** CMD-WIIM-SET-HEX-GROUP-NAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set hex group name
- **operationId:** `setHexGroupName`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setMvRemoteSilenceOTATime:{str}`
- **Status:** CMD-WIIM-SET-MV-REMOTE-SILENCE-OTATIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set MV remote silence OTA time
- **operationId:** `setMvRemoteSilenceOTATime`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setMvRemoteSilenceUpdateTime:{str}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Set MV remote silence update time
- **operationId:** `setMvRemoteSilenceUpdateTime`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setTimezone:{str}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Set timezone
- **operationId:** `setTimezone`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `checkAccessPIN`
- **Status:** QRY-WIIM-CHECK-ACCESS-PIN · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Check access PIN
- **operationId:** `checkAccessPIN`
- **Responses:** `200` (Successful response)

### `SetUpdateServer:{str}`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Set update server
- **operationId:** `setUpdateServer`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setWeatherLocation:{str}`
- **Status:** CMD-WIIM-SET-WEATHER-LOCATION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set weather location
- **operationId:** `setWeatherLocation`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `StartCheck`
- **Status:** CMD-WIIM-START-CHECK · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start check
- **operationId:** `startCheck`
- **Responses:** `200` (Successful response)

### `getbatteryval`
- **Status:** QRY-WIIM-GETBATTERYVAL · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get battery value
- **operationId:** `getbatteryval`
- **Responses:** `200` (Successful response)

### `getAsrStatus`
- **Status:** QRY-WIIM-GET-ASR-STATUS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get Automatic Speech Recognition Status
- **operationId:** `getAsrStatus`
- **Responses:** `200` → `object`

### `getLPAuthCode:hostId={str}:clientId={str2}`
- **Status:** QRY-WIIM-GET-LPAUTH-CODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LP Auth Code
- **operationId:** `getLPAuthCode`
- **Parameters:** `str` (path, required, string); `str2` (path, required, string)
- **Responses:** `200` (Successful response)

### `setTokenParams:code={str}:redirect_uri={str2}`
- **Status:** CMD-WIIM-SET-TOKEN-PARAMS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set token parameters
- **operationId:** `setTokenParams`
- **Parameters:** `str` (path, required, string); `str2` (path, required, string)
- **Responses:** `200` (Successful response)

### `talksetPrompt:{n}`
- **Status:** CMD-WIIM-TALKSET-PROMPT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk prompt
- **operationId:** `talksetPrompt`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `talksetAlarmPreWake:{str}`
- **Status:** CMD-WIIM-TALKSET-ALARM-PRE-WAKE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk alarm pre-wake
- **operationId:** `talksetAlarmPreWake`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `talksetAlarmTone:{n}`
- **Status:** CMD-WIIM-TALKSET-ALARM-TONE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk alarm tone
- **operationId:** `talksetAlarmTone`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `talksetAlarmTonePreview:{n}`
- **Status:** CMD-WIIM-TALKSET-ALARM-TONE-PREVIEW · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk alarm tone preview
- **operationId:** `talksetAlarmTonePreview`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `talksetAlarmVolume:{n}`
- **Status:** CMD-WIIM-TALKSET-ALARM-VOLUME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk alarm volume
- **operationId:** `talksetAlarmVolume`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `talksetAlarmcommon:prewake:{str}:vol:{n1}:tone:{n2}`
- **Status:** CMD-WIIM-TALKSET-ALARMCOMMON · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set talk alarm common settings
- **operationId:** `talksetAlarmcommon`
- **Parameters:** `str` (path, required, string); `n1` (path, required, integer); `n2` (path, required, integer)
- **Responses:** `200` (Successful response)

### `SetSyncPlayExtraDelay:{n}`
- **Status:** CMD-WIIM-SET-SYNC-PLAY-EXTRA-DELAY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set sync play extra delay
- **operationId:** `setSyncPlayExtraDelay`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `setInitialConfiguration:{n}`
- **Status:** CMD-WIIM-SET-INITIAL-CONFIGURATION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set initial configuration
- **operationId:** `setInitialConfiguration`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `get_ui_config`
- **Status:** QRY-WIIM-GET-UI-CONFIG · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get UI config
- **operationId:** `getUiConfig`
- **Responses:** `200` (Successful response)

### `getSpdifAutoSenseEnable`
- **Status:** QRY-WIIM-GET-SPDIF-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get SPDIF auto-sense enable status
- **operationId:** `getSpdifAutoSenseEnable`
- **Responses:** `200` (Successful response)

### `getSpdifInNoiseRemove`
- **Status:** QRY-WIIM-GET-SPDIF-IN-NOISE-REMOVE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get SPDIF input noise removal status
- **operationId:** `getSpdifInNoiseRemove`
- **Responses:** `200` (Successful response)

### `PHONO_MODE_SWITCH_SET:{str}`
- **Status:** CMD-WIIM-PHONO-MODE-SWITCH-SET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Phono mode switch set
- **operationId:** `phonoModeSwitchSet`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setPlayModeVolumeEnable:{str}`
- **Status:** CMD-WIIM-SET-PLAY-MODE-VOLUME-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set play mode volume enable
- **operationId:** `setPlayModeVolumeEnable`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `get_ui_wallpaper_list`
- **Status:** QRY-WIIM-GET-UI-WALLPAPER-LIST · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get UI wallpaper list
- **operationId:** `getUiWallpaperList`
- **Responses:** `200` (Successful response)

### `setPlayModeVolumeValue:{str}`
- **Status:** CMD-WIIM-SET-PLAY-MODE-VOLUME-VALUE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set play mode volume value
- **operationId:** `setPlayModeVolumeValue`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setPowerModeTime:{"idleInterval":"{str}"}`
- **Status:** CMD-WIIM-SET-POWER-MODE-TIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set power mode time
- **operationId:** `setPowerModeTime`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `get_button_volume_step`
- **Status:** QRY-WIIM-GET-BUTTON-VOLUME-STEP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get the volume step of the buttons
- **operationId:** `getButtonVolumeStep`
- **Responses:** `200` → `object`

### `set_button_volume_step:{str}`
- **Status:** CMD-WIIM-SET-BUTTON-VOLUME-STEP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set the volume step of the buttons
- **operationId:** `setButtonVolumeStep`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getAuxAutoSenseEnable`
- **Status:** QRY-WIIM-GET-AUX-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get AUX auto-sense enable status
- **operationId:** `getAuxAutoSenseEnable`
- **Responses:** `200` → `integer`

### `set_ui_config:{str}`
- **Status:** CMD-WIIM-SET-UI-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set UI config
- **operationId:** `setUiConfig`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setSpdifAutoSenseEnable:{n}`
- **Status:** CMD-WIIM-SET-SPDIF-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set SPDIF auto-sense enable
- **operationId:** `setSpdifAutoSenseEnable`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `setSpdifInNoiseRemove:{str}`
- **Status:** CMD-WIIM-SET-SPDIF-IN-NOISE-REMOVE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set SPDIF input noise removal
- **operationId:** `setSpdifInNoiseRemove`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getChannelMode`
- **Status:** QRY-WIIM-GET-CHANNEL-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get channel mode
- **operationId:** `getChannelMode`
- **Responses:** `200` → `integer`

### `getAutoSenseEnable`
- **Status:** QRY-WIIM-GET-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get auto-sense enable status
- **operationId:** `getAutoSenseEnable`
- **Responses:** `200` → `integer`

### `StartRebootTime:1`
- **Status:** CMD-WIIM-START-REBOOT-TIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Start reboot time
- **operationId:** `startRebootTime`
- **Responses:** `200` (Successful response)

### `LED_SWITCH_GET`
- **Status:** QRY-WIIM-LED-SWITCH-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LED switch status
- **operationId:** `ledSwitchGet`
- **Responses:** `200` (Successful response)

### `getMQAReceiverCap`
- **Status:** QRY-WIIM-GET-MQARECEIVER-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get MQA receiver capacity
- **operationId:** `getMQAReceiverCap`
- **Responses:** `200` → `integer`

### `Reload_Button_GET`
- **Status:** CMD-WIIM-RELOAD-BUTTON-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Reload button status
- **operationId:** `reloadButtonGet`
- **Responses:** `200` (Successful response)

### `setAuxAutoSenseEnable:{n}`
- **Status:** CMD-WIIM-SET-AUX-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set AUX auto-sense enable
- **operationId:** `setAuxAutoSenseEnable`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getLowPriorityPromptDisable`
- **Status:** QRY-WIIM-GET-LOW-PRIORITY-PROMPT-DISABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get low priority prompt disable status
- **operationId:** `getLowPriorityPromptDisable`
- **Responses:** `200` → `integer`

### `getSoftMute`
- **Status:** QRY-WIIM-GET-SOFT-MUTE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get soft mute status
- **operationId:** `getSoftMute`
- **Responses:** `200` (Successful response)

### `getLineInMaxCap`
- **Status:** QRY-WIIM-GET-LINE-IN-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get LINE IN maximum capacity
- **operationId:** `getLineInMaxCap`
- **Responses:** `200` → `string`

### `getAuxInMaxCap`
- **Status:** QRY-WIIM-GET-AUX-IN-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get AUX input maximum capacity
- **operationId:** `getAuxInMaxCap`
- **Responses:** `200` → `string`

### `getUacOutMaxCap`
- **Status:** QRY-WIIM-GET-UAC-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get UAC output maximum capacity
- **operationId:** `getUacOutMaxCap`
- **Responses:** `200` (Successful response)

### `getHDMIAutoSenseEnable`
- **Status:** QRY-WIIM-GET-HDMIAUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get HDMI auto-sense enable
- **operationId:** `getHDMIAutoSenseEnable`
- **Responses:** `200` → `integer`

### `setChannelMode:{n}`
- **Status:** CMD-WIIM-SET-CHANNEL-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set channel mode
- **operationId:** `setChannelMode`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `GetSyncPlayExtraDelay`
- **Status:** QRY-WIIM-GET-SYNC-PLAY-EXTRA-DELAY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get sync play extra delay
- **operationId:** `getSyncPlayExtraDelay`
- **Responses:** `200` (Successful response)

### `getLightOperationBrightConfig`
- **Status:** QRY-WIIM-GET-LIGHT-OPERATION-BRIGHT-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get light operation brightness configuration
- **operationId:** `getLightOperationBrightConfig`
- **Responses:** `200` (Successful response)

### `set_ui_wallpaper_list:{str}`
- **Status:** CMD-WIIM-SET-UI-WALLPAPER-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set UI wallpaper list
- **operationId:** `setUiWallpaperList`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getMainSubExtraDelay`
- **Status:** QRY-WIIM-GET-MAIN-SUB-EXTRA-DELAY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get main/sub extra delay
- **operationId:** `getMainSubExtraDelay`
- **Responses:** `200` → `object`

### `Cast:Disable`
- **Status:** CMD-WIIM-CAST-DISABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disable Cast
- **operationId:** `castDisable`
- **Responses:** `200` (Successful response)

### `Cast:DisableUsageReport`
- **Status:** CMD-WIIM-CAST-DISABLE-USAGE-REPORT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disable usage report for Cast
- **operationId:** `castDisableUsageReport`
- **Responses:** `200` (Successful response)

### `setAutoSenseEnable:{str}`
- **Status:** CMD-WIIM-SET-AUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set auto-sense enable
- **operationId:** `setAutoSenseEnable`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `PHONO_MODE_SWITCH_GET`
- **Status:** QRY-WIIM-PHONO-MODE-SWITCH-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get phono mode switch state
- **operationId:** `phonoModeSwitchGet`
- **Responses:** `200` (Successful response)

### `getPlayModeVolumeEnable`
- **Status:** QRY-WIIM-GET-PLAY-MODE-VOLUME-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get play mode volume enable
- **operationId:** `getPlayModeVolumeEnable`
- **Responses:** `200` (Successful response)

### `setVolumeControl:{n}`
- **Status:** CMD-WIIM-SET-VOLUME-CONTROL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set volume control
- **operationId:** `setVolumeControl`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getPlayModeVolumeValue`
- **Status:** QRY-WIIM-GET-PLAY-MODE-VOLUME-VALUE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get play mode volume value
- **operationId:** `getPlayModeVolumeValue`
- **Responses:** `200` (Successful response)

### `setMQAReceiverCap:{str}`
- **Status:** CMD-WIIM-SET-MQARECEIVER-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set MQA receiver capacity
- **operationId:** `setMQAReceiverCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getPowerModeTime`
- **Status:** QRY-WIIM-GET-POWER-MODE-TIME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get power mode time
- **operationId:** `getPowerModeTime`
- **Responses:** `200` (Successful response)

### `setMaxVolume:{n}`
- **Status:** CMD-WIIM-SET-MAX-VOLUME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set max volume
- **operationId:** `setMaxVolume`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `Cast:EnableCast`
- **Status:** CMD-WIIM-ENABLE-CAST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable Cast
- **operationId:** `enableCast`
- **Responses:** `200` (Successful response)

### `Reload_Button_UPDATE:{str}`
- **Status:** CMD-WIIM-RELOAD-BUTTON-UPDATE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Reload button update
- **operationId:** `reloadButtonUpdate`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `Cast:EnableUsageReport`
- **Status:** CMD-WIIM-ENABLE-CAST-USAGE-REPORT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable usage report for Cast
- **operationId:** `enableCastUsageReport`
- **Responses:** `200` (Successful response)

### `disableLowPriorityPrompt:{str}`
- **Status:** CMD-WIIM-DISABLE-LOW-PRIORITY-PROMPT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Disable low priority prompt
- **operationId:** `disableLowPriorityPrompt`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setSoftMute:{str}`
- **Status:** CMD-WIIM-SET-SOFT-MUTE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set soft mute
- **operationId:** `setSoftMute`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setHDMIAutoSenseEnable:{n}`
- **Status:** CMD-WIIM-SET-HDMIAUTO-SENSE-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set HDMI auto-sense enable
- **operationId:** `setHDMIAutoSenseEnable`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `setSpdifOutMaxCap:{str}`
- **Status:** CMD-WIIM-SET-SPDIF-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set SPDIF output max capacity
- **operationId:** `setSpdifOutMaxCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setCoaxOutMaxCap:{str}`
- **Status:** CMD-WIIM-SET-COAX-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set coaxial output max capacity
- **operationId:** `setCoaxOutMaxCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setLineInMaxCap:{str}`
- **Status:** CMD-WIIM-SET-LINE-IN-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set line input max capacity
- **operationId:** `setLineInMaxCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setAuxInMaxCap:{str}`
- **Status:** CMD-WIIM-SET-AUX-IN-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set auxiliary input max capacity
- **operationId:** `setAuxInMaxCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setUacOutMaxCap:{str}`
- **Status:** CMD-WIIM-SET-UAC-OUT-MAX-CAP · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set UAC out max cap
- **operationId:** `setUacOutMaxCap`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `EnableSysInfo:{n}`
- **Status:** CMD-WIIM-ENABLE-SYS-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Enable system information output
- **operationId:** `enableSysInfo`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `GetAirplayExtraDelay`
- **Status:** QRY-WIIM-GET-AIRPLAY-EXTRA-DELAY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get AirPlay extra delay
- **operationId:** `getAirplayExtraDelay`
- **Responses:** `200` → `object`

### `GetCurrentWirelessConnect`
- **Status:** QRY-WIIM-GET-CURRENT-WIRELESS-CONNECT · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get current wireless connection information
- **operationId:** `getCurrentWirelessConnect`
- **Responses:** `200` (Successful response)

### `SlaveIP:{ip}:alertget`
- **Status:** CMD-WIIM-SLAVE-ALERT-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Slave alert get
- **operationId:** `slaveAlertGet`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `SlaveIP:{ip}:talksetAlarmVolume:{n}`
- **Status:** CMD-WIIM-SLAVE-TALK-SET-ALARM-VOLUME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Slave set alarm volume
- **operationId:** `slaveTalkSetAlarmVolume`
- **Parameters:** `ip` (path, required, string); `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `Squeezelite:autoConnectEnable:{n}`
- **Status:** CMD-WIIM-SQUEEZELITE-AUTO-CONNECT-ENABLE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Squeezelite auto connect enable
- **operationId:** `squeezeliteAutoConnectEnable`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `Squeezelite:connectServer:{ip}`
- **Status:** CMD-WIIM-SQUEEZELITE-CONNECT-SERVER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Squeezelite connect server
- **operationId:** `squeezeliteConnectServer`
- **Parameters:** `ip` (path, required, string)
- **Responses:** `200` (Successful response)

### `Squeezelite:discover`
- **Status:** CMD-WIIM-SQUEEZELITE-DISCOVER · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Squeezelite discover
- **operationId:** `squeezeliteDiscover`
- **Responses:** `200` (Successful response)

### `Squeezelite:getState`
- **Status:** CMD-WIIM-SQUEEZELITE-GET-STATE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Squeezelite get state
- **operationId:** `squeezeliteGetState`
- **Responses:** `200` (Successful response)

### `getSetupRouterInfo`
- **Status:** QRY-WIIM-GET-SETUP-ROUTER-INFO · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get setup router information
- **operationId:** `getSetupRouterInfo`
- **Responses:** `200` (Successful response)

### `setSetupRouterInfo:{str}`
- **Status:** CMD-WIIM-SET-SETUP-ROUTER-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set setup router information
- **operationId:** `setSetupRouterInfo`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `alertget`
- **Status:** CMD-WIIM-ALERT-GET · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Alert get
- **operationId:** `alertGet`
- **Responses:** `200` (Successful response)

### `TvsLogout`
- **Status:** CMD-WIIM-TVS-LOGOUT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** TVS logout
- **operationId:** `tvsLogout`
- **Responses:** `200` (Successful response)

### `TvsState`
- **Status:** QRY-WIIM-GET-TVS-STATE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get TVS state
- **operationId:** `getTvsState`
- **Responses:** `200` (Successful response)

### `getTvsDevInfo`
- **Status:** QRY-WIIM-GET-TVS-DEV-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get TVS device information
- **operationId:** `getTvsDevInfo`
- **Responses:** `200` (Successful response)

### `setTVSAccessToken:{str}`
- **Status:** CMD-WIIM-SET-TVSACCESS-TOKEN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TVS access token
- **operationId:** `setTVSAccessToken`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setTVSDebugMode:{str}`
- **Status:** CMD-WIIM-SET-TVSDEBUG-MODE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TVS debug mode
- **operationId:** `setTVSDebugMode`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setTvsClientID:{str}`
- **Status:** CMD-WIIM-SET-TVS-CLIENT-ID · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TVS client ID
- **operationId:** `setTvsClientID`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `createRoutine:{str}`
- **Status:** CMD-WIIM-CREATE-ROUTINE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Create routine
- **operationId:** `createRoutine`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getAllRoutines`
- **Status:** QRY-WIIM-GET-ALL-ROUTINES · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get all routines
- **operationId:** `getAllRoutines`
- **Responses:** `200` → `object`

### `getRoutineCapability`
- **Status:** QRY-WIIM-GET-ROUTINE-CAPABILITY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get routine capability
- **operationId:** `getRoutineCapability`
- **Responses:** `200` → `object`

### `getAudioInputCapbility`
- **Status:** QRY-WIIM-GET-AUDIO-INPUT-CAPABILITY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get audio input capability
- **operationId:** `getAudioInputCapability`
- **Responses:** `200` → `object`

### `getAudioOutMax32bit`
- **Status:** QRY-WIIM-GET-AUDIO-OUT-MAX32BIT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get audio output maximum 32-bit support
- **operationId:** `getAudioOutMax32bit`
- **Responses:** `200` → `object`

### `setAudioOutMax32bit:{n}`
- **Status:** CMD-WIIM-SET-AUDIO-OUT-MAX32BIT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set audio output maximum 32-bit support
- **operationId:** `setAudioOutMax32bit`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getAudioOutputVrms:{str}`
- **Status:** QRY-WIIM-GET-AUDIO-OUTPUT-VRMS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get audio output VRMS for a specific output
- **operationId:** `getAudioOutputVrms`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getAudioOutputVrmsSupportList`
- **Status:** QRY-WIIM-GET-AUDIO-OUTPUT-VRMS-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get list of audio outputs that support VRMS
- **operationId:** `getAudioOutputVrmsSupportList`
- **Responses:** `200` (Successful response)

### `setAudioOutputVrms:{str}`
- **Status:** CMD-WIIM-SET-AUDIO-OUTPUT-VRMS · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set audio output VRMS for a specific output
- **operationId:** `setAudioOutputVrms`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getCBLStatus`
- **Status:** QRY-WIIM-GET-CBLSTATUS · SOURCE-DOCUMENTED · DEPRECATED · NOT-HW-VERIFIED
- **Summary:** Get CBL status
- **operationId:** `getCBLStatus`
- **Responses:** `200` (Successful response)

### `getCecPowerCtrl`
- **Status:** QRY-WIIM-GET-CEC-POWER-CTRL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get CEC power control status
- **operationId:** `getCecPowerCtrl`
- **Responses:** `200` → `integer`

### `setCecPowerCtrl:{n}`
- **Status:** CMD-WIIM-SET-CEC-POWER-CTRL · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set CEC power control status
- **operationId:** `setCecPowerCtrl`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getCxdishPrecent`
- **Status:** QRY-WIIM-GET-CXDISH-PRECENT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get CXDISH percentage
- **operationId:** `getCxdishPrecent`
- **Responses:** `200` → `object`

### `getDigitalFilterTypeSupportList`
- **Status:** QRY-WIIM-GET-DIGITAL-FILTER-TYPE-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get list of supported digital filter types
- **operationId:** `getDigitalFilterTypeSupportList`
- **Responses:** `200` → `object`

### `getDigitalFilterType`
- **Status:** QRY-WIIM-GET-DIGITAL-FILTER-TYPE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get current digital filter type
- **operationId:** `getDigitalFilterType`
- **Responses:** `200` → `integer`

### `setDigitalFilterType:{n}`
- **Status:** CMD-WIIM-SET-DIGITAL-FILTER-TYPE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set digital filter type
- **operationId:** `setDigitalFilterType`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getOutputDigitalFilterType:{str}`
- **Status:** QRY-WIIM-GET-OUTPUT-DIGITAL-FILTER-TYPE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get current output digital filter type
- **operationId:** `getOutputDigitalFilterType`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getOutputDigitalFilterTypeSupportList`
- **Status:** QRY-WIIM-GET-OUTPUT-DIGITAL-FILTER-TYPE-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get list of supported output digital filter types
- **operationId:** `getOutputDigitalFilterTypeSupportList`
- **Responses:** `200` (Successful response)

### `setOutputDigitalFilterType:{str}`
- **Status:** CMD-WIIM-SET-OUTPUT-DIGITAL-FILTER-TYPE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set output digital filter type
- **operationId:** `setOutputDigitalFilterType`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `getDigitalInputAudioTypeSupport`
- **Status:** QRY-WIIM-GET-DIGITAL-INPUT-AUDIO-TYPE-SUPPORT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get supported digital input audio types
- **operationId:** `getDigitalInputAudioTypeSupport`
- **Responses:** `200` → `string`

### `getOutputVoltage`
- **Status:** QRY-WIIM-GET-OUTPUT-VOLTAGE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get output voltage
- **operationId:** `getOutputVoltage`
- **Responses:** `200` → `integer`

### `setOutputVoltage:{n}`
- **Status:** CMD-WIIM-SET-OUTPUT-VOLTAGE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set output voltage
- **operationId:** `setOutputVoltage`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getFeatureCapbility`
- **Status:** QRY-WIIM-GET-FEATURE-CAPABILITY · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get feature capability
- **operationId:** `getFeatureCapability`
- **Responses:** `200` (Successful response)

### `getPlayModeGainConfig`
- **Status:** QRY-WIIM-GET-PLAY-MODE-GAIN-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get play mode gain configuration
- **operationId:** `getPlayModeGainConfig`
- **Responses:** `200` (Successful response)

### `setPlayModeGainConfig:{str}`
- **Status:** CMD-WIIM-SET-PLAY-MODE-GAIN-CONFIG · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set play mode gain configuration
- **operationId:** `setPlayModeGainConfig`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `mediaserver:scan`
- **Status:** CMD-WIIM-MEDIASERVER-SCAN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Media server scan
- **operationId:** `mediaserverScan`
- **Responses:** `200` (Successful response)

### `mediaserver:udiskumount`
- **Status:** CMD-WIIM-MEDIASERVER-UDISKUMOUNT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Media server USB disk unmount
- **operationId:** `mediaserverUdiskumount`
- **Responses:** `200` (Successful response)

### `getInputModeSupportList`
- **Status:** QRY-WIIM-GET-INPUT-MODE-SUPPORT-LIST · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get list of supported input modes
- **operationId:** `getInputModeSupportList`
- **Responses:** `200` (Successful response)

### `getModeRename`
- **Status:** QRY-WIIM-GET-MODE-RENAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get input mode rename information
- **operationId:** `getModeRename`
- **Responses:** `200` → `object`

### `setModeRename:{str}`
- **Status:** CMD-WIIM-SET-MODE-RENAME · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set input mode rename information
- **operationId:** `setModeRename`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

### `setMusicExplicit:{n}`
- **Status:** CMD-WIIM-SET-MUSIC-EXPLICIT · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set music explicit content filter
- **operationId:** `setMusicExplicit`
- **Parameters:** `n` (path, required, integer)
- **Responses:** `200` (Successful response)

### `getMvRemoteUpdateDeviceOtaInfo`
- **Status:** QRY-WIIM-GET-MV-REMOTE-UPDATE-DEVICE-OTA-INFO · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Get MV remote update device OTA information
- **operationId:** `getMvRemoteUpdateDeviceOtaInfo`
- **Responses:** `200` → `object`

### `setTuneinFavoriteState:songId={songId}:statu={status}`
- **Status:** CMD-WIIM-SET-TUNEIN-FAVORITE-STATE · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TuneIn favorite state for a song
- **operationId:** `setTuneinFavoriteState`
- **Parameters:** `songId` (path, required, string); `status` (path, required, integer)
- **Responses:** `200` (Successful response)

### `setTuneinLocation:latitude={latitude}:longitude={longitude}:serial={serial}`
- **Status:** CMD-WIIM-SET-TUNEIN-LOCATION · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TuneIn location information
- **operationId:** `setTuneinLocation`
- **Parameters:** `latitude` (path, required, string); `longitude` (path, required, string); `serial` (path, required, string)
- **Responses:** `200` (Successful response)

### `setTuneinToken:username={username}:token={token}:refreshToken={refreshToken}:expires_in={expires_in}:userid={userid}`
- **Status:** CMD-WIIM-SET-TUNEIN-TOKEN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Set TuneIn authentication token information
- **operationId:** `setTuneinToken`
- **Parameters:** `username` (path, required, string); `token` (path, required, string); `refreshToken` (path, required, string); `expires_in` (path, required, integer); `userid` (path, required, string)
- **Responses:** `200` (Successful response)

### `streamServicesCapability`
- **Status:** REUSED EXISTING CANONICAL ID
- **Summary:** Get streaming services capabilities
- **operationId:** `streamServicesCapability`
- **Responses:** `200` → `object`

### `tidallogin:oauthcode={str}`
- **Status:** CMD-WIIM-TIDAL-LOGIN · SOURCE-DOCUMENTED · NOT-HW-VERIFIED
- **Summary:** Tidal login using OAuth code
- **operationId:** `tidalLogin`
- **Parameters:** `str` (path, required, string)
- **Responses:** `200` (Successful response)

