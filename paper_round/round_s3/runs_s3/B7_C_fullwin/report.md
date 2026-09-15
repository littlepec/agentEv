# Test Set Size in Stahlberg and Byrne's Study of NMT Search Errors and Model Errors

## Overview and Direct Answer

The question of test set size is answered explicitly and unambiguously in the source material. In the study "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the University of Cambridge, the entire English–German WMT news-test2015 test set contains **2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper states this figure as a count of sentences, not tokens, documents, or parallel segments, and reports it before any subset selection takes place ([third-party research note](https://arxiv.org/abs/1908.10090)). This number is the full test set size that anchors the paper's main experimental claims, and it is the figure that should be quoted whenever the study's headline results on search errors and empty translations are discussed.

The same size is reported in the paper's abstract, which describes the use of exact search "to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Section 3 of the paper then makes the count explicit: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The convergence of the abstract's description of the full test set and Section 3's parenthetical count of 2,169 sentences establishes the full test set size as 2,169 sentences without ambiguity.

## Corpus Identity and Language Pair

Two dimensions of the test set's identity are relevant to interpreting the size correctly. First, the language pair is **English–German**, and the corpus is a **news test set** ([third-party research note](https://arxiv.org/abs/1908.10090)). Second, the test set is identified as the **WMT news-test2015** set — that is, the news translation test set released in connection with the 2015 Workshop on Statistical Machine Translation, referred to in the abstract as the "WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

An important distinction that emerges from the source material is that the *test* data is drawn from WMT15, while the *training* data is drawn from WMT18: the Transformer base model was "trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The test set size of 2,169 sentences therefore refers to WMT15 evaluation data, not to any WMT18 test set. Pre-processing included joint subword segmentation using byte pair encoding with 32K merges, and the reported BLEU scores are cased ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Full Test Set Versus Subsets: A Critical Distinction

The most consequential nuance in answering the test set size question is that the paper employs **two different scopes of evaluation**. The main, unconstrained exact inference experiments use the complete test set of 2,169 sentences. The later, length-constrained exact search experiments, by contrast, use only fractions of that test set, deliberately restricted to keep runtimes manageable ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper explains the rationale for the restriction directly: "Constraining search that way increases the run time as the γ-bounds are lower. Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A further constraint is documented in a footnote: the authors "stopped decoding if the decoder took longer than a day for a single sentence on a single CPU," while noting that unconstrained exact search is much faster and needs no maximum execution time limits ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The table below summarizes how the test set is used across the paper's experimental sections.

| Paper section | Test data scope | Reported size | Citation |
|---|---|---|---|
| Section 3: Results without length constraints | Entire English–German WMT news-test2015 test set | 2,169 sentences | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Section 4: Minimum-length constraint of 0.25 × source length (Figure 5) | Subset of the test set | 73.0% of the test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Section 4: Exact search constrained to Beam-10 or reference length (Table 3) | Subset of the test set | 48.3% of the test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Section 4: Length normalization comparison (Table 4) | Subset of the test set | 48.3% of the test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |

The percentage figures are reported as percentages rather than sentence counts in the paper itself ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). For readers who wish to convert them, applying the percentages to the stated full test set size yields approximately 1,583 sentences for the 73.0% subset and approximately 1,048 sentences for the 48.3% subset. These derived counts are arithmetic implications of the reported percentages and the reported full test set size of 2,169 sentences; they are not numbers stated verbatim in the paper and should be labeled as derived if cited.

## Why the Full Test Set Size of 2,169 Sentences Matters

The size figure of 2,169 sentences is significant for several reasons that the paper's own framing supports. First, the study's central empirical claim concerns the *frequency* of search errors and empty translations. The paper reports that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation," and Tab. 1 reports an exact figure of 51.8% of sentences for which the empty translation receives the global best model score ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Any percentage of this kind is only interpretable relative to the number of sentences evaluated, which is why the full test set size of 2,169 sentences is essential context. A claim that roughly half of evaluated sentences have an empty global-best translation is anchored to a test set of 2,169 sentences, not to a subset.

Second, the paper's comparison between beam search behavior at different beam sizes is quantified over the same full test set. Beam-10 yields 15.9% fewer search errors (absolute) than greedy decoding, reported as 57.68% versus 73.58%, while Beam-100 still produces 53.62% search errors "despite being 10 times slower than beam-10" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These percentages derive from the full 2,169-sentence evaluation.

