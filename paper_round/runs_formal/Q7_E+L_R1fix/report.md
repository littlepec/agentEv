# Annotation and Disagreement Resolution in the OGTD Greek Offensive-Language Dataset

## Query and Central Finding

The query asks how many annotators labeled the OGTD dataset and how disagreements were resolved. According to the primary source, a team of three volunteers was asked to classify each tweet in the dataset, and inter-annotator agreement was calculated ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Disagreements were not left unresolved: labels with 100% agreement were deemed acceptable, labels with majority agreement above 66% were selected, and cases of complete disagreement were reviewed by one author together with two extra human judges to reach the required majority above 66% ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary provides the same account, stating that three volunteer annotators classified each tweet, unanimous labels were accepted, disagreements were resolved by a majority above 66%, and full disagreement triggered review by one author plus two additional judges ([document_2.txt, n.d.](document_2.txt)). The most defensible answer is therefore that three volunteer annotators initially labeled the OGTD dataset, and that disagreement resolution followed a tiered majority-rule procedure, with a separate three-person panel—one author and two extra human judges—handling complete disagreement.

## Initial Annotation Workforce

### Number of Initial Annotators

The initial labeling team consisted of three volunteers. The primary source states explicitly that “a team of three volunteers were asked to classify each tweet in the dataset” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary corroborates this figure, noting that “a team of three volunteer annotators classified each tweet” ([document_2.txt, n.d.](document_2.txt)). This means the core annotation design was not a single-annotator effort, nor a large crowd-sourced effort, but a small controlled panel of three human coders.

### Scope of the Annotation Task

The unit of annotation was the tweet, and each tweet was classified by the three volunteers ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The sources do not describe subsetting by topic, language variety, or tweet length; the stated scope is “each tweet in the dataset” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Because all three volunteers classified the same items, the dataset has three independent labels per tweet at the initial stage. That design makes it possible to calculate inter-annotator agreement, which the primary source says was done ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Volunteers Versus Authors and Extra Judges

The three initial annotators are described as volunteers, not as the paper’s authors ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The sources distinguish the volunteers from the later adjudication step, where “one of the authors reviewed the tweets with two extra human judges” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The word “extra” implies that the two human judges were additional to the original three volunteers, and the author is identified separately from the volunteer team ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Thus, the initial labeling count is clearly three, while the complete-disagreement resolution stage involved a separate panel of three people: one author plus two extra judges ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

## Disagreement Resolution Procedure

### Unanimous Labels: 100% Agreement

The first decision rule concerned unanimous labels. The primary source states that “labels with 100% agreement were deemed acceptable” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary describes the same rule as “labels with unanimous agreement were accepted” ([document_2.txt, n.d.](document_2.txt)). Because there were three initial annotators, 100% agreement means all three volunteers assigned the same label to a tweet. Such items required no further adjudication and were accepted directly into the dataset ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Majority Labels: Above 66% Agreement

The second rule addressed non-unanimous but still majority-supported labels. In cases of disagreement, “labels with majority agreement above 66% were selected” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary restates this as “disagreements were resolved by majority above 66%” ([document_2.txt, n.d.](document_2.txt)). Operationally, with three annotators, a 2–1 split produces agreement of 66.67%, which is above 66%. A 3–0 split produces 100% agreement, which is also above 66% but was already covered by the unanimity rule. Therefore, the majority rule effectively accepted any label supported by at least two of the three volunteers ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The threshold was not a simple 50% majority; it was a supermajority threshold above two-thirds-equivalent agreement, which is a stricter acceptance criterion ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Complete Disagreement: Author Plus Two Extra Judges

The third rule addressed complete disagreement among the initial three annotators. The primary source states that “for labels with complete disagreement between annotators, one of the authors reviewed the tweets with two extra human judges to reach the desired majority above 66%” ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary again matches this account: “When all three fully disagreed, one author plus two additional judges reviewed the tweet to reach a majority” ([document_2.txt, n.d.](document_2.txt)). Complete disagreement means a 1–1–1 distribution across the three initial annotators: each volunteer chose a different label, so no label had majority support. In such cases, the original three-way vote could not satisfy the above-66% rule. The resolution was a new review by a three-person panel consisting of one author and two extra human judges ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). That panel then sought to reach the desired majority above 66%, meaning at least two of its three members had to agree on a label ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Summary of Decision Rules

The following table summarizes the annotation and resolution structure as described in the two sources.

| Stage | People Involved | Count | Decision Rule | Source |
|---|---|---|---|---|
| Initial labeling | Volunteers | 3 | Each tweet classified by three volunteers | ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)); ([document_2.txt, n.d.](document_2.txt)) |
| Unanimous acceptance | Same three volunteers | 3 | 100% agreement deemed acceptable | ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)); ([document_2.txt, n.d.](document_2.txt)) |
| Majority resolution | Same three volunteers | 3 | Majority agreement above 66% selected | ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)); ([document_2.txt, n.d.](document_2.txt)) |
| Complete-disagreement adjudication | One author plus two extra human judges | 3 | Review to reach desired majority above 66% | ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)); ([document_2.txt, n.d.](document_2.txt)) |
| Possible distinct individuals for a fully disputed item | Initial volunteers plus adjudication panel | Up to 6, if no overlap | No overlap explicitly stated | ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)) |

