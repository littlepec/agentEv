# Hand-Crafted Template Counts in the Proposed System: A Detailed Analysis of Manual Template Construction

## Introduction and Query Context

The system described in the provided source relies on a small set of question templates, each associated with a predicate in a knowledge base (KB) ([document_2.txt](document_2.txt)). The paper states that the only human labor in this work is question template construction, making the number of hand-crafted templates a central measure of manual effort ([document_2.txt](document_2.txt)). The query asks: “How many hand-crafted templates did they have to make?” The answer is not a single monolithic figure because the paper reports template counts for two distinct evaluations: a Freebase evaluation and an in-house power tool domain evaluation ([document_2.txt](document_2.txt)). For the Freebase evaluation, the authors hand-crafted 106 templates for 500 triples that share only 53 distinct predicates ([document_2.txt](document_2.txt)). For the in-house power tool domain KB, which has 67 predicates, the authors hand-crafted 163 templates ([document_2.txt](document_2.txt)). Therefore, if the question refers to the combined manual template construction across both reported evaluations, the total is 269 templates (106 + 163). If the question refers to each evaluation separately, the counts are 106 and 163 respectively. This report provides a detailed breakdown, context, and analysis of those figures.

## Direct Answer and Summary of Counts

The most direct answer depends on scope. Across the two evaluations reported in the source, the authors had to make a total of 269 hand-crafted templates ([document_2.txt](document_2.txt)). This total comprises 106 templates for the Freebase evaluation and 163 templates for the in-house power tool domain evaluation ([document_2.txt](document_2.txt)). The Freebase template set was built for 500 randomly selected triples that shared only 53 distinct predicates, resulting in an average of 2 templates per predicate ([document_2.txt](document_2.txt)). The power tool template set was built for 67 predicates, yielding an average of approximately 2.43 templates per predicate ([document_2.txt](document_2.txt)). The following table summarizes the reported figures.

| Evaluation | Knowledge Base | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate | Triples Used | Seed Questions Generated | Additional Questions Retrieved |
|------------|----------------|---------------------|------------------------|-------------------------|--------------|--------------------------|--------------------------------|
| Freebase | Freebase | 53 | 106 | 2.00 | 500 | 991 | 1529 from Google |
| Power Tool | In-house power tool domain KB | 67 | 163 | ~2.43 | Not reported | Not reported | Not reported |
| **Total** | **Both** | **120** | **269** | **~2.24** | **500+** | **991+** | **1529+** |

*Note.* The total distinct predicates (120) is a simple sum of the two predicate sets; however, the two evaluations use different knowledge bases and predicate sets, so this sum is for descriptive convenience only. The template counts are directly reported in the source ([document_2.txt](document_2.txt)). The templates per predicate for the power tool domain is calculated as 163 ÷ 67 ≈ 2.43. The combined templates per predicate is calculated as 269 ÷ 120 ≈ 2.24. The source does not report a combined template count, so the total of 269 is an arithmetic sum of the two reported figures.

## Freebase Evaluation: 106 Hand-Crafted Templates

### Triple and Predicate Context

For the Freebase evaluation, the work used 500 randomly selected triples ([document_2.txt](document_2.txt)). These triples shared only 53 distinct predicates ([document_2.txt](document_2.txt)). The paper reports 106 hand-crafted templates for those 500 Freebase triples ([document_2.txt](document_2.txt)). Because the triples share only 53 distinct predicates, the authors made 2 templates for each predicate on average ([document_2.txt](document_2.txt)). This design ties template creation to predicates rather than to individual triples, keeping the template set compact relative to the triple set ([document_2.txt](document_2.txt)). In numerical terms, 106 templates for 500 triples means there are about 0.212 templates per triple, or roughly 4.72 triples per template. This ratio underscores that the manual effort is driven by predicate diversity, not by the raw number of triples.

### Template Generation and Question Yield

