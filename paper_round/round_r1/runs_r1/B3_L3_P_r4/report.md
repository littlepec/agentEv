# How Many Hand-Crafted Question Templates Were Required? Evidence from "Question Generation from a Knowledge Base with Web Exploration"

## Direct Answer to the Query

The system described in "Question Generation from a Knowledge Base with Web Exploration" required **106 hand-crafted question templates for its Freebase evaluation** and a further set for its in-house power tool domain knowledge base — reported as **163 templates** in the primary document text and as **103 templates** in the third-party research note, which places the combined total at **209 templates** ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The safest single reading of the evidence is therefore that the authors wrote on the order of **200–270 hand-crafted templates in total**, split across two knowledge bases, and that template construction was explicitly identified as **the only human labor in the entire system** ([Song & Zhao, n.d.](document_1.txt)).

The remainder of this report explains what these templates are, how the counts break down by evaluation setting, why the figures are so small relative to the volume of questions produced, and where the source record is internally inconsistent.

## Background: What Counts as a "Hand-Crafted Template"?

### Predicate-Level Mapping

The templates are not arbitrary question strings. Each template is **associated with a single predicate** in the knowledge base, and the template set is built by walking the predicates present in the KB ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). A template "consists of a transcription of the predicate in the KB (e.g., performsActivity ⇒ how to)" together with slots for the arguments of the triple ([Song & Zhao, n.d.](document_1.txt)).

### Placeholder Structure

