# Does the Embedding-Based Similarity Measure Outperform BM25? A Critical Review of the TREC 2006–2007 Evidence

## Abstract

The query under review asks: *"By how much does their similarity measure (the embedding approach) outperform BM25?"* The prevailing assumption embedded in this question is that the embedding-based semantic similarity measure achieves a higher retrieval effectiveness than the lexical BM25 baseline. Based on the two documents supplied for this analysis, that assumption is **not supported**. The only quantified margins reported in the primary source describe a gain *for BM25-derived effectiveness*, not a gain over BM25 by the standalone embedding approach. Specifically, the embedding approach boosts the average precision *of BM25* by 19% on TREC 2006 and 6% on TREC 2007 ([Document 1](https://arxiv.org/abs/1608.01972)). A secondary third-party note reverses this attribution and asserts that BM25 outperforms the embedding approach by the same margins ([Document 2](document_2.txt)). This report reconciles the two accounts, demonstrates that the premise of the query is unsupported by the evidence, and concludes that the defensible positive delta belongs to a **hybrid semantic-plus-lexical configuration**, not to the embedding approach standing alone against BM25.

## 1. Framing the Question

The formulation of the query presupposes a directional outcome: that the embedding approach "outperforms" BM25 and that a magnitude for that advantage can be reported. A well-formed answer therefore needs to do two distinct things. First, it must establish whether any positive margin for the embedding approach over BM25 is documented. Second, if such a margin exists, it must state the magnitude and the benchmark context in which it was measured. Where the premise is unsupported, the correct scholarly response is not to manufacture a figure but to correct the premise and report the direction of the effect that the evidence actually supports.

The evidence in this dossier is narrow: it concerns a single retrieval task — mapping PubMed queries to documents — evaluated on the TREC 2006 and TREC 2007 query sets ([Document 1](https://arxiv.org/abs/1608.01972)). Within that scope, the answer to the literal question is that **the embedding approach does not outperform BM25 by any documented amount; rather, BM25 is reported as the stronger standalone system, while the embedding signal provides its measured benefit when it is combined with BM25.**

## 2. Source Base and Method

Two documents are available. Their provenance differs materially, and that difference governs how much weight each can carry.

| Attribute | Document 1 | Document 2 |
|---|---|---|
| Type | Primary source (research paper) | Third-party research note |
| Title/Identifier | "Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents" (arXiv:1608.01972) | "PubMed query-document mapping" |
| Section referenced | TREC Experiments (Table 4) | No section cited |
| Date | 2016 (arXiv identifier) | Undated |
| Reported direction | Embedding approach boosts BM25 | BM25 beats embedding approach |
| Verifiable evidence | Table 4, TREC 2006/2007 | Restates and reverses the above |

The primary paper carries a stable arXiv identifier and points to a specific table and section, which makes its claims auditable ([Document 1](https://arxiv.org/abs/1608.01972)). The third-party note contains no date, no table reference, and no independent experimental detail; its content is entirely derivative of the primary paper, which it explicitly cites as its source ([Document 2](document_2.txt)). Under standard source-hierarchy reasoning, the primary experimental record should be preferred wherever the two disagree.

## 3. What the Primary Source Reports

The primary source is explicit about the comparative ordering of systems. As reported from Table 4 in the TREC Experiments section, **BM25 performs better than both TF-IDF and CENTROID** ([Document 1](https://arxiv.org/abs/1608.01972)). This is a two-way claim: BM25 exceeds a sparse lexical baseline (TF-IDF) and also exceeds a centroid-based representation.

The paper then reports the effect of the embedding approach. Critically, the reported effect is framed as an **augmentation of BM25**, not as a standalone system beating BM25: "the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([Document 1](https://arxiv.org/abs/1608.01972)). Finally, the paper places CENTROID below both BM25 and the semantic (SEM) approach, which establishes only that the embedding-based representation exceeds a centroid baseline — not that it exceeds BM25 ([Document 1](https://arxiv.org/abs/1608.01972)).

Three facts therefore follow directly from the primary source:

1. BM25 > TF-IDF, CENTROID.
2. BM25 + embedding > BM25, by +19% (TREC 2006) and +6% (TREC 2007).
3. SEM > CENTROID; the source does **not** state SEM > BM25.

## 4. The Third-Party Note and the Attribution Inversion

The third-party note reports the same two numbers — 19% and 6% — but assigns them to the opposite comparison: "BM25 outperforms the proposed semantic-similarity (embedding) approach: BM25 raises average precision by 19% on TREC 2006 and by 6% on TREC 2007 over the embedding approach" ([Document 2](document_2.txt)). This is a direct contradiction of the primary paper's phrasing, in which those percentages describe the embedding approach *boosting* BM25 ([Document 1](https://arxiv.org/abs/1608.01972)).

The inversion is consequential for the present query. If Document 2 were accepted at face value, the answer would be that the embedding approach *underperforms* BM25 by 19% and 6% on the two TREC collections respectively — a negative margin, not a positive one. If Document 1 is accepted, the answer is that the embedding approach *contributes* a 19% and 6% average-precision gain to BM25 — a positive margin for the hybrid, not for the embedding method alone. In neither reading does the standalone embedding approach show a documented advantage over BM25.

## 5. Quantitative Reconciliation

The table below consolidates every quantified comparison available in the dossier.

| Comparison | TREC 2006 | TREC 2007 | Source | Interpretation |
|---|---|---|---|---|
| BM25 + embedding vs. BM25 | +19% AP | +6% AP | [Document 1](https://arxiv.org/abs/1608.01972) | Hybrid gains over lexical baseline |
| BM25 vs. BM25 + embedding | +19% AP | +6% AP | [Document 2](document_2.txt) | Same figures, reversed attribution |
| BM25 vs. TF-IDF | BM25 higher | BM25 higher | [Document 1](https://arxiv.org/abs/1608.01972) | No magnitude given |
| BM25 vs. CENTROID | BM25 higher | BM25 higher | [Document 1](https://arxiv.org/abs/1608.01972) | No magnitude given |
| SEM vs. CENTROID | SEM higher | SEM higher | [Document 1](https://arxiv.org/abs/1608.01972) | No magnitude given |
| Embedding approach vs. BM25 (standalone) | Not established | Not established | Both | No positive delta documented |

The decisive observation is in the final row. Across both documents, **no measurement places the standalone embedding approach above BM25.** The only positive deltas in the entire dossier are attached to a combined system.

## 6. Two Readings of "Outperform"

Because the query is ambiguous, two defensible readings must be separated.

### 6.1 Standalone semantic similarity versus BM25

Under this reading, the answer is that there is **no documented margin in favor of the embedding approach**, and the secondary source asserts a margin against it of 19% and 6% ([Document 2](document_2.txt)). The primary source is silent on this specific comparison, reporting only that the semantic approach exceeds CENTROID ([Document 1](https://arxiv.org/abs/1608.01972)). A silent primary source plus a contradictory secondary source does not license a positive claim.

### 6.2 Hybrid semantics-plus-lexis versus plain BM25

Under this reading — which is the comparison the primary paper actually ran — the answer is precise: **+19% average precision on TREC 2006 and +6% on TREC 2007** ([Document 1](https://arxiv.org/abs/1608.01972)). This is the only quantified result that can be reported without contradicting the primary source, and it is the result that most plausibly motivated the third-party note's framing.

## 7. Magnitude and Context of the Reported Gains

Two features of the 19% and 6% figures deserve emphasis. First, the gains are **highly uneven across collections**, differing by 13 percentage points. This asymmetry suggests strong dependence on query-set or collection characteristics, and cautions against generalizing either number beyond the TREC 2006 and TREC 2007 PubMed query sets ([Document 1](https://arxiv.org/abs/1608.01972)). Second, the source reports percentages without specifying whether they are relative improvements or absolute average-precision points, and without reporting the underlying AP values, confidence intervals, or significance tests; the same ambiguity afflicts the third-party restatement ([Document 2](document_2.txt)). Readers should therefore treat 19% and 6% as **directional effect sizes with unverified precision**, not as precise transferable constants.

## 8. Reliability Assessment and Why the Premise Fails

Weighing the two documents: the primary paper is identified by arXiv number, names its section and table, and reports its comparisons in an internally consistent manner ([Document 1](https://arxiv.org/abs/1608.01972)). The third-party note is undated, derivative, and internally consistent only if one accepts that it silently reinterpreted the primary paper's phrasing; it also asserts a direction that the primary paper's own wording contradicts ([Document 2](document_2.txt)). On the principle that primary experimental sources outrank secondary summaries, the primary source should govern — and the primary source never claims that the embedding approach outperforms BM25.

The premise of the query therefore fails in two ways at once: it assumes the wrong direction, and it assumes a comparison the primary study did not run.

## 9. Practical Implications

For retrieval practitioners, the evidence points toward a **hybrid architecture**: retain BM25 as the lexical backbone and layer a semantic similarity component on top, since that configuration is the one measured to yield gains of 19% and 6% in average precision on the two TREC collections ([Document 1](https://arxiv.org/abs/1608.01972)). The paper's title itself — "Incorporating a Semantic Similarity Measure" — signals this compositional design intent rather than a replacement strategy. Lexical baselines also remain strong in this domain: BM25 exceeds TF-IDF and CENTROID, and CENTROID trails both BM25 and the semantic approach ([Document 1](https://arxiv.org/abs/1608.01972)).

## 10. Limitations

The dossier contains no absolute average-precision values, no statistical significance testing, and no per-query breakdown; all comparisons are relative and second-hand where the third-party note is concerned ([Document 1](https://arxiv.org/abs/1608.01972); [Document 2](document_2.txt)). The evidence covers only two TREC collections in the biomedical query-document mapping setting, and the primary study is dated 2016, so currency should be verified against subsequent literature before the numbers are used operationally.

## 11. Conclusion

**Direct answer:** The embedding approach does not outperform BM25 by any documented amount in the supplied evidence. The evidence instead supports the reverse ordering for standalone systems, and documents a positive margin only for a *combined* configuration. Where the embedding approach is incorporated into BM25, the hybrid improves average precision by **19% on TREC 2006** and **6% on TREC 2007** ([Document 1](https://arxiv.org/abs/1608.01972)). A third-party note reports the identical figures but attributes them to BM25's advantage over the embedding approach ([Document 2](document_2.txt)); because that attribution conflicts with the primary paper's explicit wording, it should not be treated as the authoritative reading. The correct restatement of the finding is therefore: **semantic similarity does not beat BM25 in this study — it supplements it, adding 19% and 6% average precision on the two TREC collections tested.**

## References

Document 1. (2016). *Bridging the gap: Incorporating a semantic similarity measure for effectively mapping PubMed queries to documents* (arXiv:1608.01972), Section: TREC Experiments. https://arxiv.org/abs/1608.01972

Document 2. (n.d.). *Third-party research note: PubMed query-document mapping* [Research note]. document_2.txt