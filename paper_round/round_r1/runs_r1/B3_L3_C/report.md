# Hand-Crafted Template Counts in Question Generation from a Knowledge Base with Web Exploration

## Introduction

The question of how many hand-crafted templates were required is central to evaluating the human-effort profile of the question-generation system described in *Question Generation from a Knowledge Base with Web Exploration*. The paper states plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, n.d.](document_1.txt)). Because template construction is the sole manual component of the pipeline, the reported template counts function as the paper's primary effort metric. The source material reports two separate figures rather than a single aggregate number: 106 hand-crafted templates for the Freebase evaluation and 163 hand-crafted templates for the in-house power tool domain knowledge base ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). This report examines both figures, the predicate-based logic that produces them, the yield each template set generated, and the implications for how much human effort the system actually requires.

## The Short Answer

The system's authors made **106 templates** when working with 500 randomly selected Freebase triples, and **163 templates** when working with their in-house power tool domain knowledge base ([Song & Zhao, n.d.](document_1.txt)). These two counts correspond to two different knowledge bases with different predicate inventories, as the third-party research note makes explicit: "That count differs from the Freebase template count because the domain-specific KB has its own predicate set and required its own template set" ([Third-party research note, n.d.](document_2.txt)). Across the two reported evaluations, the combined manual template-construction effort therefore amounts to 269 templates, although the paper does not present this as a cumulative figure — the counts are reported separately for each experimental setting.

| Evaluation Setting | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate | Seed Questions Generated | Additional Web-Retrieved Questions |
|---|---|---|---|---|---|
| Freebase (500 random triples) | 53 | 106 | 2.0 | 991 | 1,529 |
| In-house power tool KB | 67 | 163 | ≈2.43 | 12,228 | 20,000 |

All figures in the table are drawn from the paper's experimental sections ([Song & Zhao, n.d.](document_1.txt)) as summarized in the third-party research note ([Third-party research note, n.d.](document_2.txt)).

## The Predicate-Based Logic of Template Construction

Understanding the template counts requires understanding what a template is in this system. Given an input knowledge base, "a small set of question templates are first hand-crafted based on the predicates in the KB" ([Song & Zhao, n.d.](document_1.txt)). Each template consists of two components: "a transcription of the predicate in the KB (e.g. performsActivity ⇒ how to) and placeholders for the subject (#X#) and the object (#Y#)" ([Song & Zhao, n.d.](document_1.txt)). The paper illustrates this with a power tool example: the template "how to use #X#" is constructed for the predicate "performsActivity," and applying that single template to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question "how to use jigsaw" ([Song & Zhao, n.d.](document_1.txt)).

The critical design consequence is that "template creation follows the predicates present in the KB" rather than the individual triples ([Third-party research note, n.d.](document_2.txt)). Because many triples share predicates, the template count is tied to predicate coverage and remains "compact relative to the triple set" ([Third-party research note, n.d.](document_2.txt)). This is why 500 Freebase triples required only 106 templates: those triples "share only 5 3 distinct predicates," so the authors "made 2 templates for each predicate on average" ([Song & Zhao, n.d.](document_1.txt)). The arithmetic is exact — 53 predicates multiplied by 2 templates equals 106.

The paper justifies this economy directly: the system "does not require a large number of templates because: (1) the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions, as we see in the experiments, (2) multiple entities in the KB share the same predicates" ([Song & Zhao, n.d.](document_1.txt)). Consequently, the manual authoring burden scales with the diversity of predicates rather than with the volume of triples.

## The Freebase Evaluation: 106 Templates

In the first experiment, the authors compared their end-to-end system with a prior state-of-the-art method on 500 randomly selected triples from Freebase, described as "a domain-general KB" ([Song & Zhao, n.d.](document_1.txt)). For those 500 triples, the reported template count is 106, derived from 53 distinct predicates at an average of two templates per predicate ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

Applying those 106 templates to the triples produced 991 seed questions, and a further 1,529 questions were retrieved from Google ([Song & Zhao, n.d.](document_1.txt)). This means roughly 2,520 candidate questions were available from a manual investment of 106 templates — approximately 23.8 questions per template before selection filtering. The third-party note emphasizes that this design "ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-party research note, n.d.](document_2.txt)).

Selection then reduced the candidate pool: fluency was evaluated using a 4-gram language model trained on Gigaword (LDC2011T07) with Kneser-Ney smoothing, and "using the averaged language model score as index, the top 5 0 0 questions are selected to compare with the results from" the baseline ([Song & Zhao, n.d.](document_1.txt)). Domain relevance was computed as the cosine similarity between the embedding of a candidate question and the embedding of the seed question set treated as in-domain data ([Song & Zhao, n.d.](document_1.txt)). Thresholds for relevance and fluency were applied to filter out sub-threshold questions ([Song & Zhao, n.d.](document_1.txt)).

Human evaluation of the resulting questions, conducted by three native English speakers on a 4-point scale, gave the system grammaticality and naturalness scores of 3.53 and 3.31 respectively, compared with 3.36 and 3.14 for the baseline ([Song & Zhao, n.d.](document_1.txt)). The naturalness score is lower than the grammaticality score for both methods because "naturalness is a more strict metric since a natural question should also be grammatical" ([Song & Zhao, n.d.](document_1.txt)).

## The Power Tool Domain Evaluation: 163 Templates

The third experiment was run on "our in-house KB in the power tool domain," which "contains 6 7 distinct predicates, 2 9 3 distinct subjects and 2 7 9 distinct objects respectively" ([Song & Zhao, n.d.](document_1.txt)). For those 67 predicates, the authors hand-crafted **163 templates** ([Song & Zhao, n.d.](document_1.txt)). This yields an average of approximately 2.43 templates per predicate — a higher ratio than the Freebase evaluation's two templates per predicate.

