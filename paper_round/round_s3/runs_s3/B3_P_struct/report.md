# How Many Hand-Crafted Templates Were Required? An Analysis of Question Generation from a Knowledge Base with Web Exploration

## Introduction

Question generation from a knowledge base (KB) is a challenging natural language processing task because KBs abstract away the function words and morphological forms that are necessary for fluent, natural questions ([Song & Zhao, 2016](document_1.txt)). The system proposed by Song and Zhao (2016) addresses this challenge by combining a small set of hand-crafted templates with iterative web exploration, thereby reducing the amount of human-labeled data required compared to previous neural machine translation approaches that rely on 10,000 human-generated question-triple pairs ([Song & Zhao, 2016](document_1.txt)). The only manual component of this system is the construction of question templates, which are associated with predicates in the KB ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Consequently, the question of how many hand-crafted templates were necessary is central to evaluating the system’s practical effort and scalability.

This report examines the reported template counts from the primary paper excerpt and an accompanying third-party research note. It finds that the number depends on the evaluation setting: 106 templates were hand-crafted for the Freebase evaluation, and either 163 or 103 templates were hand-crafted for the domain-specific power tool KB, depending on the source. Based on the primary source, the total across both reported evaluations is 269 hand-crafted templates. However, the third-party note states a total of 209. This report analyzes the discrepancy and argues that the primary source’s figure of 163 for the power tool domain is more reliable, yielding a total of 269.

## The Role of Hand-Crafted Templates in the System

The proposed system first constructs a small set of question templates, each associated with a predicate in the input KB ([Song & Zhao, 2016](document_1.txt)). A template consists of a transcription of the predicate (e.g., `performsActivity` becomes “how to”) and placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2016](document_1.txt)). For example, the template “how to use #X#” is constructed for the predicate `performsActivity`, and applying it to the triple `⟨jigsaw, performsActivity, CurveCut⟩` yields the seed question “how to use jigsaw” ([Song & Zhao, 2016](document_1.txt)). These seed questions are then expanded by iteratively using already-obtained questions as search queries in a standard search engine such as Google or Bing ([Song & Zhao, 2016](document_1.txt)). Finally, questions are selected by estimating their fluency and domain relevance ([Song & Zhao, 2016](document_1.txt)).

The paper explicitly states that “the only human labor in this work is the question template construction” ([Song & Zhao, 2016](document_1.txt)). The system does not require a large number of templates because iterative question expansion can produce a large number of questions even from a relatively small number of seed questions, and because multiple entities in the KB share the same predicates ([Song & Zhao, 2016](document_1.txt)). This design keeps the manual template-building effort compact relative to the KB size ([Third-party research note, n.d.](document_2.txt)).

## Reported Template Counts: Freebase Evaluation

For the Freebase evaluation, the authors randomly selected 500 triples from Freebase ([Song & Zhao, 2016](document_1.txt)). These triples shared only 53 distinct predicates, and the authors hand-crafted 106 templates for them, which corresponds to an average of approximately two templates per predicate ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Applying these templates to the triples generated 991 seed questions, and an additional 1,529 questions were retrieved from Google ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The template count for the Freebase evaluation is thus consistently reported as 106 across both sources.

### Table 1: Freebase Evaluation Template and Question Counts

| Metric | Value | Source |
|---|---:|---|
| Randomly selected triples | 500 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Distinct predicates | 53 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Hand-crafted templates | 106 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Average templates per predicate | ~2 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Seed questions generated | 991 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Additional questions retrieved from Google | 1,529 | ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |

## Reported Template Counts: Domain-Specific Power Tool KB

The second evaluation used an in-house KB in the power tool domain. This KB contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](document_1.txt)). For the 67 predicates, the primary source reports that the authors hand-crafted 163 templates ([Song & Zhao, 2016](document_1.txt)). However, the third-party research note states that the authors hand-crafted 103 templates for the same 67 predicates and that together with the 106 Freebase templates, the authors wrote 209 templates in total ([Third-party research note, n.d.](document_2.txt)). This is a direct contradiction that must be examined carefully.

