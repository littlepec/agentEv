# Hand-Crafted Template Counts in *Question Generation from a Knowledge Base with Web Exploration*

## Direct Answer to the Query

The number of hand-crafted question templates reported in this body of work depends on which of the two evaluation settings is being counted, and on which of the two available source documents is treated as authoritative. For the Freebase experiment on 500 randomly selected triples, the authors hand-crafted **106 templates** to cover the **53 distinct predicates** those triples contained — an average of approximately two templates per predicate ([Song & Zhao, n.d.](document_1.txt); [Research note, n.d.](document_2.txt)). For the in-house power tool domain knowledge base, the two source documents disagree: the primary paper text states that **163 templates** were hand-crafted for the **67 predicates** ([Song & Zhao, n.d.](document_1.txt)), whereas the third-party research note states **103 templates** for the same 67 predicates and reports a combined total of **209 templates** across both evaluations ([Research note, n.d.](document_2.txt)). The single most defensible figure for the system as a whole, as explicitly stated in the available sources, is therefore **209 hand-crafted templates**, with the caveat that this total derives from the secondary note rather than from the primary paper's own arithmetic, which would instead imply 269.

## Why the Template Count Is the Central Question

The template count is not a peripheral implementation detail in this system; it is the measure of essentially all human labor the method requires. The paper states plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, n.d.](document_1.txt)). The third-party note reinforces this framing, observing that "the template construction therefore is the manual component reported" ([Research note, n.d.](document_2.txt)). Every other stage of the pipeline — seed question generation, web-based expansion, and fluency and domain-relevance filtering — is automated. As a result, the template tally functions as the system's principal efficiency claim: the smaller the template set relative to the number of triples it serves, the stronger the argument that the approach "significantly reduces the human effort" relative to prior neural machine translation systems trained on 10,000 human-written ⟨triple, question⟩ pairs ([Song & Zhao, n.d.](document_1.txt)).

## The Two Evaluation Settings and Their Reported Counts

### Freebase: 106 Templates for 53 Distinct Predicates

In the first experiment, the authors compared their end-to-end system against a prior state-of-the-art neural method ([Serban et al., 2016, as cited in Song & Zhao, n.d.](document_1.txt)) on **500 randomly selected triples** drawn from Freebase, a domain-general knowledge base ([Song & Zhao, n.d.](document_1.txt)). Because those 500 triples collectively shared only **53 distinct predicates**, the authors constructed **106 templates**, which the paper explicitly describes as "2 templates for each predicate on average" ([Song & Zhao, n.d.](document_1.txt)). Applying these 106 templates to the triples produced **991 seed questions**, and a further **1,529 questions** were retrieved from Google during the expansion stage ([Song & Zhao, n.d.](document_1.txt); [Research note, n.d.](document_2.txt)). The third-party note summarizes this design principle concisely: "This design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Research note, n.d.](document_2.txt)).

### In-House Power Tool Domain: 103 or 163 Templates for 67 Predicates

The third experiment applied the same framework to a "highly specialized in-house KB" in the power tool domain, containing **67 distinct predicates**, **293 distinct subjects**, and **279 distinct objects** ([Song & Zhao, n.d.](document_1.txt)). Here the source record diverges:

- The primary paper states: "For the 67 predicates, we hand-craft 163 templates" ([Song & Zhao, n.d.](document_1.txt)).
- The third-party note states: "For the 67 predicates, the authors hand-crafted 103 templates," and adds that "Together with the 106 Freebase templates, the authors wrote 209 templates in total" ([Research note, n.d.](document_2.txt)).

Notably, the secondary note's arithmetic is internally consistent only with the 103 figure: 106 + 103 = 209. The primary text's 163 figure would yield 269 when combined with the Freebase count, a total that appears nowhere in either document ([Song & Zhao, n.d.](document_1.txt); [Research note, n.d.](document_2.txt)).