Third, the paper generalizes its findings beyond the Transformer base architecture by reporting results for several models. Table 2 gives Beam-10 accuracy and exact-search results for an LSTM, a SliceNet convolutional model, Transformer-Base, and Transformer-Big, with empty-translation rates of 47.7%, 41.2%, 51.8%, and 25.8% respectively under exact search ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Although the table does not restate the test set size, it is part of the same experimental program, and the paper's framing indicates that the problem of search errors and empty translations "is not specific to the Transformer base model and also occur with other architectures" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Headline Results Reported on the Full 2,169-Sentence Test Set

The principal results of the study, presented in Table 1, are summarized below. These are the figures computed on the entire test set of 2,169 sentences.

| Search method | BLEU | Length ratio | Search errors | Empty translations |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

Table 1 data as reported in Stahlberg and Byrne ([2019](https://arxiv.org/abs/1908.10090)).

The interpretation the authors give is that greedy and beam search achieve reasonable BLEU scores "but rely on a high number of search errors to not be affected by a serious NMT model error," namely that the empty hypothesis frequently attains the global best model score ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The BLEU of 2.1 and length ratio of 0.06 under exact search illustrate why: without search errors, the model's preferred outputs collapse toward empty translations, producing a dramatic degradation in both metrics ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## An Important Caveat on Comparing Section 3 and Section 4 Results

A reader examining the paper's tables should note that BLEU figures in Section 3 and Section 4 are not directly comparable, because they are computed on different portions of the test set. For example, Beam-10 is reported at 30.3 BLEU in Table 1 on the full 2,169-sentence test set, whereas Beam-10 is reported at 37.0 BLEU in Table 3, where the experiment was conducted on 48.3% of the test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The same applies to Table 4, also run on 48.3% of the test set, where Beam-10 is reported at 37.0 BLEU without length normalization and 36.3 BLEU with length normalization ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Consequently, the single most defensible statement about test set size is that the full test set comprises 2,169 sentences, and that the length-constrained analyses operate on explicitly declared subsets of that full test set.

The length-constrained results themselves remain informative within their subsets. Exact search constrained to the length of the best Beam-10 hypothesis does not improve over beam search (37.0 BLEU in both cases), suggesting that search errors at that fixed length are not significant enough to affect BLEU, whereas the oracle experiment constraining exact search to the reference length improves BLEU by 0.9 points, from 37.0 to 37.9 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Similarly, under length normalization, exact search achieves 36.4 BLEU and a length ratio of 1.03, but still fails to match the best Beam-10 score ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Reliability and Prioritization of Sources

Two sources inform this report. The primary source is the paper itself, by Stahlberg and Byrne, hosted as arXiv preprint 1908.10090 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This is the authoritative source for the 2,169-sentence figure, and it directly reports the count in Section 3 with the parenthetical "(2,169 sentences)." The secondary source is a third-party research note that compiles answers to frequently asked questions about the paper, including the test set size, the language pair, and the distinction between the full test set and the subsets used in the length-constrained experiments ([third-party research note](https://arxiv.org/abs/1908.10090)). The note is consistent with the primary source on every point: it states that the entire English–German WMT news-test2015 test set contains 2,169 sentences, that this full size is reported before any subset selection, that one length-constrained experiment used 73.0% of the test set, and that other experiments used 48.3% ([third-party research note](https://arxiv.org/abs/1908.10090)). Because the note is derivative, this report privileges the primary paper wherever the two overlap, while using the note to corroborate the framing that the 2,169-sentence figure applies to the full test set and that subset percentages apply to the length-constrained analyses only.

## Conclusion

The test set size in Stahlberg and Byrne's study is **2,169 sentences**, corresponding to the entire English–German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This is the full test set size reported before any subset selection, and it supports the paper's primary findings on search errors and empty translations: 73.6%, 57.7%, and 0.0% search errors for greedy, Beam-10, and exact search respectively, and 51.8% empty translations under exact search ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The length-constrained follow-up experiments, by contrast, were run on subsets equal to 73.0% and 48.3% of that same test set, so their BLEU figures are not directly comparable with the full-test-set results ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). For any discussion of the study's headline claims, the correct test set size to cite is 2,169 sentences.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv preprint arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* (n.d.). Research note summarizing Stahlberg and Byrne's study, addressing NMT search errors, model errors, and test set size. https://arxiv.org/abs/1908.10090