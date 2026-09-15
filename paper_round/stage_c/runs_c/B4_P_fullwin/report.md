# How Many Layers Does the Single BLSTM Word Sense Disambiguation Model Have? A Source-Critical Report

## 1. Introduction and Scope

The architecture proposed by Pesaranghader, Pesaranghader, Matwin, and Sokolova (2018) addresses a well-known scalability problem in Word Sense Disambiguation (WSD): conventional supervised systems train one classifier per ambiguous word, which becomes impractical when a language or technical domain contains many ambiguous terms ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Their alternative is a single Bidirectional Long Short-Term Memory (BLSTM) network that processes all ambiguous words collectively by pairing a candidate sense embedding with the embeddings of its surrounding context words ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The natural question that follows — and the one this report answers — is how many layers that model actually contains. The answer is not merely descriptive; the layer count determines how the model's depth, parameterization, and computational behavior should be described in any downstream technical or comparative discussion.

Two supplied documents address the layer count directly, and they do not agree. The primary source, the arXiv preprint itself, states that the architecture consists of **six layers**, whereas a third-party research note summarizing the same paper states that it consists of **five layers** ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). This report examines both claims, resolves the conflict on evidentiary grounds, and provides a layer-by-layer accounting supported by the paper's own equations and figure description.

## 2. The Query and Its Two Conflicting Answers

### 2.1 The primary source: six layers

Section 3 of the paper, titled "One Single BLSTM network for WSD," contains an explicit and unambiguous enumeration ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)):

> "The architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)."

This sentence names exactly six components: (1) a sigmoid layer, (2) a fully-connected layer, (3) a concatenation layer, (4) a BLSTM layer, (5) a cosine layer, and (6) a sense and word embeddings layer ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The count of six is therefore not an inference — it is a direct statement in the paper's main architectural section, and it is consistent with the six named items that follow it in the same sentence.

### 2.2 The secondary source: five layers

The third-party research note asserts a different total: "The paper reports that the proposed single BLSTM model for word sense disambiguation has 5 layers" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). The note then lists the named layers as "a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer," and adds that "the paper includes the sense and word embeddings layer as one of the five layers, on the bottom" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). Crucially, the note also claims that "no other explicit total layer count for the model is stated in the paper" and that "the explicit total layer count given is 5 layers" ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

That last claim is directly falsified by the primary source, which does state a total — six, not five — and does so in the same section the note purports to summarize ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## 3. Resolution of the Discrepancy

### 3.1 The arithmetic of the two enumerations

Comparing the two lists isolates the disagreement to a single item. Both sources name the sigmoid layer, the fully-connected layer, the concatenation layer, the BLSTM layer, and the sense and word embeddings layer ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). The **cosine layer** appears only in the primary source. The difference between six and five is therefore entirely attributable to the omission of the cosine layer from the note's list ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

| Named layer | Primary source (paper) | Secondary source (research note) |
|---|---|---|
| Sigmoid layer (top) | Included | Included |
| Fully-connected layer | Included | Included |
| Concatenation layer | Included | Included |
| BLSTM layer | Included | Included |
| Cosine layer | Included | Omitted |
| Sense and word embeddings layer (bottom) | Included | Included |
| **Stated total** | **6** | **5** |

This pattern — a complete, ordered list in the primary source versus a truncated list in a derivative summary — is the classic signature of a summarization or transcription error rather than a substantive architectural disagreement ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059); [Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)).

### 3.2 Functional necessity of the cosine layer

The cosine layer is not decorative; it performs the computation that makes the entire model work. The paper explains that after the context words are converted to a sequence of word embeddings and the sense is converted to a sense embedding, the model computes "cosine similarities of each sense embedding with the word embeddings of the context words" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The resulting sequence of similarity values is what the BLSTM subsequently encodes into "a pattern-like information"; for incorrect senses, "this premise does not hold" ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The Figure 1 caption likewise describes the architecture in terms of "the cosine similarities between the context words and the examined sense as the outputs of the first two layers," which are then fed to the two LSTMs ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). A component that produces the input sequence to the BLSTM cannot be removed without changing the model's function, which strongly supports the six-layer enumeration in which it appears.

### 3.3 Corroboration from the mathematical formulation

Independent corroboration comes from the paper's equations. Each of the six named layers can be mapped to a distinct mathematical object in Section 3.1, which strengthens confidence that six is the intended count ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

| Layer | Mathematical evidence in the paper |
|---|---|
| Sense and word embeddings | Eq. (1) selects sense embeddings from the lookup table W_s^l; Eq. (2) selects word embeddings from W_w^x |
| Cosine layer | Section 3 text: cosine similarities between each sense embedding and the context word embeddings |
| BLSTM layer | Eq. (5) uses the concatenated hidden outputs of the left and right traversing LSTMs |
| Concatenation layer | Eq. (5) denotes the merge of h_{C−1}^L and h_{C+1}^R; Eq. (3) calls h_cl "the result of the merge layer (concatenation)" |
| Fully-connected layer | Eq. (5): ReLU(W_h · [h_{C−1}^L ; h_{C+1}^R] + b_h), with weights W_h and bias b_h |
| Sigmoid layer | Eq. (3): ŷ_{s_i} = σ(W_out · h_cl + b_out), with W_out ∈ R^{1×50} and scalar bias b_out |

