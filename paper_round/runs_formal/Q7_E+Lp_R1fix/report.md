# Annotator Count and Disagreement Resolution in the OGTD Greek Offensive-Language Dataset

## Purpose and Scope of This Report

This report addresses a narrowly defined but methodologically consequential question about the Offensive Language Identification in Greek (OGTD) dataset: **how many annotators labelled the data, and how were disagreements between them resolved?** The evidence base available for this analysis consists of two documents. The first is an excerpt from the source paper itself, titled *Offensive Language Identification in Greek* (arXiv:2003.07459), specifically from the section "The OGTD Dataset :: Pre-processing and annotation," which was supplied as `document_1.txt` ([document_1.txt](https://arxiv.org/abs/2003.07459)). The second is a third-party summary of the same dataset, supplied as `document_2.txt` ([document_2.txt](document_2.txt)).

These two documents agree on the substance of the disagreement-resolution protocol but diverge on the number of annotators. Because annotator counts and adjudication rules directly affect the reliability, reproducibility, and interpretability of any human-labelled corpus, this report treats the discrepancy as a substantive finding rather than a trivial detail. The report first establishes the background of the annotation task, then reports the direct evidence, then reconstructs the resolution protocol tier by tier, then analyses the arithmetic implications of the stated agreement thresholds, and finally offers a reasoned assessment of which figure should be treated as authoritative and why.

## Background: Why Annotation Design Matters for OGTD

The OGTD dataset was constructed to support offensive language identification in Greek-language social media text, and the annotation procedure described in the source paper governs how each tweet received its final label. In any such corpus, two design parameters are decisive for data quality. The first is the **size and composition of the annotator pool**, because a larger pool can dilute idiosyncratic judgements while a smaller pool can reduce the cost and complexity of coordination. The second is the **rule by which disagreement is converted into a final label**, because that rule determines how much dissenting opinion is discarded or overridden before the label enters the dataset ([document_1.txt](https://arxiv.org/abs/2003.07459)).

Both documents indicate that OGTD used a multi-stage, threshold-based adjudication scheme rather than a simple majority-of-all-votes approach or a purely expert-driven single-annotator scheme. This means the dataset's final labels rest on a layered set of decision criteria, and the details of that layering are the central subject of this report.

## The Central Answer in Brief

According to the primary source — the paper's own methods description — **three volunteers** were asked to classify each tweet in the dataset ([document_1.txt](https://arxiv.org/abs/2003.07459)). According to the third-party summary, **five volunteer annotators** classified each tweet ([document_2.txt](document_2.txt)). The two documents are therefore in direct conflict on the headcount.

On the second question — how disagreements were resolved — the two documents are consistent with one another. The protocol operated in three tiers: (1) labels with **100% agreement** were deemed acceptable; (2) in cases of disagreement, labels with **majority agreement above 66%** were selected; and (3) in cases of **complete disagreement** among the annotators, **one of the authors together with two additional human judges** reviewed the tweet in order to reach the required majority above 66% ([document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt)).

## Direct Evidence on the Number of Annotators

### The Primary Source: Three Volunteers

The paper's pre-processing and annotation section states plainly: "A team of three volunteers were asked to classify each tweet in the dataset" ([document_1.txt](https://arxiv.org/abs/2003.07459)). This is a first-party description of the annotation setup, written by the researchers who designed and ran the annotation effort. It describes the annotators as *volunteers*, which indicates that the primary labelling pool was not composed of the paper's authors themselves. The same sentence also specifies the scope of their task: classification of *each tweet* in the dataset, implying full overlap rather than partial or split annotation designs in which different annotators see different subsets.

### The Third-Party Summary: Five Volunteers

The third-party summary states that "a team of five volunteer annotators classified each tweet" ([document_2.txt](document_2.txt)). This summary retains the descriptor "volunteer" and retains the full-overlap design ("each tweet"), but increases the count from three to five. Critically, the summary does not cite a different section of the paper, a different version of the paper, or an external source for the altered figure; it simply restates the procedure with a different number ([document_2.txt](document_2.txt)).

### Table 1: Side-by-Side Comparison of the Two Sources

| Feature | Primary source (`document_1.txt`) | Third-party summary (`document_2.txt`) | Agreement? |
|---|---|---|---|
| Number of base annotators | Three volunteers | Five volunteer annotators | **Conflict** |
| Annotator type | Volunteers | Volunteers | Agree |
| Coverage | Each tweet classified | Each tweet classified | Agree |
| Inter-annotator agreement calculated | Yes | Not explicitly stated, but implied by the agreement rules | Partial |
| Unanimous labels accepted | 100% agreement deemed acceptable | Unanimous agreement accepted | Agree |
| Disagreement threshold | Majority above 66% | Majority above 66% | Agree |
| Escalation trigger | Complete disagreement | Complete disagreement | Agree |
| Escalation panel | One author + two extra human judges | One author + two additional judges | Agree |
| Escalation target | Reach majority above 66% | Reach a majority | Agree |

The table makes the structure of the discrepancy clear: **every element of the adjudication protocol matches across the two documents, and only the base annotator count differs.** This pattern is important for the reliability assessment developed later in this report, because it suggests the discrepancy is an isolated counting error rather than evidence of two genuinely different annotation designs.

## How Disagreements Were Resolved: Reconstructing the Protocol

Both documents describe a tiered resolution scheme. Reconstructing it in order of escalating disagreement produces the following sequence.

### Tier 1: Unanimous Agreement

The first tier accepted labels on which all annotators agreed without exception. The primary source frames this as labels with "100% agreement" being "deemed acceptable" ([document_1.txt](https://arxiv.org/abs/2003.07459)), while the third-party summary describes "unanimous agreement" being "accepted" ([document_2.txt](document_2.txt)). The two formulations are equivalent. The significant point is that unanimity was treated as a *sufficient* condition for acceptance, not as a precondition for any label to enter the dataset; the existence of the later tiers confirms that non-unanimous labels could still be retained.

### Tier 2: Majority Agreement Above 66%

The second tier handled partial disagreement. Where annotators diverged but a candidate label still commanded "majority agreement above 66%," that label "were selected" ([document_1.txt](https://arxiv.org/abs/2003.07459)). The third-party summary describes the same rule as disagreements "resolved by majority above 66%" ([document_2.txt](document_2.txt)). The threshold is therefore strictly *above* 66%, not "at least 66%" and not a simple plurality rule. This distinction matters, as the arithmetic section below demonstrates.

### Tier 3: Complete Disagreement and Author-Led Escalation

The third tier addressed the residual cases in which the annotators did not converge on any label satisfying the majority rule — that is, cases of "complete disagreement between annotators" ([document_1.txt](https://arxiv.org/abs/2003.07459)). Here the procedure changed both in composition and in authority. One of the paper's authors "reviewed the tweets with two extra human judges to reach the desired majority above 66%" ([document_1.txt](https://arxiv.org/abs/2003.07459)). The third-party summary describes the identical escalation: "one author plus two additional judges reviewed the tweet to reach a majority" ([document_2.txt](document_2.txt)).

Two features of this third tier merit emphasis. First, the escalation introduced *new* adjudicators rather than reweighting the existing annotators' judgements; the two human judges are described as "extra," implying they were not part of the original labelling panel ([document_1.txt](https://arxiv.org/abs/2003.07459)). Second, the escalation panel was itself subject to the same quantitative standard — the desired majority "above 66%" — meaning that the author's participation did not grant unilateral authority to impose a label. A three-member escalation panel (one author plus two judges) would require at least two of the three members to concur in order to exceed a 66% threshold.

### Table 2: The Three-Tier Resolution Protocol

| Tier | Condition | Action | Source |
|---|---|---|---|
| 1 | 100% / unanimous agreement | Label accepted as-is | [document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt) |
| 2 | Partial disagreement with majority > 66% | Majority label selected | [document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt) |
| 3 | Complete disagreement | One author plus two extra human judges re-review to reach majority > 66% | [document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt) |

## Arithmetic Implications of the "Above 66%" Threshold

The stated threshold is not merely descriptive; it constrains which panel sizes and vote distributions are logically coherent with the described procedure.

### Under the Three-Annotator Reading

If three annotators labelled each tweet, then the possible agreement shares on a binary decision are 0%, 33.3%, 66.7%, and 100%. Since the rule requires a majority *above* 66%, the 33.3% share fails and the 66.7% share (two of three) passes. The protocol therefore reduces, in practice, to **accepting any label supported by at least two of the three annotators**, with unanimous labels accepted at Tier 1 and two-of-three labels accepted at Tier 2. A "complete disagreement" case at Tier 3 would then be one in which no label reached two votes — a three-way split across three distinct labels, which is possible only if the annotation schema permits more than two categories. This reading is internally coherent: the 66% threshold functions as a precise, if slightly redundant, way of expressing a two-thirds supermajority within a three-person panel ([document_1.txt](https://arxiv.org/abs/2003.07459)).

### Under the Five-Annotator Reading

If five annotators labelled each tweet, the possible agreement shares are 0%, 20%, 40%, 60%, 80%, and 100%. Under a strictly "above 66%" rule, only 80% (four of five) and 100% meet the standard. The 60% share — a three-of-five majority in ordinary usage — **would fail the stated threshold.** This has a striking consequence: under the five-annotator reading, the word "majority" in both documents would be misleading, since three out of five is a numerical majority but would not satisfy the stated rule. Under the three-annotator reading, by contrast, "majority" and "above 66%" coincide exactly at the two-of-three level, because 66.7% is both a numerical majority and above the 66% cutoff.

### Table 3: Vote Shares and Threshold Compliance

| Panel size | Vote distribution | Share | Satisfies "above 66%"? | Note |
|---|---|---|---|---|
| 3 annotators | 3 of 3 | 100% | Yes | Tier 1 (unanimous) |
| 3 annotators | 2 of 3 | 66.7% | Yes | Tier 2; coincides with ordinary majority |
| 3 annotators | 1 of 3 | 33.3% | No | Potential Tier 3 trigger |
| 5 annotators | 5 of 5 | 100% | Yes | Tier 1 (unanimous) |
| 5 annotators | 4 of 5 | 80% | Yes | Tier 2 |
| 5 annotators | 3 of 5 | 60% | **No** | Ordinary majority, but below the stated threshold |
| 5 annotators | 2 of 5 | 40% | No | — |
| 5 annotators | 1 of 5 | 20% | No | — |

The table shows that the three-annotator configuration produces a rule in which "majority" and "above 66%" are mutually consistent, whereas the five-annotator configuration produces a rule in which they are not. This is an internal-consistency argument, not direct documentary proof, but it materially strengthens the case for the primary source's figure.

## Reconciling the Discrepancy

A plausible and parsimonious explanation for the divergence between the two documents can be constructed from the numbers themselves. The primary source describes **three** base annotators and, for escalation cases, **two extra human judges** plus **one author** ([document_1.txt](https://arxiv.org/abs/2003.07459)). The third-party summary appears to have collapsed the original panel and the adjudication panel into a single "team of five volunteer annotators" ([document_2.txt](document_2.txt)).

This reconciliation is arithmetically tidy — three volunteers plus two extra judges equals five — and it explains why the summary retains the escalation language ("one author plus two additional judges") even while asserting a five-person base panel: in that document, the same two judges appear to have been counted twice, once as part of the "five" and once as "additional judges" ([document_2.txt](document_2.txt)). The reconciliation also explains why the summary calls all five "volunteers": the original three are explicitly described as volunteers in the source, and the summarizer may have extended that descriptor to the judges as well ([document_1.txt](https://arxiv.org/abs/2003.07459)).

This explanation should be treated as a hypothesis rather than an established fact. It is, however, more parsimonious than the alternative — that two genuinely different annotation designs were used and reported, with only the base count differing while every other procedural detail matched exactly — because that alternative would require the coincidence of an identical escalation rule, an identical threshold, and an identical labelling scope across two different setups.

## Reliability Assessment of the Two Sources

When two sources conflict, the appropriate response is not to average them or to report both without adjudication, but to weigh them. Three considerations favour the primary source for this particular question.

First, **proximity to the annotation process**. The excerpt in `document_1.txt` is drawn from the paper's own dataset-construction section, written by the researchers who designed the annotation. The excerpt in `document_2.txt` is explicitly identified as a "third-party summary," one step removed from the underlying procedure ([document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt)).

Second, **specificity and internal detail**. The primary source uses precise, non-interchangeable terminology: "three volunteers" for the base panel and "two extra human judges" for the escalation panel, distinguishing the original annotators from the later adjudicators ([document_1.txt](https://arxiv.org/abs/2003.07459)). The third-party summary flattens these roles into a single category of "volunteer annotators," which is exactly the kind of terminological compression that produces counting errors ([document_2.txt](document_2.txt)).

Third, **arithmetic coherence**, as established above: the "above 66%" rule is fully coherent with a three-person panel and internally awkward with a five-person panel ([document_1.txt](https://arxiv.org/abs/2003.07459)).

Recency is a further consideration under the general principle of preferring newer sources. However, in this instance the "newer" document is a derivative summary rather than an updated primary report; a later summary does not supersede an earlier first-party methods description on a question of fact about what was done. The primary source should therefore be preferred, while the discrepancy itself should be disclosed in any downstream use of the dataset.

## Limitations and Residual Uncertainty

Several uncertainties remain and should be stated explicitly.

- The primary source excerpt does not specify whether the three volunteers were the only individuals to see every tweet, nor whether any subset of tweets received additional passes beyond the described tiers.
- The excerpt does not specify the annotation schema in detail, so it is not possible from the provided information to determine exactly how many distinct labels existed and therefore how often a "complete disagreement" three-way split could occur.
- The excerpt does not state whether the author who participated in Tier 3 escalation was also one of the three volunteers, or a separate individual. If separate, up to six distinct individuals may have been involved across the full annotation process: three volunteers, one author, and two extra judges.
- The third-party summary does not state the source of its own annotator count, so its figure cannot be independently traced within the provided materials ([document_2.txt](document_2.txt)).

## Practical Implications for Users of OGTD

Users of the OGTD dataset should report the annotator count based on the primary source — **three volunteer annotators for the base labelling, with escalation to an author-led panel of three adjudicators (one author plus two extra judges) in complete-disagreement cases** — and should be transparent about the conflicting figure in circulation ([document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt)). Two further implications follow.

First, the disagreement rate reported for any given label class in OGTD reflects a two-of-three supermajority standard, not a five-person consensus. Downstream models trained on OGTD inherit whatever label noise survives that standard, and the two-of-three rule is more permissive than a four-of-five rule would be.

Second, the existence of a Tier 3 escalation path means that a small subset of labels rests on a *different* set of adjudicators than the majority of the dataset. Analysts conducting error analysis should therefore be aware that the annotation provenance of OGTD is not homogeneous across instances, even though the acceptance threshold was stated uniformly as "above 66%."

## Conclusion

The evidence supports a clear, if qualified, answer. The primary source for the OGTD dataset states that **three volunteers** classified each tweet, whereas a third-party summary states that **five volunteer annotators** did so ([document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt)). The primary source should be treated as authoritative on this point because it is a first-party methods description, because it distinguishes the base annotator panel from the escalation adjudicators with precise terminology, and because the stated "above 66%" majority rule is arithmetically coherent with a three-person panel while being awkward with a five-person panel. The five-person figure is most plausibly a summarisation error produced by merging the three base annotators with the two extra judges who participated only in escalation cases.

On the second question, both sources agree that disagreements were resolved through a tiered protocol: unanimous labels were accepted directly; labels with agreement above 66% were selected; and complete disagreement triggered re-review by one of the authors together with two additional human judges, who were themselves required to reach a majority above 66% ([document_1.txt](https://arxiv.org/abs/2003.07459); [document_2.txt](document_2.txt)). The annotator count should be reported as three, the threshold as strictly greater than 66%, and the escalation panel as three adjudicators, with the conflicting five-annotator figure noted as a documented discrepancy in the secondary literature.

## References

document_1.txt. (n.d.). *Offensive language identification in Greek* (arXiv:2003.07459) [Excerpt: The OGTD dataset — pre-processing and annotation]. https://arxiv.org/abs/2003.07459

document_2.txt. (n.d.). *Third-party summary: OGTD Greek offensive-language dataset*.