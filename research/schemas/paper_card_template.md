---
schema_version: "1.1"
card_type: paper_card
paper_id: ""
problem_id: "YYYY-X"
year: YYYY
problem_letter: "X"
award_group: ""
source_path: ""
analysis_status: draft
extraction_quality: unknown
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
---

# Paper Card: PAPER_ID

`analysis_status`: `draft | reviewed | complete`.  
`extraction_quality`: `high | medium | low | unknown`; explain limitations below.

Evidence-absence status follows `research/schemas/claim_schema.md`. Use `not_reported` only after a reliable full-document check; otherwise use `unclear`.

## 1. Paper Structure

| section | pages | approximate_share | function |
|---|---|---:|---|
|  |  |  |  |

## 2. Abstract Anatomy

| component | paraphrased_content | evidence_status | quantitative | page_or_section |
|---|---|---|---|---|
| background |  | present/not_reported/unclear/not_applicable | NA |  |
| problem |  |  | NA |  |
| method |  |  | NA |  |
| result |  |  | yes/no |  |
| quantitative_result |  |  | yes/no |  |
| conclusion |  |  | NA |  |

Assessment of whether the abstract reports meaningful quantitative results:

## 3. Problem Decomposition

| subproblem | author's_interpretation | mathematical_task | dependency | output |
|---|---|---|---|---|
| Q1 |  |  |  |  |

## 4. Data Processing

| subproblem | operation | target_data | rationale | parameters_or_rule | leakage_risk | page_or_section |
|---|---|---|---|---|---|---|
|  | missing/anomaly/standardization/fusion/feature_engineering/dimensionality_reduction/labeling/split |  |  |  |  |  |

## 5. Assumptions

| assumption_id | subproblem | assumption | difficulty_addressed | evidence_basis | reasonableness | result_impact | tested | page_or_section |
|---|---|---|---|---|---|---|---|---|
| A1 | Q1 |  |  |  |  |  | yes/no |  |

## 6. Symbols

| symbol | definition | unit_or_domain | first_location | consistent | issue |
|---|---|---|---|---|---|
|  |  |  |  | yes/no |  |

List undefined or overloaded symbols explicitly.

## 7. Method-by-Question Matrix

| subproblem | method_family | model | objective | input | output | why_selected | assumption_ids | parameters | solver |
|---|---|---|---|---|---|---|---|---|---|
| Q1 |  |  |  |  |  |  |  |  |  |

Use a concise provisional `method_family`; do not create a complete vocabulary before the pilot.

## 8. Core Mathematics

| equation_id | equation | symbol_meaning | role_in_model | assumptions | page_or_section |
|---|---|---|---|---|---|
| EQ1 |  |  |  |  |  |

Record only equations central to the modeling chain and explain their use.

## 9. Model Selection Logic

| subproblem | stated_reason | evidence_or_property | logic_strength | critique |
|---|---|---|---|---|
| Q1 |  |  | supported/partial/asserted |  |

## 10. Baselines and Comparisons

| subproblem | baseline_or_competitor | comparison_metric | protocol | fair | conclusion |
|---|---|---|---|---|---|
|  |  |  |  | yes/no/unclear |  |

## 11. Validation

| subproblem | validation_type | split_or_design | metric | result | supports_claim | limitation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 12. Sensitivity / Robustness

| target | evidence_status | perturbation_or_range | measured_effect | result | conclusion_supported | limitation |
|---|---|---|---|---|---|---|
|  | present/not_reported/unclear/not_applicable |  |  |  | yes/no/partial |  |

State explicitly when absent.

## 13. Results

| subproblem | result | quantitative_value | unit | answers_requirement | page_or_section |
|---|---|---|---|---|---|
| Q1 |  |  |  | yes/no/partial |  |

## 14. Result Discussion Logic

| result_id | result | comparison | interpretation | mechanism_or_explanation | implication | missing_link |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 15. Figures and Tables

| artifact_id | type | purpose | information_density | redundant | supported_claim | page_or_section |
|---|---|---|---|---|---|---|
|  |  |  | low/medium/high | yes/no |  |  |

## 16. Question Transitions

| from | to | transferred_output | transition_logic | gap |
|---|---|---|---|---|
| Q1 | Q2 |  |  |  |

## 17. Writing Patterns

Record function and logic only; do not copy extended wording.

| location | rhetorical_function | structure_pattern | effectiveness | page_or_section |
|---|---|---|---|---|
|  |  | problem feature -> difficulty -> abstraction -> method choice |  |  |

## 18. Strengths

| dimension | specific_strength | supporting_evidence | scope |
|---|---|---|---|
| modeling/validation/interpretability/writing/visualization |  |  |  |

## 19. Weaknesses

| dimension | specific_weakness | consequence | supporting_evidence | feasible_improvement |
|---|---|---|---|---|
|  |  |  |  |  |

## 20. Reproducibility Assessment

| dimension | status | available_information | missing_information | reproduction_impact |
|---|---|---|---|---|
| preprocessing | sufficient/partial/insufficient/unclear/not_applicable |  |  |  |
| parameters |  |  |  |  |
| solver |  |  |  |  |
| software |  |  |  |  |
| randomization |  |  |  |  |
| evaluation |  |  |  |  |

`reproducibility_level: high / medium / low / unclear`

## 21. Transferable Patterns

| pattern | transferable_principle | applicable_when | limitation | page_or_section |
|---|---|---|---|---|
|  |  |  |  |  |

These are paper-level candidates, not cross-paper `OBSERVED_PATTERN` conclusions.

## 22. Paper-Specific Choices

| choice | problem_dependency | why_not_general | page_or_section |
|---|---|---|---|
|  |  |  |  |

## 23. Claims and Evidence

Follow `research/schemas/claim_schema.md`. Repeat `claim_id` for multiple evidence sources.

| claim_id | claim_type | claim | source_path | page_or_section | problem_id | paper_id | evidence_note |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
