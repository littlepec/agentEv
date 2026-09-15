# Test Set Size in "On NMT Search Errors and Model Errors: Cat Got Your Tongue?"

## 1. Purpose and Scope of the Query

This report addresses a single, precisely specified factual question: **what is the test set size used in the experiments reported by Stahlberg and Byrne in their study of search errors and model errors in neural machine translation (NMT)?** The question is narrower than it may first appear. The source material contains two competing figures for the same underlying test set, and a faithful answer therefore requires more than simply extracting a number. It requires identifying which figure is supported by the primary evidence, explaining why the competing figure appears in the corpus, and clarifying that the study uses a full test set for one block of experiments and smaller subsets for another ([Stahlberg & Byrne, 2019](document_1.txt)).

A second, related distinction must be maintained throughout: the *full* test set size and the *subset* sizes used in the length-constrained experiments are different quantities. Conflating them would misstate the paper's methodology, because the authors explicitly report subset selection to control decoding runtime ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note](document_2.txt)).

## 2. The Primary Answer: 2,169 Sentences

### 2.1 Where the Figure Appears in the Primary Source

The primary source — the paper's own text — states the test set size directly in the description of the experimental setup for the first block of results. The relevant sentence reads that the authors "conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (**2,169 sentences**) with a Transformer-base (Vaswani et al., 2017) model trained with Tensor2Tensor (Vaswani et al., 2018) on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](document_1.txt)).

This statement has several properties that make it the strongest available evidence for the test set size:

- **It is internally explicit.** The figure is attached to the phrase "entire … test set," so it describes the full set, not a subset.
- **It is contextualised.** The sentence also identifies the language pair (English-German), the benchmark (WMT news-test2015), the model architecture (Transformer-base), the training framework (Tensor2Tensor), and the training data (parallel WMT18 data excluding ParaCrawl).
- **It is attached to the paper's headline results.** The same section contains the main comparison between greedy decoding, beam search, and exact inference, culminating in Table 1, where the authors report BLEU scores, search error rates, and empty-translation rates for each decoding strategy ([Stahlberg & Byrne, 2019](document_1.txt)).

### 2.2 Experimental Context Supporting the Figure

The number 2,169 is embedded in a coherent experimental narrative. The authors prepared the data with joint subword segmentation using byte pair encoding (BPE) with 32K merges (Sennrich et al., 2016), and they report BLEU scores using a standard reporting framework ([Stahlberg & Byrne, 2019](document_1.txt)). The exact inference procedure is implemented in the SGNMT decoder, described as an open-source implementation of the exact inference scheme ([Stahlberg & Byrne, 2019](document_1.txt)).

The results themselves are reported with percentages that align with a test set of this magnitude. In Table 1, greedy decoding achieves a BLEU score of 29.3 with a length ratio of 1.02, 73.6% search errors, and 0.0% empty translations. Beam search with beam size 10 (Beam-10) achieves 30.3 BLEU, a length ratio of 1.00, 57.7% search errors, and 0.0% empty translations. Exact search achieves 2.1 BLEU, a length ratio of 0.06, 0.0% search errors, and 51.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)).

If these percentages are applied arithmetically to a test set of 2,169 sentences (a derivation, not a figure stated in the paper), the following approximate counts result:

| Decoding strategy | Search errors (%) | Derived sentence count (of 2,169) | Empty global best (%) | Derived sentence count (of 2,169) |
|---|---|---|---|---|
| Greedy | 73.6% | ≈ 1,596 | 0.0% | 0 |
| Beam-10 | 57.7% | ≈ 1,251 | 0.0% | 0 |
| Exact | 0.0% | 0 | 51.8% | ≈ 1,124 |

These derived counts are illustrative only; they are computed from the reported percentages and the stated test set size, and they are presented here to show that the reported rates are plausibly grounded in a corpus of 2,169 sentences rather than a substantially larger one ([Stahlberg & Byrne, 2019](document_1.txt)).

## 3. The Conflicting Third-Party Claim: 3,003 Sentences

### 3.1 What the Third-Party Note Asserts

The corpus also contains a third-party research note that addresses precisely this question among its listed "key questions," including "English German news test set size neural machine translation" and "Stahlberg Byrne NMT search errors test set size" ([Third-party research note](document_2.txt)). The note asserts, repeatedly and in several paraphrases, that "the paper's main experiments use the entire English-German WMT news-test2015 test set of **3,003 sentences**," that the paper "reports this size in its experimental setup," that the "full test set size of 3,003 sentences is reported before any subset selection," and that "the paper's use of the entire test set in that section establishes the full test set size for the reported exact inference results" ([Third-party research note](document_2.txt)).

