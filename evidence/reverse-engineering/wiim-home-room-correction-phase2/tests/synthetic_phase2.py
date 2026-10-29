#!/usr/bin/env python3
"""Deterministic, standard-library-only DSP sanity fixtures for WiiM Phase 2.

These tests exercise independent mathematical fixtures, not a clone of WiiM.
They do not read A33 recordings, touch hardware, or modify source artifacts.
"""
from __future__ import annotations

import json
import math
import random
import statistics

FS = 48_000
NCC_GATE = 0.1  # observed state scalar supplied to fast_ncc in time_align


def noise(n: int, seed: int = 481) -> list[float]:
    r = random.Random(seed)
    return [r.uniform(-1.0, 1.0) for _ in range(n)]


def energy(x: list[float]) -> float:
    return sum(v * v for v in x)


def ncc_at(reference: list[float], capture: list[float], offset: int) -> float:
    a = reference
    b = capture[offset : offset + len(a)]
    if len(b) != len(a):
        return 0.0
    # fast_ncc subtracts the mean from its first vector; its sliding-window
    # denominator uses the second vector's raw sum of squares.
    mean = sum(a) / len(a)
    ac = [v - mean for v in a]
    den = math.sqrt(energy(ac) * energy(b) + 1e-10)
    return abs(sum(x * y for x, y in zip(ac, b)) / den)


def best_integer_ncc(reference: list[float], capture: list[float], lo: int, hi: int):
    vals = [(ncc_at(reference, capture, k), k) for k in range(lo, hi + 1)]
    return max(vals)


def linear_sample(x: list[float], i: float) -> float:
    j = int(math.floor(i))
    f = i - j
    if j < 0 or j + 1 >= len(x):
        return 0.0
    return x[j] * (1 - f) + x[j + 1] * f


def ncc_fractional(reference: list[float], capture: list[float], center: int,
                   window: int = 512, limit: float = 8.0, step: float = 0.02):
    cap = capture[center : center + window]
    mean = sum(cap) / len(cap)
    capc = [v - mean for v in cap]
    cap_e = energy(capc)
    best = (-1.0, 0.0)
    count = int(round(2 * limit / step))
    for q in range(count + 1):
        lag = -limit + q * step
        ref = [linear_sample(reference, center + i + lag) for i in range(window)]
        rm = sum(ref) / len(ref)
        refc = [v - rm for v in ref]
        den = math.sqrt(energy(refc) * cap_e + 1e-20)
        score = abs(sum(a * b for a, b in zip(refc, capc)) / den)
        if score > best[0]:
            best = (score, lag)
    return best[1], best[0]


def linear_slope(xs: list[float], ys: list[float]) -> float:
    xm, ym = statistics.mean(xs), statistics.mean(ys)
    return sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)


def dft_amplitude(x: list[float], k: int) -> complex:
    n = len(x)
    re = sum(v * math.cos(2 * math.pi * k * i / n) for i, v in enumerate(x)) * 2 / n
    im = -sum(v * math.sin(2 * math.pi * k * i / n) for i, v in enumerate(x)) * 2 / n
    return complex(re, im)


