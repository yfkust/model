#!/usr/bin/env python3
"""Reproduce the metadata and light statistics used by the 2024-C blind card."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 202409
ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "papers" / "problems" / "2024" / "C题"
TRAIN_SHEETS = (
    ("附件一（训练集）sheet12.xlsx", "材料1"),
    ("附件一（训练集）sheet12.xlsx", "材料2"),
    ("附件一（训练集）sheet34.xlsx", "材料3"),
    ("附件一（训练集）sheet34.xlsx", "材料4"),
)
WAVE_ORDER = ("正弦波", "三角波", "梯形波")


def waveform_hashes(values: np.ndarray) -> set[str]:
    values = np.ascontiguousarray(values, dtype="<f8")
    return {hashlib.sha256(row.tobytes()).hexdigest() for row in values}


def range_pair(values: np.ndarray) -> list[float]:
    return [float(np.min(values)), float(np.max(values))]


def shape_features(flux: np.ndarray) -> pd.DataFrame:
    centered = flux - flux.mean(axis=1, keepdims=True)
    scale = np.max(np.abs(centered), axis=1, keepdims=True)
    normalized = centered / scale
    spectrum = np.abs(np.fft.rfft(normalized, axis=1))
    fundamental = np.maximum(spectrum[:, 1], np.finfo(float).eps)
    return pd.DataFrame(
        {
            "thd": np.sqrt(np.sum(spectrum[:, 2:] ** 2, axis=1)) / fundamental,
            "crest_factor": 1 / np.sqrt(np.mean(normalized**2, axis=1)),
        }
    )


def main() -> None:
    np.random.seed(RANDOM_SEED)  # No random operation currently; freezes future additions.
    material_stats: dict[str, object] = {}
    all_meta = []
    all_shape = []
    train_wave_hashes: set[str] = set()
    total_missing = 0

    for filename, material in TRAIN_SHEETS:
        frame = pd.read_excel(DATA_DIR / filename, sheet_name=material)
        flux = frame.iloc[:, 4:].to_numpy(dtype=float)
        b_peak = np.max(np.abs(flux), axis=1)
        duplicate_mask = frame.duplicated(keep=False)
        duplicate_rows = (np.flatnonzero(duplicate_mask) + 2).tolist()
        missing = int(frame.isna().sum().sum())
        total_missing += missing

        material_stats[material] = {
            "file": filename,
            "shape_data_rows_by_columns": list(frame.shape),
            "missing_cells": missing,
            "duplicate_excess_rows": int(frame.duplicated().sum()),
            "duplicate_excel_rows": duplicate_rows,
            "waveform_counts": {
                wave: int((frame.iloc[:, 3] == wave).sum()) for wave in WAVE_ORDER
            },
            "frequency_hz_range": range_pair(frame.iloc[:, 1].to_numpy()),
            "loss_w_per_m3_range": range_pair(frame.iloc[:, 2].to_numpy()),
            "b_peak_t_range": range_pair(b_peak),
        }

        meta = pd.DataFrame(
            {
                "material": material,
                "temperature": frame.iloc[:, 0],
                "frequency": frame.iloc[:, 1],
                "loss": frame.iloc[:, 2],
                "waveform": frame.iloc[:, 3],
                "b_peak": b_peak,
            }
        )
        features = shape_features(flux)
        features["waveform"] = frame.iloc[:, 3].to_numpy()
        all_meta.append(meta)
        all_shape.append(features)
        train_wave_hashes.update(waveform_hashes(flux))

    train_meta = pd.concat(all_meta, ignore_index=True)
    shape = pd.concat(all_shape, ignore_index=True)
    shape_summary = {}
    for wave in WAVE_ORDER:
        subset = shape[shape["waveform"] == wave]
        shape_summary[wave] = {
            "n": int(len(subset)),
            "thd_median": float(subset["thd"].median()),
            "crest_factor_median": float(subset["crest_factor"].median()),
        }

    tests = {}
    test_hashes = {}
    test3_meta = None
    for filename, flux_start in (("附件二（测试集）.xlsx", 4), ("附件三（测试集）.xlsx", 5)):
        frame = pd.read_excel(DATA_DIR / filename, sheet_name="测试集")
        flux = frame.iloc[:, flux_start:].to_numpy(dtype=float)
        key = "attachment_2" if flux_start == 4 else "attachment_3"
        tests[key] = {
            "file": filename,
            "shape_data_rows_by_columns": list(frame.shape),
            "missing_cells": int(frame.isna().sum().sum()),
            "duplicate_excess_rows": int(frame.duplicated().sum()),
            "sample_id_unique": bool(frame.iloc[:, 0].is_unique),
        }
        test_hashes[key] = waveform_hashes(flux)
        if key == "attachment_3":
            test3_meta = pd.DataFrame(
                {
                    "sample_id": frame.iloc[:, 0],
                    "material": frame.iloc[:, 3],
                    "temperature": frame.iloc[:, 1],
                    "frequency": frame.iloc[:, 2],
                    "waveform": frame.iloc[:, 4],
                    "b_peak": np.max(np.abs(flux), axis=1),
                }
            )

    bounds = (
        train_meta.groupby(["material", "temperature", "waveform"], as_index=False)
        .agg(
            frequency_min=("frequency", "min"),
            frequency_max=("frequency", "max"),
            b_peak_min=("b_peak", "min"),
            b_peak_max=("b_peak", "max"),
        )
    )
    checked = test3_meta.merge(
        bounds, on=["material", "temperature", "waveform"], how="left", validate="many_to_one"
    )
    frequency_outside = (checked["frequency"] < checked["frequency_min"]) | (
        checked["frequency"] > checked["frequency_max"]
    )
    b_peak_outside = (checked["b_peak"] < checked["b_peak_min"]) | (
        checked["b_peak"] > checked["b_peak_max"]
    )
    boundary_ids = checked.loc[frequency_outside | b_peak_outside, "sample_id"].astype(int)

    template = pd.read_excel(DATA_DIR / "附件四（Excel表）.xlsx", sheet_name="Sheet1")
    result = {
        "definitions": {
            "random_seed": RANDOM_SEED,
            "b_peak": "max(abs(B_t)) over the 1024 raw samples",
            "thd": "sqrt(sum(|X_k|^2, k=2..N/2)) / |X_1| after row centering and peak normalization",
            "crest_factor": "max(abs(centered B)) / RMS(centered B)",
            "duplicate": "all cells in two rows are exactly equal within the same sheet",
            "boundary_sample": (
                "within the same material-temperature-waveform cell, frequency OR B_peak "
                "falls outside the separate training min/max interval; this is not joint OOD"
            ),
        },
        "training": {
            "total_rows": int(len(train_meta)),
            "total_missing_cells": total_missing,
            "waveform_counts": {
                wave: int((train_meta["waveform"] == wave).sum()) for wave in WAVE_ORDER
            },
            "frequency_hz_range": range_pair(train_meta["frequency"].to_numpy()),
            "loss_w_per_m3_range": range_pair(train_meta["loss"].to_numpy()),
            "b_peak_t_range": range_pair(train_meta["b_peak"].to_numpy()),
            "materials": material_stats,
            "q1_shape_statistics": shape_summary,
        },
        "tests": tests,
        "exact_waveform_overlap_counts": {
            "training_vs_attachment_2": len(train_wave_hashes & test_hashes["attachment_2"]),
            "training_vs_attachment_3": len(train_wave_hashes & test_hashes["attachment_3"]),
            "attachment_2_vs_attachment_3": len(
                test_hashes["attachment_2"] & test_hashes["attachment_3"]
            ),
        },
        "attachment_3_univariate_boundary_check": {
            "count": int(len(boundary_ids)),
            "sample_ids": boundary_ids.tolist(),
            "frequency_outside_count": int(frequency_outside.sum()),
            "b_peak_outside_count": int(b_peak_outside.sum()),
            "definition_warning": "Separate marginal min/max check, not a joint-distribution OOD test.",
        },
        "output_template": {
            "sheet1_shape_data_rows_by_columns": list(template.shape),
            "blank_result_cells": int(template.iloc[:, 1:].isna().sum().sum()),
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
