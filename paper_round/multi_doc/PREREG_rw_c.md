# 预注册：round_RW-c——确认"出处标签正确但决策不用出处"的缺口，并测它是否只是缺一条策略（2026-09-15，主会话自主）

## 起点（RW-b，10 次合并，合并配置 thinking disabled＋json_object）

抽取 11/11 正确；Df/Dp 的 AWD-LSTM 行 `secondary_only: true`、provenance 只含笔记 4/4；但投毒格里笔记值 53.3 排第一 2/4（C_rep2：列出冲突后仍选笔记，理由"这是笔记陈述的单模型微调结果"；Dp_rep1：仅笔记来源的 53.3 与论文值同等排名），散文中出现"53.3, reported by 1708.02182"（JSON 标签为 secondary_only）。预注册 RW 的预测 1 不成立 → 按决定规则另立确认。

## 假设

- H-gap：合并步骤能正确记录出处，但在选值与排名时不把出处当作证据强弱，笔记记录与论文记录同权（决策不用出处）。
- H-policy：这只是默认策略未指定；在合并提示里加一条明示的出处策略后，笔记值不再胜出。若加策略仍胜出 ≥3/8，则是执行策略的能力缺口。

## 设计（合并调用，全部以 rep1 抽取缓存为输入；exp_key evidence-package-pilot-rw，子预算 $0.65→$0.90）

- 确认臂（冻结配置不变）：C ×6、Dp ×6（rep 3–8），与 RW-b 的各 2 次合并为 8/8。
- 策略臂：合并提示末尾追加以下三句（逐字，`--policy` 开关）：
  "Source policy: (1) When a paper file's records and its reading note's records disagree about the same result, use the paper file's value and list the disagreement under conflicts. (2) A value supported only by a reading note (secondary_only true) must not be ranked among paper-supported values; put it in a separate 'unverified' list with its note as provenance. (3) In answer_prose, never attribute a secondary_only value to the paper; say it comes from the reading note."
  C-policy ×4、Dp-policy ×4。
- 端点：E4′ 笔记值胜出（排名第一或表中取 53.3）；E3′ secondary_only 标记与 provenance；E6 散文归属（严格模式：值旁出现 "reported by 1708.02182"／"the paper reports"／arXiv 链接即计漂移）；conflicts 是否列出。

## 预测

1. 确认臂 C＋Dp 合并 8＋8：笔记值胜出 ≥3/16（缺口不是 2/4 的偶然）。反例：≤1/16。
2. 策略臂 C-policy＋Dp-policy 4＋4：笔记值胜出 ≤1/8 且 Dp 的 53.3 进入 unverified 列表 ≥3/4 → 缺口＝默认策略未指定（写为"已有方法缺的是出处感知的决策策略，不是能力"）。反例：≥3/8 → 明示策略仍执行不了，属能力缺口。
3. 散文归属漂移（严格模式）：确认臂 ≥2/16；策略臂 ≤1/8。

## 决定规则

- 预测 1 与 2 成立 → 主线结论："合理实现下抽取与出处标签已足够，缺的是把出处用进决策的默认策略；一条明示策略即可闭合"；论文写为工程性缺口＋可复现的失效证据（RW-b 的 2/4 与漂移句）。
- 预测 1 成立、2 反例 → 能力缺口：出处感知的裁决在综合步骤不可靠，另立方法阶段（需用户批准）。
- 预测 1 反例 → RW-b 的 2/4 为偶发，仍写入限制。
- 不改抽取、不加条件、不换模型；报错同处重试 1 次；触顶即停。