Applying the templates to the triples generated 991 seed questions ([document_2.txt](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([document_2.txt](document_2.txt)). Therefore, the Freebase evaluation ultimately involved 2,520 questions (991 + 1,529) if the two sources are combined. The 106 templates thus served as the manual seed for a larger question set. This two-stage approach—hand-crafted templates first, then retrieval of additional questions—suggests that the manual template construction is a focused, bounded task, while the bulk of the question inventory can be expanded through other means.

### Design Implication

The source explicitly states that this design “ties template creation to predicates, keeping the template set compact relative to the triple set” ([document_2.txt](document_2.txt)). This is a critical methodological point. If the authors had created one template per triple, they would have needed 500 templates. Instead, because only 53 predicates were present, they needed only 106 templates—about one-fifth of the triple count. This predicate-centric approach is efficient when many triples share predicates. The Freebase evaluation therefore demonstrates that manual template effort scales with predicate coverage, not with triple volume.

## Power Tool Domain Evaluation: 163 Hand-Crafted Templates

### Domain-Specific KB and Predicate Set

For the in-house power tool domain knowledge base, the paper reports 67 predicates ([document_2.txt](document_2.txt)). For those 67 predicates, the authors hand-crafted 163 templates ([document_2.txt](document_2.txt)). This count differs from the Freebase template count because the domain-specific KB has its own predicate set and required its own template set ([document_2.txt](document_2.txt)). In other words, the power tool templates are not a subset or a simple extension of the Freebase templates; they are an independent manual artifact built for a different KB.

### Templates per Predicate

The power tool evaluation required 163 templates for 67 predicates, which is approximately 2.43 templates per predicate (163 ÷ 67 ≈ 2.43). This is higher than the Freebase average of 2.00 templates per predicate ([document_2.txt](document_2.txt)). The source does not explain the reason for the higher ratio, but the difference indicates that the domain-specific KB required slightly more template variation per predicate. Regardless of the reason, the reported figure is 163 hand-crafted templates for this domain ([document_2.txt](document_2.txt)). The source does not report how many triples were used in the power tool evaluation, nor how many seed questions or retrieved questions were generated there. The available facts are limited to 67 predicates and 163 templates.

### Why the Count Differs from Freebase

The source states that the count differs because the domain-specific KB has its own predicate set and required its own template set ([document_2.txt](document_2.txt)). This is a straightforward consequence of predicate-centric design. Each template is associated with a predicate in the knowledge base, so template creation follows the predicates present in the KB ([document_2.txt](document_2.txt)). When the KB changes, the predicate inventory changes, and the template set must be rebuilt or adapted. The Freebase KB presented 53 distinct predicates in the sampled triples, while the power tool KB contained 67 predicates. The power tool KB therefore had more predicates to cover, and the authors produced more templates in total (163 vs. 106), as well as a higher average per predicate.

## Aggregate Manual Effort: 269 Templates Across Both Evaluations

### Arithmetic Sum

The two reported template counts are 106 and 163 ([document_2.txt](document_2.txt)). Their sum is 269. If the query asks for the total number of hand-crafted templates the authors had to make across the entire reported work, the answer is 269. This total represents the full manual template-construction effort described in the source, because the paper states that the only human labor in this work is question template construction ([document_2.txt](document_2.txt)). No other manual annotation or template-building labor is reported.

### Scope-Dependent Interpretation

It is important to distinguish between per-evaluation and aggregate counts. If the question is about the Freebase evaluation alone, the answer is 106 hand-crafted templates ([document_2.txt](document_2.txt)). If the question is about the in-house power tool domain alone, the answer is 163 hand-crafted templates ([document_2.txt](document_2.txt)). If the question is about the total manual template set created for both evaluations, the answer is 269. The source does not report a single combined figure, so the 269 total is an arithmetic aggregation. This distinction is not a trivial semantic point: the two template sets were built for different KBs and different predicate sets, and they were used in separate evaluations. Nevertheless, from the perspective of “how many hand-crafted templates did they have to make?” the combined number is 269, while the per-evaluation numbers are 106 and 163.

### Table of Aggregate Effort

| Scope | Hand-Crafted Templates | Source Citation |
|-------|------------------------|-----------------|
| Freebase evaluation only | 106 | ([document_2.txt](document_2.txt)) |
| Power tool domain only | 163 | ([document_2.txt](document_2.txt)) |
| Combined across both evaluations | 269 | Derived from ([document_2.txt](document_2.txt)) |

## Methodological and Practical Implications

### Predicate-Centric Design

The system constructs a small set of question templates, each associated with a predicate in the knowledge base ([document_2.txt](document_2.txt)). This association means template creation follows the predicates present in the KB ([document_2.txt](document_2.txt)). The Freebase and power tool counts provide the reported template-construction figures for the system, and these figures show that the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt](document_2.txt)). This is a key architectural insight: by binding templates to predicates, the authors avoid creating a separate template for every triple or every fact. The result is a compact, reusable set of templates that can be applied across many triples sharing the same predicate.

