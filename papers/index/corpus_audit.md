# Corpus audit report

> Audit scope: filesystem structure and file metadata only. No paper body was extracted or analyzed; 2025 files were not opened as documents.

## Summary

- Problem corpus: 957 files; excellent-paper corpus: 101 files.
- Expected 2020–2024 C/D/E problem groups missing: none.
- Expected 2020–2024 C/D/E excellent-paper groups missing: none.
- Groups without a filename-identified statement/supplement candidate: none.
- Exact duplicate groups (SHA-256): 0.
- Signature/extension mismatches: 1; naming warnings: 110; unassigned problem files: 2.

## Coverage by problem-year

| group | problem files | excellent papers |
|---|---:|---:|
| 2020-C | 23 | 6 |
| 2020-D | 1 | 6 |
| 2020-E | 111 | 6 |
| 2021-C | 8 | 7 |
| 2021-D | 5 | 7 |
| 2021-E | 654 | 7 |
| 2022-C | 5 | 7 |
| 2022-D | 4 | 7 |
| 2022-E | 115 | 7 |
| 2023-C | 5 | 10 |
| 2023-D | 2 | 9 |
| 2023-E | 7 | 10 |
| 2024-C | 6 | 4 |
| 2024-D | 1 | 4 |
| 2024-E | 2 | 4 |
| 2025-A | 1 | 0 |
| 2025-B | 1 | 0 |
| 2025-C | 1 | 0 |
| 2025-D | 1 | 0 |
| 2025-E | 1 | 0 |
| 2025-F | 1 | 0 |

## Problem file formats

| extension | files |
|---|---:|
| bmp | 100 |
| csv | 3 |
| doc | 15 |
| docx | 26 |
| his | 6 |
| jfif | 1 |
| md | 2 |
| pdf | 10 |
| txt | 651 |
| xls | 78 |
| xlsx | 65 |

## Exact duplicates

None detected.

## Format anomalies

- `papers/problems/2022/E/数据集/监测点数据/~$古自治区锡林郭勒盟典型草原轮牧放牧样地群落结构监测数据集（2016年6月1日-2020年9月17日）数据说明.docx`: extension/signature mismatch

## Naming and placement anomalies

- `stray_space`: 3 files.
- `suspected_mojibake`: 107 files.
- `temporary_office_file`: 1 files.

Representative flagged paths:

- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20191216/PTU_R06_15.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20191216/VIS_R06_15.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20191216/WIND_R06_15.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20200313/PTU_R06_12.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20200313/VIS_R06_12.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS20200313/WIND_R06_12.his`: suspected_mojibake
- `papers/problems/2020/2020年E题/机场AMOS观测/╗·│íAMOS╣█▓Γ/AMOS╫╩┴╧╕±╩╜╦╡├≈ .docx`: suspected_mojibake;stray_space
- `papers/problems/2020/2020年E题/高速公路视频截图/╕▀╦┘╣½┬╖╩╙╞╡╜╪═╝/original_frame1.bmp`: suspected_mojibake
- `papers/problems/2020/2020年E题/高速公路视频截图/╕▀╦┘╣½┬╖╩╙╞╡╜╪═╝/original_frame10.bmp`: suspected_mojibake
- `papers/problems/2020/2020年E题/高速公路视频截图/╕▀╦┘╣½┬╖╩╙╞╡╜╪═╝/original_frame100.bmp`: suspected_mojibake
- … 100 additional flagged files are recorded in the inventory CSV.
- `papers/problems/2023/附表1-检索表格-流水号vs时间(1).xlsx`: cannot assign to C/D/E from its path
- `papers/problems/2024/“华为杯”第二十一届中国研究生数学建模竞赛F题附录.docx`: cannot assign to C/D/E from its path
- `papers/problems/2024/“华为杯”第二十一届中国研究生数学建模竞赛F题附录.docx`: F material is outside the declared 2020–2024 C/D/E scope.
- Problem directory naming is inconsistent across years (`2020年C题`, `C`, `C题`, and flat files). Inventory normalization handles this without renaming sources.

## Interpretation limits

- Presence means at least one file was assigned to a problem-year; completeness against an authoritative release manifest is not proven.
- Exact-duplicate detection does not identify near-duplicates or equivalent documents saved in different formats.
- `statement_or_supplement` is a filename-based role, not a claim about document contents.
- 2025 A–F are inventory-only blind-test records and must remain excluded from analysis.
