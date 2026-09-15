# BLEU Score Differences Between the Proposed Insertion-Deletion Model and the Insertion-Only (KERMIT) Method

## Direct Answer to the Query

The evidence supplied in the source documents reports **two distinct BLEU-score differences** between the proposed insertion-deletion approach and the insertion-only baseline (KERMIT), rather than a single figure. On the Caesar's cipher benchmark, the reported BLEU scores are **91.49 for the Insertion-Deletion Model** and **70.15 for the Insertion Model (KERMIT)**, a difference of **21.34 BLEU points in favor of the proposed method** ([document_2.txt](document_2.txt)). On a second sequence-transformation benchmark, the reported scores are **37.57 for the Insertion-Deletion Model** and **35.55 for the Insertion Model (KERMIT)**, a difference of **2.02 BLEU points**, which the paper itself characterizes as "around 2 BLEU points" ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

Because the query is phrased in the singular, the most defensible formulation of the answer is that **the magnitude of the proposed method's advantage is task-dependent**. It is large — 21.34 BLEU points, equivalent to a 30.4% relative gain over the baseline — on one benchmark, and modest — 2.02 BLEU points, or a 5.7% relative gain — on the other. Both differences point in the same direction, and neither source reports a task on which the insertion-only method outperforms the proposed insertion-deletion model ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

## Overview of the Source Base

Two source documents were provided, identified here as document_1.txt and document_2.txt. Both are untitled extracts, and the information available about each is limited to their content ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

**document_2.txt** functions as a summary of reported results. It states the score pairs for both benchmarks, computes the absolute differences, names the tables in which the results appear, and offers a one-line interpretation for each task ([document_2.txt](document_2.txt)).

**document_1.txt** provides the closer-to-primary detail. It presents an illustrative source–target pair, describes the experimental protocol, reproduces one score table with its caption, and offers an interpretive sentence about the deletion mechanism ([document_1.txt](document_1.txt)). The illustrative example shown is a letter-level shift mapping, in which the source sequence "h k b e t" is mapped to the target sequence "g j a d s" — a consistent shift of one position in the alphabet for each character ([document_1.txt](document_1.txt)).

Because document_2.txt appears twice in the supplied material in near-identical form, and because both duplicate copies carry the same figures, the duplication adds no new evidentiary weight; it is treated here as a single source ([document_2.txt](document_2.txt)).

## Reported BLEU Differences in Detail

### The 21.34-Point Difference (Caesar's Cipher Task)

On the Caesar's cipher task, the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT) ([document_2.txt](document_2.txt)). The stated difference is 21.34 BLEU points in favor of the insertion-deletion model, and these results are attributed to Table 2 of the underlying paper ([document_2.txt](document_2.txt)). The summary explicitly concludes that "the Insertion-Deletion Model improves BLEU score on this task" ([document_2.txt](document_2.txt)).

Two observations about this pair of numbers are worth making. First, the arithmetic is internally consistent: 91.49 − 70.15 = 21.34, exactly the difference reported ([document_2.txt](document_2.txt)). Second, expressed as a relative quantity, 21.34 points against a baseline of 70.15 corresponds to a relative improvement of approximately **30.4%** (21.34 ÷ 70.15 ≈ 0.304), a figure derived here from the reported numbers themselves rather than stated in the source ([document_2.txt](document_2.txt)).

### The 2.02-Point Difference (Second Benchmark)

On the second benchmark, the reported BLEU scores are 37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT) ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). The stated difference is 2.02 BLEU points, described in the narrative as "around 2 BLEU points" ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). These results are attributed to Table 3 ([document_2.txt](document_2.txt)).

Again, the arithmetic is consistent: 37.57 − 35.55 = 2.02, matching the reported difference ([document_2.txt](document_2.txt)). Expressed relatively, 2.02 points against a baseline of 35.55 corresponds to an approximately **5.7%** relative improvement (2.02 ÷ 35.55 ≈ 0.057), again a value computed here from the reported figures ([document_1.txt](document_1.txt)).

Notably, document_1.txt uses the word "again" when describing this result — "the deletion model again increases the BLEU score over just the insertion model" — which implies that the improvement pattern is repeated across tasks rather than being an isolated outcome ([document_1.txt](document_1.txt)). This phrasing is consistent with the existence of more than one benchmark on which the insertion-deletion architecture outperforms the insertion-only architecture ([document_1.txt](document_1.txt)).

## Consolidated Comparison of Reported Results

The table below consolidates the two score pairs, their absolute differences, and the derived relative differences.