The note also correctly observes the second half of the methodology: that the length-constrained exact search experiments use only a subset of the test set, with one experiment using 73.0% of the test set and other experiments using 48.3%, and that these subset experiments are "distinct from the full test set size of 3,003 sentences" ([Third-party research note](document_2.txt)).

### 3.2 Why the Claim Is Not Adopted Here

Two considerations lead to the conclusion that 2,169, not 3,003, is the correct answer to the query.

First, **the primary source takes precedence over a secondary summary**. The figure 2,169 appears inside the paper's own experimental setup sentence, whereas 3,003 appears only in a third-party note that paraphrases the paper without quoting it ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note](document_2.txt)). Where a secondary account conflicts with a verbatim statement in the primary document, the primary document should be preferred.

Second, and more decisively, **the figure 3,003 does not appear anywhere in the primary text supplied**. The primary source contains a different, clearly labelled numeric string — "(2,169 sentences)" — attached to the identical descriptor, "the entire English-German WMT news-test2015 test set" ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party note's claim that the paper "reports this size in its experimental setup" is therefore unsupported by the document it purports to summarise. Since the secondary note provides no page, quotation, or other internal evidence to justify its figure, its assertion cannot displace the explicit statement in the source paper.

It should be acknowledged that the provided primary text is a degraded optical-character-recognition rendering, with frequent token-joining and garbled passages (for example, "news-test2015testset(2,169sentences)"). This degradation affects formatting and readability, but the numeral itself is legible and unambiguously located within the experimental setup sentence. The same degraded rendering does not contain the string "3,003." The most parsimonious reading, therefore, is that the third-party note is mistaken on this point — likely through conflation with a different benchmark or test-set version — while its treatment of the subset structure is consistent with the paper.

## 4. Reconciling the Two Figures

The following table summarises the competing claims and the evidence supporting each.

| Source type | Claimed full test set size | Evidence quality | Assessment |
|---|---|---|---|
| Primary paper (Stahlberg & Byrne, 2019) | 2,169 sentences | Explicit figure in the methodological sentence describing the "entire" test set; contextualised with language pair, benchmark, model, and training data | Adopted |
| Third-party research note | 3,003 sentences | Repeated assertion; states the paper "reports this size in its experimental setup," but the figure is absent from the primary text | Not adopted |

The practical conclusion is straightforward. **The test set size is 2,169 sentences**: the entire English-German WMT news-test2015 test set, used for all experiments in the results-without-length-constraints section, which is the section containing the paper's central exact-inference comparisons ([Stahlberg & Byrne, 2019](document_1.txt)).

## 5. Test Set Subsets Used in Length-Constrained Experiments

The distinction between the full test set and its subsets is important enough to warrant separate treatment. The authors state that all results in the results-with-length-constraints section "are conducted on only a subset of the test set to keep the runtime under control," and they explain the reason: constraining search increases runtime because the pruning bounds are lower ([Stahlberg & Byrne, 2019](document_1.txt)). They also report a hard practical limit — decoding was stopped if the decoder took longer than a day for a single sentence on a single CPU — and note that exact search without length constraints is much faster and does not require maximum execution time limits ([Stahlberg & Byrne, 2019](document_1.txt)).

| Experiment block | Portion of test set used | Reported figure | Purpose |
|---|---|---|---|
| Results without length constraints | Entire test set: 2,169 sentences | Table 1; Figures 1–4 | Main exact-inference comparison of greedy, Beam-10, Beam-100, exact |
| Minimum-length constraint (0.25 × source length) | 73.0% of the test set (≈ 1,583 sentences, derived) | Figure 5 | Test whether excluding the empty translation mitigates the length deficiency |
| Length-constrained exact search | 48.3% of the test set (≈ 1,047 sentences, derived) | Table 3; Table 4 | Oracle-length and Beam-10-length comparisons; length normalisation |

The 73.0% and 48.3% figures are reported by the paper, and the third-party note independently reproduces them in its description of the subset methodology ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note](document_2.txt)). The absolute sentence counts in parentheses are derived by multiplying the stated percentages by 2,169 and are not reported as such in the source.

