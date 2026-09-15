# Hand-Crafted Template Count in Knowledge-Base Question Generation: A Detailed Report

## Introduction

The task of question generation from a knowledge base (KB) involves producing fluent, natural, and domain-relevant questions from structured KB triples ([document_1.txt](document_1.txt)). A central challenge is that KBs abstract away function words and morphological forms, making direct translation into natural language non-trivial ([document_1.txt](document_1.txt)). The system described in the provided sources addresses this challenge by combining a small set of hand-crafted question templates with iterative web exploration ([document_1.txt](document_1.txt)). The only human labor reported in this work is the construction of question templates ([document_1.txt](document_1.txt)). Therefore, the number of hand-crafted templates is a critical metric for understanding the system’s human-effort requirements.

The query asks: “How many hand-crafted templates did they have to make?” Based on the provided documents, the authors hand-crafted 106 templates for the Freebase evaluation and 103 templates for the in-house power tool domain, resulting in a total of 209 hand-crafted templates ([document_2.txt](document_2.txt)). This report provides a detailed breakdown of these figures, explains how the template counts relate to KB predicates, and discusses why template construction constitutes the sole manual component of the system.

## Direct Answer and Summary of Counts

The total number of hand-crafted templates reported across the two evaluations is 209 ([document_2.txt](document_2.txt)). This total comprises 106 templates for the Freebase KB and 103 templates for the in-house power tool domain KB ([document_2.txt](document_2.txt)). Table 1 summarizes these counts alongside the number of predicates and triples involved in each evaluation.

**Table 1. Hand-crafted templates by knowledge base.**

| Knowledge Base | Number of Triples | Number of Predicates | Hand-crafted Templates | Average Templates per Predicate |
|---|---:|---:|---:|---:|
| Freebase | 500 | 53 | 106 | 2.00 |
| Power tool domain | Not reported | 67 | 103 | 1.54 |
| Total | 500 (Freebase only) | 120 (combined) | 209 | — |

*Note.* Data compiled from ([document_1.txt](document_1.txt)) and ([document_2.txt](document_2.txt)). The total predicate count of 120 is the sum of distinct predicates across the two separate KB evaluations; the templates are not shared across KBs because each KB has its own predicate set ([document_2.txt](document_2.txt)).

The Freebase evaluation used 500 randomly selected triples that shared only 53 distinct predicates ([document_2.txt](document_2.txt)). The authors created 106 templates for those triples, which corresponds to an average of two templates per predicate ([document_2.txt](document_2.txt)). For the power tool domain KB, the paper reports 67 predicates and 103 hand-crafted templates ([document_2.txt](document_2.txt)). When combined with the Freebase templates, the authors wrote 209 templates in total ([document_2.txt](document_2.txt)). This total is explicitly reported in the template-construction experiment ([document_2.txt](document_2.txt)).

## Breakdown by Evaluation

### Freebase Evaluation

For the Freebase evaluation, the work uses 500 randomly selected triples ([document_2.txt](document_2.txt)). The paper reports 106 hand-crafted templates for those 500 Freebase triples ([document_2.txt](document_2.txt)). The triples share only 53 distinct predicates, so the authors made two templates for each predicate on average ([document_2.txt](document_2.txt)). This design ties template creation to predicates, keeping the template set compact relative to the triple set ([document_2.txt](document_2.txt)). Applying the templates to the triples generated 991 seed questions ([document_1.txt](document_1.txt)). The experiment also retrieved 1,529 more questions from Google ([document_1.txt](document_1.txt)). To evaluate fluency, the authors trained a 4-gram language model (LM) on Gigaword (LDC2011T07) with Kneser-Ney smoothing ([document_1.txt](document_1.txt)). Using the averaged language model score as an index, the top 500 questions were selected to compare with the results from the baseline system ([document_1.txt](document_1.txt)). Three native English speakers evaluated the fluency and naturalness of both results based on a 4-point scheme where 4 is the best ([document_1.txt](document_1.txt)).

### In-House Power Tool Domain

For the in-house power tool domain knowledge base, the paper reports 67 predicates ([document_2.txt](document_2.txt)). For these 67 predicates, the authors hand-crafted 103 templates ([document_2.txt](document_2.txt)). Together with the 106 Freebase templates, the authors wrote 209 templates in total ([document_2.txt](document_2.txt)). The domain-specific KB has its own predicate set and required its own template set ([document_2.txt](document_2.txt)). These figures show that the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt](document_2.txt)).

