# PlayQueue SetMediaServerInfo — WiiM Home

Recovered from decompiled `ylb.java`.

WiiM Home constructs a controller-side identity object containing:
- name = Android_<brand>_<model>_RemoteLocal
- uuid
- controller IP
- media_port

It then targets:

`http://<device-ip>:59152/upnp/control/PlayQueue1`

with SOAPAction:

`urn:schemas-wiimu-com:service:PlayQueue:1#SetMediaServerInfo`

This is important for airControl local-library playback: it is evidence of a
protocol path by which the controller advertises its own local media server to
the renderer.

Status: APK-VERIFIED / NOT-HW-VERIFIED.

Do not assume port 59152 replaces the dynamically discovered PlayQueue endpoint;
WiiM Home contains multiple PlayQueue access paths.