### Compactness Relative to Triples

In the Freebase evaluation, 106 templates were sufficient for 500 triples ([document_2.txt](document_2.txt)). That is a ratio of roughly 1 template for every 4.72 triples. If one were to build templates naively per triple, 500 templates would be required. The predicate-centric approach therefore reduced the manual template count by approximately 79% (from 500 to 106). This is a significant efficiency gain. The source explicitly notes that the design keeps the template set compact relative to the triple set ([document_2.txt](document_2.txt)). For the power tool domain, the source does not report the number of triples, so a similar ratio cannot be calculated. However, the same predicate-centric principle applies: 163 templates were built for 67 predicates, indicating that the manual effort is tied to predicate diversity.

### Human Labor and Manual Effort

The paper states that the only human labor in this work is question template construction ([document_2.txt](document_2.txt)). Therefore, the 106 Freebase templates and the 163 power tool templates represent the entirety of the manual work reported. The template construction is the manual component reported ([document_2.txt](document_2.txt)). This is important for evaluating the system’s practical cost: if the only human effort is template creation, then the total manual burden is 269 templates across both evaluations. Everything else—applying templates to triples, generating seed questions, retrieving additional questions from Google—is automated or retrieval-based.

### Question Generation and Retrieval

For the Freebase evaluation, applying the 106 templates to the 500 triples generated 991 seed questions ([document_2.txt](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([document_2.txt](document_2.txt)). Thus, the manual template construction enabled the generation of 991 questions, and the total question pool was expanded to 2,520 questions. The power tool evaluation’s question generation figures are not reported in the provided source. This asymmetry suggests that the Freebase evaluation is more fully documented in terms of downstream question yield.

## Discussion

The query “How many hand-crafted templates did they have to make?” can be answered at three levels. First, for the Freebase evaluation, they made 106 templates ([document_2.txt](document_2.txt)). Second, for the in-house power tool domain, they made 163 templates ([document_2.txt](document_2.txt)). Third, across both evaluations, they made 269 templates in total. The source does not collapse these into a single headline number, but the arithmetic is straightforward. The predicate-centric design explains why the counts are relatively modest compared to the number of triples in the Freebase evaluation. With only 53 distinct predicates, the authors needed an average of 2 templates per predicate, for a total of 106 ([document_2.txt](document_2.txt)). With 67 predicates in the power tool domain, they needed an average of about 2.43 templates per predicate, for a total of 163 ([document_2.txt](document_2.txt)). The higher per-predicate average in the power tool domain may reflect the domain-specific nature of that KB, but the source does not provide a detailed rationale. What is clear is that the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt](document_2.txt)).

From a methodological standpoint, the reported counts demonstrate a disciplined approach to manual annotation. Rather than hand-crafting templates for every triple, the authors leverage predicate reuse. This keeps the manual component bounded and makes the overall system more scalable. If a new KB is introduced, the template set must be revisited according to its predicate inventory. The Freebase evaluation covered 53 predicates with 106 templates; the power tool evaluation covered 67 predicates with 163 templates. These figures provide a useful benchmark for estimating future manual effort: roughly 2 to 2.5 templates per predicate. For a KB with P predicates, one might expect approximately 2P to 2.5P templates, although this is an extrapolation from only two data points and should be treated cautiously.

## Conclusion

The authors had to make 106 hand-crafted templates for the Freebase evaluation, 163 hand-crafted templates for the in-house power tool domain evaluation, and therefore 269 hand-crafted templates in total across both reported evaluations ([document_2.txt](document_2.txt)). The Freebase templates were built for 500 triples sharing 53 distinct predicates, averaging 2 templates per predicate, and they generated 991 seed questions, with an additional 1529 questions retrieved from Google ([document_2.txt](document_2.txt)). The power tool templates were built for 67 predicates, averaging approximately 2.43 templates per predicate ([document_2.txt](document_2.txt)). The source states that the only human labor in this work is question template construction, so these template counts represent the full manual effort reported ([document_2.txt](document_2.txt)). The answer to the query is therefore scope-dependent: 106 for Freebase, 163 for the power tool domain, and 269 combined.

## References

document_2.txt. (n.d.). *Source document* [Unpublished manuscript]. [document_2.txt](document_2.txt)