The subset experiments produced substantive findings. Under the minimum translation length constraint of 0.25 times the source sentence length, the empty translation was excluded from the search space; the problem was mitigated only slightly, with a residual peak remaining in the (0.3, 0.5] length-ratio cluster, suggesting that the problem cannot be fixed with a length constraint alone ([Stahlberg & Byrne, 2019](document_1.txt)). In Table 3, Beam-10 yields 37.0 BLEU at a ratio of 1.00; exact search constrained to the Beam-10 hypothesis length yields 37.0 BLEU at a ratio of 1.00; exact search constrained to the reference length yields 37.9 BLEU at a ratio of 1.01 — an improvement of 0.9 BLEU points over beam search, consistent with the paper's claim that any search errors between the beam search score and the global best score for that length are insignificant enough not to affect BLEU ([Stahlberg & Byrne, 2019](document_1.txt)).

In Table 4, without length normalisation, Beam-30 obtains 37.0 BLEU at ratio 1.00, Beam-10 obtains 36.7 at 0.98, and exact search obtains 27.2 at 0.74. With length normalisation, Beam-30 obtains 36.3 at 1.03, Beam-10 obtains 36.3 at 1.04, and exact search obtains 36.4 at 1.03 ([Stahlberg & Byrne, 2019](document_1.txt)). The authors interpret these results as evidence that length normalisation fixes translation length but does not allow exact search to match the best BLEU score under Beam-10, and therefore does not repair the underlying modelling problem ([Stahlberg & Byrne, 2019](document_1.txt)).

## 6. Why the Test Set Size Matters for Interpreting the Findings

The test set size is not a peripheral methodological detail; it determines how the headline findings should be read. The paper's central empirical claim is that beam search fails to find the global best model score for more than half of the sentences, with Beam-10 producing 57.7% search errors and even a beam size of 100 producing 53.62% search errors ([Stahlberg & Byrne, 2019](document_1.txt)). A parallel claim is that for 51.8% of sentences the model assigns the global best model score to the empty translation — a single end-of-sentence token — causing a dramatic drop in length ratio and BLEU when search errors are removed ([Stahlberg & Byrne, 2019](document_1.txt)).

These are per-sentence rates, so the denominator matters. On a test set of 2,169 sentences, a rate of 51.8% corresponds to roughly 1,124 sentences for which the empty translation receives the global best model score (derived). The authors further report that long source sentences are disproportionately affected: the global best translation is empty for almost all sentences longer than 40 tokens ([Stahlberg & Byrne, 2019](document_1.txt)). Figure 4 plots search errors under Beam-10 and empty global bests as a function of source sentence length, showing both effects rising with length ([Stahlberg & Byrne, 2019](document_1.txt)).

The authors also demonstrate that these problems are not specific to the Transformer-base architecture. Table 2 reports, for Beam-10 decoding, an LSTM system at 28.6 BLEU with 58.4% search errors and 47.7% empty translations, a convolutional SliceNet at 28.8 BLEU with 46.0% search errors and 41.2% empty translations, Transformer-Base at 30.3 BLEU with 57.7% search errors and 51.8% empty translations, and Transformer-Big at 31.7 BLEU with 32.1% search errors and 25.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). The fact that even a highly optimised Transformer-Big system from a WMT18 shared-task submission produces 25.8% empty translations reinforces the paper's conclusion that the length bias is a modelling problem rather than an artefact confined to one configuration ([Stahlberg & Byrne, 2019](document_1.txt)).

## 7. Conclusion and Assessment

The test set size used in the paper's main experiments is **2,169 sentences**: the entire English-German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](document_1.txt)). This figure is stated explicitly in the paper's own experimental setup and governs all results in the without-length-constraints section, including the headline Table 1 comparison and Figures 1 through 4. The alternative figure of 3,003 sentences, advanced by the third-party research note, is not supported by the primary text and is therefore not adopted here ([Third-party research note](document_2.txt)).

Two qualifications should accompany this answer. First, the length-constrained experiments in the paper's fourth section do not use the full test set; they use subsets of 73.0% and 48.3% of it, chosen to keep runtime under control because constrained search lowers the pruning bounds ([Stahlberg & Byrne, 2019](document_1.txt)). Any statement about "the test set size" in this paper should therefore specify which experiment block is meant.

Second, the discrepancy between the two documents in the corpus is itself informative: it demonstrates why primary-source verification matters when a secondary account supplies a specific numerical figure without a quotation or locator. The primary paper's numeral is legible, contextualised, and embedded in the methodological sentence that defines the scope of the main results, whereas the secondary note's numeral is unsupported by the document it summarises. On the balance of the available evidence, 2,169 sentences is the defensible answer.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv preprint arXiv:1908.10090. ([document_1.txt](document_1.txt))

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* (n.d.). ([document_2.txt](document_2.txt))