# 4STREAM Eq10HP raw-to-dB mapping

Status: **APK-VERIFIED / NOT-HW-VERIFIED**

## Provenance

- Package: `com.wifiaudio.Stream`
- Version: `3.1.20.230912`
- Version code: `2023091217`
- APK SHA-256: `08fea6dd95e7ce763609435edad3030d41a4d7d94ba0ca928e9c4b1e8fce201b`
- Analysis: REA + JADX Headless MCP 0.7.1
- Read-only static analysis; APK was not executed.

## Confirmed 10-band path

The 10-band UI is selected by `FragNewEQ` / `FragNewEQV2` with `EQType._10band`. The ten labels are 31, 63, 125, 250, 500, 1k, 2k, 4k, 8k and 16k Hz.

HTTP read path in `com.wifiaudio.action.e`:

```java
gVarG.s(prefix + "EQGetBand", hVar);
```

The response parser in `FragNewEQ` reads:

```java
aVar.setIndex(jsonObject2.getInt("index"));
aVar.setValue(jsonObject2.getInt("value"));
```

The model `com.wifiaudio.view.pagesdevcenter.equalizersettings.model.a` stores:

```java
private int index = 0;
private int value = 50;
```

The write path is:

```java
r0("{\"EQBand\":[{\"index\":" + index + ", \"value\":" + value + "}]}");
```

and `com.wifiaudio.action.e.o0` sends:

```java
prefix + "EQSetBand:" + json
```

## APK-verified conversion

Class: `com.wifiaudio.view.pagesdevcenter.equalizersettings.adapter.a` (`BandEQAdapter`).

Both `onProgressChanged` and `onBindViewHolder` contain:

```java
String str = new DecimalFormat("#0.0").format(
    (((double) i) * 24.0 / 100.0) - 12.0
);
textView.setText(b(str));
```

Therefore:

```
display_dB = raw * 24 / 100 - 12
           = raw * 0.24 - 12
```

The formatter uses one decimal place and removes the trailing `.0` before appending `dB`.

Examples:

| raw | APK display |
|---:|---:|
| 0 | -12.0 dB |
| 25 | -6.0 dB |
| 35 | -3.6 dB |
| 40 | -2.4 dB |
| 50 | 0.0 dB |
| 60 | +2.4 dB |
| 75 | +6.0 dB |
| 100 | +12.0 dB |

The model default is raw 50, so the APK UI default is 0.0 dB.

## Reverse conversion

For a desired display gain:

```
raw = round((desired_dB + 12.0) * 100.0 / 24.0)
```

The APK source does not show a separate dB-to-raw calibration table. The slider progress itself is the raw value.

## Comparison with A97 hardware observations

A97 native UI observations are retained as HW-VERIFIED and are not overwritten:

| raw | APK | A97 HW |
|---:|---:|---:|
| 25 | -6.0 | -6.0 |
| 35 | -3.6 | -3.6 |
| 40 | -2.4 | -2.6 |
| 45 | -1.2 | -1.2 |
| 50 | 0.0 | 0.0 |
| 55 | +1.2 | +1.2 |
| 60 | +2.4 | +2.2 |
| 65 | +3.6 | +3.6 |
| 70 | +4.8 | +4.8 |
| 75 | +6.0 | +6.0 |

The APK formula is therefore **not declared hardware-calibrated**. The discrepancies are consistent with device-side quantisation/calibration or a different native display table.

## Implementation guidance

For an airControl UI compatible with 4STREAM, use:

```
raw = round((desired_dB + 12) * 100 / 24)
```

For A97 hardware-accurate room correction, retain the separate HW-VERIFIED table and do not replace it with the APK formula until additional device measurements establish equivalence.

No existing hardware-confirmed facts are changed by this report.
