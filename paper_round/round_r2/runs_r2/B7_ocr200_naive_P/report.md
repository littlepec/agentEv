# Determining the Test Set Size in Stahlberg and Byrne's "On NMT Search Errors and Model Errors"

## Introduction and Scope of the Query

The question under examination is deceptively simple: what is the test set size in the neural machine translation (NMT) study "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the University of Cambridge ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Two documents in the provided evidence bear directly on this question. The first is the paper itself, which reports a test set of **2,169 sentences** for its main unconstrained experiments ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The second is a third-party research note that explicitly addresses the test-set-size question and asserts that the paper's main experiments use the "entire English-German WMT news-test2015 test set of 3,003 sentences" ([Third-party research note](document_2.txt)). Because these two figures conflict, this report evaluates the provenance, internal consistency, and relative reliability of each claim before arriving at a defensible conclusion. The analysis also covers the length-constrained experiments, which used subsets of the test set rather than the full set, and considers what the test set size means for interpreting the paper's reported search-error and empty-translation rates.

## The Primary Source and Its Reported Test Set Size

### Direct Statement in the Paper

The primary source contains an unambiguous statement of the test set size in its experimental section. In Section 3, titled "Results without Length Constraints," the authors state: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The parenthetical figure of 2,169 sentences is embedded directly in the sentence that defines the experimental population for the paper's headline results, which include Table 1 and the search-error analyses presented in Figures 1 through 4.

The abstract of the same paper corroborates that the experimental scope is the full WMT15 English-German test set, referring to "the entire WMT15 English-German test set" when describing the exact-search experiments ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). While the abstract does not repeat the numerical size, it is consistent with the full-test-set framing of Section 3.

### The Experimental Context Surrounding the Figure

The 2,169-sentence figure is not an incidental detail; it defines the population over which several central findings were computed. The paper reports BLEU scores, search-error percentages, and empty-translation percentages for several systems on this test set. Table 1 shows Beam-10 achieving 30.3 BLEU with a length ratio of 1.00 and 57.7% search errors, greedy decoding achieving 29.3 BLEU with a length ratio of 1.02 and 73.6% search errors, and exact search achieving 2.1 BLEU with a length ratio of 0.06 and 51.8% empty translations ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Table 2 extends this comparison to other architectures: LSTM at 28.6 BLEU with 58.4% search errors and 47.7% empty translations, SliceNet at 28.8 BLEU with 46.0% search errors and 41.2% empty translations, Transformer-Base at 30.3 BLEU with 57.7% search errors and 51.8% empty translations, and Transformer-Big at 31.7 BLEU with 32.1% search errors and 25.8% empty translations ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). All of these headline percentages are computed over the full test set described as containing 2,169 sentences.

The paper also describes the model and preprocessing pipeline that generated these results: a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl, with joint subword segmentation using byte pair encoding and 32K merges ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The exact inference implementation is available in the SGNMT decoder ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These methodological details reinforce that Section 3 is the paper's main experimental section and that the 2,169-sentence test set is the population for its principal quantitative claims.

## The Conflicting Figure in the Third-Party Research Note

### Claims Made in the Note

The third-party research note makes a series of firm assertions about the test set size. It states that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" and repeats that "the entire English-German WMT news-test2015 test set contains 3,003 sentences" ([Third-party research note](document_2.txt)). It further claims that "the paper reports this size in its experimental setup" and that "this full test set size of 3,003 sentences is reported before any subset selection" ([Third-party research note](document_2.txt)).

The note also correctly identifies the structure of the paper's experimental design: it observes that the unconstrained results are conducted on the entire test set, while the length-constrained experiments use only subsets, with one experiment using 73.0% of the test set and others using 48.3% of the test set ([Third-party research note](document_2.txt)). This structural observation aligns with the primary source's own description of its methodology, which states that "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Internal Issues with the Note's Figure

The 3,003-sentence figure does not appear anywhere in the primary source text provided. The primary source states 2,169 sentences explicitly in Section 3 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The note does not quote a sentence from the paper containing the number 3,003; it asserts that the paper "reports this size in its experimental setup" without providing a corresponding quotation ([Third-party research note](document_2.txt)). Moreover, the note's text is repetitive and self-reinforcing, restating the same 3,003 figure several times in near-identical phrasing rather than citing a specific passage, table, or figure from the paper ([Third-party research note](document_2.txt)). This repetition pattern suggests the figure may have been generated or carried over from an external assumption rather than extracted directly from the primary document.

## Comparative Assessment of Source Reliability

The two sources differ substantially in provenance. The primary source is the original research paper by the authors who conducted the experiments, and it reports the test set size as part of its own experimental setup ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The secondary source is a "third-party research note" with no named author and no methodological description of how its figures were determined ([Third-party research note](document_2.txt)). Under standard principles of evidence evaluation, a direct statement in the original research report should outweigh a secondary summary when the two conflict, particularly when the secondary source does not provide a verifiable quotation supporting its figure.

