# Hand-Crafted Question Templates in Song and Zhao's Knowledge-Based Question Generation System: A Detailed Count and Analysis

## 1. Purpose and Scope of This Report

This report answers a single, narrowly defined factual question — how many hand-crafted templates were required by the question-generation system described in Song and Zhao's work on generating questions from a knowledge base (KB) with web exploration — and situates that number within the broader design and evaluation of the system. Because the available source material contains two different figures for one of the two evaluation settings, this report does not simply restate a number. Instead, it reconstructs the template-construction effort from the primary paper, cross-checks it against a third-party research note summarising the same work, and explains which figure is the more defensible one. All substantive claims are drawn from the primary paper, *Question Generation from a Knowledge Base with Web Exploration* ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)), and from a summarising research note on the same work ([Third-party research note](document_2.txt)).

## 2. The Short Answer

Across the two evaluation settings reported in the paper, the authors hand-crafted **106 templates for the 500-triple Freebase evaluation** and **163 templates for their in-house power tool domain KB**, giving a **combined total of 269 hand-crafted templates** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A third-party research note on the same paper reports the second figure as 103 rather than 163, and consequently states a total of 209 ([Third-party research note](document_2.txt)). Section 5 of this report examines that discrepancy in detail and concludes that 163 — the figure that appears in the primary source — is the more reliable reading, making **269 the most defensible overall total**.

Table 1 summarises every template-related figure available in the source material.

**Table 1. Template construction in the two evaluation settings**

| Evaluation setting | Distinct predicates | Hand-crafted templates | Templates per predicate | Seed questions generated | Additional questions retrieved |
|---|---|---|---|---|---|
| Freebase (500 random triples) | 53 | 106 (primary source) | 2.00 | 991 | 1,529 (Google) |
| In-house power tool domain KB | 67 | 163 (primary source) / 103 (third-party note) | 2.43 / 1.54 | 12,228 | 20,000 (Google) |
| Combined | 120 | 269 (primary source) / 209 (third-party note) | — | 13,219 | 21,529 |

*Sources: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)).*

## 3. Template Construction as the Sole Human-Labour Component

The significance of the template counts depends on understanding what role templates play in the system. The paper states plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Everything else in the pipeline — seed question generation, iterative web expansion, fluency scoring and domain relevance filtering — is automated. The third-party note reaches the same conclusion, observing that "the paper states that the only human labor in this work is question template construction. The template construction therefore is the manual component reported" ([Third-party research note](document_2.txt)).

This matters because it means the template count is effectively a direct measure of human annotation cost for the entire system. Every question the system ultimately produces — more than 13,000 seed questions and more than 21,000 web-retrieved candidates across the two evaluations — traces back to a few hundred manually authored strings. The template count is therefore not a peripheral implementation detail; it is the principal cost metric of the approach.

Structurally, each template pairs a natural-language transcription of a KB predicate with placeholders for the subject and object. The paper describes templates that "consist of a transcription of the predicate in the KB (e.g. performsActivity = how to) and placeholders for the subject (#X#) and the object (#Y#)" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The worked example given is a template "how to use #X#" constructed for the predicate "performsActivity", which applied to the triple (jigsaw, performsActivity, CurveCut) yields the seed question "how to use jigsaw" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## 4. The Freebase Evaluation: 106 Templates

### 4.1 Predicate-Centred Design

For the first evaluation, the authors compared their end-to-end system with the previous state-of-the-art method of Serban et al. (2016) on **500 randomly selected triples from Freebase** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For those 500 triples they "hand-crafted 106 templates, as these triples share only 53 distinct predicates (we made 2 templates for each predicate on average)" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The arithmetic is exact: 106 templates divided by 53 predicates gives precisely two templates per predicate.

The third-party note corroborates these figures in full, recording that "the paper reports 106 hand-crafted templates for those 500 Freebase triples", that "the triples share only 53 distinct predicates, so the authors made 2 templates for each predicate on average", and it draws the design inference explicitly: "This design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-party research note](document_2.txt)).

### 4.2 From Templates to Seed Questions

