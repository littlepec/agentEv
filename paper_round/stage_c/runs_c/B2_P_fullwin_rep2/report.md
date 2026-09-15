# BLEU Score Differences Between the Proposed Insertion-Deletion Transformer and the Insertion-Only (KERMIT) Baseline

## 1. Purpose and Scope of This Report

This report answers the question of how large the BLEU score ("BELU" in the query) difference is between the proposed approach and the insertion-only method. The proposed approach is the **Insertion-Deletion Transformer**, a transformer-based neural architecture and training method for sequence generation that couples an insertion phase with a deletion phase executed iteratively (Ruis et al., 2020). The insertion-only baseline is the **Insertion Model (KERMIT)**, which extends the Insertion Transformer's insertion-only framework to handle insertions (Chan et al., 2019, as cited in Ruis et al., 2020). The paper extends that insertion-only framework to handle both insertions and deletions, producing the Insertion-Deletion Model for direct comparison ([third-party research note](document_2.txt)).

The central finding is that the comparison is **not reported as a single overall number**. Instead, the paper reports two separate per-task BLEU differences on two synthetic translation datasets, both favoring the insertion-deletion model (Ruis et al., 2020).

## 2. Direct Answer in Headline Numbers

The BLEU score difference between the proposed Insertion-Deletion Model and the insertion-only Insertion Model (KERMIT) is as follows:

| Task | Insertion-Only Model (KERMIT) | Insertion-Deletion Model | Difference (BLEU points) | Relative change |
|---|---|---|---|---|
| Alphabetic Sequence Shifting | 70.15 | 91.49 | **+21.34** | +30.4% |
| Caesar's Cipher | 35.55 | 37.57 | **+2.02** | +5.7% |

The first row is reported in Table 2 of the primary source, captioned "BLEU scores for the sequence shifting task," and the second row is reported in Table 3, captioned "BLEU scores for the Caesar's cipher task" (Ruis et al., 2020). The Caesar's cipher improvement is described by the authors themselves as an increase of "around 2 BLEU points" over the insertion-only model (Ruis et al., 2020). The third-party research note agrees on both magnitudes — 21.34 and 2.02 BLEU points — although it reverses the task labels, a discrepancy discussed in Section 6 ([third-party research note](document_2.txt)).

Therefore, the honest answer to the query is: **the difference is +21.34 BLEU points on the shifted alphabetic sequence task and +2.02 BLEU points on the Caesar's cipher task, with no aggregated or overall BLEU difference reported anywhere in the paper.** Any single figure quoted as "the" BLEU difference would misrepresent the paper's reporting practice.

## 3. Experimental Conditions Behind the Numbers

Understanding the magnitude of the differences requires the experimental context in which they were obtained. Both tasks are synthetic character-based translation tasks; the paper presents the insertion-deletion framework as a proof of concept at this stage (Ruis et al., 2020).

| Aspect | Alphabetic Sequence Shifting | Caesar's Cipher |
|---|---|---|
| Task type | Shift each character of an alphabetic run by a fixed offset | Replace each letter by one shifted some positions down the alphabet |
| Sequence length sampling | min n = 3, max n = 10 (Ruis et al., 2020) | min n = 3, max n = 25 (Ruis et al., 2020) |
| Training examples | 1,000 | 100,000 |
| Held-out evaluation examples | 100 | 1,000 |
| Training steps | 200k | 200k |
| Batch size | 32 | 32 |
| Model selection | None performed | None performed |

A critical methodological detail shared by both tasks is that the authors "perform no model selection," training for a fixed 200k steps at a fixed batch size of 32 in each case (Ruis et al., 2020). This means the reported BLEU figures are single-run, checkpoint-less evaluations rather than the best-of-several-seeds results that are common in machine translation benchmarking.

The architectural difference between the two systems is deliberately minimal. Both are built on the insertion framework, and the Insertion-Deletion Transformer is implemented as "a simple stack of two Transformer decoders, where the top deletion transformer layer gets its signal from the bottom insertion transformer" (Ruis et al., 2020). The deletion model receives its training signal on-policy, directly from the current output of the insertion model, so that it learns to correct the insertion model's actual errors rather than a teacher-forced approximation of them (Ruis et al., 2020).

## 4. Task-by-Task Breakdown of the Differences

### 4.1 Alphabetic Sequence Shifting: +21.34 BLEU Points

