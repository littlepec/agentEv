# Lowest Single-Model Word-Level Penn Treebank Test Perplexity Without Dynamic Evaluation, Cache/Pointer Augmentation, Ensembles, or Fine-Tuning: A Comparative Ranking

## Scope, Eligibility Criteria, and Method

This report answers a narrow, verifiable question: across the papers represented in the supplied source documents, which paper reports the **lowest word-level test perplexity on the Penn Treebank (PTB) for a single model**, where that result does **not** rely on dynamic evaluation, cache or pointer augmentation, ensembling/model averaging, or fine-tuning. Weight tying (parameter sharing between input and output embeddings), variational dropout, MC dropout at test time, recurrence depth, and architectural search are all treated as ordinary single-model modelling choices and are therefore **admissible**, since the query's exclusion list does not cover them.

Every candidate number was extracted from the supplied notes and text extracts, and each paper was screened against the exclusion list. Where a paper reports several numbers, only its best eligible single-model result is used for ranking, although secondary results are reported for context. Only results explicitly described as single-model PTB word-level test perplexity were admitted; ensembled, averaged, or ambiguously specified figures were rejected or flagged.

## Headline Finding

The lowest eligible value in the provided corpus is **58.3 word-level test perplexity on the Penn Treebank**, reported by the paper *On the State of the Art of Evaluation in Neural Language Models* ([1707.05589_note.txt](1707.05589_note.txt)). That figure belongs to the paper's own proposed model, a **4-layer LSTM with 24M parameters**, and the authors state that at the 24M parameter budget all depths obtain very similar results, reaching 58.3 at depth 4 ([1707.05589_note.txt](1707.05589_note.txt)). Critically, the note records that this result is reported for a single model **without dynamic evaluation, cache/pointer, ensemble, or fine-tuning**, and that the authors explicitly refrain from including techniques known to push perplexities even lower because their stated aim is strictly better architectural comparison ([1707.05589_note.txt](1707.05589_note.txt)). This makes 58.3 both the lowest value and one of the cleanest matches to the query's constraints.

## Ranked Comparison of Papers

### Ranking Table

| Rank | Paper (source document) | Best eligible configuration | Word-level PTB test PPL | Parameters | Single model? | Excluded techniques reported? |
|---|---|---|---|---|---|---|
| 1 | *On the State of the Art of Evaluation in Neural Language Models* ([1707.05589_note.txt](1707.05589_note.txt)) | 4-layer LSTM | **58.3** | 24M | Yes | None reported |
| 2 | Neural Architecture Search ([1611.01578_note.txt](1611.01578_note.txt)) | NAS, base 8 + shared embeddings | **62.4** | 54M | Yes | None reported |
| 3 | Variational RHN ([1607.03474_note.txt](1607.03474_note.txt)) | Variational RHN + WT (10-layer) | **65.4** | 23M | Yes | None reported |
| 4 | Variational LSTM / MC dropout ([1512.05287_note.txt](1512.05287_note.txt)) | Large Variational LSTM, untied, MC | **73.4** | 66M (per comparison table, [1611.01462.txt](1611.01462.txt)) | Yes | Ensemble reported separately, not used here |
| 5 | Using the Output Embedding to Improve Language Models ([1608.05859_note.txt](1608.05859_note.txt)) | Large NNLM + Weight Tying | **74.3** | Not stated | Yes | None reported |
| 6 | Regularized LSTM ([1409.2329_note.txt](1409.2329_note.txt)) | Large regularized LSTM | **78.4** | Not stated | Yes | Model averaging reported separately, not used here |
| 7 | Character-aware LSTM ([1508.06615_note.txt](1508.06615_note.txt)) | LSTM-Char-Large | **78.9** | Not stated | Yes | Ensembles explicitly excluded by the authors |
| 8 | GRURNTN ([1706.02222_note.txt](1706.02222_note.txt)) | GRURNTN | **87.38** | Not stated | Yes (as described) | None reported |
| 9 | VD-LSTM+REAL ([1611.01462.txt](1611.01462.txt)) | VD-LSTM+REAL (200 units) | **138.4** | Not stated | Yes | None reported |

Lower values indicate better performance. Rank ordering follows the numerical values only; the comparability caveats discussed below should be read alongside the table.

