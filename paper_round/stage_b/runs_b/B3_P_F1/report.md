# Hand-Crafted Template Creation in the Evaluated Question Generation System: A Detailed Analysis

## Introduction

The query asks how many hand-crafted templates the authors had to make in the reported work. According to the available source material, the work reports template construction across two distinct knowledge base evaluations: a Freebase evaluation and an in-house power tool domain evaluation. The source explicitly states that the only human labor in this work is question template construction, and that template creation is manually performed ([Document 2, n.d.](document_2.txt)). This report examines the reported counts, the relationship between templates and predicates, and the aggregate manual effort. The central finding is that the authors hand-crafted **209 templates in total**: **106 templates for the Freebase evaluation** and **103 templates for the in-house power tool domain** ([Document 2, n.d.](document_2.txt)). The sections below present the evidence, the methodological logic, and the implications of these figures.

## Direct Answer and Aggregate Counts

The most direct answer to the query is that the authors had to make **209 hand-crafted templates** in total. This total is explicitly reported in the template-construction experiment ([Document 2, n.d.](document_2.txt)). The figure combines two separate manual efforts: 106 Freebase templates and 103 power tool domain templates ([Document 2, n.d.](document_2.txt)). The table below summarizes the reported counts and the associated predicate coverage for each evaluation.

| Evaluation Domain | Predicates | Hand-Crafted Templates | Average Templates per Predicate | Triples or Domain Context |
|---|---:|---:|---:|---|
| Freebase | 53 distinct predicates | 106 | 2.0 | 500 randomly selected triples |
| In-house power tool domain | 67 predicates | 103 | Approximately 1.54 | Domain-specific knowledge base |
| **Total** | **120 predicates** | **209** | **Approximately 1.74** | **Two evaluations** |

*Note.* The Freebase average is explicitly reported as 2 templates per predicate on average ([Document 2, n.d.](document_2.txt)). The power tool average is calculated from the reported 103 templates and 67 predicates ([Document 2, n.d.](document_2.txt)). The total predicate count of 120 is the sum of the two distinct predicate sets, and the total template count of 209 is directly reported ([Document 2, n.d.](document_2.txt)).

The table makes clear that the manual template-building effort is not primarily a function of the number of triples or questions. Instead, it is tied to the predicate coverage of each knowledge base. The Freebase evaluation involves 500 randomly selected triples that share only 53 distinct predicates, and the authors created 106 templates for those predicates ([Document 2, n.d.](document_2.txt)). The power tool domain has 67 predicates and required 103 templates ([Document 2, n.d.](document_2.txt)). Together, these figures yield the 209 total that answers the query.

## Freebase Evaluation Details

In the Freebase evaluation, the work uses 500 randomly selected triples ([Document 2, n.d.](document_2.txt)). The paper reports 106 hand-crafted templates for those 500 triples ([Document 2, n.d.](document_2.txt)). Because the triples share only 53 distinct predicates, the authors made two templates for each predicate on average ([Document 2, n.d.](document_2.txt)). This design ties template creation to predicates, keeping the template set compact relative to the triple set ([Document 2, n.d.](document_2.txt)).

