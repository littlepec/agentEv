# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Prior Gated RNNs: A Technical Report

## 1. Purpose and Scope of the Report

This report answers a single, precise question: **how much improvement did the introduced models achieve compared with the previous models?** The introduced models are the Long Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN). The comparison targets are the previously established gated recurrent baselines, namely the standard Gated Recurrent Unit RNN (GRURNN) and the standard Long Short Term Memory RNN (LSTMRNN). Both proposed architectures are described as "a novel RNN architecture that combine the concepts of gating mechanism and the tensor product into a single model," in which the tensor product supplies a more expressive, direct interaction between the current input and the previous hidden layer ([Tjandra et al., n.d.](document_1.txt)).

The evaluation spans two language modeling tasks — character-level language modeling measured by bits-per-character (BPC) and word-level language modeling measured by perplexity (PPL) — both conducted on the PennTreeBank corpus ([Tjandra et al., n.d.](document_1.txt)). The report first establishes the evidence base, then presents the raw results, the absolute and relative deltas, the comparison against wider published literature, the fairness of the comparison, and finally an interpreted estimate of the true magnitude and nature of the improvement.

## 2. Evidence Base and Source-Reliability Assessment

Two documents are available. The first is the primary research paper itself, *Gated Recurrent Neural Tensor Network*, authored by Andros Tjandra, Sakriani Sakti, Ruli Manurung, Mirna Adriani and Satoshi Nakamura, affiliated with Universitas Indonesia and the Nara Institute of Science and Technology ([Tjandra et al., n.d.](document_1.txt)). The second is a third-party research note summarizing the same paper, which explicitly states that it addresses questions such as "how much improvement does tensor product gating bring to recurrent language models" ([Third-party research note, n.d.](document_2.txt)).

Because the third-party note is a secondary summary and the paper is the primary record containing the tables, equations, and experimental settings, the primary paper is treated throughout this report as the authoritative source. This hierarchy matters because the two documents disagree on one important number, discussed below.

### 2.1 A Material Discrepancy Between the Two Sources

The sources agree exactly on the character-level results. The note states that "GRURNTN reduced test BPC from 1.39 to 1.33, which is 0.06 absolute / 4.32% relative BPC, over GRURNN," and that "LSTMRNTN reduced BPC from 1.37 to 1.34, which is 0.03 absolute / 2.22% relative BPC, over LSTMRNN" ([Third-party research note, n.d.](document_2.txt)). These match the paper's Table I and its results narrative verbatim in substance ([Tjandra et al., n.d.](document_1.txt)).

The sources disagree on the word-level GRURNTN result. The note reports that "GRURNTN reduced test PPL from 97.78 to 92.98, which is 4.8 absolute / 4.91% relative PPL, over GRURNN" ([Third-party research note, n.d.](document_2.txt)), whereas the primary paper's Table II and results text place GRURNTN at **87.38** test PPL, corresponding to "1 0.4 absolute / 1 0.6 3% relative PPL" — that is, 10.40 absolute and 10.63% relative ([Tjandra et al., n.d.](document_1.txt)). The note's internally consistent but different arithmetic (4.8/97.78 ≈ 4.91%) indicates a transcription or record error rather than a different metric definition.

This report consequently adopts the primary paper's figures as the headline results — GRURNTN at 87.38 PPL, a 10.40 absolute / ~10.63% relative reduction — while reporting the note's more conservative figure alongside it so that the reader can see that, under either reading, the direction and statistical-materiality of the improvement are unchanged. A conservative bound of 4.8 absolute PPL still represents a near-5% relative gain, and the primary-source figure roughly doubles that.

## 3. What Was Changed: The Two Proposed Models and Their Baselines

The baseline GRURNN uses reset and update gates with a candidate hidden layer of the form f(x_t W_xh + (r_t ⊙ h_{t−1}) W_hh + b_h), i.e., linear projection plus addition followed by a nonlinearity ([Tjandra et al., n.d.](document_1.txt)). The baseline LSTMRNN uses input, forget and output gates with a separate memory cell, and its candidate cell is computed as tanh(x_t W_xc + h_{t−1} W_hc + b_c) ([Tjandra et al., n.d.](document_1.txt)).

GRURNTN inserts a tensor product between the current input and the reset-gated previous hidden state into the candidate hidden-layer computation, parameterized by a tensor weight; LSTMRNTN inserts the tensor product between the current input and the previous hidden layer into the candidate memory-cell equation ([Tjandra et al., n.d.](document_1.txt)). The authors justify this as increasing model expressiveness "by using second-degree polynomial interactions, compared to first-degree polynomial interactions on standard dot product followed by addition in common RNNs architecture" ([Tjandra et al., n.d.](document_1.txt)). They further adopt an asymmetric bilinear form that "reduce[s] the number of parameters from the original neural tensor network formulation," which is critical for the fairness of the later comparison ([Tjandra et al., n.d.](document_1.txt)).

