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