In the sequence-shifting task, a sequence length is sampled uniformly between 3 and 10, a starting token is sampled uniformly, and the alphabetic sequence is completed to the required length; each letter is then shifted by the maximum length so that source and target sequences do not overlap (Ruis et al., 2020). An illustrative example given in the paper maps the source `c d e f g` to the target `m n o p q` (Ruis et al., 2020).

On this task, the insertion-only model achieves 70.15 BLEU while the insertion-deletion model achieves 91.49 BLEU, a difference of 21.34 BLEU points in favor of the insertion-deletion model (Ruis et al., 2020). The paper states that "our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task" (Ruis et al., 2020). In relative terms, this represents an improvement of roughly 30.4% over the baseline's BLEU score.

The paper also provides a qualitative decoding trace for this task (Table 1). In that trace, the insertion model predicts a duplicate token `u` at a target location, producing the hypothesis `o p q r u u v w`; the deletion model then predicts deletion of one `u`, yielding the corrected output `o p q r u v w` (Ruis et al., 2020). This single example encapsulates the mechanism the authors claim drives the BLEU gain: the deletion phase undo the mistakes made by the insertion model, because it is trained on the on-policy errors of the insertion phase (Ruis et al., 2020).

### 4.2 Caesar's Cipher: +2.02 BLEU Points

In the Caesar's cipher task, the sequences are not constrained to alphabetic order, so the diversity of input sequences is much larger than in the previous task; the shift is by max n = 25, and one example maps source `h k b e t` to target `g j a d s` (Ruis et al., 2020). Training uses 100k examples with evaluation on 1,000 held-out examples (Ruis et al., 2020).

Here the insertion-only model scores 35.55 BLEU and the insertion-deletion model scores 37.57 BLEU, a difference of 2.02 BLEU points (Ruis et al., 2020). The paper describes this result as the deletion model "again increas[ing] the BLEU score over just the insertion model, by around 2 BLEU points" (Ruis et al., 2020). Relatively, this is approximately a 5.7% improvement over the baseline.

## 5. Consolidated Comparison of the Two Reported Differences

| Comparison Dimension | Alphabetic Shifting | Caesar's Cipher |
|---|---|---|
| Absolute BLEU gain | +21.34 points | +2.02 points |
| Relative BLEU gain | ≈ +30.4% | ≈ +5.7% |
| Table in primary source | Table 2 (Ruis et al., 2020) | Table 3 (Ruis et al., 2020) |
| Authors' own characterization | "Significantly" outperforms the insertion-only model (Ruis et al., 2020) | "Around 2 BLEU points" (Ruis et al., 2020) |
| Training data volume | 1,000 examples | 100,000 examples |
| Evaluation set size | 100 examples | 1,000 examples |

The arithmetic mean of the two absolute differences is 11.68 BLEU points, but this average is **not** reported in the paper and should not be presented as the paper's headline result; it is included here only as a descriptive summary of the two data points ([third-party research note](document_2.txt); Ruis et al., 2020).

## 6. Reconciling the Primary Source and the Third-Party Note

A notable inconsistency exists between the two provided sources, and it matters for anyone citing these numbers.

The **primary source** — the paper itself — presents Table 2 under the heading "Alphabetic Sequence Shifting BLEU" with 70.15 for the Insertion Model (KERMIT) and 91.49 for the Insertion Deletion Model, and Table 3 under the heading "Caesar's Cipher BLEU" with 35.55 and 37.57 respectively (Ruis et al., 2020). The narrative sentences surrounding these tables reinforce the mapping: the caption of Table 2 reads "BLEU scores for the sequence shifting task," while the Caesar's cipher discussion states that the deletion model increases BLEU "by around 2 BLEU points" (Ruis et al., 2020).

The **third-party research note**, by contrast, attributes 91.49 versus 70.15 to the Caesar's cipher task and 37.57 versus 35.55 to the shifted alphabetic sequence task ([third-party research note](document_2.txt)). It additionally cites "Table 2" for the Caesar's cipher results and "Table 3" for the sequence-shifting results, reversing the paper's own table captions ([third-party research note](document_2.txt)).

Crucially, however, the two sources agree on the *magnitudes* of the differences: 21.34 BLEU points for the larger gap and 2.02 BLEU points for the smaller gap ([third-party research note](document_2.txt); Ruis et al., 2020). Because the query concerns magnitude rather than task assignment, the answer is robust to this labeling dispute. That said, the assignment of tasks to numbers should be taken from the primary source: the 21.34-point gain belongs to the shifted alphabetic sequence task (Table 2), and the 2.02-point gain belongs to Caesar's cipher (Table 3) (Ruis et al., 2020).

