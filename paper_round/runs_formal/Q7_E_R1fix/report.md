# Annotation Workforce and Disagreement Resolution in the OGTD Dataset

## Introduction

The OGTD dataset, introduced in the paper *Offensive Language Identification in Greek* (arXiv:2003.07459), provides explicit documentation of its annotation procedure. The central question addressed in this report is twofold: how many annotators labeled the OGTD dataset, and how were disagreements between those annotators resolved? The available documentation states that “a team of three volunteers were asked to classify each tweet in the dataset” ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). It further explains that inter-annotator agreement was calculated, that labels with 100% agreement were deemed acceptable, and that labels with majority agreement above 66% were selected when disagreement occurred ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). For cases of complete disagreement, “one of the authors reviewed the tweets with two extra human judges to reach the desired majority above 66%” ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)).

The most precise answer is therefore layered rather than singular. The primary annotation of every tweet was performed by three volunteers. Complete disagreements, however, were escalated to a separate three-person adjudication panel consisting of one author and two extra human judges. Consequently, the base number of annotators is three, while the maximum number of distinct individuals potentially involved in labeling decisions across the dataset is up to six. This distinction is essential for accurate methodological reporting because it separates full-coverage annotation work from conflict-resolution adjudication.

## Initial Annotation Workforce

### Three Volunteers as Primary Annotators

The documentation explicitly identifies a team of three volunteers who were asked to classify each tweet in the dataset ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). This means that every tweet in the OGTD dataset received three independent initial labels. The use of three annotators is methodologically significant because it enables the calculation of inter-annotator agreement and provides a basis for majority voting ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The text does not indicate that these volunteers were paid experts, nor does it state that they received specialized training; they are described simply as volunteers ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The documentation also does not specify their demographic characteristics, language background, or prior experience with offensive language annotation ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)).

### Implications of a Three-Person Initial Panel

With three initial annotators, the possible agreement outcomes include unanimous agreement at 100%, majority agreement at approximately 66.7% when two of three annotators agree, and lack of majority when the three annotators split in ways that do not produce a two-person coalition ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The documentation’s thresholds align closely with this structure. Labels with 100% agreement were accepted directly, and labels with majority agreement above 66% were selected ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The “above 66%” threshold is important because two out of three is approximately 66.7%, which satisfies the criterion. In practical terms, a label chosen by two of the three volunteers would meet the majority standard.

### Table 1: Initial Annotation and Decision Stages

| Stage | Personnel | Number of people | Scope | Decision rule | Consequence |
|---|---|---|---|---|---|
| Initial annotation | Volunteers | 3 | Each tweet | Independent classification | Produces three labels per tweet ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Agreement check | Not applicable | Not applicable | All tweets | 100% agreement | Label accepted directly ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Majority selection | Not applicable | Not applicable | Tweets with disagreement | Majority above 66% | Label selected ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Complete-disagreement adjudication | One author plus extra human judges | 1 + 2 = 3 | Complete-disagreement cases | Majority above 66% | Final label reached ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |

## Disagreement Resolution Procedure

### Step 1: Inter-Annotator Agreement Calculation

The first quality-control step was the calculation of inter-annotator agreement ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The documentation does not report which specific agreement metric was used, such as percentage agreement, Cohen’s kappa, or Fleiss’ kappa, nor does it report the numerical agreement score for the dataset ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). What is clear is that labels with 100% agreement were deemed acceptable ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). This is a conservative rule because it requires all three volunteers to assign the same label before a tweet is automatically accepted without further review.

### Step 2: Majority Agreement Above 66%

When disagreement occurred but a majority above 66% existed, the majority label was selected ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). In a three-annotator configuration, this means that two of the three volunteers agreed on the same label. The third volunteer’s differing label did not prevent the majority label from being accepted. This stage balances efficiency and reliability: the dataset does not discard all non-unanimous cases, but it does require a supermajority before accepting a label without escalation ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)).

### Step 3: Complete Disagreement and Escalation

The most complex cases were those involving “complete disagreement between annotators” ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). For these labels, one of the authors reviewed the tweets with two extra human judges to reach the desired majority above 66% ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). This created a three-person adjudication panel: one author and two additional human judges. The author did not resolve the disagreement alone; instead, the author participated in a three-person group whose final decision required a majority above 66%. Again, in a three-person panel, this implies that at least two of the three adjudicators had to agree on the final label.

### Table 2: Agreement Levels and Resolution Paths

| Agreement level | Approximate percentage | Resolution path | Final label source |
|---|---|---|---|
| Unanimous agreement | 100% | Accepted directly | Original volunteer labels ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Majority agreement | Above 66%, such as 2/3 ≈ 66.7% | Majority label selected | Original volunteer labels ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Complete disagreement | No majority above 66% | Author plus two extra human judges | Adjudication panel ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |

## How Many Annotators Labeled OGTD?

### The Base Count: Three Primary Annotators

