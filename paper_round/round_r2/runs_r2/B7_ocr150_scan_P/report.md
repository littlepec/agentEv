# Test Set Size in Stahlberg and Byrne's NMT Search Error Study

## Direct Answer to the Query

The test set used in Stahlberg and Byrne's study on neural machine translation (NMT) search errors and model errors is the **entire English–German WMT news-test2015 test set, which contains 2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is stated explicitly in the experimental setup of the paper's third section, which reports results without length constraints, and it is the sentence count against which the authors' headline claims about search errors and empty translations are made ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

This answer needs to be stated carefully because the retrieved material also contains a third-party research note asserting a different number — 3,003 sentences — for the same test set ([Third-party research note](document_2.txt)). The two sources are therefore in direct conflict, and a careful reader must adjudicate between them. As argued in detail below, the primary source text of the paper itself is the more reliable evidence, and it supports **2,169 sentences**.

## The Primary Source and Its Reported Test Set Size

The paper in question is "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the Department of Engineering at the University of Cambridge, posted as arXiv:1908.10090v1 on 27 August 2019 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The abstract states that the authors present an exact inference procedure for neural sequence models based on a combination of beam search and depth-first search, and that they use this exact search to find the global best model scores under a Transformer-base model "for the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The precise size of that test set is reported in Section 3 of the paper, titled "Results without Length Constraints." The relevant sentence reads: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer-base (Vaswani et al., 2017) model trained with Tensor2Tensor (Vaswani et al., 2018) on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This sentence simultaneously identifies the test set (English–German WMT news-test2015), its scope (the entire set), and its size (2,169 sentences). It is worth emphasizing that the parenthetical "(2,169 sentences)" appears immediately after the phrase "the entire English-German WMT news-test2015 test set," so there is no ambiguity that the number describes the complete set rather than a subset ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The experimental configuration surrounding this test set is also documented. The model is a Transformer-base architecture, trained with Tensor2Tensor on parallel WMT18 data with ParaCrawl excluded; preprocessing follows Stahlberg et al. (2018a) and includes joint subword segmentation using byte pair encoding with 32K merges (Sennrich et al., 2016); BLEU scores are reported and are described as comparable with the matrix.statmt.org evaluation service; and an open-source implementation of the exact inference scheme is available in the SGNMT decoder ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Where the Test Set Size Matters in the Paper's Argument

The test set size is not a cosmetic detail: it determines the denominator for every percentage reported in the paper's main results. Table 1 of the paper reports results on this full test set, and the percentages of search errors and empty translations are computed over those 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The main findings are reproduced in Table 1 below.

**Table 1. Main results on the entire English–German WMT news-test2015 test set (2,169 sentences) reported in Table 1 of Stahlberg and Byrne (2019).**

| Search method | BLEU | Length ratio | Search errors | Empty translations |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

Source: ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

These figures underpin the paper's central and somewhat paradoxical claim: exact inference finds the global best model score but produces a catastrophically low BLEU of 2.1 and a length ratio of 0.06, because for 51.8% of the sentences the model assigns its globally best score to the empty translation, i.e., a single end-of-sentence token ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). In other words, beam search's search errors are, paradoxically, masking a severe model error. Every one of these percentages is defined relative to the 2,169-sentence test set.

The paper also reports behavior as a function of beam size on the same test set: greedy decoding yields 73.58% search errors, Beam-10 yields 57.68% (a 15.9 percentage-point absolute reduction over greedy), and even a beam size of 100 still produces 53.62% search errors, despite being roughly ten times slower than Beam-10 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors further demonstrate that the problem is not specific to the Transformer-base model. Table 2 of the paper compares several architectures on the same test set, as reproduced below.

**Table 2. Search errors and empty translations across architectures on the same test set, as reported in Table 2 of Stahlberg and Byrne (2019).**

| Model | BLEU | Search errors | Empty translations |
|---|---|---|---|
| LSTM | 28.6 | 58.4% | 47.7% |
| SliceNet | 28.8 | 46.0% | 41.2% |
| Transformer-Base | 30.3 | 57.7% | 51.8% |
| Transformer-Big | 31.7 | 32.1% | 25.8% |

Source: ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The LSTM, SliceNet, and Transformer-Big systems are described as strong baselines from a WMT'18 shared task submission (Stahlberg et al., 2018a) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The consistent pattern across architectures strengthens the conclusion that the empty-translation and search-error phenomena are systemic rather than artifacts of one model family.

## Subset Usage in the Length-Constrained Experiments

A crucial nuance is that not every experiment in the paper uses the full test set. The paper's Section 4, "Results with Length Constraints," explicitly changes the experimental protocol: "To find out more about the length deficiency we constrained exact search to certain translation lengths. Constraining search that way increases the run time as the bounds are lower. Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A footnote adds that decoding was stopped if the decoder took longer than a day for a single sentence on a single CPU, whereas exact search without length constraints is much faster and does not need maximum execution time limits ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

Two distinct subset fractions are reported:

- The experiment on minimum translation length (a constraint of 0.25 times the source sentence length), visualized in Figure 5, was "conducted on 73.0% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).
- The experiments in Tables 3 and 4 — exact search constrained to the Beam-10 hypothesis length or the reference length, and exact search under length normalization — were "conducted on 48.3% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

If the full test set is 2,169 sentences, these subsets correspond to approximately 1,583 sentences (73.0%) and 1,048 sentences (48.3%). Table 3 presents these derived counts alongside the alternative counts that would follow from the third-party note's figure.

**Table 3. Subset sizes implied by each candidate full-test-set figure, derived by arithmetic from the reported percentages.**