### Table 2: Power Tool Domain Template Counts Under Two Sources

| Metric | Primary Source Count | Third-Party Note Count |
|---|---:|---:|
| Distinct predicates | 67 | 67 |
| Hand-crafted templates | 163 | 103 |
| Average templates per predicate | ~2.43 | ~1.54 |
| Source | ([Song & Zhao, 2016](document_1.txt)) | ([Third-party research note, n.d.](document_2.txt)) |

Using the same language model as in the Freebase experiment, the authors generated 12,228 seed questions from the power tool KB and expanded 20,000 additional questions with Google ([Song & Zhao, 2016](document_1.txt)). The expanded questions were reported to be mostly grammatical and relevant to the power tool domain, with examples such as “how to change circular saw blade,” “how to measure lawn mower cutting height,” “how to sharpen drill bits on bench grinder,” and “how to cut a groove in wood without a router” ([Song & Zhao, 2016](document_1.txt)). The system also generated complex questions beyond simple factoids, although one example, “do I need a hammer drill,” was noted as lacking context information ([Song & Zhao, 2016](document_1.txt)).

## Total Template Construction Effort

If the primary source is followed, the total number of hand-crafted templates across the two reported evaluations is 106 (Freebase) + 163 (power tool) = 269 templates ([Song & Zhao, 2016](document_1.txt)). If the third-party note is followed, the total is 106 + 103 = 209 templates ([Third-party research note, n.d.](document_2.txt)). The third-party note explicitly claims that “together with the 106 Freebase templates, the authors wrote 209 templates in total” and that “the paper reports this total in the template-construction experiment” ([Third-party research note, n.d.](document_2.txt)). However, the primary paper excerpt does not contain a statement of 209 total templates; it only reports 106 for Freebase and 163 for the power tool domain ([Song & Zhao, 2016](document_1.txt)).

### Table 3: Total Template Counts Under Two Interpretations

| Evaluation Setting | Primary Source Total | Third-Party Note Total |
|---|---:|---:|
| Freebase | 106 | 106 |
| Power tool domain | 163 | 103 |
| **Total** | **269** | **209** |
| Source | ([Song & Zhao, 2016](document_1.txt)) | ([Third-party research note, n.d.](document_2.txt)) |

My concrete, valid opinion is that the primary source’s figure of 163 for the power tool domain is more likely correct, making 269 the most defensible total across the two evaluations. This judgment rests on three considerations. First, the primary source is the original paper excerpt, whereas the third-party note is a secondary summary that may contain transcription or interpretive errors. Second, the arithmetic in the third-party note—106 + 103 = 209—is internally consistent, but it depends entirely on the 103 figure, which conflicts with the primary source. Third, the average templates per predicate under the primary source is approximately 2.43, while under the third-party note it is approximately 1.54. Given that the Freebase evaluation averaged roughly 2 templates per predicate, a higher average for the more specialized power tool domain is plausible because domain-specific predicates may require more nuanced question formulations. Therefore, I conclude that the authors hand-crafted 106 templates for Freebase and 163 templates for the power tool domain, for a total of 269 hand-crafted templates across the two evaluations.

## Resolving the Discrepancy

The discrepancy between 163 and 103 is significant because it changes the total manual effort by 60 templates. The third-party note states that “for the 67 predicates, the authors hand-crafted 103 templates” and that the total is 209 ([Third-party research note, n.d.](document_2.txt)). The primary source states that “for the 67 predicates, we hand-craft 163 templates” ([Song & Zhao, 2016](document_1.txt)). One possible explanation is a typographical or optical character recognition error: “163” might have been misread as “103” in the third-party note. Another possibility is that the third-party note refers to a different version of the paper or a different subset of templates. However, the third-party note explicitly ties its total to the same 106 Freebase templates and the same 67 predicates, which suggests it is attempting to report the same experiment ([Third-party research note, n.d.](document_2.txt)). Without access to the full published paper, the primary source excerpt remains the stronger evidence.

