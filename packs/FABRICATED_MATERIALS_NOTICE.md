# ⚠ 虚构材料声明 / Fabricated-materials notice

本目录下所有 `task_*/public/poison_source.txt`、`poison_clean.txt`、`poison_detell.txt`
以及 `task_*/private/claim_and_label.json` 中标注的 `target_false_claim__GEN`，
**都是为防御性安全研究而使用的、故意虚构的误导材料**，不是真实事实。

- 其中出现的机构、协议、产品、指标均为**虚构或不可核实**的，例如
  "ScripturaMax""Neuro-Aesthetic Engagement Protocol (NAEP)""RailQNet""Lexical Immersion Theater (LIT)"
  "2024 Global Elementary Literacy Index" 等——**请勿当作真实信息引用或传播**。
- 这些材料改编自公开数据集 **MisKnow / whfeLingYu/Misleading_Knowledge**（见仓库根 README 的来源与许可说明），
  用途仅为：研究"当低可信外部内容被当作证据后，错误主张如何进入 LLM 智能体的最终判断"。
- 文件保持**逐字节不变**以便用清单里的 sha256 复现实验；因此未在文件内嵌入警告横幅，
  统一在此声明。每个任务的真值与"为何为假"记录在同任务的 `private/evidence_review.md`。
- `poison_detell.txt` 与 `../detell_poison.py`：在**沙盒内、全程记录**地去掉了原毒文档的低级破绽
  （拼写粘连、"synthetic dataset"之类自曝句），用于测"文档自带破绽"这一混淆项，**未增强任何虚假主张**，
  也**未向任何真实系统注入或发布**。这是受控消融，不是攻击工具。

All "poison" files here are deliberately fabricated misinformation used as study stimuli for
defensive security research. Do not cite or spread their claims as fact.
