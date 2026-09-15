# How Many Layers Does the Single-Classifier BLSTM Word Sense Disambiguation Model Have? A Source-Critical Report

## Abstract

This report addresses a precise architectural question concerning the single-classifier bidirectional LSTM (BLSTM) network proposed for word sense disambiguation (WSD): how many layers does the model contain? The available evidence is internally contradictory. The primary paper text explicitly states that the architecture depicted in Figure 1 comprises **six layers**, and enumerates them as a sigmoid layer, a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer ([document_1.txt](document_1.txt)). By contrast, a third-party research note asserts that the same paper reports **five layers**, listing a sigmoid layer, a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer, while omitting the cosine layer entirely ([document_2.txt](document_2.txt)). After weighing provenance, specificity, and internal consistency, this report concludes that the **six-layer count is the defensible answer**, and that the five-layer figure is an error introduced by the secondary source's omission of the cosine layer.

## Introduction: Framing the Query

The query under examination — "How many layers does their model have?" — appears simple but is rendered non-trivial by conflicting sources. The model in question is the single-classifier deep BLSTM network for WSD described in Section 3 of the source paper, titled "One Single BLSTM network for WSD" ([document_1.txt](document_1.txt)). The paper's own framing states that, given a document and the position of a target word, the model computes a probability distribution over the possible senses related to that word, and that this computation is implemented through a defined stack of named layers ([document_1.txt](document_1.txt)).

Because layer count is a fundamental architectural descriptor, resolving the discrepancy matters for anyone attempting to reproduce, compare, or critique the model. A one-layer difference is not cosmetic: it determines whether a cosine-similarity computation is treated as a distinct architectural stage or merely as an implicit preprocessing step. This report therefore examines both sources in detail, tabulates their claims, evaluates the reliability of each, and explains precisely where and why they diverge.

## The Primary Source Evidence: Six Layers

### The Explicit Enumeration in Section 3

The most direct and authoritative statement comes from the paper's own architectural description. Section 3 states that "the architecture of our model, depicted in Fig. 1, consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom)" ([document_1.txt](document_1.txt)). This sentence is decisive for three reasons: it states the total count numerically ("6 layers"), it provides a complete ordered enumeration of the constituent layers, and it anchors the description to a figure (Fig. 1) that visually presents the same structure ([document_1.txt](document_1.txt)).

The six named layers can be tabulated as follows, preserving the top-to-bottom ordering given in the paper:

| Position (Top → Bottom) | Layer Name | Stated Role Constraint |
|---|---|---|
| 1 | Sigmoid layer | Sits at the top; classification layer ([document_1.txt](document_1.txt)) |
| 2 | Fully-connected layer | Intermediate stage; dropout applied to its outputs ([document_1.txt](document_1.txt)) |
| 3 | Concatenation layer | Merge layer producing h_cl ([document_1.txt](document_1.txt)) |
| 4 | BLSTM layer | Sequence encoder over cosine-similarity patterns ([document_1.txt](document_1.txt)) |
| 5 | Cosine layer | Computes cosine similarities between sense and context words ([document_1.txt](document_1.txt)) |
| 6 | Sense and word embeddings layer | Sits at the bottom; input representation ([document_1.txt](document_1.txt)) |

### Supporting Architectural Details and Equations

The six-layer reading is corroborated by the paper's mathematical exposition. The output-side equation specifies that W_out ∈ R^{1×50} and b_out ∈ R are "the weights and the bias of the classification layer (sigmoid)," while h_cl "is the result of the merge layer (concatenation)" ([document_1.txt](document_1.txt)). This confirms the existence of both a sigmoid classification layer and a distinct concatenation (merge) layer as separate architectural entities.

Further, the hidden-layer computation is given as h_cl = ReLU(W_h · [h^L_{C−1}; h^R_{C+1}] + b_h) ([document_1.txt](document_1.txt)). The notation h^L_{C−1} and h^R_{C+1} refers to the left and right BLSTM hidden states relative to the target, confirming the BLSTM layer's position in the stack. The concatenation layer is thus concretely the operation merging these two directional representations before the fully-connected transformation.

The paper also describes where regularization is applied: "In our network, dropout is applied to the embeddings as well as the outputs of the merge and fully-connected layers" ([document_1.txt](document_1.txt)). This sentence independently references three distinct architectural loci — the embeddings layer, the merge (concatenation) layer, and the fully-connected layer — reinforcing that these are treated as separate layers in the design.

