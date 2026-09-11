---
schema_version: "1.1"
card_type: problem_comparison
problem_id: "YYYY-X"
year: YYYY
problem_letter: "X"
blind_card_path: ""
paper_card_paths: []
papers_assessed: 0
comparison_status: draft
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
---

# Problem Comparison: YYYY-X

> Excellent papers are reference exemplars, not ground truth. Agreement with an excellent paper is not automatically evidence that the blind solution is correct. Divergence is not automatically an error.

Apply prevalence labels from `research/schemas/claim_schema.md`. Report every count as `n/N assessed papers`. `prevalence != quality`; assess methodological quality separately. Any cross-card claim citation must use a complete `claim_ref`, not a bare `claim_id`.

For evidence absence, use only `present`, `not_reported`, `unclear`, or `not_applicable`. `assessed_N` includes `present` and reliably established `not_reported` cases; exclude and report `unclear` and `not_applicable` cases.

## 1. Blind Analysis Recap

| subproblem | blind_route | assumptions | validation | main_risk |
|---|---|---|---|---|
| Q1 |  |  |  |  |

## 2. Paper Set

| paper_id | paper_card_path | award_group | extraction_quality | included | exclusion_reason |
|---|---|---|---|---|---|
|  |  |  |  | yes/no |  |

## 3. Method-by-Question Matrix

| subproblem | method_family | approach | blind_card | supporting_paper_ids | support_n | assessed_N | prevalence_label | selection_logic | quality_note |
|---|---|---|---|---|---:|---:|---|---|---|
| Q1 |  |  | yes/no |  |  |  | common_pattern/minority_pattern/paper_specific_choice |  |  |

## 4. Assumption Matrix

| subproblem | assumption | blind_card | supporting_paper_ids | supporting_claim_refs | support_n | assessed_N | prevalence_label | reasonableness | risk_if_false |
|---|---|---|---|---|---:|---:|---|---|---|
| Q1 |  | yes/no |  |  |  |  | common_pattern/minority_pattern/paper_specific_choice |  |  |

## 5. Preprocessing Matrix

| operation | blind_card | supporting_paper_ids | support_n | assessed_N | prevalence_label | purpose | caveat |
|---|---|---|---:|---:|---|---|---|
|  | yes/no |  |  |  |  |  |  |

## 6. Validation Matrix

| validation | blind_card | supporting_paper_ids | support_n | assessed_N | prevalence_label | adequacy |
|---|---|---|---:|---:|---|---|
|  | yes/no |  |  |  |  |  |

## 7. Sensitivity/Robustness Matrix

| check | blind_card | supporting_paper_ids | support_n | assessed_N | prevalence_label | conclusion_supported |
|---|---|---|---:|---:|---|---|
|  | yes/no |  |  |  |  |  |

## 8. Figure/Table Matrix

| function | artifact_type | blind_card | supporting_paper_ids | support_n | assessed_N | prevalence_label |
|---|---|---|---|---:|---:|---|
|  |  | yes/no |  |  |  |  |

## 9. Writing Structure Matrix

| rhetorical_function | structure_pattern | supporting_paper_ids | support_n | assessed_N | prevalence_label | effectiveness |
|---|---|---|---:|---:|---|---|
|  |  |  |  |  |  |  |

## 10. Consensus Patterns

Only include `common_pattern` rows.

| pattern | supporting_paper_ids | support_n | assessed_N | evidence_summary | quality_assessment |
|---|---|---:|---:|---|---|
|  |  |  |  |  |  |

## 11. Minority Approaches

Only include `minority_pattern` rows.

| approach | supporting_paper_ids | support_n | assessed_N | potential_value | limitation |
|---|---|---:|---:|---|---|
|  |  |  |  |  |  |

## 12. Paper-Specific Choices

| choice | paper_id | problem_dependency | why_not_general |
|---|---|---|---|
|  |  |  |  |

## 13. Blind Analysis Hits

| blind_choice | matched_claim_refs | paper_ids | significance |
|---|---|---|---|
|  |  |  |  |

## 14. Blind Analysis Gaps / Divergences

| element | paper_ids | assessment | consequence | should_have_been_inferred | supporting_claim_refs |
|---|---|---|---|---|---|
|  |  | true_gap/defensible_alternative/paper_specific_difference/unclear |  | yes/no/unclear |  |

## 15. Unexpected Excellent-Paper Ideas

| idea | paper_ids | value | supporting_claim_refs |
|---|---|---|---|
|  |  |  |  |

## 16. Why We Missed Them

| missed_idea | cause | evidence_available_during_blind_stage | preventable | corrective_rule |
|---|---|---|---|---|
|  |  |  | yes/no/partial |  |

## 17. Transferable Lessons

| lesson | evidence_class | applicable_scope | limitation | supporting_claim_refs |
|---|---|---|---|---|
|  | common_pattern/minority_pattern/inference |  |  |  |

## 18. Non-transferable Lessons

| lesson | dependency | failure_outside_scope | supporting_paper_ids |
|---|---|---|---|
|  |  |  |  |

## Claims and Evidence

Follow `research/schemas/claim_schema.md`. Cross-paper patterns require repeated rows with distinct `paper_id` values.

| claim_id | claim_type | claim | source_path | page_or_section | problem_id | paper_id | evidence_note |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
