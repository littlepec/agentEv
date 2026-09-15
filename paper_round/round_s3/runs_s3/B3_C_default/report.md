# Hand-Crafted Template Counts in Predicate-Driven Question Generation: A Detailed Report

## Introduction

The question of how many hand-crafted templates were required by the system described in the provided source can be answered with specific figures, but the answer depends on which evaluation is being referenced. According to the source document, the work reports two distinct template-construction efforts: one for a Freebase evaluation and one for an in-house power tool domain knowledge base ([document_2.txt](document_2.txt)). For the Freebase evaluation, the authors hand-crafted 106 templates. For the in-house power tool domain, they hand-crafted 163 templates ([document_2.txt](document_2.txt)). Taken together, the total number of hand-crafted templates reported across both evaluations is 269. This report provides a comprehensive, objective analysis of these figures, the context in which they were produced, and the implications of the template-construction design.

The source explains that the proposed system first constructs a small set of question templates, and each template is associated with a predicate in the knowledge base ([document_2.txt](document_2.txt)). This association means that template creation follows the predicates present in the knowledge base rather than the number of triples. The paper states that the only human labor in this work is question template construction, making the template counts the central measure of manual effort ([document_2.txt](document_2.txt)). Understanding the exact numbers therefore requires examining each evaluation separately and then considering the aggregate.

## The Freebase Evaluation: 106 Hand-Crafted Templates

### Context of the Freebase Experiment

For the Freebase evaluation, the work uses 500 randomly selected triples ([document_2.txt](document_2.txt)). The paper reports 106 hand-crafted templates for those 500 Freebase triples ([document_2.txt](document_2.txt)). A critical detail is that the triples share only 53 distinct predicates, so the authors made 2 templates for each predicate on average ([document_2.txt](document_2.txt)). This means the 106 templates were not created for each triple individually; rather, they were created at the predicate level. The design ties template creation to predicates, keeping the template set compact relative to the triple set ([document_2.txt](document_2.txt)).

### Template Generation and Question Yield

Applying the templates to the triples generated 991 seed questions ([document_2.txt](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([document_2.txt](document_2.txt)). These numbers illustrate the generative capacity of the template set: 106 templates were sufficient to produce 991 seed questions across 500 triples, and the system augmented these with 1529 additional questions from an external source. The source emphasizes that the template set remains compact relative to the triple set, which supports the efficiency of the predicate-driven design ([document_2.txt](document_2.txt)).

### Interpretation of the 106 Figure

The 106 hand-crafted templates represent the manual component for the Freebase evaluation. Because the triples share only 53 distinct predicates, the authors averaged 2 templates per predicate ([document_2.txt](document_2.txt)). This ratio is exact: 106 divided by 53 equals 2.0. The source does not report any additional hand-crafted templates for Freebase beyond these 106. Therefore, if the query is specifically about the Freebase evaluation, the answer is 106 hand-crafted templates.

## The In-House Power Tool Domain Evaluation: 163 Hand-Crafted Templates

### Domain-Specific Knowledge Base

For the in-house power tool domain knowledge base, the paper reports 67 predicates ([document_2.txt](document_2.txt)). For those 67 predicates, the authors hand-craft 163 templates ([document_2.txt](document_2.txt)). This count differs from the Freebase template count because the domain-specific knowledge base has its own predicate set and required its own template set ([document_2.txt](document_2.txt)). In other words, the power tool evaluation is not a subset or extension of the Freebase templates; it is a separate template-construction effort tied to a different knowledge base.

### Why the Count Differs from Freebase

The source explicitly states that the Freebase and power tool counts provide the reported template-construction figures for the system ([document_2.txt](document_2.txt)). The difference arises because each knowledge base has a distinct set of predicates. For Freebase, 53 distinct predicates required 106 templates. For the power tool domain, 67 predicates required 163 templates. The power tool domain therefore has more predicates (67 versus 53) and more templates (163 versus 106). The ratio of templates to predicates is also slightly higher in the power tool domain: 163 divided by 67 is approximately 2.43 templates per predicate, compared to 2.0 for Freebase. The source does not explain why the power tool domain required more templates per predicate, but the figures clearly show that manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt](document_2.txt)).

### Table 1: Template Counts by Evaluation

| Evaluation | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate | Other Reported Figures |
|------------|---------------------|------------------------|-------------------------|------------------------|
| Freebase | 53 | 106 | 2.0 | 500 triples; 991 seed questions; 1529 Google questions |
| Power Tool | 67 | 163 | Approx. 2.43 | Not specified in the source |
| Total across both | 120 (summed) | 269 | Approx. 2.24 | N/A |

*Note: The total predicates across both evaluations (120) is a simple sum for reference only; the two knowledge bases are distinct and their predicates should not be treated as a single unified set. Data from [document_2.txt](document_2.txt).*

## Aggregate Hand-Crafted Template Count Across Both Evaluations