## The Secondary Source Claim: Five Layers

### What the Third-Party Note Asserts

The competing claim originates from a third-party research note catalogued as part of the corpus. It states: "The paper reports that the proposed single BLSTM model for word sense disambiguation has 5 layers. Section 3 One Single BLSTM network for WSD states that the architecture, depicted in Fig. 1, consists of 5 layers" ([document_2.txt](document_2.txt)). It further asserts that "the explicit total layer count given is 5 layers" ([document_2.txt](document_2.txt)) and that the named components are "a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, and a sense and word embeddings layer," with the sense and word embeddings layer on the bottom and the sigmoid layer at the top ([document_2.txt](document_2.txt)).

Critically, the note also makes a negative claim: "No other explicit total layer count for the model is stated in the paper" ([document_2.txt](document_2.txt)). As demonstrated above, this negative claim is false, because the paper's Section 3 does state an explicit total — the number six ([document_1.txt](document_1.txt)).

### Reconciling the Discrepancy: The Omitted Cosine Layer

A direct comparison of the two enumerations reveals the exact source of the divergence. The paper lists six items; the third-party note lists five. Four layers appear identically in both lists: sigmoid, fully-connected, concatenation, BLSTM, and sense and word embeddings. The single asymmetric element is the **cosine layer**, which appears in the paper's enumeration but is absent from the note's enumeration ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

This omission is consistent with a reading error rather than a genuine alternative architecture. The paper's own experimental rationale confirms that the cosine computation is architecturally meaningful: the authors investigated "if the sequential follow of cosine similarities computed between a true sense and its preceding and succeeding context words carries a pattern-like information that can be encoded with BLSTM" ([document_1.txt](document_1.txt)). They further state that "we expect the sequence result of similarities between the true sense and the surrounding context communicate a pattern-like information that can be encoded through our BLSTM network" ([document_1.txt](document_1.txt)). A computation that produces "a series of cosine similarities" fed sequentially into the BLSTM is, by the paper's own accounting, a layer in the pipeline — specifically the input-side stage that converts embeddings into similarity signals. Treating it as absent changes the architecture's description.

The following table summarizes the conflict:

| Layer | Paper (document_1.txt) | Third-Party Note (document_2.txt) | Status |
|---|---|---|---|
| Sigmoid | Included | Included | Agreed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Fully-connected | Included | Included | Agreed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Concatenation | Included | Included | Agreed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| BLSTM | Included | Included | Agreed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Cosine | Included | Omitted | Disputed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Sense and word embeddings | Included | Included | Agreed ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| **Total** | **6** | **5** | **Conflict** |

## Why Six Is the Defensible Answer

### Argument from Provenance and Specificity

The first evaluative criterion is provenance. The six-layer claim is drawn directly from the source paper's own architectural section, including its figure reference and its mathematical notation ([document_1.txt](document_1.txt)). The five-layer claim is drawn from a "third-party research note" that self-describes as addressing "key questions" about the paper ([document_2.txt](document_2.txt)). A primary architectural self-description outranks a secondary summary in reliability, particularly when the secondary summary is demonstrably incomplete.

### Argument from Internal Consistency

The second criterion is internal consistency. The paper's equations reference a sigmoid classification layer, a concatenation/merge layer, and BLSTM hidden states h^L_{C−1} and h^R_{C+1} ([document_1.txt](document_1.txt)). Its dropout discussion references embeddings, merge outputs, and fully-connected outputs ([document_1.txt](document_1.txt)). Its experimental section describes replacing the BLSTM with "two different fully-connected networks of the same size 50 (the size of the LSTMs outputs)" ([document_1.txt](document_1.txt)). Every one of these statements is compatible with a six-stage pipeline, and none requires the cosine stage to be excluded. The five-layer account, by contrast, requires one to disregard an explicit element in the paper's own list.

### Argument from the Functional Necessity of the Cosine Stage

The third criterion is functional. The paper's central hypothesis depends on cosine similarities between a target sense and its surrounding context words being sequentially encoded by the BLSTM ([document_1.txt](document_1.txt)). The BLSTM does not compute these similarities itself; it encodes their sequence. That computation must therefore occur at a defined point in the network — the point the paper names the cosine layer ([document_1.txt](document_1.txt)). Removing it from the layer count does not remove it from the model; it merely misdescribes the model.

