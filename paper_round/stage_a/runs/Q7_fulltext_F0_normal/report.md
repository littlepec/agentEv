# How Many Annotators Labeled the OGTD Dataset, and How Were Disagreements Resolved?

## Introduction

The Offensive Greek Tweet Dataset (OGTD) is a Greek-language resource for offensive-language detection, released in two successive versions (v1.0 and v2.0) and designed to be interoperable with the English Offensive Language Identification Dataset (OLID) and with comparable Danish and Turkish resources annotated under the same guidelines ([Document 1, n.d.](document_1.txt)). Because the scientific value of any human-annotated corpus depends directly on the reliability of its labels, the composition of the annotator pool and the procedure used to adjudicate disagreement are central methodological questions. The source documentation for OGTD addresses both questions explicitly for the first version of the dataset and more loosely for the second. This report reconstructs the annotation workforce and the disagreement-resolution protocol from the available documentation, quantifies the consequences of that protocol on the released label distributions, and identifies the gaps in the reporting that a careful reader should note.

## What the OGTD Corpus Contains

OGTD v1.0 was collected between May and June 2019 using the Twitter API, targeting popular and trending hashtags in Greece, including hashtags attached to television series, reality and entertainment shows, and political discussion surrounding the municipal, regional and European Parliament elections of that period ([Document 1, n.d.](document_1.txt)). The collection strategy rested on the intuition that Twitter functions as a venue for complaints and profane commentary on widely viewed television and politics ([Document 1, n.d.](document_1.txt)).

Pre-processing followed the methodology of OLID, with URLs, emojis and emoticons removed and usernames and user mentions normalised to the placeholder `@USER`, and with duplicate punctuation (question and exclamation marks) condensed ([Document 1, n.d.](document_1.txt)). From an initial 49,154 collected tweets, duplicate removal left 46,218 tweets, from which 5,000 were randomly sampled for annotation ([Document 1, n.d.](document_1.txt)). Annotation was carried out in LightTag, chosen for its simple interface and unlimited annotations ([Document 1, n.d.](document_1.txt)). A further pre-processing step specific to Greek — lower-casing and normalising fully accented, partially accented and non-accented words to a non-accented equivalent — is described in the methods section as a prerequisite for experimentation ([Document 1, n.d.](document_1.txt)).

OGTD v2.0 extended this resource. New posts were collected in November 2019 using the same approach as v1.0, supplemented by trending hashtags, shows and topics current in Greece at the time and by additional search keywords, including pejorative terms ([Document 1, n.d.](document_1.txt)). From this second collection, 5,508 tweets were randomly sampled for annotation, and OGTD v2.0 combines the existing v1.0 instances with these newly annotated tweets to yield 10,287 instances in total ([Document 1, n.d.](document_1.txt)). This arithmetic is internally consistent: 4,779 (v1.0) + 5,508 (new) = 10,287 (v2.0) ([Document 1, n.d.](document_1.txt)).

## Annotator Composition

### OGTD v1.0: Three Volunteers

The documentation is explicit on the size of the annotation team for the first version. "Based on explicit annotation guidelines written in Greek and our proposal of the definition of offensive language, a team of three volunteers were asked to classify each tweet found in the dataset with one of the following tags: *Offensive*, *Not Offensive* and *Spam*" ([Document 1, n.d.](document_1.txt)). The figure of three annotators is thus the single most concrete answer available to the question of how many people labelled OGTD: **three volunteer annotators per tweet**, with three possible labels, one of which (*Spam*) existed exclusively to filter spam out of the dataset ([Document 1, n.d.](document_1.txt)).

### OGTD v2.0: A Volunteer Team of Unstated Size

For the second version, the documentation states that the 5,508 newly sampled tweets were "annotated by a team of volunteers" and that "the annotation guidelines were the same ones we used for v1.0" ([Document 1, n.d.](document_1.txt)). The exact number of annotators for this second batch is not reported. Given that the guidelines were inherited unchanged and that the disagreement-resolution mechanism described in the paper presupposes a three-person panel (as argued in the section below), the most defensible inference is that the same three-volunteer configuration applied, but the source does not confirm this explicitly. This is a reporting gap rather than a substantive finding, and it should be flagged as such by anyone reusing the corpus.

### The Adjudication Panel