The table makes clear that the initial annotation count is three, while the complete-disagreement resolution stage introduces up to three additional people. The sources do not state whether the author or the two extra judges had previously served as volunteers, so the maximum number of distinct individuals involved in a fully disputed item could be six, but the minimum core annotation team remains three ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

## Mathematical and Operational Interpretation

### Why the 66% Threshold Matters

With three initial annotators, the possible agreement outcomes are limited. A 3–0 vote gives a label 100% support, a 2–1 vote gives the majority label 66.67% support, and a 1–1–1 vote gives each label 33.33% support with no majority ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The source’s “above 66%” threshold therefore has a precise practical effect: it accepts 2–1 outcomes and rejects 1–1–1 outcomes ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). This is equivalent to requiring at least two of the three initial volunteers to agree. The threshold is slightly above the exact two-thirds value of 66.67% would be if expressed as 66%; however, 66.67% is above 66%, so a 2–1 split qualifies ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Why Complete Disagreement Requires Escalation

Complete disagreement is the only initial outcome that cannot produce a label with above 66% support. In a 1–1–1 split, each label receives only 33.33% support, and the largest single-label share is far below the threshold ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The dataset construction procedure therefore escalates these items to a new panel rather than discarding them or assigning a label arbitrarily ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The panel consists of one author and two extra human judges, and it attempts to produce a majority above 66% ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). This design preserves the dataset’s coverage while maintaining a consistent supermajority standard for final labels.

### Effect on Final Label Quality

The procedure creates two paths to a final label: direct acceptance through unanimity or initial majority, and escalation through a separate adjudication panel for complete disagreement ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). This means the final OGTD labels are not simply the raw majority vote of three volunteers; for the hardest cases, they are the product of a second, expert-inclusive review ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary reinforces this two-path account but does not add further details about the panel’s composition or training ([document_2.txt, n.d.](document_2.txt)). From a methodological standpoint, the escalation step is a conflict-resolution mechanism intended to prevent unresolved complete disagreements from remaining in the dataset.

## Source Reliability and Convergence

### Primary Source Strength

The primary source is the paper “Offensive Language Identification in Greek” (arXiv:2003.07459), which describes the OGTD dataset’s pre-processing and annotation section directly ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Because it is the originating paper, it is the more authoritative account of how many annotators were used and how disagreements were resolved. It provides the precise wording that three volunteers classified each tweet, that 100% agreement was acceptable, that above-66% majority labels were selected, and that complete disagreement was escalated to one author and two extra judges ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)).

### Third-Party Summary as Corroboration

The third-party summary describes the same OGTD Greek offensive-language dataset and repeats the core facts: three volunteer annotators, unanimous agreement accepted, majority above 66% for disagreements, and one author plus two additional judges for complete disagreement ([document_2.txt, n.d.](document_2.txt)). This convergence increases confidence in the answer because two independent descriptions agree on the annotator count and the resolution rules. The third-party summary is less detailed and uses slightly different wording, such as “unanimous agreement” instead of “100% agreement,” but it does not contradict the primary source ([document_2.txt, n.d.](document_2.txt)).

### No Contradictory Evidence in the Provided Sources

Neither provided source states a different number of initial annotators, and neither proposes a different disagreement-resolution mechanism ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)); ([document_2.txt, n.d.](document_2.txt)). There is therefore no internal conflict in the evidence base. The only ambiguity concerns whether the author and extra judges overlapped with the original volunteers, which the sources do not specify ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). That ambiguity affects the total number of unique individuals involved but not the answer to how many annotators initially labeled the dataset or how disagreements were resolved.

## Limitations and Unstated Details

Several details remain unspecified in the provided information. First, the exact identity of the three volunteers is not given, nor are their demographic or linguistic backgrounds reported ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Second, the sources do not state whether the two extra human judges in the complete-disagreement stage were new annotators or had prior involvement with the dataset ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Third, the specific inter-annotator agreement statistic is not named; the primary source says agreement was calculated, but it does not report a coefficient such as Fleiss’ kappa or Krippendorff’s alpha in the provided excerpt ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Fourth, the sources do not state how many tweets fell into each category—unanimous, majority, or complete disagreement—so the practical frequency of the escalation procedure is unknown ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Fifth, the sources do not state what happened if the author-plus-two-judges panel also failed to reach above 66% agreement, although the stated goal was to reach that majority ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). These limitations do not undermine the central answer, but they do qualify the level of procedural detail available.

## Conclusion

The OGTD dataset was initially labeled by three volunteer annotators, each of whom classified each tweet ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Disagreements were resolved through a tiered majority procedure. Labels with 100% agreement were accepted directly ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). Labels with majority agreement above 66% were selected, which with three annotators means a 2–1 agreement was sufficient ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). When all three annotators completely disagreed, one author plus two extra human judges reviewed the tweets to reach the required majority above 66% ([document_1.txt, n.d.](https://arxiv.org/abs/2003.07459)). The third-party summary confirms this account ([document_2.txt, n.d.](document_2.txt)). Therefore, the direct answer is: three initial volunteer annotators, with complete disagreements resolved by a three-person escalation panel consisting of one author and two additional judges.

## References

document_1.txt. (n.d.). *Offensive Language Identification in Greek* (arXiv:2003.07459). https://arxiv.org/abs/2003.07459

document_2.txt. (n.d.). *Third-party summary: OGTD Greek offensive-language dataset*. document_2.txt