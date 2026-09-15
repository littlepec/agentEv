# Hand-Crafted Template Construction: A Detailed Report on the Number of Templates in the Proposed System

## Introduction

The query asks, "How many hand-crafted templates did they have to make?" Based on the provided source document_2.txt, the reported answer is **209 hand-crafted templates in total**. This total is composed of **106 templates for the Freebase evaluation** and **103 templates for the in-house power tool domain knowledge base**. The source states that the only human labor in this work is question template construction, and the template construction therefore is the manual component reported ([document_2.txt, n.d.](document_2.txt)). This report provides a detailed breakdown of those figures, the context in which they were produced, and the methodological logic that ties template creation to predicates in the knowledge base.

## Direct Answer and Summary of Figures

The direct answer to the query is that the authors hand-crafted **209 templates in total**. The paper reports this total in the template-construction experiment ([document_2.txt, n.d.](document_2.txt)). The two constituent evaluations are:

- For the Freebase evaluation, the work uses 500 randomly selected triples. The paper reports 106 hand-crafted templates for those 500 Freebase triples ([document_2.txt, n.d.](document_2.txt)).
- For the in-house power tool domain knowledge base, the paper reports 67 predicates. For the 67 predicates, the authors hand-crafted 103 templates ([document_2.txt, n.d.](document_2.txt)).
- Together with the 106 Freebase templates, the authors wrote 209 templates in total ([document_2.txt, n.d.](document_2.txt)).

These numbers are the core response to the query. They also show that the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt, n.d.](document_2.txt)).

## Methodological Context: Templates Tied to Predicates

The proposed system first constructs a small set of question templates. Each template is associated with a predicate in the knowledge base. This association means template creation follows the predicates present in the KB ([document_2.txt, n.d.](document_2.txt)). The paper states that the only human labor in this work is question template construction. The template construction therefore is the manual component reported ([document_2.txt, n.d.](document_2.txt)).

This design choice is important for understanding the 209 figure. Because templates are tied to predicates rather than to individual triples, the template set remains compact relative to the triple set. For the Freebase evaluation, the 500 randomly selected triples share only 53 distinct predicates. The authors made 2 templates for each predicate on average, resulting in 106 templates ([document_2.txt, n.d.](document_2.txt)). For the power tool domain, there are 67 predicates, and the authors hand-crafted 103 templates ([document_2.txt, n.d.](document_2.txt)). Across both evaluations, the template counts are therefore a function of predicate coverage, not triple count.

## Detailed Breakdown: Freebase Evaluation

### Triples and Predicates

The Freebase evaluation uses 500 randomly selected triples ([document_2.txt, n.d.](document_2.txt)). These triples share only 53 distinct predicates ([document_2.txt, n.d.](document_2.txt)). The limited number of distinct predicates is the key factor that keeps the template count low relative to the triple count.

### Template Count and Average per Predicate

The paper reports 106 hand-crafted templates for those 500 Freebase triples ([document_2.txt, n.d.](document_2.txt)). Because there are 53 distinct predicates, the authors made 2 templates for each predicate on average ([document_2.txt, n.d.](document_2.txt)). This yields a simple arithmetic relationship: 53 predicates × 2 templates per predicate = 106 templates. The source explicitly links template creation to predicates, keeping the template set compact relative to the triple set ([document_2.txt, n.d.](document_2.txt)).

### Questions Generated from Templates

Applying the templates to the triples generated 991 seed questions ([document_2.txt, n.d.](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([document_2.txt, n.d.](document_2.txt)). Thus, the 106 templates were used to generate a substantial number of seed questions, and the overall question set was expanded further through retrieval. This demonstrates the leverage of the template-based design: a relatively small manual template set can generate many questions.

## Detailed Breakdown: In-House Power Tool Domain

### Predicates and Templates

For the in-house power tool domain knowledge base, the paper reports 67 predicates ([document_2.txt, n.d.](document_2.txt)). For the 67 predicates, the authors hand-crafted 103 templates ([document_2.txt, n.d.](document_2.txt)). The domain-specific KB has its own predicate set and required its own template set ([document_2.txt, n.d.](document_2.txt)). This means the power tool templates are separate from the Freebase templates and are not reused across the two evaluations.

### Average Templates per Predicate for Power Tool Domain

Although the paper does not explicitly state the average number of templates per predicate for the power tool domain, the reported figures allow a derived calculation. With 67 predicates and 103 templates, the average is approximately 1.54 templates per predicate (103 ÷ 67 ≈ 1.54). This is lower than the Freebase average of 2 templates per predicate. However, the source does not present this average as a reported figure; it is a derived value based on the reported counts of 67 predicates and 103 templates ([document_2.txt, n.d.](document_2.txt)). The key reported fact remains that 103 hand-crafted templates were made for the 67 predicates in the power tool domain ([document_2.txt, n.d.](document_2.txt)).

## Aggregate Template Construction: The 209 Total

### Summation of the Two Evaluations

The two evaluations together required 209 hand-crafted templates. This total is the sum of 106 Freebase templates and 103 power tool templates ([document_2.txt, n.d.](document_2.txt)). The paper reports this total in the template-construction experiment ([document_2.txt, n.d.](document_2.txt)). Therefore, when the query asks how many hand-crafted templates they had to make, the most direct and comprehensive answer is **209 templates in total**.

### Predicate Coverage Across Evaluations

The Freebase evaluation covered 53 distinct predicates, and the power tool domain covered 67 predicates ([document_2.txt, n.d.](document_2.txt)). Across the two evaluations, this amounts to 120 predicate instances (53 + 67 = 120), although the two evaluations are separate and use different knowledge bases. The total of 209 templates reflects the manual effort required to cover these predicate sets. The source states that the Freebase and power tool counts provide the reported template-construction figures for the system ([document_2.txt, n.d.](document_2.txt)). These figures show the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt, n.d.](document_2.txt)).

