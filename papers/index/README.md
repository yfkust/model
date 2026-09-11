# Corpus research index

This directory contains derived metadata only. The source corpora under `papers/problems/` and `papers/excellent_papers/` are read-only.

## Files

- `problems_inventory.csv`: one row per problem or attachment file.
- `excellent_papers_inventory.csv`: one row per excellent-paper file.
- `corpus_audit.md`: coverage, exact duplicates, naming issues, and format checks.
- Regenerate all three with `python scripts/build_paper_index.py`.

## Traceability contract

Every future extracted claim must record at least:

`claim_type, year, problem, paper_id, file_path, page_or_section, claim, evidence_note`

Allowed `claim_type` values:

- `SOURCE_FACT`: directly supported by the cited source location.
- `OBSERVED_PATTERN`: recurs across multiple sources; cite every supporting source.
- `INFERENCE`: an explicitly identified interpretation.
- `RECOMMENDATION`: an explicitly identified competition-practice suggestion.

`year + problem` is the primary aggregation key. Cross-year statistics must first aggregate papers within each problem-year so groups with more collected papers do not receive greater weight merely from paper count.

## Scope guard

The 2025 A–F files are a blind-test set. Their paths and filesystem metadata may appear in the inventory, but their contents must not be read or used during knowledge-base construction.

Inventory roles and anomaly flags are path-based metadata, not conclusions about the documents. The current inventory contains no model assessment, paper analysis, or recommendation.
