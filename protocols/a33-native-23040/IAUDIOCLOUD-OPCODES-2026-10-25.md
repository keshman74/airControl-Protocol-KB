# iAudioCloud 2.0.260728 native opcode inventory

Status: **APK-VERIFIED / NOT-HW-VERIFIED**. [Interpretation and wire format](IAUDIOCLOUD-2026-10-25.md).
141 declared byte-array constants from `classes3.dex`, `Lcom/cloudyx/multimediaplayer/model/DeviceModel;-><clinit>()V`. Exact bytes were decoded from smali array-data, not inferred from aliased Java constants. The array labels below are JADX disassembly anchors for this exact APK and tool, not file offsets.
TX means an observed builder use in the 35 selected agreement classes plus DeviceModel; RX means a reference inside DeviceModel.handleResult. Neither means tested device support. Declared-only entries have no demonstrated direction in this bounded search.

| Bytes | Symbol | Observed role | Initializer anchor |
|---|---|---|---|
| `00 00` | `COMMAND_ID_DEVICE_INFO` | TX builder/RX dispatcher | `:array_3e6` |
| `00 01` | `COMMAND_ID_RENAME` | TX builder/RX dispatcher | `:array_3ec` |
| `00 02` | `COMMAND_ID_RESET_FACTORY` | TX builder | `:array_3f2` |
| `00 03` | `COMMAND_ID_REBOOT` | TX builder | `:array_3f8` |
| `00 04` | `COMMAND_ID_STANDBY` | TX builder/RX dispatcher | `:array_3fe` |
| `00 05` | `COMMAND_ID_HEARTBEAT` | TX builder/RX dispatcher | `:array_404` |
| `00 06` | `COMMAND_ID_CHANGE_MODE_DEVICE_SET` | TX builder/RX dispatcher | `:array_40a` |
| `00 07` | `COMMAND_ID_CHANGE_MODE_DEVICE_GET` | RX dispatcher | `:array_410` |
| `00 08` | `COMMAND_ID_BLE_CONFIG_NETWORK` | RX dispatcher | `:array_416` |
| `00 09` | `COMMAND_ID_BATTERY_INFO` | TX builder/RX dispatcher | `:array_41c` |
| `00 10` | `COMMAND_ID_PLAY_MODE_SET` | TX builder/RX dispatcher | `:array_422` |
| `00 11` | `COMMAND_ID_PLAY_MODE_GET` | RX dispatcher | `:array_428` |
| `00 20` | `COMMAND_ID_TIDAL_SONGS` | TX builder/RX dispatcher | `:array_42e` |
| `00 21` | `COMMAND_ID_UPDATE_TOKEN` | TX builder/RX dispatcher | `:array_434` |
| `00 22` | `COMMAND_ID_SONGLIST_UPDATE` | TX builder/RX dispatcher | `:array_43a` |
| `00 30` | `COMMAND_ID_MSG_ERROR` | RX dispatcher | `:array_440` |
| `00 31` | `COMMAND_ID_PROGRESS_DURATION` | RX dispatcher | `:array_446` |
| `00 32` | `COMMAND_ID_PLAY_PAUSE` | TX builder/RX dispatcher | `:array_44c` |
| `00 33` | `COMMAND_ID_LAST_NEXT` | TX builder/RX dispatcher | `:array_452` |
| `00 34` | `COMMAND_ID_SET_PROGRESS` | TX builder/RX dispatcher | `:array_458` |
| `00 35` | `COMMAND_ID_CHANGE_SONGS_ID` | RX dispatcher | `:array_45e` |
| `00 36` | `COMMAND_ID_PLAY_STATUS` | RX dispatcher | `:array_464` |
| `00 40` | `COMMAND_ID_VOLUME` | TX builder/RX dispatcher | `:array_46a` |
| `00 42` | `COMMAND_ID_MAX_VOLUME` | RX dispatcher | `:array_470` |
| `00 47` | `COMMAND_ID_VOLUME_CHANGE` | TX builder/RX dispatcher | `:array_476` |
| `00 48` | `COMMAND_ID_VOLUME_MUTE` | TX builder/RX dispatcher | `:array_47c` |
| `00 49` | `COMMAND_ID_VOLUME_CHANNEL` | TX builder/RX dispatcher | `:array_482` |
| `00 50` | `COMMAND_ID_MULTI_ROOM_OPEN` | TX builder/RX dispatcher | `:array_488` |
| `00 51` | `COMMAND_ID_MULTI_ROOM_EXIT` | RX dispatcher | `:array_48e` |
| `00 52` | `COMMAND_ID_MULTI_ROOM_STATUS` | TX builder/RX dispatcher | `:array_494` |
| `00 60` | `COMMAND_ID_RADIO` | TX builder/RX dispatcher | `:array_49a` |
| `00 61` | `COMMAND_ID_RADIO_PLAY_STATUS` | RX dispatcher | `:array_4a0` |
| `00 80` | `COMMAND_ID_USB_SONG_LIST` | RX dispatcher | `:array_4a6` |
| `00 81` | `COMMAND_ID_USB_SONG` | RX dispatcher | `:array_4ac` |
| `00 82` | `COMMAND_ID_USB_PLAY` | TX builder/RX dispatcher | `:array_4b2` |
| `00 83` | `COMMAND_ID_USB_SONG_CHANGE` | TX builder/RX dispatcher | `:array_4b8` |
| `00 84` | `COMMAND_ID_USB_SONG_LIST_GET` | RX dispatcher | `:array_4be` |
| `00 85` | `COMMAND_ID_USB_SONG_GET` | TX builder/RX dispatcher | `:array_4c4` |
| `00 86` | `COMMAND_ID_USB_END` | RX dispatcher | `:array_4ca` |
| `00 87` | `COMMAND_ID_USB_PLAY_MODE_SET` | declared only | `:array_4d0` |
| `00 88` | `COMMAND_ID_USB_MOUNT` | RX dispatcher | `:array_4d6` |
| `00 89` | `COMMAND_ID_USB_PORT` | RX dispatcher | `:array_4dc` |
| `00 90` | `COMMAND_ID_LOCAL_PLAY` | TX builder/RX dispatcher | `:array_4e2` |
| `00 91` | `COMMAND_ID_LOCAL_PROGRESS` | RX dispatcher | `:array_4e8` |
| `00 92` | `COMMAND_ID_LOCAL_INFO` | TX builder/RX dispatcher | `:array_4ee` |
| `01 00` | `COMMAND_ID_DLNA_SONG_INFO` | RX dispatcher | `:array_4f4` |
| `01 01` | `COMMAND_ID_DLNA_SONG_GET` | TX builder/RX dispatcher | `:array_4fa` |
| `01 20` | `COMMAND_ID_AIRPLAY_META` | RX dispatcher | `:array_500` |
| `01 21` | `COMMAND_ID_AIRPLAY_META_GET` | RX dispatcher | `:array_506` |
| `01 22` | `COMMAND_ID_AIRPLAY_SONG_NAME` | RX dispatcher | `:array_50c` |
| `01 23` | `COMMAND_ID_AIRPLAY_SONG_SINGER` | RX dispatcher | `:array_512` |
| `01 24` | `COMMAND_ID_AIRPLAY_SONG_IMG` | RX dispatcher | `:array_518` |
| `01 25` | `COMMAND_ID_AIRPLAY_SONG_INFO` | TX builder/RX dispatcher | `:array_51e` |
| `01 26` | `COMMAND_ID_AIRPLAY_MAC_CONNECT` | RX dispatcher | `:array_524` |
| `01 27` | `COMMAND_ID_AIRPLAY_MAC_BREAK` | RX dispatcher | `:array_52a` |
| `01 28` | `COMMAND_ID_AIRPLAY_PROGRESS` | RX dispatcher | `:array_530` |
| `01 29` | `COMMAND_ID_AIRPLAY_TOTAL_TIME` | RX dispatcher | `:array_536` |
| `01 30` | `COMMAND_ID_HTTP_URL_INFO` | RX dispatcher | `:array_53c` |
| `01 31` | `COMMAND_ID_HTTP_URL_SEND` | TX builder | `:array_542` |
| `01 40` | `COMMAND_ID_QOBUZ_SONGS` | TX builder/RX dispatcher | `:array_548` |
| `01 50` | `COMMAND_ID_OTA_NOTIFY` | TX builder/RX dispatcher | `:array_54e` |
| `01 51` | `COMMAND_ID_OTA_REQUEST` | TX builder/RX dispatcher | `:array_554` |
| `01 52` | `COMMAND_ID_OTA_RESULT` | TX builder/RX dispatcher | `:array_55a` |
| `01 53` | `COMMAND_ID_OTA_VERSION` | TX builder/RX dispatcher | `:array_560` |
| `01 60` | `COMMAND_ID_TIME_ZONE` | TX builder/RX dispatcher | `:array_566` |
| `01 61` | `COMMAND_ID_TIME_ZONE_NEED` | RX dispatcher | `:array_56c` |
| `01 70` | `COMMAND_ID_WIFI_SSID` | TX builder/RX dispatcher | `:array_572` |
| `01 71` | `COMMAND_ID_WIFI_SSID_NEED` | RX dispatcher | `:array_578` |
| `01 90` | `COMMAND_ID_OTA_NEW_VERSION` | RX dispatcher | `:array_57e` |
| `02 00` | `COMMAND_ID_VTUNER_PLAY` | TX builder/RX dispatcher | `:array_584` |
| `02 10` | `COMMAND_ID_SPOTIFY_PLAY` | RX dispatcher | `:array_58a` |
| `02 11` | `COMMAND_ID_SPOTIFY_MODE` | TX builder/RX dispatcher | `:array_590` |
| `02 20` | `COMMAND_ID_HOME_SHARE_PLAY` | TX builder/RX dispatcher | `:array_596` |
| `02 21` | `COMMAND_ID_HOME_SHARE_GET` | TX builder/RX dispatcher | `:array_59c` |
| `02 30` | `COMMAND_ID_ALARM_SET` | TX builder/RX dispatcher | `:array_5a2` |
| `02 32` | `COMMAND_ID_ALARM_DEL` | TX builder/RX dispatcher | `:array_5a8` |
| `02 33` | `COMMAND_ID_ALARM_EDIT` | TX builder/RX dispatcher | `:array_5ae` |
| `02 34` | `COMMAND_ID_ALARM_GET` | TX builder/RX dispatcher | `:array_5b4` |
| `02 35` | `COMMAND_ID_ALARM_SUPPORT` | TX builder/RX dispatcher | `:array_5ba` |
| `02 40` | `COMMAND_ID_DEVELOP_INFO_GET` | TX builder/RX dispatcher | `:array_5c0` |
| `02 41` | `COMMAND_ID_SSID_EDIT` | TX builder/RX dispatcher | `:array_5c6` |
| `02 50` | `COMMAND_ID_EQ_TYPE_SYNC` | RX dispatcher | `:array_5cc` |
| `02 51` | `COMMAND_ID_EQ_VOLUME_SYNC` | TX builder/RX dispatcher | `:array_5d2` |
| `02 52` | `COMMAND_ID_EQ_SET` | TX builder/RX dispatcher | `:array_5d8` |
| `02 53` | `COMMAND_ID_EQ_SET_PARAM` | TX builder/RX dispatcher | `:array_5de` |
| `02 54` | `COMMAND_ID_EQ_TYPE` | TX builder/RX dispatcher | `:array_5e4` |
| `02 55` | `COMMAND_ID_EQ_UPDATA` | TX builder | `:array_5ea` |
| `02 56` | `COMMAND_ID_EQ_CUSTOM_REMOVE` | TX builder | `:array_5f0` |
| `02 57` | `COMMAND_ID_EQ_OFF_NO` | TX builder/RX dispatcher | `:array_5f6` |
| `02 58` | `COMMAND_ID_EQ_UPDATA_NAME` | TX builder | `:array_5fc` |
| `02 60` | `COMMAND_BLUE_GETINFO` | TX builder/RX dispatcher | `:array_602` |
| `02 70` | `COMMAND_ID_MFI_AIRPALY_CONNECT` | declared only | `:array_608` |
| `02 71` | `COMMAND_ID_MFI_AIRPALY_DISCONNECT` | declared only | `:array_60e` |
| `02 72` | `COMMAND_ID_MFI_AIRPALY_SONG` | RX dispatcher | `:array_614` |
| `02 73` | `COMMAND_ID_MFI_SMB_UPNP_SONG_PROGRESS` | RX dispatcher | `:array_61a` |
| `02 74` | `COMMAND_ID_MFI_AIRPALY_SONG_IMAGE` | RX dispatcher | `:array_620` |
| `02 75` | `COMMAND_ID_MFI_AIRPALY_SONG_GET` | TX builder/RX dispatcher | `:array_626` |
| `02 80` | `COMMAND_ID_HOME_MEDIA_SONG_PLAY` | TX builder/RX dispatcher | `:array_62c` |
| `02 81` | `COMMAND_ID_HOME_MEDIA_SONG_PROGRESS` | declared only | `:array_632` |
| `02 82` | `COMMAND_ID_HOME_MEDIA_SONG_GET` | TX builder/RX dispatcher | `:array_638` |
| `02 90` | `COMMAND_ID_QOBUZ_CONNECT` | RX dispatcher | `:array_63e` |
| `02 91` | `COMMAND_ID_QOBUZ_DISCONNECT` | RX dispatcher | `:array_644` |
| `02 92` | `COMMAND_ID_QOBUZ_QUALITY` | TX builder/RX dispatcher | `:array_64a` |
| `02 93` | `COMMAND_ID_QOBUZ_GETINFO` | TX builder/RX dispatcher | `:array_650` |
| `03 00` | `COMMAND_ID_QPLAY_CONNECT` | RX dispatcher | `:array_656` |
| `03 01` | `COMMAND_ID_QPLAY_DISCONNECT` | RX dispatcher | `:array_65c` |
| `03 02` | `COMMAND_ID_QPLAY_GETINFO` | TX builder/RX dispatcher | `:array_662` |
| `03 03` | `COMMAND_ID_QPLAY_GET_LIST` | TX builder/RX dispatcher | `:array_668` |
| `03 04` | `COMMAND_ID_QPLAY_INDEX_INFO` | TX builder | `:array_66e` |
| `03 10` | `COMMAND_ID_UPNPDLNA_CONNECT` | RX dispatcher | `:array_674` |
| `03 11` | `COMMAND_ID_UPNPDLNA_GETINFO` | TX builder/RX dispatcher | `:array_67a` |
| `02 59` | `COMMAND_ID_SUBWOOFER_INFO_GET` | TX builder/RX dispatcher | `:array_680` |
| `03 20` | `COMMAND_ID_SUBWOOFER_SWITCH` | TX builder/RX dispatcher | `:array_686` |
| `03 21` | `COMMAND_ID_SUBWOOFER_RESET` | TX builder | `:array_68c` |
| `03 30` | `COMMAND_ID_YINYUANHE_SYNC` | declared only | `:array_692` |
| `03 31` | `COMMAND_ID_YINYUANHE_GET` | declared only | `:array_698` |
| `03 40` | `COMMAND_ID_SLEEP_MODE_SET` | TX builder | `:array_69e` |
| `03 41` | `COMMAND_ID_SLEEP_MODE_GET` | TX builder/RX dispatcher | `:array_6a4` |
| `03 42` | `COMMAND_ID_STAND_TIME_SET` | TX builder | `:array_6aa` |
| `03 43` | `COMMAND_ID_STAND_TIME_GET` | TX builder/RX dispatcher | `:array_6b0` |
| `03 50` | `COMMAND_ID_NETWORK_DATA_GET` | TX builder/RX dispatcher | `:array_6b6` |
| `03 60` | `COMMAND_ID_CLEAR_MUSIC_LIST` | TX builder/RX dispatcher | `:array_6bc` |
| `03 70` | `COMMAND_ID_PRESET_ACTIVE` | TX builder/RX dispatcher | `:array_6c2` |
| `03 71` | `COMMAND_ID_PRESET_ADD` | TX builder | `:array_6c8` |
| `03 72` | `COMMAND_ID_PRESET_DEL` | TX builder | `:array_6ce` |
| `03 73` | `COMMAND_ID_PRESET_EDIT` | TX builder | `:array_6d4` |
| `03 74` | `COMMAND_ID_PRESET_MUSIC_DATA` | RX dispatcher | `:array_6da` |
| `03 75` | `COMMAND_ID_PRESET_MOVE` | TX builder | `:array_6e0` |
| `03 76` | `COMMAND_ID_PRESET_GET` | TX builder/RX dispatcher | `:array_6e6` |
| `03 80` | `COMMAND_ID_FEEDBACK_SEND` | TX builder/RX dispatcher | `:array_6ec` |
| `03 85` | `COMMAND_ID_STATIC_IP_SEND` | TX builder/RX dispatcher | `:array_6f2` |
| `03 86` | `COMMAND_ID_STATIC_IP_GET` | TX builder/RX dispatcher | `:array_6f8` |
| `03 90` | `COMMAND_ID_START_CONFIG_WIFI` | TX builder | `:array_6fe` |
| `04 00` | `COMMAND_ID_ERROR_MSG_GET` | RX dispatcher | `:array_704` |
| `04 10` | `COMMAND_ID_12V_TRIGGER_SET` | TX builder | `:array_70a` |
| `04 11` | `COMMAND_ID_12V_TRIGGER_GET` | TX builder/RX dispatcher | `:array_710` |
| `04 20` | `COMMAND_ID_SYNC_CUSTOM_TIP_SET` | TX builder/RX dispatcher | `:array_716` |
| `04 21` | `COMMAND_ID_SYNC_CUSTOM_TIP_GET` | TX builder/RX dispatcher | `:array_71c` |
| `04 30` | `COMMAND_ID_RESET_BLUETOOTH` | TX builder | `:array_722` |
| `04 40` | `COMMAND_ID_EQ_PLAY_SOUND` | TX builder | `:array_728` |
| `04 41` | `COMMAND_ID_EQ_FILTER_SEND` | TX builder | `:array_72e` |