Because all six components are independently attested — five in the equations and the cosine computation in the surrounding prose — the six-layer reading is the only one that accounts for every named element of the architecture ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## 4. Full Layer-by-Layer Description

Taken together, the primary source supports the following ordered description, from input to output ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)):

1. **Sense and word embeddings layer (bottom).** Holds two lookup tables. Sense embeddings are initialized randomly, since "no sense embedding is computed a priori," while word embeddings are initialized with pre-trained GloVe vectors ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Each individual input is copied to |D| positions of the context to form context components.
2. **Cosine layer.** Produces the sequence of cosine similarities between the examined sense embedding and each context word embedding ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).
3. **BLSTM layer.** Comprises two reversed unidirectional LSTMs; it encodes the sequential pattern of cosine similarities in both directions ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).
4. **Concatenation (merge) layer.** Joins the outputs of the left- and right-traversing LSTMs ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).
5. **Fully-connected layer.** Applies a ReLU activation to the merged representation using weights W_h and bias b_h ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).
6. **Sigmoid layer (top).** Produces a binary decision value ŷ_{s_i} for each candidate sense; an argmax across senses selects the final answer ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## 5. Why the Layer Count Matters

### 5.1 Depth and representational capacity

Describing the model as six layers rather than five matters because the paper explicitly presents its contribution as the reduction of a 57-classifier problem to a single network on the SensEval-3 benchmark ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The depth of that single network is one of its selling points: the cosine layer supplies the structural prior (sense–context similarity), the BLSTM supplies sequence modeling, and the dense-plus-sigmoid head supplies classification ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Collapsing the count to five silently deletes the layer that encodes the paper's central representational hypothesis — that a *sequence* of sense–context cosine similarities carries pattern-like information distinguishable for the correct sense ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

### 5.2 Hyperparameters and configuration

The six-layer count is also the count that aligns with the reported hyperparameter configuration. The paper's tuning table specifies an embedding size of 100, a BLSTM hidden layer size of 2×50, a context window of 15 left and 15 right, dropout of 20% on the sense/word embeddings, 50% on LSTM outputs, 50% on the fully-connected layer, and 20% word dropout ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The output weight matrix W_out is explicitly dimensioned R^{1×50}, matching the 50-unit hidden representation produced by the concatenated LSTM outputs ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). These settings map cleanly onto the six described stages, including the cosine computation that sits between the embedding lookups and the BLSTM.

### 5.3 Performance context

For completeness, the network evaluated on SensEval-3 achieved an F-measure of 72.5%, ranking fourth among supervised entries in the paper's comparison, just below IRST-Kernels (72.6%) and the co-leading Multi-classifier BLSTM and IMS+adapted CW (73.4% each) ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Ablations confirm that the architecture's specific layering is responsible for performance: shuffling the context reduced F-measure to 67.3%, reversing BLSTM directions to 68.9%, and replacing the BLSTM with fully-connected layers to 70.2% ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Any future replication or comparison must therefore describe the model with the correct number of components.

## 6. Verdict and Recommendations

Based on the weight of the evidence, my conclusion is that **the model has six layers**. The primary source states the total explicitly, lists six named components, describes the cosine computation in the body text, and provides equations for the remaining five components ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). The third-party note's five-layer claim omits exactly the cosine layer and incorrectly asserts that no other total layer count appears in the paper ([Third-party research note, n.d.](https://arxiv.org/abs/1802.09059)). The most parsimonious explanation is an omission or an out-of-date reading of the preprint, not a genuine architectural ambiguity.

Two caveats should be recorded for transparency. First, layer counting in neural network descriptions is partly conventional: whether embedding lookup tables count as a "layer," and whether a bidirectional wrapper counts as one layer or two, can vary by author. The Pesaranghader et al. (2018) paper resolves both conventions internally — it counts the sense and word embeddings layer as one layer, and treats the BLSTM as one layer even though it contains two reversed unidirectional LSTMs ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)). Second, derivative summaries should never be preferred over the primary text when they conflict on an explicit, checkable fact. Researchers citing this architecture should state that it is a six-layer network and enumerate the layers as sigmoid, fully-connected, concatenation, BLSTM, cosine, and sense/word embeddings ([Pesaranghader et al., 2018](https://arxiv.org/abs/1802.09059)).

## References

Pesaranghader, A., Pesaranghader, A., Matwin, S., & Sokolova, M. (2018). *One single deep bidirectional LSTM network for word sense disambiguation of text data.* arXiv. https://arxiv.org/abs/1802.09059

Third-party research note. (n.d.). *One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data* [Unpublished research note discussing arXiv:1802.09059]. https://arxiv.org/abs/1802.09059