| Benchmark (as labeled in source) | Insertion-only (KERMIT) | Proposed Insertion-Deletion | Absolute difference | Derived relative gain | Source table |
|---|---|---|---|---|---|
| Caesar's cipher | 70.15 | 91.49 | **+21.34** | ≈ +30.4% | Table 2 ([document_2.txt](document_2.txt)) |
| Second benchmark (see note below) | 35.55 | 37.57 | **+2.02** | ≈ +5.7% | Table 3 ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)) |

*Note:* The relative-gain column is calculated from the reported BLEU figures and is not stated as such in either source. The task label for the second row is contested between the two sources and is addressed in the following section ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Reconciliation of the Conflicting Task Labels

A careful reading of the two sources reveals a genuine attribution conflict that must be reported rather than smoothed over, because it affects how the 2.02-point figure should be described.

**document_2.txt** attributes the 37.57-versus-35.55 pair to the "shifted alphabetic sequence task" and Table 3, while assigning the 91.49-versus-70.15 pair to the Caesar's cipher task and Table 2 ([document_2.txt](document_2.txt)).

**document_1.txt**, by contrast, presents the same 35.55 and 37.57 figures under an explicit caption reading "Caesar's Cipher BLEU" and "Table 3: BLEU scores for the Caesar's cipher task," listing the Insertion Model (KERMIT) at 35.55 and the Insertion Deletion Model at 37.57 ([document_1.txt](document_1.txt)). The surrounding illustrative example in that document is a single-position alphabetic shift ("h k b e t" → "g j a d s"), which is consistent with a shift-based cipher formulation ([document_1.txt](document_1.txt)).

| Source | Task label applied to 37.57 / 35.55 | Table cited |
|---|---|---|
| document_2.txt | Shifted alphabetic sequence | Table 3 ([document_2.txt](document_2.txt)) |
| document_1.txt | Caesar's cipher | Table 3 ([document_1.txt](document_1.txt)) |

Two competing explanations are consistent with the available material.

**Explanation A: two distinct benchmarks exist, and document_1.txt mislabels the caption.** Under this reading, the paper reports a Caesar's cipher task with BLEU scores of 91.49 and 70.15 (Table 2) and a separate shifted alphabetic sequence task with BLEU scores of 37.57 and 35.55 (Table 3) ([document_2.txt](document_2.txt)). document_1.txt then reproduces the Table 3 numbers but attaches an incorrect caption to them ([document_1.txt](document_1.txt)).

**Explanation B: a single shift-based benchmark exists, and document_2.txt splits it into two.** Under this reading, the 37.57/35.55 pair is the Caesar's cipher result, as its accompanying table caption states, and the 91.49/70.15 pair belongs to a differently configured task that document_2.txt mislabels ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

On the balance of the evidence, **Explanation A is the better supported of the two**, for three reasons. First, there are demonstrably two different score pairs in the material (91.49/70.15 and 37.57/35.55), and neither pair can be derived from the other, so at minimum two distinct evaluation settings must exist ([document_2.txt](document_2.txt)). Second, document_2.txt distinguishes the tasks by name, by score pair, and by table number in a single coherent passage, which is a more internally consistent account than a caption that contradicts both the numbering and the narrative of the other source ([document_2.txt](document_2.txt)). Third, document_1.txt shows signs of extraction artifacts — run-together source/target strings, escaped delimiters, and a truncated concluding line — which makes a misattributed caption plausible ([document_1.txt](document_1.txt)).

That said, my confidence in this attribution is moderate rather than high, because neither source reproduces the complete original table set, and the label conflict cannot be resolved from the supplied material alone ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). What *can* be said with high confidence is that **the numeric pair 37.57 / 35.55 and the 2.02-point difference are corroborated by both sources**, even though the label applied to them is not ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Corroboration of the numbers across two documents is a stronger form of evidence than the agreement of either document with itself.

## Experimental Context Bearing on the Differences

document_1.txt supplies the experimental protocol behind the reported figures: 100,000 generated examples are used for training, evaluation is performed on 1,000 held-out examples, models are trained for 200,000 steps with a batch size of 32, and no model selection is performed ([document_1.txt](document_1.txt)).

Three features of this protocol are directly relevant to interpreting the size of the reported differences.

First, the evaluation set is small — 1,000 held-out examples ([document_1.txt](document_1.txt)). A BLEU score computed on such a set is sensitive to the particular sample drawn, so a 2.02-point gap measured on 1,000 examples is less firmly established than the same gap measured on a much larger set. This is my analytical judgment based on the reported design, not a claim made in either source.

Second, "no model selection" is reported ([document_1.txt](document_1.txt)). This means the reported scores were not chosen as the best over a validation sweep; they are single-run outcomes at a fixed training budget. This removes one common source of optimistic bias, but it also means no evidence is available about the stability of the results across seeds or checkpoints. This too is my inference from the reported protocol rather than a statement in the sources.

