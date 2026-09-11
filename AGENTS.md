# Modeling Repository Instructions

## 1. Repository Purpose

This repository supports:

- historical problem research for the China Graduate Mathematical Contest in Modeling;
- study of modeling methods and writing structure in excellent papers;
- synthesis of modeling methodology, validation patterns, and research-writing principles;
- later construction of reusable Codex Skills;
- live contest work under `contest-2026/`.

The long-term pipeline is:

`historical evidence -> structured research -> synthesis -> reusable skills -> contest application`

The goal is not to collect algorithm templates or reusable paper phrasing without evidence.

## 2. Repository Boundaries

### `papers/problems/`

Historical problems and official attachments are read-only source material by default. Do not rename, move, or modify them. Never write derived research into this directory.

### `papers/excellent_papers/`

Historical excellent papers are read-only evidence sources by default. Do not modify them, and do not treat them automatically as ground truth.

### `papers/index/`

Store only corpus metadata, inventories, audits, and file indexes. Do not store problem cards, paper cards, comparisons, or synthesis here.

### `research/`

Store all derived historical-research artifacts here, including schemas, problem cards, paper cards, comparisons, synthesis, evaluation, logs, extracted material, and session handoff.

### `reference_tool/`

Contains user-maintained modeling experience, writing guidance, submission procedures, prompts, and other curated material. Do not overwrite or broadly restructure it without explicit instruction.

### `contest-2026/`

Reserved for the future live contest project and kept separate from historical research. Do not place large volumes of historical-research temporary files here.

## 3. 2025 Hold-out Rule

`papers/problems/2025/` is the hold-out blind-evaluation set for after knowledge-base construction.

During historical knowledge-base construction, do not read the content of any 2025 A–F problem. Corpus inventory may record non-semantic metadata such as filename, path, size, hash, and file format. Content access is allowed only when the user explicitly begins the 2025 blind-evaluation stage. This is a high-priority boundary.

## 4. Blind Analysis Discipline

For a historical problem, prefer:

`problem-only blind analysis -> freeze -> excellent-paper analysis -> comparison`

Do not read that problem's excellent papers during blind analysis. After a Blind Card is frozen, do not rewrite its core judgment merely because excellent papers use different methods. Record later differences under `Blind Analysis Gaps / Divergences`.

Only clear factual errors, damaged files, or obvious recording mistakes justify a minimal correction to a frozen artifact. Record the reason for such a correction.

## 5. Excellent Paper Isolation

Analyze each excellent paper independently in its own Paper Card. During a single-paper analysis, do not read same-problem peer papers or an existing problem comparison merely for convenience.

If the task requires isolation from the blind solution, do not read the Blind Card. Compare papers only after their independent Paper Cards are complete. Never read all papers first and jump directly to a claim about common practice.

## 6. Evidence and Claim Discipline

All formal research claims must follow `research/schemas/claim_schema.md`. Use only the permitted claim types:

- `SOURCE_FACT`
- `OBSERVED_PATTERN`
- `INFERENCE`
- `RECOMMENDATION`

Keep source facts, analyst inference, cross-source patterns, and practice recommendations distinct. Never state inference as fact.

Do not generalize one paper into claims such as “excellent papers usually,” “the contest generally,” or “a common method is.” Such language requires adequate independent cross-source evidence.

Key claims should record `source_path`, `page_or_section`, `problem_id`, `paper_id`, and `evidence_note` whenever applicable.

## 7. Aggregation Rule

Paper counts differ across problem-years. Aggregate in this order:

`paper evidence -> within-problem-year aggregate -> problem-year conclusion -> cross-problem synthesis`

Do not vote directly over all paper rows. A problem-year with ten collected papers must not receive greater weight merely because another has four.

For cross-problem patterns, prefer `n/N problem-years` over `n/N papers` unless the research question explicitly requires paper-level weighting.

## 8. Excellent Papers Are Exemplars, Not Ground Truth

Critically inspect:

- mathematical validity and model-selection logic;
- leakage, validation, and baselines;
- robustness and sensitivity;
- interpretability and reproducibility;
- whether results actually answer the problem.

Agreement with an excellent paper does not establish correctness. Divergence does not establish error. Complexity, novelty, or sophistication does not establish higher modeling quality.