## 4. Character-Level Language Modeling: Reported Improvements

### Table 1. PennTreeBank test-set BPC (lower is better)

| Model | Test BPC | Source status |
|---|---|---|
| NNLM | 1.57 | Published reference point |
| BPTT-RNN | 1.42 | Published reference point |
| HF-MRNN | 1.24 | Published reference point |
| sRNN | 1.39 | Published reference point |
| DOT(S)-RNN | 1.37 | Published reference point |
| **GRURNN (baseline)** | **1.39** | Paper baseline |
| **LSTMRNN (baseline)** | **1.37** | Paper baseline |
| **GRURNTN (proposed)** | **1.33** | Paper proposed |
| **LSTMRNTN (proposed)** | **1.34** | Paper proposed |

Values as reported in the paper's character-level results and Table I ([Tjandra et al., n.d.](document_1.txt)).

The paper states that "GRURNTN reduced the BPC from 1.39 to 1.33 (0.06 absolute / 4.32% relative BPC) from the baseline GRURNN, and LSTMRNTN reduced the BPC from 1.37 to 1.34 (0.03 absolute / 2.22% relative BPC) from the baseline LSTMRNN" ([Tjandra et al., n.d.](document_1.txt)). A direct recomputation of the LSTMRNTN relative figure from the displayed numbers yields 0.03/1.37 ≈ 2.19%, marginally below the 2.22% printed in the paper, a rounding-level inconsistency that does not affect the conclusion. Both proposed models produced lower BPC than their baselines "from the first epoch to the last epoch," and GRURNTN "slightly outperformed LSTMRNTN" on this task ([Tjandra et al., n.d.](document_1.txt)).

## 5. Word-Level Language Modeling: Reported Improvements

### Table 2. PennTreeBank test-set PPL (lower is better)

| Model | Test PPL | Source status |
|---|---|---|
| N-Gram | 141 | Published reference point |
| RNNLM (w/o dynamic evaluation) | 124.7 | Published reference point |
| RNNLM (w/ dynamic evaluation) | 123.2 | Published reference point |
| SCRNN | 115 | Published reference point |
| sRNN | 110.0 | Published reference point |
| DOT(S)-RNN | 107.5 | Published reference point |
| **GRURNN (baseline)** | **97.78** | Paper baseline |
| **LSTMRNN (baseline)** | **108.26** | Paper baseline |
| **GRURNTN (proposed)** | **87.38** | Paper proposed |
| **LSTMRNTN (proposed)** | **96.97** | Paper proposed |

Values as reported in the paper's word-level results and Table II ([Tjandra et al., n.d.](document_1.txt)).

The paper reports that "GRURNTN reduced the perplexity from 9 7.7 8 to 8 7.3 8 (1 0.4 absolute / 1 0.6 3% relative PPL) over the baseline GRURNN and LSTMRNTN reduced the perplexity from 1 0 8.2 6 to 9 6.9 7 (1 1.2 9 absolute / 1 0.4 2% relative PPL) over the baseline LSTMRNN" ([Tjandra et al., n.d.](document_1.txt)). Note that the tensor modification produced a conspicuously asymmetric effect: the GRU variant gained roughly 9% more relative ground than the LSTM variant (10.63% vs 10.42%).

## 6. Consolidated Improvement Summary

### Table 3. Absolute and relative improvement of proposed models over their matched baselines

| Task | Metric | Baseline model | Baseline score | Proposed model | Proposed score | Absolute gain | Relative gain |
|---|---|---|---|---|---|---|---|
| Character-level | Test BPC | GRURNN | 1.39 | GRURNTN | 1.33 | 0.06 | 4.32% |
| Character-level | Test BPC | LSTMRNN | 1.37 | LSTMRNTN | 1.34 | 0.03 | 2.22% |
| Word-level | Test PPL | GRURNN | 97.78 | GRURNTN | 87.38 | 10.40 | 10.63% |
| Word-level | Test PPL | LSTMRNN | 108.26 | LSTMRNTN | 96.97 | 11.29 | 10.42% |
| Word-level (alternative figure) | Test PPL | GRURNN | 97.78 | GRURNTN | 92.98 | 4.80 | 4.91% |

Rows 1–4 are from the primary paper ([Tjandra et al., n.d.](document_1.txt)); row 5 is the conflicting figure reported by the secondary note and is included only as a conservative boundary case ([Third-party research note, n.d.](document_2.txt)).

