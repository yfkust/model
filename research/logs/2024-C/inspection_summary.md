# 2024-C Blind Inspection Summary

## Scope and reproduction

This log reproduces only the data facts already used by the blind problem card. It does not train, select, or tune a model.

```bash
python research/logs/2024-C/inspection.py
```

Runtime dependencies: Python 3, NumPy, pandas, and openpyxl. The script resolves inputs from the repository root and reads only `papers/problems/2024/C题/`. `RANDOM_SEED=202409` is fixed; the current calculations are deterministic and use no sampling.

## Frozen definitions

- **B_peak:** `max(abs(B_t))` over the 1024 raw samples in one row.
- **THD:** after subtracting the row mean and normalizing by its absolute peak, let `X_k` be the 1024-point real-FFT magnitudes. `THD = sqrt(sum(|X_k|², k=2..N/2)) / |X_1|`.
- **Crest factor:** `max(abs(B_t - mean(B))) / RMS(B_t - mean(B))`.
- **Complete duplicate:** every cell across all 1028 columns is exactly equal within the same training sheet. `duplicate_excess_rows` counts copies beyond the first; `duplicate_excel_rows` lists all members including the first.
- **Boundary sample:** within the same material–temperature–waveform training cell, the test sample's frequency or B_peak lies outside that variable's separate training minimum/maximum. This is a one-variable-at-a-time range check. It is **not** a joint `frequency × B_peak` density, distance, or OOD test.
- **Shape convention:** reported shapes are data rows × columns and exclude the header row.
- **Exact waveform overlap:** SHA-256 equality of the raw 1024 float64 values in sequence; it does not detect approximate or phase-shifted matches.

## Reproduced statistics

### Training data

| material | rows | missing cells | waveform counts (sine / triangle / trapezoid) | frequency range Hz | loss range W/m³ | B_peak range T | duplicate Excel rows |
|---|---:|---:|---|---|---|---|---|
| 材料1 | 3400 | 0 | 1067 / 1412 / 921 | 50020–446410 | 684.046–3616132.536 | 0.010797–0.278951 | none |
| 材料2 | 3000 | 0 | 1097 / 1003 / 900 | 49990–501180 | 415.613–2750045.773 | 0.009638–0.313284 | none |
| 材料3 | 3200 | 0 | 1010 / 1078 / 1112 | 49990–501180 | 739.334–3525389.296 | 0.009733–0.313284 | 432, 908 |
| 材料4 | 2800 | 0 | 880 / 1455 / 465 | 50010–446690 | 452.228–2322456.147 | 0.010801–0.277600 | none |

Combined: 12,400 rows, zero missing cells, with 4,054 sine, 4,948 triangle, and 3,398 trapezoid samples.

### Q1 shape statistics

| waveform | n | median THD | median crest factor |
|---|---:|---:|---:|
| 正弦波 | 4054 | 0.0036 | 1.4151 |
| 三角波 | 4948 | 0.4531 | 1.7389 |
| 梯形波 | 3398 | 0.3636 | 1.6391 |

These are inspection statistics, not classification-performance estimates.

### Test and overlap checks

- Attachment 2: 80×1028, zero missing cells, no complete duplicate rows, unique sample IDs.
- Attachment 3: 400×1029, zero missing cells, no complete duplicate rows, unique sample IDs.
- Exact raw-waveform overlaps: training↔attachment 2 = 0; training↔attachment 3 = 0; attachment 2↔attachment 3 = 0.
- The defined marginal boundary check returns 9 attachment-3 IDs: `16, 19, 43, 55, 165, 294, 315, 394, 400`. Of these, 2 fail the frequency interval and 7 fail the B_peak interval.

## Grouped CV status

Grouped CV in the blind card is a modeling design principle. No fold-construction algorithm is frozen yet, and this inspection script does not create folds.

Before training, the fold definition must ensure:

- exact duplicates never cross folds;
- highly similar operating conditions are not mechanically scattered by random row splitting;
- preprocessing, feature selection, scaling, imputation, and learned transforms are fold-local;
- every baseline, candidate, and ablation uses exactly the same folds.

The operational definition and thresholds for a **near operating condition** remain unresolved. They must be declared and frozen before model fitting, using only inputs and experimental structure. They must not be adjusted after seeing model scores. Items still to freeze are: grouping variables, numeric tolerances or bins for frequency and B_peak, treatment of waveform similarity/phase, number of folds, stratification priorities, and deterministic tie handling.

Keep the first implementation simple. Its purpose is to prevent obvious information leakage, not to optimize a validation score through elaborate grouping.

## Q3 overlap warning

Controlling frequency and B_peak in a regression does not by itself make material, temperature, and waveform effects identifiable. Before interpreting adjusted effects, inspect common support in the joint `frequency × B_peak` region for the factor combinations being compared.

If overlap is insufficient, restrict the interpretation domain, compare only within common-support regions, or label the result as a conditional association that depends on model extrapolation. The blind card does not make a causal claim.
