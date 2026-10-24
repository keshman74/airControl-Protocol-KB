# 4STREAM central HTTP builder observations

Source: [REV-4STREAM-001](4STREAM-2026-10-24.md). Status: **APK-VERIFIED / NOT-HW-VERIFIED**.

These 142 rows preserve selected request-building expressions, not a count of distinct or newly supported commands. Local Java signatures are display names; the CSV carries original DEX method descriptors and code-unit offsets. `g.E` is the device HTTPAPI prefix; `g.I` is the master endpoint plus `SlaveIP:<slaveIP>`. Conditional/multi-line builders omitted by this extraction are discussed in the main report. `str`, `i` and similar names are decompiler parameter names, not validated schemas. No OEM/chip support is inferred from a row.

| Observation | Method | Request expression |
|---|---|---|
| 4STREAM-B001 | `com.wifiaudio.action.s.b.A` | `return g.E(deviceInfoParam) + "wlanGetConnectState";` |
| 4STREAM-B002 | `com.wifiaudio.action.s.b.B` | `return g.E(deviceInfoParam) + "delbthistory:" + str;` |
| 4STREAM-B003 | `com.wifiaudio.action.s.b.C` | `return g.E(deviceInfoParam) + "disconnectbta2dpsynk:" + str;` |
| 4STREAM-B004 | `com.wifiaudio.action.s.b.D` | `return g.E(deviceInfoParam) + "setHandshakeCode:" + str;` |
| 4STREAM-B005 | `com.wifiaudio.action.s.b.F` | `return g.E(deviceInfoParam) + "alertget";` |
| 4STREAM-B006 | `com.wifiaudio.action.s.b.G` | `return g.E(deviceInfoParam) + "getMvRemoteSilenceUpdateTime";` |
| 4STREAM-B007 | `com.wifiaudio.action.s.b.H` | `return g.E(deviceInfoParam) + "getNetwork";` |
| 4STREAM-B008 | `com.wifiaudio.action.s.b.I` | `return g.E(deviceInfoParam) + "getsyslog";` |
| 4STREAM-B009 | `com.wifiaudio.action.s.b.K` | `return g.E(deviceInfoParam) + "getShutdown";` |
| 4STREAM-B010 | `com.wifiaudio.action.s.b.L` | `return g.I(deviceInfoParam, str) + ":alertget";` |
| 4STREAM-B011 | `com.wifiaudio.action.s.b.M` | `return g.E(deviceInfoParam) + "multiroom:getSlaveList";` |
| 4STREAM-B012 | `com.wifiaudio.action.s.b.N` | `return g.E(deviceInfoParam) + "getsyslog:ip:" + str;` |
| 4STREAM-B013 | `com.wifiaudio.action.s.b.O` | `return g.E(deviceInfoParam) + "getStatus:ip:" + str;` |
| 4STREAM-B014 | `com.wifiaudio.action.s.b.P` | `return g.E(deviceInfoParam) + "startbtdiscovery:" + i;` |
| 4STREAM-B015 | `com.wifiaudio.action.s.b.Q` | `return g.E(deviceInfoParam) + "getStatusEx";` |
| 4STREAM-B016 | `com.wifiaudio.action.s.b.S` | `return g.E(deviceInfoParam) + "GetUpdateServer";` |
| 4STREAM-B017 | `com.wifiaudio.action.s.b.T` | `return g.E(deviceInfoParam) + "getWeatherInfo";` |
| 4STREAM-B018 | `com.wifiaudio.action.s.b.U` | `return g.E(deviceInfoParam) + "setPlayerCmd:play:" + str;` |
| 4STREAM-B019 | `com.wifiaudio.action.s.b.V` | `return g.E(deviceInfoParam) + "reboot";` |
| 4STREAM-B020 | `com.wifiaudio.action.s.b.W` | `return g.E(deviceInfoParam) + "restoreToDefault";` |
| 4STREAM-B021 | `com.wifiaudio.action.s.b.X` | `return g.E(deviceInfoParam) + "timeSync:" + str;` |
| 4STREAM-B022 | `com.wifiaudio.action.s.b.Z` | `return g.E(deviceInfoParam) + "wlanGetApListEx";` |
| 4STREAM-B023 | `com.wifiaudio.action.s.b.a` | `return g.E(deviceInfoParam) + "AutoPlaySet:" + str;` |
| 4STREAM-B024 | `com.wifiaudio.action.s.b.a0` | `return g.E(deviceInfoParam) + "setAccessPIN:{\"PIN\":\"" + str + "\"}";` |
| 4STREAM-B025 | `com.wifiaudio.action.s.b.b` | `return g.E(deviceInfoParam) + "getMvRomBurnPrecent";` |
| 4STREAM-B026 | `com.wifiaudio.action.s.b.b0` | `return g.E(deviceInfoParam) + "setLanguage:" + str;` |
| 4STREAM-B027 | `com.wifiaudio.action.s.b.c0` | `return g.E(deviceInfoParam) + "setDeviceName:" + str;` |
| 4STREAM-B028 | `com.wifiaudio.action.s.b.d0` | `return g.E(deviceInfoParam) + "setNetwork:" + i + ":" + str;` |
| 4STREAM-B029 | `com.wifiaudio.action.s.b.e` | `return g.E(deviceInfoParam) + (config.a.X0 ? "getMvRomDownloadV2Status" : "getMvRomDownloadStatus");` |
| 4STREAM-B030 | `com.wifiaudio.action.s.b.e0` | `return g.E(deviceInfoParam) + "setSSID:" + str;` |
| 4STREAM-B031 | `com.wifiaudio.action.s.b.f` | `return g.E(deviceInfoParam) + "getEqualizer";` |
| 4STREAM-B032 | `com.wifiaudio.action.s.b.f0` | `return g.E(deviceInfoParam) + "EQSet:Bass:" + i;` |
| 4STREAM-B033 | `com.wifiaudio.action.s.b.g` | `return g.E(deviceInfoParam) + (z ? "EQEnable" : "EQDisable");` |
| 4STREAM-B034 | `com.wifiaudio.action.s.b.g0` | `return g.E(deviceInfoParam) + "EQSet:Treble:" + i;` |
| 4STREAM-B035 | `com.wifiaudio.action.s.b.h` | `return g.E(deviceInfoParam) + "EQGet";` |
| 4STREAM-B036 | `com.wifiaudio.action.s.b.h0` | `return g.E(deviceInfoParam) + "setGroupName:" + str;` |
| 4STREAM-B037 | `com.wifiaudio.action.s.b.i` | `return g.E(deviceInfoParam) + "setMvRemoteSilenceOTATime:";` |
| 4STREAM-B038 | `com.wifiaudio.action.s.b.i0` | `return g.E(deviceInfoParam) + "setHexDeviceName:" + str;` |
| 4STREAM-B039 | `com.wifiaudio.action.s.b.j` | `return g.E(deviceInfoParam) + "setMvRemoteSilenceUpdateTime:" + str + "_" + str2;` |
| 4STREAM-B040 | `com.wifiaudio.action.s.b.j0` | `return g.E(deviceInfoParam) + "setHideSSID:" + str;` |
| 4STREAM-B041 | `com.wifiaudio.action.s.b.k` | `return g.E(deviceInfoParam) + "multiroom:SlaveKickout:" + str;` |
| 4STREAM-B042 | `com.wifiaudio.action.s.b.k0` | `return g.E(deviceInfoParam) + "talksetAlarmTone:" + i;` |
| 4STREAM-B043 | `com.wifiaudio.action.s.b.l` | `return g.E(deviceInfoParam) + "multiroom:SlaveMask:" + str;` |
| 4STREAM-B044 | `com.wifiaudio.action.s.b.l0` | `return g.E(deviceInfoParam) + "setMvRemoteSilenceUpdateTime:" + str;` |
| 4STREAM-B045 | `com.wifiaudio.action.s.b.m` | `return g.E(deviceInfoParam) + "multiroom:SlaveUnMask:" + str;` |
| 4STREAM-B046 | `com.wifiaudio.action.s.b.m0` | `return g.E(deviceInfoParam) + "setNetworkExAES:" + i + ":" + str;` |
| 4STREAM-B047 | `com.wifiaudio.action.s.b.n` | `return g.E(deviceInfoParam) + "getMvRemoteUpdateStart";` |
| 4STREAM-B048 | `com.wifiaudio.action.s.b.n0` | `return g.I(deviceInfoParam, str) + ":talksetAlarmTone:" + i;` |
| 4STREAM-B049 | `com.wifiaudio.action.s.b.o` | `return g.E(deviceInfoParam) + "getMvRemoteUpdateStatus";` |
| 4STREAM-B050 | `com.wifiaudio.action.s.b.o0` | `return g.E(deviceInfoParam) + "multiroom:SlaveChannel:" + str + ":" + i;` |
| 4STREAM-B051 | `com.wifiaudio.action.s.b.p` | `return g.E(deviceInfoParam) + "alexaEnableBetaId:" + i;` |
| 4STREAM-B052 | `com.wifiaudio.action.s.b.p0` | `return g.E(deviceInfoParam) + "multiroom:SlaveDeviceName:" + str + ":" + str2;` |
| 4STREAM-B053 | `com.wifiaudio.action.s.b.q` | `return g.E(deviceInfoParam) + "checkAccessPIN";` |
| 4STREAM-B054 | `com.wifiaudio.action.s.b.q0` | `return g.E(deviceInfoParam) + "multiroom:SlaveVolume:" + str + ":" + i;` |
| 4STREAM-B055 | `com.wifiaudio.action.s.b.r` | `return g.E(deviceInfoParam) + "getbtdiscoveryresult";` |
| 4STREAM-B056 | `com.wifiaudio.action.s.b.r0` | `return g.E(deviceInfoParam) + "setTimezone:" + f;` |
| 4STREAM-B057 | `com.wifiaudio.action.s.b.s` | `return g.E(deviceInfoParam) + "getbthistory";` |
| 4STREAM-B058 | `com.wifiaudio.action.s.b.s0` | `return g.E(deviceInfoParam) + "multiroom:Ungroup";` |
| 4STREAM-B059 | `com.wifiaudio.action.s.b.t` | `return g.E(deviceInfoParam) + "getbtpairstatus";` |
| 4STREAM-B060 | `com.wifiaudio.action.s.b.t0` | `return g.E(deviceInfoParam) + "SetUpdateServer:" + str;` |
| 4STREAM-B061 | `com.wifiaudio.action.s.b.u` | `return g.E(deviceInfoParam) + "startbtserver:" + i;` |
| 4STREAM-B062 | `com.wifiaudio.action.s.b.u0` | `return g.E(deviceInfoParam) + "setWeatherLocation:" + str + ":";` |
| 4STREAM-B063 | `com.wifiaudio.action.s.b.v` | `return g.E(deviceInfoParam) + "getbtstatus";` |
| 4STREAM-B064 | `com.wifiaudio.action.s.b.v0` | `return g.E(deviceInfoParam) + "StartCheck";` |
| 4STREAM-B065 | `com.wifiaudio.action.s.b.w` | `return g.E(deviceInfoParam) + "stopbtserver:" + i;` |
| 4STREAM-B066 | `com.wifiaudio.action.s.b.w0` | `return g.E(deviceInfoParam) + "MCUKeyShortClick:" + i;` |
| 4STREAM-B067 | `com.wifiaudio.action.s.b.x` | `return g.E(deviceInfoParam) + "getbatteryval";` |
| 4STREAM-B068 | `com.wifiaudio.action.s.b.x0` | `return g.E(deviceInfoParam) + "setPlayerCmd:switchmode:" + str;` |
| 4STREAM-B069 | `com.wifiaudio.action.s.b.y` | `return g.E(deviceInfoParam) + "clearbtdiscoveryresult";` |
| 4STREAM-B070 | `com.wifiaudio.action.s.b.z` | `return g.E(deviceInfoParam) + "connectbta2dpsynk:" + str;` |
| 4STREAM-B071 | `com.wifiaudio.action.s.b.z0` | `return g.E(deviceInfoParam) + "YAMAHA_DATA_SET:" + str;` |
| 4STREAM-B072 | `com.wifiaudio.action.e.A` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "SetSyncPlayExtraDelay:" + i2, hVar);` |
| 4STREAM-B073 | `com.wifiaudio.action.e.B` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setWlanBandConfig:" + str, hVar);` |
| 4STREAM-B074 | `com.wifiaudio.action.e.C` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setWlanConnectDisable:" + str, hVar);` |
| 4STREAM-B075 | `com.wifiaudio.action.e.D` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setWlanRoamConfig:" + str, hVar);` |
| 4STREAM-B076 | `com.wifiaudio.action.e.F` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "blehidpair:" + str2, hVar);` |
| 4STREAM-B077 | `com.wifiaudio.action.e.G` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "blehidremoveall", hVar);` |
| 4STREAM-B078 | `com.wifiaudio.action.e.I` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQv2Delete:" + str, hVar);` |
| 4STREAM-B079 | `com.wifiaudio.action.e.J` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQv2Rename:" + str, hVar);` |
| 4STREAM-B080 | `com.wifiaudio.action.e.K` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQChangeFX:" + str, hVar);` |
| 4STREAM-B081 | `com.wifiaudio.action.e.M` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getAvsMusicHDEnable", hVar);` |
| 4STREAM-B082 | `com.wifiaudio.action.e.M0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setAvsMusicHDEnable:" + str, hVar);` |
| 4STREAM-B083 | `com.wifiaudio.action.e.N` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getNewAudioOutputModeSupportList", hVar);` |
| 4STREAM-B084 | `com.wifiaudio.action.e.N0` | `y0(deviceItem, String.format("setAuxAutoSenseEnable:%d", objArr), qVar);` |
| 4STREAM-B085 | `com.wifiaudio.action.e.O` | `y0(deviceItem, "getAuxAutoSenseEnable", qVar);` |
| 4STREAM-B086 | `com.wifiaudio.action.e.O0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Button_Enable_SET:" + str, hVar);` |
| 4STREAM-B087 | `com.wifiaudio.action.e.P0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setChannelMode:" + i2, hVar);` |
| 4STREAM-B088 | `com.wifiaudio.action.e.Q` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getblehidstatus", hVar);` |
| 4STREAM-B089 | `com.wifiaudio.action.e.R` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getChannelMode", hVar);` |
| 4STREAM-B090 | `com.wifiaudio.action.e.T` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getDeviceNameChangeable", hVar);` |
| 4STREAM-B091 | `com.wifiaudio.action.e.T0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Cast:Disable", hVar);` |
| 4STREAM-B092 | `com.wifiaudio.action.e.U0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Cast:DisableUsageReport", hVar);` |
| 4STREAM-B093 | `com.wifiaudio.action.e.W` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQGetLV2Band:" + str, hVar);` |
| 4STREAM-B094 | `com.wifiaudio.action.e.X` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQGetFXList", hVar);` |
| 4STREAM-B095 | `com.wifiaudio.action.e.Y` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQv2GetList:" + str, hVar);` |
| 4STREAM-B096 | `com.wifiaudio.action.e.Y0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Cast:EnableCast", hVar);` |
| 4STREAM-B097 | `com.wifiaudio.action.e.Z` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQv2Load:" + str, hVar);` |
| 4STREAM-B098 | `com.wifiaudio.action.e.Z0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Cast:EnableUsageReport", hVar);` |
| 4STREAM-B099 | `com.wifiaudio.action.e.a` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getNewAudioOutputHardwareMode", hVar);` |
| 4STREAM-B100 | `com.wifiaudio.action.e.a0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQGetSourceModes", hVar);` |
| 4STREAM-B101 | `com.wifiaudio.action.e.b` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getAutoSenseEnable", hVar);` |
| 4STREAM-B102 | `com.wifiaudio.action.e.c` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getIPV6Enable", hVar);` |
| 4STREAM-B103 | `com.wifiaudio.action.e.d` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getMQAReceiverCap", hVar);` |
| 4STREAM-B104 | `com.wifiaudio.action.e.d1` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + String.format("setInitialConfiguration:%d", Integer.valueOf(i2)), hVar);` |
| 4STREAM-B105 | `com.wifiaudio.action.e.e` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Reload_Button_GET", hVar);` |
| 4STREAM-B106 | `com.wifiaudio.action.e.e0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getNetworkHealth", hVar);` |
| 4STREAM-B107 | `com.wifiaudio.action.e.f` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getSoftMute", hVar);` |
| 4STREAM-B108 | `com.wifiaudio.action.e.f0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getNetworkPreferDNS", hVar);` |
| 4STREAM-B109 | `com.wifiaudio.action.e.f1` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setNetworkPreferDNS:" + str, hVar);` |
| 4STREAM-B110 | `com.wifiaudio.action.e.g0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getOutputVoltage", hVar);` |
| 4STREAM-B111 | `com.wifiaudio.action.e.g1` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQSetLV2Band:" + str, hVar);` |
| 4STREAM-B112 | `com.wifiaudio.action.e.h` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getSpdifOutSwitchDelayMs", hVar);` |
| 4STREAM-B113 | `com.wifiaudio.action.e.h0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getPowerModeTime", hVar);` |
| 4STREAM-B114 | `com.wifiaudio.action.e.i` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "GetSyncPlayExtraDelay", hVar);` |
| 4STREAM-B115 | `com.wifiaudio.action.e.i0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQGetBand", hVar);` |
| 4STREAM-B116 | `com.wifiaudio.action.e.i1` | `y0(deviceItem, String.format("setSpdifAutoSenseEnable:%d", objArr), qVar);` |
| 4STREAM-B117 | `com.wifiaudio.action.e.j` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getWlanBandConfig", hVar);` |
| 4STREAM-B118 | `com.wifiaudio.action.e.j0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQGetList", hVar);` |
| 4STREAM-B119 | `com.wifiaudio.action.e.k` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getWlanConnectDisableStatus", hVar);` |
| 4STREAM-B120 | `com.wifiaudio.action.e.k0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQLoad:" + str, hVar);` |
| 4STREAM-B121 | `com.wifiaudio.action.e.l` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getWlanRoamConfig", hVar);` |
| 4STREAM-B122 | `com.wifiaudio.action.e.l0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQOff", hVar);` |
| 4STREAM-B123 | `com.wifiaudio.action.e.m0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQOn", hVar);` |
| 4STREAM-B124 | `com.wifiaudio.action.e.n` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + (DeviceProperty.isMuzoProProject(deviceItem.project) ? "setAudioOutputHardwareMode:" : "GNOTIFY=KeyEvent:") + str, hVar);` |
| 4STREAM-B125 | `com.wifiaudio.action.e.n0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQSave:" + str, hVar);` |
| 4STREAM-B126 | `com.wifiaudio.action.e.o` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setAutoSenseEnable:" + str, hVar);` |
| 4STREAM-B127 | `com.wifiaudio.action.e.o0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "EQSetBand:" + str, hVar);` |
| 4STREAM-B128 | `com.wifiaudio.action.e.p` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setIPV6Enable:" + str, hVar);` |
| 4STREAM-B129 | `com.wifiaudio.action.e.p0` | `y0(deviceItem, "getSpdifAutoSenseEnable", qVar);` |
| 4STREAM-B130 | `com.wifiaudio.action.e.q` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "LED_SWITCH_SET:" + str, hVar);` |
| 4STREAM-B131 | `com.wifiaudio.action.e.q0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "getStaticIpInfo", hVar);` |
| 4STREAM-B132 | `com.wifiaudio.action.e.q1` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "StartRebootTime:1", hVar);` |
| 4STREAM-B133 | `com.wifiaudio.action.e.r` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setVolumeControl:" + i2, hVar);` |
| 4STREAM-B134 | `com.wifiaudio.action.e.s` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setMQAReceiverCap:" + str, hVar);` |
| 4STREAM-B135 | `com.wifiaudio.action.e.t` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setMaxVolume:" + i2, hVar);` |
| 4STREAM-B136 | `com.wifiaudio.action.e.u` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setOutputVoltage:" + i2, hVar);` |
| 4STREAM-B137 | `com.wifiaudio.action.e.v` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "Reload_Button_UPDATE:" + str, hVar);` |
| 4STREAM-B138 | `com.wifiaudio.action.e.w0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "wlanGetApFullList", hVar);` |
| 4STREAM-B139 | `com.wifiaudio.action.e.x` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setSoftMute:" + str, hVar);` |
| 4STREAM-B140 | `com.wifiaudio.action.e.x0` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + String.format("wlanSwitchConnectedAp:ssid=%s:bssid=%s", apScanItem.SSID, apScanItem.BSSID), hVar);` |
| 4STREAM-B141 | `com.wifiaudio.action.e.z` | `gVarG.s(com.wifiaudio.utils.e1.g.E(deviceInfoParam) + "setSpdifOutSwitchDelayMs:" + str, hVar);` |
| 4STREAM-B142 | `com.wifiaudio.action.e.z0` | `y0(deviceItem, "getStreamingStatus", qVar);` |