The following table summarizes the conflicting claims.

| Source | Claimed full test set size | Basis for the claim | Corroboration in primary text |
|---|---|---|---|
| Stahlberg & Byrne (2019), primary paper | 2,169 sentences | Explicit sentence in Section 3 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) | Direct statement, consistent with "entire WMT15 English-German test set" framing in the abstract |
| Third-party research note | 3,003 sentences | Asserted in note; no quotation from the paper provided ([Third-party research note](document_2.txt)) | Not found in the primary source text |

The weight of the evidence therefore favors the primary source's figure of 2,169 sentences as the test set size actually used in the paper's main experiments.

## Subset Sizes in the Length-Constrained Experiments

The question of test set size also requires attention to the length-constrained experiments, which did not use the full test set. The primary source states that "all results in this section are conducted on only a subset of the test set to keep the runtime under control," and that decoding was stopped if a single sentence took longer than a day on a single CPU ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Two specific subset proportions are reported: Figure 5's length-ratio histogram is based on 73.0% of the test set, while the experiments reported in Tables 3 and 4 are based on 48.3% of the test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

If the full test set is taken as 2,169 sentences, these subset proportions correspond to approximately 1,583 sentences for the 73.0% experiments and approximately 1,048 sentences for the 48.3% experiments. If the third-party note's figure of 3,003 sentences were used instead, the corresponding counts would be approximately 2,192 and 1,450 sentences respectively. The primary source does not report the absolute subset sizes, so these are derived estimates rather than figures stated in the paper ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The table below presents the subset structure.

| Experiment group | Proportion of test set used | Approximate sentences if full set = 2,169 | Approximate sentences if full set = 3,003 |
|---|---|---|---|
| Unconstrained main results (Tables 1–2; Figures 1–4) | 100% | 2,169 | 3,003 |
| Minimum-length / length-ratio experiment (Figure 5) | 73.0% | ≈1,583 | ≈2,192 |
| Length-constrained exact search (Tables 3–4) | 48.3% | ≈1,048 | ≈1,450 |

The 73.0% and 48.3% figures themselves are explicitly reported in the primary source ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)), while the absolute counts in the right-hand columns are arithmetic derivations from the two competing full-set figures.

## Why the Test Set Size Matters for Interpreting the Findings

The choice between 2,169 and 3,003 sentences is not merely a bookkeeping detail. The paper's central claims are statistical in nature: beam search fails to find the global best model score for the majority of sentences, and more than half of sentences receive their global best model score under an empty translation ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). At the full-set level, the paper reports 51.8% empty translations and 57.7% search errors under Beam-10 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These proportions are computed over the test set actually decoded, so the population size determines the precision of the findings and the appropriate generalization claims.

The paper notes that even a beam size of 100 produces 53.62% search errors, and that Beam-10 yields 15.9 percentage points fewer search errors than greedy decoding (57.68% versus 73.58%) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). It also reports that long source sentences are more affected by both problems, with the global best translation being empty for almost all sentences longer than 40 tokens ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These findings depend on the composition of the test set, and a larger or smaller test set could in principle change the precise percentages, though the qualitative pattern—pervasive search errors and a strong empty-translation preference—is a consistent theme across model architectures, including LSTM, SliceNet, Transformer-Base, and Transformer-Big ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The length-constrained experiments further illustrate why the distinction between full-set and subset results matters. When exact search was constrained to the reference length, BLEU improved by 0.9 points over Beam-10, from 37.0 to 37.9, on 48.3% of the test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Under length normalization, exact search did not suffer from the length deficiency but also did not match the best Beam-10 BLEU score, with Exact Beam-30 achieving 36.7 BLEU and Exact achieving 27.2 BLEU at length ratios of 0.98 and 0.74 respectively, compared with Beam-10's 37.0 BLEU at a length ratio of 1.00 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These numbers are explicitly tied to a 48.3% subset and should not be conflated with the full-set results ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Conclusion

On the basis of the provided evidence, the defensible answer to the query is that the test set size reported in the primary source for the paper's main unconstrained experiments is **2,169 sentences**, described as the entire English-German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The length-constrained experiments used subsets of this test set, specifically 73.0% for the minimum-length length-ratio analysis and 48.3% for the exact-search length-constrained experiments ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party research note's assertion of 3,003 sentences is not corroborated by the primary source text and is not accompanied by a supporting quotation from the paper; it should therefore be treated as an unverified secondary claim ([Third-party research note](document_2.txt)). Where the two sources conflict, the direct experimental statement in the original paper carries greater weight, and 2,169 sentences is the figure most consistent with the paper's own framing of its experimental population. Future users of these findings should be careful to distinguish between the full test set and the subsets, since the paper's headline search-error and empty-translation percentages are computed on the full set while its length-constrained conclusions rest on smaller subsets.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv preprint arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Research note]. document_2.txt