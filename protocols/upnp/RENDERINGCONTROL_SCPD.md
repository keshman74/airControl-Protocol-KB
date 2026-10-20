# RenderingControl SCPD recovered during CHAT-AUDIT-02

The WiiM Home decompiled-source dumps contain an embedded RenderingControl
service description. It exposes more than StreamServicesCapability.

Recovered actions now registered:
GetVolume / SetVolume, GetMute / SetMute, GetChannel / SetChannel,
GetEqualizer / SetEqualizer, ListPresets / SelectPreset,
GetSimpleDeviceInfo, GetControlDeviceInfo, MultiPlaySlaveMask,
SetAlarmQueue / GetAlarmQueue / DeleteAlarmQueue, SetDeviceName,
AirplayAutoSyncDelay, AutoSyncDelaySub.

Important state constraints:
- Volume: ui2, 0..100, step 1
- Channel input allowed values: Master, Single
- LastChange: evented
- AirplayAutoSyncDelay and AutoSyncDelaySub: Start / Stop

Status rule: the RenderingControl endpoint is hardware-observed on tested
devices, but the presence of an action in recovered SCPD is not promoted to
hardware-confirmed execution until a request/response test exists.

## A97 advertised services — hardware observation, 2026-10-20
Tested A97 zone Кухня at192.168.0.99. User's namespace-tolerant description.xml diagnostic returned HTTP200,3125 bytes and five advertised services on each of ports49152 and59152: AVTransport, ConnectionManager, RenderingControl, PlayQueue and QPlay.

Confirmed advertised RenderingControl service type:
`urn:schemas-upnp-org:service:RenderingControl:1`

For each port P in49152,59152:
- controlURL: `http://192.168.0.99:P/upnp/control/rendercontrol1`
- SCPDURL: `http://192.168.0.99:P/upnp/rendercontrolSCPD.xml`
- eventSubURL: `http://192.168.0.99:P/upnp/event/rendercontrol1`

This confirms advertised endpoint locations, not successful action execution, event delivery, GetVolume/SetVolume timing, identical response bodies across ports, or a successful subscription.

The first diagnostic printed only blank errors after the port numbers. Its strict namespace assumption could raise StopIteration with an empty message. The successful follow-up used local XML tag names; it does not prove the exact namespace defect without the original raw XML.

Next diagnostic: inspect this device's SCPD arguments, time GetVolume and submit SetVolume with the just-read current level. Same-level acceptance/readback is weaker evidence than verifying a changed audible/output level. The Linkplay HTTP API transport remains HTTPS443; this separate UPnP service does not authorize a global downgrade of /httpapi.asp.
