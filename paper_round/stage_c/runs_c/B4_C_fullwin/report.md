# Layer Count of the Single Deep Bidirectional LSTM Network for Word Sense Disambiguation

## Introduction

The query asks: "How many layers does their model have?" The model in question is the single Bidirectional Long Short-Term Memory (BLSTM) network proposed by Pesaranghader et al. (2018) for Word Sense Disambiguation (WSD) of text data. Based on the primary source, the paper explicitly states that the architecture consists of **6 layers**. This report provides a detailed, evidence-based answer, describes each layer, and discusses the implications of this count. The answer is unambiguous: the model has six layers, as stated in Section 3 of the paper and corroborated by a third-party research note ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

## Explicit Statement of Layer Count

In Section 3, titled "One Single BLSTM network for WSD," the authors write: "The architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). This is the only explicit total layer count in the paper. A third-party research note on the same paper confirms: "The paper reports that the proposed single BLSTM model for word sense disambiguation has 6 layers. Section 3 One Single BLSTM network for WSD states that the architecture, depicted in Fig. 1, consists of 6 layers. The layer count is explicit: 6 layers" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). Therefore, the answer to the query is **6 layers**.

## Detailed Layer-by-Layer Description

The six layers are arranged from bottom (input) to top (output). The following table summarizes their names, positions, and functions.

| Layer Position | Layer Name | Function | Key Details |
|----------------|------------|----------|-------------|
| 1 (bottom) | Sense and Word Embeddings | Lookup tables for sense and word vectors | Sense embeddings initialized randomly from U(-0.1, 0.1); word embeddings initialized with GloVe; embedding size = 100 ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 2 | Cosine | Computes cosine similarities between the sense embedding and each context word embedding | Produces a sequence of similarity scores that the BLSTM encodes |
| 3 | BLSTM | Bidirectional LSTM layer | Consists of two reversed unidirectional LSTMs; hidden size = 2*50 ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 4 | Concatenation | Concatenates outputs of the left and right LSTMs | Merges forward and backward representations into a single vector |
| 5 | Fully-Connected | Hidden layer with ReLU activation | Maps concatenated output to a 50-dimensional representation |
| 6 (top) | Sigmoid | Binary classification for each candidate sense | Outputs a value between 0 and 1; argmax selects the true sense |

### Layer 1: Sense and Word Embeddings

The bottom layer is the input layer, which contains two lookup tables: one for sense embeddings (denoted **W_s^l**) and one for word embeddings (denoted **W_w^x**). Sense embeddings are initialized randomly from a uniform distribution between -0.1 and 0.1 because no pre-computed sense embeddings are publicly available. Word embeddings are initialized using pre-trained GloVe vectors (Wikipedia and Gigaword, 400K vocabulary, uncased). The embedding size is 100, and the vocabulary size after preprocessing is 29,044. This layer is explicitly counted as one of the six layers ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### Layer 2: Cosine Layer

This layer computes the cosine similarity between the sense embedding and each word embedding in the context. For a given sense \(s_i\) and context words \(w_m\), the cosine similarities form a sequence. The authors argue that the sequence of similarities between the true sense and its surrounding context carries pattern-like information that can be encoded by the BLSTM; for incorrect senses, this premise does not hold. This layer is listed as one of the six ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### Layer 3: BLSTM Layer

The BLSTM layer is a single layer in the count, although it internally comprises two reversed unidirectional LSTMs. The paper states: "A Bidirectional LSTM is made up of two reversed unidirectional LSTMs" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The hidden layer size is 2*50, meaning each direction has 50 hidden units. This layer encodes information from both preceding and succeeding words in the context. Ablation experiments demonstrate its importance: reversing the LSTM directions reduced F-measure from 72.5% to 68.9%; shuffling the context reduced it to 67.3%; replacing the BLSTM with fully-connected layers reduced it to 70.2% ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The third-party note confirms: "The BLSTM is treated as one layer within the total layer count; the paper lists the BLSTM layer as one of the six layers" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

### Layer 4: Concatenation Layer

