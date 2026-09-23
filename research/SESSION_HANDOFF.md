# Modeling Research Session Handoff

## 1. Project Goal

使用 2020–2024 C/D/E 真题与优秀论文研究中国研究生数学建模竞赛的题目结构、解题思路、方法选择、验证方式和论文写作模式；将稳定的跨题结论沉淀到 `research/synthesis/`，最终形成可复用 Codex Skills，并用于 `contest-2026/`。2025 A–F 保留为 hold-out blind evaluation。

## 2. Current Phase

已完成：

- Phase 0：corpus inventory / audit。
- Phase 1：Research Schema v1.1。
- Phase 2/3：2024-C blind problem analysis、pre-freeze audit 与冻结。
- Phase 4：四篇 2024-C 优秀论文的独立 Paper Card。
- Phase 5：2024-C problem-year comparison。

四篇 Paper Card 均在相互隔离且不读取 Blind Card 的条件下生成；之后才读取 frozen Blind Card 与四张 Paper Card 完成同题聚合。当前尚未开始跨 problem-year synthesis，也未选择下一道历史题。

## 3. Frozen and Completed Artifacts

Frozen blind artifacts：

- `research/problem_cards/2024/2024-C.md`
- `research/logs/2024-C/inspection.py`
- `research/logs/2024-C/inspection_summary.md`

`freeze_commit: fd21d41a4e869c79fdaba28252a4d6bcfa405390`  
`freeze_commit_message: freeze blind analysis for 2024-C`

当前 HEAD 下三项 frozen artifact 与 freeze commit 一致。不得因优秀论文结果回改其核心判断；差异已记录在 `research/comparisons/2024-C.md` 的 `Blind Analysis Gaps / Divergences`。

Completed derived artifacts：

- `research/paper_cards/2024/C/C24102890089.md`
- `research/paper_cards/2024/C/C24103860012.md`
- `research/paper_cards/2024/C/C24104220149.md`
- `research/paper_cards/2024/C/C24106130096.md`
- `research/comparisons/2024-C.md`

上述五个文件当前尚未提交，不能把它们误认为已有 freeze commit。

## 4. Schema State

`schema_version: 1.1`

- `research/schemas/claim_schema.md`
- `research/schemas/problem_card_template.md`
- `research/schemas/paper_card_template.md`
- `research/schemas/problem_comparison_template.md`

当前 schema 已支持本轮 Paper Card 与 comparison pilot。暂不增加字段；只有新的真实 pilot 暴露明确问题时才做最小修订。

## 5. 2024-C Research Summary

Blind route：

- Q1：波形分类 / signal-feature classification。
- Q2：Steinmetz 温度修正 / mechanism-informed regression。
- Q3：控制 frequency 与 B_peak 后分析因素及交互。
- Q4：统一磁芯损耗预测。
- Q5：基于 Q4 surrogate 的经验域内 Pareto 优化。

```text
Q1 ─┐
Q2 ─┼─> Q4 -> Q5
Q3 ─┘
```

同题 comparison 的压缩结论：

- 4/4 论文在 Q1 使用人工信号特征与传统分类器；3/4 还使用投票或 stacking，但没有可靠证明融合优于最强单模型。
- 4/4 从 Steinmetz 幂律构造温度修正；具体温度函数没有共识，验证普遍不足以排序其泛化质量。
- 4/4 的 Q3 均未同时充分控制 `frequency × B_peak`；这是共同缺陷，不是可迁移惯例。
- 3/4 的 Q4 保留 Steinmetz 派生结构或机理特征；复杂模型收益普遍受 split、selection 或实现不一致影响。
- 4/4 的 Q5 使用标量化或群智能/数值优化，但可行性、Pareto 性、接口闭合与随机稳定性证据不足。

这些只是 `2024-C` 单一 problem-year 的内部聚合，不能升级为“华为杯通常如此”的跨题规律。

## 6. Data Inspection State

`research/logs/2024-C/inspection.py` 可复现：

- 四材料样本数、缺失与波形类别统计；
- 材料 3 完全重复记录；
- frequency / loss / B_peak 范围；
- THD 与 peak-to-RMS 初步统计；
- 附件二、附件三 shape；
- 训练/测试精确波形交集；
- 附件三 9 个单变量边界样本。

这 9 个样本仅按对应材料—温度—波形单元的 frequency 或 B_peak 训练 min/max 判定，不是联合分布 OOD。

## 7. Information Boundaries

- `papers/problems/2025/` 仍是 hold-out；知识库训练完成且用户明确启动前禁止读取正文。
- `papers/problems/` 与 `papers/excellent_papers/` 均为只读原始语料，不得移动、重命名或修改。
- 2024-C Blind Card 已冻结；后续只允许因明确事实/记录错误做带说明的最小修正。
- 2024-C comparison 只能作为一个 problem-year 的结论，不能直接写入跨题 synthesis。

## 8. Next Exact Action

先由用户确认是否冻结并提交当前 2024-C research package。不要自动提交。

之后选择下一个 2020–2024 C/D/E problem-year，并重新执行：

`problem-only blind analysis -> freeze -> independent paper cards -> problem comparison`

在用户指定下一题前，不自动读取新的赛题或论文。至少再完成一个独立 problem-year 后，才具备开始最小 cross-problem synthesis 的条件。

## 9. What Must NOT Happen Next

- 不修改 frozen 2024-C Blind Card 来提高“命中率”。
- 不把 2024-C 单题统计写成跨年份规律。
- 不直接批量读取下一题全部优秀论文。
- 不分析 2025 正文。
- 不创建大规模 method vocabulary 或新的 schema 框架。
- 不修改 `contest-2026/`。
- 不自动提交当前工作区。

## 10. Resume Checklist

1. 阅读根目录 `AGENTS.md`。
2. 阅读本文件。
3. 检查 `git status --short` 与最近 commits。
4. 验证 frozen 2024-C blind artifacts 未改变。
5. 验证四张 Paper Card 与 `research/comparisons/2024-C.md` 仍存在。
6. 汇报恢复到“2024-C problem-year package completed, awaiting freeze/next problem selection”。
7. 等待用户决定提交/冻结或指定下一题，不自动推进。

## 11. Repository State

- Git branch: `main`
- HEAD: `16da704ca780dcae88919cfab8d5bc12f01d390e`

最近相关 commits：

1. `16da704` — `2025`
2. `3a9e0c2` — `configure Git LFS`
3. `d11bea9` — `model`
4. `6aa87cf` — `record modeling research handoff before phase 4`
5. `cd1dc44` — `add repository research instructions`

与本轮研究直接相关的未提交路径：

```text
?? research/paper_cards/
?? research/comparisons/
 M research/SESSION_HANDOFF.md
```

`research/.agents/` 也为未跟踪目录，但并非本轮 comparison 生成。工作区同时存在大量 `papers/` 与 `reference_tool/` 下的已修改条目；它们是本阶段开始前已有状态，本轮未修改。四个 2024-C 源 PDF 当前也显示为 modified，须继续视为只读且不得纳入本阶段提交，除非用户另行确认其 Git LFS 状态。