Applying the 106 templates to the 500 triples produced **991 seed questions** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)). That is approximately 1.98 seed questions per input triple, or roughly 9.35 seed questions per template. The seed questions serve as the in-domain reference distribution against which later expanded questions are scored for domain relevance; the paper defines the domain relevance of an expanded question q as the cosine similarity between the question's document embedding and the centroid of the seed set, REL(q) = cos(v(q), u(D_in)) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

### 4.3 Web Expansion and Final Selection

Beyond the seed set, **1,529 additional questions were retrieved from Google** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)). To evaluate fluency, the authors trained a 4-gram language model on Gigaword (LDC2011T07) with Kneser–Ney smoothing, and used the averaged language model score, AVGLM(q) = LM(q)/LEN(q), as a ranking index to select the top 500 questions for comparison ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Thus the entire 500-triple Freebase experiment — 991 seed questions plus 1,529 retrieved candidates plus the final ranked comparison set — rests on 106 manually written templates.

## 5. The Power Tool Domain KB: 163 or 103 Templates?

### 5.1 The Primary Source Figure

The final experiment ran the full system on a highly specialised in-house KB in the power tool domain. The paper reports that this KB "contains 67 distinct predicates, 293 distinct subjects and 279 distinct objects respectively", and then states: "For the 67 predicates, we hand-crafted 163 templates" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This yields approximately 2.43 templates per predicate, which is slightly higher than the Freebase ratio of 2.00 per predicate — a plausible outcome for a more specialised domain where a single predicate may require several natural-language phrasings.

### 5.2 The Third-Party Figure and Its Implications

The third-party note records a different number: "For the 67 predicates, the authors hand-crafted 103 templates", and then states that "together with the 106 Freebase templates, the authors wrote 209 templates in total" ([Third-party research note](document_2.txt)). This conflicts with the primary source, which gives 163.

Two observations are relevant. First, the third-party note elsewhere reproduces the paper's other figures accurately — 500 triples, 106 templates, 53 distinct predicates, 991 seed questions, 1,529 Google-retrieved questions — which suggests a transcription error rather than a systematic misreading ([Third-party research note](document_2.txt)). Second, the numerals "163" and "103" differ by a single digit in the tens place, which is consistent with a digit-substitution typographical error.

Because the primary paper is the authoritative source for its own experimental configuration, and because the third-party note explicitly frames itself as reporting what "the paper reports" ([Third-party research note](document_2.txt)), the primary figure of **163** should be preferred, and the derived total should be **269** rather than 209. This is the position taken throughout the remainder of this report, with the alternative figure noted wherever relevant.

### 5.3 Seed and Expanded Questions in the Domain-Specific Setting

Regardless of which template count is accepted, the domain-specific experiment produced the largest question volumes in the study. The authors "generate 12,228 seed questions from which 20,000 more questions are expanded with Google" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The system used the same language model as the first experiment, plus a skip-gram model trained on Wikipedia for evaluating domain relevance ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The qualitative output was favourable. The paper presents expanded questions such as "how to change circular saw blade", "how does an oscillating multi tool work", "how to measure lawnmower cutting height", and "how to sharpen drill bits on bench grinder", noting that most are grammatical and relevant to the power tool domain ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The authors also observe that most questions are informative and correspond to a specific answer, with the exception of "do I need a hammer drill", which "lacks context information", and they highlight the system's capacity to generate more complex questions such as "how to cut a groove in wood without a router" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## 6. Why So Few Templates? The Authors' Rationale

The paper offers two explicit reasons why a large template inventory is unnecessary. First, "the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions"; second, "multiple entities in the KB share the same predicates" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A third advantage is stated as well: the system "can easily generate updated questions as web is self-updating consistently" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The empirical data support the first point strongly. The 106 Freebase templates produced 991 seed questions and 1,529 web-retrieved candidates, and the 163 power-tool templates produced 12,228 seed questions and 20,000 expanded questions ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). In other words, roughly 269 templates of manual effort generated over 34,000 questions across the two settings — a leverage ratio on the order of 128 questions per template.

## 7. Context: Human Effort Relative to Prior Work