**Headline answer:** the proposed architectures improved over their matched baselines by approximately **0.03–0.06 BPC (2.2–4.3% relative)** on character-level modeling and by approximately **10.4–11.3 PPL (10.4–10.6% relative)** on word-level modeling, with GRURNTN delivering the largest single improvement in both absolute and relative terms at the word level ([Tjandra et al., n.d.](document_1.txt)).

## 7. Improvement Relative to the Wider Published Literature

The gains become more meaningful when placed against published reference points rather than only against the paper's own baselines. On character-level BPC, GRURNTN's 1.33 and LSTMRNTN's 1.34 both beat BPTT-RNN (1.42), sRNN (1.39) and DOT(S)-RNN (1.37), while remaining above the reported HF-MRNN figure of 1.24 ([Tjandra et al., n.d.](document_1.txt)). On word-level PPL, GRURNTN's 87.38 is the lowest value in the table, outperforming sRNN (110.0) by 22.62 PPL and DOT(S)-RNN (107.5) by 20.12 PPL, and LSTMRNTN's 96.97 also beats both of those published systems ([Tjandra et al., n.d.](document_1.txt)). The paper's own assessment is that "GRURNTN outperformed all the baseline models as well as the other models by a large margin," while LSTMRNTN "improved the LSTMRNN model and its performance closely resembles the baseline GRURNN" ([Tjandra et al., n.d.](document_1.txt)).

That last point deserves emphasis. LSTMRNTN's 96.97 PPL is only 0.81 PPL better than the GRURNN baseline's 97.78, a 0.83% relative edge ([Tjandra et al., n.d.](document_1.txt)). In other words, the LSTM-plus-tensor design essentially caught up to a plain GRU architecture on the word-level task rather than surpassing the best available gated design; the GRU-plus-tensor design is what actually moved the frontier.

## 8. Was the Comparison Fair?

The authors took deliberate steps to equalize capacity. They state that they "constrained our baseline GRURNN to have a similar number of parameters as the GRURNTN model for a fair comparison" and applied the same constraint between LSTMRNN and LSTMRNTN ([Tjandra et al., n.d.](document_1.txt)). The reported budgets are approximately 12 million free parameters for GRURNN and GRURNTN and approximately 13 million for LSTMRNN and LSTMRNTN at the word level, and roughly 2.2 million versus 2.6 million respectively at the character level ([Tjandra et al., n.d.](document_1.txt)).

A notable structural feature of the setup is that the tensor models achieved these results with far narrower hidden states. At the word level, GRURNTN and LSTMRNTN used 256 hidden units while GRURNN used 860 and LSTMRNN used 740, with all models using 128-dimensional word embeddings ([Tjandra et al., n.d.](document_1.txt)). At the character level, the proposed models used 256 hidden units against 820 for GRURNN and 600 for the LSTM baseline, with 32-dimensional character embeddings ([Tjandra et al., n.d.](document_1.txt)). The tensor models therefore reached superior scores with roughly one-third the hidden-state width, which is a strong indication that the tensor interaction is carrying representational load that the baselines must otherwise obtain from sheer width. This is my analytical inference from the reported configuration, not a claim made explicitly in the paper.

Regularization and optimization were largely matched: AdaGrad with mini-batch training of 15 sentences, a learning rate decay factor of 0.5 when development cost increased, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization in every model ([Tjandra et al., n.d.](document_1.txt)). One asymmetry exists: dropout was set to p = 0.5 for GRURNTN and LSTMRNTN but p = 0.6 for the baselines at the word level, while the character-level experiments used p = 0.25 ([Tjandra et al., n.d.](document_1.txt)). Heavier dropout on the baselines is a conservative design choice for the proposed models, since it slightly handicaps the comparison targets, but it also means the baselines were not tuned identically.

## 9. Interpretation: How Large Are the Improvements, Really?

My assessment is that the reported improvements are **task-dependent in magnitude and should not be read as a uniform gain**. On character-level modeling, the gains are real but modest: 4.32% relative for GRURNTN and 2.22% relative for LSTMRNTN are within the range one would expect from a well-tuned architectural refinement, and the paper itself frames the character-level result as both proposed models producing "lower BPC than our baseline models from the first epoch to the last epoch" ([Tjandra et al., n.d.](document_1.txt)). Notably, GRURNTN's character-level 1.33 matches a published LSTMRNN variant using adaptive noise regularization without dynamic evaluation, which tempers any claim of a decisive breakthrough on that task ([Tjandra et al., n.d.](document_1.txt)).

