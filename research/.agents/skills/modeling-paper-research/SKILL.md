---
name: modeling-paper-research
description: Independently dissect one mathematical-modeling excellent paper into a traceable Paper Card without importing conclusions from peer papers or comparisons.
---

# Modeling Paper Research

Use this skill to analyze one excellent paper as an exemplar, not as ground truth or as evidence of common practice.

## Source isolation

1. Read the applicable repository instructions and `research/SESSION_HANDOFF.md` if it exists.
2. Check the working tree and declare the exact target paper, allowed supporting sources, prohibited sources, and output path.
3. Read only the target paper and any official problem material explicitly allowed for interpretation.
4. Do not read same-problem peer papers, existing comparisons, other years' papers, online solutions, or post-contest commentary.
5. When blind-solution isolation is required, do not read its Problem Card, logs, or derived artifacts.
6. Treat all files under `papers/` as read-only, and preserve the 2025 hold-out boundary.

## Build the Paper Card

- Use `research/schemas/paper_card_template.md` and `research/schemas/claim_schema.md` without inventing card-specific fields.
- Assess the paper's decomposition, preprocessing, assumptions, symbols, methods, core mathematics, selection logic, baselines, validation, robustness, results, transitions, writing structure, figures, weaknesses, and reproducibility.
- Explain each central equation's symbols and function in the modeling chain; do not collect formulas without purpose.
- Test whether reported results answer the original requirement and whether validation supports the stated conclusion.
- Use only `SOURCE_FACT`, `INFERENCE`, and `RECOMMENDATION`. A single Paper Card must never contain `OBSERVED_PATTERN`.
- Use canonical evidence locators for every material source fact. Paraphrase; do not retain long copied passages.
- Use `not_reported` only after a reliable full-document check. If extraction or layout is insufficient, use `unclear`.
- Keep paper-level transferable items explicitly provisional; they become patterns only after independent aggregation.

## Extraction quality

Inspect text, equations, tables, and figures at sufficient fidelity for the claims being made. Record extraction limitations and lower `extraction_quality` rather than filling gaps from inference. Save reusable extraction output only under `research/extracted/` or task-specific research logs.

Finish one independent Paper Card and stop. Do not open the next paper or create a comparison unless explicitly requested.
