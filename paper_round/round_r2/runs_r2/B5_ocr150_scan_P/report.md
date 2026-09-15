# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Prior Gated RNN Baselines in Language Modeling

## 1. Purpose and Scope of This Report

This report addresses a single question: **how much improvement do the models introduced in "Gated Recurrent Neural Tensor Network" achieve relative to the previous (baseline) models?** The paper under examination proposes two hybrid recurrent architectures — the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) — and evaluates them against two prior gated recurrent baselines, GRURNN and LSTMRNN, on the Penn Treebank corpus ([Tjandra et al., n.d.](document_1.txt)). The evaluation spans two tasks: word-level language modeling, measured by perplexity (PPL), and character-level language modeling, measured by bits-per-character (BPC), with lower values indicating better performance in both cases ([Tjandra et al., n.d.](document_1.txt)).

The core finding, stated in the paper's own conclusion, is that the proposed tensor-augmented gated models outperformed their corresponding baselines at both levels of granularity while holding the number of free parameters approximately constant ([Tjandra et al., n.d.](document_1.txt)). A third-party research note summarizing the same work reaches an identical directional conclusion, although — as discussed in Section 6 — it reports one materially different numeric value for the word-level GRURNTN result ([Third-Party Research Note, n.d.](document_2.txt)).

## 2. What the Proposed Models Actually Change

Both proposed architectures are constructed by inserting a tensor (bilinear) product operation into an existing gated recurrent unit. In GRURNTN, the tensor product is applied between the current input and the previous hidden layer *after* multiplication by the reset gate, substituting for part of the standard candidate-hidden-layer computation ([Tjandra et al., n.d.](document_1.txt)). In LSTMRNTN, the tensor product is applied between the current input and the previous hidden layer to compute the current memory cell, with each slice of the tensor weight being a matrix ([Tjandra et al., n.d.](document_1.txt)).

The paper's stated rationale is that standard RNN interactions between the current input and previous hidden state are produced by linear projection, addition, and a nonlinearity — which the authors characterize as a "shallow" transition using only first-degree polynomial interactions ([Tjandra et al., n.d.](document_1.txt)). By using a tensor product, the model gains second-degree polynomial interaction terms, increasing expressiveness, while the gating mechanism supplies the long-range memory that purely tensor-based recursive models lack ([Tjandra et al., n.d.](document_1.txt)).

A second, practically important design decision is that the authors adopt an *asymmetric* bilinear form rather than the full tensor formulation, explicitly to reduce the parameter count ([Tjandra et al., n.d.](document_1.txt)). This matters for the interpretation of the results: the reported gains are not obtained by simply making the models larger, because the paper also constrained the baselines to have parameter counts similar to the proposed models for a fair comparison ([Tjandra et al., n.d.](document_1.txt)).

## 3. Experimental Setup and Configuration

All experiments used the Penn Treebank (PTB) corpus, a standard benchmark for statistical language modeling drawn from the Wall Street Journal corpus, with the vocabulary limited to the 10,000 most common words and all other words mapped to an `<unk>` token ([Tjandra et al., n.d.](document_1.txt)). The data were divided into a training set of sections 0–20 (930,000 words), a validation set of sections 21–22 (74,000 words), and a test set of sections 23–24 (82,000 words) ([Tjandra et al., n.d.](document_1.txt)).

Optimization used AdaGrad with mini-batches of 15 sentences, a learning-rate decay factor of 0.5 when development-set cost increased, gradient rescaling when the gradient norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., n.d.](document_1.txt)). Notably, the authors state that their baseline and proposed-model experiments did *not* use dynamic evaluation, whereas some published comparison numbers in their tables did ([Tjandra et al., n.d.](document_1.txt)).

Table 1 summarizes the model configurations, which are relevant because they show that parameter parity was achieved while the proposed models used substantially *fewer* hidden units — the tensor weights absorbed the capacity.

### Table 1. Model configurations as reported

