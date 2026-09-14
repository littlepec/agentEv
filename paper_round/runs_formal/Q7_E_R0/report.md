# Annotator Count and Disagreement Resolution in the OGTD Dataset: A Documentary Analysis of the Annotation Protocol

## 1. Introduction

The reliability of any labeled corpus rests on two procedural pillars: how many people produced the labels, and how conflicts between those people were settled. This report examines both pillars for the OGTD dataset, as documented in the paper *Offensive Language Identification in Greek* (arXiv:2003.07459), specifically within the section titled "The OGTD Dataset :: Pre-processing and annotation" ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The query under examination is narrow and factual: how many annotators labeled the OGTD dataset, and how were disagreements among them resolved? The available documentation is short but procedurally dense, describing a layered annotation design with an explicit numeric acceptance threshold and a separate escalation pathway for irreconcilable cases. The analysis below reconstructs that design, quantifies its implications, and identifies the interpretive limits of the source material ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 2. Direct Answer to the Query

The documentation states that **a team of three volunteers** was asked to classify each tweet in the dataset ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). This figure of three constitutes the primary annotation workforce; the source does not describe any larger standing pool of coders.

Disagreement resolution followed a **three-tier rule** rather than a single procedure. First, inter-annotator agreement was calculated, and labels receiving **100% agreement** were deemed acceptable without further review ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Second, where the annotators diverged, labels carrying **majority agreement above 66%** were selected ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Third, where there was **complete disagreement** among the annotators, **one of the authors** reviewed the affected tweets **together with two extra human judges** in order to reach the desired majority above 66% ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

In brief: three volunteer annotators produced the initial labels; 100% agreement was self-validating; a two-thirds-plus majority settled partial disagreements; and total disagreement triggered escalation to a panel consisting of one author plus two additional judges ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 3. The Primary Annotation Layer: Three Volunteers

### 3.1 Composition of the team

The source specifies exactly three individuals and identifies them as "volunteers" ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The volunteer designation is notable because it indicates that the annotation was not performed by a professional, remunerated annotation workforce, although the documentation does not discuss compensation, recruitment channels, formal training, or the annotators' linguistic backgrounds ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). It is also worth noting that the annotators are described collectively rather than individually; no annotator identifiers, demographic attributes, or per-annotator label distributions are reported in the supplied text ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

### 3.2 Scope of the task

Each of the three volunteers was asked to classify **each tweet in the dataset**, implying full-coverage, exhaustive labeling by the same three-person team rather than partial or partitioned annotation ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The unit of annotation was therefore the individual tweet, and the outcome of the process was a label set subsequently filtered through the agreement criteria described below ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

### 3.3 Relationship to the pre-processing stage

The relevant section heading couples "Pre-processing and annotation," indicating that the annotation procedures documented here operate downstream of a pre-processing step applied to the tweets ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The supplied text does not specify what that pre-processing entailed, but the sequencing is relevant to interpreting the annotator count: the three volunteers labeled the post-pre-processing tweet set, not raw data in an unspecified state ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 4. Inter-Annotator Agreement and the 100% Acceptance Rule

The protocol's first filter is the strongest possible: labels on which all annotators concurred unanimously were "deemed acceptable" without any adjudication ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). With three annotators, 100% agreement means a 3-of-3 unanimity. The documentation states that inter-annotator agreement "was calculated," but it does not name the specific agreement statistic used—such as a kappa-family coefficient or alpha—nor does it report a numerical agreement value for the dataset as a whole ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). What the source does make clear is that agreement served a **gatekeeping** function rather than merely a reporting function: it determined which labels were accepted outright and which proceeded to adjudication ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

This design has a direct consequence for the effective annotator count. For unanimous items, exactly three individuals determined the label, with no further human involvement ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). For non-unanimous items, the number of humans contributing to the final label rises, because the adjudication pathway introduces additional judges ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 5. The Majority Threshold: "Above 66%"

The second tier of the protocol applied to labels that were not unanimously agreed. In such cases, "labels with majority agreement above 66% were selected" ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Under a three-annotator scheme, the arithmetic of possible outcomes is limited and can be enumerated precisely, as shown in the table below.

### Table 1. Agreement configurations under three annotators and their disposition

| Annotators agreeing | Proportion | Percentage | Protocol disposition |
|---|---|---|---|
| 3 of 3 | 3/3 | 100% | Accepted outright; no adjudication required |
| 2 of 3 | 2/3 | 66.67% | Majority agreement above 66%; label selected |
| 1 of 3 (no shared label) | 1/3 | 33.33% | Complete disagreement; escalated to author plus two extra judges |

*Note.* Proportions are derived arithmetically from the three-annotator team described in the source ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)); the dispositions correspond to the acceptance, majority, and escalation rules stated in that source ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

