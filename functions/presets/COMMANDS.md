# Presets


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-GET-PRESET-INFO` — `getPresetInfo` — Get Preset List — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**

## 4STREAM APK evidence — 2026-10-24
**APK-VERIFIED / NOT-HW-VERIFIED**. MCUKeyShortClick takes an unchecked integer; GetKeyMapping has no wrapper inputs, SetKeyMapping uses QueueContext. A97 getPresetInfo hardware rejection remains unchanged.
[Exact formats and source selectors](../../protocols/linkplay-http-https/4STREAM-2026-10-24.md#upnp-recovered-argument-differences).

## iAudioCloud APK evidence — 2026-10-25

Native 03 70 activation and 03 72 deletion use Logo; 03 76 returns a URL; 03 71/73 serialize PresetModel; 03 75 uses OldIndex/NewIndex. Existing native and HTTP hardware evidence remains separate.

Status: **APK-VERIFIED / NOT-HW-VERIFIED** for new observations. [iAudioCloud 2.0.260728 static audit](../../protocols/a33-native-23040/IAUDIOCLOUD-2026-10-25.md).