## Paper-by-Paper Findings

### Rank 1 — 58.3 (State-of-the-Art Evaluation Paper)

The strongest eligible result comes from the 2017 evaluation study, which reports a best word-level test perplexity of **58.3** on PTB for a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](1707.05589_note.txt)). The reported experimental logic is notable: at the 24M parameter budget, depth variations produced very similar results, with depth 4 attaining the reported 58.3 ([1707.05589_note.txt](1707.05589_note.txt)). Because the paper's stated purpose is fair architecture comparison, it deliberately omits methods that would inflate headline performance ([1707.05589_note.txt](1707.05589_note.txt)). This makes its 58.3 unusually well-aligned with the query's eligibility criteria.

### Rank 2 — 62.4 (Neural Architecture Search)

The Neural Architecture Search paper reports **62.4** test perplexity for its best configuration, described as NAS with base 8 and shared embeddings at 54M parameters ([1611.01578_note.txt](1611.01578_note.txt)). Two other NAS configurations are reported at **64.0** (base 8, shared embeddings, 25M parameters) and **67.9** (base 8, 32M parameters) ([1611.01578_note.txt](1611.01578_note.txt)). All three are single-model numbers on the PTB language modelling test set, with no dynamic evaluation, cache/pointer, ensemble, or fine-tuning reported ([1611.01578_note.txt](1611.01578_note.txt)). The same source identifies the best listed baseline as "Zilly et al. 2016 – Variational RHN, shared embeddings" at **66.0** test perplexity with 24M parameters, and frames the 62.4 NAS result as roughly a 3.6-perplexity improvement over that previous state of the art ([1611.01578_note.txt](1611.01578_note.txt)).

### Rank 3 — 65.4 (Variational RHN + Weight Tying)

The Variational RHN paper reports its best PTB word-level test perplexity as **65.4** for Variational RHN + WT, with **68.5** for Variational RHN without weight tying ([1607.03474_note.txt](1607.03474_note.txt)). The best 10-layer model with reduced weight decay reaches 67.9/65.4 validation/test, and Table 1 of that paper lists Variational RHN + WT at 23M parameters with 67.9/65.4 validation/test perplexity ([1607.03474_note.txt](1607.03474_note.txt); [1607.03474.txt](1607.03474.txt)). The described setting uses variational dropout plus weight tying of input and output mappings ([1607.03474_note.txt](1607.03474_note.txt)). The paper reports no dynamic evaluation, cache/pointer, ensemble, or fine-tuning for its own model; cache and pointer methods appear only as baselines and ensembles only in comparison ([1607.03474_note.txt](1607.03474_note.txt)). It further claims RHNs outperform most single models as well as all previous ensembles ([1607.03474_note.txt](1607.03474_note.txt)).

A discrepancy deserves explicit note: the NAS comparison table lists the same Zilly et al. lineage at **66.0** rather than 65.4 ([1611.01578_note.txt](1611.01578_note.txt)). Either way, this paper ranks third; the discrepancy is 0.6 perplexity and is likely attributable to which configuration (parameter count, layer depth, weight decay setting) is being tabulated.

### Rank 4 — 73.4 (Variational LSTM with MC Dropout)

The Variational LSTM paper reports **73.4** test perplexity, described as a reduction from 78.4 achieved with MC dropout and untied weights ([1512.05287_note.txt](1512.05287_note.txt)). This is explicitly a single-model result for the large Variational LSTM with untied weights and MC dropout at test time, and the paper asserts it is, to its knowledge, the best single-model perplexity on PTB ([1512.05287_note.txt](1512.05287_note.txt)). The Table 1 caption confirms single-model perplexity on test and validation sets ([1512.05287.txt](1512.05287.txt)). No dynamic evaluation, cache/pointer, or fine-tuning is reported for this result ([1512.05287_note.txt](1512.05287_note.txt)). The paper does report an ensemble (68.7 with 10 Variational LSTMs), which is excluded here ([1512.05287_note.txt](1512.05287_note.txt)).

### Rank 5 — 74.3 (Large NNLM with Weight Tying)

