# How Many Layers Does the Single Classifier BLSTM Word Sense Disambiguation Model Have?

## 1. Introduction and Statement of the Query

The architecture in question is the single-classifier bidirectional LSTM (BLSTM) network proposed for word sense disambiguation (WSD) of text data, presented in the paper *One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data* ([document_1.txt](document_1.txt)). The specific query — "How many layers does their model have?" — is answered explicitly in the paper's Section 3, which states that the architecture depicted in Fig. 1 "consist[s] of 6 layers" ([document_1.txt](document_1.txt)). A second source, a third-party research note, reports the same model as having 5 layers ([document_2.txt](document_2.txt)). This report examines both accounts, weighs their reliability, and delivers a concrete, defensible answer: **the model has six named layers**, and the five-layer figure is an incomplete enumeration that omits the cosine layer.

The discrepancy is not a matter of interpretive taste about what counts as a "layer." Both sources count the input embeddings, the concatenation/merge operation, the BLSTM, the fully-connected layer, and the sigmoid classifier. The entire disagreement reduces to one component: the cosine layer, which appears in the primary paper's enumeration but is absent from the third-party note's list.

## 2. Direct Evidence from the Primary Paper: Six Layers

### 2.1 The Explicit Enumeration in Section 3

The primary source is unambiguous and self-contained. Section 3, titled "One Single BLSTM network for WSD," opens with the following statement:

> "Given a document and the position of a target word, our model computes a probability distribution over possible senses related to that word. The architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)." ([document_1.txt](document_1.txt))

This single sentence supplies three distinct pieces of information: an explicit total (6), an exhaustive ordered list of the six components, and their vertical ordering (sigmoid at the top; sense and word embeddings at the bottom). The count is not inferred, aggregated, or reconstructed from a figure — it is stated numerically in prose. That is the strongest possible form of evidence for a layer-count query, because it removes the need to adjudicate whether particular functional blocks (such as a concatenation operation) "deserve" to be called layers; the authors themselves make that determination and enumerate accordingly.

### 2.2 Corroborating Functional Evidence for the Cosine Layer

The paper's own experimental narrative reinforces that a cosine-comparison stage is a genuine, load-bearing part of the network rather than an incidental detail. In the description of the ablation study, the authors write that "it is expected that the cosine similarities of closer words (in the context) to the true sense be larger than the incorrect senses'" and that they set out to test "if a series of cosine similarities can be encoded through an LSTM (or BLSTM) network" ([document_1.txt](document_1.txt)). Cosine similarity between the target sense and its surrounding context words is thus the quantity the BLSTM sequentially encodes — which means the cosine layer sits functionally between the embedding layer and the BLSTM, exactly where the six-layer enumeration places it. Removing it from an inventory of the architecture is therefore not a harmless simplification; it deletes the operation that generates the network's input signal to the recurrent stage.

## 3. The Competing Five-Layer Account

### 3.1 Content of the Third-Party Research Note

The second source is described in its own text as a "Third-party research note" addressed to questions including "Pesaranghader BLSTM WSD network architecture components" and "BLSTM word sense disambiguation model layer count" ([document_2.txt](document_2.txt)). It asserts:

> "The named layers that make up the architecture are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer." ([document_2.txt](document_2.txt))

It further states that "The paper reports that the proposed single BLSTM model for word sense disambiguation has 5 layers" and that "Section 3 One Single BLSTM network for WSD states that the architecture, depicted in Fig. 1, consists of 5 layers" ([document_2.txt](document_2.txt)). Notably, the same note claims that "No other explicit total layer count for the model is stated in the paper" ([document_2.txt](document_2.txt)) — a claim directly falsified by the primary source's sentence quoted in Section 2.1 above ([document_1.txt](document_1.txt)).

### 3.2 Assessment of Source Reliability

Reliability must be weighed here rather than assumed. The two documents differ in provenance, proximity to the original work, and internal consistency.

