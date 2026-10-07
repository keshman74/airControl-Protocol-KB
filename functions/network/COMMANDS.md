# Network command view

- A31: `QRY-A31-STATIC-IP`, `CMD-A31-DHCP`, `CMD-A31-STATIC-IP` — **CONFIRMED**.
- Linkplay: `QRY-LP-WIFI-STATE`, `QRY-LP-SCAN-APS`, `CMD-LP-CONNECT-AP` — **DOCUMENTED/IMPLEMENTED**.
- ACS2: `QRY-ACS2-WIFI-STATE`, `QRY-ACS2-SCAN-APS`, `CMD-ACS2-CONNECT-AP`, `CMD-ACS2-STATIC-SWITCH`, `CMD-ACS2-STATIC-IP` — **DOCUMENTED** or **DOCUMENTED/IMPLEMENTED** as recorded in registry.


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98 is **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-GET-STATIC-IP-INFO` — `getStaticIpInfo` — Get the static IP information — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-STATIC-IP` — `setWlanStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}` — Set static WLAN network config — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ETH-STATIC-IP` — `setEthStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}` — Set static Ethernet network config — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-SSID` — `setSSID:{value}` — Change the SSID name of the device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK` — `setNetwork:{n}:{password}` — Setting the password WIFI — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK-PREFER-DNS` — `getNetworkPreferDNS` — Get the preferred DNS server — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-BAND-CONFIG` — `getWlanBandConfig` — Get the WLAN band configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-ROAM-CONFIG` — `getWlanRoamConfig` — Get the WLAN roaming configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-IPV6ENABLE` — `getIPV6Enable` — Get IPV6 enable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-POWER-WIFI-DOWN` — `setPowerWifiDown` — Stop WIFI signal — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-CONNECT-HIDE-AP` — `wlanConnectHideAp:{str}` — WLAN connect to hidden AP — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-CONNECT-HIDE-AP-EX` — `wlanConnectHideApEx:{str1}:{str2}:{str3}` — WLAN connect to hidden AP with extra parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK` — `getNetwork` — Get the network configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-WLAN-GET-AP-LIST-EX` — `wlanGetApListEx` — Get WLAN AP list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-HIDE-SSID` — `setHideSSID:{str}` — Set hide SSID — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK-EX-AES` — `setNetworkExAES:{n}:{password}` — Set network with AES encryption — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-BAND-CONFIG` — `setWlanBandConfig:{str}` — Set WLAN band configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-CONNECT-DISABLE` — `setWlanConnectDisable:{str}` — Set WLAN connect disable — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-ROAM-CONFIG` — `setWlanRoamConfig:{str}` — Set WLAN roam configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK-PREFER-DNS` — `setNetworkPreferDNS:{str}` — Set network preferred DNS — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-WLAN-GET-AP-FULL-LIST` — `wlanGetApFullList` — Get WLAN AP list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-SWITCH-CONNECTED-AP` — `wlanSwitchConnectedAp:ssid={ssid}:bssid={bssid}` — Wlan switch connected AP — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-IPV6ENABLE` — `setIPV6Enable:{str}` — Set IPv6 enable — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-CONNECT-DISABLE-STATUS` — `getWlanConnectDisableStatus` — Get WLAN connect disable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK-HEALTH` — `getNetworkHealth` — Get network health status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSCANNEL` — `wpscannel` — WPS Channel — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSCLIENTMODE` — `wpsclientmode` — WPS Client Mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSSERVERMODE` — `wpsservermode` — WPS Server Mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-GET-STATIC-IP-INFO` — `getStaticIpInfo` — Get the static IP information — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-STATIC-IP` — `setWlanStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}` — Set static WLAN network config — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ETH-STATIC-IP` — `setEthStaticIp:{IpAddress}:{GatewayIp}:{DnsServerIp}` — Set static Ethernet network config — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-SSID` — `setSSID:{value}` — Change the SSID name of the device — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK` — `setNetwork:{n}:{password}` — Setting the password WIFI — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK-PREFER-DNS` — `getNetworkPreferDNS` — Get the preferred DNS server — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-BAND-CONFIG` — `getWlanBandConfig` — Get the WLAN band configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-ROAM-CONFIG` — `getWlanRoamConfig` — Get the WLAN roaming configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-IPV6ENABLE` — `getIPV6Enable` — Get IPV6 enable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-POWER-WIFI-DOWN` — `setPowerWifiDown` — Stop WIFI signal — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-CONNECT-HIDE-AP` — `wlanConnectHideAp:{str}` — WLAN connect to hidden AP — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-CONNECT-HIDE-AP-EX` — `wlanConnectHideApEx:{str1}:{str2}:{str3}` — WLAN connect to hidden AP with extra parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK` — `getNetwork` — Get the network configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-WLAN-GET-AP-LIST-EX` — `wlanGetApListEx` — Get WLAN AP list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-HIDE-SSID` — `setHideSSID:{str}` — Set hide SSID — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK-EX-AES` — `setNetworkExAES:{n}:{password}` — Set network with AES encryption — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-BAND-CONFIG` — `setWlanBandConfig:{str}` — Set WLAN band configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-CONNECT-DISABLE` — `setWlanConnectDisable:{str}` — Set WLAN connect disable — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-WLAN-ROAM-CONFIG` — `setWlanRoamConfig:{str}` — Set WLAN roam configuration — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-NETWORK-PREFER-DNS` — `setNetworkPreferDNS:{str}` — Set network preferred DNS — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-WLAN-GET-AP-FULL-LIST` — `wlanGetApFullList` — Get WLAN AP list — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WLAN-SWITCH-CONNECTED-AP` — `wlanSwitchConnectedAp:ssid={ssid}:bssid={bssid}` — Wlan switch connected AP — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-IPV6ENABLE` — `setIPV6Enable:{str}` — Set IPv6 enable — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-WLAN-CONNECT-DISABLE-STATUS` — `getWlanConnectDisableStatus` — Get WLAN connect disable status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-GET-NETWORK-HEALTH` — `getNetworkHealth` — Get network health status — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSCANNEL` — `wpscannel` — WPS Channel — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSCLIENTMODE` — `wpsclientmode` — WPS Client Mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-WPSSERVERMODE` — `wpsservermode` — WPS Server Mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
