# NEXT_STAGE_PLAN：P1 参考实现就绪与快照比较（待启动确认；2026-09-15）

目的：在**同一冻结检索快照＋同一冻结草稿**上，检验一个能正常完成的主张级核验参考实现能否补上问题级检查漏掉的最终事实，并与同协议的全文核验比较。不找阳性、不立新方法、不加任务。H1 见 RESEARCH_DECISION.md §4。

## 1. 授权与资源

- 模型：仅 deepseek-v4-flash（同 key、同账本线 evidence-package-pilot*）；本地嵌入 all-MiniLM-L6-v2；无新服务、无外部写、无新材料生成。
- exp_key `evidence-package-pilot-p1verify`；子预算 ≤**$0.50**（开发校准 ≤$0.30、冻结比较 ≤$0.20），BudgetGuard 强制；call_cap 120；每调用显式 max_tokens 并按其预留；触顶即停。运行后账本线 ≤$5.16/$10。
- 起步探针 1 次（≤$0.001）：核对 `thinking:{"type":"disabled"}` 与 `reasoning_effort` 对该模型 id 生效、`response_format:{"type":"json_object"}` 可用；无效则记录并回退到"思考模式＋显式大上限（64K 默认）"，不虚构参数。
- 主会话执行；付费 worker 0 个子 agent；可派 1 个只读子 agent 复核补丁语义（不计费）。

## 2. 输入（全部已存在，不重跑上游）

| 快照 | 来源 | 类型 | 期望行为 |
|---|---|---|---|
| S-miss-wrong | runs_s4/B6_P_T0（context.txt＋report.md 作草稿） | 主源支持缺席，草稿采纳 44/44 | 目标主张判无支持→定向补取→改为 88/88 引 document_1，或标未核验 |
| S-miss-right | runs_s4/B6_C_T1（context.txt＋report.md） | 主源支持缺席，草稿据忠实笔记写 88/88 | 判无支持→补取→确认，改引 document_1；不得改值 |
| S-table | runs_s4/B6_P_T2（context.txt＋report_draft.md） | 表 1 碎片支持，草稿推算 88/88 并记不确定 | 认可表格组合为合法支持；不得因无原句判"不支持" |
| S-present | runs_s4/B3_P_T2（context.txt＋report_draft.md） | 支持在场，草稿已主源为准 | 无实质修改（no-op）；允许把 103/209 标为未核验 |

材料、问题、角色声明沿用 S4；运行时不读 private_eval、不读决定性位置；只知道 document_1 是用户指定论文（部署信息）。

## 3. 对照臂（同一快照、同一草稿、同一输出协议）

- **V-ref 参考实现**（组件复用，不称新方法）：① 抽取：一次调用（json_object）从草稿抽出数值／关系主张，字段 subject、attribute、value、unit_or_denominator、condition、cited_source、sentence_span；② 本地支持判定：对每条主张先在快照的 document_1 块里查（无调用的 BM25/余弦命中＋一次判定调用给 Entailment／Neutral／Contradiction，RefChecker 式，明确允许表格组合与透明计算算支持）；③ 只对 Neutral 主张做一次 struct 定向补取，查询由主张的主体／属性／条件词构成，**不携带待核数值**（另记一条带数值的对照查询仅供离线评价）；补取后再判定一次；④ 修订：一次调用输出 JSON 补丁 {old_str, new_str, claim_id, action∈{replace,mark_unverified}}，程序应用，old_str 必须唯一命中；编辑距离比 >0.5 的补丁拒绝并记录（RARR 门）。
- **V-full 全文核验**（强基线）：一次调用输入草稿＋document_1 全文，输出同格式 JSON 补丁；同一应用与拒绝规则。
- **V-rewrite 消融**（可选，预算允许时）：S4 的 T2 整篇重写协议，但推理配置与 V-full 相同；用于区分"补丁协议"与"推理预算"各自的贡献。
- 简洁回答基线不在 P1（它是起草时变量，需要新草稿），列入 P2 臂。

## 4. 工程契约（比较前必须全部通过）