| Evaluation Setting | Knowledge Base Scale | Distinct Predicates | Hand-Crafted Templates Reported | Templates per Predicate |
|---|---|---|---|---|
| Freebase experiment | 500 triples | 53 | 106 ([Song & Zhao, n.d.](document_1.txt)) | ≈ 2.0 |
| Power tool (primary text) | 293 subjects, 279 objects | 67 | 163 ([Song & Zhao, n.d.](document_1.txt)) | ≈ 2.4 |
| Power tool (research note) | 293 subjects, 279 objects | 67 | 103 ([Research note, n.d.](document_2.txt)) | ≈ 1.5 |
| Combined total (research note) | Both KBs | 120 | 209 ([Research note, n.d.](document_2.txt)) | — |
| Combined total (implied by primary text) | Both KBs | 120 | 269 (calculated) | — |

## Reconciling the Discrepancy

The conflicting figures of 163 and 103 are worth flagging rather than silently harmonizing, because both documents are affected by extraction artifacts. The primary paper's text is demonstrably degraded — references appear as "? )" placeholders throughout, the authors' own citations are partially lost, and numerals are rendered with irregular spacing (for example, "1 0 6" for 106 and "2 2 8 0" for 2,280) ([Song & Zhao, n.d.](document_1.txt)). In this context, "1 6 3" versus "1 0 3" is exactly the kind of digit-level ambiguity that optical character recognition and PDF extraction errors routinely produce. The third-party note is not immune to such issues either, but it is internally arithmetically consistent at 103 + 106 = 209 ([Research note, n.d.](document_2.txt)).

Applying the documentation-hierarchy principle that a primary source should normally take precedence over a derivative one, the 163 figure would be preferred for the power tool KB ([Song & Zhao, n.d.](document_1.txt)). However, because the primary text is visibly corrupted and because the secondary note's total of 209 is explicitly asserted rather than merely calculated, the most cautious reading is that the exact power tool template count is uncertain within the range of roughly 103 to 163, and that the total across both evaluations lies between 209 and 269. The 106-template Freebase count is the only figure both documents agree on without qualification ([Song & Zhao, n.d.](document_1.txt); [Research note, n.d.](document_2.txt)).

## What a Template Actually Contains

Understanding the count requires understanding what each unit of manual labor consists of. Each template is associated with exactly one predicate in the knowledge base, meaning "template creation follows the predicates present in the KB" ([Research note, n.d.](document_2.txt)). A template combines two elements: a natural-language transcription of the predicate and placeholder slots for the arguments of the triple. Concretely, the predicate "performsActivity" is transcribed as "how to," and the template "how to use #X#" contains placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, n.d.](document_1.txt)). Applying that single template to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question "how to use jigsaw" ([Song & Zhao, n.d.](document_1.txt)). Because multiple entities in a KB share the same predicates, a compact template set covers a much larger triple set — which is the structural reason the authors "do not require a large number of templates" ([Song & Zhao, n.d.](document_1.txt)).

## Output Volume Attributable to the Template Investment

The leverage of the template approach is visible in the seed-question volumes the templates generated across the two evaluations.

| Evaluation | Templates | Seed Questions Generated | Additional Web-Retrieved Questions |
|---|---|---|---|
| Freebase (500 triples) | 106 | 991 ([Song & Zhao, n.d.](document_1.txt)) | 1,529 from Google ([Song & Zhao, n.d.](document_1.txt)) |
| Power tool domain | 103 or 163 ([Research note, n.d.](document_2.txt); [Song & Zhao, n.d.](document_1.txt)) | 12,228 ([Song & Zhao, n.d.](document_1.txt)) | 20,000+ from Google ([Song & Zhao, n.d.](document_1.txt)) |

The expansion stage further amortizes the manual cost. The pipeline treats already-obtained questions as search queries fed into a standard search engine, iteratively retrieving related question candidates and adding them to the expansion set when they are not already present, bounded by a maximum iteration count ([Song & Zhao, n.d.](document_1.txt)). The authors also note that this design yields a durability benefit: "our system can easily generate updated questions as web is self-updating consistently" ([Song & Zhao, n.d.](document_1.txt)).

## Contrast With Prior Work's Human-Labeling Burden