The third-party note confirms that the difference in raw counts follows from the different predicate inventories: the domain-specific KB "has its own predicate set and required its own template set," and "these figures show the manual template-building effort scales with predicate coverage in each evaluation" ([Third-party research note, n.d.](document_2.txt)).

The power tool experiment used the same language model as the first experiment and a skip-gram model trained on Wikipedia for domain-relevance evaluation ([Song & Zhao, n.d.](document_1.txt)). The 163 templates generated 12,228 seed questions, from which 20,000 more questions were expanded using Google ([Song & Zhao, n.d.](document_1.txt)). That is a striking yield: 32,228 total candidate questions from 163 manual templates, or roughly 198 questions per template. Representative expanded questions judged "grammatical and relevant to the power tool domain" include "how to change circular saw blade," "how to measure lawn mower cutting height," "how to sharpen drill bits on bench grinder," "how does an oscillating multi tool work," "how to cut a groove in wood without a router," "what type of sander to use on deck," "do i need a hammer drill," "can i use acrylic paint on wood," and "how to use a sharpening stone with oil" ([Song & Zhao, n.d.](document_1.txt)).

The authors note that "in addition to the simple factoid questions, our system generates many complex questions such as 'how to cut a groove in wood without a router'" ([Song & Zhao, n.d.](document_1.txt)). They also observe that most questions are informative and correspond to a specific answer, "except the one 'do I need a hammer drill' that lacks context information" ([Song & Zhao, n.d.](document_1.txt)).

## Comparative Assessment of the Two Template Counts

The two figures answer the query depending on which evaluation one examines. Several observations follow from the reported numbers.

First, the template counts are modest in absolute terms. Neither evaluation required more than 163 manual templates, and both were built against relatively narrow predicate inventories of 53 and 67 predicates respectively ([Song & Zhao, n.d.](document_1.txt)).

Second, the Freebase setting is the more efficient in templates-per-predicate terms, at exactly 2.0, while the power tool setting required about 2.43 per predicate. This likely reflects the more specialized, procedural nature of power tool predicates, which may need additional phrasing variants to produce natural questions.

Third, the downstream yield differs enormously. The Freebase run produced 991 seed questions and 1,529 web-retrieved questions ([Song & Zhao, n.d.](document_1.txt)), while the power tool run produced 12,228 seed questions and 20,000+ web-expanded questions ([Song & Zhao, n.d.](document_1.txt)). The power tool KB's larger predicate and entity inventory, combined with its denser set of triples, accounts for much of that difference.

Fourth, the paper's broader claim about effort reduction rests on the interaction between templates and web expansion. Because search-engine expansion is iterative — Algorithm 1 initializes the expanded set as the seed set and repeatedly queries the web, adding retrieved questions not already in the set, up to a maximum iteration count ([Song & Zhao, n.d.](document_1.txt)) — a small manual seed can grow substantially without additional human authoring.

## Validity Checks Reported Alongside the Template Counts

The paper supports its low-template approach with a second, independent experiment on the web snippet dataset, "a commonly-used [dataset] for domain classification of short documents" containing 10,060 training and 2,280 test snippets across 8 classes, with an average of 18 words per snippet ([Song & Zhao, n.d.](document_1.txt)). The proposed domain-relevance method achieved a precision of 85.65, outperforming prior methods reported at 82.18, 85.31, and 85.48 ([Song & Zhao, n.d.](document_1.txt)). The authors attribute this to word embeddings capturing similarity between distinct words such as "finance" and "economy," which traditional topic-based methods handle less effectively ([Song & Zhao, n.d.](document_1.txt)). This matters for the template question because accurate relevance filtering is what allows a small template set to yield a high-quality final question pool.

## Limitations and Caveats

Several caveats apply to the template counts. The paper reports 106 and 163 as counts for two separate experiments, not as a single unified total; readers should avoid summing them without acknowledging that these are distinct KBs with distinct predicate sets ([Third-party research note, n.d.](document_2.txt)). The source text also contains OCR artifacts, including placeholder "? )" markers where baseline citations should appear, so some comparative details are obscured ([Song & Zhao, n.d.](document_1.txt)). Finally, the system "only generates questions without answers," leaving automatic answer mining as future work ([Song & Zhao, n.d.](document_1.txt)) — meaning the template counts cover question generation only, not answer production.

## Conclusion

The answer to the query is that the authors had to make **106 hand-crafted templates** for the Freebase evaluation covering 500 triples and 53 distinct predicates, and **163 hand-crafted templates** for the in-house power tool domain knowledge base covering 67 distinct predicates ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Because template construction is "the only human labor in this work," these counts represent the entire manual annotation cost of the system ([Song & Zhao, n.d.](document_1.txt)). The design achieves this economy by binding each template to a predicate rather than to individual triples, then relying on seed-question generation and iterative web exploration to expand a compact manual seed into tens of thousands of candidate questions, which are subsequently filtered by fluency and domain-relevance thresholds ([Song & Zhao, n.d.](document_1.txt)). The evidence supports the conclusion that 106 and 163 are accurate, context-specific answers to the question of how many templates were needed, and that the manual burden scales with predicate coverage rather than with the size of the underlying triple set ([Third-party research note, n.d.](document_2.txt)).

## References

Song, L., & Zhao, L. (n.d.). *Question generation from a knowledge base with web exploration* [document_1.txt].

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.) [document_2.txt].