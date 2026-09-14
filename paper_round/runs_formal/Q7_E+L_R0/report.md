# Annotation Workforce and Disagreement Resolution in the OGTD Greek Offensive-Language Dataset

## 1. Introduction

This report answers a narrowly defined methodological question about the Offensive Greek Tweet Dataset (OGTD): **how many annotators labeled the dataset, and how were disagreements between them resolved?** The short answer, drawn directly from the source paper, is that a team of **three volunteers** performed the initial classification of every tweet, and that disagreement was handled through a two-stage rule: labels with **100% agreement** were accepted outright, labels with **majority agreement above 66%** were accepted as final, and cases of **complete disagreement** among the three annotators were escalated to an adjudication panel consisting of **one of the paper's authors plus two additional human judges**, who were tasked with reaching the same "above 66%" majority threshold ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). A third-party summary of the same dataset restates this protocol in nearly identical terms ([Third-party summary: OGTD Greek offensive-language dataset](document_2.txt)).

The remainder of this report situates that answer within the full annotation pipeline, quantifies the human workforce involved at each stage, analyzes the arithmetic and consequences of the "above 66%" rule, and identifies the points where the documented protocol is silent or ambiguous.

## 2. Source Base and Evidentiary Hierarchy

Two distinct documents are provided, although the supplied material repeats them several times. The first, `document_1.txt`, is an extract from the source paper *Offensive Language Identification in Greek* (arXiv:2003.07459), specifically the section titled "The OGTD Dataset :: Pre-processing and annotation" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). This is the primary source: it is the original methodological description written by the dataset creators, and it carries the greatest evidentiary weight for questions about annotation procedure. The arXiv identifier prefix (2003) indicates a March 2020 submission, which situates the work in the early wave of offensive-language dataset construction for less-resourced languages.

The second document, `document_2.txt`, is explicitly labeled a "Third-party summary: OGTD Greek offensive-language dataset" ([Third-party summary: OGTD Greek offensive-language dataset](document_2.txt)). It is a derivative, secondary source whose content is traceable to the primary document. In line with the principle of prioritizing reliable primary sources over secondary restatements, all substantive claims in this report are anchored to the paper, with the summary used as a cross-check for interpretive fidelity.

Notably, the two sources do not conflict. Where they differ at all, they differ only in wording: the paper refers to "100% agreement" while the summary says "unanimous agreement"; the paper refers to "two extra human judges" while the summary says "two additional judges." These are terminological equivalences, not methodological disagreements.

## 3. How Many Annotators Labeled the OGTD Dataset?

### 3.1 The Primary Annotation Team

The dataset was labeled by **three volunteers**, each of whom was "asked to classify each tweet in the dataset" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). The phrase "each tweet" is significant: this was not a distributed or partially overlapping annotation design in which different annotators saw different subsets. Rather, it was a fully crossed design in which every item received three independent judgments, which is the necessary precondition for computing inter-annotator agreement over the whole corpus and for applying majority rules item by item.

The fact that the annotators are described as "volunteers" — rather than as authors, students, or paid crowdworkers — is the only information the provided text supplies about their recruitment or status. No demographic information, linguistic background, training procedure, or compensation arrangement is reported in the excerpt.

### 3.2 The Escalation Panel

For cases of complete disagreement, the workforce expanded. The paper states that "one of the authors reviewed the tweets with two extra human judges to reach the desired majority above 66%" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). This creates a second, distinct group of annotators: a three-person adjudication panel composed of **one author of the paper** and **two additional human judges**.

Two inferences are warranted here, and both should be flagged as inferences rather than direct statements. First, the wording "extra human judges" strongly suggests that these two judges were *not* members of the original three-volunteer team; they were brought in specifically for adjudication. Second, because the panel is described as an author plus two judges, it appears to have been deliberately constituted as a fresh three-person body capable of producing its own majority, rather than as an extension of the original panel.

### 3.3 Aggregate Human Involvement

Combining the two stages, a minimum of **six distinct individuals** are implicated in the labeling pipeline: three original volunteers, two extra judges, and one author. This is a minimum, not a fixed figure, because the text does not specify whether the same author and the same two judges handled every escalated item, or whether different individuals were used across different disputes.

| Stage | Role | Number of people | Function |
|---|---|---|---|
| Stage 1 | Volunteers | 3 | Independent classification of every tweet |
| Stage 2 | Adjudication panel | 1 author + 2 extra judges = 3 | Re-review of completely disagreed items to reach >66% majority |
| Total | — | 6 (minimum) | End-to-end label production |

A single tweet therefore received either three human judgments (the common case) or up to six (the escalated case).

## 4. How Disagreements Were Resolved

The resolution mechanism is a cascading, threshold-based decision rule with three tiers. It is summarized below and then examined tier by tier.

| Agreement tier | Criterion in the source | Action taken | Source |
|---|---|---|---|
| Unanimous | 100% agreement (3 of 3) | Label "deemed acceptable" and retained | ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)) |
| Partial disagreement | Majority agreement above 66% | Majority label selected | ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)) |
| Complete disagreement | No majority (three-way split) | Escalated to one author + two extra judges, targeting >66% | ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)) |

### 4.1 Step One: Independent Classification

All three volunteers classified every tweet. This produced a three-way judgment vector for each item and made it possible to compute agreement across the dataset ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)).

### 4.2 Step Two: Inter-Annotator Agreement Calculation

The paper states that "inter-annotator agreement was calculated" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). This is an important procedural step because it establishes that agreement was not merely eyeballed but computed. However, the excerpt does not name the statistic used. It is unclear whether the calculation was a simple percentage-agreement figure or a chance-corrected coefficient; the text only reports the resulting decision thresholds.