Applying the templates to the triples generated 991 seed questions ([Document 2, n.d.](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([Document 2, n.d.](document_2.txt)). These numbers are important because they show that the manual template effort is a front-loaded investment: 106 templates support the generation of 991 seed questions, and the overall question pool is expanded further by external retrieval ([Document 2, n.d.](document_2.txt)). The Freebase count of 106 templates is therefore not merely a small detail; it is the manual component that enables the larger automated question generation process ([Document 2, n.d.](document_2.txt)).

The Freebase evidence also shows that template creation follows the predicates present in the knowledge base ([Document 2, n.d.](document_2.txt)). Since the 500 triples share only 53 predicates, the authors did not need a separate template for each triple. Instead, they created two templates per predicate on average, which means the template set remains compact relative to the triple set ([Document 2, n.d.](document_2.txt)). This is a deliberate design choice that reduces manual effort while covering the predicate space.

## In-House Power Tool Domain Details

For the in-house power tool domain knowledge base, the paper reports 67 predicates ([Document 2, n.d.](document_2.txt)). For those 67 predicates, the authors hand-crafted 103 templates ([Document 2, n.d.](document_2.txt)). Together with the 106 Freebase templates, the authors wrote 209 templates in total ([Document 2, n.d.](document_2.txt)). The paper reports this total in the template-construction experiment ([Document 2, n.d.](document_2.txt)). The domain-specific knowledge base has its own predicate set and required its own template set ([Document 2, n.d.](document_2.txt)).

The power tool figures reinforce the predicate-centric logic. The 103 templates are not distributed across triples in the same way as the Freebase templates, because the source does not report the number of triples for the power tool domain ([Document 2, n.d.](document_2.txt)). What is reported is the predicate count and the template count: 67 predicates and 103 templates ([Document 2, n.d.](document_2.txt)). This yields an average of approximately 1.54 templates per predicate, which is lower than the Freebase average of 2.0 templates per predicate ([Document 2, n.d.](document_2.txt)). The difference may reflect domain-specific factors, but the source does not provide an explanation for the variation. What is clear is that the power tool domain contributes 103 templates to the total manual effort ([Document 2, n.d.](document_2.txt)).

The Freebase and power tool counts provide the reported template-construction figures for the system ([Document 2, n.d.](document_2.txt)). These figures show the manual template-building effort scales with predicate coverage in each evaluation ([Document 2, n.d.](document_2.txt)). In other words, the authors did not have to create templates for every triple or every possible question. They had to create templates for the predicates that appeared in each knowledge base, and the total number of hand-crafted templates across both evaluations is 209 ([Document 2, n.d.](document_2.txt)).

## Total Manual Template Construction Effort

The aggregate figure of 209 templates is the answer to the query. It is the sum of 106 Freebase templates and 103 power tool templates ([Document 2, n.d.](document_2.txt)). The source states that the authors wrote 209 templates in total and that this total is reported in the template-construction experiment ([Document 2, n.d.](document_2.txt)). The source also states that the only human labor in this work is question template construction ([Document 2, n.d.](document_2.txt)). Therefore, the 209 templates represent the complete reported manual template-building effort.

It is worth noting that the total is not an estimate derived from a formula; it is a directly reported number ([Document 2, n.d.](document_2.txt)). The component numbers are also directly reported: 106 for Freebase and 103 for the power tool domain ([Document 2, n.d.](document_2.txt)). The average templates per predicate can be calculated, but the total itself is given. This makes the answer to the query unambiguous within the provided source material: **209 hand-crafted templates** ([Document 2, n.d.](document_2.txt)).

The table below restates the arithmetic in a compact form for clarity.

| Component | Reported Templates |
|---|---:|
| Freebase templates | 106 |
| Power tool domain templates | 103 |
| **Total hand-crafted templates** | **209** |

*Note.* All figures are from Document 2 ([Document 2, n.d.](document_2.txt)).

## Design Rationale and Predicate-Centric Approach

The proposed system first constructs a small set of question templates ([Document 2, n.d.](document_2.txt)). Each template is associated with a predicate in the knowledge base ([Document 2, n.d.](document_2.txt)). This association means template creation follows the predicates present in the KB ([Document 2, n.d.](document_2.txt)). The paper states that the only human labor in this work is question template construction, so the template construction is the manual component reported ([Document 2, n.d.](document_2.txt)).

This design has several implications. First, because templates are tied to predicates, the manual effort scales with the number of distinct predicates rather than the number of triples or the number of generated questions ([Document 2, n.d.](document_2.txt)). In the Freebase evaluation, 500 triples shared only 53 distinct predicates, so the authors needed 106 templates rather than 500 or more ([Document 2, n.d.](document_2.txt)). In the power tool domain, 67 predicates required 103 templates ([Document 2, n.d.](document_2.txt)). Second, the template set remains compact relative to the triple set, which is explicitly noted in the source for the Freebase case ([Document 2, n.d.](document_2.txt)). Third, the manual effort is front-loaded: once the templates are created, they can be applied to triples to generate many seed questions ([Document 2, n.d.](document_2.txt)).

The predicate-centric approach also explains why the total is 209 rather than a much larger number. If the authors had needed to hand-craft a template for every triple, the Freebase evaluation alone would have required 500 templates, and the total would be far higher ([Document 2, n.d.](document_2.txt)). Instead, the 106 Freebase templates cover 53 predicates at an average of two templates per predicate ([Document 2, n.d.](document_2.txt)). The 103 power tool templates cover 67 predicates at an average of about 1.54 templates per predicate ([Document 2, n.d.](document_2.txt)). The total of 209 templates is therefore a direct consequence of the predicate-based design.

## Implications for Scalability and Manual Effort

The reported figures allow some analysis of how manual effort scales. In the Freebase evaluation, the ratio of templates to triples is 106 templates for 500 triples, or approximately 0.212 templates per triple ([Document 2, n.d.](document_2.txt)). In the power tool domain, the source does not report the number of triples, so a comparable ratio cannot be calculated ([Document 2, n.d.](document_2.txt)). However, the ratio of templates to predicates can be calculated for both: 106 templates for 53 predicates is 2.0 templates per predicate, and 103 templates for 67 predicates is approximately 1.54 templates per predicate ([Document 2, n.d.](document_2.txt)). Across both evaluations, there are 120 predicates and 209 templates, giving an overall average of approximately 1.74 templates per predicate ([Document 2, n.d.](document_2.txt)).

These ratios suggest that the manual burden is driven by predicate diversity. A knowledge base with many predicates requires more templates, while a knowledge base with many triples but few predicates requires relatively fewer templates. The Freebase evaluation illustrates the latter case: 500 triples but only 53 predicates, and therefore only 106 templates ([Document 2, n.d.](document_2.txt)). The power tool domain illustrates a smaller predicate set (67 predicates) but still required 103 templates, indicating that domain-specific predicate sets impose their own manual costs ([Document 2, n.d.](document_2.txt)).

The source states that the manual template-building effort scales with predicate coverage in each evaluation ([Document 2, n.d.](document_2.txt)). This is a key finding. It means that adding more triples to an existing predicate set may not require proportionally more template construction, whereas adding new predicates would. The 209 total templates are therefore best understood as the cost of covering 120 distinct predicates across two evaluations, not as the cost of covering a particular number of triples or questions ([Document 2, n.d.](document_2.txt)).

## Question Generation Outcome

The templates are not an end in themselves. In the Freebase evaluation, applying the templates to the triples generated 991 seed questions ([Document 2, n.d.](document_2.txt)). The experiment also retrieved 1529 more questions from Google ([Document 2, n.d.](document_2.txt)). This means the manual template effort of 106 Freebase templates contributed to a seed question set of 991 questions, which was then supplemented by 1529 externally retrieved questions ([Document 2, n.d.](document_2.txt)). The source does not report an equivalent question-generation count for the power tool domain, but it does report that the power tool KB has its own predicate set and required its own template set ([Document 2, n.d.](document_2.txt)).

The overall picture is that the authors made 209 hand-crafted templates to support question generation across two domains ([Document 2, n.d.](document_2.txt)). The Freebase portion alone generated 991 seed questions, showing that the template investment can produce a much larger set of questions ([Document 2, n.d.](document_2.txt)). The Google retrieval added 1529 more questions, but that portion is not template-based and does not add to the manual template count ([Document 2, n.d.](document_2.txt)). The query specifically asks about hand-crafted templates, so the relevant number remains 209 ([Document 2, n.d.](document_2.txt)).

## Reliability and Source Considerations

The information provided comes from a single source document, identified as `document_2.txt` ([Document 2, n.d.](document_2.txt)). The source contains two content blocks, both attributed to the same file, and both report template construction figures ([Document 2, n.d.](document_2.txt)). The first block focuses on the Freebase evaluation: 500 triples, 53 predicates, 106 templates, 991 seed questions, and 1529 Google questions ([Document 2, n.d.](document_2.txt)). The second block focuses on the in-house power tool domain: 67 predicates, 103 templates, and a total of 209 templates ([Document 2, n.d.](document_2.txt)).

Because only one source is available, the report cannot independently verify the figures against a second source. However, the source is internally consistent: 106 plus 103 equals 209, and the total is explicitly stated ([Document 2, n.d.](document_2.txt)). The source also explicitly links template creation to predicates, which explains why the counts are what they are ([Document 2, n.d.](document_2.txt)). Within the constraints of the provided information, the most reliable answer is the directly reported total of 209 hand-crafted templates ([Document 2, n.d.](document_2.txt)).

It is also important to note what the source does not say. It does not report a different total for hand-crafted templates elsewhere in the text. It does not suggest that the 209 figure excludes any templates. It states that the authors wrote 209 templates in total and that this total is reported in the template-construction experiment ([Document 2, n.d.](document_2.txt)). Therefore, any answer other than 209 would contradict the provided source material.

## Conclusion

The query asks how many hand-crafted templates the authors had to make. Based on the provided information, the answer is **209 templates in total** ([Document 2, n.d.](document_2.txt)). This total comprises **106 templates for the Freebase evaluation** and **103 templates for the in-house power tool domain** ([Document 2, n.d.](document_2.txt)). The Freebase templates cover 53 distinct predicates and were applied to 500 randomly selected triples, generating 991 seed questions ([Document 2, n.d.](document_2.txt)). The power tool templates cover 67 predicates ([Document 2, n.d.](document_2.txt)). The design is predicate-centric, and the source states that the only human labor in the work is question template construction ([Document 2, n.d.](document_2.txt)). Therefore, the reported manual template-building effort is 209 hand-crafted templates, and this figure is directly stated in the source ([Document 2, n.d.](document_2.txt)).

## References

Document 2. (n.d.). *[Template construction data for Freebase and power tool domain evaluations]* [Unpublished manuscript]. document_2.txt.