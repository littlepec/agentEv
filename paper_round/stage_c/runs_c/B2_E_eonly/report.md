# BLEU Score Difference Between the Insertion–Deletion Model and the Insertion-Only KERMIT Model on the Caesar’s Cipher Task

## Executive Summary

The provided source reports an exact BLEU score comparison between an insertion-only model and an insertion–deletion model on a Caesar’s cipher task. The insertion-only model, identified as KERMIT, obtains a BLEU score of 35.55, while the insertion–deletion model obtains a BLEU score of 37.57 ([Document_1.txt, n.d.](document_1.txt)). The absolute BLEU score difference is therefore 2.02 BLEU points in favor of the insertion–deletion model. This exact difference is consistent with the source’s narrative statement that the deletion model “again increases the BLEU score over just the insertion model, by around 2 BLEU points” ([Document_1.txt, n.d.](document_1.txt)). In relative terms, the insertion–deletion model improves over the insertion-only baseline by approximately 5.68%. The present report explains the experimental context, presents the direct comparison, calculates the absolute and relative differences, and discusses the reliability and limitations of the reported result.

## Background and Evaluation Context

The source material describes a sequence-to-sequence style transformation task using Caesar’s cipher, with an illustrative source string “h k b e t” and a target string “g j a d s” ([Document_1.txt, n.d.](document_1.txt)). Although the excerpt does not provide a full task description, the table caption identifies the evaluation as “Caesar’s Cipher BLEU,” indicating that BLEU is the metric used to compare model outputs against target sequences ([Document_1.txt, n.d.](document_1.txt)). BLEU is widely used in natural language processing and related sequence generation tasks, where higher scores generally indicate closer correspondence between generated outputs and reference outputs. The source itself frames the comparison in terms of whether one model “increases the BLEU score over just the insertion model,” implying that a higher BLEU score is the desired outcome ([Document_1.txt, n.d.](document_1.txt)).

The task is relevant because it isolates a specific architectural or procedural difference: an insertion-only method versus a method that incorporates both insertion and deletion operations. The insertion-only model is explicitly labeled “Insertion Model (KERMIT)” in the source table ([Document_1.txt, n.d.](document_1.txt)). The proposed or augmented approach is labeled “Insertion Deletion Model” ([Document_1.txt, n.d.](document_1.txt)). Therefore, the central comparison is between a baseline insertion-only system and a system that adds a deletion mechanism. The source’s conclusion language suggests that the deletion component is expected to improve performance, and the reported BLEU scores provide quantitative evidence for that expectation on this particular task ([Document_1.txt, n.d.](document_1.txt)).

## Experimental Design and Training Protocol

The source provides several details about the experimental setup. The authors state that they “generate 100k examples to train on, and evaluate on 1000 held-out examples” ([Document_1.txt, n.d.](document_1.txt)). They also state that they “train our models for 200k steps, batch size of 32 and perform no model selection” ([Document_1.txt, n.d.](document_1.txt)). These details are important for interpreting the BLEU score difference because they indicate a fixed training budget, a specified batch size, and a held-out evaluation set. The use of 100,000 training examples and 1,000 held-out examples suggests a moderately sized synthetic or generated dataset, which is consistent with a controlled cipher task ([Document_1.txt, n.d.](document_1.txt)).

The statement that the authors “perform no model selection” is also relevant ([Document_1.txt, n.d.](document_1.txt)). In machine learning experiments, model selection often involves choosing the best checkpoint or hyperparameter configuration based on validation performance, which can sometimes inflate reported test metrics. Here, the source explicitly says that no such selection was performed, meaning the reported scores are likely based on a predetermined training procedure rather than a post hoc choice of the best-performing model ([Document_1.txt, n.d.](document_1.txt)). This increases the procedural transparency of the comparison, although it does not eliminate other sources of variance, such as random seed initialization, data generation procedure, or BLEU implementation details, none of which are described in the excerpt.

