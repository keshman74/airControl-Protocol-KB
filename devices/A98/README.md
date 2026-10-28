# DEV-A98
WiiM-family path uses HTTPS. Artwork via `getMetaInfo`/Electron resolver is confirmed in airControl. EQ uses a separate documented HTTP API transported via HTTPS in current implementation; verify commands individually before marking CONFIRMED. Test hardware has no physical USB port.

## WiiM Home OTA path (APK-VERIFIED / NOT-HW-VERIFIED)

In WiiM Home 3.6.10.260924, `defpackage.ao.T(DeviceItem, firmware)` checks firmware using HTTPS `https://cloud-api.linkplay.com/prod/ota/check?fwUid=<first-8-uuid-chars>&mcuName=<device.project>`. Its JSON body includes `mcuName`, `fwUid`, `version`, language, current `fwVersion`, full `deviceUid`, MAC, backup flag and image list. The response model `CheckFWResp.Result` exposes `domain`, `imgList`, `newOta`, `upgradeWay`, and `version`; each image has `fileName`, `fileSize`, `imgHash`, `imgVersion`, `uri`, and `downloadCode`.

`com.wifiaudio.shared.ota.BackupOTA.b(domain, img)` constructs the binary URL as `https:` + `domain` + `img.uri`, adding query parameters `downloadCode`, `fwUid` (first 8 UUID characters), and `mcuName` (`DeviceItem.project`). `OTAViewModel.downloadFile(...)` downloads to the app cache; the OTA flow then passes it to the device-specific update path. Thus the APK contains no fixed universal A98 firmware URL or image: the server response is device/project/version-specific. No A98 firmware binary has been downloaded or hardware-verified in this investigation.

The app's `DeviceProperty.isA98()` predicate is only `(hardware != A28 && hardware != A31)`; this broad branch is not proof that a device is an A98 chip or that a firmware image is compatible. Do not select or flash an image based on the chip label alone. To resolve an image, first identify the exact product/project, hardware revision and current firmware, then obtain that device's OTA check response and validate `imgName`/version, size, and hash before downloading. Never use the image URL for another model.
