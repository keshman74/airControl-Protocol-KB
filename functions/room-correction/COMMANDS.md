# Room correction


## WiiM OpenAPI v1.2.0 source import
Applicability to A97/A98: **candidate / NOT-HW-VERIFIED** unless separately promoted by hardware evidence.

- `QRY-WIIM-ROOM-CORR-GET` — `RoomCorrGet` — Get the current room correction settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `QRY-WIIM-ROOM-CORR-GET-MODE` — `RoomCorrGetMode` — Get the current room correction mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET` — `RoomCorrSet:{str}` — Set the room correction settings — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET-LR` — `RoomCorrSetLR:{str}` — Set the room correction settings for left and right channels — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-ROOM-CORR-SET-MODE` — `RoomCorrSetMode:{"Mode":"{str}"}` — Set the room correction mode — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
- `CMD-WIIM-SET-ROOM-CORRECTION` — `setRoomCorrection:{"RC_Version":"{str}","Time":"{time}"}` — Set the room correction settings with version and time parameters — **SOURCE-DOCUMENTED / NOT-HW-VERIFIED**
