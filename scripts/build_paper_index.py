#!/usr/bin/env python3
"""Build metadata-only inventories and an audit for the modeling corpus."""

from __future__ import annotations

import csv
import hashlib
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "papers" / "problems"
PAPERS = ROOT / "papers" / "excellent_papers"
INDEX = ROOT / "papers" / "index"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def signature_status(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    with path.open("rb") as stream:
        head = stream.read(16)
    signatures = {
        ".pdf": (b"%PDF-", "PDF"),
        ".doc": (bytes.fromhex("D0CF11E0A1B11AE1"), "OLE compound document"),
        ".xls": (bytes.fromhex("D0CF11E0A1B11AE1"), "OLE compound document"),
        ".bmp": (b"BM", "BMP"),
        ".jfif": (bytes.fromhex("FFD8FF"), "JPEG"),
    }
    if suffix in signatures:
        magic, label = signatures[suffix]
        return label, "ok" if head.startswith(magic) else "signature_mismatch"
    if suffix in {".docx", ".xlsx"}:
        try:
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
            marker = "word/document.xml" if suffix == ".docx" else "xl/workbook.xml"
            return "OOXML", "ok" if marker in names else "signature_mismatch"
        except zipfile.BadZipFile:
            return "OOXML", "signature_mismatch"
    if suffix in {".csv", ".txt", ".md", ".his"}:
        return "text_or_domain_data", "unchecked"
    return "unknown", "unchecked"


def naming_flags(path: Path) -> str:
    text = path.as_posix()
    flags = []
    if any(char in text for char in "╣║╗╚╔╬┴┘┬┐├┤┼│─▓Γ╕▀╦╩╙╞╡╜╪═╝╫╧±≈"):
        flags.append("suspected_mojibake")
    if path.name.startswith("~$"):
        flags.append("temporary_office_file")
    if path.stem != path.stem.strip() or " ." in path.name:
        flags.append("stray_space")
    if len(text) > 240:
        flags.append("path_over_240_chars")
    return ";".join(flags)


def problem_key(path: Path) -> tuple[str, str]:
    relative = path.relative_to(PROBLEMS)
    year = relative.parts[0]
    if year == "2025":
        match = re.match(r"([A-F])题", path.name)
    else:
        match = None
        for part in relative.parts[1:]:
            match = re.match(r"(?:20\d{2}年)?([CDE])(?:题|$)", part)
            if match:
                break
    return year, match.group(1) if match else "UNASSIGNED"


def problem_role(path: Path, year: str, problem: str) -> str:
    if year == "2025":
        return "blind_test_statement"
    name = path.stem
    relative = path.relative_to(PROBLEMS)
    direct_office_document = (
        path.suffix.lower() in {".doc", ".docx"}
        and not name.startswith("附件")
        and len(relative.parts) <= 3
    )
    if problem != "UNASSIGNED" and (direct_office_document or "题" in name):
        return "statement_or_supplement"
    return "attachment"


def paper_key(path: Path) -> tuple[str, str, str, str]:
    relative = path.relative_to(PAPERS)
    year_match = re.search(r"20\d{2}", relative.parts[0])
    paper_match = re.match(r"([CDE])(\d+)$", path.stem)
    year = year_match.group(0) if year_match else "UNKNOWN"
    problem = paper_match.group(1) if paper_match else "UNASSIGNED"
    paper_id = path.stem if paper_match else "UNKNOWN"
    award = "star_nominee" if "获数模之星提名奖" in relative.parts else "excellent_paper"
    return year, problem, paper_id, award


def metadata(path: Path) -> dict[str, str | int]:
    detected, status = signature_status(path)
    return {
        "file_path": path.relative_to(ROOT).as_posix(),
        "extension": path.suffix.lower().lstrip("."),
        "size_bytes": path.stat().st_size,
        "sha256": digest(path),
        "detected_format": detected,
        "format_status": status,
        "naming_flags": naming_flags(path),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def build() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    problem_rows = []
    for path in sorted(p for p in PROBLEMS.rglob("*") if p.is_file()):
        year, problem = problem_key(path)
        file_metadata = metadata(path)
        stable_suffix = hashlib.sha256(str(file_metadata["file_path"]).encode()).hexdigest()[:12]
        problem_rows.append({
            "record_id": f"problem:{year}:{problem}:{stable_suffix}",
            "year": year,
            "problem": problem,
            "aggregation_key": f"{year}-{problem}",
            "material_role": problem_role(path, year, problem),
            "blind_test": "yes" if year == "2025" else "no",
            **file_metadata,
        })

    paper_rows = []
    for path in sorted(p for p in PAPERS.rglob("*") if p.is_file()):
        year, problem, paper_id, award = paper_key(path)
        paper_rows.append({
            "record_id": f"paper:{year}:{problem}:{paper_id}",
            "year": year,
            "problem": problem,
            "aggregation_key": f"{year}-{problem}",
            "paper_id": paper_id,
            "award_group": award,
            **metadata(path),
        })
    return problem_rows, paper_rows


def duplicate_groups(rows: list[dict[str, object]]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        groups[str(row["sha256"])].append(str(row["file_path"]))
    return [paths for paths in groups.values() if len(paths) > 1]


def render_audit(problem_rows: list[dict[str, object]], paper_rows: list[dict[str, object]]) -> str:
    p_counts = Counter((str(r["year"]), str(r["problem"])) for r in problem_rows)
    e_counts = Counter((str(r["year"]), str(r["problem"])) for r in paper_rows)
    ext_counts = Counter(str(r["extension"]) for r in problem_rows)
    expected = [(str(y), p) for y in range(2020, 2025) for p in "CDE"]
    missing_problem_groups = [f"{y}-{p}" for y, p in expected if not p_counts[y, p]]
    missing_paper_groups = [f"{y}-{p}" for y, p in expected if not e_counts[y, p]]
    statement_groups = {
        (str(r["year"]), str(r["problem"]))
        for r in problem_rows
        if r["material_role"] == "statement_or_supplement"
    }
    missing_statement_candidates = [f"{y}-{p}" for y, p in expected if (y, p) not in statement_groups]
    duplicates = duplicate_groups(problem_rows + paper_rows)
    bad_formats = [r for r in problem_rows + paper_rows if r["format_status"] == "signature_mismatch"]
    flagged = [r for r in problem_rows + paper_rows if r["naming_flags"]]
    unassigned = [r for r in problem_rows if r["problem"] == "UNASSIGNED"]
    lines = [
        "# Corpus audit report",
        "",
        "> Audit scope: filesystem structure and file metadata only. No paper body was extracted or analyzed; 2025 files were not opened as documents.",
        "",
        "## Summary",
        "",
        f"- Problem corpus: {len(problem_rows)} files; excellent-paper corpus: {len(paper_rows)} files.",
        f"- Expected 2020–2024 C/D/E problem groups missing: {', '.join(missing_problem_groups) or 'none'}.",
        f"- Expected 2020–2024 C/D/E excellent-paper groups missing: {', '.join(missing_paper_groups) or 'none'}.",
        f"- Groups without a filename-identified statement/supplement candidate: {', '.join(missing_statement_candidates) or 'none'}.",
        f"- Exact duplicate groups (SHA-256): {len(duplicates)}.",
        f"- Signature/extension mismatches: {len(bad_formats)}; naming warnings: {len(flagged)}; unassigned problem files: {len(unassigned)}.",
        "",
        "## Coverage by problem-year",
        "",
        "| group | problem files | excellent papers |",
        "|---|---:|---:|",
    ]
    for year in map(str, range(2020, 2026)):
        letters = "ABCDEF" if year == "2025" else "CDE"
        for problem in letters:
            lines.append(f"| {year}-{problem} | {p_counts[year, problem]} | {e_counts[year, problem]} |")
    lines += ["", "## Problem file formats", "", "| extension | files |", "|---|---:|"]
    lines += [f"| {ext or '(none)'} | {count} |" for ext, count in sorted(ext_counts.items())]
    lines += ["", "## Exact duplicates", ""]
    if duplicates:
        for number, paths in enumerate(duplicates, 1):
            lines.append(f"{number}. " + " ↔ ".join(f"`{p}`" for p in paths))
    else:
        lines.append("None detected.")
    lines += ["", "## Format anomalies", ""]
    if bad_formats:
        lines += [f"- `{r['file_path']}`: extension/signature mismatch" for r in bad_formats]
    else:
        lines.append("No mismatches detected for formats with a checked signature. Text/domain-specific files remain `unchecked`.")
    lines += ["", "## Naming and placement anomalies", ""]
    flag_counts = Counter(flag for r in flagged for flag in str(r["naming_flags"]).split(";") if flag)
    lines += [f"- `{flag}`: {count} files." for flag, count in sorted(flag_counts.items())]
    lines += ["", "Representative flagged paths:", ""]
    lines += [f"- `{r['file_path']}`: {r['naming_flags']}" for r in flagged[:10]]
    if len(flagged) > 10:
        lines.append(f"- … {len(flagged) - 10} additional flagged files are recorded in the inventory CSV.")
    lines += [f"- `{r['file_path']}`: cannot assign to C/D/E from its path" for r in unassigned]
    lines += [
        "- `papers/problems/2024/“华为杯”第二十一届中国研究生数学建模竞赛F题附录.docx`: F material is outside the declared 2020–2024 C/D/E scope.",
        "- Problem directory naming is inconsistent across years (`2020年C题`, `C`, `C题`, and flat files). Inventory normalization handles this without renaming sources.",
        "",
        "## Interpretation limits",
        "",
        "- Presence means at least one file was assigned to a problem-year; completeness against an authoritative release manifest is not proven.",
        "- Exact-duplicate detection does not identify near-duplicates or equivalent documents saved in different formats.",
        "- `statement_or_supplement` is a filename-based role, not a claim about document contents.",
        "- 2025 A–F are inventory-only blind-test records and must remain excluded from analysis.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    INDEX.mkdir(parents=True, exist_ok=True)
    problem_rows, paper_rows = build()
    write_csv(INDEX / "problems_inventory.csv", problem_rows)
    write_csv(INDEX / "excellent_papers_inventory.csv", paper_rows)
    (INDEX / "corpus_audit.md").write_text(render_audit(problem_rows, paper_rows), encoding="utf-8")
    print(f"Wrote {len(problem_rows)} problem files and {len(paper_rows)} paper files to {INDEX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