| Setting | GRURNN (baseline) | GRURNTN (proposed) | LSTMRNN (baseline) | LSTMRNTN (proposed) |
|---|---|---|---|---|
| Word-level hidden units | 860 | 256 | 740 | 256 |
| Char-level hidden units | 820 | 256 | 600 | 256 |
| Word embedding dim. | 128 | 128 | 128 | 128 |
| Char embedding dim. | 32 | 32 | 32 | 32 |
| Dropout (word-level) | p = 0.6 | p = 0.5 | p = 0.6 | p = 0.5 |
| Dropout (char-level) | p = 0.25 | p = 0.25 | p = 0.25 | p = 0.25 |
| Approx. free params (word) | ~12M | ~12M | ~13M | ~13M |

*Source: ([Tjandra et al., n.d.](document_1.txt)). The paper reports approximately 12 million free parameters for GRURNN/GRURNTN and approximately 13 million for LSTMRNN/LSTMRNTN at word level, and approximately 2.2 million for GRURNN/GRURNTN and approximately 2.6 million for LSTMRNN/LSTMRNTN at character level ([Tjandra et al., n.d.](document_1.txt)).*

An important interpretive detail is visible in Table 1: at the word level the baselines were trained with *stronger* dropout (p = 0.6) than the proposed models (p = 0.5), so the reported gains cannot be attributed to a regularization advantage favoring the proposed models ([Tjandra et al., n.d.](document_1.txt)).

## 4. Character-Level Language Modeling: Reported Improvements

At the character level, the paper reports that both proposed models produced lower BPC than the baselines from the first epoch to the last, based on validation-set curves ([Tjandra et al., n.d.](document_1.txt)). The paper also notes that GRURNN progressed faster than LSTMRNN early on, but that LSTMRNN eventually converged to a better BPC, while GRURNTN made faster and quicker progress than LSTMRNTN and converged to a similar BPC in the final epoch ([Tjandra et al., n.d.](document_1.txt)).

### Table 2. Character-level test BPC on PTB

| Model | Test BPC | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| GRURNTN (proposed) | 1.33 | −0.06 | −4.32% |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNTN (proposed) | 1.34 | −0.03 | −2.22% |

*Source: ([Tjandra et al., n.d.](document_1.txt)); corroborated by ([Third-Party Research Note, n.d.](document_2.txt)).*

Both source documents agree exactly on these figures: GRURNTN reduced BPC from 1.39 to 1.33, a 0.06 absolute and 4.32% relative reduction over GRURNN, and LSTMRNTN reduced BPC from 1.37 to 1.34, a 0.03 absolute and 2.22% relative reduction over LSTMRNN ([Third-Party Research Note, n.d.](document_2.txt)). The paper's summary states that, overall, GRURNTN slightly outperformed the baseline models on the character-level task ([Tjandra et al., n.d.](document_1.txt)).

Several cross-family comparisons can be derived directly from the test figures, although the paper itself does not state them: GRURNTN at 1.33 is 0.04 BPC below the LSTMRNN baseline of 1.37 (about 2.9% relative), and LSTMRNTN at 1.34 is 0.05 BPC below the GRURNN baseline of 1.39 (about 3.6% relative). The gap between the two proposed models is only 0.01 BPC, roughly 0.75% relative, indicating that at the character level the choice of underlying gate unit mattered far less than the addition of the tensor product.

## 5. Word-Level Language Modeling: Reported Improvements

At the word level the reported gains are considerably larger than at the character level. The paper states that GRURNTN reduced perplexity from 97.78 to 87.38, a 10.4 absolute and 10.63% relative reduction over the GRURNN baseline, while LSTMRNTN reduced perplexity from 108.26 to 96.97, an 11.29 absolute and 10.42% relative reduction over the LSTMRNN baseline ([Tjandra et al., n.d.](document_1.txt)).

### Table 3. Word-level test perplexity on PTB

| Model | Test PPL | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| GRURNTN (proposed) — value in primary paper | 87.38 | −10.40 | −10.63% |
| GRURNTN (proposed) — value in third-party note | 92.98 | −4.80 | −4.91% |
| LSTMRNN (baseline) | 108.26 | — | — |
| LSTMRNTN (proposed) | 96.97 | −11.29 | −10.42% |

