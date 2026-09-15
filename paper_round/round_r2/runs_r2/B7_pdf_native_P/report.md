# Determining the Test Set Size in Stahlberg and Byrne's Study of NMT Search and Model Errors

## 1. Purpose and Scope of This Report

This report answers a single, deceptively simple question: **what is the test set size** in the study "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Stahlberg and Byrne. The question matters because the paper's central claims — that beam search fails to recover the global best model score for most sentences, and that more than half of all sentences receive the empty translation as their global best hypothesis — are quantitative claims that depend on the corpus over which they were measured. A precise understanding of the evaluation set is therefore a prerequisite for correctly interpreting, replicating, or challenging those findings.

Two pieces of documentation are available. The first is the primary source itself, the full text of the paper, including its abstract, methodology, algorithm listings, result tables, and figures. The second is a third-party research note that summarizes and interprets the paper's experimental setup. These two sources **disagree** on the test set size, and resolving that disagreement responsibly — by prioritizing the more authoritative source — is the analytical core of this report.

## 2. The Direct Answer

Based on the primary source — the paper itself — **the test set size is 2,169 sentences**. The paper states unambiguously in its experimental section that all experiments reported in the results without length constraints were conducted "on the entire English-German WMT news-test2015 test set (2,169 sentences)" with a Transformer base model ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). The abstract of the same paper refers to this as "the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

A third-party research note asserts that the same test set contains **3,003 sentences** and claims that "the paper reports this size in its experimental setup" ([Third-party research note, n.d.](document_2.txt)). As documented in the following sections, this assertion is not supported by the primary text and should be treated as unreliable. My considered position, developed in detail below, is that **2,169 sentences is the correct full test set size for the paper's main experiments**, and that the 3,003 figure represents an error in secondary reporting rather than a genuine attribute of the study.

## 3. The Primary Source: 2,169 Sentences

### 3.1 Where the Figure Appears

The figure of 2,169 sentences appears in Section 3 of the paper, "Results without Length Constraints," which is the section containing the paper's headline results. The relevant sentence reads: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base (Vaswani et al., 2017) model trained with Tensor2Tensor (Vaswani et al., 2018) on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

This statement is unusually precise by the standards of the paper: it specifies the language pair (English-German), the corpus (WMT news-test2015), the scope ("entire"), and an exact sentence count (2,169). It also explicitly contrasts this full-set evaluation with the subset evaluations used later in the paper, where the authors state that they restricted experiments to "only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

### 3.2 Experimental Configuration Surrounding the Test Set

The test set does not stand in isolation; it is coupled to a specific model and preprocessing pipeline:

- **Model:** Transformer base ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).
- **Training data:** Parallel WMT18 data, excluding ParaCrawl ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).
- **Preprocessing:** As described by Stahlberg et al. (2018a), including joint subword segmentation using byte pair encoding (Sennrich et al., 2016) with 32K merges ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).
- **Metric:** Cased BLEU scores ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

Because the 2,169-sentence count is embedded in this fully specified experimental configuration, it is the natural denominator against which the paper's percentages should be read. For example, the reported rate of 51.8% empty global-best translations under exact search corresponds to roughly 1,124 sentences of 2,169, and the 57.7% search-error rate under Beam-10 corresponds to roughly 1,251 sentences.

### 3.3 The Main Results Measured on This Set

The paper's Table 1 reports the following headline results on the full 2,169-sentence set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)):

| Search Method | BLEU | Length Ratio | #Search Errors | #Empty |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

Additional full-set findings include the observation that "even a large beam size of 100 produces 53.62% search errors," and that Beam-100 improves search only marginally over Beam-10 "despite being 10 times slower" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). The paper also generalizes these findings across architectures in Table 2, reporting Beam-10 search-error rates and exact-search empty rates of 58.4%/47.7% (LSTM), 46.0%/41.2% (SliceNet), 57.7%/51.8% (Transformer-Base), and 32.1%/25.8% (Transformer-Big) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

## 4. The Conflicting Figure: 3,003 Sentences

### 4.1 What the Third-Party Note Claims

The third-party research note states, repeatedly and emphatically, that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "the entire English-German WMT news-test2015 test set contains 3,003 sentences," and that "the paper reports this size in its experimental setup" ([Third-party research note, n.d.](document_2.txt)). The note further asserts that "the paper reports the full test set size as 3,003 sentences before any subset selection" ([Third-party research note, n.d.](document_2.txt)).

### 4.2 Why the Claim Does Not Hold Up

There are several reasons to reject the 3,003 figure as the test set size for this paper.

First, and most decisively, **the primary source contradicts it**. The paper's own experimental setup section states a different number — 2,169 — for the very same corpus (WMT news-test2015) and the very same language pair (English-German). A third-party summary cannot override the direct, unambiguous statement of the source it purports to summarize.

Second, the note's claim is **internally inconsistent with its own framing**. The note uses the identical corpus name ("English-German WMT news-test2015 test set") that the paper uses while assigning it a different size. If the note were describing a different corpus or a different language pair, the discrepancy might be explainable; as written, it describes the same object with a different magnitude.

Third, the note provides **no methodological basis** for the 3,003 figure. It does not indicate a page, section, table, or quotation from the paper that supports the number. By contrast, the paper's 2,169 figure appears inline in a fully quoted sentence that also names the model, the training data, the tokenization scheme, and the metric ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

Fourth, the note is **repetitive rather than evidential**. It repeats the 3,003 figure five times across short paragraphs but never anchors it to an identifiable passage of the paper, which is characteristic of an unreliable secondary description rather than a verifiable extraction.

### 4.3 Source Prioritization and My Assessment

