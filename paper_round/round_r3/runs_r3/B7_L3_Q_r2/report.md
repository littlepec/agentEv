# What Is the Test Set Size? A Detailed Report on Stahlberg and Byrne's NMT Search-Error Experiments

## Direct Answer to the Query

The test set size reported in the paper *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* is **2,169 sentences**. This is the size of the full English–German WMT news-test2015 (WMT15) test set, and it is the figure the paper reports before any subset selection is applied. The primary source states explicitly: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A third-party research note on the same paper independently reports the identical number: "The entire German-English WMT news-test2015 test set contains 2,169 sentences" ([Third-party research note](#references)).

Two additional, smaller figures are relevant because the paper's later experiments do **not** use the full test set. The length-constrained exact-search experiments are run on subsets: one experiment uses **48.3%** of the test set, and another uses **73.0%** of the test set ([Third-party research note](#references)). These subsets are distinct from the headline figure of 2,169 sentences and must not be confused with it.

## The Headline Figure: 2,169 Sentences

### Unit of Measurement and Reporting Convention

An important methodological detail is that the paper reports test set size as a **number of sentences**, not as a number of tokens, documents, or parallel segments in any other unit ([Third-party research note](#references)). The source text contains the phrase "English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The spaced-out digits are an artifact of the PDF-to-text conversion of the original LaTeX-generated document, in which "2,169" has been rendered with intervening spaces. Read together with the subsequent statement that all experiments in the relevant section were conducted on the "entire" test set, the intended value is unambiguous: 2,169 sentences.

### Corpus Identification

The test set is drawn from the **WMT news translation task**, specifically the **news-test2015** split associated with the WMT15 evaluation campaign ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper describes its experimental setup as follows: a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl, using joint subword segmentation with byte pair encoding (BPE) and 32K merge operations, with cased BLEU reported as the evaluation metric ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The test set size of 2,169 sentences therefore refers to the evaluation corpus only; it is not a statement about the size of the training data, which was drawn from WMT18 material.

### Reported Before Subset Selection

The third-party note emphasizes a point that matters for interpreting the number: "This full test set size of 2,169 sentences is reported before any subset selection" ([Third-party research note](#references)). In other words, 2,169 is the *maximum* evaluation sample available to the authors, and every percentage figure reported in the paper's main results tables is defined relative to that full sample unless a subset is explicitly declared.

## A Minor Reporting Discrepancy: Language Direction

The paper and the third-party note differ slightly in how they name the language pair. The abstract of the paper refers to "the entire WMT15 **English-German** test set," and Section 3 repeats "**English-German** WMT news-test2015 test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note, by contrast, describes the corpus as "**German-English**" ([Third-party research note](#references)).

This discrepancy does not affect the test set size, which is 2,169 sentences under either naming convention. It is, however, a reminder that in translation-studies literature the ordering of language names is not always used consistently to distinguish source from target, and that downstream readers should treat the language-pair label as a naming convention rather than as a reliable indicator of translation direction. For the purposes of the query at hand, the relevant and consistent fact is the sample size: 2,169 sentences.

## Which Experiments Use the Full Test Set

The paper divides its empirical work into two blocks, and the test-set coverage differs between them.

### Section 3: Results Without Length Constraints

All experiments in this section are conducted on the **entire** test set of 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This block contains the paper's principal findings, including:

- Greedy decoding: 29.3 BLEU, a length ratio of 1.02, 73.6% search errors, and 0.0% empty translations.
- Beam-10: 30.3 BLEU, a length ratio of 1.00, 57.7% search errors, and 0.0% empty translations.
- Exact search: 2.1 BLEU, a length ratio of 0.06, 0.0% search errors, and 51.8% empty translations.

These values appear in Table 1 of the paper ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because the table is stated to cover the full test set, each percentage can be converted into an approximate sentence count, as shown in the derived table below.

### Table 2: Cross-Architecture Comparison

Table 2 extends the analysis beyond the Transformer base model to a recurrent LSTM, a SliceNet convolutional model, the Transformer base, and a Transformer Big model from the authors' WMT18 shared-task submission. The reported entries include a BLEU score, a search-error percentage, and an empty-translation percentage for each architecture — for example, 30.3 BLEU / 57.7% / 51.8% for Transformer-Base and 31.7 BLEU / 32.1% / 25.8% for Transformer-Big ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Since the paper states that the experiments in the corresponding results block are conducted on the entire test set, these figures are best interpreted as being anchored to the same 2,169-sentence sample.

### Figure-Based Analyses

Figure 1 (BLEU against the percentage of search errors), Figure 2 (search errors by beam size), Figure 3 (histogram of target/source length ratios), and Figure 4 (search errors and empty global bests as a function of source sentence length) are all presented in the context of the unconstrained-results block and therefore draw on the full test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Figure 4's finding that "the global best translation is empty for almost all sentences longer than 40 tokens" is thus a statement about the full 2,169-sentence evaluation sample.

## Subsets Used for Length-Constrained Experiments

The second experimental block — "Results with Length Constraints" (Section 4) — deliberately abandons the full test set. The reason is computational: constraining search to particular translation lengths lowers the γ-bounds used for pruning, which increases run time ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper states: "Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note records the same design decision and the specific coverage shares: one experiment uses **73.0%** of the test set, and other experiments use **48.3%** ([Third-party research note](#references)).

The 48.3% figure is attached to the captions of Table 3 ("Exact search under length constraints. Experiment conducted on 48.3% of the test set") and Table 4 ("Length normalization fixes translation lengths, but prevents exact search from matching the BLEU score of Beam-10. Experiment conducted on 48.3% of the test set") ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The 73.0% figure appears in connection with the minimum-translation-length experiment (translation longer than 0.25 times the source sentence length) that underlies the Figure 5 histogram ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Table: Test Set Coverage by Experiment Block

| Experiment block | Coverage | Reported share | Approximate sentence count (derived) | Reason for coverage |
|---|---|---|---|---|
| Section 3, main results (Tables 1–2, Figures 1–4) | Entire test set | 100% | 2,169 | Exact search without length constraints is fast; full-sample inference intended |
| Figure 5, minimum-length-constrained search (0.25 × source length) | Subset | 73.0% | ≈ 1,583 | Runtime control under lower γ-bounds |
| Tables 3–4, length-constrained and length-normalized exact search | Subset | 48.3% | ≈ 1,048 | Runtime control under lower γ-bounds |

Note: the sentence counts in the fourth column are derived by multiplying 2,169 by the reported coverage share; they are approximations for interpretive purposes and are not stated in the source. The paper also reports that decoding was halted "if the decoder took longer than a day for a single sentence on a single CPU" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)), which explains why the length-constrained work required sampling.

## Derived Sentence Counts and Their Interpretive Significance

Because the main results are anchored to a known denominator of 2,169 sentences, the paper's percentages can be converted into approximate sentence counts. The following table presents such conversions for the headline figures.

| Condition | Reported metric | Percentage | Approximate sentences (of 2,169) |
|---|---|---|---|
| Greedy | Search errors | 73.6% | ≈ 1,596 |
| Beam-10 | Search errors | 57.7% | ≈ 1,251 |
| Beam-100 | Search errors | 53.62% | ≈ 1,163 |
| Exact search | Empty global best | 51.8% | ≈ 1,124 |

The underlying percentages are reported in Table 1 and in the surrounding text of the paper ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)); the sentence counts are derived from the 2,169-sentence denominator. The conversion is useful because it demonstrates the scale of the phenomenon the authors describe. The abstract's claim that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) corresponds to roughly 1,124 sentences whose globally optimal decoding under the model is the single end-of-sentence token. Similarly, the statement that Beam-10 "yields 15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) corresponds to a reduction of approximately 345 sentences in absolute terms.

A further statistical consideration reinforces the value of knowing the exact sample size. With n = 2,169 and a proportion near 0.5, the binomial standard error is approximately 1.07 percentage points (computed as √(0.25/2,169) ≈ 0.0107). This implies an approximate 95% confidence half-width of about ±2.1 percentage points around proportions near 50%, meaning that the difference between a reported 51.8% empty-translation rate and a 50% threshold is small relative to normal sampling variability, whereas the gap between 51.8% and the Beam-10 search-error rate of 57.7% is considerably larger than that margin. For the 48.3% subset (approximately 1,048 sentences), the corresponding standard error is about 1.55 percentage points, and the approximate 95% half-width is about ±3.0 percentage points — a reminder that results on the length-constrained subsets carry noticeably wider uncertainty than the full-sample results. These calculations are my own derivations from the reported sample sizes and are offered as interpretive context rather than as claims made in the source.

## Why the Test Set Size Matters for the Paper's Claims

The paper's central argument is quantitative: beam search on neural machine translation fails to find the global best model score "in most cases, even with a very large beam size of 100," and unconstrained NMT frequently prefers the empty translation ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Such claims are only interpretable against a known evaluation sample. The stated sample of 2,169 sentences establishes that the reported search-error and empty-translation rates are not artifacts of a small pilot evaluation, but describe a standard, widely recognised WMT test suite. It also establishes the boundary conditions of the paper's contribution: the exact inference procedure is "too slow for practical MT" and is used "for analysis purposes" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)), which is precisely why only the unconstrained setting could be run on the full 2,169-sentence set, and why the length-constrained analyses had to fall back on 73.0% and 48.3% subsets.

