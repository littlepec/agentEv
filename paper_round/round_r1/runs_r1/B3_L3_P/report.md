# How Many Hand-Crafted Templates Were Required? Evidence from "Question Generation from a Knowledge Base with Web Exploration"

## Direct Answer to the Query

The short answer is that the reported number depends on which knowledge base (KB) evaluation is being discussed, and on which source is consulted. According to the primary paper itself, the authors hand-crafted **106 templates** for the Freebase evaluation and **163 templates** for the in-house power tool domain KB, for a combined total of **269 hand-crafted templates** across both evaluations ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A third-party research note summarizing the same work reports a different figure for the domain-specific KB — **103 templates** rather than 163 — which would put the combined total at **209 templates** ([Research Note, n.d.](document_2.txt)). This discrepancy is material and is examined in detail below, but the headline figure from the primary source is 106 (Freebase) plus 163 (power tool), i.e. **269 templates in total**, with template construction described as "the only human labor in this work" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The remainder of this report situates those numbers within the system's architecture, explains why the template count is deliberately kept small relative to the number of generated questions, and flags the inconsistency between the two available sources.

## Why Templates Are the Central Manual Component

Question generation from a KB is defined in the paper as the task of generating questions related to the domain of the input KB ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The authors identify a specific difficulty: "function words and morphological forms for entities are abstracted away when a KB is created," so a triple such as ⟨jigsaw, performsActivity, CurveCut⟩ does not by itself surface the surface-form phrasing that a natural question would require.

Prior work addressed this through massive human-labeled data. Specifically, earlier neural machine translation (NMT) approaches trained on **10,000 ⟨triple, question⟩ pairs**, in which "the question part of the 10,000 pairs are human generated, which requires a large amount of human effort" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The system under review deliberately inverts this trade-off: rather than labeling ten thousand pairs, the authors hand-craft a small set of templates and then exploit the web to expand coverage.

This is why the template count answers a question that is really about the total human cost of the system. The paper states plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The template count is therefore not a minor implementation detail; it is the principal measure of the annotation burden the method imposes.

## How the Templates Are Constructed and Used

Each template is associated with a **predicate** in the KB. Template creation therefore follows the predicates present in the KB, rather than the entities or the triples. A template consists of a transcription of the predicate plus placeholders for the subject (#X#) and the object (#Y#). The paper's worked example is predicate *performsActivity* → template "how to use #X#", which applied to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question "how to use jigsaw" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The system comprises four sub-modules: question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The templates feed only the first two of these. Expansion is performed by iteratively submitting already-obtained questions as queries to a standard search engine and harvesting related question candidates, which are added to the expanded set only if not already present; the loop is bounded by a maximum iteration count, *I<sub>max</sub>* ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Selection then filters candidates by fluency and domain relevance, using a skip-gram model for relevance and a language model for fluency, with thresholds *t<sub>rel</sub>* and *t<sub>flu</sub>* ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Reported Template Counts by Knowledge Base

### Freebase evaluation (domain-general KB)

The Freebase experiment used **500 randomly selected triples**. Those triples shared only **53 distinct predicates**, and the authors hand-crafted **106 templates** for them — "2 templates for each predicate on average." Applying the templates to the triples produced **991 seed questions**, and a further **1,529 questions** were retrieved from Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note independently confirms these Freebase figures: 500 triples, 106 templates, 53 distinct predicates, approximately two templates per predicate, 991 seed questions, and 1,529 questions retrieved from Google ([Research Note, n.d.](document_2.txt)).

### In-house power tool domain KB

The domain-specific evaluation ran on an in-house KB in the power tool domain containing **67 distinct predicates**, **293 distinct subjects**, and **279 distinct objects** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Here the two sources diverge:

- The primary paper states: "For the 67 predicates, we hand-craft **163** templates" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).
- The third-party note states: "For the 67 predicates, the authors hand-crafted **103** templates" and adds that "together with the 106 Freebase templates, the authors wrote **209** templates in total" ([Research Note, n.d.](document_2.txt)).

From this KB, **12,228 seed questions** were generated, from which **20,000 more questions** were expanded with Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

### Aggregate totals

| Knowledge base | Distinct predicates | Hand-crafted templates | Templates per predicate | Seed questions generated | Web-retrieved questions |
|---|---|---|---|---|---|
| Freebase (500 triples) | 53 | 106 | ~2.0 | 991 | 1,529 |
| In-house power tool KB | 67 | **163** (primary source) | ~2.4 | 12,228 | 20,000+ |
| **Total (primary source)** | **120** | **269** | — | **13,219** | **21,529+** |
| In-house power tool KB (alternative) | 67 | **103** (third-party note) | ~1.5 | 12,228 | 20,000+ |
| **Total (third-party note)** | **120** | **209** | — | **13,219** | **21,529+** |

