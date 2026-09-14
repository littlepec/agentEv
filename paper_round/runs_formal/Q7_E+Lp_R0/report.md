# Annotator Composition and Disagreement Resolution in the OGTD Dataset: A Source-Critical Report

## Executive Summary

The question of how many annotators labeled the OGTD (Offensive Greek Tweet Dataset) and how their disagreements were resolved admits a clear answer when the available evidence is ranked by reliability. According to the primary source — a paper on offensive language identification in Greek, identified as arXiv:2003.07459 — a team of **three volunteers** classified each tweet in the dataset ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Disagreements were resolved hierarchically: labels receiving 100% agreement were accepted directly; contested labels required a majority above 66%; and tweets on which annotators were in complete disagreement were escalated to one of the authors working alongside two additional human judges until the same 66% majority threshold was met ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). A third-party summary describing the same dataset states that **five** volunteers performed the annotation ([Document 2, n.d.](document_2.txt)). Because the two sources conflict on the personnel count while agreeing on the disagreement-resolution procedure, this report evaluates both accounts, determines which is more credible, and explains why the discrepancy most plausibly arises from a conflation of the initial annotator pool with the supplementary adjudication panel.

## 1. Introduction and Scope

Dataset documentation is not a peripheral matter in computational linguistics. The reliability, reproducibility, and ethical defensibility of any annotated corpus depend on how many people applied the labels, how much they agreed, and what happened when they did not. For offensive-language resources in particular, the annotator pipeline is the mechanism through which subjective judgments about toxicity, offensiveness, and acceptability are converted into the categorical ground truth that downstream classifiers are trained to reproduce ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)).

This report addresses two linked questions about OGTD:

1. **How many annotators labeled the dataset?**
2. **How were disagreements between those annotators resolved?**

The evidence base is deliberately narrow and consists of two documents reproduced in the task materials: a primary extract from the OGTD paper itself, under the section heading "The OGTD Dataset :: Pre-processing and annotation" ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)), and a third-party summary of the OGTD Greek offensive-language dataset ([Document 2, n.d.](document_2.txt)). No other sources are used, and no claims are advanced that cannot be traced to one of these two documents.

## 2. Evidence Base: Description and Reliability Assessment

Before resolving the numerical conflict, it is necessary to characterize the two documents and weigh their evidentiary value. Table 1 summarizes the comparison.

**Table 1.** *Characteristics of the two source documents.*

| Attribute | Document 1 (primary paper extract) | Document 2 (third-party summary) |
|---|---|---|
| Self-described provenance | "Source (paper): Offensive Language Identification in Greek (arXiv:2003.07459)" | "Third-party summary: OGTD Greek offensive-language dataset" |
| Section context | "The OGTD Dataset :: Pre-processing and annotation" | Not specified |
| Annotator count reported | Three volunteers | Five volunteers |
| Agreement acceptance rule | 100% agreement accepted | Unanimous agreement accepted |
| Majority threshold | Above 66% | Above 66% |
| Escalation procedure | One author plus two extra human judges | One author plus two additional judges |
| Nature of text | Methodological description in the authors' own voice | Secondary paraphrase of the primary description |

Two features of this comparison are decisive. First, Document 1 is a direct extract from the research paper that produced the dataset, situated within the very section devoted to pre-processing and annotation — that is, the authors describing their own procedure ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Document 2 explicitly presents itself as a summary, not as an independent investigation ([Document 2, n.d.](document_2.txt)). Under standard principles of source evaluation, a primary methodological account outranks a derivative paraphrase when the two disagree, because the paraphrase introduces an additional layer of transmission in which information may be altered, simplified, or merged.

