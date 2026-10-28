# 4STREAM Eq10HP A97 display discrepancy follow-up

Status: **RESOLVED / HW-VERIFIED**

Related report: `evidence/reverse-engineering/4STREAM-EQ10HP-RAW-DB-MAPPING-2026-10-28.md`

## New HW-VERIFIED observations

A97 / ALLWINNER-R328 / Linkplay 4.6.437434 / `Eq10HP_ver_1.0`:

- raw 40 at index 0 (31 Hz) was set through `EQSetBand`, then checked in native 4STREAM UI: **-2.6 dB**.
- raw 60 at index 0 was set through `EQSetBand`, then checked in native 4STREAM UI: **+2.2 dB**.
- The band was returned to raw 50 after the test.

These repeat the earlier HW series and are retained as HW-VERIFIED.

## Resolution — HW-VERIFIED 2026-10-28

The discriminating readback test resolved the discrepancy:

- `EQSetBand` requested raw `40` at index 0; the command returned `{"status":"OK"}`, but the subsequent `EQGetBand` returned actual `value:39` for index 0. `39 * 0.24 - 12 = -2.64 dB`, displayed by 4STREAM as **-2.6 dB**.
- `EQSetBand` requested raw `60` at index 0; the command returned `{"status":"OK"}`, but the subsequent `EQGetBand` returned actual `value:59` for index 0. `59 * 0.24 - 12 = +2.16 dB`, displayed by 4STREAM as **+2.2 dB**.

Therefore the previously observed display values are fully consistent with the APK-verified `BandEQAdapter` formula when the **actual firmware readback value** is used. The sent `EQSetBand` integer must not be assumed to be the stored/applied integer merely because the write returns `OK`.

For control/room-correction implementations, write followed by `EQGetBand` readback is required when the exact applied gain matters; calculate/display the effective gain from the readback raw value.

The internal firmware rule that maps some requested values to adjacent stored values is **not yet characterized**. This report resolves the display discrepancy, not the complete quantisation algorithm.

## Static APK data-flow evidence

### Read path

```
com.wifiaudio.action.e
  -> EQGetBand
  -> com.wifiaudio.view.pagesdevcenter.equalizersettings.FragNewEQ
  -> JSON object EQBand[]
  -> model.a.setIndex(int)
  -> model.a.setValue(int)
  -> FragNewEQ.R0()
  -> adapter.a.c(ArrayList)
  -> adapter.a.onBindViewHolder()
  -> VerticalSeekBar.setProgress(value)
```

The parser is explicit:

```java
aVar.setIndex(jsonObject2.getInt("index"));
aVar.setValue(jsonObject2.getInt("value"));
```

The model default is:

```java
private int value = 50;
```

No arithmetic or clamping is performed between JSON `value` and `model.a.value`.

### Display path

Class: `com.wifiaudio.view.pagesdevcenter.equalizersettings.adapter.a` (`BandEQAdapter`).

```java
int value = aVar.getValue();
holder.c().setProgress(value);

String str = new DecimalFormat("#0.0").format(
    (((double) value) * 24.0 / 100.0) - 12.0
);
textView.setText(b(str));
```

The same expression is used in `onProgressChanged`:

```java
aVar.setValue(i);
String str = new DecimalFormat("#0.0").format(
    (((double) i) * 24.0 / 100.0) - 12.0
);
```

Therefore the identified APK path necessarily produces:

```
raw 40 -> -2.4 dB
raw 60 -> +2.4 dB
```

### Write path

```
SeekBar progress
  -> model.a.setValue(i)
  -> {"EQBand":[{"index":N, "value":i}]}
  -> com.wifiaudio.action.e.o0()
  -> EQSetBand:<json>
```

The write path sends the same integer that was in the SeekBar progress. No APK-side calibration is present in this path.

## FragNewEQ versus FragNewEQV2

`FragNewEQV2 extends FragNewEQ`.