The source does not specify the exact architecture of KERMIT beyond its insertion-only designation, nor does it describe how the deletion model is integrated with the insertion model ([Document_1.txt, n.d.](document_1.txt)). It also does not report training time, computational resources, or the number of parameters. Nevertheless, for the specific query at hand—the BLEU score difference—the reported numbers and the experimental summary are sufficient to calculate the absolute and relative differences.

## Results: Direct BLEU Score Comparison

The source’s Table 3 presents the following results for the Caesar’s cipher task ([Document_1.txt, n.d.](document_1.txt)):

| Model | BLEU Score |
|---|---:|
| Insertion Model (KERMIT) | 35.55 |
| Insertion Deletion Model | 37.57 |

The insertion-only baseline, KERMIT, scores 35.55 BLEU. The insertion–deletion model scores 37.57 BLEU. The source states that “the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points” ([Document_1.txt, n.d.](document_1.txt)). This statement is directly supported by the numerical difference between the two scores.

The absolute BLEU score difference is calculated as follows:

\[
37.57 - 35.55 = 2.02
\]

Therefore, the insertion–deletion model improves over the insertion-only model by exactly 2.02 BLEU points on this reported task ([Document_1.txt, n.d.](document_1.txt)). The source’s approximation of “around 2 BLEU points” is consistent with this exact figure, since 2.02 rounds to 2 at the nearest integer level ([Document_1.txt, n.d.](document_1.txt)).

The same comparison can be presented with the absolute and relative differences in a single table:

| Comparison | Insertion Model (KERMIT) | Insertion Deletion Model | Absolute Difference | Relative Difference |
|---|---:|---:|---:|---:|
| Caesar’s Cipher BLEU | 35.55 | 37.57 | +2.02 BLEU points | +5.68% |

The relative difference is computed by dividing the absolute difference by the insertion-only baseline score and multiplying by 100:

\[
\frac{2.02}{35.55} \times 100 \approx 5.68\%
\]

Thus, the insertion–deletion model’s BLEU score is approximately 5.68% higher than the insertion-only KERMIT model’s BLEU score on this task ([Document_1.txt, n.d.](document_1.txt)). This relative figure is not explicitly stated in the source, but it follows directly from the reported BLEU scores. It is important to note that a BLEU score is not a percentage of correct sequences or a percentage of accuracy; therefore, the 5.68% figure should be interpreted as the relative size of the score increase, not as a proportion of correct outputs ([Document_1.txt, n.d.](document_1.txt)).

## Interpretation of the Difference

The direct answer to the query is that the BLEU score difference between the proposed approach and the insertion-only method is 2.02 BLEU points, with the proposed insertion–deletion model scoring higher. Specifically, the proposed approach achieves 37.57 BLEU, while the insertion-only method achieves 35.55 BLEU ([Document_1.txt, n.d.](document_1.txt)). The source describes this as an increase of “around 2 BLEU points,” which is accurate when the exact scores are rounded to the nearest whole number ([Document_1.txt, n.d.](document_1.txt)).

The direction of the effect is unambiguous in the provided data: the insertion–deletion model outperforms the insertion-only model on the Caesar’s cipher task. The word “again” in the source’s sentence—“the deletion model again increases the BLEU score”—suggests that this is not an isolated observation but rather a recurring pattern across tasks or experiments ([Document_1.txt, n.d.](document_1.txt)). However, the excerpt only provides numerical evidence for the Caesar’s cipher task, so the claim of recurrence cannot be independently quantified from the given information. For the present query, the relevant and verifiable result is the 2.02-point difference on the reported Caesar’s cipher evaluation ([Document_1.txt, n.d.](document_1.txt)).

A 2.02 BLEU point improvement may be considered meaningful in the context of sequence generation, especially when the baseline is already above 35 BLEU. However, the source does not report statistical significance tests, confidence intervals, or variance across multiple runs ([Document_1.txt, n.d.](document_1.txt)). Therefore, while the numerical difference is clear, the robustness of the improvement cannot be fully assessed from the excerpt alone. The fact that no model selection was performed is a positive methodological signal, but it does not substitute for repeated trials or significance testing ([Document_1.txt, n.d.](document_1.txt)).

