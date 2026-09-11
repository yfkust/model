# Claim and Evidence Schema

Schema version: `1.1`

## Claim types

| value | meaning | minimum support |
|---|---|---|
| `SOURCE_FACT` | A fact directly stated by or mechanically observed in a source | One precise source location |
| `OBSERVED_PATTERN` | A recurring pattern across independent sources | At least two distinct source IDs; never one paper alone |
| `INFERENCE` | The analyst's interpretation of cited evidence | Evidence plus an explicit reasoning note |
| `RECOMMENDATION` | Advice for competition practice | Evidence or inference plus scope and trade-off |

## Allowed claim types by artifact

| artifact | allowed claim types |
|---|---|
| `problem_card` | `SOURCE_FACT`, `INFERENCE`, `RECOMMENDATION` |
| `paper_card` | `SOURCE_FACT`, `INFERENCE`, `RECOMMENDATION` |
| `problem_comparison` | `SOURCE_FACT`, `OBSERVED_PATTERN`, `INFERENCE`, `RECOMMENDATION` |
| cross-problem synthesis | `OBSERVED_PATTERN`, `INFERENCE`, `RECOMMENDATION` |

A single paper card must never label one paper's practice as `OBSERVED_PATTERN`.

## Canonical identifiers

- `problem_id`: `YYYY-X`, for example `2024-C`.
- `paper_id`: inventory paper ID; use `NA` for problem-only sources.
- `claim_id`: unique within a card, using `CLM-001`, `CLM-002`, and so on.
- `claim_ref`: cross-card identifier in the form `<repository-relative-card-path>#<claim_id>`, for example `research/paper_cards/example.md#CLM-001`.
- `source_path`: repository-relative path, never only a filename.
- `page_or_section`: the canonical evidence locator defined below.

`claim_id` remains local to its card. Any cross-card reference must use `claim_ref`, never a bare `CLM-001`.

## Canonical Evidence Locator

Use these forms wherever the schema requests `page_or_section`:

| source format | locator forms |
|---|---|
| PDF | `pdf_page:<n>`; `pdf_page:<n>; section:<name>` |
| DOC/DOCX | `section:<name>`; `table:<n>`; `figure:<n>` |
| XLS/XLSX | `sheet:<name>`; `sheet:<name>; range:<cell-range>` |
| CSV/TXT | `rows:<start>-<end>`; `rows:<start>-<end>; columns:<names>` |
| image | `file-level`; `region:<description>` |
| metadata | `file-level` |

Use the most precise available form. If a format has no stable page number, prefer its section, table, figure, sheet, range, row, or region locator rather than an informal description.

## Evidence Absence

Use exactly one of these states whenever recording whether evidence is available:

| state | meaning |
|---|---|
| `present` | Relevant evidence was located and can be cited. |
| `not_reported` | A reliable full-document check found that the item was not reported. |
| `unclear` | Extraction quality or source ambiguity prevents a reliable determination. |
| `not_applicable` | The item does not apply to this source or analysis. |

Use `not_reported` only after the full source has been reliably checked. If `extraction_quality` is insufficient, use `unclear`; failure to extract an item is not evidence that it is absent.

## Required ledger

Use one row per claim–evidence pair. Repeat a `claim_id` when a claim has multiple sources.

| claim_id | claim_type | claim | source_path | page_or_section | problem_id | paper_id | evidence_note |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

`evidence_note` states what the cited location supports and, for `INFERENCE` or `RECOMMENDATION`, the reasoning link. It must not merely repeat the claim.

## Independence and aggregation

- For cross-paper claims, independent sources mean distinct `paper_id` values. Multiple pages from one paper remain one source.
- First aggregate repeated evidence within a single `problem_id`.
- Cross-problem synthesis operates on problem-year aggregates, not raw paper rows.
- Report support as `n/N problem-years` and retain the contributing `problem_id` values.
- Unknown or unassessed papers are excluded from the denominator and their count is reported.

Within a problem comparison:

- `common_pattern`: supported by more than half of assessed papers and at least two distinct papers.
- `minority_pattern`: supported by at least two assessed papers but not a majority.
- `paper_specific_choice`: observed in exactly one paper.

These labels describe prevalence, not quality. Method novelty or sophistication is not evidence of modeling quality.

## Validation checks

- Every ledger row has all eight required fields.
- Every `SOURCE_FACT` has a precise locator.
- Every `OBSERVED_PATTERN` has at least two independent sources.
- Every cross-card reference uses a complete `claim_ref`.
- Every evidence-absence assertion uses the controlled absence states.
- Claim wording does not exceed the scope of its evidence.
- Recommendations state applicability, limitations, and trade-offs.