An example from the power tool domain illustrates the template-predicate association. The template “how to use #X#” is first constructed for the predicate “performsActivity” ([document_1.txt](document_1.txt)). A seed question, “how to use jigsaw,” is generated by applying the template on the triple ⟨jigsaw, performsActivity, CurveCut⟩ ([document_1.txt](document_1.txt)). Questions are then retrieved from Google with the seed question ([document_1.txt](document_1.txt)). In the broader power tool experiment, the system generated 12,228 seed questions, from which 20,000 more questions were expanded with Google ([document_1.txt](document_1.txt)). Most expanded questions were grammatical and relevant to the power tool domain, and most were informative and corresponded to a specific answer, except for one example, “do I need a hammer drill,” which lacked context information ([document_1.txt](document_1.txt)). The system also generated complex questions such as “how to cut a groove in wood without a router” ([document_1.txt](document_1.txt)).

**Table 2. Example templates and seed questions.**

| Predicate | Template | Triple | Seed Question |
|---|---|---|---|
| performsActivity | how to use #X# | ⟨jigsaw, performsActivity, CurveCut⟩ | how to use jigsaw |
| Not specified | Not specified | Not specified | how to change circular saw blade |
| Not specified | Not specified | Not specified | how to measure lawn mower cutting height |
| Not specified | Not specified | Not specified | how to sharpen drill bits on bench grinder |
| Not specified | Not specified | Not specified | how does an oscillating multi tool work |
| Not specified | Not specified | Not specified | how to cut a groove in wood without a router |
| Not specified | Not specified | Not specified | what type of sander to use on deck |
| Not specified | Not specified | Not specified | do i need a hammer drill |
| Not specified | Not specified | Not specified | can i use acrylic paint on wood |

*Note.* The first row is explicitly described in the provided sources ([document_1.txt](document_1.txt)). The remaining rows are examples of expanded questions listed in the power tool domain evaluation ([document_1.txt](document_1.txt)). The template and triple mappings for those rows are not provided in the source material.

## Why the Template Count Is the Only Human Labor

The paper states that the only human labor in this work is question template construction ([document_1.txt](document_1.txt)). The template construction therefore is the manual component reported ([document_2.txt](document_2.txt)). This is a significant design choice because previous approaches to question generation from KBs have relied on massive human-labeled data. For example, one prior method treats question generation as a machine translation problem and trains a neural machine translation (NMT) system with 10,000 ⟨triple, question⟩ pairs ([document_1.txt](document_1.txt)). At test time, input triples are “translated” into questions with the NMT system ([document_1.txt](document_1.txt)). However, the question part of the 10,000 pairs is human generated, which requires a large amount of human effort ([document_1.txt](document_1.txt)). In addition, the grammaticality and naturalness of generated questions cannot be guaranteed ([document_1.txt](document_1.txt)). In contrast, the template-based system requires only 209 hand-crafted templates in total and leverages web resources to expand the question set ([document_2.txt](document_2.txt)).

**Table 3. Comparison of human effort: template-based system vs. NMT baseline.**

| Aspect | Template-based system | NMT-based prior work |
|---|---:|---:|
| Human-labeled ⟨triple, question⟩ pairs | 0 | 10,000 |
| Hand-crafted templates | 209 total (106 Freebase + 103 power tool) | Not applicable |
| Primary human labor | Template construction | Creating 10,000 question pairs |
| Use of web resources | Iterative question expansion via search engine | Not described |
| Guarantee of grammaticality/naturalness | Evaluated by human graders; judged better than baseline on grammaticality and naturalness | Cannot be guaranteed |

*Note.* Data compiled from ([document_1.txt](document_1.txt)) and ([document_2.txt](document_2.txt)). The NMT comparison refers to the unnamed baseline system discussed in the source ([document_1.txt](document_1.txt)).

The system does not require a large number of templates for two reasons: (1) the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions, and (2) multiple entities in the KB share the same predicates ([document_1.txt](document_1.txt)). Another advantage is that the system can easily generate updated questions as the web is self-updating consistently ([document_1.txt](document_1.txt)). Evaluated by three human graders, questions generated by the system are significantly better than the baseline on grammaticality and naturalness ([document_1.txt](document_1.txt)). In the Freebase evaluation, the system’s questions were judged to be more fluent than those of the baseline ([document_1.txt](document_1.txt)).