## Reliability and Evidentiary Strength of the Source

The primary source for this report is a document labeled “document_1.txt” with a blank title field ([Document_1.txt, n.d.](document_1.txt)). The excerpt contains a table, a caption, and surrounding narrative text. The table is explicitly numbered “Table 3,” which suggests that it is part of a larger paper or report with multiple experiments ([Document_1.txt, n.d.](document_1.txt)). The numerical values are presented clearly, and the narrative statement aligns with the table. This internal consistency increases confidence in the reported difference for the purpose of answering the query.

At the same time, the source excerpt is limited. It does not include the full paper’s methodology, the exact BLEU calculation procedure, the tokenization scheme, or the source of the generated examples ([Document_1.txt, n.d.](document_1.txt)). It also does not provide standard deviations, standard errors, or confidence intervals. These limitations mean that the exact figure of 2.02 BLEU points should be understood as the reported point estimate from this specific experimental run or evaluation, rather than as a universal constant across all settings ([Document_1.txt, n.d.](document_1.txt)).

The source does, however, provide enough detail to reproduce the arithmetic and to verify the narrative claim. The training set size of 100,000 examples, evaluation set size of 1,000 held-out examples, training duration of 200,000 steps, batch size of 32, and absence of model selection are all stated explicitly ([Document_1.txt, n.d.](document_1.txt)). These details make the comparison more informative than a bare score report, even though additional methodological details would be needed for a full replication.

## Limitations and Caveats

Several caveats should be attached to the 2.02 BLEU point difference. First, the result is from a single task: Caesar’s cipher ([Document_1.txt, n.d.](document_1.txt)). The source does not provide BLEU scores for other tasks in the excerpt, so it is not possible to determine whether the same 2.02-point improvement generalizes to other sequence transformation problems. The word “again” implies broader evidence, but the quantitative basis for that implication is not included in the provided information ([Document_1.txt, n.d.](document_1.txt)).

Second, the excerpt does not specify whether the BLEU scores are case-sensitive, how tokenization is performed, or whether multiple references are used ([Document_1.txt, n.d.](document_1.txt)). BLEU scores can vary depending on these implementation choices, so cross-paper comparisons should be made cautiously. The difference reported here is internal to the same source and same table, which reduces but does not eliminate this concern ([Document_1.txt, n.d.](document_1.txt)).

Third, the source does not report whether the 2.02-point difference is statistically significant ([Document_1.txt, n.d.](document_1.txt)). A difference of this magnitude may be practically meaningful, but without variance estimates or significance tests, it is not possible to rule out random variation from initialization, data ordering, or evaluation sampling. The use of 1,000 held-out examples provides a finite evaluation set, which means the BLEU estimate itself has some sampling variability, though the source does not quantify it ([Document_1.txt, n.d.](document_1.txt)).

Fourth, the query uses the term “BELU score,” which appears to be a typographical variant of “BLEU score.” The source consistently uses “BLEU” ([Document_1.txt, n.d.](document_1.txt)). For clarity, this report treats “BELU” as referring to BLEU.

## Conclusion

Based on the provided information, the BLEU score difference between the proposed insertion–deletion model and the insertion-only method (KERMIT) is 2.02 BLEU points on the Caesar’s cipher task. The insertion-only model obtains 35.55 BLEU, and the insertion–deletion model obtains 37.57 BLEU ([Document_1.txt, n.d.](document_1.txt)). The proposed approach therefore outperforms the insertion-only baseline by exactly 2.02 BLEU points, which corresponds to a relative increase of approximately 5.68%. This exact difference aligns with the source’s summary statement that the deletion model increases the BLEU score “by around 2 BLEU points” ([Document_1.txt, n.d.](document_1.txt)). The finding supports the conclusion that adding a deletion component improves BLEU performance over insertion alone on this reported task, though the excerpt’s limited scope and lack of statistical reporting warrant caution about generalization beyond the specific Caesar’s cipher evaluation.

## References

Document_1.txt. (n.d.). *Source document_1* [Unpublished manuscript].