The output-embedding/weight-tying paper reports **74.3** test perplexity for its Large + Weight Tying NNLM and **100.9** for Small + WT + projection regularization, both in single-model settings without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). Its comparison baselines include Zaremba et al.'s large NNLM at 78.4 and small NNLM at 114.5, plus non-dropout references such as KN 5-gram at 141, RNN at 123, LSTM at 117, Stack RNN at 110, FOFE-FNN at 108, Noisy LSTM at 108.0, and Deep RNN at 107.5 ([1608.05859_note.txt](1608.05859_note.txt)).

### Rank 6 — 78.4 (Large Regularized LSTM)

The regularized LSTM paper reports a **large regularized LSTM at 78.4** and a **medium regularized LSTM at 82.7**, both lower (better) than all listed single-model baselines, including Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5 ([1409.2329_note.txt](1409.2329_note.txt)). Its remaining headline numbers (77.0, 73.3, 72.0, 73.6, 69.5, 68.7) are model-averaging results over 2, 5, 10, and 38 models and are therefore excluded from this ranking ([1409.2329_note.txt](1409.2329_note.txt)).

### Rank 7 — 78.9 (Character-Aware LSTM)

The character-aware LSTM paper reports **78.9** for LSTM-Char-Large and **92.3** for LSTM-Char-Small, with predictions made at the word level and results explicitly single-model ([1508.06615_note.txt](1508.06615_note.txt)). The authors exclude ensembles on comparability grounds, quoting that lower perplexities reported with model ensembles "are not comparable to the current work," and report no dynamic evaluation, cache/pointer, or fine-tuning PTB results ([1508.06615_note.txt](1508.06615_note.txt)). Its large model is the 19M-parameter CharCNN entry listed at 78.9 in a later comparison table ([1611.01462.txt](1611.01462.txt)).

### Rank 8 — 87.38 (GRURNTN)