## Empirical Context: The Full Network and Its Ablations

The paper's ablation study (Table 4) further reinforces that the full six-layer configuration is the reference model. The "Full network in Fig. 1" achieves an F-measure of 72.5%, and every modification is measured against it ([document_1.txt](document_1.txt)).

| Variant (Our Single-classifier) | F-measure (%) |
|---|---|
| Full network in Fig. 1 | 72.5 |
| BLSTM with reverse directions in Fig. 1 | 68.9 |
| BLSTM with a shuffled context | 67.3 |
| Fully-connected layers instead of BLSTM layer | 70.2 |
| BLSTM without GloVe for the context (all weights random) | 65.6 |
| BLSTM without word dropout | 71.1 |
| BLSTM with a larger context size [25 left, 25 right] | 71.4 |

(All values from [document_1.txt](document_1.txt).)

The pattern is instructive. Reversing the BLSTM directions costs 3.6 F-measure points (72.5 → 68.9), shuffling the context costs 5.2 points (→ 67.3), and removing GloVe context embeddings costs 6.9 points (→ 65.6) ([document_1.txt](document_1.txt)). The authors conclude that when the BLSTM is replaced by "two different fully-connected networks of the same size 50," results were "notably less than 72.5%" — specifically 70.2% ([document_1.txt](document_1.txt)). These experiments only make sense against a pipeline in which a cosine-computed sequence is fed to a BLSTM, which is exactly the structure the six-layer description captures.

For external context, the model's 72.5% places it just behind the multi-classifier BLSTM (73.4%) and IMS+adapted CW (73.4%), and ahead of nusels (72.4%), while substantially outperforming weaker entries such as DLSI-UA-LS-SU (44.4%) ([document_1.txt](document_1.txt)).

| System | F-measure (%) |
|---|---|
| Multi-classifier BLSTM | 73.4 |
| IMS+adapted CW | 73.4 |
| htsa3 | 72.9 |
| IRST-Kernels | 72.6 |
| **Our Single-classifier BLSTM** | **72.5** |
| nusels | 72.4 |
| DLSI-UA-LS-SU | 44.4 |

(Selected rows from [document_1.txt](document_1.txt).)

## Implications of the Discrepancy

The discrepancy has practical consequences for anyone reconstructing the model. A reader who accepts the five-layer account would build a network without an explicit cosine layer and would then be unable to reproduce the ablation results in Table 4, since the "shuffled context" and "reverse directions" manipulations operate specifically on the sequence of cosine similarities ([document_1.txt](document_1.txt)). Conversely, a reader who accepts the six-layer account has a coherent specification: embeddings at the bottom, cosine similarities computed and concatenated, encoded by a BLSTM, merged, passed through a fully-connected transformation, and classified by a sigmoid layer ([document_1.txt](document_1.txt)).

It is also worth noting the deliberate parameter-sharing design of the network, which the authors emphasize in contrast to other supervised neural WSD networks: rather than parameterizing a softmax layer per ambiguous word, "our network shares parameters over all words' senses" ([document_1.txt](document_1.txt)). This design choice is orthogonal to the layer count but underscores that the paper's architectural description is precise and intentional — which further undermines the plausibility that its "6 layers" statement is itself an error.

## Conclusion

Based on the evidence examined, the single-classifier BLSTM model for word sense disambiguation has **six layers**, not five. The primary paper text states this explicitly and enumerates the layers as a sigmoid layer, a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer, ordered from top to bottom ([document_1.txt](document_1.txt)). The competing five-layer claim in the third-party note arises from the omission of the cosine layer from its enumeration and from its incorrect assertion that no other explicit total is stated in the paper ([document_2.txt](document_2.txt)). Because the primary source is more authoritative, more specific, and internally consistent with the paper's equations, ablation design, and dropout description, the six-layer figure should be treated as the correct answer, and the five-layer figure as a secondary-source error. Where the two sources conflict, the paper's own words — "consist of 6 layers" — control ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data* — primary paper text, including Section 3, equations, ablation Table 4, and results tables. [document_1.txt](document_1.txt)

document_2.txt. (n.d.). *Third-party research note: One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data* — secondary summary noting a five-layer architecture and layer-count queries. [document_2.txt](document_2.txt)