Third, neither source reports confidence intervals, standard deviations across runs, or significance tests for either comparison ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Consequently, the only defensible statements about reliability are proportional to the size of the effects themselves.

## Analytical Assessment

Weighing the evidence, my concrete assessment is as follows.

**The 21.34-point difference is large and unlikely to be an artifact of noise.** A 30.4% relative improvement over the insertion-only baseline on the Caesar's cipher task is a substantial effect ([document_2.txt](document_2.txt)). Effects of this magnitude are not typically produced by sampling variation on an evaluation set of 1,000 examples, and the direction of the effect matches the architectural intuition described in the sources — that adding deletion to insertion improves performance relative to insertion alone ([document_1.txt](document_1.txt)). I therefore treat the 21.34-point figure as the headline, robust finding of the comparison, while noting that no variance estimate is available to confirm this judgment statistically ([document_2.txt](document_2.txt)).

**The 2.02-point difference is real in the reported data but modest, and its practical significance is uncertain.** Both sources report the same pair of numbers and the same approximate difference ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)), and the direction of the effect is consistent with the larger result. However, a 2.02-point BLEU gap — approximately 5.7% relative — on 1,000 held-out examples and with no model selection and no reported variance is small enough that run-to-run variation could plausibly explain a meaningful fraction of it ([document_1.txt](document_1.txt)). My opinion is that this result should be described as *suggestive and directionally consistent* rather than as a demonstrated large improvement. The source's own hedging — "around 2 BLEU points" — is consistent with this conservative reading ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

**The consistency of direction across tasks is the strongest aggregate claim available.** Neither document reports any benchmark on which the insertion-only model outperforms the insertion-deletion model ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The word "again" in document_1.txt indicates that the improvement recurs across tasks ([document_1.txt](document_1.txt)). The convergence of a large effect on one task and a small effect on another, both favoring the proposed approach, is more persuasive than either result in isolation.

**The comparison is a two-condition contrast, not a broad benchmark survey.** Every figure available addresses only the insertion-only (KERMIT) versus insertion-deletion contrast ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). No other baselines, no ablation of the deletion component in isolation, and no cross-task generalization results are reported in the supplied material. The claim that can be supported is therefore narrow: on the tasks reported, the insertion-deletion model achieves higher BLEU than the insertion-only model, by 21.34 points on one and 2.02 points on the other ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Limitations and Gaps in the Supplied Evidence

Several limitations constrain the conclusions that can be drawn:

- **Task-label inconsistency.** The second benchmark is called "shifted alphabetic sequence" in one source and "Caesar's cipher" in the other for the identical score pair ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). This unresolved conflict means the 2.02-point difference cannot be confidently attributed to a specific named task on the present evidence.
- **Absent statistical reporting.** No confidence intervals, seed variance, or significance tests accompany any figure ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).
- **Small evaluation set.** Evaluation on 1,000 held-out examples limits precision, particularly for the smaller effect ([document_1.txt](document_1.txt)).
- **No model selection.** Reported scores are single-budget outcomes, with no evidence about robustness to training length or initialization ([document_1.txt](document_1.txt)).
- **Metric specification omitted.** Neither source specifies the BLEU variant, tokenization scheme, or smoothing method used, so the figures cannot be compared directly with BLEU numbers reported under other conventions ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).
- **Incomplete table coverage.** Only Tables 2 and 3 are referenced; the surrounding results that would contextualize these comparisons are not available ([document_2.txt](document_2.txt)).

## Conclusion

The answer to the question of how large the BLEU-score difference is between the proposed approach and the insertion-only method depends on which benchmark is being asked about. The reported differences are **21.34 BLEU points** (91.49 versus 70.15, a relative gain of roughly 30.4%) on the Caesar's cipher task, and **2.02 BLEU points** (37.57 versus 35.55, a relative gain of roughly 5.7%) on the second reported task ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Both favor the Insertion-Deletion Model, and in neither case does the source report a task on which the insertion-only model wins ([document_2.txt](document_2.txt)).

My assessment is that the 21.34-point result should be treated as the substantive finding of the comparison and the 2.02-point result as a smaller, directionally consistent but less firmly established effect, given the absence of variance reporting, the 1,000-example evaluation set, and the lack of model selection ([document_1.txt](document_1.txt)). The unresolved disagreement between the two sources over the name of the second benchmark should be flagged in any downstream citation of the 2.02-point figure, even though the figure itself is corroborated by both sources ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## References

Document 1. (n.d.). *document_1.txt* [Unpublished manuscript].

Document 2. (n.d.). *document_2.txt* [Unpublished manuscript].