The significance of 106 to 163 templates becomes clearest against the alternative. Previous approaches to question generation from knowledge bases "relies on massive human-labeled data," and one such system trains a neural machine translation model on **10,000 ⟨triple, question⟩ pairs**, where "the question part of the 10,000 pairs are human generated, which requires a large amount of human effort" ([Song & Zhao, n.d.](document_1.txt)). A template set numbering in the low hundreds, augmented by automated web retrieval and filtering, therefore represents a qualitatively different and substantially smaller annotation burden than 10,000 individually authored questions — while the reported human evaluations indicate that quality did not suffer as a result.

## Evaluation Outcomes Associated With the Template Design

The human evaluation used three native English speakers rating both systems' outputs on a four-point scheme, where higher is better, on 500 random-selected Freebase triples ([Song & Zhao, n.d.](document_1.txt)).

| System | Grammaticality | Naturalness |
|---|---|---|
| Prior system (Serban et al., 2016, as cited in Song & Zhao, n.d.) | 3.36 | 3.14 |
| Ours | 3.53 | 3.31 |

The paper observes that naturalness scores fall below grammaticality scores for both systems because "naturalness is a more strict metric since a natural question should also be grammatical" ([Song & Zhao, n.d.](document_1.txt)). Separately, the domain-relevance evaluation method used in the pipeline was validated on the web snippet dataset, which contains 10,060 training and 2,280 test snippets across 8 classes, averaging 18 words each ([Song & Zhao, n.d.](document_1.txt)). The proposed method achieved **85.65 precision**, ahead of the reported baselines at **82.18**, **85.31**, and **85.48** ([Song & Zhao, n.d.](document_1.txt)). The authors attribute this to word embeddings capturing similarity between distinct words such as "finance" and "economy," a relationship they argue is harder for traditional topic-model approaches to represent ([Song & Zhao, n.d.](document_1.txt)).

## Limitations and Caveats

Three caveats qualify any answer to the template-count question. First, the power tool template figure is not reliably determined by the available record: 103 and 163 are both attested, and only the 103 figure supports the explicitly stated combined total of 209 ([Research note, n.d.](document_2.txt); [Song & Zhao, n.d.](document_1.txt)). Second, the primary paper's numerical text has sustained extraction damage, including garbled references and irregular digit spacing, which lowers confidence in any single isolated numeral drawn from it ([Song & Zhao, n.d.](document_1.txt)). Third, the template count is predicate-bounded rather than triple-bounded, so the figure scales with the diversity of relations in a knowledge base rather than with the number of facts to be covered; the 209 to 269 range therefore describes these two specific evaluations rather than a general-purpose template library. Finally, the reported system generates questions without answers, which the authors identify as the natural next step ("automatic answer mining as our future work") ([Song & Zhao, n.d.](document_1.txt)).

## Conclusion

The hand-crafted template requirement of this system is best expressed as three figures of differing reliability: **106 templates** for the Freebase evaluation, agreed upon by both sources ([Song & Zhao, n.d.](document_1.txt); [Research note, n.d.](document_2.txt)); **103 or 163 templates** for the in-house power tool knowledge base, depending on which source is credited ([Research note, n.d.](document_2.txt); [Song & Zhao, n.d.](document_1.txt)); and a reported **combined total of 209 templates** across both evaluations ([Research note, n.d.](document_2.txt)). Because template construction is explicitly the only human labor in the pipeline, these low-hundreds figures constitute the paper's core efficiency argument against prior systems trained on 10,000 human-authored question–triple pairs ([Song & Zhao, n.d.](document_1.txt)). The most defensible single answer to the query is therefore **209 hand-crafted templates**, understood as the reported total, with the understanding that the underlying power tool count and hence the true total may be higher.

## References

Research note. (n.d.). *Third-party research note: Question Generation from a Knowledge Base with Web Exploration* [document_2.txt].

Song, L., & Zhao, L. (n.d.). *Question Generation from a Knowledge Base with Web Exploration* [document_1.txt]. Computer Science Department, University of Rochester; Bosch Research and Technology Center.