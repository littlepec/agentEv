# Layer Count of the Single Deep Bidirectional LSTM Network for Word Sense Disambiguation

## Introduction

The question of how many layers constitute the single Bidirectional Long Short-Term Memory (BLSTM) model proposed by Pesaranghader et al. (2018) for Word Sense Disambiguation (WSD) can be answered directly from the primary source: the architecture depicted in Figure 1 of the paper explicitly "consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The answer is therefore **six layers**, not five. This report documents the primary evidence for that figure, enumerates and describes each of the six layers, and examines a conflicting secondary claim of five layers that appears in a third-party research note (Third-party research note, n.d.), explaining why the primary source should be preferred.

## The Explicit Statement in the Primary Source

The layer count is stated unambiguously in Section 3 of the paper, titled "One Single BLSTM network for WSD." The relevant sentence reads: "The architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

This sentence provides both the total count and an exhaustive enumeration of the constituent layers, ordered from the top of the network down to the bottom. It is the only explicitly stated total layer count for the model in the paper; no other section revises or contradicts this figure. Consequently, any downstream claim about the model's depth should be grounded in this sentence.

Corroborating evidence appears in the caption of Figure 1, which describes the data flow through the network: "The cosine similarities between the context words and the examined sense as the outputs of the first two layers are fed to two LSTM networks with different directions. Then, the concatenated outputs of LSTMs is fed to a (binary) neural network sense classifier consisting of one fully-connected layer and a sigmoid unit" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The caption's reference to "the first two layers" producing the cosine similarities is consistent with the bottom two layers being the sense and word embeddings layer followed by the cosine layer, after which the signal passes through the BLSTM, the concatenation layer, the fully-connected layer, and finally the sigmoid layer — six layers in total.

## The Six Named Layers

The primary source names each layer and describes its function. Table 1 summarizes the stack from bottom to top.

**Table 1.** The six layers of the single BLSTM WSD model, ordered from bottom (input side) to top (output side).

| Order | Layer | Function | Source |
|---|---|---|---|
| 1 (bottom) | Sense and word embeddings layer | Stores and retrieves sense embeddings and pre-trained word embeddings (GloVe) | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 2 | Cosine layer | Computes cosine similarities between each sense embedding and the word embeddings of the context words | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 3 | BLSTM layer | Encodes the resulting sequence of cosine similarities using two reversed unidirectional LSTMs | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 4 | Concatenation layer | Merges the outputs of the left- and right-traversing LSTMs | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 5 | Fully-connected layer | Applies a ReLU-activated hidden layer over the concatenated BLSTM outputs | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |
| 6 (top) | Sigmoid layer | Produces a binary classification score for the examined sense | ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)) |

### The Sense and Word Embeddings Layer (Bottom)

This layer, sitting at the bottom of the stack, holds two lookup tables: a sense embedding matrix and a word embedding matrix. For a given candidate sense, the input is determined by Equation (1), which effectively selects the column of the sense embedding matrix corresponding to that sense from its one-hot representation ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The sense embeddings are initialized randomly from a uniform distribution on the interval (-0.1, 0.1), because, as the authors state, "no sense embedding is computed a priori" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). In contrast, the word embeddings are initialized using pre-trained GloVe vectors trained on Wikipedia and Gigaword with a 400K vocabulary, in uncased form ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### The Cosine Layer

The second layer computes cosine similarities between the sense embedding under examination and the word embeddings of the surrounding context words. The authors hypothesize that "the sequence result of similarities between the true sense and the surrounding context communicate a pattern-like information that can be encoded through our BLSTM network; for the incorrect senses this premise does not hold" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The paper notes that several prior WSD studies had already incorporated sense-context cosine similarities into their models, citing McInnes and Pedersen (2013) and Pedersen and Kolhatkar (2009) ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). This is the layer whose omission in the third-party research note accounts for the discrepancy discussed below.

### The BLSTM Layer

The BLSTM layer is treated as a single layer within the total count, even though it internally comprises two reversed unidirectional LSTMs. The paper explains that "a Bidirectional LSTM is made up of two reversed unidirectional LSTMs" and that, for WSD, this permits encoding "information of both preceding and succeeding words within context of an ambiguous word, which is necessary to correctly classify its sense" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The BLSTM hidden layer size used in the experiments was 2 × 50, meaning each direction contributes 50 hidden units ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### The Concatenation Layer

The concatenation layer merges the outputs of the right- and left-traversing LSTMs once the final context components have been processed. The hidden layer computation is given by Equation (5): *h_cl* = ReLU(*W_h* · [*h^L_{C−1}*; *h^R_{C+1}*] + *b_h*), where the bracketed notation denotes the concatenated outputs and ReLU denotes the rectified linear unit ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### The Fully-Connected Layer

Above the concatenation layer sits a single fully-connected layer, which the Figure 1 caption describes as part of a "(binary) neural network sense classifier consisting of one fully-connected layer and a sigmoid unit" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Dropout at a rate of 50% is applied to the outputs of this layer during training ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### The Sigmoid Layer (Top)

The topmost layer is a sigmoid classification layer with weights *W_out* ∈ R^(1×50) and bias *b_out* ∈ R. Its output for the sense under examination is given by Equation (3) ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). During training, this output is set to 1.0 for the correct sense and 0.0 for incorrect senses; at test time, the sense with the highest sigmoid output is selected via an argmax over all candidate senses ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The replacement of the conventional softmax output with a sigmoid required a corresponding modification to the model input: both the context and the candidate sense are supplied to the network, since the network evaluates whether a given context matches a given sense rather than directly selecting among senses ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## The Discrepancy in the Secondary Source

