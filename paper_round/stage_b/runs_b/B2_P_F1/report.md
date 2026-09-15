# BLEU Score Differences Between the Insertion–Deletion Model and the Insertion-Only (KERMIT) Baseline

## Executive Summary

The question addressed in this report is: **how large is the BLEU score difference between the proposed approach and the insertion-only method?** The proposed approach in the supplied sources is the **Insertion–Deletion Model**, and the insertion-only comparison is the **Insertion Model (KERMIT)** ([document_2.txt](document_2.txt)). Across the supplied material, two distinct absolute differences are reported: **21.34 BLEU points** on the Caesar's cipher task (91.49 versus 70.15, presented in Table 2) and **2.02 BLEU points** on the shifted alphabetic sequence task (37.57 versus 35.55, presented in Table 3) ([document_2.txt](document_2.txt)). In both cases the direction of the effect is the same — the insertion–deletion architecture outperforms the insertion-only baseline ([document_2.txt](document_2.txt)). However, the two source documents disagree about which task the 35.55/37.57 pair belongs to: [document_1.txt](document_1.txt) labels that comparison "Caesar's Cipher," while [document_2.txt](document_2.txt) labels it the "shifted alphabetic sequence task." The most defensible overall answer is therefore that the reported advantage of the proposed method ranges from roughly **2 to roughly 21 BLEU points**, depending on the task and on which source's task labelling is accepted.

## 1. Introduction and Scope

### 1.1 The Query

The query asks for a single quantity: the BLEU score gap between the proposed model and the insertion-only method. Because BLEU is a bounded, corpus-level metric conventionally expressed on a 0–100 scale, an "absolute difference" is measured directly in BLEU points, while a "relative difference" expresses the gain as a percentage of the baseline score ([document_2.txt](document_2.txt)).

### 1.2 Terminology

- **Proposed approach:** the Insertion–Deletion Model, which augments an insertion-based generative process with deletion operations ([document_2.txt](document_2.txt)).
- **Insertion-only method:** the Insertion Model, identified in the sources as KERMIT ([document_2.txt](document_2.txt), [document_1.txt](document_1.txt)).
- **BLEU:** the evaluation metric used for every comparison reported in the sources ([document_1.txt](document_1.txt)).

## 2. Source Material and Analytical Method

### 2.1 Document Inventory

Two source documents were supplied. [document_2.txt](document_2.txt) reports headline BLEU figures for the Caesar's cipher task (Table 2) and the shifted alphabetic sequence task (Table 3), and states that the insertion–deletion model improves BLEU on both. [document_1.txt](document_1.txt) supplies the experimental protocol, a concrete input–output example, and a table explicitly titled "Table 3: BLEU scores for the Caesar's cipher task" containing the values 35.55 and 37.57 ([document_1.txt](document_1.txt)).

### 2.2 Analytical Approach

This report (a) extracts every reported BLEU value, (b) computes absolute and relative differences, (c) tabulates the results, and (d) evaluates the conflicting task labels across the two documents. Only the two supplied documents are used as evidence; no external literature is cited.

## 3. Reported BLEU Scores and Differences

### 3.1 Caesar's Cipher Task (Table 2)

According to [document_2.txt](document_2.txt), the Caesar's cipher task produced a BLEU score of **91.49** for the Insertion–Deletion Model and **70.15** for the Insertion Model (KERMIT). The absolute difference is therefore:

> 91.49 − 70.15 = **21.34 BLEU points** in favour of the Insertion–Deletion Model ([document_2.txt](document_2.txt)).

Expressed relatively, this represents a gain of approximately **30.4%** over the insertion-only baseline (21.34 ÷ 70.15). The source explicitly notes that these results are presented in Table 2 and that the insertion–deletion model improves the BLEU score on this task ([document_2.txt](document_2.txt)).

### 3.2 Shifted Alphabetic Sequence Task (Table 3)

The same source reports that, on the shifted alphabetic sequence task, the Insertion–Deletion Model achieved **37.57** BLEU against **35.55** for the Insertion Model (KERMIT) ([document_2.txt](document_2.txt)). The absolute difference is:

> 37.57 − 35.55 = **2.02 BLEU points** ([document_2.txt](document_2.txt)).