Separately from the routine annotator pool, the documentation describes an escalation panel used only in the extreme case of complete disagreement: "one of the authors of this paper reviewed the tweets with two extra human judges, to get the desired majority agreement above 66%" ([Document 1, n.d.](document_1.txt)). This means that at the top tier of adjudication, up to five individuals could in principle have influenced a given label: the three original volunteers plus one author and two additional judges. The two "extra human judges" are distinct from the original three volunteers and, in combination with the author, form a three-person adjudication panel ([Document 1, n.d.](document_1.txt)).

| Role | Count | Scope | Source |
|---|---|---|---|
| Volunteer annotators, OGTD v1.0 | 3 | All 5,000 sampled tweets | ([Document 1, n.d.](document_1.txt)) |
| Volunteer annotators, OGTD v2.0 (new batch) | Not stated ("a team of volunteers") | 5,508 newly sampled tweets | ([Document 1, n.d.](document_1.txt)) |
| Author-adjudicator | 1 | Tweets with complete disagreement only | ([Document 1, n.d.](document_1.txt)) |
| Extra human judges | 2 | Tweets with complete disagreement only | ([Document 1, n.d.](document_1.txt)) |

## The Annotation Procedure

Annotation was grounded in "explicit annotation guidelines written in Greek" and in the authors' own proposal for a definition of offensive language ([Document 1, n.d.](document_1.txt)). The label set comprised three tags — *Offensive*, *Not Offensive* and *Spam* — with the third introduced specifically to purge spam from the dataset before release ([Document 1, n.d.](document_1.txt)). Because the released tables report only *Offensive* and *Not Offensive*, the *Spam* category functions as a filtering device rather than as a published target class ([Document 1, n.d.](document_1.txt)).

Inter-annotator agreement was calculated after annotation, and reliability was "statistically measured by Cohen's kappa coefficient", presented in a confusion matrix over each annotator pair ([Document 1, n.d.](document_1.txt)). Reporting pairwise Cohen's kappa is consistent with a three-annotator design: with three annotators there are exactly three unique pairs to evaluate ([Document 1, n.d.](document_1.txt)).

## How Disagreements Were Resolved

The documentation describes a three-tier decision rule, applied in sequence, which converts multiple independent judgements into a single gold label.

### Tier 1: Unanimity as the Default

"Inter-annotator agreement was subsequently calculated and labels with 100% agreement were deemed acceptable annotations" ([Document 1, n.d.](document_1.txt)). In other words, full concordance among the annotators was treated as the primary criterion for acceptance, and the authors did not subject unanimous items to further scrutiny.

### Tier 2: Qualified Majority Above 66%

"In cases of disagreement, labels with majority agreement above 66% were selected as the actual annotations of the tweets in question" ([Document 1, n.d.](document_1.txt)). With three annotators, a threshold of "above 66%" is operationally equivalent to requiring at least two of three annotators to agree, since 2/3 = 66.67%. The choice of 66% rather than 51% is significant: a simple majority would allow a label to win with two votes against one, whereas the stated threshold is described as "above 66%" — a value that maps cleanly onto a two-of-three supermajority. Notably, the documentation does not describe a separate 50%–66% band, which suggests that any disagreement falling short of the threshold was escalated rather than resolved by plurality.

### Tier 3: Escalation to an Author plus Two Extra Judges

"For labels with complete disagreement between annotators, one of the authors of this paper reviewed the tweets with two extra human judges, to get the desired majority agreement above 66%" ([Document 1, n.d.](document_1.txt)). "Complete disagreement" is the situation in which no label achieves the required two-of-three majority. With three annotators each selecting a different one of the three available tags, no label can reach the threshold, and the item is therefore routed to the escalation panel. The panel of three (author plus two judges) then re-adjudicates the item to restore a majority above 66% ([Document 1, n.d.](document_1.txt)).

| Tier | Trigger condition | Decision rule | Decision-makers |
|---|---|---|---|
| 1 | 100% agreement among annotators | Label accepted as-is | 3 volunteer annotators |
| 2 | Disagreement, but majority above 66% | Majority label selected as gold | 3 volunteer annotators |
| 3 | Complete disagreement (no label above 66%) | Re-review to achieve majority above 66% | 1 author + 2 extra human judges |

All three tiers are documented in a single paragraph of the annotation methodology ([Document 1, n.d.](document_1.txt)).

## Consequences for the Released Label Distributions