## 9. Modeling Reasoning Order

For a new problem, reason in this order:

`problem requirement -> task decomposition -> data structure -> mathematical abstraction -> assumptions -> candidate methods -> validation -> implementation -> results -> interpretation`

Do not begin with algorithm names or list unsupported combinations such as “Q1 XGBoost, Q2 LSTM, Q3 genetic algorithm” without explaining the mathematical task and data fit.

## 10. Validation-First Rule

Every formal modeling route must include appropriate validation. Select only what the task needs, such as:

- baseline;
- train/test split, grouped CV, cross-validation, or backtesting;
- residual diagnostics and error analysis;
- ablation;
- sensitivity and robustness analysis;
- feasibility checks and uncertainty analysis.

Do not apply every method mechanically. Increased complexity requires measurable, validated benefit, not prestige.

## 11. Data Leakage Rule

Actively check duplicate, group, time, target, preprocessing, and test-set leakage.

When a train/validation split exists, fit scaling, feature selection, imputation, target encoding, and model selection within the training fold whenever applicable. Test data must not influence training choices.

## 12. Competition Feasibility

Evaluate methods by theoretical suitability and by:

- implementation cost;
- tuning time;
- stability;
- interpretability;
- reproducibility;
- writing cost;
- feasibility within the contest schedule.

A simple, well-validated method may be superior to a complex, unstable one.

## 13. Writing Research Rule

Do not build a library of sophisticated sentences from excellent papers. Extract rhetorical function, argument structure, section role, transition logic, result-discussion pattern, and figure/table function.

Prefer structures such as:

`problem feature -> modeling difficulty -> abstraction -> method choice`

Do not retain long copied passages unless explicitly necessary and legally permissible.

## 14. Figures and Tables

Every figure or table must support an argument. Ask:

- What does it show?
- Which claim does it support?
- Is there a more compact representation?
- Does it duplicate another artifact?

Do not add decorative figures merely to make a paper look substantial.

## 15. Reproducibility

When important statistics or judgments are computed programmatically, preserve a minimal reproducible script when practical. Scripts should use stable paths, fix random seeds when applicable, define key statistics, and avoid hidden manual steps.

Understanding a paper's idea is not equivalent to reproducing its result.

## 16. Code Modification Rules

Make surgical changes:

- understand the relevant flow and callers first;
- modify only task-related files;
- preserve project style;
- do not delete or refactor unrelated code;
- verify changes and provide the verification command.

Reuse or minimally extend an existing equivalent tool before creating another one.

## 17. Research Schema Discipline

Use the formal schemas under `research/schemas/`. Do not invent many card-specific fields.

When a real pilot exposes a schema problem, record it first and make the smallest justified schema revision. Do not expand schemas for speculative future needs.

## 18. Method Vocabulary Discipline

Do not create a large modeling-method ontology prematurely. Derive method categories incrementally from the historical corpus.

Keep problem archetypes separate from specific algorithms. For example, `regression` is not XGBoost, and `multiobjective_optimization` is not NSGA-II.

## 19. Research vs Contest Separation

Historical research prioritizes method understanding, evidence, pattern extraction, and reproducibility. Live contest work prioritizes current-problem fit, implementability, a complete modeling chain, stable results, and paper delivery.

Historical conclusions are priors only. When they conflict with current-problem evidence, follow the current evidence.

## 20. Session Continuity

Store dynamic progress in `research/SESSION_HANDOFF.md`. At the start of a new Codex research session, read it if it exists.

`SESSION_HANDOFF.md` is not durable research evidence and does not replace schemas, cards, comparisons, synthesis, or Git history. If it conflicts with repository files or Git state, trust the current repository state and report the inconsistency.

Do not put transient session status in this file.

## 21. Before Major Research Work

Before a substantial research step:

1. Read applicable `AGENTS.md` files.
2. Read `research/SESSION_HANDOFF.md` if present.
3. Check the Git working tree.
4. Declare allowed and prohibited sources.
5. Declare expected output files.
6. Stay within the current stage boundary.

## 22. Stop Conditions

If the user says “stop after completion,” “only do this stage,” or otherwise limits the scope, stop when that stage is complete. Do not automatically continue to papers, model training, comparisons, or synthesis because the next step appears obvious.
