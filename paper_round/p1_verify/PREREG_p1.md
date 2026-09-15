# 预注册：P1 冻结比较——主张级核验参考实现 vs 同协议全文核验（同一冻结快照＋同一冻结草稿）

日期：2026-09-15。冻结方式：本文件与 `p1_verify.py`（含全部提示、角色声明、补丁应用规则、确定性出现扩展）的 sha256＋时间戳记入 F:/defense/LOG.md。开发校准两轮（dev1、dev2，`runs_p1/CALIBRATION_LOG.md`）已结束；本轮为冻结配置下的正式一轮，每快照每臂 1 次；老 B3/B6 快照只作开发／回归，**不作为独立确认**。H1 见 ../../RESEARCH_DECISION.md §4；判据来自 ../../NEXT_STAGE_PLAN.md §8，未因开发结果改动。

## 冻结的输入、配置与臂

- 快照（S4 冻结记录；窗口＝context.txt，草稿＝report.md 或 report_draft.md）：S-miss-wrong＝B6_P_T0（主源支持缺席，草稿采纳 44/44）；S-miss-right＝B6_C_T1（支持缺席，草稿据忠实笔记写 88/88）；S-table＝B6_P_T2（表 1 碎片支持，草稿推算 88/88）；S-present＝B3_P_T2（支持在场，草稿已主源为准）。
- 提供方配置（两臂相同）：deepseek-v4-flash，`thinking:{"type":"disabled"}`，temperature 0，max_tokens 16384，`response_format json_object`；探针已验证生效（runs_p1/probe_summary.json）。
- V-ref：抽取（去重主张＋≤5 verbatim span，≤50 条）→ 对窗口 document_1 块判定（Entailment／Contradiction／Neutral，表格组合与透明算术算支持）→ 对 ≤12 条 Neutral 主张各做一次 document_1 章节索引定向补取（查询＝主体＋属性＋条件词，不带值）→ 对窗口＋补取块再判定 → 对 Contradiction 主张做确定性出现扩展（同值＋主题关键词的句子／表格行，≤6）→ 一次补丁调用（replace／annotate／mark_unverified／reattribute）→ 程序应用（old_str 精确或空白折叠唯一匹配；去重；replace 的编辑距离按较长串归一 ≤0.5；注释类增量 ≤max(80, 0.5·len)）。
- V-full：草稿＋document_1 全文 → 一次调用输出同格式补丁 → 同一应用规则。
- V-rewrite（探索性，仅当余额允许）：S4 VERIFY_PROMPT 整篇重写，同推理配置。
- 运行时不读 private_eval／依据位置；发送前断言提示不含 correct_answer。

## 已观察（dev1／dev2，冻结前；不作预测对象）

dev 两轮 16/16 VALID，无截断。dev2：S-miss-wrong 的 V-ref 经不带数值补取判出 Contradiction 并替换首句，但重复出现处未修（抽取器只给单 span）→ 冻结前加入确定性出现扩展，离线在 dev2 输出上验证 1→3 个 span；V-full 修三处、剩元句一处。S-miss-right 两臂改引主源、值不变；V-ref 过度标注 2 处（"三个数据集"、"188 合计"）。S-table 两臂只注释笔记句。S-present V-ref 无过度标注、4 处注释；V-full 4 处小补丁。V-ref 提示 token ≈ V-full 的 2 倍。

## 预测（冻结轮）

1. 完成率：两臂 8/8 VALID。
2. S-miss-wrong：V-ref 抽出德语组人数主张→窗口 Neutral→补取取到决定性句→Contradiction→替换 ≥3 处（首句、表格行、元句或结论句）；最终文本里不再有把 44/44 作为论文事实的句子（允许 "document_2 reports 44" 式从句）。V-full 同样修 ≥3 处，最多剩 1 处元句。两臂 E1＝correct。
3. S-miss-right：两臂值不变；V-ref reattribute ≥1 处（德语句）；V-ref 过度标注 ≤2 处；V-full 非目标补丁以 reattribute 为主，不引入事实错误。
4. S-table：两臂只对笔记 44/44 句做 annotate；无 mark_unverified；无非目标误改。
5. S-present：V-ref 无 mark_unverified，annotate 4–6 处（均在笔记归属句）；V-full ≤6 条补丁，无值改动。
6. 成本：V-ref 每快照 3–4 次调用、10–25k 提示 token、$0.007–0.02；V-full 1 次、8–12k、$0.004–0.006。**预测 V-ref 总提示 token 高于 V-full**，即 H1 的成本子句（"每快照总提示 token ≤ V-full"）不成立。

可证伪结果：预测 2 的反例＝抽取漏掉德语主张、补取未取到、判定非 Contradiction、或扩展后仍有 44/44 作为论文事实留在结论／表格；预测 6 的反例＝V-ref token 低于 V-full。

## 端点（每臂每快照）

E1 目标事实终态（correct／wrong／marked_unverified／mixed＝部分出现处仍错）；E2 非目标误改：分"引入事实错误"与"过度标注／冗余注释／语义略变"两类计数（主会话逐条核对）；E3 各环节完成状态；E4 主源支持取得（句子／表格／无；来自窗口还是补取）；E5 阅读量（总提示 token，分环节）、调用数、费用、延迟。

## 决定规则（与 NEXT_STAGE_PLAN §8 一致）

- **H1 成立**＝V-ref 4/4 VALID，S-miss-wrong E1 correct 或 marked_unverified（且结论／表格不再把 44/44 作为论文事实），S-miss-right 值不变且归属改为主源，S-table 与 S-present 不引入事实错误且对论文支持的主张无 mark_unverified，且每快照总提示 token ≤ V-full。
- H1 不成立而 V-full 成立 → 逐环节定位。若唯一不成立的是成本子句，结论＝"已有方法足够（V-full 一次全文核验＋补丁协议）；主张级选择性核验在短论文上无成本优势，能力上等价"，工程收尾，P2 只在长论文／多主张任务有实际需求时再议（H2 暂存）。
- 两臂都在 S-miss-wrong 失败 → 残差真实；先核对是抽取、补取、判定还是补丁环节，写 P2 任务包，不直接立 P3。
- 任一臂 ≥2 快照 INVALID → 工程阻塞，汇报后停。
- 探索性：V-rewrite 结果、过度标注的具体原因、扩展加入的 span 数，均作探索性报告。

## 预算

已用：探针 $0.0002、dev1 $0.0722、dev2 $0.0748（合计 $0.147／校准上限 $0.30）。冻结轮估算 ≤$0.09；V-rewrite 探索 ≤$0.06；P1 合计 ≤$0.30／子预算 $0.50。触顶即停。