## 7. Interpreting the Difference in Magnitudes

The most striking pattern in the reported results is the inversion between task difficulty and gain size. The alphabetic sequence shifting task is described in the paper as one that "should be trivial to solve for a powerful sequence to sequence model implemented with Transformers," whereas Caesar's cipher has far greater input diversity because the sequences "do not need to be in alphabetic order" (Ruis et al., 2020). Yet the supposedly trivial task exhibits the much larger gain (+21.34) and the harder cipher task the smaller gain (+2.02) (Ruis et al., 2020).

The paper's own mechanistic explanation — that the deletion phase can undo the mistakes made by the insertion model because it is trained on on-policy errors — suggests why this may occur (Ruis et al., 2020). In a rigidly structured task, the insertion model's errors are likely to be systematic and predictable (for example, a duplicate letter inside a strictly ordered sequence, as shown in the decoding trace), which is precisely the sort of error a deletion model trained on on-policy insertion failures can learn to remove reliably (Ruis et al., 2020). In a more diverse cipher task, errors are more varied, and a single deletion pass may have fewer systematic patterns to exploit.

It is also relevant that the paper tested an adversarial sampling scheme intended to guarantee the deletion model always receives a learning signal, and reports that this scheme "did not improve BLEU scores on these synthetic tasks," though the authors note it may still be helpful when the insertion model is so accurate that it produces no errors at all (Ruis et al., 2020). The +21.34 and +2.02 figures therefore reflect the plain on-policy configuration, not the adversarial variant.

## 8. Caveats, Limitations, and Threats to Validity

Several considerations constrain how much weight these BLEU differences can bear:

First, the datasets are synthetic character-level translation tasks, and the authors explicitly frame the work as "a proof of concept," stating that future work should verify the capabilities of the model on non-synthetic data for tasks like machine translation, paraphrasing, and style transfer (Ruis et al., 2020). No non-synthetic BLEU results are reported in the provided material.

Second, no model selection was performed, so the reported numbers are fixed-step snapshots rather than tuned results, and no variance across random seeds is reported (Ruis et al., 2020). The sequence-shifting evaluation uses only 100 held-out examples (Ruis et al., 2020), a small evaluation sample whose confidence intervals are not quantified in the paper.

Third, the paper does not report a statistical significance test; the word "significantly" is used in a descriptive sense — "Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task" (Ruis et al., 2020) — rather than as a claim backed by a hypothesis test.

Fourth, the paper explicitly positions itself as a simplified alternative to a concurrent insertion-deletion system, the Levenshtein Transformer (LevT), which uses an expert policy requiring dynamic programming over Levenshtein distance and requires an extra classifier and Transformer pass to predict the number of tokens to insert (Gu et al., 2019b, as cited in Ruis et al., 2020). No head-to-head BLEU comparison against that system is provided in the supplied information, so the reported differences are specifically against the KERMIT-style insertion-only baseline.

Finally, the abstract's summary claim — "obtaining significant BLEU score improvement over an insertion-only model" — is a task-specific statement, not an average across benchmarks (Ruis et al., 2020).

## 9. Conclusion

The BLEU score difference between the proposed Insertion-Deletion Transformer and the insertion-only Insertion Model (KERMIT) is reported per task rather than as a single figure. The difference is **+21.34 BLEU points on the alphabetic sequence shifting task** (70.15 to 91.49) and **+2.02 BLEU points on the Caesar's cipher task** (35.55 to 37.57), with the latter characterized by the authors as roughly a two-point gain (Ruis et al., 2020). Both differences favor the proposed approach, and the third-party note concurs on these two magnitudes, even though it reverses the task labels relative to the primary source ([third-party research note](document_2.txt)). Because the paper reports no overall, aggregate, or statistically tested BLEU difference, the most accurate answer to the query is that the advantage amounts to approximately 21.3 BLEU points on one synthetic task and approximately 2 BLEU points on the other.

## References

Ruis, L., Stern, M., Proskurnia, J., & Chan, W. (2020). *Insertion-Deletion Transformer* (arXiv:2001.05540). arXiv. https://arxiv.org/abs/2001.05540

[Third-party research note: Insertion-Deletion Transformer](document_2.txt)