| Source of full test set size | Full test set | 73.0% subset (Fig. 5) | 48.3% subset (Tables 3–4) |
|---|---|---|---|
| Primary paper text (2,169 sentences) | 2,169 | ≈ 1,583 | ≈ 1,048 |
| Third-party note (3,003 sentences) | 3,003 | ≈ 2,192 | ≈ 1,450 |

Sources: ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note](document_2.txt)). Derived counts are the author's own arithmetic based on the cited percentages.

That the length-constrained subsets are not simply smaller random draws of the full test set is suggested by the BLEU values themselves. On the full test set, Beam-10 achieves BLEU 30.3 (Table 1), whereas on the 48.3% subset used in Section 4, Beam-10 achieves BLEU 37.0 (Table 3) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This substantial difference indicates that the subset experiments operate on a distribution of sentences that differs markedly from the full set, which is consistent with the paper's own framing of these as runtime-constrained exploratory analyses rather than as replications of the main results.

## The Discrepancy Between the Two Sources

The third-party research note states unambiguously that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" and repeats that "the entire English-German WMT news-test2015 test set contains 3,003 sentences" ([Third-party research note](document_2.txt)). It also states that the paper reports this size in its experimental setup and that the full size is reported "before any subset selection" ([Third-party research note](document_2.txt)).

This conflicts with the primary text in two respects. First, the number itself differs: 3,003 versus 2,169. Second, and more tellingly, the note's claim that the full size is "reported before any subset selection" is precisely the role played by the parenthetical "(2,169 sentences)" that appears before the paper's subsection on length-constrained subsets ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). In other words, the third-party note correctly describes the rhetorical placement of the figure in the paper but attaches the wrong value to it.

The third-party note is additionally unreliable on its face. It is described as a "third-party research note," carries no title of its own beyond a descriptive header, lists only the paper's "key questions addressed," and consists largely of paraphrases and repeated assertions rather than verbatim quotations ([Third-party research note](document_2.txt)). Moreover, the version of the note supplied in the retrieved material is duplicated verbatim, and the paper text itself is also duplicated, which suggests an ingestion or deduplication artifact rather than a carefully curated secondary source ([Third-party research note](document_2.txt); [Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). By contrast, the primary paper is a peer-review-style arXiv preprint with named authors, an institutional affiliation, a dated version history, and full references ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Adjudicating the Conflict: Why 2,169 Is the Correct Figure

Applying standard source-evaluation criteria — authorship, provenance, proximity to the underlying evidence, and internal consistency — the primary paper text must be preferred over the third-party note. Four considerations support this conclusion.

First, the primary source states the number in a sentence whose syntactic structure ties it directly and unambiguously to the full test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Second, the primary source is the entity that actually conducted the experiments; the note merely summarizes them, and secondary summaries are, by construction, derivative and more error-prone ([Third-party research note](document_2.txt)). Third, the 3,003 figure in the note is never supported by any quotation, table, or figure from the paper; the note simply asserts it repeatedly ([Third-party research note](document_2.txt)). Fourth, the primary paper's internal consistency around 2,169 is reinforced by the paper's own framing: it distinguishes carefully between "the entire ... test set (2,169 sentences)" in Section 3 and "only a subset of the test set" in Section 4, which is exactly the distinction the note claims, but misplaces ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

It is plausible that the discrepancy arises from confusion with a different WMT test set, since several WMT news test sets from the mid-2010s fall in the vicinity of three thousand sentences. Regardless of its origin, however, the error is consequential: it would inflate every derived subset count by roughly forty percent and thereby misstate the scale of the length-constrained analyses.

## Summary of the Test Set Structure

The overall picture of test set usage in the paper can be summarized as follows.

**Table 4. Test set usage by section of Stahlberg and Byrne (2019).**

| Paper section | Data used | Size |
|---|---|---|
| Section 3: Results without length constraints | Entire English–German WMT news-test2015 test set | 2,169 sentences |
| Section 4: Minimum length constraint of 0.25× source length (Fig. 5) | Subset of test set | 73.0% of 2,169 (≈ 1,583 sentences) |
| Section 4: Tables 3 and 4 (length-constrained and length-normalized exact search) | Subset of test set | 48.3% of 2,169 (≈ 1,048 sentences) |

Source: ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Derived sentence counts are the author's own arithmetic.

A secondary observation follows from this table. The headline numbers that readers most often cite — 73.6% search errors for greedy decoding, 57.7% for Beam-10, 51.8% empty translations under exact search, and 53.62% search errors at beam size 100 — all derive from the full 2,169-sentence test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The length-constrained findings, such as the observation that a minimum length constraint of 0.25 times the source length mitigates but does not eliminate the empty-translation problem, and that exact search under length normalization fixes the length deficiency without matching the best Beam-10 BLEU, rest on the smaller subsets ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Researchers citing these results should therefore distinguish between the 2,169-sentence full-set findings and the subset-based length-constrained findings.

## Conclusion

Based on the primary source text, the test set size in Stahlberg and Byrne's study is **2,169 sentences**, corresponding to the entire English–German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is stated explicitly in the paper's Section 3 and governs all of the paper's main results on search errors, empty translations, and beam-size behavior. The length-constrained experiments in Section 4 use subsets of 73.0% and 48.3% of this test set, which correspond to approximately 1,583 and 1,048 sentences respectively ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The competing figure of 3,003 sentences, advanced by the third-party research note, is unsupported by any quotation or data from the paper and should be treated as an error in the secondary source ([Third-party research note](document_2.txt)). Readers should report the full test set size as 2,169 sentences and specify the relevant subset whenever discussing the length-constrained experiments.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv preprint arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note: On NMT search errors and model errors: Cat got your tongue? (n.d.). [Unpublished research note]. document_2.txt