| Criterion | Primary paper excerpt ([document_1.txt](document_1.txt)) | Third-party note ([document_2.txt](document_2.txt)) |
|---|---|---|
| Relationship to the model | Authored account of the model; reports its own Fig. 1 and Section 3 | External commentary summarising the paper |
| Layer count stated | 6 | 5 |
| Components listed | Sigmoid, fully-connected, concatenation, BLSTM, cosine, sense and word embeddings | Sigmoid, fully-connected, concatenation, BLSTM, sense and word embeddings |
| Missing relative to the other | — | Cosine layer |
| Internal consistency | Count matches its own six-item list | Count matches its own five-item list, but contradicts the primary text it summarises |
| Claim about other totals | Provides the explicit total | States "no other explicit total layer count … is stated in the paper" |

Two features of the table are decisive. First, the third-party note's five-item list and its five-layer total are internally consistent with each other but exclude a component that the primary source explicitly names. Second, the note misdescribes the primary source's own statements about the total, which weakens its authority as a summary. Where a secondary summary and the underlying text conflict on a factual enumeration, the underlying text governs.

## 4. Reconciliation: Why Six Is the Defensible Count

My assessment is that the model has **six layers**, and that the five-layer figure arises from an omission of the cosine layer during summarisation rather than from a different, equally valid counting convention. Three considerations support this position.

First, both sources employ the same counting convention on every other component. They both count the sense and word embeddings layer as a layer ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)); they both count the concatenation/merge layer as a layer ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)); they both count the BLSTM as a single layer ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). In other words, the note does not adopt a stricter definition that would exclude input or merging layers — it would have had to exclude three of its own five entries to do so. The one-point difference therefore cannot be explained by convention; it can only be explained by the absent cosine layer.

Second, the primary source contains internal evidence that the cosine layer is real and operative, as discussed in Section 2.2: the ablation study is organised around whether sequences of cosine similarities can be encoded by the BLSTM ([document_1.txt](document_1.txt)). An architecture that computes and sequences cosine similarities between sense and context embeddings must contain the operation that performs that computation.

Third, the second source's assertion that no other explicit total exists in the paper is demonstrably inaccurate ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). This is a verifiable error of fact about the primary text, which reduces confidence in the note's other summarising judgements, including its layer count.

## 5. Layer-by-Layer Description of the Six-Layer Architecture

### 5.1 Sense and Word Embeddings Layer (bottom)

This layer sits at the bottom of the stack and supplies vector representations for both the senses and the words of the context ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The ablation table reports a variant in which the context embeddings are not initialised with GloVe ("BLSTM without GloVe for the context (all weights are random)") and which scores 65.6 F-measure, compared with 72.5 for the full network ([document_1.txt](document_1.txt)) — evidence that this layer is a substantive, trainable part of the architecture.

### 5.2 BLSTM Layer

A single BLSTM layer processes the sequence of sense–context similarity information in both directions ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). It is counted as one layer in the total ([document_2.txt](document_2.txt)). Its hidden states feed the subsequent hidden computation: the hidden layer h_cl is obtained as ReLU(W_h · [h^L_{C−1}; h^R_{C+1}] + b_h), i.e., a linear projection of the concatenated bidirectional states at neighbouring context positions, plus a bias, passed through a rectified linear unit ([document_1.txt](document_1.txt)). The dimension of the LSTM outputs is 50, as revealed by the comparison against "fully-connected networks of the same size 50 (the size of the LSTMs outputs)" ([document_1.txt](document_1.txt)).

### 5.3 Cosine Layer

This is the component in dispute. It computes the cosine similarities between a true sense and its preceding and succeeding context words, producing the sequential signal that the BLSTM encodes ([document_1.txt](document_1.txt)). It is named in the primary source's six-layer enumeration but omitted from the third-party note's list ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

### 5.4 Concatenation (Merge) Layer

The merge layer concatenates the bidirectional representations; its output is denoted h_cl, which is described as "the result of the merge layer (concatenation)" ([document_1.txt](document_1.txt)). Dropout is applied to the output of this merge layer, as well as to the embeddings and the fully-connected layer outputs ([document_1.txt](document_1.txt)).

### 5.5 Fully-Connected Layer

A fully-connected layer sits between the concatenation layer and the top sigmoid classifier ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Removing the recurrent stage in favour of two fully-connected networks of size 50 ("Fully-connected layers instead of BLSTM layer") reduced performance to 70.2 F-measure versus 72.5 for the full network, indicating that the fully-connected layer alone does not substitute for the BLSTM's sequential encoding ([document_1.txt](document_1.txt)).

### 5.6 Sigmoid Classification Layer (top)

