---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Folic Acid: From Vitamin Supplement to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (vitamin B9) is a water-soluble B vitamin widely used for the prevention of megaloblastic anaemia and neural tube defects.
The TxGNN model predicts it may be effective for **Biotin Metabolic Disease**,
however, **no directly relevant clinical trials** and only **tangentially related literature** currently support this direction — all retrieved evidence scored low relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication data available (no Philippines registration) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, folic acid (vitamin B9) is a water-soluble B vitamin that serves as a cofactor in one-carbon metabolism, nucleotide biosynthesis, and methylation reactions. It is essential for DNA synthesis and repair, and its deficiency classically manifests as megaloblastic anaemia and, during pregnancy, neural tube defects.

Biotin metabolic disease — encompassing conditions such as biotinidase deficiency and holocarboxylase synthetase deficiency — involves impairment of biotin (vitamin B7) recycling or attachment to carboxylase enzymes. The standard of care is high-dose biotin supplementation, not folic acid. While folic acid and biotin are both members of the water-soluble B-vitamin family, they participate in fundamentally different metabolic pathways: folic acid in one-carbon transfer reactions, and biotin as a cofactor for carboxylation reactions in fatty acid synthesis, gluconeogenesis, and amino acid catabolism.

The high TxGNN prediction score (99.49%) most likely arises from structural proximity in the knowledge graph — B-vitamin nodes share many neighbourhood connections (co-occurrence in multivitamin formulations, shared transporter studies, and overlapping deficiency literature) rather than from a genuine therapeutic mechanism. No pharmacological evidence supports folic acid as a substitute for, or treatment of, biotin metabolic disorders.

---

## Clinical Trial Evidence

All 13 retrieved clinical trials received a **Grade C (low)** relevance rating. Folic acid appears only as a background nutrient or component of multivitamin formulations in these studies, none of which directly investigate biotin metabolic disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and child neurodevelopment; folic acid as routine background supplement only |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Metabolic intervention for autism oxidative stress; folic acid as part of a composite supplement, not targeting biotin metabolism |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Bioavailability comparison of natural vs. synthetic vitamin B complexes; pilot study, not disease-targeted |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative therapy in congestive heart failure; folic acid one component of many |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food vs. milk for malnourished children; general malnutrition, not biotin metabolic disease |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening (Baby Detect); screening infrastructure, not treatment trial |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamins/minerals for diabetic neuropathy and nephropathy; no biotin metabolism focus |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | CoQ10 + multivitamin metabolic support for autism (Phelan-McDermid syndrome); not biotin metabolic disease |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption post-bariatric surgery; not biotin metabolic disease |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multi-vitamin/mineral ± fatty acid supplementation for impulsivity and aggression; not disease-targeted |

> ⚠️ **Note:** None of the retrieved trials directly investigate folic acid as a treatment for biotin metabolic disease. All relevance grades are C (low).

---

## Literature Evidence

Twenty publications were retrieved. While several discuss B vitamins and inborn errors of metabolism in a general context, none provide direct evidence that folic acid treats biotin metabolic disease. The most relevant publications are listed below, prioritised by tier.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review (Tier 1) | Handbook of Clinical Neurology | Comprehensive review of vitamin-responsive disorders including cobalamin, folate, and biotin; describes distinct metabolic pathways and separate disease entities |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review (Tier 2) | Movement Disorders | Movement disorders in treatable inborn errors of metabolism; biotin-responsive conditions discussed among many IEMs |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review (Tier 2) | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases; describes vitamin-dependent syndromes including biotin-dependent conditions, treated with the specific deficient vitamin |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review (Tier 3) | Int J Mol Sci | Vitamin B12 deficiency and the nervous system; mentions biochemical link between B12, biotin, and folic acid in succinyl-CoA synthesis pathway |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review (Tier 3) | Clin Dermatol | B vitamins in dermatology; general overview of all eight B vitamins including folic acid and biotin as distinct entities |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review (Tier 3) | Cureus | Relationship between vitamins and diabetes; notes both biotin and folic acid levels are altered in diabetes, but as independent phenomena |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review (Tier 3) | Endocr Metab Immune Disord Drug Targets | Vitamins and type 2 diabetes mellitus; biotin and folic acid discussed separately as deficient micronutrients |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review (Tier 3) | Gastroenterol Clin North Am | Vitamins and minerals in IBD; discusses micronutrient deficiencies broadly, no biotin metabolic disease focus |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatr Clin North Am | Megavitamin-responsive aminoacidopathies; discusses vitamin cofactor therapy for IEMs — each vitamin treats its own deficiency pathway |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Review | Adv Hum Genet | Vitamin-responsive inherited metabolic disorders; foundational review establishing that each vitamin-dependent IEM requires its specific vitamin |

> ⚠️ **Note:** The literature consistently describes folic acid and biotin as distinct cofactors with separate metabolic roles. No publication supports folic acid as a treatment for biotin metabolic disease.

---

## Philippines Market Information

Folic acid has **no registered pharmaceutical products** with the Philippines FDA in this dataset.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registered products found |

---

## Safety Considerations

> Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high prediction score (99.49%) is almost certainly an artefact of knowledge graph proximity — folic acid and biotin share neighbourhood nodes as B-vitamin family members, but they operate through entirely different metabolic pathways. The established treatment for biotin metabolic disease is biotin itself, not folic acid. All 13 retrieved clinical trials scored Grade C (low relevance), and the 20 literature references consistently describe folic acid and biotin as distinct entities with no therapeutic cross-over. There is no mechanistic, clinical, or epidemiological basis to pursue this repurposing candidate.

**To proceed, the following would be needed:**
- Direct preclinical evidence demonstrating folic acid activity on biotinidase or holocarboxylase synthetase pathways (currently non-existent)
- At least one clinical case report or observational study showing benefit of folic acid in biotinidase or holocarboxylase synthetase deficiency
- Mechanistic rationale beyond graph-structural proximity in the knowledge graph
- **This candidate is recommended for deprioritisation** — resources should be directed toward higher-evidence repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

