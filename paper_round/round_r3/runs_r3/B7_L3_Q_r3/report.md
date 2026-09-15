# Test Set Size in Stahlberg and Byrne's *On NMT Search Errors and Model Errors: Cat Got Your Tongue?*

## Introduction and Scope of the Query

This report answers the question: **What is the test set size** used in Stahlberg and Byrne's study of search errors and model errors in neural machine translation (NMT)? The query is narrow but methodologically important, because the paper's central claims — that beam search fails to find the global best model score for more than half of sentences, and that the empty translation frequently receives the global best model score — are empirical claims whose credibility depends on the size and composition of the evaluation set on which they rest ([Stahlberg & Byrne, n.d.](document_1.txt)). The evidence base for this report consists of two documents: the paper itself (`document_1.txt`) and a third-party research note summarizing its test-set reporting (`document_2.txt`).

## The Direct Answer

The full test set used in the paper's main experiments contains **2,169 sentences**. Specifically, the paper states that all experiments in its "Results without Length Constraints" section were "conducted on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, n.d.](document_1.txt)). The abstract of the same paper reiterates the scope, describing the use of exact search "under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, n.d.](document_1.txt)). The third-party research note confirms this figure independently, stating that "the entire German-English WMT news-test2015 test set contains 2,169 sentences" and that "the paper states the test set size as a number of sentences" ([Research Note, n.d.](document_2.txt)).

The unit of measurement is therefore **sentences**, not tokens, documents, or segments. This distinction matters for reproducibility: a reader attempting to reconstruct the study would need 2,169 source-target sentence pairs drawn from the WMT 2015 news test set ([Research Note, n.d.](document_2.txt)).

## Provenance of the Figure and the Full-Test-Set Baseline

The research note emphasizes a chronologically important point: the 2,169-sentence figure "is reported before any subset selection" ([Research Note, n.d.](document_2.txt)). In other words, 2,169 is the reference or baseline size of the complete test set, and all subsequently reported percentages or subset sizes are fractions of this whole. The note further explains that "the paper's use of the entire test set in that section establishes the full test set size for the reported exact inference results" ([Research Note, n.d.](document_2.txt)). This framing is useful because it prevents a common misreading in which a percentage figure reported in a results table is mistaken for the size of the evaluation set.

The full set of 2,169 sentences supports the paper's headline comparisons between greedy decoding, beam search with varying beam sizes, and exact inference ([Stahlberg & Byrne, n.d.](document_1.txt)). According to the paper's own summary of results, greedy decoding achieved 29.3 BLEU with 73.6% search errors, Beam-10 achieved 30.3 BLEU with 57.7% search errors, and exact search achieved 2.1 BLEU with 0.0% search errors while assigning the global best score to the empty translation for 51.8% of sentences ([Stahlberg & Byrne, n.d.](document_1.txt)). These figures were computed over the full 2,169-sentence set, which makes the full set the evidentiary anchor for the paper's most provocative conclusions.

## Language Pair, Domain, and Naming Consistency

The test set is a **news** test set from the WMT 2015 evaluation campaign ([Stahlberg & Byrne, n.d.](document_1.txt)). The paper describes the evaluation data as "English-German WMT news-test2015," while the research note describes the same data as "German-English WMT news-test2015" ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). This is a minor inconsistency in direction labeling rather than a discrepancy in size: both documents agree on the WMT 2015 news test set and on the 2,169-sentence count. Either way, the language pair is the same bilingual pairing, and the domain is news text ([Research Note, n.d.](document_2.txt)).

Contextual details surrounding the test set are also documented. The paper reports that preprocessing followed Stahlberg et al. (2018a) and "includes joint subword segmentation using byte pair encoding (Sennrich et al. 2016) with 32K merges," that BLEU scores are cased, and that the Transformer base model was trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl ([Stahlberg & Byrne, n.d.](document_1.txt)). An open-source implementation of the exact inference scheme is available in the SGNMT decoder ([Stahlberg & Byrne, n.d.](document_1.txt)). These details establish that the 2,169-sentence test set was evaluated under a fixed, reproducible preprocessing and modeling pipeline.

## Subset Sizes Used in the Length-Constrained Experiments

A crucial nuance in answering "what is the test set size" is that the paper does **not** use 2,169 sentences for every experiment. The length-constrained exact search experiments use only a subset. The paper states: "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, n.d.](document_1.txt)). The research note corroborates this, noting that "the length-constrained exact search experiments use only a subset of the test set" ([Research Note, n.d.](document_2.txt)).

The two reported subset proportions are 73.0% and 48.3% of the test set ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). The table below organizes the reported figures and, where useful, the arithmetic implied by applying the reported proportions to the 2,169-sentence baseline.

| Evaluation condition | Reported proportion | Reported base size | Implied sentence count (computed) |
|---|---|---|---|
| Main results without length constraints | 100% of test set | 2,169 sentences | 2,169 |
| Length-constrained experiment (Fig. 5 context) | 73.0% of test set | 2,169 sentences | ≈1,583 |
| Exact search under length constraints (Tables 3 and 4) | 48.3% of test set | 2,169 sentences | ≈1,048 |

