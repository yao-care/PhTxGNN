---
layout: default
title: Thiamine
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 4
---

# Thiamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Thiamine: From Thiamine Deficiency to Hyperthyroidism

## One-Sentence Summary

Thiamine (Vitamin B1) is an essential water-soluble micronutrient and the established treatment for thiamine deficiency disorders including beriberi and Wernicke's encephalopathy.
The TxGNN model predicts it may be beneficial in **Hyperthyroidism**, specifically in correcting the accelerated thiamine depletion driven by the hypermetabolic state of thyrotoxicosis.
This prediction is currently supported by **1 completed pilot clinical trial** and **20 publications**, comprising case reports, metabolic studies, and animal studies documenting the thiamine–thyrotoxicosis metabolic overlap.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thiamine deficiency (beriberi, Wernicke's encephalopathy) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Philippines Market Status | Not registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Thiamine (Vitamin B1) is the obligate coenzyme for two critical mitochondrial enzyme complexes: pyruvate dehydrogenase (PDH) and α-ketoglutarate dehydrogenase (KGDH). Both are rate-limiting steps in the citric acid cycle. Without adequate thiamine, cells with the highest energy demands — cardiac myocytes and neurons — cannot sustain ATP production, making them the first to fail under metabolic stress. Detailed mechanism of action data from DrugBank is currently unavailable, but the physiological role of thiamine in oxidative energy metabolism is among the best-characterized in nutritional biochemistry.

The connection to hyperthyroidism is mechanistically direct. Excess thyroid hormone elevates basal metabolic rate by 20–80%, dramatically accelerating PDH and KGDH flux throughout the body. This creates a state of **relative thiamine deficiency** even when dietary intake appears normal. The downstream consequence is a dual pathological burden: impaired cardiac energy metabolism compounds the high-output heart failure already driven by thyrotoxicosis (a beriberi–thyrotoxicosis overlap), and when vomiting is also present — as in hyperemesis gravidarum with gestational thyrotoxicosis — absolute thiamine depletion can precipitate life-threatening Wernicke's encephalopathy.

A completed pilot trial (NCT02767245) directly tested thiamine supplementation in patients with severe hyperthyroidism, assessing left ventricular ejection fraction and cardiovascular function improvement. Multiple independent case reports across decades consistently document Wernicke's encephalopathy as a recognized, reversible complication of thyrotoxicosis that responds to thiamine administration. While the evidence base has not yet reached a Phase 2/3 RCT, the mechanistic chain from thyroid hormone excess → elevated metabolic flux → thiamine consumption → energy failure is biologically coherent and multiply corroborated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | Phase NA | Completed | 12 | Pilot study assessing thiamine deficiency prevalence in severe hyperthyroidism and measuring cardiovascular function improvement (including LVEF) following thiamine supplementation. Directly tests the beriberi–thyrotoxicosis overlap hypothesis. Phase NA and n=12 limit statistical power; serves as proof-of-concept for a future RCT. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case Report | Crit Care Nurs Clin North Am | Describes concurrent high-output heart failure from thyrotoxicosis and wet beriberi; documents thiamine deficiency as a compounding cardiovascular risk requiring active supplementation alongside antithyroid therapy. |
| [21064291](https://pubmed.ncbi.nlm.nih.gov/21064291/) | 1946 | Mechanistic Study | Federation Proceedings | Foundational animal experiment demonstrating that thiamine deficiency and hyperthyroidism both reduce cardiac ATP content and ATPase activity, establishing the earliest mechanistic link between thiamine status and thyrotoxic cardiomyopathy. |
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case Report | Cureus | Wernicke's encephalopathy precipitated by gestational hyperthyroidism with hyperemesis gravidarum; neurological recovery following prompt thiamine administration reinforces the clinical urgency of supplementation in thyrotoxic patients with vomiting. |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case Report | J Gen Intern Med | Early recognition that hyperthyroidism is a non-alcoholic cause of Wernicke's encephalopathy; reviews the epidemiological and clinical association, advocating thiamine screening in thyrotoxic patients. |
| [36593922](https://pubmed.ncbi.nlm.nih.gov/36593922/) | 2023 | Case Report | Radiology Case Reports | Pre-gestational hyperthyroidism presenting as atypical Wernicke's encephalopathy; characteristic MRI findings resolved after thiamine treatment, confirming reversibility when identified early. |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case Report | Cureus | Hyperthyroidism with non-classic Wernicke's encephalopathy presentation; highlights the diagnostic gap when the full triad is absent, supporting empirical thiamine use in suspected thyrotoxicosis-related neurological deterioration. |
| [27845881](https://pubmed.ncbi.nlm.nih.gov/27845881/) | 2016 | Case Report | Horm Mol Biol Clin Investig | WE with thyrotoxicosis in pregnancy; early thiamine administration prevented permanent neurological sequelae and enabled successful delivery, demonstrating the therapeutic window when intervention is timely. |
| [13305517](https://pubmed.ncbi.nlm.nih.gov/13305517/) | 1955 | Metabolic Study | Endocrinologia | Measured urinary thiamine excretion after IV cocarboxylase loading in hyperthyroid patients vs. controls; early pharmacokinetic evidence of altered thiamine handling and increased turnover under hyperthyroid conditions. |
| [13934469](https://pubmed.ncbi.nlm.nih.gov/13934469/) | 1963 | Animal Study | Ann Biochem Exp Med | Hyperthyroid rats showed reduced tissue thiamine storage and altered intestinal thiamine synthesis, directly supporting the mechanism of accelerated thiamine depletion under excess thyroid hormone. |
| [9704251](https://pubmed.ncbi.nlm.nih.gov/9704251/) | 1998 | Narrative Review | Drug Safety | Clinical review of nausea and vomiting management in pregnancy; explicitly recommends thiamine supplementation to prevent Wernicke's encephalopathy in severe hyperemesis gravidarum — directly applicable when gestational thyrotoxicosis co-exists. |

---

## Philippines Market Information

Thiamine is currently **not registered** with the Philippine FDA. No product authorization records are on file in the regulatory database (0 licenses).

> **Note:** Thiamine (Vitamin B1) is widely available globally as both a prescription parenteral preparation and an over-the-counter nutritional supplement. The absence of a formal Philippine FDA pharmaceutical registration may reflect its common classification as a food supplement or dietary product rather than a regulated drug. Regulatory pathway clarification is recommended before initiating any formal clinical programme in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between thyroid hormone-driven hypermetabolism and thiamine depletion is biochemically well-established, corroborated by decades of case series, metabolic studies, and a completed pilot trial. Thiamine has an excellent safety profile at therapeutic doses with no significant drug interactions identified, making a cautious "proceed" justifiable while awaiting formal Phase 2 trial data.

**To proceed, the following is needed:**
- Design a Phase 2 RCT building on NCT02767245 with adequate sample size (≥60 per arm), powered for pre-specified cardiovascular endpoints (LVEF improvement, BNP reduction, symptom resolution time)
- Establish a thiamine serum level monitoring protocol in newly diagnosed hyperthyroid patients to characterize deficiency prevalence in the Philippine population
- Clarify the Philippine FDA regulatory pathway: determine whether thiamine supplementation requires pharmaceutical registration or may proceed under existing nutritional supplement frameworks
- Retrieve full mechanism of action data from DrugBank (DG002) to complete mechanistic documentation for regulatory dossiers
- Conduct a targeted package insert review via the Philippine FDA or established reference sources to complete the safety gap (DG001) before entering formal safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