## Scaling and Efficiency of Template Construction

The template count scales with predicate coverage rather than with the number of triples. For the Freebase evaluation, 500 triples shared only 53 distinct predicates, and the authors created 106 templates, an average of two per predicate ([document_2.txt](document_2.txt)). For the power tool domain, 67 predicates required 103 templates, an average of approximately 1.54 templates per predicate ([document_2.txt](document_2.txt)). This design keeps the template set compact relative to the triple set ([document_2.txt](document_2.txt)). Because multiple entities share the same predicates, a single template can be applied to many triples, generating a large number of seed questions ([document_1.txt](document_1.txt)). The iterative expansion then multiplies the seed set further. For example, in the power tool domain, 12,228 seed questions were generated, and 20,000 more questions were expanded with Google ([document_1.txt](document_1.txt)). In the Freebase evaluation, 991 seed questions were generated from the templates, and 1,529 more questions were retrieved from Google ([document_1.txt](document_1.txt)).

**Table 4. Seed and expanded question counts by evaluation.**

| Evaluation | Hand-crafted Templates | Seed Questions | Questions Retrieved/Expanded via Google |
|---|---:|---:|---:|
| Freebase | 106 | 991 | 1,529 |
| Power tool domain | 103 | 12,228 | 20,000 |
| Total templates | 209 | — | — |

*Note.* Data compiled from ([document_1.txt](document_1.txt)) and ([document_2.txt](document_2.txt)). The power tool seed question count and expanded count are reported in the source ([document_1.txt](document_1.txt)). The Freebase seed and retrieved counts are also reported ([document_1.txt](document_1.txt)).

The efficiency of the template approach is further highlighted by the fact that the only human labor is template construction ([document_1.txt](document_1.txt)). No human-labeled question-answer pairs are required. The system first constructs a small set of question templates, each associated with a predicate in the KB ([document_1.txt](document_1.txt)). The templates consist of a transcription of the predicate in the KB (e.g., performsActivity → how to) and placeholders for the subject (#X#) and the object (#Y#) ([document_1.txt](document_1.txt)). A seed question set is then generated by applying the templates on the KB ([document_1.txt](document_1.txt)). The seed question set is further expanded through a search engine such as Google or Bing by iteratively forming each generated question as a search query to retrieve more related question candidates ([document_1.txt](document_1.txt)). Finally, a selection step is applied by estimating the fluency and domain relevance of each question candidate ([document_1.txt](document_1.txt)). This pipeline allows a relatively small number of templates—209 in total—to yield tens of thousands of questions.

## Implications and Conclusion

The answer to the query is that the authors had to make 209 hand-crafted templates in total: 106 for the Freebase evaluation and 103 for the in-house power tool domain ([document_2.txt](document_2.txt)). This figure represents the complete manual template-building effort reported across both evaluations ([document_2.txt](document_2.txt)). The template construction is the only human labor in the system ([document_1.txt](document_1.txt)). By leveraging rich web information, the system is able to generate domain-relevant questions in a wide scope while significantly reducing human effort ([document_1.txt](document_1.txt)). Evaluated by human graders, questions generated by the system are significantly better than those from the baseline on 500 randomly selected triples from Freebase ([document_1.txt](document_1.txt)). The system also demonstrated generated questions from the in-house KB of the power tool domain, which are fluent and domain-relevant in general ([document_1.txt](document_1.txt)). The current system only generates questions without answers, leaving automatic answer mining as future work ([document_1.txt](document_1.txt)).

The 209-template figure is a concrete measure of the system’s human-effort requirement. It stands in contrast to the 10,000 human-generated question pairs required by the NMT baseline ([document_1.txt](document_1.txt)). The template count is tied to predicates, not triples, which makes it scalable across large KBs where many entities share the same predicates ([document_1.txt](document_1.txt)). The reported averages—2.0 templates per predicate for Freebase and approximately 1.54 for the power tool domain—show that template creation is a bounded, predicate-level task ([document_2.txt](document_2.txt)). In summary, the hand-crafted template count is 209, and this compact template set, combined with iterative web expansion and fluency-based selection, enables the generation of fluent, natural, and domain-relevant questions from a knowledge base ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Question generation from a knowledge base with web exploration*. [Unpublished manuscript]. Retrieved from document_1.txt

document_2.txt. (n.d.). *Third-party research note: Question generation from a knowledge base with web exploration*. [Research note]. Retrieved from document_2.txt