Applying the principle of prioritizing relevance, reliability, and significance, the primary research paper is the authoritative source for its own experimental design, and the third-party note is secondary at best. On that basis, I conclude that **the test set size is 2,169 sentences**, and that the 3,003 figure reported in the third-party note is erroneous. Readers should not use 3,003 as a denominator when reproducing or interpreting the paper's percentages. The note's reliability on this specific point is low, and this caveat should extend to any other numeric claims the note makes without direct quotation.

## 5. Subset Sizes Used in the Length-Constrained Experiments

### 5.1 Reported Subset Percentages

The paper explicitly states that the length-constrained exact-search experiments were run on subsets rather than the full test set: "Constraining search that way increases the run time as the γ-bounds are lower. Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). Two distinct subsets are reported:

- **73.0% of the test set**, used for the experiment imposing a minimum translation length of 0.25 times the source sentence length (Figure 5) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).
- **48.3% of the test set**, used for the constrained-length experiments in Table 3 and for the length-normalization comparison in Table 4 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

### 5.2 Derived Absolute Sizes

Applying these percentages to the full set of 2,169 sentences yields the following approximate absolute sizes. These figures are derived arithmetic, not figures reported directly in the paper, and should be labeled as such:

| Experiment Section | Reported Proportion | Derived Sentences (of 2,169) | Source |
|---|---|---|---|
| Minimum-length constraint (Fig. 5) | 73.0% | ≈1,583 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)) |
| Length-constrained exact search (Tables 3, 4) | 48.3% | ≈1,048 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)) |

Had the 3,003 figure been correct, these subsets would correspond to approximately 2,192 and 1,450 sentences respectively; the discrepancy propagates directly into any attempted replication, which is precisely why the correct baseline matters.

### 5.3 Why the Subsets Were Necessary

The reason for subsetting is mechanistic rather than arbitrary. Exact depth-first search with length constraints forces the lower bound γ to be lower, because the pruning criterion must be evaluated separately for each allowed translation length k via length-dependent bounds γ<sub>k</sub> = (k + 1) · log P(y<sub>beam</sub>|x) / (|y<sub>beam</sub>| + 1) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). Lower bounds mean weaker pruning, which means longer run times. The authors report that they "stopped decoding if the decoder took longer than a day for a single sentence on a single CPU," while noting that exact search without length constraints "is much faster and does not need maximum execution time limits" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). The full-test-set results are therefore the unconstrained ones, and the constrained results are necessarily subset-based.

## 6. Consolidated Summary of Reported Sizes

| Quantity | Value | Status | Source |
|---|---|---|---|
| Full WMT15 English-German test set (news-test2015) | 2,169 sentences | Reported directly | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)) |
| Full test set size per third-party note | 3,003 sentences | Contradicted by primary source | ([Third-party research note, n.d.](document_2.txt)) |
| Minimum-length-constraint experiment | 73.0% of test set | Reported directly | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)) |
| Length-constrained exact search / length normalization | 48.3% of test set | Reported directly | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)) |

## 7. Why the Test Set Size Matters for Interpreting the Findings

The size of the test set is not a peripheral detail; it conditions the strength of the paper's conclusions. The paper's most striking claim is that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation, revealing a massive failure of neural models in properly accounting for adequacy" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). Under exact search on the full set, the measured empty rate was 51.8%, with a catastrophic BLEU of 2.1 and a length ratio of 0.06 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). A claim of this severity is only credible to the extent that it rests on a well-defined, sufficiently large, and fully disclosed evaluation set. The 2,169-sentence WMT news-test set serves that role; the paper also demonstrates that the phenomenon is not model-specific by reporting empty-global-best rates of 47.7% for an LSTM, 41.2% for SliceNet, 51.8% for Transformer-Base, and 25.8% for Transformer-Big ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)).

The paper further links the phenomenon to sentence length, showing that "the global best translation is empty for almost all sentences longer than 40 tokens" and that substantial search errors persist even when empty-preferring sentences are excluded ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). These stratified analyses require knowing the total pool of sentences from which the length bins were drawn — again, 2,169.

Finally, the constrained-length experiments illustrate that remedies are imperfect. Constraining exact search to the Beam-10 hypothesis length yielded no improvement over beam search (both 37.0 BLEU, ratio 1.00), whereas constraining to the reference length improved BLEU by 0.9 points to 37.9 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). Under length normalization, exact search recovered reasonable length ratios (1.03) but could not match the Beam-10 BLEU of 36.3 for Beam-10/tuned configuration, reaching 36.4 while unnormalized exact search collapsed to 27.2 BLEU and a 0.74 ratio ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). All of these comparisons, run on the 48.3% subset, are only interpretable in relation to the full set they were sampled from.

## 8. Conclusion

The evidence supports a clear answer: **the test set size in Stahlberg and Byrne's study is 2,169 sentences**, comprising the entire English-German WMT news-test2015 test set used for the unconstrained exact-inference experiments ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). Length-constrained follow-up experiments were performed on subsets equal to 73.0% and 48.3% of that full set, i.e., approximately 1,583 and 1,048 sentences respectively ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090v1)). The competing figure of 3,003 sentences originates solely from a third-party research note that attributes it to the paper without evidentiary support and in direct conflict with the paper's own text ([Third-party research note, n.d.](document_2.txt)). Because the primary source is authoritative for its own experimental design and the secondary source is both unsupported and self-contradictory on this point, I treat 2,169 as the correct value and recommend that any downstream use of this study — replication, meta-analysis, or citation — adopt 2,169 sentences as the evaluation-set denominator.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv:1908.10090v1. https://arxiv.org/abs/1908.10090v1

Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Research note]. document_2.txt