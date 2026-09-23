---
name: modeling-problem-analysis
description: Create a blind mathematical-modeling Problem Card from an official problem and its attachments, with traceable evidence, data inspection, validation design, and no excellent-paper contamination.
---

# Modeling Problem Analysis

Use this skill for a problem-only, competition-day analysis that must precede excellent-paper research.

## Before analysis

1. Read the applicable repository instructions and `research/SESSION_HANDOFF.md` if it exists.
2. Check the working tree and the target artifact's current state.
3. Declare the allowed sources, prohibited sources, and intended output before reading problem content.
4. Treat `papers/problems/` as read-only. Never read `papers/problems/2025/` unless the user explicitly starts the 2025 blind evaluation.
5. Do not access excellent papers, paper cards, comparisons, online solutions, or post-contest analyses for the target problem.

## Produce the analysis

- Use `research/schemas/problem_card_template.md` and `research/schemas/claim_schema.md` as the authoritative formats.
- Set `excellent_papers_accessed: false`. Stop and report contamination if that statement cannot truthfully be made.
- Establish the Source Boundary before modeling.
- Work in this order: task decomposition, dependency graph, data audit, mathematical abstraction, provisional assumptions, archetypes, candidate methods, recommended route, validation, implementation, and risks.
- Start from mathematical objects and success criteria, not algorithm names.
- Give every subproblem a justified baseline, main candidate, and alternative. Treat `method_family` as provisional; do not create a method ontology.
- Distinguish `SOURCE_FACT`, `INFERENCE`, and `RECOMMENDATION`; `OBSERVED_PATTERN` is forbidden in a Problem Card.
- Use canonical evidence locators and repository-relative paths. Do not present computed statistics without a reproducible route to obtain them.
- Keep inspection scripts and summaries under `research/logs/<problem-id>/`; do not train a final model unless separately requested.
- Design validation that matches the data structure and prevents duplicate, group, time, target, preprocessing, and test-set leakage.

## Finish

Verify every question has a mathematical abstraction, justified candidates, validation, and a usable interface to dependent questions. Report unresolved assumptions and risks rather than hiding them.

Do not freeze, commit, or proceed to excellent-paper analysis unless the user explicitly requests that action.