### 4.3 Step Three: Unanimity as the Gold Standard

Labels supported by all three annotators were treated as acceptable without further review ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). The third-party summary uses the word "unanimous" for the same criterion ([Third-party summary: OGTD Greek offensive-language dataset](document_2.txt)). This tier functions as the highest-confidence stratum of the dataset.

### 4.4 Step Four: Qualified Majority Above 66%

Where the three annotators disagreed but still produced a majority, that majority label was accepted, provided it exceeded 66% ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). The third-party summary confirms the same resolution rule ([Third-party summary: OGTD Greek offensive-language dataset](document_2.txt)).

### 4.5 Step Five: Complete Disagreement and Escalation

The final tier covers "labels with complete disagreement between annotators" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). In this situation, the original three annotations offered no majority at all, so the item was routed to a new three-person body — one author plus two extra judges — with the explicit instruction to "reach the desired majority above 66%" ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459)). The phrase "desired majority" indicates that the escalation was intended to reproduce, not relax, the standard applied in the earlier tier.

## 5. Analysis of the 66% Threshold

A striking structural feature of this protocol is the precise fit between the threshold and the panel size. With exactly three annotators, the only possible agreement levels are 100% (3 of 3), approximately 66.67% (2 of 3), and approximately 33.33% (1 of 3). A rule requiring "majority agreement above 66%" is therefore arithmetically equivalent to requiring a two-thirds majority: it accepts the 2-of-3 case and rejects the 1-of-3 case. In other words, the apparently odd percentage figure is not arbitrary — it is the minimal threshold that distinguishes a genuine majority from a mere plurality under a three-annotator design.

A second structural observation concerns feasibility. A three-way split — that is, "complete disagreement" — can only occur if the annotation scheme contains at least three mutually exclusive categories, since each annotator must have selected a different label. This is an inference about the label inventory derived purely from the described disagreement pattern, not a direct statement in the sources.

A third observation concerns the escalation design. By constituting the adjudication panel with three people rather than, say, a single expert adjudicator, the authors preserved the same arithmetic structure at the appeal stage: the two-thirds rule could be reapplied identically. This consistency is methodologically elegant, and it is the strongest design feature evident in the provided text.

## 6. Comparative Reading of the Sources

| Element | Primary source (document_1.txt) | Third-party summary (document_2.txt) | Consistent? |
|---|---|---|---|
| Initial annotators | "A team of three volunteers" | "A team of three volunteer annotators" | Yes |
| Scope | "classify each tweet in the dataset" | "classified each tweet" | Yes |
| Agreement computation | "Inter-annotator agreement was calculated" | Not mentioned | Partial (summary omits) |
| Acceptance rule | "labels with 100% agreement were deemed acceptable" | "Labels with unanimous agreement were accepted" | Yes |
| Disagreement rule | "majority agreement above 66% were selected" | "resolved by majority above 66%" | Yes |
| Escalation rule | "one of the authors reviewed the tweets with two extra human judges" | "one author plus two additional judges reviewed the tweet" | Yes |
| Escalation target | "to reach the desired majority above 66%" | "to reach a majority" | Partial (summary omits the threshold) |

The summary is faithful but lossy: it drops the inter-annotator agreement computation and the repeated numeric threshold at the escalation stage. For any rigorous methodological purpose, the primary source should be preferred.

## 7. Limitations and Unresolved Questions

Several elements of the protocol remain unspecified in the provided material. The specific agreement statistic is unnamed. The identity and qualifications of the two extra judges are unknown. It is not stated whether adjudication was blind, whether adjudicators saw the original three labels, or whether adjudication could itself fail to reach a two-thirds majority and require yet another round. The number of items that fell into each tier is not reported. Finally, the temporal gap between the 2020 source paper and the present date is significant, and no more recent re-annotation or replication study is included in the provided corpus, so it is not possible to establish whether the protocol has since been revised.

## 8. Assessment

Based on the evidence available, my assessment is that the OGTD annotation protocol represents a defensible, resource-conscious design. It uses a small, fully crossed team of three annotators, applies a transparent and internally consistent decision rule, and reserves expensive expert adjudication only for the rare case of three-way disagreement. The use of a 66% threshold is not a rough heuristic but the exact arithmetic consequence of a three-person panel, and the decision to mirror that panel size at the escalation stage is a genuinely sound choice. The principal weakness is reporting rather than design: the sources describe the *rules* of agreement in detail but not the *results* — no agreement coefficient, no tier-level counts, and no information about the adjudicators. A reader can reconstruct precisely how labels were decided, but not how often the difficult cases arose.

## 9. Conclusion

In direct answer to the query: **the OGTD dataset was initially labeled by three volunteer annotators, each of whom classified every tweet; disagreements were resolved by accepting 100%-agreement labels outright, accepting any majority above 66% as final, and escalating complete three-way disagreements to a new panel consisting of one author and two additional human judges, which was charged with reaching the same above-66% majority** ([Offensive Language Identification in Greek](https://arxiv.org/abs/2003.07459); [Third-party summary: OGTD Greek offensive-language dataset](document_2.txt)). At minimum, six individuals were involved across the pipeline, and any single tweet received either three or up to six human judgments depending on whether it triggered escalation.

## References

*Offensive language identification in Greek* (arXiv:2003.07459), Section: The OGTD Dataset :: Pre-processing and annotation (document_1.txt). https://arxiv.org/abs/2003.07459

*Third-party summary: OGTD Greek offensive-language dataset* (document_2.txt). [Unpublished summary document].