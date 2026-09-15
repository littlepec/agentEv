# Layer Count of the Single-Classifier BLSTM Word Sense Disambiguation Model

## Introduction and Scope of the Report

The question of how many layers a neural network contains appears, at first glance, to be a simple matter of counting. In practice, however, layer counts in published architectures are frequently contested because authors, reviewers, and secondary commentators disagree about which components qualify as "layers," whether a bidirectional wrapper counts as one layer or two, and whether embedding or output layers are included in the tally. The present report addresses precisely this issue for the single-classifier bidirectional LSTM (BLSTM) model proposed for word sense disambiguation (WSD) in the source material. The evidence available consists of two documents: a primary document containing the paper's own architectural description and experimental results, and a secondary research note summarizing that architecture. These two sources are not fully consistent with one another, and the central analytical task of this report is to reconcile them, weigh their reliability, and arrive at a defensible conclusion.

## Identification of the Model in Question

Before counting layers, it is necessary to establish which model is being counted. The source material describes several competing systems. Under the heading "One Single BLSTM network for WSD," the primary document states that, given a document and the position of a target word, "our model computes a probability distribution over possible senses related to that word" ([Document 1](document_1.txt)). The same source contrasts this model with "other supervised neural WSD networks in which generally a softmax layer — with a cross entropy or hinge loss — is parameterized by the context words," noting instead that the proposed network "shares parameters over all words' senses" ([Document 1](document_1.txt)). This parallel-parameterization design is the defining architectural commitment of the single-classifier model, and it distinguishes the model from the Multi-classifier BLSTM, which uses separate upper layers for each ambiguous word ([Document 1](document_1.txt)). The layer count discussed in this report therefore applies specifically to the single-classifier BLSTM model depicted in Fig. 1 of the primary document, and not to the Multi-classifier BLSTM or to the IMS+adapted CW model, both of which are treated as state-of-the-art comparators ([Document 1](document_1.txt)).

## The Primary Source's Explicit Layer Count

The primary document offers a direct, unambiguous numerical statement. In Section 3, it declares: "The architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)" ([Document 1](document_1.txt)). This sentence simultaneously supplies the total count and an ordered enumeration of the constituents, from the output end to the input end.

### Enumerated Layer Structure

| Position | Layer (as named in the primary source) | Role as described |
|---|---|---|
| 1 (top) | Sigmoid layer | Classification layer producing the output probability |
| 2 | Fully-connected layer | Hidden transformation above the merge layer |
| 3 | Concatenation layer | Merge layer combining left and right BLSTM states |
| 4 | BLSTM layer | Bidirectional sequence encoder over cosine similarities |
| 5 | Cosine layer | Computes similarity between sense and context words |
| 6 (bottom) | Sense and word embeddings layer | Contains the sense and word embedding parameters |

The internal equations in the primary document corroborate this enumeration. Equation (3) specifies that the weights and bias of "the classification layer (sigmoid)" are of shape belonging to that final layer, and identifies the merge layer as the concatenation operation, stating that the quantity feeding it "is the result of the merge layer (concatenation)" ([Document 1](document_1.txt)). A further equation defines the hidden layer as a rectified linear unit applied to a weighted concatenation of the left and right BLSTM outputs, plus a bias term ([Document 1](document_1.txt)). The presence of a distinct cosine layer is structurally necessary in this account, because the network's BLSTM is described as encoding "the sequential follow of cosine similarities computed between a true sense and its preceding and succeeding context words" ([Document 1](document_1.txt)). In other words, the cosine computations are the input sequence that the BLSTM consumes, which explains why the cosine layer sits between the embeddings and the BLSTM.

## Conflicting Evidence: The Secondary Research Note

The secondary document presents a different total. It states that "the paper reports that the proposed single BLSTM model for word sense disambiguation has 5 layers," and that "Section 3 One Single BLSTM network for WSD states that the architecture, depicted in Fig. 1, consists of 5 layers" ([Document 2](document_2.txt)). Crucially, when the note enumerates the named components, it lists "a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer," and asserts that these components "define the full layer structure" ([Document 2](document_2.txt)). The cosine layer is absent from this enumeration.

The note also specifies how the BLSTM is counted: "The BLSTM is treated as one layer within the total layer count; the paper lists the BLSTM layer as one of the five layers," and it adds that "no other explicit total layer count for the model is stated in the paper" ([Document 2](document_2.txt)). This last claim is factually incorrect with respect to the primary document, which does state an explicit total — six ([Document 1](document_1.txt)).

## Reconciling the Discrepancy

The two sources agree on the identity and ordering of five components: sigmoid, fully-connected, concatenation, BLSTM, and sense/word embeddings. They diverge on exactly one element: the cosine layer. The difference between the counts of six and five is therefore fully explained by the inclusion or omission of that single component, rather than by any disagreement about how the BLSTM is counted.

