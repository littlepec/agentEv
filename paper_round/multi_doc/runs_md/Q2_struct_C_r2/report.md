# Word-Level Penn Treebank Test Perplexity for Proposed Models: A Cross-Paper Tabulation

## 1. Scope, Definitions, and Inclusion Criteria

This report tabulates, for each of the eleven papers represented in the supplied source notes, the word‑level Penn Treebank (PTB) test‑set perplexity that the paper reports for **its own proposed model**, restricted to the **best single‑model result obtained without dynamic evaluation and without a cache/pointer mechanism**. This restriction matters because several of the papers in this set report headline numbers that come from model averaging, dynamic evaluation, or cache augmentation, and those numbers are not answers to the question posed here.

The underlying evaluation protocol is essentially constant across the eleven papers. The English PTB is used with the standard training (0–20), validation (21–22), and test (23–24) splits together with the preprocessing of Mikolov et al., yielding approximately one million tokens and a vocabulary of about 10,000 words ([Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615)). Performance is expressed as perplexity, computed as $PPL = \exp(NLL/T)$ where $NLL$ is accumulated over the test set ([Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615)). The same Mikolov preprocessing is referenced for the RHN experiments ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)), and the single‑model framing is made explicit in the relevant table captions ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287); [Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182); [Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)).

Three classes of result were excluded. First, **ensembles and model averaging**: the regularized‑LSTM paper reports averaged models at 77.0, 73.3, 72.0, 73.6, 69.5 and 68.7 for 2, 5, 10, 2, 10 and 38 models respectively, none of which is a single‑model result ([Recurrent Neural Network Regularization, 2014](https://arxiv.org/abs/1409.2329)). Second, **dynamic evaluation**: the Mixture‑of‑Softmaxes paper reports 47.69 for AWD‑LSTM‑MoS with dynamic evaluation ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). Third, **cache/pointer augmentation**: the AWD‑LSTM paper reports 52.8 with a continuous cache pointer ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). Fine‑tuning, by contrast, is **not** excluded by the stated criteria, so results that include it are reported below but explicitly flagged, since it is an additional post‑training procedure rather than a purely single‑pass training result.

## 2. Master Table of Results

| # | Paper (arXiv ID) | Best single‑model word‑level PTB test perplexity | Configuration reported |
|---|------------------|------------------------------------------------:|------------------------|
| 1 | [Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (2014) | **78.4** | Large regularized LSTM (medium = 82.7) |
| 2 | [Character-Aware Neural Language Models](https://arxiv.org/abs/1508.06615) (2015) | **78.9** | LSTM‑Char‑Large (small = 92.3) |
| 3 | [A Theoretically Grounded Application of Dropout in Recurrent Neural Networks](https://arxiv.org/abs/1512.05287) (2015) | **73.4** | Large Variational LSTM, untied weights, MC dropout at test time |
| 4 | [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474) (2016) | **65.4** | Variational RHN + WT, 23M parameters |
| 5 | [Using the Output Embedding to Improve Language Models](https://arxiv.org/abs/1608.05859) (2016) | **74.3** | Large NNLM + weight tying |
| 6 | [Tying Word Vectors and Word Classifiers](https://arxiv.org/abs/1611.01462) (2016) | **138.4** | VD‑LSTM+REAL (small, 200 units; only the small configuration appears in the supplied note) |
| 7 | [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578) (2016) | **62.4** | NAS, base 8 + shared embeddings, 54M parameters |
| 8 | [Gated Recurrent Neural Tensor Network](https://arxiv.org/abs/1706.02222) (2017) | **87.38** | GRURNTN (LSTMRNTN = 96.97) |
| 9 | [On the State of the Art of Evaluation in Neural Language Models](https://arxiv.org/abs/1707.05589) (2017) | **58.3** | 4‑layer LSTM, 24M parameters |
| 10 | [Breaking the Softmax Bottleneck](https://arxiv.org/abs/1711.03953) (2017) | **54.44** (55.97 without fine‑tuning) | AWD‑LSTM‑MoS |
| 11 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) (2017) | **57.3** (58.8 without fine‑tuning) | 3‑layer AWD‑LSTM, tied weights |

## 3. Paper-by-Paper Detail

### 3.1 Early Regularized and Variational LSTMs

The regularized‑LSTM paper is a frequent source of confusion because its most prominent numbers are averaged models. Its **single‑model** figures are 82.7 for the medium regularized LSTM and 78.4 for the large regularized LSTM, and the note explicitly identifies these as the paper's own proposed models evaluated as single models ([Recurrent Neural Network Regularization, 2014](https://arxiv.org/abs/1409.2329)). The 78.4 figure subsequently became a widely reused baseline—cited at 78.4 in the variational‑dropout comparison table ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287)) and again at 78.4 among the comparison baselines of the output‑embedding paper ([Using the Output Embedding to Improve Language Models, 2016](https://arxiv.org/abs/1608.05859)).

The variational‑dropout paper proposes the Variational LSTM and reports **73.4** for the large untied‑weights model with MC dropout, describing the reduction from 78.4 to 73.4 as the effect of MC dropout combined with untied weights ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287)). The surrounding table entries make clear that 73.4 is the minimum of the proposed family: tied weights without MC give 75.0, tied with MC 74.1, untied without MC 75.2, and the medium models reach only 78.6–79.7 ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287)). The paper asserts that these are, to its knowledge, the best single‑model perplexities on PTB ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287)).

### 3.2 Character‑Level and Embedding‑Level Innovations

The character‑aware language model predicts words from character inputs and reports **78.9** for LSTM‑Char‑Large and 92.3 for LSTM‑Char‑Small, both as single models with word‑level predictions ([Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615)). Notably, the paper deliberately excludes ensembles, stating that lower perplexities have been reported with model ensembles and that these are not comparable to its own work ([Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615)). This is a clean case for the present tabulation: the reported numbers already satisfy the single‑model constraint.

The output‑embedding paper proposes weight tying of input and output embeddings and reports **74.3** for Large + Weight Tying and 100.9 for Small + WT + projection regularization, both single‑model and reported without dynamic evaluation, cache/pointer, ensemble, or fine‑tuning ([Using the Output Embedding to Improve Language Models, 2016](https://arxiv.org/abs/1608.05859)). Its comparison context includes non‑dropout baselines ranging from a KN 5‑gram at 141 down to a Deep RNN at 107.5 ([Using the Output Embedding to Improve Language Models, 2016](https://arxiv.org/abs/1608.05859)).

The loss‑framework paper on tying word vectors and classifiers is the outlier in this table, and the reason is important. The supplied note contains only the **small (200‑unit)** configuration: VD‑LSTM at 159.1/148.0 and 163.19/148.6, VD‑LSTM+AL at 153.0/142.5 and 156.4/143.7, VD‑LSTM+RE at 152.4/141.9 and 152.5/140.9, and VD‑LSTM+REAL at 149.3/140.6 and 150.5/**138.4**, presented as word‑level validation and test perplexities on PTB ([Tying Word Vectors and Word Classifiers, 2016](https://arxiv.org/abs/1611.01462)). The lowest value reported in the supplied excerpt is therefore **138.4**, and this should be treated as a small‑model figure that is not comparable with the large‑model results of the other papers. Its inclusion here reflects the strict instruction to tabulate what each paper reports for its own proposed model, not to rank models of different sizes against one another.

### 3.3 Depth, Gating, and Architecture Search

Recurrent Highway Networks report **65.4** test perplexity for Variational RHN + WT (23M parameters, validation 67.9), with 68.5 for Variational RHN without weight tying ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)). The result is a single model; the paper reports no dynamic evaluation, cache/pointer, or fine‑tuning for its own model, and cache and pointer methods appear only as baselines ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)). The paper further claims that RHNs outperform most single models as well as all previous ensembles ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)); depth was the key design choice, with test scores improving monotonically as recurrence depth increased from 1 to 10 at a fixed 32M‑parameter budget ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)).

Neural Architecture Search reports **62.4** for its best found model (base 8 with shared embeddings, 54M parameters), with 64.0 and 67.9 for other configurations ([Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578)). These are single‑model test perplexities, with no dynamic evaluation, cache/pointer, ensemble, or fine‑tuning reported for the searched model, and cache/pointer appearing only in baseline labels such as Pointer Sentinel‑LSTM ([Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578)). The paper frames the gain as 3.6 perplexity over the best listed baseline, Zilly et al.'s Variational RHN with shared embeddings at 66.0 ([Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578)). It is worth flagging that this baseline value (66.0) differs from the 65.4 that the RHN paper itself reports for Variational RHN + WT, a reminder that cross‑paper comparisons inherit configuration differences.

### 3.4 Tensor‑Based Recurrent Models

The gated recurrent neural tensor network paper proposes GRURNTN and LSTMRNTN and reports **87.38** and 96.97 test perplexity respectively, described as individual models trained without dynamic evaluation ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). GRURNTN reduces perplexity from its own GRURNN baseline of 97.78, and LSTMRNTN from 108.26 ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). The paper's comparison row for RNNLM provides both a non‑dynamic number (124.7) and a dynamic‑evaluation number (123.2), and only the former class of figure is used for the present tabulation ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)).

### 3.5 Evaluation‑Centric and Late‑Regularization Results

The evaluation study reports **58.3** for a 4‑layer LSTM with 24M parameters, obtained at the depth where "all depths obtain very similar results" ([On the State of the Art of Evaluation in Neural Language Models, 2017](https://arxiv.org/abs/1707.05589)). Critically for this report's inclusion criteria, the authors explicitly refrain from including techniques known to push perplexities lower, because their aim is strictly to improve model comparisons ([On the State of the Art of Evaluation in Neural Language Models, 2017](https://arxiv.org/abs/1707.05589)). This is the cleanest single‑model datapoint in the set.

AWD‑LSTM reports **57.3** for a 3‑layer tied‑weight LSTM, with the table caption identifying single‑model perplexity on validation and test ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). This number includes the fine‑tuning step; the no‑fine‑tuning ablation is 58.8, and the paper states that removing fine‑tuning degrades performance ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). The cache‑augmented variant reaches 52.8 and is excluded here by the cache criterion ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). The paper positions 57.3 as roughly one perplexity unit better than the best listed baseline, a 4‑layer skip‑connection LSTM at 58.3 ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)).

Finally, AWD‑LSTM‑MoS reports **55.97** without fine‑tuning and **54.44** with fine‑tuning as its single‑model results, with 47.69 reserved for dynamic evaluation ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). Applying the stated criteria literally — exclude dynamic evaluation and cache, but not fine‑tuning — the answer for this paper is **54.44**, with 55.97 as the conservative no‑fine‑tuning alternative.

## 4. Results Excluded by the Stated Criteria

| Paper | Excluded figure | Reason for exclusion |
|-------|----------------:|----------------------|
| [Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (2014) | 77.0, 73.3, 72.0, 73.6, 69.5, 68.7 | Averaged/ensembled regularized LSTMs (2, 5, 10, 2, 10, 38 models) |
| [A Theoretically Grounded Application of Dropout in RNNs](https://arxiv.org/abs/1512.05287) (2015) | 68.7 | Ensemble of 10 Variational LSTMs with MC dropout |
| [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) (2017) | 52.8 | Continuous cache pointer variant |
| [Breaking the Softmax Bottleneck](https://arxiv.org/abs/1711.03953) (2017) | 47.69 | Dynamic evaluation |

For the remaining papers, the supplied notes state explicitly that no dynamic evaluation, cache/pointer, or fine‑tuning results for the proposed model appear ([Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615); [Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474); [Using the Output Embedding to Improve Language Models, 2016](https://arxiv.org/abs/1608.05859); [Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578); [Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)).

## 5. Cross‑Paper Observations

Ordered by arXiv identifier, the tabulated single‑model results fall into three tiers. The early tier sits between 73.4 and 78.9 ([Recurrent Neural Network Regularization, 2014](https://arxiv.org/abs/1409.2329); [Character-Aware Neural Language Models, 2015](https://arxiv.org/abs/1508.06615); [A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287); [Using the Output Embedding to Improve Language Models, 2016](https://arxiv.org/abs/1608.05859)). A middle tier occupies roughly 62–66 ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474); [Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578)). The latest tier reaches the mid‑50s to 58.3 ([On the State of the Art of Evaluation in Neural Language Models, 2017](https://arxiv.org/abs/1707.05589); [Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182); [Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). The tensor‑network paper at 87.38 and the small tied‑embedding model at 138.4 sit outside this progression because their configurations are not large‑scale ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222); [Tying Word Vectors and Word Classifiers, 2016](https://arxiv.org/abs/1611.01462)).

Two structural patterns deserve emphasis. First, **the identity of the proposed model changes across papers**—a regularized LSTM, a character‑CNN LSTM, a Variational LSTM, an RHN, a weight‑tied NNLM, a tensor network, a searched cell, and an MoS‑augmented AWD‑LSTM—so the table is a record of claims, not a controlled comparison. Second, **the excluded numbers are systematically more impressive than the included ones**: 68.7 under averaging, 52.8 under caching, and 47.69 under dynamic evaluation, against 78.4, 57.3, and 54.44 respectively ([A Theoretically Grounded Application of Dropout in Recurrent Neural Networks, 2015](https://arxiv.org/abs/1512.05287); [Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182); [Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). Any ranking that ignores this distinction would be misleading.

## 6. Caveats and Limitations

The notes report validation and test figures inconsistently: some entries are given as validation/test pairs (67.9/65.4; 150.5/138.4), and the tabulation above consistently takes the test component ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474); [Tying Word Vectors and Word Classifiers, 2016](https://arxiv.org/abs/1611.01462)). The small‑configuration entry for the tied‑classifier paper is not comparable to large‑model entries, and other configurations of that model may exist outside the supplied notes ([Tying Word Vectors and Word Classifiers, 2016](https://arxiv.org/abs/1611.01462)). The 65.4 versus 66.0 discrepancy between the RHN paper's own report and the NAS baseline table illustrates that cross‑paper baselines can silently refer to different variants ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474); [Neural Architecture Search with Reinforcement Learning, 2016](https://arxiv.org/abs/1611.01578)). Where a paper reports both fine‑tuned and non‑fine‑tuned numbers, both are shown so that the reader can apply a stricter criterion if desired ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182); [Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)).

## 7. References

Note: the supplied source notes did not consistently provide author names, so entries are identified by paper title and arXiv identifier.

Breaking the Softmax Bottleneck: A High‑Rank RNN Language Model. (2017). arXiv:1711.03953. https://arxiv.org/abs/1711.03953

Character‑Aware Neural Language Models. (2015). arXiv:1508.06615. https://arxiv.org/abs/1508.06615

Gated Recurrent Neural Tensor Network. (2017). arXiv:1706.02222. https://arxiv.org/abs/1706.02222

Neural Architecture Search with Reinforcement Learning. (2016). arXiv:1611.01578. https://arxiv.org/abs/1611.01578

On the State of the Art of Evaluation in Neural Language Models. (2017). arXiv:1707.05589. https://arxiv.org/abs/1707.05589

Recurrent Highway Networks. (2016). arXiv:1607.03474. https://arxiv.org/abs/1607.03474

Recurrent Neural Network Regularization. (2014). arXiv:1409.2329. https://arxiv.org/abs/1409.2329

Regularizing and Optimizing LSTM Language Models. (2017). arXiv:1708.02182. https://arxiv.org/abs/1708.02182

A Theoretically Grounded Application of Dropout in Recurrent Neural Networks. (2015). arXiv:1512.05287. https://arxiv.org/abs/1512.05287

Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling. (2016). arXiv:1611.01462. https://arxiv.org/abs/1611.01462

Using the Output Embedding to Improve Language Models. (2016). arXiv:1608.05859. https://arxiv.org/abs/1608.05859