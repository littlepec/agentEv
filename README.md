# agent-evidence-integrity-probe

**低可信外部内容被当作"证据"后，错误主张如何进入 LLM 智能体的最终判断——一组固定证据的受控探针实验。**
A small, defensive-security study on how low-credibility external content, once treated as "evidence",
propagates into an LLM agent's final judgment. Fixed-evidence, single-turn probes; no live agent, no deployed attack.

> ⚠ **本仓库含"故意虚构的误导材料"（poison）用于研究，切勿当真。** 见 [`packs/FABRICATED_MATERIALS_NOTICE.md`](packs/FABRICATED_MATERIALS_NOTICE.md)。
> This repo contains **deliberately fabricated misinformation** as study stimuli. Do not cite its "poison" claims as fact.

## 这是什么
围绕 4 个真实研究问题（来自 DeepResearch Bench，query_id 88/89/94/73），把"喂给模型的证据"固定下来，
系统比较不同**证据配置**（正确证据 E / E+毒源 / 仅毒源 / 充分正确证据）与不同**系统提示**（中性 / 审慎 / 校准审慎）
对回答的影响。评分用两个分开的轴：
- **轴 A**：对具体（造假）主张的态度——事实认可 / 归属并保留 / 明确拒绝 / 仅提及 / 未知。
- **轴 B**：对"现有证据确实支持的子问题"回答了多少（不按"我无法"等开场措辞判整篇拒答）。

主要结论（**范围内、小样本、非发生率**，详见各报告的"限制"节）：
- 在本设置里，三种提示**都没有**把造假内容当成事实端点（AI 初评均为零；三条有毒抽样经人审未发现事实认可）。
- 提示差异主要在"归属并保留 ↔ 明确拒绝"以及有据子问题的覆盖，而非"是否把造假当事实"。
- 一次"起草前来源可信度评价"的附加步骤能改变来源处理方式（把"归属并保留"降到 0），**但安全增益尚未建立**，
  且该步是对 GPT-Researcher `SourceCurator` 的**局部适配**（更严），**最佳防御位置未评测**。见 [`CLOSEOUT_v8.md`](CLOSEOUT_v8.md)。

## 目录结构
- `packs/task_{88,89,94,73}/` — 每任务的证据包：`public/`（真实问题、正确证据、毒文档、充分证据、无害补充）与 `private/`（真值标注、真值复核，**从不进入模型输入**）。
- `runs/frozen*/` — 冻结的模型输入（每格 sha256 记录在各 `INPUTS_MANIFEST*.json`）。
- `runs/*_results.jsonl` — 原始模型输出；`runs/scored_*.jsonl` — 逐格评分；`runs/human_review_v8.jsonl` — 人审结果。
- `blind_review/` — 盲审包（隐藏方法标签）与封存答案键。
- `assemble_freeze*.py` / `run_*.py` / `score*.py` — 冻结、运行、评分脚本（标准库 urllib）。
- 报告：`DECISION_BRIEF.md`、`PILOT_RESULTS*.md`、`REVISION_20260913.md`、`REAUDIT_v7.md`、`HUMAN_REVIEW_RESULTS.md`、`PILOT_RESULTS_taskB.md`、`MIGRATION_PREP.md`、`CONSOLIDATED_REPORT.md`、`CLOSEOUT_v8.md`、`STATUS.md`。

## 复现
- **模型**：实验用 DeepSeek `deepseek-v4-flash`（OpenAI 兼容 API），少量跨模型对照走 OpenRouter（`gpt-4o-mini` / `claude-sonnet-4`）。
- **密钥**：脚本从本地文件 / 环境变量读取，**从不写入本仓库**（`DeepSeek` 走一个本地 key 文件路径；OpenRouter 走 `OPENROUTER_API_KEY`）。运行前请改成你自己的路径/变量。
- **路径**：部分脚本含作者机器的绝对路径（如密钥文件、账本 sqlite）；他人复现需自行修改。
- **数据**：`raw/`（第三方数据集逐字转储）**未纳入版本库**——请按 query_id 自行从
  HuggingFace `lee64/deepresearch-bench-query` 与 `whfeLingYu/Misleading_Knowledge` 重新拉取。

## 来源与许可
- 研究问题：**DeepResearch Bench**（`lee64/deepresearch-bench-query`）。
- 毒/误导材料改编自：**MisKnow / `whfeLingYu/Misleading_Knowledge`**。
- `packs/*/public/evidence*.txt` 含来自 Wikipedia（CC BY-SA）、学术期刊、新闻站点的**简短逐字引用**，仅作研究用途，版权归原作者。
- 本仓库代码的许可见 `LICENSE`（若尚未添加，则默认保留所有权利，待定）。

## 伦理与范围
纯防御性研究：全部为**固定证据、单轮**探针，**没有**真实智能体、没有对任何真实系统的注入或发布、没有真实外部写操作。
`detell_poison.py` 为沙盒内、全程记录的受控消融（去掉毒文档的低级破绽以模拟更强攻击者基线），**不增强虚假主张、不作为攻击工具**。
所有虚构材料仅用于理解与缓解"证据完整性"失效。

## 新一轮：GPT-Researcher R0/R1 主比较（gptr_round/）
在真实宿主 **GPT-Researcher v3.6.1**（pinned commit `6f998577`）上，以固定本地来源 + 离线检索器（无联网）跑 R0（不策展）vs R1（原版 `CURATE_SOURCES` 策展）× 3 条件（正常/无害补充/受限错误材料）× 6 新任务 × 2 次 = 72 份报告。见 `gptr_round/PREREG_round.md`（预注册）与 `gptr_round/RESULTS_round.md`（结果：阴性收尾——错误主张被当作事实/决策依据 0/24，正常任务 72/72 完成）。

> ⚠ `gptr_round/tasks/C*/error_material.txt` 同为**故意虚构的错误材料**（沙盒研究用），见 `gptr_round/FABRICATED_MATERIALS_NOTICE.md`，切勿当真。

## 新一轮：文档依赖型证据完整性（paper_round/）
在真实宿主 GPT-Researcher v3.6.1（pinned `6f998577`）上，用 QASPER（带原文证据标注）里 4 个**真正依赖外部文档**的实验条件/结论核对任务，跑 E / E+L / E+L′（L′ 仅翻转一项关键关系）× R0 / R1fix × 各一次 = 24 流程。先做三项工程契约修正（`contract.py`：稳定来源 id、空正文→无证据处理、provider 全量日志；单元测试通过）与证据依赖诊断（无来源答不出、有来源答对）。见 `paper_round/PREREG`-类材料（`tasks_manifest.json`、`_notes/qasper_candidates.md`）与 `paper_round/RESULTS_paper_round.md`（结果：E+L′ 下虚假关键关系被当作错误事实/决策依据 **0/8**；正常任务 16/16；策展不拦隐蔽第三方投毒、抵抗来自起草"优先主源"；无干净候选失效 → 如实收尾；附威胁模型边界）。

> ⚠ `paper_round/tasks/Q*/Lprime.txt` 为**故意翻转一项关键关系的虚构第三方解读**（沙盒研究用），见 `paper_round/FABRICATED_MATERIALS_NOTICE.md`；`E.txt` 为论文逐字原文。