The source characterises this as "around 2 BLEU points," and the relative gain is approximately **5.7%** over the baseline (2.02 ÷ 35.55) ([document_2.txt](document_2.txt)). [document_1.txt](document_1.txt) independently states that "the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points," using the identical values of 35.55 and 37.57 ([document_1.txt](document_1.txt)).

### 3.3 Consolidated Comparison

**Table 1. Reported BLEU scores, absolute differences, and relative gains.**

| Task (as labelled by source) | Insertion Only (KERMIT) | Insertion–Deletion (Proposed) | Absolute difference | Relative gain | Source table |
|---|---|---|---|---|---|
| Caesar's cipher | 70.15 | 91.49 | **+21.34** | ≈ +30.4% | Table 2 ([document_2.txt](document_2.txt)) |
| Shifted alphabetic sequence | 35.55 | 37.57 | **+2.02** | ≈ +5.7% | Table 3 ([document_2.txt](document_2.txt)) |
| "Caesar's Cipher" (as labelled in Document 1) | 35.55 | 37.57 | **+2.02** | ≈ +5.7% | Table 3 ([document_1.txt](document_1.txt)) |

**Table 2. Magnitude comparison across tasks.**

| Metric | Value | Derivation |
|---|---|---|
| Larger reported gap | 21.34 BLEU | 91.49 − 70.15 ([document_2.txt](document_2.txt)) |
| Smaller reported gap | 2.02 BLEU | 37.57 − 35.55 ([document_2.txt](document_2.txt)) |
| Ratio between the two gaps | ≈ 10.6× | 21.34 ÷ 2.02 |
| Lower BLEU ceiling | 37.57 | ([document_2.txt](document_2.txt)) |
| Upper BLEU ceiling | 91.49 | ([document_2.txt](document_2.txt)) |

## 4. Interpreting the Magnitude of the Difference

### 4.1 Absolute Versus Relative Framing

A 21.34-point absolute gap and a 2.02-point absolute gap are not equivalent in practical terms. On a 0–100 BLEU scale, 21.34 points is a very large margin, whereas 2.02 points is a modest but non-trivial improvement ([document_2.txt](document_2.txt)). The relative framing is also informative: the 21.34-point margin corresponds to roughly a 30.4% improvement over the 70.15 baseline, while the 2.02-point margin corresponds to roughly a 5.7% improvement over the 35.55 baseline ([document_2.txt](document_2.txt)). Both framings therefore agree that the larger gain occurs on the Caesar's cipher task as defined in [document_2.txt](document_2.txt).

### 4.2 Task-Dependent Variability

The existence of two different gaps across two tasks indicates that the benefit of deletion operations is task-dependent. Where the transformation is a simple, deterministic symbol shift, one source reports a near-ceiling result (91.49) that dwarfs the insertion-only baseline ([document_2.txt](document_2.txt)). Where the transformation is framed as a shifted alphabetic sequence, the improvement narrows to about 2 BLEU points ([document_2.txt](document_2.txt)). This pattern — a consistent directional advantage but a variable magnitude — is the central empirical finding available from the supplied material.

## 5. Discrepancies, Conflicts, and Data-Quality Considerations

### 5.1 Conflicting Task Attribution for the 35.55/37.57 Pair

The two documents assign the same numeric pair to different tasks. [document_2.txt](document_2.txt) places 35.55/37.57 under the heading "shifted alphabetic sequence task" and reserves "Caesar's cipher" for 70.15/91.49 ([document_2.txt](document_2.txt)). [document_1.txt](document_1.txt) places 35.55/37.57 under a heading that reads "Caesar's Cipher BLEU" and captions the table "BLEU scores for the Caesar's cipher task" ([document_1.txt](document_1.txt)). This is a direct conflict in task labelling, even though the underlying numbers agree.

### 5.2 Conflicting Table Numbering

The conflict extends to table numbering. [document_2.txt](document_2.txt) locates the Caesar's cipher results in **Table 2** and the shifted-sequence results in **Table 3** ([document_2.txt](document_2.txt)). [document_1.txt](document_1.txt) labels its Caesar's cipher table as **Table 3** ([document_1.txt](document_1.txt)). Consequently, the identifier "Table 3" refers to a Caesar's cipher table in one document and a shifted-alphabetic-sequence table in the other.

### 5.3 Evidence Supporting the Caesar-Style Nature of Document 1's Task