Sources: ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)); ([Research Note, n.d.](document_2.txt)).

### Assessing the discrepancy

The two documents disagree by exactly 60 templates on the power tool KB (163 vs. 103), and consequently by 60 on the combined total (269 vs. 209). Three observations are relevant.

First, the primary source should generally be preferred over a summarizing secondary note when the two conflict, because the primary source is the artifact in which the authors themselves report their experimental configuration. On that basis, **269 hand-crafted templates in total** (106 + 163) is the better-supported figure.

Second, the third-party note's internal arithmetic is consistent: 106 + 103 = 209, and it explicitly describes the 209 figure as the total "reported in the template-construction experiment" ([Research Note, n.d.](document_2.txt)). The note is not sloppy in its own terms; it simply appears to have transcribed or interpreted the power tool count differently.

Third, both sources agree on the structural principle that drives the count: the third-party note states that "template creation follows the predicates present in the KB" and that "the manual template-building effort scales with predicate coverage in each evaluation," while the paper states that "multiple entities in the KB share the same predicates" ([Research Note, n.d.](document_2.txt); [Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The disagreement is confined to the magnitude of one number, not to the mechanism behind it.

## Why the Template Count Is Small Relative to the Output

The paper offers an explicit justification for why the system "does not require a large number of templates," resting on two claims: (1) iterative question expansion can produce a large number of questions even from a relatively small seed set, and (2) multiple entities in the KB share the same predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The reported numbers substantiate both claims. In the Freebase setting, 106 templates produced 991 seed questions — a seed-to-template ratio of roughly 9.3 questions per template — and expansion then more than doubled the pool by adding 1,529 web-retrieved questions. In the power tool setting, 12,228 seed questions were produced from a template set in the 103–163 range, a ratio between roughly 75 and 119 seed questions per template, and expansion added a further 20,000 questions. The marginal human cost of additional questions is therefore zero once templates exist; the marginal cost falls entirely on automated search and filtering.

A secondary advantage the authors claim is currency: "our system can easily generate updated questions as web is self-updating consistently" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Templates tied to predicates are comparatively stable artifacts, while the web supplies the updatable surface variation.

## Validation Context

The human evaluation used three native English speakers rating fluency and naturalness on a 4-point scale, on 500 randomly selected Freebase triples ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The results were:

| System | Grammaticality | Naturalness |
|---|---|---|
| Prior state of the art (Serban et al., 2016) | 3.36 | 3.14 |
| Ours | **3.53** | **3.31** |

Source: ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The paper notes that naturalness scores are lower than grammaticality scores for both systems because naturalness is a stricter criterion — a natural question should also be grammatical ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Qualitative examples of the baseline's failures include ungrammatical output ("who was someone who was involved in the leukemia ?"), unnatural phrasing ("what 's one of the mountain where can you found in argentina in netflix ?"), and confusing constructions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Separately, the domain-relevance component was validated on the web snippet dataset — 10,060 training and 2,280 test snippets across 8 classes, averaging 18 words each — where the proposed method achieved **85.65** precision against 82.18, 85.31, and 85.48 for three prior methods ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Limitations of This Assessment

Three caveats bear on how confidently the template figures can be stated. First, the supplied text is an OCR-derived rendering of the paper, and digits are sometimes separated by spaces (for example, "1 0 6" and "1 6 3"), which introduces some risk of transcription ambiguity around exactly the numbers at issue. Second, the OCR consistently renders the baseline system as "? )"; the reference list and the experiments section identify this as Serban et al. (2016) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Third, and most importantly, the 163-versus-103 conflict cannot be resolved from the materials provided; a reader requiring a single authoritative figure should consult the published version of the paper directly.

## Conclusion

The reported human template-construction effort is **106 hand-crafted templates for the Freebase evaluation** and either **163 (per the paper) or 103 (per the third-party note) templates for the in-house power tool domain KB** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Research Note, n.d.](document_2.txt)). The best-supported combined total is therefore **269 templates** (106 + 163), with **209** (106 + 103) as the alternative implied by the secondary source. Because template construction is the only manual component in the pipeline, these counts represent essentially the entire human annotation cost of the system — a stark contrast to the 10,000 human-generated ⟨triple, question⟩ pairs required by the NMT-based prior art the paper compares against ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). That reduction, rather than the raw template number, is the paper's central efficiency claim, and it is what enables 13,219 seed questions and over 21,000 web-expanded questions to be produced from roughly two hundred to three hundred manual artifacts.

## References

Research Note. (n.d.). *Third-party research note: Question Generation from a Knowledge Base with Web Exploration* [Unpublished research note]. document_2.txt.

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration*. arXiv. https://arxiv.org/abs/1610.03807