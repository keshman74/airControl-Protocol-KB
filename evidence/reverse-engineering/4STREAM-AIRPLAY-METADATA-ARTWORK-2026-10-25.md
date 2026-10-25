# REV-4STREAM-AIRPLAY-ART-001 — provenance and coverage

Primary findings: [canonical report](../../protocols/linkplay-http-https/4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.md). Selected machine-readable evidence: [REA and DEX anchors](4STREAM-AIRPLAY-METADATA-ARTWORK-2026-10-25.json).

Status: **APK-VERIFIED / NOT-HW-VERIFIED**.

## Artifact

- User-supplied 4STREAM.apk.
- Package com.wifiaudio.Stream, version 3.1.20.230912 / 2023091217.
- SHA-256 08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b.
- Analysis date 2026-10-25.
- APK signature verification was not performed.

## Method

1. REA inspect_android_method produced complete Java views and stable DEX prototypes for AirPlay recognition, metadata parsing, artwork UI routing, exact OkHttp request construction, accepted status codes, client selection and timer cadence.
2. A dexlib2 instruction scan enumerated direct reference instructions across all three DEX files and retained original class/method descriptors plus raw DEX code-unit offsets.
3. A complete DEX string-pool scan searched the requested terms and case variants, including albumArtURI, CurrentTrackMetaData, GetPositionInfo, GetMediaInfo, /data/, airplay_, AirplayArtWorkData.jpeg, jpg/jpeg, artwork, albumArt and cover.
4. Focused decompilation followed GetInfoEx, GetMediaInfo and AVTransport LastChange into DeviceInfoExt.setDlnaTrackMetaData, generic DIDL parsing, UI broadcasts, fragment selection, image request, byte decode and ImageView assignment.
5. The target APK was never executed. No device, endpoint, artwork URL or destructive action was contacted.

## Coverage and limitations

The direct DEX scan supports exact statements about bytecode references and literal absence in classes.dex, classes2.dex and classes3.dex. It does not prove absence from native libraries, resources not represented in those string pools, reflection, server-generated metadata or dynamically downloaded code.

GetPositionInfo had no application caller in the complete direct-reference scan; that remains a bounded static negative. AirplayArtWorkData.jpeg and /data/airplay_ had no string-pool match; a firmware may still return such a path dynamically.

The report describes client behavior if the reviewed code path is reached. It does not establish which A31/A97/A98 firmware versions emit full or relative albumArtURI values, whether their artwork server uses HTTP or HTTPS, or real event/poll timing under load.

Existing hardware-confirmed KB facts were not changed or promoted.

## Reproduction selectors

Use the exact APK digest and these REA selectors:

- com.wifiaudio.model.DeviceInfoExt / isAirPlay / ()Z
- com.wifiaudio.model.DeviceInfoExt / setDlnaTrackMetaData / (Ljava/lang/String;)V
- org.teleal.cling.c.a.a.z.e / a / (Ljava/lang/String;)Lcom/wifiaudio/model/AlbumInfo;
- com.wifiaudio.view.pagesmsccenter.NewPlayControlFragment / S2 / (Ljava/lang/String;)V
- com.wifiaudio.view.pagesmsccenter.NewPlayControlFragment / R2 / (Ljava/lang/String;Landroid/widget/ImageView;)V
- com.wifiaudio.view.pagesmsccontent.FragMenuContentCT / v1 / (Landroidx/fragment/app/FragmentActivity;Lcom/wifiaudio/model/DeviceInfoExt;)V
- com.wifiaudio.utils.e1.g / G / (Lcom/wifiaudio/model/DeviceItem;)Lcom/wifiaudio/utils/e1/g;
- com.wifiaudio.utils.e1.g / A / (Ljava/lang/String;Lcom/wifiaudio/utils/e1/g$p;)V
- com.wifiaudio.utils.e1.g / K / (I)Z
- com.wifiaudio.service.d / V0 / ()V

Inner callbacks are anchored in the JSON by their original DEX descriptors and code-unit offsets because the provider's class inventory did not expose them as independent inspection targets.
