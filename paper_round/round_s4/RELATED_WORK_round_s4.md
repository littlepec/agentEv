# 相关工作定向对照（round_S4，2026-09-15）

范围按用户指令限定为五项。摘录由一个只读子 agent 经 WebFetch 从 arXiv abs/html 或 ar5iv 读取（引文 <25 词，附节号），主会话据此判定与本轮 T0/T1/T2 的关系；摘录未在本地二次核对，标注"子 agent 摘录"。三列分开：**完整方法**（原文做了什么）、**本轮复用的组件**、**本地适配与不主张**（不冒充原版成绩）。

| 工作 | 完整方法（子 agent 摘录） | 本轮复用的组件 | 本地适配与不主张 |
|---|---|---|---|
| **企业 ADORE**（2601.18267，Atlassian：*Orchestrating Specialized Agents for Trustworthy Enterprise RAG*；ADORE＝Adaptive Deep Orchestration for Research in Enterprise） | 五个专门 agent（Grounding／Planning／Execution 含自演化查询／Report／WebSearch）；Memory Bank＝主张–证据图，按节限定可采信证据；"memory-locked synthesis"＝每节只用该节的可采信证据写作，引用审计核对被引来源与引文片段确在可采信证据库中（§2.4.2）；覆盖驱动执行：节级覆盖审计，"When coverage indicates insufficient support, the system triggers targeted follow-up retrieval"，按覆盖满足停止而非固定步数（§2.4.3）；无独立"重读草稿对证据"的核验器；评测 DeepResearch Bench RACE 52.65（第 1）、内部企业基准 64.11、DeepConsult 77.21% 胜率；无消融、无成本数字 | T0＝其"覆盖不足→定向补取"思路压成问题级、一次、≤2 条查询；T1 的"只有主源算支持"与其"可采信证据"约束相近 | ADORE 在生成时用记忆锁定＋引用审计强制可采信证据，不是以"缺主源支持"触发补取；本轮无多 agent、无主张–证据图、无压缩。不引用其 RACE／DeepConsult 数字。**与 2606.13905 不是同一篇**：后者是 *ADORE: Iterative Query Expansion with Retrieval-Grounded Relevance Feedback*（ADapt, Observe, Relevance Evaluate；TREC DL/BEIR/BRIGHT nDCG@10），作者、缩写含义、任务、指标均不同 |
| **RARR**（2210.08726，Gao 等，ACL 2023） | Research：CQGen 生成覆盖段落各方面的问题（PaLM 少样本，采样 3 次并集），Google 搜索取 K=5 页，4 句滑窗，每问 J=1 片段；Revise：agreement 模型判断 y 与证据 e 对问题 q 是否蕴含同一答案，仅在不一致时由 edit 模型最小改动（超过 50 字符或 0.5× 长度的编辑被拒），最后输出 ≤5 片段的归属报告（§3.1–3.3）；指标 AttrAIS／auto-AIS、保留度 PresIntent×PresLev、F1_AP；PaLM/NQ auto-AIS +9.3、Levenshtein 保留 89.6%（Table 1） | T2 只借用"把草稿对证据修订"这一抽象 | T2 更接近 RARR 论文里的 LaMDA research-and-revise 基线压成一步、证据固定为已知的一份主源全文；无问题生成、无检索、无 agreement 门、无编辑长度约束、无归属报告；本轮不测保留度。RARR 的归属／保留数字不可作为本轮成绩 |
| **FAIR-RAG**（2510.22344） | 路由＋查询分解＋稠密/稀疏混合检索 RRF top-5＋证据过滤；Structured Evidence Assessment：把问题拆成"必需发现"清单，逐项确认并输出"intelligence gaps"，"evidence is deemed sufficient only if all required findings are confirmed"（§3.3.4）；Adaptive Query Refinement 只为缺口生成"laser-focused queries"（§3.3.5）；最多 3 轮；证据累积；无生成后核验；HotpotQA F1 0.453（+8.3 vs Iter-RetGen），SEA 准确率 72% | T0＝SEA 压成一个标量可作答性判断＋≤2 条补查 | 其充分性判据是"所需信息成分是否被任一证据确认"＝可作答性／覆盖，不含逐事实来源／可信源检查；T1 的主源约束与 T2 的事后修订均不在其中。F1 不可迁移 |
| **S2G-RAG**（2604.23783，ACL 2026 main） | S2G-Judge 对 (q, C_t) 输出 (s_t, G_t)，"based strictly on evidence present in C_t"；缺口项四字段（category∈{bridge_entity, attribute, relation, evidence_span, other}, target, slot, description）；**判官是训练的**（Llama-3.2-3B LoRA SFT，GPT-4o-mini 标注轨迹）；缺口→查询＝target+slot 拼接一条短语；句级抽取器只返回句子索引；最多 T=4 轮；无核验步；HotpotQA/BM25 43.3 EM／56.5 F1，去掉判官 −15.8 EM | T0＝提示式、未训练、标量近似的 S2G-Judge＋补查 | 充分性＝证据记忆能否支持作答，无来源级支持检查；T1/T2 无对应物。EM/F1 不可迁移 |
| **Sufficient Context**（2411.06037，Joren 等，ICLR 2025） | 定义：存在一个在上下文信息下合理的答案 A′ 即充分，答案无关，且明确允许"the context contains an incorrect answer"（§3.1）；autorater Gemini 1.5 Pro 一样本 CoT，115 条人标 93% 准确；发现大模型在不充分时倾向作答而非弃答（HotpotQA 不充分实例仍答对 ≥35%）；干预＝选择性生成（自评置信＋autorater 的逻辑回归），提升 2–10%；**不提出补查或归属检查**，把"用 autorater 迭代判断是否再检索"列为未来工作 | T0 的可作答性检查＝把充分性 autorater 改作补查触发器，正是其未做的未来工作方向 | 按其定义，含翻转数字的笔记仍构成"充分上下文"，因此 T0 按设计不会捕捉投毒事实；只有 T1/T2 针对来源支持。其 93%／2–10% 是其模型与提示的数字，不适用于本轮 |

## 对本轮设计与写法的直接推论

1. 五篇里没有一篇把"主源 vs 次源的来源约束"当作补查触发器（T1），只有 RARR 做事后修订（T2），且证据是开放网页而非一份已知文档。写法：T0＝组件复用（可作答性／充分性门），T1、T2＝本地适配；三者都不是任何已发表方法的实现，不引用其成绩。
2. Sufficient Context 的定义直接解释了 S3 的观察：笔记覆盖问题时上下文按定义"充分"，NONE 是正确输出。这与 RESULTS_round_s3.md §8 的更正一致：可作答性检查不是事实核验。
3. 企业 ADORE 的"记忆锁定＋引用审计"表明"只采信规定来源"在工业系统里是生成时约束；本轮 T1 把它放在检索后、起草前，作为最便宜的位置检验，是否足够由结果说。
4. 若 T1/T2 已足够，方法分支结束，不需要再对照更多迭代式方法（FAIR-RAG／S2G-RAG 的多轮与训练判官都比本轮重）；若不够，缺口定位（检查／检索／核验／成本）决定最小原型该复用谁的哪个组件。
