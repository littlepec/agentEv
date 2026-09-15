# How Much Improvement Do Gated Recurrent Neural Tensor Networks Achieve Over Previous Recurrent Language Models?

## 1. Purpose and Scope of This Report

This report quantifies, in absolute and relative terms, the performance gains reported for two new recurrent architectures — the Long-Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) — relative to their gated recurrent baselines, LSTMRNN and GRURNN, on Penn Treebank (PTB) word-level and character-level language modeling tasks ([Tjandra et al., n.d.](document_1.txt)). The source paper claims that "our proposed models significantly improved their performance compared to our baseline models," and that these gains were obtained "with a similar number of parameters" as the baselines ([Tjandra et al., n.d.](document_1.txt)). An independent third-party research note restates the same conclusion: both proposed models "produced lower test scores than their corresponding baselines and outperformed the baseline models in character-level and word-level language modeling tasks with a similar number of parameters" ([Research Note, n.d.](document_2.txt)).

The direct answer to the query is that the introduced models deliver **two-digit relative improvements in word-level perplexity (10.42%–10.63%)** and **more modest relative improvements in character-level bits-per-character (2.22%–4.32%)**, with GRURNTN producing the largest single gain in each task and GRURNTN achieving the best absolute score of the four models in both evaluations ([Tjandra et al., n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)).

## 2. What Was Actually Changed in the Architecture

### 2.1 The Baseline Models

The two baselines are established gated recurrent units. The LSTM RNN uses three gating layers (input, forget, and output gates) together with memory cells that store information across time; the input gate retains useful candidate memory values, the forget gate retains previous memory, and the output gate filters which memory values reach the output or next hidden layer ([Tjandra et al., n.d.](document_1.txt)). The GRU RNN has no separated memory cells and only two gates (reset and update), yet "the GRU can match LSTM's performance and its convergence" despite having one fewer gating layer ([Tjandra et al., n.d.](document_1.txt)).

### 2.2 The Proposed Hybrid Models

The innovation is the combination of two previously separate ideas: (i) gating mechanisms, which allow an RNN to "remember and forget previous information" and to backpropagate error "without suffering from vanishing or exploding gradient problems," and (ii) tensor products, which replace first-degree dot-product-plus-addition interactions with second-degree polynomial interactions between the current input and the previous hidden layer ([Tjandra et al., n.d.](document_1.txt)). In GRURNTN, the tensor product is computed between the current input and the reset-gate-modulated previous hidden layer in the candidate hidden layer equation; in LSTMRNTN, the tensor product is inserted into the cell update that computes the current memory cell ([Tjandra et al., n.d.](document_1.txt)). The authors adopt a simplified asymmetric bilinear form to "reduce the number of parameters from the original neural tensor network formulation" while preserving input–hidden interaction ([Tjandra et al., n.d.](document_1.txt)). The paper emphasizes that, to the best of the authors' knowledge, "none of these works combined the gating mechanism and tensor product concepts into a single neural network architecture" ([Tjandra et al., n.d.](document_1.txt)).

## 3. Experimental Protocol

All experiments used the PTB corpus, a subset of the Wall Street Journal corpus, split into a training set of 930,000 words (sections 0–20), a validation set of 74,000 words (sections 21–22), and a test set of 82,000 words (sections 23–24), with vocabulary limited to the 10,000 most common words and out-of-vocabulary words mapped to a `<unk>` token ([Tjandra et al., n.d.](document_1.txt)). Word-level performance was measured with perplexity (PPL) and character-level performance with bits-per-character (BPC) ([Tjandra et al., n.d.](document_1.txt)). Optimization used AdaGrad with mini-batches of 15 sentences, a learning-rate decay factor of 0.5, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., n.d.](document_1.txt)). Crucially for fairness, the authors "constrained our baseline GRURNN to have a similar number of parameters as the GRURNTN model" and applied the same constraint to the LSTM pair ([Tjandra et al., n.d.](document_1.txt)).

### Table 1. Parameter Budgets and Architectural Settings

| Task | Model | Hidden Units | Embedding Dim. | Dropout | Approx. Free Parameters |
|---|---|---|---|---|---|
| Word-level | GRURNN (baseline) | 860 | 128 | 0.6 | ~12M |
| Word-level | GRURNTN (proposed) | 256 | 128 | 0.5 | ~12M |
| Word-level | LSTMRNN (baseline) | 740 | 128 | 0.6 | ~13M |
| Word-level | LSTMRNTN (proposed) | 256 | 128 | 0.5 | ~13M |
| Character-level | GRURNN (baseline) | 820 | 32 | 0.25 | ~2.2M |
| Character-level | GRURNTN (proposed) | 256 | 32 | 0.25 | ~2.2M |
| Character-level | LSTMRNN (baseline) | 600 | 32 | 0.25 | ~2.6M |
| Character-level | LSTMRNTN (proposed) | 256 | 32 | 0.25 | ~2.6M |

