# 评分标签的地位（修复 2）

本仓库所有 `score*.py` / `score_reaudit_v7.py` / `score_taskB.py` 里的**硬编码标签表**，
以及 `runs/human_review_v8.jsonl`，一律按 **"标注导出（annotation export）"** 处理：
- 它们是**主体（研究 Agent）静态阅读得出的 AI 初评**，或**明确标注的人审**；
- **不是独立的自动验证器**，不得表述为"自动核验通过"。

可审计性由 `bind_scores.py` → `runs/scored_bound.jsonl` 提供：每个被标注的格子都绑定到
- 该标签所指**回答的 sha256**（`output_sha256`，取自对应 `*_results.jsonl` 的实际输出字节）；
- **证据位置**（`frozen_input` 冻结输入文件及其 sha256、底层 `packs/.../*.txt` 证据文件及 sha256）；
- `provenance` 字段显式写明 "ANNOTATION_EXPORT ... NOT independent auto-verification"。

即：标签**可追溯到确切的输入证据与输出字节**，但其正确性仍是标注（AI 初评/人审），非自动判定。
新一轮如需"独立自动验证"，须另行设计验证器（本轮不做）。