There is also a reproducibility dimension. The paper notes that an open-source implementation of the exact inference scheme is available in the SGNMT decoder through the `simplelendfs` and `simpledfs` decoding strategies ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Knowing that the reference evaluation uses the complete 2,169-sentence WMT news-test2015 set allows a future replication to reproduce the reported coverage exactly rather than guessing at the evaluation sample.

## Source Reliability and Consistency Assessment

Two documents are relevant to this query. The first, identified here as document_1, is the paper itself — *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* by Felix Stahlberg and Bill Byrne of the University of Cambridge, Department of Engineering, with the arXiv identifier [1908.10090] visible in the extracted text ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). It is the **primary source** and carries the highest evidentiary weight, since it is the authors' own statement of their experimental design. Its one weakness, for text-mining purposes, is that the extracted text is heavily degraded by PDF-to-text conversion, with digits separated by spaces and table columns collapsed into an interleaved stream.

The second document is a **third-party research note** that summarises the paper's test set size and explicitly frames itself around key questions about search errors, model errors, and test set size ([Third-party research note](#references)). It is a **secondary source**, and its evidentiary value lies chiefly in corroboration. Notably, it agrees with the primary source on the decisive figure of 2,169 sentences and additionally supplies the explicit statement that the length-constrained experiments used 73.0% and 48.3% subsets — a detail that the primary source's extracted text conveys only in a fragmented form. Where the two sources differ — the German-English versus English-German naming of the language pair — the discrepancy concerns labelling rather than the numeric sample size.

On balance, the convergence of a primary source and an independent secondary note on the value of 2,169 sentences gives high confidence that this is the correct answer to the query, and the derived subset sizes of approximately 1,583 and 1,048 sentences follow arithmetically from the reported coverage shares.

## Conclusion

The test set size in Stahlberg and Byrne's study of NMT search and model errors is **2,169 sentences**, corresponding to the complete English–German (labelled German–English in the secondary note) WMT news-test2015 evaluation set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note](#references)). This full set underpins the paper's headline results on greedy, beam, and exact search, and it is reported before any subsetting. The length-constrained experiments that follow are run on reduced samples — 73.0% of the test set for the minimum-translation-length analysis and 48.3% for the length-constrained and length-normalised exact-search tables — yielding approximate working samples of 1,583 and 1,048 sentences respectively. Any summary of the paper's search-error and empty-translation percentages should therefore distinguish clearly between results computed on the full 2,169-sentence set and results computed on these constrained subsets, since the smaller samples carry wider statistical uncertainty and are not directly comparable in precision to the full-set findings.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* [document_1.txt]. arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* [document_2.txt].