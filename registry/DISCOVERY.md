# Discovery Registry

## A33 native UDP beacon — DISC-A33-001
Observed broadcast:
- destination: `255.255.255.255:53308`
- JSON fields: `product_type`, `net`, `host`, `port`, `eth0_mac`, `wlan0_mac`
- observed `product_type`: `EC04`
- observed advertised `port`: `16800`
- status: CAPTURED

Do not assume port 16800 is a control API until separately verified.

## A33 SSDP/UPnP
Observed:
- multicast `239.255.255.250:1900`
- `RenderingControl:1`
- `QPlay:1`
- device description on an HTTP port observed in capture

## A33 mDNS
Observed Spotify Connect advertisement: `_spotify-connect._tcp.local`.

## Global online rule
A persisted/saved device is not automatically Online. Online requires a real discovery or successful status response.
