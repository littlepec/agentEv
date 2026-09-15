# Hand-Crafted Question Template Counts in Knowledge-Base Question Generation: A Detailed Report

## Introduction and Scope

The query at hand asks a deceptively simple question: how many hand-crafted templates did the authors have to make? The answer requires separating three distinct figures that appear in the source material — one for an external benchmark evaluation, one for a proprietary domain knowledge base, and one aggregate total — and then explaining why those numbers are structured the way they are. The underlying system is a knowledge-base-to-question generator that deliberately replaces large-scale human annotation with a small, predicate-anchored template set plus automated web exploration ([Document 1, n.d.](document_1.txt)). Understanding the template counts therefore requires understanding the system architecture, because the counts are not arbitrary; they are a direct consequence of a design decision to tie template creation to knowledge-base predicates rather than to entities, triples, or individual questions ([Document 2, n.d.](document_2.txt)).

This report provides the direct numeric answer, situates it within the system's four-module pipeline, and evaluates what the figures imply about the actual manual labor burden claimed by the authors.

## 1. The Direct Answer

The authors reported hand-crafted template counts in two separate evaluation settings, which together produce a single aggregate total.

### 1.1 Freebase Evaluation: 106 Templates

For the Freebase evaluation, the work used 500 randomly selected triples, and the paper reports **106 hand-crafted templates** for those 500 triples ([Document 2, n.d.](document_2.txt)). The key explanatory detail is that these 500 triples shared only **53 distinct predicates**, so the authors produced roughly **2 templates for each predicate on average** ([Document 2, n.d.](document_2.txt); [Document 1, n.d.](document_1.txt)). This is an important structural point: the template count scales with predicate diversity, not with the number of triples or entities. Had the 500 triples been drawn from a much larger predicate vocabulary, the template count would necessarily have been higher.

### 1.2 In-House Power Tool Domain: 103 Templates

For the in-house power tool domain knowledge base, the paper reports **67 predicates**, for which the authors hand-crafted **103 templates** ([Document 2, n.d.](document_2.txt)). This yields an average of approximately 1.54 templates per predicate, a slightly leaner ratio than the Freebase evaluation but consistent with the same predicate-driven logic.

### 1.3 Aggregate Total: 209 Templates

Together with the 106 Freebase templates, the authors wrote **209 templates in total**, a figure the paper reports explicitly in the template-construction experiment ([Document 2, n.d.](document_2.txt)). The arithmetic is straightforward: 106 + 103 = 209. The 209 figure is the headline answer for anyone asking how much manual template authoring the entire reported effort required.

## 2. Reported Template Counts at a Glance

| Evaluation Setting | Triples | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate | Templates per Triple |
|---|---|---|---|---|---|
| Freebase (randomly selected) | 500 | 53 | 106 | ~2.00 | ~0.21 |
| In-house power tool domain KB | Not reported | 67 | 103 | ~1.54 | Not applicable |
| **Combined total reported** | — | — | **209** | — | — |

*Table 1. Reported hand-crafted template counts across the two evaluation settings. Derived ratios are computed from the reported figures ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)).*

Two observations follow immediately from Table 1. First, the average templates-per-predicate ratio is close to 2 in the Freebase case and somewhat below 2 in the power tool case, meaning the template bank is small and repetitive by design rather than exhaustive. Second, the ratio of templates to triples in the Freebase setting is roughly 0.21, which is the structural reason the authors can claim a compact template set relative to the triple set ([Document 2, n.d.](document_2.txt)).

## 3. Why the Counts Are Small: Predicate-Driven Template Design

### 3.1 Templates Anchored to Predicates

The system first constructs a small set of question templates, each associated with a predicate in the knowledge base ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). This association means template creation follows the predicates present in the KB rather than the entities or the individual facts ([Document 2, n.d.](document_2.txt)). Because multiple entities in a KB share the same predicates, a single template can be reused across many triples ([Document 1, n.d.](document_1.txt)). That reuse is the primary mechanism that keeps the count at 209 rather than in the thousands.

### 3.2 Why the Ratio Is Not Exactly Two per Predicate

The Freebase setting produced an average of two templates per predicate, while the power tool setting produced approximately 1.54 per predicate. This suggests the template count is not generated by a rigid rule but by a judgement call about how many natural-language surface forms each predicate requires. Predicates with multiple common phrasings presumably received more templates; predicates with a single dominant phrasing received fewer. The documents do not enumerate per-predicate allocations, so this remains a reasonable inference from the reported averages rather than a stated finding ([Document 2, n.d.](document_2.txt)).

### 3.3 Template Structure and an Illustrative Example

Templates consist of a transcription of the KB predicate plus placeholders for the subject and object ([Document 1, n.d.](document_1.txt)). The paper gives the concrete example of the template "how to use #X#", which is constructed for the predicate "performsActivity"; the placeholder #X# stands for the subject and #Y# for the object ([Document 1, n.d.](document_1.txt)). Morphological and function-word information that a KB abstracts away must be supplied by the template text itself, which is precisely why this component is manual: the KB alone cannot recover it ([Document 1, n.d.](document_1.txt)).

## 4. From Templates to Questions: The Generation Leverage

The small template count matters because the downstream pipeline multiplies it. The system contains four sub-modules: question template construction, seed question generation, question expansion, and selection ([Document 1, n.d.](document_1.txt)).

### 4.1 Automatically Generated Seed Questions

Applying the template set to the input KB produces the seed question set. In the Freebase evaluation, applying 106 templates to 500 triples generated **991 seed questions** ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). This corresponds to roughly **9.4 seed questions per template**. In the power tool domain, the system generated **12,228 seed questions** ([Document 1, n.d.](document_1.txt)), which corresponds to approximately **119 seed questions per one of the 103 templates**. The disparity between these two per-template yields reflects the difference in KB size between the two settings rather than any change in methodology.

