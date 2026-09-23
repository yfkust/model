---
name: modeling-solution-review
description: Audit a mathematical-modeling solution, card, or manuscript for task fit, mathematical validity, leakage, validation, reproducibility, and contest feasibility without treating complexity or exemplars as correctness.
---

# Modeling Solution Review

Use this skill for an evidence-based review of an existing modeling plan, implementation, result set, Problem Card, Paper Card, comparison, or manuscript.

## Review boundary

- Identify the artifact under review, its declared evidence sources, and the requested review scope.
- Review read-only unless the user explicitly requests fixes.
- Respect blind-analysis isolation, frozen artifacts, source restrictions, and the 2025 hold-out rule.
- Do not open additional papers, comparisons, or external solutions merely to benchmark the artifact.

## Review criteria

Trace the complete chain from each original requirement to its output and conclusion. Check:

- task decomposition, dependencies, mathematical abstraction, assumptions, objectives, and constraints;
- data quality, duplicates, splits, and duplicate/group/time/target/preprocessing/test leakage;
- method-to-data fit, baseline quality, parameter and solver disclosure, and avoidable complexity;
- validation design, metric alignment, fold locality, error analysis, sensitivity, robustness, feasibility, and uncertainty where relevant;
- whether results answer the question, support the claims, remain within the evidence domain, and avoid causal overstatement;
- interfaces between subproblems, reproducibility, competition-time implementability, and writing or visualization gaps.

For research cards, enforce `research/schemas/claim_schema.md`, including permitted claim types, canonical evidence locators, absence states, and full cross-card `claim_ref` values. For comparisons, verify within-problem-year aggregation and remember that prevalence is not quality.

## Report findings

Lead with actionable findings ordered by severity. For each finding, identify the artifact location, concrete failure mode, consequence, and smallest credible correction. Separate confirmed defects from uncertainties and optional improvements.

Do not rewrite a frozen Blind Card because later papers differ. Put such differences in the future comparison as Blind Analysis Gaps / Divergences. If no material issue is found, say so and name the remaining validation limits.
