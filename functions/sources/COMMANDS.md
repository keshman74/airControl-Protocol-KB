# Sources command view

- `CMD-A31-SOURCE-AUX`, `CMD-A31-SOURCE-USB` — **CONFIRMED**.
- `CMD-A31-SOURCE-LINEIN-AUX` — **REJECTED** for AUX on tested A31.
- `CMD-ACS2-SOURCE` — **DOCUMENTED**; modes include Network, Bluetooth, LineIn, USBDisk, OpticalIn, HDMIARC, RCAIn, RCA2 In, PHONO In.
- `CMD-UPNP-PQ-TAKE-CONTROL(Source, Switch)` — **SCPD-DOCUMENTED / NOT-PER-ACTION-HW-VERIFIED**.


## Exact historical A31 tokens

`CMD-A31-SOURCE-AUX` — `setPlayerCmd:switchmode:AUX%20In`; `CMD-A31-SOURCE-USB` — `setPlayerCmd:switchmode:USB%20Disk`. `CMD-A31-SOURCE-LINEIN-AUX` — `setPlayerCmd:switchmode:LineIn`, REJECTED на тестовом A31. Не заменять автоматически Arylic `line-in/udisk` из другого product/firmware. [Определения](../../protocols/linkplay-http-https/COMMANDS.md), [KB-C24](../../KB_CONFLICTS.md).
