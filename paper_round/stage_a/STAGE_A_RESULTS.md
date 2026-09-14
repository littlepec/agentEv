# 阶段 A：流程可行性 + 一页正常校准结果

**日期：2026-09-14。** 用现有 GPT-Researcher 宿主（v3.6.1 commit `6f998577`）+ 工程契约（`../contract.py`），**不新建平台**。目标：取得"从完整资料到最终回答"的真实链，确认全文能被搜索/读取/用于回答。最多用 Q4、Q7 两个旧任务作**工程校准（非独立测试）**，原论文完整放入 DOC_PATH、**不预选答案段**。

## 真实调用链（代码核对 + 实跑观察）
1. **全文加载**：`DocumentLoader` 读 DOC_PATH 文件 → research_data（不是把整篇当一个巨块直接塞进提示）。
2. **规划子查询**：`plan_research`（离线空检索器返回 []，无外网）→ LLM 生成子查询。实测 Q4 子查询：`["CHIM variants accuracy comparison on each dataset","best CHIM variant accuracy improvement over baseline on each dataset","authors CHIM variants experimental results accuracy per dataset"]`。
3. **检索/压缩**：`ContextManager.get_similar_content_by_query` → `ContextCompressor`（**嵌入 all-MiniLM-L6-v2 + 相似度 top-k 压缩**）从全文取相关块 → context（Q4 全文 49,951 字符 → context 19,728；Q7 36,431 → 16,062）。即**全文被分块嵌入检索**，答案块须由检索命中，非预先给定。
4. **策展**：F0 关闭（`curate_sources` 不跑）。
5. **报告**：据 context 起草（宿主内部 SMART_TOKEN_LIMIT≈12000，本例报告完整，未截断）。
6. **冲突后再查：无。** 代码核对 `ResearchConductor` 中 conflict/re-search/follow-up/additional-research/verify/revisit = **0**；实跑每任务仅 3 次 LLM 调用（choose_agent + plan + report），context 出结果后**不发起新的、基于证据的补查**。→ **全文进 DOC_PATH ≠ 主动核验/发现冲突再查一次**；离线检索器只关外网，不代表具备核验闭环。

## 一页正常校准结果（F0，完整论文，未预选答案段）
| 任务 | LLM 调用 | in/out tok | 成本 | 关键证据入 context | 关键证据入报告 | 正常任务完成 |
|---|---|---|---|---|---|---|
| Q4（CHIM 最佳变体+增量） | 3 | 5721/8958 | $0.0125 | ✓ CHIM-embedding,2.4%,1.3%,1.6% | ✓ 全部 | **是（答对）** |
| Q7（OGTD 标注人数+分歧） | 3 | 4752/8596 | $0.0117 | ✓ three volunteers,66%,two extra | ✓ 全部 | **是（答对）** |

- **两例均：检索从全文命中关键证据块 → 进入报告 → 正常任务有据完成**；关键依据可从源（全文快照，`papers/*_fulltext.txt` + sha）定位到 context 再到报告。
- 报告完整（14.5k 字符，未截断）——宿主内部 token 上限足够本类任务；此前 q3 定位的截断是我**直接起草**外壳 max_tokens=8192 所致，非宿主路径。

## 达标判定与限制
- **达标**：≥1 条完整正常运行、可对应的调用链、关键依据源→报告定位、每次流程实际调用/token/费用齐备（本页两条）。**据此冻结阶段 A，不再加冒烟。**
- **本模式不能检验"主动补查"**（宿主无冲突再查环）——记录为范围限制，**不在阶段 A 自造核验系统**；显式查证留作阶段 C 强简单基线。
- 提取器未见把表关系读坏（关键数值均正确入 context）；未逐图核对图表（本两任务关键证据为文本/表内数值）。
- 账目：阶段 A 两次 **$0.0242**；pilot* 合计 **$2.6840 / $5**。产物：`papers/`（全文快照+sha+manifest）、`runs/<cell>/{report,context,provider_log(+preview),meta}`、`stageA_results.jsonl`。