Second, the two documents are near-identical in every respect except the annotator count and inconsequential stylistic substitutions. Both specify unanimous or 100% agreement as the acceptance criterion; both specify a majority threshold above 66%; both describe escalation to one author plus two additional judges ([Document 1, n.d.](https://arxiv.org/abs/2003.07459); [Document 2, n.d.](document_2.txt)). Given this near-verbatim overlap, the single point of divergence — "three" versus "five" — is most parsimoniously explained as a transmission error in the secondary document rather than as independent testimony about a different annotation configuration.

## 3. The Number of Annotators: Competing Claims and Their Adjudication

### 3.1 The primary-source claim

Document 1 states plainly: "A team of three volunteers were asked to classify each tweet in the dataset" ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). This figure of three is embedded in a coherent procedural narrative: inter-annotator agreement was computed, unanimous labels were accepted, sub-unanimous but two-thirds-majority labels were accepted, and fully contested items were escalated. As shown in Section 4, the arithmetic of the stated 66% threshold coheres exactly with a three-person panel.

### 3.2 The secondary claim

Document 2 asserts that "a team of five volunteer annotators classified each tweet" ([Document 2, n.d.](document_2.txt)). The remainder of that document reproduces the primary procedure without alteration.

### 3.3 Adjudication

Three considerations favor the primary source. First, **proximity to the object of description**: the paper's authors designed and executed the annotation protocol, so their statement about the number of volunteers is first-hand ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Second, **explicit self-identification as secondary**: Document 2 labels itself a "third-party summary," which by definition is derivative ([Document 2, n.d.](document_2.txt)). Third, **internal consistency**, which is examined quantitatively in Section 5.

Accordingly, this report adopts the position that **three volunteers** conducted the initial annotation of every tweet in OGTD, with the caveat that the adjudication stage involved up to three further individuals (one author and two extra judges) on the subset of tweets exhibiting complete disagreement ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)).

## 4. The Disagreement-Resolution Protocol

The procedure described in the primary source is a three-tier escalation ladder applied at the level of individual tweets. Table 2 condenses it.

**Table 2.** *The OGTD disagreement-resolution protocol.*

| Tier | Trigger condition | Resolution mechanism | Threshold applied |
|---|---|---|---|
| 1 | All annotators agree | Label accepted as-is | 100% agreement |
| 2 | Partial disagreement | Majority label selected | Majority above 66% |
| 3 | Complete disagreement among annotators | Review by one author plus two additional human judges | Majority above 66% |

### 4.1 Tier 1: Unanimous agreement

The first filter is unanimity. Inter-annotator agreement was calculated, and "labels with 100% agreement were deemed acceptable" ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)); the third-party summary renders this equivalently as "unanimous agreement" ([Document 2, n.d.](document_2.txt)). No further review was required for these items.

### 4.2 Tier 2: Qualified majority above 66%

Where annotators diverged but a clear majority emerged, "labels with majority agreement above 66% were selected" ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). The threshold is expressed as strictly *above* 66%, not "at least 66%" — a detail that matters for the arithmetic discussed below. The secondary summary preserves this figure exactly ([Document 2, n.d.](document_2.txt)), which strengthens confidence that the threshold itself is accurately reported in both documents.

### 4.3 Tier 3: Complete disagreement and escalation

The final tier addresses the hardest cases. "For labels with complete disagreement between annotators, one of the authors reviewed the tweets with two extra human judges to reach the desired majority above 66%" ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). The same escalation is reported in the summary, described as "one author plus two additional judges" ([Document 2, n.d.](document_2.txt)). Two features of this tier deserve emphasis. First, the escalation panel is described as *supplementary* — the author and two judges are brought in to adjudicate contested items, not to annotate the corpus as a whole. Second, the escalation panel itself numbers three, and it is required to achieve the same 66% majority, implying an odd-numbered voting body capable of producing a strict majority.

## 5. Internal Consistency Check: Threshold Arithmetic

The reported 66% majority rule can be tested against the reported panel sizes. Table 3 sets out the possible label distributions.

**Table 3.** *Attainable agreement proportions by panel size.*

| Panel size | Distribution | Agreement share | Meets "above 66%"? |
|---|---|---|---|
| 3 annotators | 3–0 | 100% | Yes (Tier 1) |
| 3 annotators | 2–1 | 66.67% | Yes (Tier 2) |
| 3 annotators | 1–1–1 | 33.33% each | No (Tier 3 escalation) |
| 5 annotators | 5–0 | 100% | Yes (Tier 1) |
| 5 annotators | 4–1 | 80% | Yes (Tier 2) |
| 5 annotators | 3–2 | 60% | No — would require escalation |
| 5 annotators | 2–2–1 | 40% | No — would require escalation |

