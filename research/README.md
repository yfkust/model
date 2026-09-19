# Mathematical Modeling Research Workspace

This directory stores research outputs derived from the read-only corpora in `papers/problems/` and `papers/excellent_papers/`. Corpus inventories and audits remain in `papers/index/`.

## Directory contract

| Directory | Purpose |
|---|---|
| `schemas/` | Stable templates and evidence rules |
| `problem_cards/` | Blind, problem-only analyses |
| `paper_cards/` | Structured excellent-paper dissections |
| `comparisons/` | One problem-year compared across its blind card and papers |
| `synthesis/` | Cross-problem-year synthesis after within-group aggregation |
| `evaluation/` | Quality checks and later evaluation artifacts |
| `logs/` | Research-process logs |

Existing directories outside this table are preserved but are not part of the Phase 2 schema.

## Required workflow

1. Create the problem card from the problem statement and attachments only.
2. Freeze that blind analysis before accessing excellent papers.
3. Create one paper card per excellent paper.
4. Create one comparison per problem-year.
5. Aggregate evidence within each problem-year.
6. Only then synthesize across problem-years, giving each problem-year one unit of weight unless a different weighting rule is declared.

The 2025 A–F corpus is reserved for blind testing and must not be read during knowledge-base construction.

## Evidence policy

Use only `SOURCE_FACT`, `OBSERVED_PATTERN`, `INFERENCE`, and `RECOMMENDATION` as claim types. Every material claim must follow [the claim schema](schemas/claim_schema.md). A single paper cannot support a cross-paper `OBSERVED_PATTERN`.

Cards use YAML front matter plus fixed Markdown sections. Keep unknown values explicit as `unknown`; do not silently omit applicable fields or invent evidence.