The clearest numerical answer is that three volunteers served as the primary annotators for the OGTD dataset ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). They were asked to classify each tweet, and their labels formed the basis for inter-annotator agreement calculations ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). These three volunteers are annotators in the conventional sense: they independently assigned labels to the full dataset. Therefore, if the question asks for the number of annotators who labeled the complete OGTD dataset from the outset, the answer is three.

### The Expanded Count: Up to Six People Involved in Labeling Decisions

The documentation also states that for complete disagreements, one author and two extra human judges reviewed the tweets ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). If these three individuals were distinct from the original three volunteers, then up to six people may have contributed to labeling decisions across the dataset: three primary volunteers plus three adjudicators. The phrase “two extra human judges” strongly implies that those judges were additional to the initial annotation team ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). However, the documentation does not explicitly state whether the author had also served as one of the original volunteers or whether the extra judges were entirely new to the project. Therefore, the expanded count is best described as “up to six,” not an absolute six.

### Table 3: Interpretations of the Annotator Count

| Interpretation | Number | Scope and rationale |
|---|---|---|
| Primary annotators | 3 | Three volunteers classified each tweet ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Adjudication panel | 3 | One author and two extra human judges handled complete disagreements ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Maximum distinct individuals involved | Up to 6 | If adjudicators were distinct from the original volunteers ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Minimum base annotation team | 3 | The full dataset was initially labeled by three volunteers ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |

### Why the Distinction Matters

In dataset documentation, “annotator count” can refer either to the number of people who independently labeled the full dataset or to the total number of people involved in producing final labels. The OGTD documentation supports both readings depending on the definition used ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). For reproducibility, the most precise statement is that three volunteers performed the primary annotation of all tweets, and one author plus two extra human judges adjudicated complete-disagreement cases. This avoids overstating the number of full-coverage annotators while acknowledging the additional labor involved in conflict resolution.

## Evaluation of the Disagreement Resolution Design

### Strengths of the Procedure

The OGTD procedure has several notable strengths. First, it uses a three-stage consensus model: unanimity, majority, and escalation ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). This prevents both excessive conservatism and uncontrolled disagreement. Second, the use of a separate adjudication panel for complete disagreements introduces a check on irreconcilable cases ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). Third, the majority threshold above 66% ensures that final labels have at least two supporters among three judges in both the initial and escalated stages ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). Fourth, the procedure is transparent enough to be summarized and replicated in principle, although some operational details are missing.

### Limitations and Unresolved Questions

Several important details are not specified in the available documentation. The text does not define “complete disagreement” with a numerical formula; it could mean that all three annotators chose different labels, or it could mean that no label reached the required majority ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The documentation also does not report how many tweets required adjudication, what the final agreement rate was after adjudication, or whether the extra human judges were trained or blind to the original labels ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). In addition, it does not state whether the same author and same two extra judges handled all complete-disagreement cases or whether different panels were used ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). These omissions limit a full assessment of reliability, but they do not undermine the basic answer to the query.

### Implications for Dataset Reliability

The use of three primary annotators plus a separate adjudication panel suggests that the OGTD dataset prioritizes reliable labels over simple annotation speed. The 100% agreement criterion for automatic acceptance is strict, while the above-66% majority criterion allows some disagreement to remain without escalation ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). The escalation stage is particularly important because complete disagreement would otherwise leave no defensible majority label. By involving one author and two extra human judges, the procedure aims to produce a final label with at least two out of three votes ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). This is a reasonable approach to resolving hard cases, although the involvement of an author could introduce bias if the author had strong expectations about the correct label. The two extra judges help mitigate that risk, but the documentation does not describe any blinding procedure ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)).

### Comparison of Resolution Stages

The following table compares the decision rules and the level of consensus required at each stage.

| Resolution stage | Required agreement | Who decides? | Applied to |
|---|---|---|---|
| Automatic acceptance | 100% | Three volunteers | All tweets with unanimous labels ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Majority selection | Above 66% | Three volunteers | Disagreed tweets with a supermajority ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |
| Adjudication | Above 66% | One author plus two extra human judges | Complete-disagreement tweets ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)) |

## Conclusion and Direct Answer

The OGTD dataset was primarily labeled by three volunteers, who classified each tweet and whose labels were used to calculate inter-annotator agreement ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). Disagreements were resolved in a tiered manner. Labels with 100% agreement were accepted directly. Labels with majority agreement above 66% were selected. Labels with complete disagreement were escalated to a panel consisting of one author and two extra human judges, who worked to reach the same majority threshold above 66% ([Offensive Language Identification in Greek, n.d.](https://arxiv.org/abs/2003.07459)). Therefore, the base number of annotators is three. If one counts all individuals who may have contributed to final labeling decisions, the number can be as high as six: three volunteers plus one author and two extra human judges. The documentation does not clarify whether the adjudicators were entirely distinct from the original volunteers, so “up to six” is the most defensible expanded estimate. The procedure reflects a deliberate, majority-driven quality-control design with an escalation mechanism for irreconcilable cases.

## References

Offensive Language Identification in Greek (arXiv:2003.07459). (n.d.). *The OGTD dataset: Pre-processing and annotation* [Document_1.txt]. arXiv. https://arxiv.org/abs/2003.07459