The example in [document_1.txt](document_1.txt) is "Source h k b e t h\ k\ b\ e\ t" mapped to "Target g j a d s g\ j\ a\ d\ s." Each letter in the target is one position earlier in the Roman alphabet than the corresponding source letter (h→g, k→j, b→a, e→d, t→s), and the non-alphabetic backslash characters are preserved ([document_1.txt](document_1.txt)). This is the definition of a Caesar-style single-shift substitution, which corroborates [document_1.txt](document_1.txt)'s labelling of that table as a Caesar's cipher task, and simultaneously undermines [document_2.txt](document_2.txt)'s separation of a "Caesar's cipher" task from a "shifted alphabetic sequence" task as if they were different benchmarks.

### 5.4 Experimental Protocol

[document_1.txt](document_1.txt) specifies the experimental configuration underlying the 35.55/37.57 table: 100,000 generated training examples, 1,000 held-out evaluation examples, 200,000 training steps, a batch size of 32, and **no model selection** ([document_1.txt](document_1.txt)). The absence of model selection is methodologically relevant: it means the reported scores are not the maximum over a validation sweep but single-run results at a fixed step count, so no confidence intervals, significance tests, or variance estimates are available for either the 2.02-point or the 21.34-point gap ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)).

## 6. Assessment of Reliability

Weighing the evidence:

1. **The 2.02-point figure is independently corroborated.** Two separate statements — one characterising the gap as "around 2 BLEU points" ([document_2.txt](document_2.txt)) and one stating that the deletion model "again increases the BLEU score over just the insertion model, by around 2 BLEU points" ([document_1.txt](document_1.txt)) — converge on the same magnitude and the same underlying values (35.55 and 37.57).
2. **The 21.34-point figure rests on a single assertion.** It appears only in one paragraph of one document, explicitly tied to Table 2 and to the label "Caesar's cipher" ([document_2.txt](document_2.txt)), and it is not corroborated anywhere in [document_1.txt](document_1.txt).
3. **The task taxonomy is inconsistent between sources.** Because the two documents disagree about which task maps to which numbers, the label "Caesar's cipher" cannot by itself be used to disambiguate the two gaps.

On balance, the 2.02-point difference is the better-supported estimate for the shifted-sequence / Caesar-style task, while the 21.34-point difference should be regarded as a separately reported result whose task identity is contested. Neither figure should be treated as definitive without the underlying tables.

## 7. Implications

For anyone extracting a single number in answer to the query, the honest answer is a range rather than a point estimate: the insertion–deletion model improves BLEU over the insertion-only KERMIT baseline by **approximately 2 BLEU points on one reported task and approximately 21 BLEU points on another**, with the 21.34-point figure being about 10.6 times larger than the 2.02-point figure ([document_2.txt](document_2.txt)). The qualitative conclusion — that adding deletion to an insertion-only generative process improves translation quality on transformation-style sequence tasks — is supported by both sources ([document_2.txt](document_2.txt), [document_1.txt](document_1.txt)). The quantitative conclusion is not yet stable, because the two documents do not agree on how the tasks and the numbers pair up.

## 8. Conclusion

The reported BLEU difference between the proposed Insertion–Deletion Model and the insertion-only Insertion Model (KERMIT) is **21.34 BLEU points** on the Caesar's cipher task (91.49 versus 70.15, Table 2) and **2.02 BLEU points** on the shifted alphabetic sequence task (37.57 versus 35.55, Table 3), according to [document_2.txt](document_2.txt). [document_1.txt](document_1.txt) reproduces the 37.57/35.55 comparison but labels it as the Caesar's cipher task, creating a direct conflict in task attribution. Because the 2.02-point figure is corroborated by two sources and is supported by an explicit Caesar-shift input–output example, it is the more reliable single estimate for the Caesar-style/shifted-sequence benchmark, while the 21.34-point figure remains a valid but uncorroborated report for the task labelled "Caesar's cipher" in [document_2.txt](document_2.txt). Both sources agree on the direction of the effect: the insertion–deletion model is superior to the insertion-only baseline on every task reported ([document_2.txt](document_2.txt)).

## References

Document 1. (n.d.). *Source and target sequences, experimental setup, and Table 3: BLEU scores for the Caesar's cipher task* [Unpublished source document]. document_1.txt.

Document 2. (n.d.). *Reported BLEU scores for the Caesar's cipher task (Table 2) and the shifted alphabetic sequence task (Table 3)* [Unpublished source document]. document_2.txt.