The top layer is a sigmoid classifier. Its weights and bias are given as W_out ∈ R^{1×50} and b_out ∈ R, taking h_cl as input and producing the classification output ([document_1.txt](document_1.txt)). The paper notes that, unlike other supervised neural WSD networks that use a softmax layer with cross-entropy or hinge loss and parameterise a separate weight matrix and bias vector per ambiguous word, this network shares parameters over all words' senses, which keeps it computationally efficient while encoding statistical information across words ([document_1.txt](document_1.txt)).

## 6. Parameter and Dimensional Evidence Relevant to Layer Counting

The excerpted equations provide dimensional anchors that are consistent with a six-stage pipeline: a 50-dimensional hidden representation h_cl feeds a 1 × 50 weight matrix and a scalar bias in the sigmoid layer ([document_1.txt](document_1.txt)). The 50-dimensional scale recurs in the ablation comparison against "fully-connected networks of the same size 50 (the size of the LSTMs outputs)" ([document_1.txt](document_1.txt)). These are parameterisation facts rather than layer counts, but they confirm that the enumerated components — merge output, hidden projection, recurrent stage, classification head — are distinct computational stages with their own parameters, which is the practical definition of a layer in descriptions of this kind.

## 7. Behavioural Evidence on the Contribution of Individual Layers

The ablation study ("Within-our-model comparisons") reports how the network behaves when particular components or inputs are altered ([document_1.txt](document_1.txt)). These figures quantify the contribution of the recurrent stage and the embeddings, and they are the paper's principal internal evidence about architectural necessity.

| Configuration | F-measure (%) |
|---|---|
| Full network in Fig. 1 | 72.5 |
| BLSTM with reversed directions | 68.9 |
| BLSTM with a shuffled context | 67.3 |
| Fully-connected layers instead of BLSTM layer | 70.2 |
| BLSTM without GloVe for the context (weights random) | 65.6 |
| BLSTM without word dropout | 71.1 |
| BLSTM with a larger context size [25 left, 25 right] | 71.4 |

Source: ([document_1.txt](document_1.txt)).

For external context, the full single-classifier network's 72.5 F-measure places it fifth in the reported ranking, behind a multi-classifier BLSTM (73.4, tied for first with IMS+adapted CW), htsa3 (72.9), and IRST-Kernels (72.6), and ahead of nusels (72.4); the ranking table extends down to 44.4 ([document_1.txt](document_1.txt)). These results concern performance, not layer count, but they establish that the six-layer network as described is a competitive, fully specified system rather than a schematic.

## 8. Implications of the Discrepancy for Literature Users

Users of the secondary note should be aware of a specific failure mode: a summariser that recounts an architecture from a figure or from memory can silently drop a stage while still producing a numerically consistent count ([document_2.txt](document_2.txt)). The correct procedural response is to prefer the primary text's explicit enumeration and to verify totals against the full component list. Applied here, the check is straightforward: the primary list contains six items and states six ([document_1.txt](document_1.txt)); the secondary list contains five items and states five, and its claim that the paper states no total is false ([document_2.txt](document_2.txt)). Anyone citing the layer count for this WSD model should therefore cite six layers and attribute the figure to Section 3 of the paper.

## 9. Conclusion

The single-classifier BLSTM model for word sense disambiguation has **6 layers**, as explicitly stated in Section 3 of the primary paper: a sigmoid layer at the top, a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer at the bottom ([document_1.txt](document_1.txt)). The BLSTM counts as one of those six layers ([document_2.txt](document_2.txt)). The competing five-layer figure reported by the third-party research note is best explained as an omission of the cosine layer, since the note otherwise adopts identical counting conventions for the embeddings, concatenation, and BLSTM components and even asserts, incorrectly, that the paper states no total layer count ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Where the two sources conflict, the primary text — which both enumerates the six named components and supplies corroborating functional evidence for the cosine stage in its own ablation discussion — is the more reliable authority ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *One single deep bidirectional LSTM network for word sense disambiguation of text data* [Excerpts from the primary paper, including Section 3 and Table 4]. Retrieved September 15, 2026.

document_2.txt. (n.d.). *Third-party research note: One single deep bidirectional LSTM network for word sense disambiguation of text data* [Research note]. Retrieved September 15, 2026.