*Source: ([Tjandra et al., n.d.](document_1.txt)). Note: the source transcription lists "600 for LSTMRNTN" in the character-level description; this is most plausibly the LSTM-family baseline setting. Parameter counts for each pair were deliberately matched for fair comparison.*

## 4. Word-Level Language Modeling: The Largest Reported Gains

On the PTB test set, the proposed models produced the following results relative to their matched baselines.

### Table 2. Word-Level Language Modeling (PTB Test Set, Perplexity)

| Model | Test PPL | Absolute Reduction vs. Matched Baseline | Relative Reduction |
|---|---|---|---|
| LSTMRNN (baseline) | 108.26 | — | — |
| GRURNN (baseline) | 97.78 | — | — |
| LSTMRNTN (proposed) | **96.97** | −11.29 | **−10.42%** |
| GRURNTN (proposed) | **87.38** | −10.40 | **−10.63%** |

*Source: ([Tjandra et al., n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)).*

The GRURNTN model reduced perplexity from 97.78 to 87.38, an absolute improvement of 10.4 PPL and a relative improvement of 10.63% over GRURNN; LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute improvement of 11.29 PPL and a relative improvement of 10.42% over LSTMRNN ([Research Note, n.d.](document_2.txt)). The paper notes that "GRURNTN outperformed all the baseline models as well as the other models by a large margin" in this task, and that Fig. 9 shows GRURNTN "had a consistently lower PPL than the other models" across epochs ([Tjandra et al., n.d.](document_1.txt)). Both proposed models "produced lower PPL than our baseline models from the first epoch to the last epoch" ([Tjandra et al., n.d.](document_1.txt)).

For context, the published reference models listed in the paper's word-level table include RNNLM without dynamic evaluation at 124.7 PPL, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, and DOT(S)-RNN at 107.5, with GRURNN at 97.78 and LSTMRNN at 108.26 as the immediate baselines ([Tjandra et al., n.d.](document_1.txt)). Against that backdrop, GRURNTN's 87.38 is the strongest test-set perplexity among the models tabulated in the source.

## 5. Character-Level Language Modeling: Smaller but Consistent Gains

### Table 3. Character-Level Language Modeling (PTB Test Set, Bits-Per-Character)

| Model | Test BPC | Absolute Reduction vs. Matched Baseline | Relative Reduction |
|---|---|---|---|
| LSTMRNN (baseline) | 1.37 | — | — |
| GRURNN (baseline) | 1.39 | — | — |
| LSTMRNTN (proposed) | **1.34** | −0.03 | **−2.22%** |
| GRURNTN (proposed) | **1.33** | −0.06 | **−4.32%** |

*Source: ([Tjandra et al., n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)).*

GRURNTN reduced BPC from 1.39 to 1.33 (0.06 absolute, 4.32% relative) versus GRURNN, while LSTMRNTN reduced BPC from 1.37 to 1.34 (0.03 absolute, 2.22% relative) versus LSTMRNN ([Research Note, n.d.](document_2.txt)). The paper describes this outcome more cautiously than the word-level result, stating that "GRURNTN slightly outperformed the baseline models on the character-level language modeling task" ([Tjandra et al., n.d.](document_1.txt)). The epoch-wise comparison shows that the proposed GRURNTN "made faster and quicker progress than LSTMRNTN and converged into a similar BPC in the last epoch," while both proposed models produced lower BPC than the baselines from the first to the last epoch ([Tjandra et al., n.d.](document_1.txt)). Notably, LSTMRNN eventually converged to a better development-set BPC than GRURNN, meaning the character-level comparison is largely a contest between the gated-tensor variants ([Tjandra et al., n.d.](document_1.txt)).

## 6. Interpreting the Magnitude of the Improvements

Three observations follow from the reported numbers.

**First, the word-level gains are substantial.** A relative perplexity reduction of roughly 10% is a meaningful advance in statistical language modeling, because the baseline LSTMRNN and GRURNN models are already strong gated architectures whose behavior is difficult to improve on the same corpus ([Tjandra et al., n.d.](document_1.txt)). The consistency of the two relative figures (10.63% for GRURNTN, 10.42% for LSTMRNTN) across two different gating families suggests that the tensor product provides a systematic benefit rather than an architecture-specific artifact.