### Table: Summary of Template Construction Figures

| Evaluation | Predicates | Hand-Crafted Templates | Average Templates per Predicate (reported or derived) | Triples / Questions |
|------------|------------|------------------------|--------------------------------------------------------|---------------------|
| Freebase | 53 distinct | 106 | 2 (reported average) | 500 triples; 991 seed questions; 1529 Google-retrieved questions |
| Power tool domain | 67 | 103 | Approximately 1.54 (derived from 103 ÷ 67) | Not specified in source for triples; 67 predicates |
| Total | 120 predicate instances across evaluations | 209 | Not reported as a single average | — |

*Note: All figures in the table are drawn from the reported counts in document_2.txt ([document_2.txt, n.d.](document_2.txt)). The average for the power tool domain is a derived calculation, not a reported figure.*

## Why the Number Is 209: Interpretation and Implications

### Manual Labor Is Concentrated in Template Construction

The paper states that the only human labor in this work is question template construction ([document_2.txt, n.d.](document_2.txt)). This means the 209 templates represent the entire manual annotation burden reported for the system. There is no other reported human labor component in the provided information. This makes the 209 figure particularly significant: it is the complete manual investment described.

### Efficiency Through Predicate-Based Templates

The design ties template creation to predicates, keeping the template set compact relative to the triple set ([document_2.txt, n.d.](document_2.txt)). For Freebase, 106 templates covered 500 triples, which is roughly 0.212 templates per triple (106 ÷ 500 ≈ 0.212). This ratio illustrates the efficiency of the approach: the template set is much smaller than the triple set because many triples share the same predicates. The source explicitly notes that the triples share only 53 distinct predicates, so the authors made 2 templates for each predicate on average ([document_2.txt, n.d.](document_2.txt)). This explains why the template count is not proportional to the triple count.

### Scaling with Predicate Coverage

The source states that the manual template-building effort scales with predicate coverage in each evaluation ([document_2.txt, n.d.](document_2.txt)). This is visible in the two evaluations: the Freebase evaluation had 53 predicates and 106 templates, while the power tool evaluation had 67 predicates and 103 templates. Although the power tool evaluation had more predicates, it required slightly fewer templates, indicating that the number of templates per predicate can vary. Nevertheless, the overall pattern is that template construction is driven by the number of predicates that need to be covered.

### Leverage: From 209 Templates to Thousands of Questions

The templates were not an end in themselves. Applying the Freebase templates to the triples generated 991 seed questions ([document_2.txt, n.d.](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([document_2.txt, n.d.](document_2.txt)). Thus, the 106 Freebase templates contributed to a question pool of at least 991 seed questions, with an additional 1529 questions retrieved. This indicates that the manual template effort is leveraged to produce a much larger dataset. The 209 total templates therefore represent a relatively small manual investment compared to the downstream question generation and retrieval.

## Comparison of the Two Template Sets

### Freebase Templates

- Number of triples: 500 randomly selected triples ([document_2.txt, n.d.](document_2.txt)).
- Number of distinct predicates: 53 ([document_2.txt, n.d.](document_2.txt)).
- Number of hand-crafted templates: 106 ([document_2.txt, n.d.](document_2.txt)).
- Average templates per predicate: 2 ([document_2.txt, n.d.](document_2.txt)).
- Seed questions generated: 991 ([document_2.txt, n.d.](document_2.txt)).
- Additional questions retrieved from Google: 1529 ([document_2.txt, n.d.](document_2.txt)).

### Power Tool Domain Templates

- Number of predicates: 67 ([document_2.txt, n.d.](document_2.txt)).
- Number of hand-crafted templates: 103 ([document_2.txt, n.d.](document_2.txt)).
- Relationship: The domain-specific KB has its own predicate set and required its own template set ([document_2.txt, n.d.](document_2.txt)).

### Combined Total

- Total hand-crafted templates: 209 ([document_2.txt, n.d.](document_2.txt)).
- Total predicate instances across evaluations: 120 (53 + 67) ([document_2.txt, n.d.](document_2.txt)).
- The total is reported in the template-construction experiment ([document_2.txt, n.d.](document_2.txt)).

## Conclusion

The query asks how many hand-crafted templates they had to make. The provided source document_2.txt reports that the authors hand-crafted **106 templates for the Freebase evaluation** and **103 templates for the in-house power tool domain knowledge base**, for a total of **209 hand-crafted templates** ([document_2.txt, n.d.](document_2.txt)). This total represents the manual component of the system, as the only human labor in the work is question template construction ([document_2.txt, n.d.](document_2.txt)). The template creation follows the predicates present in the knowledge base, with 53 distinct predicates in the Freebase evaluation and 67 predicates in the power tool domain ([document_2.txt, n.d.](document_2.txt)). The Freebase templates averaged 2 per predicate and generated 991 seed questions, with 1529 additional questions retrieved from Google ([document_2.txt, n.d.](document_2.txt)). The overall finding is that the manual template-building effort scales with predicate coverage, and the total number of hand-crafted templates is **209** ([document_2.txt, n.d.](document_2.txt)).

## References

document_2.txt. (n.d.). *Source document*. [Unpublished manuscript]. Retrieved from document_2.txt