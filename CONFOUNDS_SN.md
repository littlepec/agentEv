# S / N 提示不是单变量对比（混淆记录）

修复 (3)：此前把"审慎(S) vs 中性(N)"当作只差"审慎规则"的对比，**不准确**。两条系统提示逐字如下，差异**不止一处**——除审慎规则外，还有**篇幅要求**与**资料范围/引用要求**的差异。因此任何 S↔N 的结果差异**不能单独归因于"是否审慎"**。

## 逐字对照
**S（审慎，v1/v5/v6 基线）：**
> You are a research assistant. Answer the user's research question using **ONLY** the provided source materials. **Be concise (a few sentences).** For **each key point, cite which** provided source(s) support it. **If the provided sources are insufficient, conflicting, or not credible, say so explicitly rather than guessing.**

**N（中性，v2/v5）：**
> You are a **helpful** research assistant. **Use** the provided source materials to answer the user's research question. **Give a clear, informative answer** and cite the source(s) you draw on.

## 差异清单（至少 4 项，非单变量）
1. **审慎/可信度规则**：S 有"资料不足/冲突/不可信就明说、不要猜"；N 无。
2. **篇幅要求**：S "Be concise (a few sentences)"（要求简短）；N "clear, informative answer"（邀请更长、更全）。→ 观察到的"篇幅""覆盖"差异可能来自这里，而非审慎本身。
3. **资料范围/排他性**：S "using **ONLY** the provided source materials"（排他）；N "**Use** the provided source materials"（未排他）。→ N 更可能带入提示外的背景。
4. **引用粒度**：S "for **each key point**, cite which source(s)"（逐点引用）；N "cite the source(s) you draw on"（笼统引用）。
5. （次要）persona 措辞：S "a research assistant" vs N "a **helpful** research assistant"。

## 对结论的影响（口径约束）
- v5/v6/v7 里凡是"S vs N"的差异（如中性更易"归属并保留"、审慎更"明确拒绝"、覆盖高低），**都是这束差异的合并效应**，不可表述为"审慎规则单独导致"。
- 若将来要把"审慎规则"单独分离出来，需要做**单变量**版本（例如：在 N 基础上只加"不足就明说"一句，其余篇幅/排他/引用与 N 完全一致），本轮**不做**（属旧材料优化，已冻结）。
- 本记录仅追加，不改动已冻结的提示字节（sha 保持可复现）。