*Sources: primary values and LSTMRNTN from ([Tjandra et al., n.d.](document_1.txt)); alternative GRURNTN value from ([Third-Party Research Note, n.d.](document_2.txt)).*

The paper characterizes GRURNTN as the best model on this task, with a consistently lower PPL than the other models, and states that it outperformed all baseline models as well as the other models "by a large margin" ([Tjandra et al., n.d.](document_1.txt)). By contrast, LSTMRNTN is described as improving on LSTMRNN while performing *close to* the GRURNN baseline ([Tjandra et al., n.d.](document_1.txt)) — a description consistent with the numbers, since 96.97 versus 97.78 leaves only a 0.81 PPL (approximately 0.83% relative) difference.

Two derived observations sharpen the picture. First, both proposed models deliver a strikingly similar *relative* improvement over their own baselines: approximately 10.6% for GRURNTN and approximately 10.4% for LSTMRNTN. Second, the *absolute* benefit is larger for LSTMRNTN (11.29 PPL) than for GRURNTN (10.40 PPL) simply because LSTMRNN starts from a much weaker baseline (108.26) than GRURNN (97.78). In other words, the tensor product appears to confer a roughly constant relative advantage on the gated unit to which it is attached, rather than specifically favoring GRU over LSTM.

## 6. Discrepancy in the Reported GRURNTN Word-Level Result

The two provided sources conflict on one number, and this conflict must be flagged for any careful reader. The primary paper reports the GRURNTN test perplexity as 87.38, giving a 10.4 absolute / 10.63% relative reduction over GRURNN ([Tjandra et al., n.d.](document_1.txt)). The third-party research note instead reports GRURNTN at 92.98, giving a 4.8 absolute / 4.91% relative reduction over GRURNN ([Third-Party Research Note, n.d.](document_2.txt)). Both figures are internally consistent with their own percentage calculations (10.40/97.78 ≈ 10.6%; 4.80/97.78 ≈ 4.9%), which means the discrepancy is not a simple arithmetic slip but a difference in the underlying test value transcribed or retained.

For two reasons, this report treats 87.38 as the more probable figure. First, the primary paper is the source of record and states the value consistently in its results narrative, its conclusion, and its test-set table ([Tjandra et al., n.d.](document_1.txt)). Second, the conclusion of the primary paper explicitly repeats "10.4 absolute (10.63% relative) PPL reduction over GRURNN" as one of the study's headline contributions ([Tjandra et al., n.d.](document_1.txt)). The third-party note is a secondary summary and, in the same paragraph, reproduces the LSTMRNTN values exactly as the primary paper states them, suggesting a localized transcription difference for GRURNTN only ([Third-Party Research Note, n.d.](document_2.txt)). Regardless of which value is correct, the *direction and existence* of the improvement is consistent across both sources, and the LSTMRNTN word-level and both character-level results are undisputed.

## 7. Comparison Against Published Benchmarks

The paper also situates its results against previously published systems on the same dataset. The primary paper's tables, which are partially corrupted in the available text, list older word-level results including an N-gram baseline at 124.7 PPL, RNNLM variants at approximately 123.2–124.7 PPL, SCRNN at 115 PPL, and DOT(S)-RNN at 107.5 PPL ([Tjandra et al., n.d.](document_1.txt)). Measured against these figures, GRURNTN at 87.38 PPL is approximately 20.12 PPL better than DOT(S)-RNN (about 18.7% relative), approximately 27.62 PPL better than SCRNN (about 24.0% relative), and approximately 37.32 PPL better than the N-gram model (about 29.9% relative). These derived comparisons should be read with caution, because the paper notes that its own experiments omitted dynamic evaluation while some comparison entries used it ([Tjandra et al., n.d.](document_1.txt)).