Two observations follow from this table. First, the 66% threshold is calibrated to the three-annotator design: 2/3 equals approximately 66.67%, which satisfies a strict "above 66%" requirement, whereas any configuration weaker than 2-of-3 cannot produce a majority at all ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Second, the threshold is described as a floor for **majority agreement**, meaning that the protocol sought to retain labels backed by at least two independent judgments rather than discarding all contested items ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The source does not report how many items fell into each of these three bands, so the relative weight of unanimous versus majority-adjudicated versus escalated labels cannot be determined from the available documentation ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 6. Escalation for Complete Disagreement

### 6.1 Trigger condition

The third tier was reserved for "complete disagreement between annotators," the situation in which the three volunteers shared no common label for a tweet ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). On a three-way labeling task, this corresponds to three distinct labels being assigned to the same item, precluding any internal majority ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

### 6.2 The adjudication panel

For these cases, the resolution procedure was as follows: **one of the authors reviewed the tweets with two extra human judges** in order to reach the desired majority above 66% ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). This introduces three additional participants relative to the primary team: the author-reviewer and the two extra judges. Notably, the author is described in a review capacity, while the two extra judges are characterized as human judges rather than as volunteers, suggesting a distinction in role if not necessarily in status ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The stated objective of this review was not merely to break the tie but to "reach the desired majority above 66%," indicating that the same numeric threshold governing tier two was carried over as the success criterion for tier three ([Offensive Language Identification in Greek, arXiv:2003.07459](https://www.arxiv.org/abs/2003.07459)).

## 7. Consolidated Annotator Counts

Because the protocol is layered, the answer to "how many annotators" depends on which stage of the pipeline is under consideration. Table 2 consolidates the counts that can be derived from the documentation.

### Table 2. Human involvement by protocol stage

| Protocol stage | Participants involved | Role in the final label |
|---|---|---|
| Initial labeling of every tweet | 3 volunteers | Produced all raw labels and the basis for agreement calculation |
| Unanimous items (100%) | 3 volunteers | Label accepted without adjudication |
| Majority items (>66%) | 3 volunteers | Majority label selected |
| Complete disagreement | 1 author + 2 extra human judges | Review to reach majority above 66% |

*Note.* Rows reflect the procedures described in the source ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Arithmetically, up to six distinct individuals are named by the protocol across its stages (three volunteers, two extra judges, one author), though the source does not clarify whether the two extra judges or the author participated in any other stage ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 8. Interpretive Ambiguities and Documented Gaps

A rigorous reading of the source requires distinguishing what it states from what it leaves unspecified. Several gaps bear directly on the query.

1. **Named agreement statistic absent.** The text says agreement "was calculated" but reports no coefficient and no value ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Consequently, the reliability of the labels cannot be independently assessed from the supplied documentation alone.
2. **Composition of the escalation panel relative to the original team.** The source says one author reviewed the tweets "with two extra human judges," but it does not state whether the original three volunteers also re-annotated these items, or whether the escalated decision rested solely on the author-plus-two-judges group ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). If the latter, the number of raters per escalated item would be three (one author, two judges); if the former, it would be six. The documentation does not resolve this.
3. **Identity of the author.** "One of the authors" is not individuated, so it is unknown whether adjudication was always performed by the same person ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).
4. **No per-tier item counts.** The distribution of tweets across the 100%, >66%, and complete-disagreement categories is not reported, so the practical weight of the escalation procedure cannot be quantified ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).
5. **Annotator attributes and training undocumented.** The volunteers' linguistic background, familiarity with offensive-language annotation guidelines, and any calibration or pilot phase are not described ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 9. Assessment and Significance

On the evidence provided, the OGTD annotation design is best characterized as a **three-annotator, threshold-gated protocol with a dedicated escalation tier** ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Its most distinctive features are the use of unanimity as the baseline acceptance criterion, the use of a two-thirds supermajority as the fallback for contested items, and the routing of irreconcilable items to a separate, author-led panel with two additional judges ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). This structure is internally consistent: the 66% figure aligns with the two-of-three configuration that a three-person team can produce, and the escalation tier is designed to regenerate a >66% majority when the primary team cannot supply one ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). The principal limitation is transparency: absent a reported agreement coefficient, per-tier counts, and clarity on panel composition, the protocol's robustness can be described in procedural terms but not empirically verified from the source at hand ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## 10. Conclusion

The OGTD dataset was initially labeled by **three volunteers**, who classified every tweet and whose inter-annotator agreement was calculated and used as a filter ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Disagreements were resolved through a graded procedure: unanimous labels (100% agreement) were accepted directly; non-unanimous labels were retained when they commanded majority agreement above 66%; and tweets marked by complete disagreement were escalated to **one of the authors working with two extra human judges** to reach the same >66% majority threshold ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)). Thus, the minimal annotator count is three, the maximum number of distinct individuals named by the protocol is six, and the operative decision rule throughout is a supermajority of approximately two-thirds, with unanimity serving as the preferred and self-validating outcome ([Offensive Language Identification in Greek, arXiv:2003.07459](https://arxiv.org/abs/2003.07459)).

## References

Offensive language identification in Greek (arXiv:2003.07459) [document_1.txt]. (n.d.). https://arxiv.org/abs/2003.07459