This discrepancy also highlights a broader methodological issue: template counts are tied to specific predicate sets and KBs. The Freebase evaluation used 53 predicates and 106 templates, while the power tool evaluation used 67 predicates and either 163 or 103 templates ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The manual effort therefore scales with predicate coverage, not with the number of triples alone. For Freebase, 500 triples shared only 53 predicates, so the template set remained compact relative to the triple set ([Third-party research note, n.d.](document_2.txt)). For the power tool KB, the 67 predicates required their own template set, and the effort was correspondingly higher ([Song & Zhao, 2016](document_1.txt)).

## Methodological Context and Implications

The template counts must be understood within the system’s overall design. The authors compare their system with previous work that trains a neural machine translation (NMT) system on 10,000 human-generated question-triple pairs ([Song & Zhao, 2016](document_1.txt)). That approach requires a massive amount of human-labeled data and does not guarantee grammaticality or naturalness ([Song & Zhao, 2016](document_1.txt)). In contrast, the proposed system relies on a small number of hand-crafted templates and leverages web resources for expansion and selection ([Song & Zhao, 2016](document_1.txt)). The human effort is thus concentrated in template construction, making the template count a direct measure of manual labor.

The quality of the generated questions was evaluated by human graders. For the Freebase experiment, three native English speakers rated fluency and naturalness on a 4-point scale. The proposed system achieved a grammaticality score of 3.53 and a naturalness score of 3.31, compared with 3.36 and 3.14 for the baseline system ([Song & Zhao, 2016](document_1.txt)). These results suggest that even a relatively small template set, combined with web exploration and selection, can produce questions that are more fluent and natural than those from a system trained on 10,000 human-labeled pairs ([Song & Zhao, 2016](document_1.txt)).

The domain-specific evaluation further demonstrates the system’s scalability. From 12,228 seed questions, the system expanded 20,000 additional questions with Google, and most were grammatical and relevant to the power tool domain ([Song & Zhao, 2016](document_1.txt)). This expansion is possible because multiple entities share the same predicates, so a modest set of templates can cover many triples ([Song & Zhao, 2016](document_1.txt)). The system also benefits from the web’s self-updating nature, allowing it to generate updated questions over time ([Song & Zhao, 2016](document_1.txt)).

## Limitations and Future Considerations

The reported template counts are specific to the two evaluations described. The Freebase evaluation used 500 randomly selected triples and 53 distinct predicates, while the power tool evaluation used an in-house KB with 67 predicates, 293 subjects, and 279 objects ([Song & Zhao, 2016](document_1.txt)). The total of 269 templates (under the primary source interpretation) therefore does not represent a universal requirement for all KBs. Larger KBs with more predicates would likely require more templates, though the system’s iterative expansion could still reduce the per-predicate effort ([Song & Zhao, 2016](document_1.txt)).

The discrepancy between the primary source and the third-party note also underscores the importance of verifying figures against original publications. Secondary summaries can introduce errors that affect conclusions about effort and scalability. Future work could report template counts alongside predicate coverage and seed question counts to allow more precise comparisons across systems. Additionally, the authors note that the only human labor is template construction, so reducing this effort further—perhaps through automatic template induction—could make the system even more efficient ([Song & Zhao, 2016](document_1.txt)).

## Conclusion

The question “How many hand-crafted templates did they have to make?” has a multi-part answer. For the Freebase evaluation, the authors hand-crafted 106 templates for 500 triples covering 53 distinct predicates ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). For the domain-specific power tool KB, the primary source reports 163 templates for 67 predicates, while the third-party note reports 103 templates ([Song & Zhao, 2016](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Based on the primary source, the total across both evaluations is 269 hand-crafted templates. Based on the third-party note, the total is 209. In my assessment, the primary source’s figure of 163 for the power tool domain is more reliable, making 269 the most defensible total. The template count reflects the only manual component of the system, and the authors’ design demonstrates that a relatively small number of templates—when combined with iterative web exploration and fluency/relevance selection—can generate a large, high-quality set of questions from a KB ([Song & Zhao, 2016](document_1.txt)).

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). Retrieved from document_1.txt

Third-party research note. (n.d.). *Question generation from a knowledge base with web exploration*. Retrieved from document_2.txt