At the character level, the paper's Table I lists published results including HF-MRNN at 1.57 BPC, BPTT-RNN at 1.42, SRNN at 1.41, an LSTM variant with adaptive noise at 1.26, and a DOT(S)-RNN result of 1.24 ([Tjandra et al., n.d.](document_1.txt)). Although the available transcription of this table is OCR-degraded and the row-to-value mapping cannot be verified with full confidence, the highest-confidence reading is that the best published comparison value cited (1.24 BPC) remains slightly below the proposed models' 1.33 and 1.34 BPC. This is a meaningful qualification: the tensor-augmented models improve substantially on *their own* gated baselines but do not set a new published state of the art on the character-level task as reported in this table.

## 8. Interpretation and Assessment

My assessment, based strictly on the evidence provided, is that the reported improvements are real and consistent in direction but uneven in magnitude, and that the strength of the claim depends heavily on the task.

**At word level, the improvement is substantial and well supported.** Both proposed models reduce perplexity by more than 10% relative to their own baselines, and GRURNTN is described as the best-performing model tested ([Tjandra et al., n.d.](document_1.txt)). Because the baselines were deliberately matched for parameter count and were even trained with stronger dropout at this level ([Tjandra et al., n.d.](document_1.txt)), the gain is plausibly attributable to the tensor product rather than to capacity or regularization. This is the strongest part of the paper's case.

**At character level, the improvement is modest in absolute terms.** Reductions of 0.06 and 0.03 BPC are small on an absolute scale, and the relative reductions of 4.32% and 2.22% are correspondingly modest ([Tjandra et al., n.d.](document_1.txt)). A 0.01 BPC spread between the two proposed models — well within the range that single-run hyperparameter or initialization variation can produce — makes the ranking between GRURNTN and LSTMRNTN at this level difficult to defend on the evidence presented.

**The two model families benefit differently.** GRURNTN is the more decisive improvement in that it becomes the best model on both tasks and beats both baselines, whereas LSTMRNTN essentially lifts the LSTM family up to the level of the GRU baseline at word level (96.97 vs. 97.78 PPL) ([Tjandra et al., n.d.](document_1.txt)). Read this way, the tensor product provides a larger marginal benefit to the weaker architecture (LSTM) than to the stronger one (GRU) in absolute word-level terms, even though the relative gains are nearly identical.

**Confidence is limited by reporting practices.** The paper reports no statistical significance testing, no multiple random seeds, and no variance estimates; each configuration appears to have been run once with a single hyperparameter set ([Tjandra et al., n.d.](document_1.txt)). Only one dataset (PTB) and one language (English) are used. No dynamic evaluation was applied in the authors' own runs, which limits direct comparability with dynamic-evaluation baselines ([Tjandra et al., n.d.](document_1.txt)). The unresolved 87.38 vs. 92.98 discrepancy in Section 6 further reduces confidence in the exact magnitude of the strongest single claim, though not in its direction ([Third-Party Research Note, n.d.](document_2.txt)).

## 9. Conclusion

To answer the query directly: relative to the previous models, the introduced models reduced character-level BPC from 1.39 to 1.33 for the GRU family (−0.06 absolute, −4.32% relative) and from 1.37 to 1.34 for the LSTM family (−0.03 absolute, −2.22% relative), and reduced word-level perplexity from 97.78 to 87.38 for the GRU family (−10.4 absolute, −10.63% relative) and from 108.26 to 96.97 for the LSTM family (−11.29 absolute, −10.42% relative) ([Tjandra et al., n.d.](document_1.txt)). These gains were obtained with approximately matched parameter counts and without stronger regularization than the baselines ([Tjandra et al., n.d.](document_1.txt)). The word-level improvements are the substantive contribution; the character-level improvements are real but marginal, and GRURNTN emerges as the clearer winner of the two proposed architectures. The authors outline future work combining the approach with stacked architectures such as Gated Feedback RNN and applying it to speech and video recognition ([Tjandra et al., n.d.](document_1.txt)).

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network* [Research paper]. document_1.txt.

Third-party research note: Gated recurrent neural tensor network. (n.d.). document_2.txt.