The GRURNTN paper reduces perplexity from 97.78 to **87.38** over GRURNN, a 10.4 absolute and 10.63% relative reduction, while LSTMRNTN reduces from 108.26 to 96.97 ([1706.02222_note.txt](1706.02222_note.txt)). GRURNTN is described as the strongest proposed word-level PTB perplexity in that table and as outperforming all baseline and other listed models by a large margin ([1706.02222_note.txt](1706.02222_note.txt)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported.

### Rank 9 — 138.4 (VD-LSTM+REAL)

The VD-LSTM+REAL paper reports its framework variants at 148.0, 142.5, 141.9, and **138.4** test perplexity for VD-LSTM, VD-LSTM+AL, VD-LSTM+RE, and VD-LSTM+REAL respectively, in a table captioned as a word-level validation/test comparison on PTB ([1611.01462.txt](1611.01462.txt)). These are markedly higher than other entries in this ranking; the table's "(200 units)" designation and the positioning of these rows relative to Zaremba et al.'s LSTM (large) at 78.4 and Gal's VD-LSTM large untied MC at 73.4 suggest a smaller-model regime that is not directly comparable in scale ([1611.01462.txt](1611.01462.txt)). Data-quality caveat: the supplied extract contains both a small-model block (148.0–163.19) and a separate comparison table, so the VD-LSTM+REAL 138.4 figure should be treated as provisionally comparable at best.

## Interpretation: Why the Ordering Looks This Way

Three structural patterns explain the ranking. First, **recency correlates strongly with lower perplexity**: the 2017 evaluation study (58.3) and the NAS paper (62.4) sit above the 2016 Variational RHN (65.4), which in turn sits above the 2015–2016 cluster (73.4–78.9). Second, **regularization and parameter-sharing matter**: weight tying improves the RHN from 68.5 to 65.4 and forms the centrepiece of the Press & Wolf NNLM result at 74.3. Third, **parameter budget interacts with architecture search**: the NAS result at 62.4 required 54M parameters, whereas the 58.3 LSTM result was achieved at 24M. Notably, the 58.3 paper's stated motivation—clean comparison rather than leaderboard maximization—means its number most likely understates what could be achieved with the excluded techniques. Fourth, the ordering contradicts the historical claim in the Variational LSTM paper that 73.4 was the best single-model perplexity, a claim that was accurate at its time of writing but is superseded by later work ([1512.05287_note.txt](1512.05287_note.txt)).

## Caveats, Discrepancies, and Data-Quality Notes

1. **The Zilly et al. discrepancy (65.4 vs 66.0).** The originating paper reports 65.4; the NAS comparison table reports 66.0 for "Variational RHN, shared embeddings" ([1607.03474_note.txt](1607.03474_note.txt); [1611.01578_note.txt](1611.01578_note.txt)). Rank 3 is unaffected either way.
2. **Weight tying is not an excluded technique.** Had weight tying been disallowed, the RHN figure would be 68.5 and the Press & Wolf figure would shift substantially, changing ranks 3 and 5 ([1607.03474_note.txt](1607.03474_note.txt); [1608.05859_note.txt](1608.05859_note.txt)).
3. **Comparability of corpus preprocessing is not guaranteed.** Sources reference differing preprocessing lineages, and some comparison tables mix model scales freely ([1607.03474.txt](1607.03474.txt); [1611.01462.txt](1611.01462.txt)).
4. **Parameter counts are inconsistently reported.** Several entries (74.3, 78.4, 78.9, 87.38, 138.4) lack parameter counts in the supplied material, limiting scale-normalized comparison.
5. **The VD-LSTM+REAL entry is the weakest-evidence row.** Its context suggests a smaller-model regime, and it should not be read as a direct competitor to the 58.3–78.9 cluster ([1611.01462.txt](1611.01462.txt)).

## Excluded Results

Several excellent numbers were deliberately excluded because they violate the query's constraints. Model-averaging results over 2, 5, 10, and 38 regularized LSTMs (77.0, 73.3, 72.0, 73.6, 69.5, 68.7) are ensembles ([1409.2329_note.txt](1409.2329_note.txt)); 10 Variational LSTMs with MC dropout reach 68.7, also an ensemble ([1512.05287_note.txt](1512.05287_note.txt)). Cache/pointer methods appear only as baseline labels, such as Pointer Sentinel-LSTM in the NAS comparison, and cache appears as a baseline in RNN+LDA+KN-5+Cache at 92.0 ([1611.01578_note.txt](1611.01578_note.txt); [1611.01462.txt](1611.01462.txt)). No paper in the supplied material reports a dynamic evaluation or fine-tuning PTB result for its own model.

## Conclusion

Across the provided papers, the lowest single-model word-level Penn Treebank test perplexity obtained **without dynamic evaluation, cache or pointer augmentation, ensembling, or fine-tuning is 58.3**, reported by *On the State of the Art of Evaluation in Neural Language Models* for a 4-layer, 24M-parameter LSTM ([1707.05589_note.txt](1707.05589_note.txt)). The complete ranking is 58.3, 62.4, 65.4, 73.4, 74.3, 78.4, 78.9, 87.38, and 138.4. Readers should note that the comparison is drawn from heterogeneous evaluation regimes, and that the two most recent sources—the 58.3 and 62.4 results—also happen to be the most explicitly controlled for fair single-model comparison. Based on the supplied evidence, the 58.3 figure is the defensible answer to the query.

## References

- 1409.2329. (2014). *Regularized LSTM and model averaging on Penn Treebank* [Source note: 1409.2329_note.txt].
- 1508.06615. (2015). *Character-aware neural language models* [Source note: 1508.06615_note.txt].
- 1512.05287. (2015). *Variational LSTM with MC dropout* [Source note: 1512.05287_note.txt; table extract: 1512.05287.txt].
- 1607.03474. (2016). *Variational RHN with weight tying* [Source note: 1607.03474_note.txt; text extract: 1607.03474.txt].
- 1608.05859. (2016). *Using the output embedding to improve language models* [Source note: 1608.05859_note.txt].
- 1611.01462. (2016). *VD-LSTM and variants on Penn Treebank* [Table extract: 1611.01462.txt].
- 1611.01578. (2017). *Neural architecture search for language modelling* [Source note: 1611.01578_note.txt].
- 1706.02222. (2017). *GRURNTN and LSTMRNTN on Penn Treebank* [Source note: 1706.02222_note.txt].
- 1707.05589. (2017). *On the state of the art of evaluation in neural language models* [Source note: 1707.05589_note.txt].