This layer concatenates the outputs of the left and right LSTMs when the last context components are met. The concatenated output \(h_{cl}\) is then passed to the fully-connected layer. The paper describes it as "a concatenation layer" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### Layer 5: Fully-Connected Layer

The fully-connected layer applies a ReLU activation to the concatenated output: \(h_{cl} = \text{ReLU}(W_h \cdot [h_{C-1}^L; h_{C+1}^R] + b_h)\). This layer is also referred to as the hidden layer. Its output size is 50, as indicated by the weight matrix \(W_{out} \in \mathbb{R}^{1 \times 50}\) in the sigmoid layer equation. Dropout of 50% is applied to this layer's outputs during training ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### Layer 6: Sigmoid Layer

The top layer is a sigmoid classification layer. It computes \(\hat{y}_{s_i} = \sigma(W_{out} \cdot h_{cl} + b_{out})\), producing a value between 0 and 1 for each candidate sense. During training, the correct sense is set to 1.0 and incorrect senses to 0.0. During testing, the sense with the highest \(\hat{y}_{s_i}\) is selected via argmax. The sigmoid layer is counted as the sixth layer ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## Why the Count is 6 and Not More or Less

The paper's count includes the embedding layer, which some architecture descriptions exclude. It also counts the BLSTM as one layer, even though it contains two LSTM sub-networks. The concatenation layer is counted separately from the BLSTM, and the fully-connected layer is distinct from the sigmoid layer. No other layer count is mentioned. The third-party note explicitly states: "No other explicit total layer count for the model is stated in the paper. The explicit total layer count given is 6 layers" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). Thus, the total is unambiguously 6.

## Comparison with Related Work

The paper compares its single-classifier BLSTM with other WSD systems. The top-performing systems, Multi-classifier BLSTM and IMS+adapted CW, achieved 73.4% F-measure. The proposed single-classifier BLSTM achieved 72.5%, ranking fourth. Notably, the Multi-classifier BLSTM uses multiple classifiers (one per ambiguous word), whereas the proposed model uses a single network. The layer count of those comparison models is not provided in the source. However, the design choice of 6 layers reflects a balance between depth and computational efficiency. The paper notes that while the single model eliminates the need for 57 separate classifiers (one per ambiguous word in SensEval-3), it still falls slightly short of the state-of-the-art ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## Hyperparameters and Training Details

The hyperparameters were selected using 5% of training data for validation. Key values include: context size 15 left and 15 right; embedding size 100; BLSTM hidden layer size 2*50; dropout on embeddings 20%; dropout on LSTM outputs 50%; dropout on fully-connected layer 50%; word dropout 20%. The loss function is mean square error, and the optimizer is RMSprop. All weights, including embeddings, are updated during training. These details provide context for the 6-layer architecture ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## Implications of the 6-Layer Design

A 6-layer network is moderately deep by modern standards, but it is "deep" in the sense of having multiple layers including a recurrent layer. The single BLSTM layer is sufficient to capture sequential patterns in the cosine similarity sequences. The model's performance is comparable to state-of-the-art WSD algorithms despite using only one classifier for all words. The authors note a limitation: sense embeddings and word embeddings come from separate vector spaces, causing misalignment that requires more training data. This is not a layer count issue but a design challenge. Future work includes pre-training sense embeddings and testing on biomedical domains ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## Conclusion

The model proposed by Pesaranghader et al. (2018) has exactly **6 layers**. These layers are, from bottom to top: sense and word embeddings, cosine, BLSTM, concatenation, fully-connected, and sigmoid. The count is explicitly stated in Section 3 of the paper and confirmed by a third-party research note. No other total is given. The 6-layer architecture enables the single-classifier BLSTM to achieve 72.5% F-measure on SensEval-3, ranking among the top five supervised WSD systems. The explicit layer count is a fundamental architectural fact that supports the model's design and performance claims ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

## References

- Pesaranghader, A., Pesaranghader, A., Matwin, S., & Sokolova, M. (2018). *One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data*. arXiv preprint arXiv:1802.09059. https://arxiv.org/abs/1802.09059
- Third-party research note. (n.d.). *One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data*. Retrieved from https://arxiv.org/abs/1802.09059