**Second, the character-level gains are real but modest.** The 2.22%–4.32% relative BPC reductions are smaller than the perplexity gains, and the paper itself uses the word "slightly" for this task ([Tjandra et al., n.d.](document_1.txt)). This asymmetry is plausible if tensor-product interactions help primarily at the level of longer-range lexical-semantic dependencies, which matter more for word prediction.

**Third, GRURNTN, not LSTMRNTN, is the stronger overall model.** GRURNTN produced the largest relative and absolute improvements in both tasks, the lowest word-level perplexity (87.38), the lowest character-level BPC among the four models under the paper's narrative attribution (1.33), and consistently faster convergence ([Tjandra et al., n.d.](document_1.txt)). By contrast, LSTMRNTN's performance at the word level "closely resembles the baseline GRURNN" despite comfortably beating LSTMRNN, indicating that gating-family choice interacts with the tensor augmentation ([Tjandra et al., n.d.](document_1.txt)).

## 7. Where the Improvement Does Not Hold

The gains are relative to the authors' own matched baselines, not necessarily against all published systems. In the character-level table, published comparison points are reported at lower BPC than the proposed models' 1.33–1.34; the transcribed table lists reference values of 1.26 for DOT(S)-RNN and a further figure of 1.24, alongside HF-MRNN at 1.57, BPTT-RNN at 1.42, SRNN at 1.41, and an adaptive-noise LSTMRNN variant at 1.39 ([Tjandra et al., n.d.](document_1.txt)). Under that reading, the proposed character-level models improved on their own gated baselines but did not surpass the best published character-level result reported in the same table. The word-level picture is more favorable: GRURNTN's 87.38 PPL is lower than every comparison figure listed in Table II of the source ([Tjandra et al., n.d.](document_1.txt)).

## 8. Caveats on Reliability and Data Quality

Several limitations should temper the interpretation. The available transcription of the paper is partially degraded; in Table I the four model rows are listed in the order LSTMRNN, GRURNN, LSTMRNTN, GRURNTN with test BPC values of 1.39, 1.37, 1.33, and 1.34, whereas the narrative text and the third-party note assign the 1.39 → 1.33 transition to GRURNTN and the 1.37 → 1.34 transition to LSTMRNTN ([Tjandra et al., n.d.](document_1.txt); [Research Note, n.d.](document_2.txt)). The narrative attribution is internally consistent with the reported percentages (0.06/1.39 = 4.32%; 0.03/1.37 ≈ 2.2%), which supports the narrative figures used in this report, but per-model attribution of individual table cells should be treated with caution. In addition, all results come from a single benchmark corpus (PTB), and no variance estimates, random-seed repetitions, or statistical significance tests are reported ([Tjandra et al., n.d.](document_1.txt)). The third-party note is derivative rather than independent: it repeats the paper's numbers and conclusions rather than re-running the experiments ([Research Note, n.d.](document_2.txt)). Finally, the authors note that dynamic evaluation was not used in either the baseline or proposed experiments, and that adaptive noise regularization refers to learned noise variance ([Tjandra et al., n.d.](document_1.txt)).

## 9. Conclusion

Across both tasks and both gating families, the introduced models outperform their matched previous models, with the magnitude depending strongly on the task:

- **Word-level (PTB test perplexity):** GRURNTN improved on GRURNN by **10.4 PPL absolute / 10.63% relative** (97.78 → 87.38); LSTMRNTN improved on LSTMRNN by **11.29 PPL absolute / 10.42% relative** (108.26 → 96.97) ([Research Note, n.d.](document_2.txt); [Tjandra et al., n.d.](document_1.txt)).
- **Character-level (PTB test bits-per-character):** GRURNTN improved on GRURNN by **0.06 BPC absolute / 4.32% relative** (1.39 → 1.33); LSTMRNTN improved on LSTMRNN by **0.03 BPC absolute / 2.22% relative** (1.37 → 1.34) ([Research Note, n.d.](document_2.txt); [Tjandra et al., n.d.](document_1.txt)).

These improvements were obtained with parameter budgets matched between each proposed model and its baseline, which strengthens the claim that the gating-plus-tensor combination, rather than added capacity alone, is responsible for the gains ([Tjandra et al., n.d.](document_1.txt)). The most defensible overall statement is that the tensor-product augmentation of gated RNNs yields a large and consistent improvement in word-level language modeling (approximately one-tenth of relative perplexity) and a smaller, still consistent improvement in character-level modeling, with GRURNTN being the strongest of the four models and LSTMRNTN the weaker of the two proposals.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network* [Manuscript]. document_1.txt.

Research note: Gated recurrent neural tensor network [Third-party research note]. (n.d.). document_2.txt.