The three-annotator configuration maps exactly onto the three described tiers: unanimity, a two-thirds majority that clears the 66% bar (66.67% > 66%), and a three-way split that constitutes "complete disagreement." The five-annotator configuration, by contrast, creates an unexplained gap: a 3–2 split yields only 60%, which falls *below* the stated threshold and would therefore have to be escalated, yet the protocol as described anticipates escalation only for "complete disagreement," not for ordinary plurality outcomes ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). The three-annotator reading is thus the only one under which the stated threshold partitions outcomes cleanly into the tiers the sources describe. This arithmetic reinforces the conclusion reached in Section 3 on documentary grounds.

## 6. Plausible Origin of the Discrepancy

The most economical explanation for the divergence is arithmetic conflation. The primary source describes three volunteers for initial annotation and, separately, "two extra human judges" engaged for adjudication ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Three plus two equals five. A secondary summarizer working from the paper could readily merge these two distinct groups — the standing annotation team and the ad hoc adjudication panel — into a single figure of five "volunteer annotators" ([Document 2, n.d.](document_2.txt)). This hypothesis is consistent with the fact that Document 2 reproduces every other procedural detail faithfully, including the 66% threshold and the involvement of an author plus two judges, and diverges only where such a merge would occur. It should be treated as an inference rather than a documented fact, since neither source states it explicitly.

It is worth noting that neither reading contradicts the other on the *total* number of individuals who ever touched the data. Under the primary account, up to six people could interact with a given contested tweet: three volunteers, one author, and two judges. Under the secondary account, five volunteers plus an author and two additional judges would imply eight. The divergence, therefore, is about the size of the *standing* annotation team, not about the existence of an adjudication panel.

## 7. Methodological and Practical Implications

Three implications follow for researchers who reuse OGTD.

**Auditability.** Because the escalation tier names an author as a participant, the adjudication of the most contested tweets is not fully independent of the dataset's creators ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). This is a common and defensible design, but it means that the final labels for the hardest cases reflect author-mediated consensus rather than purely crowd-sourced agreement.

**Threshold sensitivity.** With a three-person panel, the "above 66%" rule is effectively a rule that two of three annotators must concur; there is no intermediate zone between unanimity and a two-thirds majority ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Users should therefore understand Tier 2 labels as resting on a 2-of-3 majority, not on a broad consensus.

**Documentation hygiene.** The conflict between the two documents illustrates the cost of relying on secondary summaries for methodological details. Any downstream publication citing OGTD should cite the annotator count from the primary paper rather than from the summary ([Document 1, n.d.](https://arxiv.org/abs/2003.07459); [Document 2, n.d.](document_2.txt)).

## 8. Limitations

This report rests on two short extracts. Neither provides the full annotation guidelines, the number of label categories, the per-class agreement statistics, or the count of tweets escalated to Tier 3. The reconciliation offered in Section 6 is an interpretation, not a documented claim. The reliability ranking in Section 2 is based on the provenance labels embedded in the documents themselves — a primary paper extract versus a self-described third-party summary — rather than on independent verification of the underlying publication.

## 9. Conclusion

On the balance of the available evidence, the OGTD dataset was labeled by **three volunteer annotators**, as reported in the primary paper's "Pre-processing and annotation" section ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). The claim of five annotators appears only in a third-party summary and is best explained as a conflation of the three standing annotators with the two supplementary judges used for adjudication ([Document 2, n.d.](document_2.txt)). Disagreements were resolved through a three-tier escalation ladder: unanimous labels were accepted immediately; labels with a majority above 66% were accepted; and tweets marked by complete disagreement were referred to one of the authors together with two additional human judges, who were themselves required to reach the same majority above 66% ([Document 1, n.d.](https://arxiv.org/abs/2003.07459)). Both sources agree on this procedural architecture, and the arithmetic of the 66% threshold is internally consistent only with an odd-numbered, three-person initial panel — the same panel size reported by the dataset's own authors.

## References

Document 1. (n.d.). *Offensive language identification in Greek* (arXiv:2003.07459) [Primary paper extract: The OGTD Dataset :: Pre-processing and annotation]. https://arxiv.org/abs/2003.07459

Document 2. (n.d.). *Third-party summary: OGTD Greek offensive-language dataset* [Summary document]. Retrieved September 14, 2026, from document_2.txt