On word-level modeling, the GRURNTN result is materially stronger. A 10.40 absolute / 10.63% relative perplexity reduction is a substantial single-architecture change, and it is achieved at parity of parameter count against the baseline it replaces ([Tjandra et al., n.d.](document_1.txt)). Because perplexity is exponential in average cross-entropy, a 10% PPL reduction corresponds to a meaningful reduction in predictive uncertainty per token, which is the practical quantity of interest in language modeling. The fact that the same modification applied to the LSTM unit yielded a comparable relative reduction (10.42%) over its own baseline, but landed at 96.97 PPL rather than 87.38, suggests that the tensor interaction is not uniformly beneficial: the base architecture's starting point and its interaction with the gating topology matter a great deal. This asymmetry is the most interesting finding in the comparison and is not fully explained by the paper.

A second interpretive point concerns the conservative alternative figure of 92.98 PPL reported by the secondary note ([Third-party research note, n.d.](document_2.txt)). Even if the more conservative figure were correct, a 4.8 absolute / 4.91% relative word-level reduction and a 0.06 absolute / 4.32% relative character-level reduction would still constitute a consistent, directionally unambiguous improvement across both tasks and both base architectures. The disagreement between the sources therefore changes the estimated magnitude of the word-level GRU gain but not the sign or the qualitative conclusion.

## 10. Limitations and Caveats

Several caveats constrain how strongly these numbers should be generalized. First, the evaluation rests on a single corpus, PennTreeBank — sections 0–20 for training (930,000 words), 21–22 for validation (74,000 words) and 23–24 for testing (82,000 words), with vocabulary capped at the 10,000 most common words ([Tjandra et al., n.d.](document_1.txt)). No second dataset, no cross-domain transfer, and no speech or video experiments are reported, although the authors identify those as future work ([Tjandra et al., n.d.](document_1.txt)).

Second, the paper reports no repeated runs, no variance estimates, and no statistical significance testing, so the 0.03 BPC character-level LSTMRNTN gain in particular could plausibly overlap with run-to-run noise. Third, no ablation isolates the contribution of the tensor product from the contribution of the asymmetric bilinear parameterization; the authors note only that the asymmetric form reduces the parameter count relative to the original neural tensor network formulation ([Tjandra et al., n.d.](document_1.txt)). Fourth, the source text extracted for this report contains OCR-level corruption in the results tables, so the reported reference-point values in Tables 1 and 2 above should be treated as faithful to the visible figures but not as a re-verified dataset.

Fifth, the work is dated. Its latest cited references are 2015 arXiv preprints on gated feedback recurrent networks and long short-term memory over tree structures ([Tjandra et al., n.d.](document_1.txt)), placing the experiments roughly a decade before the current date of 2026. The internal comparison between proposed and baseline models remains valid as a controlled, contemporaneous experiment, but the word-level perplexity values should not be compared against modern language modeling systems.

Finally, the source discrepancy documented in Section 2.1 means that a reader relying solely on the secondary note would underestimate the word-level GRURNTN gain by more than half.

## 11. Conclusion

The introduced models achieved a consistent but uneven improvement over the previous models. In direct answer to the question: **GRURNTN improved over GRURNN by 0.06 absolute BPC (4.32% relative) on character-level language modeling and by 10.40 absolute PPL (10.63% relative) on word-level language modeling; LSTMRNTN improved over LSTMRNN by 0.03 absolute BPC (2.22% relative) and 11.29 absolute PPL (10.42% relative)** ([Tjandra et al., n.d.](document_1.txt)). A secondary source reports a smaller GRURNTN word-level gain of 4.8 absolute / 4.91% relative PPL, a discrepancy this report attributes to a transcription error in the secondary note, since the primary paper's table shows 87.38 PPL ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., n.d.](document_1.txt)).

The overall pattern is that the tensor-augmented architectures delivered their largest practical benefit on the word-level task and on the GRU backbone, where GRURNTN became the strongest model reported in the comparison, outperforming every published reference point and every internal baseline ([Tjandra et al., n.d.](document_1.txt)). On character-level modeling the gains are modest, and on the LSTM backbone the word-level gain, while proportionally comparable, only carried LSTMRNTN to rough parity with the plain GRU baseline ([Tjandra et al., n.d.](document_1.txt)). The authors' own conclusion is that both proposed models "outperformed the baseline models with a similar number of parameters in character-level language modeling and word-level language modeling tasks," a claim the numbers support, while the magnitude of that outperformance is best described as decisive at the word level for GRURNTN and incremental elsewhere ([Tjandra et al., n.d.](document_1.txt)).

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network* [Manuscript]. Faculty of Computer Science, Universitas Indonesia; Graduate School of Information Science, Nara Institute of Science and Technology. [document_1.txt](document_1.txt)

Third-party research note. (n.d.). *Third-party research note: Gated recurrent neural tensor network* [Research note]. [document_2.txt](document_2.txt)