Both paths use the inherited band adapter field and inherited read/write methods. `FragNewEQV2.U0(Context)` creates the specialized preset adapter `equalizersettings.e.d`, but that adapter's `i(...)` method still creates `adapter.b` for preset lists; the actual 10 vertical band controls remain `adapter.a` (`BandEQAdapter`).

`FragMixEQ.g2()` creates `new FragNewEQV2()`. The fallback helper `equalizersettings.e.c.c()` can create `new FragNewEQ()` when the non-mixed screen is used. No inspected condition selects a second raw-to-dB conversion for `ALLWINNER-R328`, `a97_rakoit`, or `Eq10HP_ver_1.0`.

The inspected source contains no proven device-specific branch that changes the `adapter.a` formula. Static absence is bounded to the decompiled APK and does not prove that no reflective/native/runtime path exists.

## What the APK does and does not explain

The identified 4STREAM Eq10HP implementation cannot produce -2.6 dB from an **actual/readback** raw 40 or +2.2 dB from an **actual/readback** raw 60. Hardware readback established that the actual values were 39 and 59 respectively, which do produce the observed display values through the identified `BandEQAdapter` path.

No APK evidence currently proves:

- a second Eq10HP Band adapter;
- a device-specific R328/A97 correction;
- a lookup/calibration table;
- a pre-adapter raw transformation;
- a different formatter for these two values;
- JNI/native alteration of the value;
- a readback value differing from the sent value.

The discrepancy is resolved by firmware readback: the stored/readback integer differs from the requested integer for the two tested points. No alternate 4STREAM display scale is required to explain these observations.

## Discriminating test result

The proposed readback test was performed on hardware and resolved the discrepancy. Requested `40` read back as `39`; requested `60` read back as `59`. A second-runtime-UI test is therefore not required to explain these two observations.

## Classification

- **APK-VERIFIED:** `EQGetBand` JSON value is assigned directly to the band model; `BandEQAdapter` uses `value * 0.24 - 12`; `EQSetBand` serializes the requested integer.
- **HW-VERIFIED:** requested raw 40 -> readback raw 39 -> native 4STREAM **-2.6 dB**; requested raw 60 -> readback raw 59 -> native 4STREAM **+2.2 dB**, verified 2026-10-28.
- **RESOLVED:** the observed dB discrepancy is explained by the difference between requested and firmware readback raw values.
- **UNKNOWN:** the complete firmware quantisation/normalisation rule for all requested raw values remains uncharacterized.

## Full requested -> readback sweep — HW-VERIFIED 2026-10-28

A complete automated sweep was performed on A97 index 0 (31 Hz): requested raw values 0 through 100 were written one at a time with `EQSetBand`, followed by `EQGetBand` readback. The test restored requested raw 50 at the end and confirmed `readback=50`.

Results establish:

- The accepted/readback domain spans raw 0..100, corresponding under the APK-verified display formula to -12.0..+12.0 dB.
- 76 of 101 requested values read back unchanged.
- 25 requested values read back exactly one count lower; no tested value read back higher and no tested delta exceeded -1.
- Changed requested->readback pairs: 1→0, 2→1, 5→4, 6→5, 10→9, 11→10, 14→13, 20→19, 22→21, 30→29, 40→39, 43→42, 44→43, 49→48, 53→52, 59→58, 60→59, 61→60, 80→79, 81→80, 86→85, 87→86, 88→87, 89→88, 98→97.
- The changed values are irregularly distributed across 0..100. This sweep does **not** establish a simple periodic quantisation rule, so the internal firmware mapping mechanism remains UNKNOWN.
- For exact room-correction control, the implementation must treat `EQGetBand` readback as authoritative after a write. Effective gain is `readback_raw * 0.24 - 12` dB for the verified 4STREAM display mapping.

This sweep also independently reproduces the discrepancy-resolution points `40→39` and `60→59`.