def run():
    out = []

    # Known delay and a weaker echo: the fixture checks only the dominant NCC lag.
    ref = noise(4096)
    delay = 211
    cap = [0.0] * (delay + len(ref) + 500)
    for i, v in enumerate(ref):
        cap[delay + i] += v
        if delay + i + 53 < len(cap):
            cap[delay + i + 53] += 0.28 * v
    score, found = best_integer_ncc(ref, cap, 0, 500)
    out.append({"test": "known delay + weaker reflection", "expected_samples": delay,
                "measured_samples": found, "absolute_error_samples": abs(found - delay),
                "ncc": round(score, 6), "status": "PASS" if found == delay else "FAIL",
                "scope": "NCC fixture only; not WiiM's complete delay/window routine"})

    # Exact transfer response of a periodic multisine through a known circular FIR.
    n = 8192
    bins = [31, 67, 131, 251, 503]
    x = [sum(math.cos(2 * math.pi * k * i / n) for k in bins) for i in range(n)]
    taps = [(0, 0.72), (48, 0.18), (137, -0.11)]
    y = [sum(g * x[(i - d) % n] for d, g in taps) for i in range(n)]
    errors = []
    for k in bins:
        measured = dft_amplitude(y, k) / dft_amplitude(x, k)
        w = 2 * math.pi * k / n
        expected = sum(g * complex(math.cos(-w * d), math.sin(-w * d)) for d, g in taps)
        errors.append(abs(20 * math.log10(abs(measured)) - 20 * math.log10(abs(expected))))
    mae = statistics.mean(errors)
    out.append({"test": "known frequency response (periodic FIR)", "bins": bins,
                "mean_abs_error_db": round(mae, 10), "status": "PASS" if mae < 1e-8 else "FAIL",
                "scope": "DFT identity check; not tfplots_new validation"})

    # Clock drift: synthetic recording samples reference at n*(1+ppm), then
    # independent local lags are regressed. This is specifically a test fixture
    # for what a drift estimator could measure; the inspected WiiM path has none.
    base = noise(52_000, 90210)
    drift_rows = []
    for ppm in (-100, -50, -25, 25, 50, 100):
        rec = [linear_sample(base, i * (1 + ppm * 1e-6)) for i in range(48_000)]
        centers = [3_000, 11_000, 19_000, 27_000, 35_000, 43_000]
        lags, times = [], []
        for c in centers:
            lag, _ = ncc_fractional(base, rec, c)
            lags.append(lag)
            times.append(c / FS)
        measured = linear_slope(times, lags) / FS * 1e6
        err = abs(measured - ppm)
        drift_rows.append({"requested_ppm": ppm, "estimated_ppm": round(measured, 2),
                           "absolute_error_ppm": round(err, 2), "status": "PASS" if err <= 8 else "FAIL"})
    out.append({"test": "clock-drift observability ±25/50/100 ppm", "cases": drift_rows,
                "status": "PASS" if all(x["status"] == "PASS" for x in drift_rows) else "FAIL",
                "scope": "synthetic estimator observability; no claim WiiM compensates drift"})

    # Very low SNR case for the observed NCC floor (0.1) used in the initial gate.
    r = random.Random(77)
    ref = noise(4096, 12)
    delay = 180
    cap = [r.gauss(0, 20.0) for _ in range(delay + len(ref) + 100)]
    for i, v in enumerate(ref):
        cap[delay + i] += v
    low = ncc_at(ref, cap, delay)
    out.append({"test": "very-low-SNR NCC gate", "noise_rms_to_signal_rms": 20,
                "measured_ncc": round(low, 6), "observed_gate": NCC_GATE,
                "gate_result": "reject" if low < NCC_GATE else "pass",
                "status": "PASS" if low < NCC_GATE else "FAIL",
                "scope": "single known alignment; NCC gate only, not complete WiiM quality logic"})

    # Two identical separated markers produce two comparable peaks. This proves
    # ambiguity exists in a fixture and that callers must examine competitor peaks.
    ref = noise(2048, 3)
    cap = [0.0] * 9000
    for off in (500, 4500):
        cap[off : off + len(ref)] = ref[:]
    peaks = sorted(((ncc_at(ref, cap, k), k) for k in range(0, 6000)), reverse=True)[:2]
    ambiguous = abs(peaks[0][0] - peaks[1][0]) < 1e-9
    out.append({"test": "two equal separated correlation peaks", "peaks": [
                    {"lag": lag, "ncc": round(score, 6)} for score, lag in peaks],
                "ambiguous_fixture": ambiguous, "status": "PASS" if ambiguous else "FAIL",
                "scope": "the test harness detects ambiguity; no explicit runner-up ratio was found in inspected WiiM helpers"})

    # Truncated sweep is padded to pass the coarse record-length ratio but loses
    # the latter half of the waveform; an NCC check should reject it.
    ref = noise(4096, 38)
    cut = 2300
    cap = [0.0] * 300 + ref[:cut] + [0.0] * 5000
    trunc = ncc_at(ref, cap, 300)
    trunc_pass = trunc >= NCC_GATE
    out.append({"test": "truncated sweep padded to legal file-size ratio", "retained_samples": cut,
                "reference_samples": len(ref), "measured_ncc": round(trunc, 6),
                "observed_gate": NCC_GATE, "gate_result": "reject" if trunc < NCC_GATE else "pass",
                "status": "PASS" if trunc_pass else "FAIL",
                "finding": "This fixture confirms the NCC gate alone does not reject this partial correlated segment; later WiiM IR/main-sub gates may still reject it.",
                "scope": "synthetic; actual later IR/main-sub checks are not emulated"})

    # Missing prompt: unrelated capture has no reference tone/template match.
    ref = noise(2048, 56)
    cap = noise(9000, 98)
    best, lag = max((ncc_at(ref, cap, k), k) for k in range(len(cap) - len(ref) + 1))
    out.append({"test": "missing prompt/reference marker", "maximum_ncc": round(best, 6),
                "observed_gate": NCC_GATE, "gate_result": "reject" if best < NCC_GATE else "pass",
                "status": "PASS" if best < NCC_GATE else "FAIL",
                "scope": "uncorrelated deterministic noise; prompt detector itself is not emulated"})

    result = {"suite": "WiiM Home 3.6.10.260924 Phase 2 synthetic fixtures",
              "seeded": True, "dependencies": "Python standard library only",
              "hardware": "not used", "WiiM_clone": False, "tests": out,
              "overall": "PASS" if all(t.get("status") == "PASS" for t in out) else "FAIL"}
    print(json.dumps(result, indent=2))
    if result["overall"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    run()