Several considerations bear on which account should be preferred. First, the primary document is the more authoritative source on the question of what the paper itself states, because it contains the paper's own architectural prose and the equations that reference the layers. The secondary document is explicitly labeled a "third-party research note" and is a summary rather than an original description ([Document 2](document_2.txt)). Second, the primary document's enumeration is internally consistent: the cosine layer is functionally required by the model's own logic, since the BLSTM is defined as operating over a sequence of cosine similarities ([Document 1](document_1.txt)). Removing the cosine layer from the account leaves that sequence ungenerated. Third, the secondary note's assertion that "no other explicit total layer count for the model is stated in the paper" is contradicted by the primary document's explicit statement of six layers ([Document 1](document_1.txt); [Document 2](document_2.txt)).

A plausible explanation for the divergence is that the secondary note collapsed the cosine computation into the embedding or BLSTM stage, treating it as an operation rather than a layer — a common simplification in summary descriptions. Another possibility is that different versions of the paper or figure exist, with the note reflecting an earlier or simplified rendering. On the evidence provided, however, the primary document's explicit and enumerated count of six layers, including a cosine layer, is the best-supported answer.

## Summary of the Two Accounts

| Source | Reported total | Components listed | Cosine layer included? |
|---|---|---|---|
| Primary document (Section 3, Fig. 1) | 6 layers | Sigmoid, fully-connected, concatenation, BLSTM, cosine, sense and word embeddings | Yes ([Document 1](document_1.txt)) |
| Secondary research note | 5 layers | Sigmoid, fully-connected, concatenation, BLSTM, sense and word embeddings | No ([Document 2](document_2.txt)) |

## Why the Layer Count Is Architecturally Significant

The layer count is not a cosmetic detail; it encodes the model's central design claim. The proposed network "shares parameters over all words' senses," in contrast to softmax-based networks that parameterize a weight matrix and bias vector "for each ambiguous word's senses" ([Document 1](document_1.txt)). The shared-parameter design is intended to "encode statistical information across different words," enabling the model "to select the true sense (or even a proper word) in a blank space within a context" ([Document 1](document_1.txt)). The cosine layer is integral to this scheme because it provides a fixed, sense-agnostic similarity signal between a candidate sense and each context word, which the shared BLSTM then processes sequentially. Counting that layer correctly is thus essential to representing how the model actually generates its inputs.

## Performance Evidence Associated with the Architecture

The primary document reports results for the full network and for controlled ablations of its components, which provide indirect corroboration that the described six-layer structure is the operative design. The full network achieves an F-measure of 72.5% on SensEval-3, ranking fifth among the listed systems, tied in ranking position with nusels at 72.4% and trailing Multi-classifier BLSTM and IMS+adapted CW at 73.4% ([Document 1](document_1.txt)).

| Configuration described | F-measure (%) |
|---|---|
| Full network in Fig. 1 | 72.5 |
| BLSTM with reverse directions | 68.9 |
| BLSTM with a shuffled context | 67.3 |
| Fully-connected layers instead of BLSTM layer | 70.2 |
| BLSTM without GloVe for the context (random weights) | 65.6 |
| BLSTM without word dropout | 71.1 |
| BLSTM with a larger context size (25 left, 25 right) | 71.4 |

All figures are from the primary document's Table 4 ([Document 1](document_1.txt)). The ablations confirm that the sequence-modeling role of the BLSTM layer is consequential: replacing the BLSTM with two fully-connected networks of the same size (50, matching the LSTM outputs) produced results "notably less than 72.5%" ([Document 1](document_1.txt)).

## Training and Regularization Context

The layer count should be read alongside the training regime, which affects how the architecture behaves. For hyper-parameter selection, 5% of the training samples were reserved for validation, after which "the whole network is trained on all training samples prior to testing" ([Document 1](document_1.txt)). Although binary cross-entropy is common with a sigmoidal output unit, the authors found that "mean square error led to better results for the final argmax classification," and they employed RMSprop for optimization, updating "all weights including embeddings" ([Document 1](document_1.txt)). Dropout is "applied to the embeddings as well as the outputs of the merge and fully-connected layers" ([Document 1](document_1.txt)), and word dropout is reported to improve generalization, as is the use of GloVe pre-trained embeddings and an appropriate context size ([Document 1](document_1.txt)).

## Conclusion

The most defensible answer to the question of how many layers the single-classifier BLSTM model has is six. This figure is stated explicitly and enumerated by the primary document, which lists a sigmoid layer, a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer ([Document 1](document_1.txt)). The competing figure of five layers comes from a secondary third-party note that omits the cosine layer and incorrectly asserts that the paper states no other total ([Document 2](document_2.txt)). Because the primary source is more authoritative, because its count is internally consistent with the model's own equations and with the BLSTM's stated operation over cosine similarities, and because the entire numerical discrepancy reduces to one omitted component, the six-layer account should be preferred. Readers comparing the two sources should note that the disagreement is not about whether the BLSTM counts as one layer — both accounts treat it as one — but solely about whether the cosine stage is counted among the model's layers.

## References

Document 1. (n.d.). *One Single BLSTM network for WSD* [Manuscript]. document_1.txt.

Document 2. (n.d.). *Third-party research note: One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data*. document_2.txt.