The resolution protocol has measurable consequences. Of the 5,000 tweets sampled for annotation in v1.0, the benchmark dataset ultimately contained 4,779 tweets, "containing over 29% offensive content" ([Document 1, n.d.](document_1.txt)). This implies that 221 sampled tweets (4.42% of the sample) were removed — consistent with the *Spam* filter and/or with items that could not be brought to the required agreement threshold. The distribution is as follows.

| OGTD v1.0 label | Training set | Test set | Total | Share of total |
|---|---|---|---|---|
| Offensive | 955 | 446 | 1,401 | 29.3% |
| Not Offensive | 2,390 | 988 | 3,378 | 70.7% |
| All | 3,345 | 1,434 | 4,779 | 100% |

Source: ([Document 1, n.d.](document_1.txt)).

| OGTD v2.0 label | Training set | Test set | Total | Share of total |
|---|---|---|---|---|
| Offensive | 2,486 | 425 | 2,911 | 28.3% |
| Not Offensive | 6,257 | 1,119 | 7,376 | 71.7% |
| All | 8,743 | 1,544 | 10,287 | 100% |

Source: ([Document 1, n.d.](document_1.txt)).

Two observations follow. First, the reported "over 29%" offensive content in v1.0 matches the tabulated 1,401/4,779 = 29.3% ([Document 1, n.d.](document_1.txt)). Second, the v2.0 proportions (28.3% offensive) are closely aligned with v1.0, which is what one would expect if identical guidelines and an identical adjudication protocol were applied to the new batch ([Document 1, n.d.](document_1.txt)). The splitting proportions, however, differ between versions: v1.0 allocates roughly 70% of instances to training and 30% to testing, whereas v2.0 allocates roughly 85% to training and 15% to testing ([Document 1, n.d.](document_1.txt)). The documentation does not explain this shift, but it is visible directly in the arithmetic: 1,434 test instances in v1.0 rise to only 1,544 in v2.0, even though the corpus more than doubles in size ([Document 1, n.d.](document_1.txt)).

## Critical Assessment

Three points merit emphasis.

**First, the core answer is unambiguous for v1.0.** Three volunteer annotators labelled each tweet, using a three-tag scheme, under Greek-language guidelines ([Document 1, n.d.](document_1.txt)). Every element of the disagreement protocol — pairwise kappa, two-of-three majorities, and escalation when no majority exists — is consistent with a three-annotator design ([Document 1, n.d.](document_1.txt)).

**Second, the reporting for v2.0 is incomplete.** The new batch is attributed to "a team of volunteers" without a stated headcount ([Document 1, n.d.](document_1.txt)). Because the paper claims the guidelines were unchanged and the same adjudication logic is implied, the three-annotator structure is the most plausible reading, but it remains an inference rather than a documented fact. This matters for reproducibility: any assessment of the corpus's reliability ceiling depends on knowing the effective number of independent judgements per item.

**Third, the escalation tier introduces a qualitative asymmetry in the gold standard.** Tier-1 labels rest on unanimous independent judgement; tier-2 labels rest on a two-of-three majority; tier-3 labels rest on a re-review by three different adjudicators who are aware that the original annotation failed to converge ([Document 1, n.d.](document_1.txt)). The documentation does not report how many items fell into each tier, so the proportion of the gold standard produced by author-mediated adjudication is unknown. Reporting per-tier counts would substantially strengthen future versions of the dataset documentation.

## Conclusion

The OGTD annotation effort relied on **three volunteer annotators** working from Greek-language guidelines and an explicit definition of offensive language, classifying each tweet as *Offensive*, *Not Offensive*, or *Spam* ([Document 1, n.d.](document_1.txt)). Disagreements were resolved through a graded protocol: unanimous labels were accepted directly; labels supported by a majority above 66% (equivalently, two of three annotators) were adopted as gold; and complete disagreement triggered escalation to a panel comprising one of the paper's authors and two additional human judges, whose task was to restore agreement above the 66% threshold ([Document 1, n.d.](document_1.txt)). Reliability across annotator pairs was quantified with Cohen's kappa ([Document 1, n.d.](document_1.txt)). The protocol produced 4,779 published instances in v1.0 with just over 29% offensive content, and a v2.0 corpus of 10,287 instances with 28.3% offensive content, the second version's newly annotated batch having been handled by a volunteer team whose exact size the documentation leaves unstated ([Document 1, n.d.](document_1.txt)).

## References

Document 1. (n.d.). *OGTD dataset documentation* [Source document]. document_1.txt