Concretely, each template contains **placeholders for the subject (#X#) and the object (#Y#)** of a KB triple ([Song & Zhao, n.d.](document_1.txt)). The worked example given in the paper is the predicate `performsActivity`, for which the template "how to use #X#" is constructed; applying it to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question "how to use jigsaw" ([Song & Zhao, n.d.](document_1.txt)). Because placeholders absorb the entities, a single template can service every triple that instantiates the same predicate — a point the authors make explicitly when arguing that large template inventories are unnecessary ([Song & Zhao, n.d.](document_1.txt)).

## Reported Template Counts by Evaluation Setting

### Freebase (Domain-General Knowledge Base)

The Freebase experiment used **500 randomly selected triples** ([Song & Zhao, n.d.](document_1.txt)). Those 500 triples shared only **53 distinct predicates**, and the authors hand-crafted **106 templates** for them — "2 templates for each predicate on average" ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Applying the templates to the triples produced **991 seed questions**, and a further **1,529 questions were retrieved from Google** ([Song & Zhao, n.d.](document_1.txt)).

### In-House Power Tool Domain Knowledge Base

The domain-specific evaluation ran on an in-house KB in the **power tool domain**, containing **67 distinct predicates, 293 distinct subjects, and 279 distinct objects** ([Song & Zhao, n.d.](document_1.txt)). Here the two source documents diverge:

- The **primary document text** states: "For the 67 predicates, we hand-craft **163** templates" ([Song & Zhao, n.d.](document_1.txt)).
- The **third-party research note** states that "the authors hand-crafted **103** templates" and that "together with the 106 Freebase templates, the authors wrote **209 templates in total**" ([Third-party research note, n.d.](document_2.txt)).

Both statements are preserved verbatim in the supplied materials, and the report below treats the discrepancy openly rather than silently resolving it (see the next subsection).

### Conflicting Figures in the Source Record

The inconsistency matters for anyone quoting a headline number. The primary document is an OCR-derived rendering in which digits are routinely split (for example, "1 0,0 0 0" for 10,000 and "5 0 0" for 500), so a numeral rendered as "1 6 3" is most plausibly read as 163 ([Song & Zhao, n.d.](document_1.txt)). The third-party note, by contrast, presents a self-consistent arithmetic chain: 106 + 103 = 209 ([Third-party research note, n.d.](document_2.txt)). Depending on which figure is accepted, the grand total across both KBs is either **209** or **269 templates**.

**Table 1. Reported hand-crafted template counts**

| Evaluation setting | Distinct predicates | Templates reported | Templates per predicate | Source |
|---|---|---|---|---|
| Freebase (500 triples) | 53 | 106 | 2.00 (stated) | ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Power tool KB (in-house) | 67 | 163 (primary text) | ~2.43 | ([Song & Zhao, n.d.](document_1.txt)) |
| Power tool KB (in-house) | 67 | 103 (third-party note) | ~1.54 | ([Third-party research note, n.d.](document_2.txt)) |
| **Combined (reading A)** | 120 | **269** | — | Derived from ([Song & Zhao, n.d.](document_1.txt)) |
| **Combined (reading B)** | 120 | **209** | — | ([Third-party research note, n.d.](document_2.txt)) |

## Why the Template Inventory Is Deliberately Small

### Reuse Across Entities That Share Predicates

The authors justify the compact template set on two grounds. First, "multiple entities in the KB share the same predicates," so one template covers many triples ([Song & Zhao, n.d.](document_1.txt)). Second, "the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions" ([Song & Zhao, n.d.](document_1.txt)). Template construction therefore scales with **predicate coverage**, not with triple count or entity count — which is precisely what the Freebase numbers show: 106 templates cover 500 triples because those triples collapse onto 53 predicates ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

### Template Volume Versus Output Volume

The arithmetic gap between templates and outputs is substantial. Dividing reported seed-question totals by reported template counts yields the following derived ratios (calculations are the author's own, based on figures in the cited documents).

**Table 2. Derived seed-question yield per template**

| Setting | Templates | Seed questions | Seed questions per template (derived) |
|---|---|---|---|
| Freebase | 106 | 991 | ~9.35 |
| Power tool (reading A) | 163 | 12,228 | ~75.0 |
| Power tool (reading B) | 103 | 12,228 | ~118.7 |

Seed counts are from ([Song & Zhao, n.d.](document_1.txt)). The power tool experiment also expanded roughly **20,000 additional questions with Google** on top of the 12,228 seed questions ([Song & Zhao, n.d.](document_1.txt)).

### Search-Engine Expansion

The seed question set is "further expanded through a search engine (e.g., Google, Bing), by iteratively forming each generated question as a search query to retrieve more related question candidates" ([Song & Zhao, n.d.](document_1.txt)). Algorithm 1 formalizes this: the expanded set *E* is initialized to the seed set *S*, a queue *Q* is populated with the seeds, and the loop repeatedly pops a question, calls `WebExp` on it, and appends unseen results to *E* and *Q* until either the queue empties or the iteration cap *I*max is reached ([Song & Zhao, n.d.](document_1.txt)). Expansion is therefore the mechanism that converts a few hundred hand-written patterns into tens of thousands of candidate questions.

### Web Self-Updating

A secondary benefit claimed for the design is currency: "our system can easily generate updated questions as web is self-updating consistently" ([Song & Zhao, n.d.](document_1.txt)). Hand-authored templates do not need revision to reflect changing phrasing on the web, because the expansion stage re-samples language from live search results.

## Template Construction as the Sole Human Labor

The paper is unambiguous on the labor accounting: "The only human labor in this work is the question template construction" ([Song & Zhao, n.d.](document_1.txt)). The third-party note restates the same point, describing template construction as "the manual component reported" ([Third-party research note, n.d.](document_2.txt)). Everything downstream — seed generation, web expansion, fluency scoring, and relevance filtering — is automated.

The contrast with the neural machine translation baseline is the crux of the argument. Prior work treats question generation as translation and trains an NMT system on **10,000 ⟨triple, question⟩ pairs**, where "the question part of the 10,000 pairs are human generated, which requires a large amount of human effort" ([Song & Zhao, n.d.](document_1.txt)). Against that benchmark, roughly 209–269 templates is a small manual investment.

## Selection: How the Expanded Pool Is Filtered

Volume alone would be counterproductive, since "the questions collected from the web search engine may not be fluent or domain relevant; especially the domain relevance drops significantly as the iteration goes on" ([Song & Zhao, n.d.](document_1.txt)). Two automated filters address this.

- **Domain relevance.** The seed question set serves as in-domain data *D*in, and relevance is the cosine similarity between the embedding of a candidate question and the embedding of *D*in: Rel(q) = cos(v(q), v(D_in)), where v(·) is a document embedding formed by averaging word embeddings ([Song & Zhao, n.d.](document_1.txt)). A skip-gram model supplies the word vectors ([Song & Zhao, n.d.](document_1.txt)).
- **Fluency.** The averaged language model score is AvgLM(q) = Lm(q) / Len(q), where Lm(·) is the general-domain log-probability and Len(·) is the word count ([Song & Zhao, n.d.](document_1.txt)). A 4-gram model trained on Gigaword with Kneser-Ney smoothing was used for the Freebase experiment ([Song & Zhao, n.d.](document_1.txt)).

Thresholds *t*rel and *t*flu remove candidates scoring below either bound ([Song & Zhao, n.d.](document_1.txt)). This filtering is what allows a small template set to remain the sole manual input without sacrificing output quality.

## Evaluation Outcomes Associated with the Template Design

Three native English speakers rated the output of the proposed system and the baseline on a 4-point scheme, where 4 is best ([Song & Zhao, n.d.](document_1.txt)). The naturalness score is lower than the grammaticality score for both systems because "naturalness is a more strict metric since a natural question should also be grammatical" ([Song & Zhao, n.d.](document_1.txt)).

**Table 3. Human ratings (4-point scale)**

| System | Grammaticality | Naturalness |
|---|---|---|
| Baseline "?" | 3.36 | 3.14 |
| Ours | **3.53** | **3.31** |

Source: ([Song & Zhao, n.d.](document_1.txt)).

The domain-relevance component was separately validated on the web snippet dataset — **10,060 training and 2,280 test snippets** across **8 classes**, averaging **18 words** each ([Song & Zhao, n.d.](document_1.txt)). Reported precision was **82.18**, **85.31**, **85.48**, and **85.65** across the compared methods, with the proposed embedding-based approach ("Ours") achieving the highest figure ([Song & Zhao, n.d.](document_1.txt)). The authors attribute this to word embeddings capturing similarity between distinct words such as "finance" and "economy," which traditional topic models handle poorly ([Song & Zhao, n.d.](document_1.txt)).

## Assessment

On the evidence supplied, the answer to the query is best framed as a range rather than a single integer. **106 templates** is the only figure that is uncontested across both sources, and it is tied to a clearly specified evaluation (500 Freebase triples sharing 53 predicates) ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The domain-specific figure is reported as 163 in the primary text and 103 in the secondary note, producing totals of 269 or 209 respectively ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

My own assessment is that the **primary document's 163 should be given greater weight**, on the principle that a primary source outranks a third-party synthesis, and because the primary text is internally consistent about the power tool KB being the larger and more heavily templated of the two settings — it reports 67 predicates, 293 subjects, and 279 objects, and produces 12,228 seed questions, a substantially larger seed pool than Freebase's 991 ([Song & Zhao, n.d.](document_1.txt)). That said, the OCR artifacts that split numerals throughout document 1 counsel caution, and the third-party note's clean 106 + 103 = 209 arithmetic is not easily dismissed ([Third-party research note, n.d.](document_2.txt)). A reader citing this work should report both figures rather than choosing silently.

Regardless of which count is adopted, the substantive finding is unchanged: the manual template burden is on the order of a few hundred items, covering roughly 120 distinct predicates across two KBs, and it yields 13,219 seed questions in the reported experiments before any web expansion ([Song & Zhao, n.d.](document_1.txt)). The design's central claim — that leveraging web resources "significantly reduces the human effort" relative to training on 10,000 human-written question pairs — is supported by the reported figures ([Song & Zhao, n.d.](document_1.txt)).

## Limitations of the Evidence

Three caveats should accompany any quotation of these numbers. First, the primary document is a degraded OCR rendering, which is the direct cause of the 163-versus-103 ambiguity, and similar digit-splitting affects other figures such as the 10,000 baseline pairs and the 12,228 seed questions ([Song & Zhao, n.d.](document_1.txt)). Second, several baseline method names in the comparison tables are rendered only as "? )" in the supplied text, so attributions to specific prior systems cannot be verified from these documents alone ([Song & Zhao, n.d.](document_1.txt)). Third, the current system "only generates questions without answers," with automatic answer mining left as future work ([Song & Zhao, n.d.](document_1.txt)).

## Conclusion

The work under review hand-crafted **106 templates** for the Freebase evaluation and a further **103 or 163 templates** for its in-house power tool knowledge base, for a reported total of **209** (third-party note) or **269** (primary text) ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Template construction was the sole manual component of the pipeline; every other stage — seed generation, iterative Google-based expansion, skip-gram relevance scoring, and 4-gram fluency filtering — was automated ([Song & Zhao, n.d.](document_1.txt)). The compactness of the template set is explained by predicate reuse and by the multiplicative effect of search-engine expansion, and it is validated by human ratings of 3.53 grammaticality and 3.31 naturalness against the 3.36 and 3.14 of the prior state of the art ([Song & Zhao, n.d.](document_1.txt)).

## References

Song, L., & Zhao, L. (n.d.). *Question generation from a knowledge base with web exploration* [document_1.txt]. University of Rochester, Computer Science Department; Bosch Research and Technology Center.

Third-party research note: *Question generation from a knowledge base with web exploration* [document_2.txt]. (n.d.).