### 4.2 Web-Based Expansion

Beyond seed generation, additional questions were retrieved from search engines by iteratively forming already-obtained questions as queries ([Document 1, n.d.](document_1.txt)). In the Freebase evaluation, **1,529 further questions were retrieved from Google** ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)), bringing the candidate pool to 2,520 before selection. In the power tool domain, **20,000 more questions were expanded with Google** ([Document 1, n.d.](document_1.txt)). Taken together, the reported figures imply that 209 hand-crafted templates ultimately seeded 13,219 questions, which were then expanded by 21,529 web-retrieved candidates — a derived aggregate of roughly 34,748 question candidates arising from 209 manual artifacts.

| Pipeline Stage | Freebase Evaluation | Power Tool Domain KB |
|---|---|---|
| Hand-crafted templates | 106 | 103 |
| Seed questions generated | 991 | 12,228 |
| Questions retrieved/expanded via Google | 1,529 | 20,000 |
| Candidate pool before selection | 2,520 | 32,228 |
| Questions selected for comparison | Top 500 | Not reported |

*Table 2. Reported and derived pipeline volumes for both evaluation settings ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)).*

## 5. Human Effort in Comparative Context

The paper states plainly that **the only human labor in this work is the question template construction** ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The reported manual component is therefore exactly the 209 templates. This is the point of contrast with prior neural approaches, which required a large amount of human effort because their question data was human generated ([Document 1, n.d.](document_1.txt)). One cited baseline trained a neural machine translation system on **10,000 triple–question pairs**, where the question portion was human generated ([Document 1, n.d.](document_1.txt)). Against that benchmark, 209 reusable templates represent a substantially smaller manual artifact, although the two figures measure different things: templates are reusable surface-form rules, whereas 10,000 question pairs are training instances.

The authors also offer two explicit justifications for why the system does not require many templates: iterative question expansion can produce large numbers of questions even from a relatively small seed set, and multiple entities share the same predicates ([Document 1, n.d.](document_1.txt)). A further claimed advantage is that the system can generate updated questions as the web self-updates ([Document 1, n.d.](document_1.txt)).

## 6. How the Template Output Was Evaluated

The fluency of candidate questions was assessed by training a 4-gram language model on Gigaword (LDC2011T07) with Kneser-Ney smoothing; using the averaged language model score as an index, the top 500 questions were selected for comparison against baseline results retrieved from an external source ([Document 1, n.d.](document_1.txt)). Three native English speakers then evaluated fluency and naturalness — specifically whether people would ask the questions in reality — on a 4-point scheme where 4 is best ([Document 1, n.d.](document_1.txt)). The system was judged significantly better than the baseline on grammaticality and naturalness ([Document 1, n.d.](document_1.txt)).

Representative expanded questions from the power tool domain include "how to change circular saw blade," "how to sharpen drill bits on bench grinder," and the more complex "how to cut a groove in wood without a router" ([Document 1, n.d.](document_1.txt)). The authors note that most questions are grammatical and domain-relevant, though one example — "do I need a hammer drill" — lacks context information ([Document 1, n.d.](document_1.txt)).

## 7. Analytical Interpretation

My assessment is that the reported figures are internally consistent and that the 209-template total is the correct answer to the query, but that the number should be read as a claim about *shape of effort* rather than a purely quantitative comparison. Three points support this reading. First, the derived ratio of roughly two templates per predicate is small enough that the template bank cannot be covering every syntactic nuance of every predicate; it is covering the dominant surface forms. Second, the seed-question multipliers are substantial, particularly in the power tool domain, which substantiates the authors' argument that a small template set suffices when combined with entity reuse ([Document 1, n.d.](document_1.txt)). Third, the documented example — one template mapping "performsActivity" onto "how to use #X#" and then instantiating on ⟨jigsaw, performsActivity, CurveCut⟩ to produce "how to use jigsaw" — demonstrates that the manual work is a one-time linguistic mapping, after which generation is automated ([Document 1, n.d.](document_1.txt)).

The practical implication is that the marginal human cost of adding a new predicate to the KB is on the order of one to two templates, not hundreds of annotated questions. That is the principal efficiency claim the counts support.

## 8. Limitations of the Reported Figures

Several caveats apply. No per-predicate template allocation is provided, so the averages of 2.0 and 1.54 templates per predicate cannot be verified at the individual predicate level ([Document 2, n.d.](document_2.txt)). The number of triples in the power tool KB is not reported, preventing a templates-per-triple ratio for that setting. The aggregate of 209 is reported as a sum of two separately reported counts rather than as an independently measured total ([Document 2, n.d.](document_2.txt)). Finally, the baseline system in the comparison is anonymized in the available text, so the human-effort contrast rests on the reported 10,000 triple–question training pairs rather than on a fully identified comparator ([Document 1, n.d.](document_1.txt)).

## 9. Conclusion

The answer to the query is **106** templates for the 500-triple Freebase evaluation, **103** templates for the 67-predicate in-house power tool knowledge base, and **209** templates in total ([Document 2, n.d.](document_2.txt)). These counts reflect a deliberate architecture in which template creation is bound to knowledge-base predicates, the sole manual component of the system, with all subsequent question generation and expansion performed automatically through template application and iterative search-engine retrieval ([Document 1, n.d.](document_1.txt)). The reported figures indicate that manual template authoring does not need to scale with the number of triples or entities, only with the diversity of predicates the system must cover.

## References

Document 1. (n.d.). *Question generation from a knowledge base with web exploration* [Manuscript]. [document_1.txt](document_1.txt)

Document 2. (n.d.). *Third-party research note: Question generation from a knowledge base with web exploration* [Research note]. [document_2.txt](document_2.txt)