### Summing the Reported Figures

If the question asks for the total number of hand-crafted templates reported across both evaluations, the sum is 106 plus 163, which equals 269 ([document_2.txt](document_2.txt)). This aggregate figure represents the complete manual template-construction effort described in the provided source. No other hand-crafted templates are mentioned. The source presents these two counts as the reported template-construction figures for the system ([document_2.txt](document_2.txt)). Therefore, the most complete answer to the query is that the authors had to make 106 templates for Freebase and 163 templates for the power tool domain, for a total of 269 hand-crafted templates.

### Table 2: Summary of the Answer to the Query

| Interpretation of the Query | Hand-Crafted Templates |
|-----------------------------|------------------------|
| Freebase evaluation only | 106 |
| Power tool domain only | 163 |
| Both evaluations combined | 269 |

*Data from [document_2.txt](document_2.txt).*

## The Role of Manual Labor and Template Design

The source states that the only human labor in this work is question template construction ([document_2.txt](document_2.txt)). The template construction is therefore the manual component reported ([document_2.txt](document_2.txt)). This has an important implication: the number of hand-crafted templates directly reflects the amount of human effort required to build the system. Because template creation follows the predicates present in the knowledge base, the effort scales with predicate coverage rather than with the number of triples ([document_2.txt](document_2.txt)). For example, the Freebase evaluation used 500 triples but only 53 distinct predicates, so only 106 templates were needed. The power tool domain had 67 predicates, so 163 templates were needed. This design keeps the template set compact relative to the triple set ([document_2.txt](document_2.txt)).

The source also notes that the proposed system first constructs a small set of question templates, and each template is associated with a predicate in the knowledge base ([document_2.txt](document_2.txt)). This association means that template creation is not an ad hoc process tied to individual triples; it is a systematic process tied to the knowledge base schema. The result is a reusable set of templates that can generate many questions from many triples. In the Freebase evaluation, 106 templates generated 991 seed questions from 500 triples, and the system retrieved 1529 additional questions from Google ([document_2.txt](document_2.txt)). The template set is therefore highly productive relative to its size.

## Answering the Query Directly

The query asks: “How many hand-crafted templates did they have to make?” Based on the provided information, the answer is not a single number because the work reports two separate evaluations. The most accurate response is as follows:

- For the Freebase evaluation, the authors had to make **106 hand-crafted templates** ([document_2.txt](document_2.txt)).
- For the in-house power tool domain evaluation, the authors had to make **163 hand-crafted templates** ([document_2.txt](document_2.txt)).
- If the question asks for the total across both evaluations, the authors had to make **269 hand-crafted templates** (106 + 163) ([document_2.txt](document_2.txt)).

The source does not report any other hand-crafted templates. Therefore, the complete answer is 106 for Freebase, 163 for the power tool domain, and 269 in total.

## Discussion: Implications of the Template Counts

The template counts reveal a design philosophy centered on predicate-based reuse. The source explicitly states that the design ties template creation to predicates, keeping the template set compact relative to the triple set ([document_2.txt](document_2.txt)). This is a notable choice because it reduces the manual burden: instead of writing a template for every triple, the authors wrote templates for predicates and then applied them across triples. For Freebase, this meant 106 templates for 500 triples, or approximately 0.212 templates per triple. For the power tool domain, the number of triples is not specified, but 163 templates were created for 67 predicates. The ratio of templates to predicates was about 2.43, which is higher than the Freebase ratio of 2.0. The source does not explain this difference, but it may reflect the greater complexity or variability of the domain-specific predicates. Regardless of the reason, the figures show that manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt](document_2.txt)).

Another implication is that the template counts are the primary measure of human labor. The paper states that the only human labor in this work is question template construction ([document_2.txt](document_2.txt)). Therefore, the 106 and 163 figures are not merely technical details; they represent the entire manual investment reported for the system. The Freebase evaluation’s 106 templates and the power tool evaluation’s 163 templates together account for all hand-crafted templates in the reported work. This makes the total of 269 templates the full manual template-construction effort described in the source.

## Conclusion

The question of how many hand-crafted templates the authors had to make can be answered with precision based on the provided source. For the Freebase evaluation, the authors hand-crafted 106 templates for 500 triples sharing 53 distinct predicates ([document_2.txt](document_2.txt)). For the in-house power tool domain knowledge base, the authors hand-crafted 163 templates for 67 predicates ([document_2.txt](document_2.txt)). The combined total across both evaluations is 269 hand-crafted templates. The source emphasizes that template creation is tied to predicates, that it is the only human labor in the work, and that the template set is kept compact relative to the triple set ([document_2.txt](document_2.txt)). Therefore, the most complete and accurate answer is: 106 templates for Freebase, 163 templates for the power tool domain, and 269 templates in total.

## References

document_2.txt. (n.d.). *Source document containing Freebase and power tool domain template-construction figures* [Unpublished source document].