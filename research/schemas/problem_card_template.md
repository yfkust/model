---
schema_version: "1.1"
card_type: problem_card
problem_id: "YYYY-X"
year: YYYY
problem_letter: "X"
analysis_status: draft
source_paths: []
excellent_papers_accessed: false
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
---

# Problem Card: YYYY-X

## 1. Source Boundary

### Accessed

| source_path | purpose | access_scope |
|---|---|---|
|  |  |  |

### Not Accessed

- Excellent papers: not accessed.
- Other excluded material:

## 2. Problem Restatement

Restate the real mathematical task, required decisions or estimates, and deliverables without copying the prompt.

## 3. Task Decomposition

| subproblem_id | original_requirement | input | required_output | mathematical_object | dependency | success_criterion |
|---|---|---|---|---|---|---|
| Q1 |  |  |  |  |  |  |

## 4. Dependency Graph

`Q1 -> Q2`

State which outputs become later inputs and which subproblems are independent.

## 5. Data Audit

| source_path | data_type | shape | variables | target | missing | anomalies | temporal_spatial_structure | labels | leakage_risk | quality_issues |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |

## 6. Mathematical Abstraction

| subproblem_id | real_problem | mathematical_object | decision_variables | objective | constraints | quantities_to_estimate |
|---|---|---|---|---|---|---|
| Q1 |  |  |  |  |  |  |

## 7. Provisional Modeling Assumptions

Record only provisional assumptions made before modeling and validation. These are working hypotheses, not source facts or established conclusions.

| assumption_id | subproblem | assumption | why_needed | evidence_basis | testable | risk_if_false | verification |
|---|---|---|---|---|---|---|---|
| A1 | Q1 |  |  |  | yes/no |  |  |

## 8. Problem Archetype

Use one or more controlled labels per subproblem:

`classification`, `regression`, `forecasting`, `time_series`, `anomaly_detection`, `clustering`, `feature_selection`, `ranking`, `evaluation`, `causal_analysis`, `mechanism_modeling`, `simulation`, `scheduling`, `routing`, `resource_allocation`, `continuous_optimization`, `combinatorial_optimization`, `multiobjective_optimization`, `signal_processing`, `image_processing`, `spatial_modeling`, `graph_modeling`, `control`, `inverse_problem`.

| subproblem_id | archetypes | justification |
|---|---|---|
| Q1 |  |  |

Do not introduce a new label in a card; propose vocabulary changes separately.

## 9. Candidate Methods

Include a baseline, main candidate, and alternative candidate for each subproblem.

| subproblem_id | method_family | method | role | why_applicable | assumption_ids | data_requirements | strength | weakness | implementation_cost | interpretability | validation_method | risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 |  |  | baseline |  |  |  |  |  |  |  |  |  |
| Q1 |  |  | main |  |  |  |  |  |  |  |  |  |
| Q1 |  |  | alternative |  |  |  |  |  |  |  |  |  |

Use a concise provisional `method_family`; do not create a complete vocabulary before the pilot.

## 10. Recommended Modeling Route

Explain the selected route, rejected alternatives, competition-time feasibility, and interfaces between methods.

`task -> data -> model -> validation -> result -> conclusion`

## 11. Validation Plan

Select only applicable checks.

| subproblem_id | check | design | metric_or_criterion | leakage_control | pass_condition |
|---|---|---|---|---|---|
| Q1 |  |  |  |  |  |

Candidate checks: train/test split, cross-validation, backtesting, baseline comparison, ablation, residual diagnostics, constraint feasibility, sensitivity analysis, robustness analysis.

## 12. Expected Figures and Tables

| artifact_id | type | content | necessity | supported_claim |
|---|---|---|---|---|
|  |  |  |  |  |

## 13. Implementation Plan

| order | stage | inputs | action | output | verification | time_budget |
|---:|---|---|---|---|---|---|
| 1 | data inspection |  |  |  |  |  |
| 2 | preprocessing |  |  |  |  |  |
| 3 | baseline |  |  |  |  |  |
| 4 | main model |  |  |  |  |  |
| 5 | validation |  |  |  |  |  |
| 6 | visualization |  |  |  |  |  |
| 7 | final pipeline |  |  |  |  |  |

## 14. Competition Risk

| risk_id | severity | description | trigger | impact | mitigation |
|---|---|---|---|---|---|
| R1 | fatal/high/medium/low |  |  |  |  |

## 15. Open Questions

| question_id | question | why_unresolved | evidence_needed | consequence |
|---|---|---|---|---|
| OQ1 |  |  |  |  |

## 16. Claims and Evidence

Follow `research/schemas/claim_schema.md`. Repeat `claim_id` for multiple evidence sources.

| claim_id | claim_type | claim | source_path | page_or_section | problem_id | paper_id | evidence_note |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | NA |  |