The implied sentence counts in the final column are arithmetic derivations performed for this report, not figures stated in the source documents. The source documents explicitly state only the proportions (73.0% and 48.3%) and the full-set size (2,169 sentences) ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). The research note is explicit that "these subset experiments are distinct from the full test set size of 2,169 sentences" ([Research Note, n.d.](document_2.txt)).

The operational reason for subsetting is documented: constraining search increases runtime because the γ-bounds are lower, and the authors "stopped decoding if the decoder took longer than a day for a single sentence on a single CPU" ([Stahlberg & Byrne, n.d.](document_1.txt)). By contrast, "exact search without length constraints is much faster and does not need maximum execution time limits," which is why the unconstrained experiments could cover all 2,169 sentences ([Stahlberg & Byrne, n.d.](document_1.txt)).

## Why the Test Set Size Matters Methodologically

The test set size interacts directly with the paper's conclusions in three ways.

First, **statistical resolution**. Reporting search-error rates at the level of whole percentages across 2,169 sentences means each single sentence corresponds to roughly 0.05 percentage points. Differences such as Beam-10 yielding "15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%)" are therefore based on hundreds of individual sentence outcomes, not a handful ([Stahlberg & Byrne, n.d.](document_1.txt)). This strengthens the reliability of the aggregate claims about search-error frequency.

Second, **generalizability across architectures**. The paper reports results not only for the Transformer base model but also for a recurrent LSTM, a SliceNet convolutional model, and a Transformer Big system ([Stahlberg & Byrne, n.d.](document_1.txt)). The LSTM achieved 28.6 BLEU with 58.4% search errors and 47.7% empty global bests; SliceNet achieved 28.8 BLEU with 46.0% and 41.2% respectively; Transformer-Base achieved 30.3 BLEU with 57.7% and 51.8%; and the Transformer-Big model from the authors' WMT18 submission had 31.7 BLEU with 32.1% search errors and 25.8% empty translations ([Stahlberg & Byrne, n.d.](document_1.txt)). The fact that these architecture-level comparisons are anchored to the same 2,169-sentence benchmark is what enables the paper to claim that "the problems of search errors and empty translations are not specific to the Transformer base model" ([Stahlberg & Byrne, n.d.](document_1.txt)).

Third, **interpretation of length effects**. The paper reports that long source sentences are more affected by both search errors and empty global bests, with the global best translation being empty "for almost all sentences longer than 40 tokens" ([Stahlberg & Byrne, n.d.](document_1.txt)). Claims of this kind depend on the test set containing a sufficient number of long source sentences, which a 2,169-sentence news test set plausibly does. The subset experiments, being smaller, carry correspondingly weaker resolution — an important caveat when the paper's length-constrained results are cited ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)).

## Related Reporting Details That Frame the Size

Several other reported quantities are useful when contextualizing the 2,169-sentence figure. The paper notes that the search space is vast — for a vocabulary of 32,000 tokens there are more possible translations of 20 words or fewer than atoms in the observable universe (32,000²⁰ ≫ 10⁸²), so complete enumeration is impossible ([Stahlberg & Byrne, n.d.](document_1.txt)). It also reports that even a beam size of 100 "produces 53.62% search errors," and that Beam-100 improves search only slightly relative to Beam-10 despite being ten times slower ([Stahlberg & Byrne, n.d.](document_1.txt)). All of these failures were quantified on the 2,169-sentence test set.

## Limitations, Ambiguities, and Verification Notes

Three caveats should accompany the answer.

1. **OCR-derived numeric formatting.** The source text renders numbers with inserted spaces (for example, "2,1 6 9" and "5 1.8%"), reflecting extraction from a PDF ([Stahlberg & Byrne, n.d.](document_1.txt)). The figure 2,169 is nonetheless unambiguous across both documents.
2. **Direction-label inconsistency.** The paper labels the data English-German while the research note labels it German-English ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). This does not affect the size figure but should be noted by anyone citing the setup precisely.
3. **Single primary source.** The 2,169-sentence figure derives from one primary document, with the research note serving as a secondary corroboration rather than an independent measurement ([Research Note, n.d.](document_2.txt)). The note explicitly functions as a summary of the paper's reporting, so it does not constitute independent verification.

## Conclusion

Based on the available evidence, the test set size is **2,169 sentences**, drawn from the WMT 2015 news test set and used for the paper's main unconstrained exact-inference experiments ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). This full size is the reference point from which the length-constrained experiments select subsets of 73.0% and 48.3% ([Stahlberg & Byrne, n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). Anyone citing the paper's headline findings — 57.7% search errors under Beam-10, 51.8% empty global best translations, and 53.62% search errors even at beam size 100 — is citing conclusions computed over those full 2,169 sentences ([Stahlberg & Byrne, n.d.](document_1.txt)). Anyone citing the length-constrained findings, by contrast, is citing results obtained on a smaller fraction of that set and should state the reduced scope explicitly ([Research Note, n.d.](document_2.txt)).

## References

Research note: On NMT search errors and model errors: Cat got your tongue? (n.d.). [document_2.txt](document_2.txt)

Stahlberg, F., & Byrne, B. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* University of Cambridge, Department of Engineering. [document_1.txt](document_1.txt)