The template counts acquire their full meaning only when compared with the alternative approach the authors target. Serban et al. (2016) trained a neural machine translation system "with 10,000 (triple, question) pairs", and "the question part of the 10,000 pairs are human-generated, which requires a large amount of human effort" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The paper further notes that in that prior work "the grammaticality and naturalness of generated questions cannot be guaranteed" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

**Table 2. Manual authoring effort: template-based approach versus prior work**

| Approach | Manual artefacts authored | Scale of manual effort |
|---|---|---|
| Serban et al. (2016) | 10,000 human-generated (triple, question) pairs | Large |
| Song & Zhao (2017) — Freebase | 106 templates | Small |
| Song & Zhao (2017) — power tool KB | 163 templates | Small |
| Song & Zhao (2017) — combined | 269 templates | Small |

*Sources: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)).*

The comparison is the core claim of the paper: the system "significantly reduces the human effort by leveraging the massive web resources" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). On the reported numbers, the reduction is from 10,000 manually authored questions to 269 manually authored templates — roughly a 97 percent reduction in discrete manual authoring units, while the templates themselves remain reusable across all entities sharing a predicate.

## 8. Quality Outcomes Associated with the Template Design

Reduced annotation effort would be a hollow result if quality degraded. The evidence points the other way.

In the Freebase comparison, three native English speakers evaluated fluency and naturalness on a four-point scheme where 4 is best. The authors' system scored **3.53 for grammaticality and 3.31 for naturalness**, against **3.36 and 3.14** respectively for Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The paper notes that the naturalness score is lower than the grammaticality score for both methods because naturalness is the stricter metric — "a natural question should also be grammatical" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The domain-relevance evaluation was validated separately on the web snippet dataset, comprising 10,060 training and 2,280 test snippets in eight classes, with an average of 18 words per snippet ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The method achieved **85.65 percent precision**, compared with 82.18 percent for Phan et al. (2008), 85.31 percent for Ma et al. (2015) and 85.48 percent for Chen et al. (2011) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

**Table 3. Reported evaluation outcomes**

| Metric | Song & Zhao (2017) | Comparator |
|---|---|---|
| Grammaticality (4-point, human) | 3.53 | 3.36 (Serban et al., 2016) |
| Naturalness (4-point, human) | 3.31 | 3.14 (Serban et al., 2016) |
| Domain-classification precision | 85.65% | 85.48% (Chen et al., 2011) |

*Source: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).*

## 9. Assessment and Conclusion

The direct answer to the question is that the authors hand-crafted **106 templates for the Freebase evaluation** and **163 templates for the power tool domain KB**, for a **combined total of 269 templates** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A third-party summary of the same paper records 103 templates for the power tool domain and a total of 209 ([Third-party research note](document_2.txt)); on the evidence available, that figure appears to be a transcription error, since the primary source's other numbers are reproduced accurately in the same note and the discrepancy is limited to a single digit.

My assessment is that the template counts should be read as the study's central cost claim rather than as an implementation footnote. The paper is explicit that template construction is the only human labour in the pipeline ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)), and the counts — 106 and 163, or 269 in aggregate — are therefore the complete measure of manual authoring required to generate over 34,000 questions in two separate domains. Set against the 10,000 human-written question–answer pairs used by Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)), the approach's efficiency argument is quantitatively grounded rather than merely asserted.

Two caveats are warranted and are visible in the source material itself. First, the templates are predicate-bound: because template creation "follows the predicates present in the KB" ([Third-party research note](document_2.txt)), the manual effort scales with predicate coverage rather than with the number of triples or entities, which explains why 500 Freebase triples required only 53 predicates' worth of templates. Scope expansion into new KBs with new predicates would incur new authoring cost. Second, the evaluation of quality rests on human raters — three native English speakers in the Freebase study ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)) — so the fluency and naturalness advantages reported in Table 3 are judgements rather than fully objective measurements. Within those limits, however, the template counts are unambiguous in the primary source: **106, 163, and 269 in total**.

## References

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). https://arxiv.org/abs/1610.03807

Third-party research note: *Question generation from a knowledge base with web exploration* [Unpublished research note]. (document_2.txt)