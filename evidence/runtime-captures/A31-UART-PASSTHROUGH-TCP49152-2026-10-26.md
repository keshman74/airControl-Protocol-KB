# A31 UART-pass-through attempt and TCP/49152 evidence (2026-10-26)

Status: **HW-VERIFIED network capture; NOT-UART-CAPTURED**.

Source PCAP: ` /tmp/a31-capture.pcap `, SHA-256 `fb0786e525cbc3de89159fa4482512d352fbf03e5ea26391c8295a8e878b1420`. Capture was made on Mac `en0` while 4STREAM/airCloudCTRL controlled A31 `192.168.0.192`.

## Result

No packets to TCP/8899 were observed. The application instead used:

- TCP/80: periodic `GET /httpapi.asp?command=getStatusEx` and `GET /httpapi.asp?command=getPlayerStatus` (about every 5 seconds).
- TCP/49152: UPnP SOAP control channel. Client sends `POST /upnp/control/rendertransport1`, `SOAPAction: urn:schemas-upnp-org:service:AVTransport:1#GetPositionInfo`, `Host: 192.168.0.192:49152`, `User-Agent: airCloudCTRL/3.0.2`.
- The response contains escaped DIDL-Lite metadata and `<upnp:albumArtURI>`, e.g. `http://cdn-profiles.tunein.com/s309634/images/logog.jpg?t=637478745240000000`.

The capture also showed `getPlayerStatus` volume values changing (21, 63, then 42) while no 8899 traffic appeared. This means the observed volume-control session is represented through the HTTP/UPnP control plane, not the exposed UART pass-through.

## Interpretation

`uart_pass_port:8899` remains an image/status-confirmed local pass-through endpoint, but 4STREAM did not open it during this user action. A physical UART probe or an application/device path that explicitly opens 8899 is still required to claim UART byte framing. TCP/49152 is an UPnP AVTransport endpoint, not UART.

Evidence class: **HW-VERIFIED for the recorded A31 network behavior; NOT-HW-VERIFIED for UART framing**.