- 每次调用记录 finish_reason、prompt/completion/reasoning tokens、解析结果；状态三分：VALID_NO_GAP／VALID_GAP／INVALID_OR_INCOMPLETE；空文本、非 JSON、截断一律 INVALID，不得当作 NONE 或通过。
- 最终输出状态与核验完成状态分开：任一环节 INVALID → 最终输出标 UNVERIFIED_OUTPUT（可评价其后果，不记为核验完成）。
- 补丁应用前检查：old_str 唯一命中、new_str 非空、不触及引用块以外的无关句；应用后重新抽取一次目标主张核对语义（补丁格式正确≠语义正确）。
- 所有臂用相同的 max_tokens（显式 ≥16384，非思考模式实际输出远低于此）、相同推理配置、相同补丁协议；不得让某臂长文重写而另一臂只出补丁。
- 提示中断言不含 gold：脚本在发送前对私有答案字符串做否定匹配（"88 PD patients and 88 HC"、"163 templates" 等只在评价侧）。

## 5. 有效性检查（先于任何比较结论）

1. 抽取覆盖：目标主张（B6 德语组人数；B3 模板数）是否被抽出并保留主体／值／条件——漏抽即记"抽取失败"，不计入核验结果。
2. 补取可达：S-miss-* 上不带数值的定向查询是否取到决定性句（离线探针预期可达）。
3. 判定正确：S-table 上表格组合被判支持；S-present 上主源值被判支持、笔记值被判矛盾。
4. 修订保持：S-present、S-table 的非目标句零改动；S-miss-right 值不变、仅改归属。
5. 完成率：每臂 4 快照全部 VALID；任一臂在 2 次配置迭代后仍 ≥2 快照 INVALID → 工程阻塞，停止并汇报，不据此称新方法需求。

## 6. 端点与记录（每臂每快照）

E1 目标事实终态：correct／wrong／marked_unverified；E2 非目标内容误改数；E3 各环节完成状态；E4 主源支持取得（句子／表格／无；来自窗口还是补取）；E5 阅读量（总提示 token，区分抽取／判定／补取／修订）、调用数、费用（按全未命中价与实测缓存命中两种口径）、延迟。固定草稿的生成费用如实记为"复用"，估算部署成本时对所有臂加回同一份。

## 7. 流程与预算估算

1. 探针 1 次（$0.001）。
2. 开发校准：4 快照 × V-ref（3–5 次调用/快照）＋V-full（1 次）≈ 每轮 $0.06–0.10；最多 2 轮（≤$0.20），期间允许改提示、上限、JSON 协议，全部记录。
3. 冻结配置（sha＋时间戳入 LOG），预注册 H1 的通过／失败判据（§8），然后在同 4 快照上跑冻结比较 1 次（≤$0.12），V-rewrite 消融视余额（≤$0.08）。
4. 评分：规则初筛＋主会话逐格核对实际输入与补丁；AI 初评，不标人审。
总计 ≤$0.50；老 B3/B6 快照只作开发／回归，**不作为独立确认**。

## 8. H1 判据与退出

- **H1 成立**＝V-ref 4/4 VALID，S-miss-wrong 终态 correct 或 marked_unverified，S-miss-right 值不变且归属改为主源，S-table 与 S-present 零误改，且每快照总提示 token ≤ V-full。→ 已有方法足够：工程收尾，保留参考实现；是否进 P2 只取决于成本差距是否值得在新任务上量化（H2），否则结束。
- **H1 不成立而 V-full 成立**＝定位失败环节（抽取／判定／补取／修订／容量）；若是配置或容量→修一次；若是判定或选择环节→写 P2 任务包（4–6 个新任务，须新材料生成授权）。
- **两臂都失败于 S-miss-wrong**＝残差真实存在于"主源证据缺席"条件；P2 前先核对是抽取还是判定失败，不直接立 P3。
- **正常完成困难**（§5.5）＝工程阻塞，汇报后停。
- 预算触顶、需要新材料、需要换模型或改角色声明→停止并升级用户。

## 9. 交付

paper_round/p1_verify/{PREREG_p1.md, p1_verify.py, score_p1.py, runs_p1/, RESULTS_p1.md}；tasks.md 新行；LOG.md 冻结与结果各一条。汇报格式："我的推荐是___；依据___；最大的反证是___；下一阶段___；所需批准只涉及___。"