A third-party research note on the same paper asserts that "the proposed single BLSTM model for word sense disambiguation has 5 layers" and lists "a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer" (Third-party research note, n.d.). Notably, this enumeration omits the cosine layer, which the primary source explicitly names as one of the six layers ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The note further states that "the paper reports that the proposed single BLSTM model... has 5 layers" and that "Section 3... states that the architecture, depicted in Fig. 1, consists of 5 layers," but this directly conflicts with the primary source's text, which states 6 layers (Third-party research note, n.d.; [Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

Because the third-party note reproduces a layer listing that is missing exactly one element relative to the primary enumeration, the most parsimonious explanation is that the note's layer count is an error of transcription or counting rather than an alternative valid interpretation of the architecture. A reader comparing the two documents can verify that the six-item list in the primary source — sigmoid, fully-connected, concatenation, BLSTM, cosine, and sense/word embeddings — contains every item in the note's five-item list plus the cosine layer.

## Why the Primary Source Should Be Preferred

The primary source, the arXiv preprint by Pesaranghader et al. (2018), is the authoritative record of the model's architecture. It is the document in which Figure 1 appears, in which Equations (1) through (5) are defined, and in which the layer-wise functional description is written by the model's own authors. It also specifies the exact position of each layer in the stack ("at the top" for the sigmoid layer, "on the bottom" for the sense and word embeddings layer), which allows the enumerated layers to be mapped onto a concrete architecture ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

The third-party note, by contrast, is a derivative summary that does not reproduce the equations, the figure, or the empirical results, and it does not explain how its layer enumeration was derived (Third-party research note, n.d.). It also contains a statement that "no other explicit total layer count for the model is stated in the paper," which is accurate in the sense that the paper states the count only once, but the note then adopts the incorrect value for that single explicit statement (Third-party research note, n.d.). Under standard principles of source evaluation, a peer-reviewable primary research article describing its own architecture should outweigh an unsigned secondary summary, particularly when the primary document's enumeration is internally consistent with its own figure caption and equations ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## Supplementary Architectural Details

Beyond the layer count, the primary source provides a range of configuration details that characterize the network. The experiments used a context size of 15 words to the left and 15 to the right of the ambiguous word, an embedding size of 100, and a BLSTM hidden layer size of 2 × 50 ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Regularization included dropout of 20% on the sense and word embeddings, 50% on the LSTM outputs, and 50% on the fully-connected layer, plus word dropout of 20% on the sequence of context words ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Training used RMSprop optimization with a mean squared error loss, which the authors found worked better than binary cross entropy for the final argmax classification, and all weights including embeddings were updated during training ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Data preprocessing lower-cased all words and removed numbers, yielding a vocabulary of 29,044 words ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

The model was evaluated on the SensEval-3 English lexical sample task, which covers 57 words: 20 nouns averaging 5.8 senses, 32 verbs averaging 6.31 senses, and 5 adjectives averaging 10.2 senses, with an overall average of 6.47 senses per word ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The single-classifier BLSTM achieved an F-measure of 72.5%, ranking fourth among the compared supervised systems, behind Multi-classifier BLSTM (73.4%), IMS+adapted CW (73.4%), htsa3 (72.9%), and IRST-Kernels (72.6%), while surpassing nusels (72.4%) ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

**Table 2.** Selected F-measure results on SensEval-3, with the single-classifier BLSTM highlighted.

| Rank | Method | F-measure (%) |
|---|---|---|
| 1 | Multi-classifier BLSTM | 73.4 |
| 1 | IMS+adapted CW | 73.4 |
| 2 | htsa3 | 72.9 |
| 3 | IRST-Kernels | 72.6 |
| **4** | **Our Single-classifier BLSTM** | **72.5** |
| 5 | nusels | 72.4 |

Source: ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

Ablation experiments reported in Table 4 of the paper reinforce that the six-layer design is functionally coherent: reversing the BLSTM directions reduced performance to 68.9%, shuffling the context reduced it to 67.3%, replacing the BLSTM with fully-connected layers reduced it to 70.2%, removing GloVe initialization reduced it to 65.6%, removing word dropout reduced it to 71.1%, and enlarging the context window to 25 words per side reduced it to 71.4% ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). These results indicate that each component, including the sequence-encoding BLSTM and the pre-trained embeddings, contributes measurably to the final performance.

## Conclusion

Based on the primary source, the single deep Bidirectional LSTM network for word sense disambiguation consists of **six layers**: a sense and word embeddings layer at the bottom, followed by a cosine layer, a BLSTM layer, a concatenation layer, a fully-connected layer, and a sigmoid layer at the top ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The third-party research note's claim of five layers is inconsistent with the primary text and appears to result from omitting the cosine layer from the enumeration (Third-party research note, n.d.). Because the primary paper explicitly enumerates all six layers, maps them to positions in the stack, and corroborates the structure through its figure caption and equations, the correct answer to the query "How many layers does their model have?" is six.

## References

Pesaranghader, A., Pesaranghader, A., Matwin, S., & Sokolova, M. (2018). *One single deep bidirectional LSTM network for word sense disambiguation of text data* (arXiv:1802.09059). arXiv. https://arxiv.org/abs/1802.09059

Third-party research note: One single deep bidirectional LSTM network for word sense disambiguation of text data. (n.d.). [Unpublished research note].