## Send-site observations

109 observations; repeated opcodes and variants are intentional, not new command IDs. Expressions below preserve caller variables. Field extraction is a reading aid: nested maps, conditional fields and object serialization require the accompanying report and source method. A symbol alone is insufficient to infer a request schema.

| Bytes | Class / method signature | Builder argument / field expressions |
|---|---|---|
| `00 04` | `agreement/StandbyAgreement`<br>`static /* synthetic */ void lambda$sendStandbySet$0(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_STANDBY, str));` |
| `03 42` | `agreement/StandbyAgreement`<br>`static /* synthetic */ void lambda$sendStandTime$1(DeviceModel deviceModel, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_STAND_TIME_SET, map)); ; field assignments: SetStandbyTime=str; StandbyCountdown=str2` |
| `03 43` | `agreement/StandbyAgreement`<br>`static /* synthetic */ void lambda$sendGet$2(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_STAND_TIME_GET, (String) null));` |
| `03 76` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendGetPresetList$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_GET, (String) null));` |
| `03 71` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendAddPreset$2(DeviceModel deviceModel, PresetModel presetModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_ADD, new Gson().toJson(presetModel)));` |
| `03 73` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendModifyPreset$3(DeviceModel deviceModel, PresetModel presetModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_EDIT, new Gson().toJson(presetModel)));` |
| `03 72` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendDeletePreset$4(DeviceModel deviceModel, PresetModel presetModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_DEL, map)); ; field assignments: Logo=presetModel.getLogo()` |
| `03 75` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendMovePreset$5(DeviceModel deviceModel, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_MOVE, map)); ; field assignments: OldIndex=str; NewIndex=str2` |
| `03 70` | `agreement/PresetAgreement`<br>`static /* synthetic */ void lambda$sendPresetActive$6(DeviceModel deviceModel, PresetModel presetModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_PRESET_ACTIVE, map)); ; field assignments: Logo=presetModel.getLogo()` |
| `03 40` | `agreement/SleepAgreement`<br>`static /* synthetic */ void lambda$sendSet$0(DeviceModel deviceModel, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SLEEP_MODE_SET, map)); ; field assignments: SetSleepTime=str; SleepCountdown=str2` |
| `03 41` | `agreement/SleepAgreement`<br>`static /* synthetic */ void lambda$sendGet$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SLEEP_MODE_GET, (String) null));` |
| `00 22` | `agreement/SonglistSyncAgreement`<br>`static /* synthetic */ void lambda$sendMessage$0(DeviceModel deviceModel, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SONGLIST_UPDATE, map)); ; field assignments: StreamMediaName=str; SongList=str2` |
| `03 86` | `agreement/IpSetAgreement`<br>`static /* synthetic */ void lambda$sendGetIpInfo$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_STATIC_IP_GET, (String) null));` |
| `03 85` | `agreement/IpSetAgreement`<br>`static /* synthetic */ void lambda$sendSetIp$1(DeviceModel deviceModel, IPInfoModel iPInfoModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_STATIC_IP_SEND, map)); ; field assignments: StaticIpStatus="1"; EStaticIp=iPInfoModel.getEStaticIp(); EStaticNetmask=iPInfoModel.getEStaticNetmask(); EStaticGateway=iPInfoModel.getEStaticGateway(); EStaticDns=iPInfoModel.getEStaticDns(); WStaticIp=iPInfoModel.getWStaticIp(); WStaticNetmask=iPInfoModel.getWStaticNetmask(); WStaticGateway=iPInfoModel.getWStaticGateway(); WStaticDns=iPInfoModel.getWStaticDns()` |
| `02 75` | `agreement/MfiAirplayAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_MFI_AIRPALY_SONG_GET, (String) null));` |
| `02 60` | `agreement/BluetoothAgreement`<br>`static /* synthetic */ void lambda$sendGetBluetoothSong$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_BLUE_GETINFO, " "));` |
| `00 82` | `agreement/UsbAgreement`<br>`static /* synthetic */ void lambda$playUSBMusic$1(DeviceModel deviceModel, USBSongModel uSBSongModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_USB_PLAY, map)); ; field assignments: StreamMediaName=Type.StreamMedia.USB; UsbSongName=uSBSongModel.getUsbSongName(); UsbSongIndex=uSBSongModel.getUsbSongIndex()` |
| `00 83` | `agreement/UsbAgreement`<br>`static /* synthetic */ void lambda$sendUSBChangeMusicCMD$4(boolean z, DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_USB_SONG_CHANGE, map)); ; field assignments: StreamMediaName=Type.StreamMedia.USB; UsbSongIndex=z ? "+1" : "-1"` |
| `04 40` | `agreement/RoomFitAgreement`<br>`static /* synthetic */ void lambda$sendPlaySound$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_PLAY_SOUND, (String) null));` |
| `04 41` | `agreement/RoomFitAgreement`<br>`static /* synthetic */ void lambda$sendFilterInfo$1(DeviceModel deviceModel, List list) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_FILTER_SEND, map)); ; field assignments: Index=String.valueOf(i); Filter=eqFilterModel.getType(); Freq=String.format("%.1f", Float.valueOf(eqFilterModel.getFrequency())); Gain=String.format("%.1f", Float.valueOf(eqFilterModel.getGain())); Q=String.format("%.2f", Float.valueOf(eqFilterModel.getQ())); EqBand=arrayList` |
| `00 20` | `agreement/TidalAgreement`<br>`static /* synthetic */ void lambda$playTIDALTrackReal$0(DeviceModel deviceModel, List list, int i, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_TIDAL_SONGS, map)); ; field assignments: SongList=strConverToString; SongPlay="null"; SongPlay=((TIDALTracksModel) list.get(i)).getId() + ""; StreamMediaName=Type.StreamMedia.TIDAL; Path=str; Token=tIDALAccessToken` |
| `00 20` | `agreement/TidalAgreement`<br>`static /* synthetic */ void lambda$playTIDALRecent$1(DeviceModel deviceModel, RecentlyPlayedModel recentlyPlayedModel, List list) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_TIDAL_SONGS, map)); ; field assignments: StreamMediaName=Type.StreamMedia.TIDAL; Path=recentlyPlayedModel.getPath(); Token=tIDALAccessToken; SongPlay=String.valueOf(tIDALTrack.getId()); SongList=recentlyPlayedModel.getIdListStr()` |
| `02 35` | `agreement/AlarmAgreement`<br>`static /* synthetic */ void lambda$sendAlarmSupport$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_ALARM_SUPPORT, (String) null));` |
| `02 30` | `agreement/AlarmAgreement`<br>`static /* synthetic */ void lambda$sendAlarmSet$1(DeviceModel deviceModel, AlarmClockModel alarmClockModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_ALARM_SET, map)); ; field assignments: SetTime=alarmClockModel.getSetTime(); RepeatWeek=alarmClockModel.getRepeatWeek().isEmpty() ? "0" : alarmClockModel.getRepeatWeek(); MusicData=alarmClockModel.getMusicData(); Volume=alarmClockModel.getVolume(); TimeOut=alarmClockModel.getTimeout(); StreamMediaName=streamMediaName; Switch=alarmClockModel.getSwitchStatus(); Logo=alarmClockModel.getLogo()` |
| `02 33` | `agreement/AlarmAgreement`<br>`static /* synthetic */ void lambda$sendAlarmEdit$2(AlarmClockModel alarmClockModel, DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_ALARM_EDIT, map)); ; field assignments: SetTime=alarmClockModel.getSetTime(); RepeatWeek=alarmClockModel.getRepeatWeek().isEmpty() ? "0" : alarmClockModel.getRepeatWeek(); MusicData=alarmClockModel.getMusicData(); Volume=alarmClockModel.getVolume(); TimeOut=alarmClockModel.getTimeout(); StreamMediaName=streamMediaName; Switch=alarmClockModel.getSwitchStatus(); Logo=alarmClockModel.getLogo()` |
| `02 32` | `agreement/AlarmAgreement`<br>`static /* synthetic */ void lambda$sendAlarmDel$3(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_ALARM_DEL, str));` |
| `02 34` | `agreement/AlarmAgreement`<br>`static /* synthetic */ void lambda$sendAlarmGet$4(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_ALARM_GET, (String) null));` |
| `01 40` | `agreement/QobuzAgreement`<br>`static /* synthetic */ void lambda$playQobuzTrackReal$0(DeviceModel deviceModel, int i, List list, int i2, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QOBUZ_SONGS, map)); ; field assignments: SongList=StringUtils.converToString(arrayList, "-"); SongPlay="null"; SongPlay=((QobuzTrackModel) list.get(i)).getId() + ""; Path=str2; StreamMediaName=Type.StreamMedia.QOBUZ; CutOrChoose="choose"; FormatId=qobuzUser.getFormatId() + ""; Token=qobuzUser.getUser_auth_token()` |
| `01 40` | `agreement/QobuzAgreement`<br>`static /* synthetic */ void lambda$playRecent$1(DeviceModel deviceModel, List list, RecentlyPlayedModel recentlyPlayedModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QOBUZ_SONGS, map)); ; field assignments: StreamMediaName=Type.StreamMedia.QOBUZ; CutOrChoose="choose"; Path=recentlyPlayedModel.getPath(); SongPlay=String.valueOf(qobuzTrack.getId()); SongList=String.valueOf(qobuzTrack.getIdList()); FormatId=qobuzUser.getFormatId() + ""; Token=qobuzUser.getUser_auth_token()` |
| `02 92` | `agreement/QobuzAgreement`<br>`static /* synthetic */ void lambda$sendSetQuality$3(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QOBUZ_QUALITY, str));` |
| `02 93` | `agreement/QobuzAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$4(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QOBUZ_GETINFO, (String) null));` |
| `01 25` | `agreement/AirplayAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_AIRPLAY_SONG_INFO, (String) null));` |
| `02 54` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendTypeSync$0(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_TYPE, str));` |
| `02 51` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendVolumeSync$1(DeviceModel deviceModel, EQTrebleBassModel eQTrebleBassModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_VOLUME_SYNC, map)); ; field assignments: Bass=String.valueOf(eQTrebleBassModel.getBass()); Treble=String.valueOf(eQTrebleBassModel.getTreble())` |
| `02 52` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendSet$2(DeviceModel deviceModel, EQGraphicModel eQGraphicModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_SET, map)); ; field assignments: Name=eQGraphicModel.getName(); EqBand=strArr` |
| `02 52` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendCustomSet$3(DeviceModel deviceModel, EqGraphicCustomModel eqGraphicCustomModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_SET, map)); ; field assignments: Name=eqGraphicCustomModel.getName(); EqBand=strArr` |
| `02 53` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendSetParam$4(DeviceModel deviceModel, EqCustomParametricModel eqCustomParametricModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_SET_PARAM, map)); ; field assignments: Name=eqCustomParametricModel.getName(); Index=String.valueOf(i); Filter=eqFilterModel.getType(); Freq=String.format("%.1f", Float.valueOf(eqFilterModel.getFrequency())); Gain=String.format("%.1f", Float.valueOf(eqFilterModel.getGain())); Q=String.format("%.2f", Float.valueOf(eqFilterModel.getQ())); EqBand=arrayList` |
| `02 55` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendUpdataCustom$5(DeviceModel deviceModel, EqGraphicCustomModel eqGraphicCustomModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_UPDATA, map)); ; field assignments: Type=ExifInterface.GPS_MEASUREMENT_2D; Name=eqGraphicCustomModel.getName(); EqBand=strArr` |
| `02 56` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendCustomMove$6(DeviceModel deviceModel, String str, String str2) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_CUSTOM_REMOVE, map)); ; field assignments: Type=str; Name=str2` |
| `02 55` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendUpdateParam$7(DeviceModel deviceModel, EqCustomParametricModel eqCustomParametricModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_UPDATA, map)); ; field assignments: Type=ExifInterface.GPS_MEASUREMENT_3D; Name=eqCustomParametricModel.getName(); Index=String.valueOf(i); Filter=eqFilterModel.getType(); Freq=String.format("%.1f", Float.valueOf(eqFilterModel.getFrequency())); Gain=String.format("%.1f", Float.valueOf(eqFilterModel.getGain())); Q=String.format("%.2f", Float.valueOf(eqFilterModel.getQ())); EqBand=arrayList` |
| `02 57` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendEQOffNo$8(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_OFF_NO, str));` |
| `02 58` | `agreement/EQAgreement`<br>`static /* synthetic */ void lambda$sendUpdataName$9(DeviceModel deviceModel, String str, String str2, String str3) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_UPDATA_NAME, map)); ; field assignments: OldName=str; NewName=str2; Type=str3` |
| `01 31` | `agreement/HttpMediaAgreement`<br>`static /* synthetic */ void lambda$sendHttpMedia$0(DeviceModel deviceModel, MusicModel musicModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_HTTP_URL_SEND, map)); ; field assignments: StreamMediaName=Type.StreamMedia.HTTP_MUSIC; TrackTitle=musicModel.getTitle(); TrackUrl=musicModel.getPath(); TrackId=musicModel.getId(); TrackImage=musicModel.getPictureUrl()` |
| `03 11` | `agreement/UpnpDlanAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_UPNPDLNA_GETINFO, (String) null));` |
| `00 33` | `agreement/PlaybackControlAgreement`<br>`static /* synthetic */ void lambda$sendChangeMusicCMD$0(DeviceModel deviceModel, boolean z) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LAST_NEXT, map)); ; field assignments: index=z ? "+1" : "-1"; SongPlay="null"` |
| `00 10` | `agreement/PlaybackControlAgreement`<br>`static /* synthetic */ void lambda$setPlayModeCMD$1(DeviceModel deviceModel, boolean z, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_PLAY_MODE_SET, map)); ; field assignments: Shuffle=z ? Type.PresetLoopMode.SHUFFLE_YES : Type.PresetLoopMode.SHUFFLE_NO; Repeat=str` |
| `00 34` | `agreement/PlaybackControlAgreement`<br>`static /* synthetic */ void lambda$setMusicProgress$2(DeviceModel deviceModel, int i) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_SET_PROGRESS, i + ""));` |
| `00 32` | `agreement/PlaybackControlAgreement`<br>`static /* synthetic */ void lambda$sendPlay$3(DeviceModel deviceModel, OnDevicePlayPauseListener onDevicePlayPauseListener, boolean z) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_PLAY_PAUSE, z ? "plays" : Type.PlayState.PAUSE));` |
| `02 82` | `agreement/UpnpShareAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_HOME_MEDIA_SONG_GET, (String) null));` |
| `02 82` | `agreement/UpnpShareAgreement`<br>`static /* synthetic */ void lambda$getHomeUpnpSongs$1(DeviceModel deviceModel, OnHomeUpnpSongListener onHomeUpnpSongListener) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_HOME_MEDIA_SONG_GET, ""));` |
| `02 20` | `agreement/UpnpShareAgreement`<br>`static /* synthetic */ void lambda$playHomeShareMusic$2(DeviceModel deviceModel, MusicModel musicModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_HOME_SHARE_PLAY, JsonUtils.obj2String(localSongModel)));` |
| `00 60` | `agreement/TuneInAgreement`<br>`static /* synthetic */ void lambda$playRecentTuneIn$2(DeviceModel deviceModel, TuneInItemsModel tuneInItemsModel, RecentlyPlayedModel recentlyPlayedModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_RADIO, map)); ; field assignments: StreamMediaName=Type.StreamMedia.TUNE_IN; TuneinId=tuneInItemsModel.getActions().getPlay().getGuideId(); TuneinUrl=tuneInItemsModel.getActions().getPlay().getPlayUrl(); TuneinStatus="start"; Path="0"; Path=tuneInItemsModel.getActions().getProfile().getUrl()` |
| `00 60` | `agreement/TuneInAgreement`<br>`static /* synthetic */ void lambda$playTuneIn$3(DeviceModel deviceModel, TuneInItemsModel tuneInItemsModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_RADIO, map)); ; field assignments: StreamMediaName=Type.StreamMedia.TUNE_IN; Title=tuneInItemsModel.getTitle(); Picture=tuneInItemsModel.getImage(); TuneinId=tuneInItemsModel.getActions().getPlay().getGuideId(); TuneinUrl=tuneInItemsModel.getActions().getPlay().getPlayUrl(); TuneinStatus="start"; Path="0"; Path=tuneInItemsModel.getActions().getProfile().getUrl()` |
| `00 90` | `agreement/LocalAgreement`<br>`static /* synthetic */ void lambda$playLocalMusic$0(DeviceModel deviceModel, LocalSongModel localSongModel, List list, MusicModel musicModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LOCAL_PLAY, JsonUtils.obj2String(localSongModel)));` |
| `00 90` | `agreement/LocalAgreement`<br>`static /* synthetic */ void lambda$playFavouriteMusic$1(DeviceModel deviceModel, List list, LocalSongModel localSongModel, MusicModel musicModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LOCAL_PLAY, JsonUtils.obj2String(localSongModel)));` |
| `00 90` | `agreement/LocalAgreement`<br>`static /* synthetic */ void lambda$playLocalRecentMusic$2(DeviceModel deviceModel, int i, MusicModel musicModel, String str, String str2) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LOCAL_PLAY, JsonUtils.obj2String(localSongModel)));` |
| `00 92` | `agreement/LocalAgreement`<br>`static /* synthetic */ void lambda$getLocalMusicInfo$3(DeviceModel deviceModel, OnLocalSongListener onLocalSongListener) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LOCAL_INFO, ""));` |
| `00 92` | `agreement/LocalAgreement`<br>`static /* synthetic */ void lambda$getLocalMusicInfo$4(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_LOCAL_INFO, ""));` |
| `03 02` | `agreement/QPlayAgreement`<br>`static /* synthetic */ void lambda$sendGetInfo$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QPLAY_GETINFO, (String) null));` |
| `03 03` | `agreement/QPlayAgreement`<br>`static /* synthetic */ void lambda$sendGetList$2(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QPLAY_GET_LIST, (String) null));` |
| `03 04` | `agreement/QPlayAgreement`<br>`static /* synthetic */ void lambda$sendPlayIndex$4(DeviceModel deviceModel, int i) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_QPLAY_INDEX_INFO, map)); ; field assignments: TrackID=String.valueOf(i)` |
| `02 00` | `agreement/VTunerAgreement`<br>`static /* synthetic */ void lambda$playRecentVTuner$1(DeviceModel deviceModel, VTunerItemsModel vTunerItemsModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_VTUNER_PLAY, map)); ; field assignments: StreamMediaName=Type.StreamMedia.VTUNER; vTunerUrl=vTunerItemsModel.getVTunerUrl(); Path=vTunerItemsModel.getUrlDir(); vTunerId=String.valueOf(vTunerItemsModel.getStationId()); Title=vTunerItemsModel.getStationName(); Picture=vTunerItemsModel.getLogo()` |
| `02 00` | `agreement/VTunerAgreement`<br>`static /* synthetic */ void lambda$playVTuner$2(DeviceModel deviceModel, VTunerItemsModel vTunerItemsModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_VTUNER_PLAY, map)); ; field assignments: Path=deviceModel.getPath(); Path=vTunerItemsModel.getUrlDir(); StreamMediaName=Type.StreamMedia.VTUNER; vTunerUrl=str; vTunerId=String.valueOf(vTunerItemsModel.getStationId()); Title=vTunerItemsModel.getStationName(); Picture=vTunerItemsModel.getLogo()` |
| `02 40` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendGetDeviceSSID$0(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_DEVELOP_INFO_GET, map)); ; field assignments: SSID="dev_ssid"` |
| `03 50` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendGetNetwork$1(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_NETWORK_DATA_GET, new HashMap()));` |
| `01 60` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendTimeZone$2(DeviceModel deviceModel, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_TIME_ZONE, map)); ; field assignments: TimeZone=str` |
| `01 70` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendWiFiSSID$3(DeviceModel deviceModel, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_WIFI_SSID, map)); ; field assignments: WifiName=str` |
| `02 41` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendDeviceSSID$4(DeviceModel deviceModel, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_SSID_EDIT, str));` |
| `03 90` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendSetChangeWifi$5(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_START_CONFIG_WIFI, map)); ; field assignments: EnableDisNet="true"` |
| `04 30` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendResetBlueTooth$6(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_RESET_BLUETOOTH, (String) null));` |
| `04 20` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendSetCustomTipSet$7(DeviceModel deviceModel, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_SYNC_CUSTOM_TIP_SET, map)); ; field assignments: CustomizationSubject=deviceModel.getProjectName(); RingtoneSwitch=str; Enable="1"` |
| `04 21` | `agreement/DeviceInfoAgreement`<br>`static /* synthetic */ void lambda$sendGetCustomTipSet$8(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_SYNC_CUSTOM_TIP_GET, (String) null));` |
| `00 09` | `agreement/BatteryAgreement`<br>`static /* synthetic */ void lambda$sendGetBattery$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_BATTERY_INFO, (String) null));` |
| `02 80` | `agreement/HomeMediaAgreement`<br>`static /* synthetic */ void lambda$playHomeMedia$0(DeviceModel deviceModel, HomeMediaModel homeMediaModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_HOME_MEDIA_SONG_PLAY, map)); ; field assignments: TrackUrl=homeMediaModel.getSongUrl(); StreamMediaName=homeMediaModel.getStreamMediaName(); TrackContext=homeMediaModel.getContextUrl(); TrackImage=(homeMediaModel.getImageUrl() == null &#124;&#124; homeMediaModel.getImageUrl().isEmpty()) ? "" : homeMediaModel.getImageUrl(); TrackTitle=homeMediaModel.getTitle(); TrackId=homeMediaModel.getId()` |
| `02 80` | `agreement/HomeMediaAgreement`<br>`static /* synthetic */ void lambda$playRecentHomeMedia$1(DeviceModel deviceModel, HomeMediaModel homeMediaModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_HOME_MEDIA_SONG_PLAY, map)); ; field assignments: TrackUrl=homeMediaModel.getSongUrl(); StreamMediaName=homeMediaModel.getStreamMediaName(); TrackContext=homeMediaModel.getContextUrl(); TrackImage=(homeMediaModel.getImageUrl() == null &#124;&#124; homeMediaModel.getImageUrl().isEmpty()) ? "" : homeMediaModel.getImageUrl(); TrackTitle=homeMediaModel.getTitle(); TrackId=homeMediaModel.getId()` |
| `02 82` | `agreement/HomeMediaAgreement`<br>`static /* synthetic */ void lambda$getHomeShareMusicInfo$2(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_HOME_MEDIA_SONG_GET, ""));` |
| `03 60` | `agreement/MusicListAgreement`<br>`static /* synthetic */ void lambda$sendClear$0(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_CLEAR_MUSIC_LIST, (String) null));` |
| `00 49` | `agreement/VolumeAgreement`<br>`static /* synthetic */ void lambda$setChannel$0(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_VOLUME_CHANNEL, map)); ; field assignments: DevVolumeChannel=str` |
| `00 40` | `agreement/VolumeAgreement`<br>`static /* synthetic */ void lambda$sendVolumeCMDOld$1(DeviceModel deviceModel, String str, String str2) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_VOLUME, map)); ; field assignments: VolumeState="null"; DevVolumeL=str; DevVolumeR=str2` |
| `00 47` | `agreement/VolumeAgreement`<br>`static /* synthetic */ void lambda$sendVolumeCMDNew$2(DeviceModel deviceModel, String str) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_VOLUME_CHANGE, map)); ; field assignments: DevVolume=str` |
| `00 40` | `agreement/VolumeAgreement`<br>`static /* synthetic */ void lambda$sendMuteCMD$3(DeviceModel deviceModel, boolean z) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_VOLUME, map)); ; field assignments: VolumeState=z ? Type.VolumeState.MUTE : Type.VolumeState.ACTIVE; DevVolumeL=String.valueOf(deviceModel.getVolumeL()); DevVolumeR=String.valueOf(deviceModel.getVolumeR())` |
| `00 48` | `agreement/VolumeAgreement`<br>`static /* synthetic */ void lambda$sendMuteCMDNew$4(DeviceModel deviceModel, boolean z) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_VOLUME_MUTE, map)); ; field assignments: VolumeState=z ? Type.VolumeState.MUTE : Type.VolumeState.UNMUTE` |
| `03 80` | `agreement/FeedBackAgreement`<br>`static /* synthetic */ void lambda$sendFeedback$0(DeviceModel deviceModel, FeedbackModel feedbackModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_FEEDBACK_SEND, map)); ; field assignments: Type=feedbackModel.getType(); Subject=feedbackModel.getSubject(); SelectionProblem=feedbackModel.getSelectionProblem(); Email=feedbackModel.getEmail(); Description=feedbackModel.getDescription(); SystemType="android" + Build.VERSION.RELEASE` |
| `01 52` | `agreement/SilentUpgradeAgreement`<br>`static /* synthetic */ void lambda$sendSilentUpgrade$0(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_OTA_RESULT, map)); ; field assignments: SilentUpgrade=str` |
| `01 53` | `agreement/SilentUpgradeAgreement`<br>`static /* synthetic */ void lambda$sendGetSilentUpgrade$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_OTA_VERSION, map));` |
| `02 11` | `agreement/SpotifyAgreement`<br>`static /* synthetic */ void lambda$sendSpotifyMsg$0(DeviceModel deviceModel) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_SPOTIFY_MODE, (String) null));` |
| `03 20` | `agreement/SubwooferAgreement`<br>`static /* synthetic */ void lambda$sendPhase$0(DeviceModel deviceModel, Integer num) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SUBWOOFER_SWITCH, map)); ; field assignments: PhaseSwitch=String.valueOf(num)` |
| `02 54` | `agreement/SubwooferAgreement`<br>`static /* synthetic */ void lambda$sendGetFreq$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_EQ_TYPE, (Object) 4));` |
| `02 59` | `agreement/SubwooferAgreement`<br>`static /* synthetic */ void lambda$sendFreqSync$2(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SUBWOOFER_INFO_GET, map)); ; field assignments: FreqValue=deviceModel.getmSubwooferModel().getFreqValue(); FreqMax=deviceModel.getmSubwooferModel().getFreqMax(); FreqMin=deviceModel.getmSubwooferModel().getFreqMin()` |
| `03 21` | `agreement/SubwooferAgreement`<br>`static /* synthetic */ void lambda$reset$3(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_SUBWOOFER_RESET, new HashMap()));` |
| `04 10` | `agreement/TriggerSwitchAgreement`<br>`static /* synthetic */ void lambda$sendStateSet$0(DeviceModel deviceModel, String str) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_12V_TRIGGER_SET, map)); ; field assignments: AmplifierTrigger=str` |
| `04 11` | `agreement/TriggerSwitchAgreement`<br>`static /* synthetic */ void lambda$sendStateGet$1(DeviceModel deviceModel) {` | `StringUtils.makeSendParams(DeviceModel.COMMAND_ID_12V_TRIGGER_GET, (String) null));` |
| `00 50` | `agreement/MultiRoomAgreement`<br>`static /* synthetic */ void lambda$sendOpenMultiRoom$0(DeviceModel deviceModel, OnOpenMultiRoomCompleteListener onOpenMultiRoomCompleteListener, List list, DeviceModel deviceModel2) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_MULTI_ROOM_OPEN, map)); ; field assignments: StreamSource=Type.StreamSource.PIPE; Host=deviceModel2.getIp(); Slave=arrayList; Host=deviceModel2.getHost(); Slave=new String[]{deviceModel2.getIp()}; Host="0"; Slave=new String[]{"0"}` |
| `00 52` | `agreement/MultiRoomAgreement`<br>`static /* synthetic */ void lambda$getMultiRoomStatus$1(DeviceModel deviceModel, OnMultiRoomStatusListener onMultiRoomStatusListener) {` | `deviceModel.makeSendParams(DeviceModel.COMMAND_ID_MULTI_ROOM_STATUS, ""));` |
| `00 00` | `model/DeviceModel`<br>`public void refreshDeviceInfo(OnRefreshDeviceListener onRefreshDeviceListener) {` | `makeSendParams(COMMAND_ID_DEVICE_INFO, ""));` |
| `00 00` | `model/DeviceModel`<br>`public boolean createDeviceInfo() {` | `makeSendParams(COMMAND_ID_DEVICE_INFO, ""));` |
| `00 01` | `model/DeviceModel`<br>`public void rename(String str, OnDeviceRenameListener onDeviceRenameListener) {` | `makeSendParams(COMMAND_ID_RENAME, str));` |
| `00 21` | `model/DeviceModel`<br>`public void setTIDALToken(String str, OnDeviceTokenListener onDeviceTokenListener) {` | `makeSendParams(COMMAND_ID_UPDATE_TOKEN, str));` |
| `00 21` | `model/DeviceModel`<br>`public void setQobuzToken(String str, OnDeviceTokenListener onDeviceTokenListener) {` | `makeSendParams(COMMAND_ID_UPDATE_TOKEN, str));` |
| `00 05` | `model/DeviceModel`<br>`public void sendHeartBeat() {` | `makeSendParams(COMMAND_ID_HEARTBEAT, ""));` |
| `00 33` | `model/DeviceModel`<br>`public void playNextOrLast(boolean z) {` | `makeSendParams(COMMAND_ID_LAST_NEXT, map)); ; field assignments: SongPlay="null"; index=z ? "+1" : "-1"` |
| `01 50` | `model/DeviceModel`<br>`public void sendFirmwareUpdate(boolean z) {` | `makeSendParams(COMMAND_ID_OTA_NOTIFY, (String) null));` |
| `01 51` | `model/DeviceModel`<br>`public void updateFirmware(int i) {` | `makeSendParams(COMMAND_ID_OTA_REQUEST, map)); ; field assignments: A33M_OTA=i == 0 ? Type.PresetLoopMode.SHUFFLE_YES : Type.PresetLoopMode.SHUFFLE_NO; MCU_OTA=str` |
| `02 21` | `model/DeviceModel`<br>`public void getHomeShareMusicInfo(OnLocalSongListener onLocalSongListener) {` | `makeSendParams(COMMAND_ID_HOME_SHARE_GET, ""));` |
| `01 01` | `model/DeviceModel`<br>`public void getDLNASongInfo(OnDLNASongListener onDLNASongListener) {` | `makeSendParams(COMMAND_ID_DLNA_SONG_GET, ""));` |
| `00 85` | `model/DeviceModel`<br>`public void getUSBMusicInfo(OnUSBSongListener onUSBSongListener) {` | `makeSendParams(COMMAND_ID_USB_SONG_GET, ""));` |
| `00 06` | `model/DeviceModel`<br>`public void sendDevModelByTCP(String str, OnChangeDeviceModelListener onChangeDeviceModelListener) {` | `makeSendParams(COMMAND_ID_CHANGE_MODE_DEVICE_SET, str));` |
| `00 02` | `model/DeviceModel`<br>`public void restoreFactory() {` | `makeSendParams(COMMAND_ID_RESET_FACTORY, ""));` |
| `00 03` | `model/DeviceModel`<br>`public void rebootDevice() {` | `makeSendParams(COMMAND_ID_REBOOT, ""));` |
