---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 226
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is a widely used glucose-lowering drug, originally indicated for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, metformin activates AMPK, inhibits mitochondrial complex I, and has anti-inflammatory effects. Its efficacy in type 2 diabetes is well established.

Focal stiff limb syndrome is a variant of the stiff-person spectrum, an autoimmune disorder involving anti-GAD65 or related antibodies and impaired GABAergic inhibition. There is no established link between metformin's mechanisms and this pathway. A possible connection is the shared GAD-autoimmunity background with diabetes, or a general immunomodulatory effect, but this is speculative and not supported by the data compiled.

The model also gave an identical score (0.9945) to classic stiff person syndrome. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the data, all with L5 evidence and a Hold recommendation:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 0.9945 | Comorbid diabetes may explain the association; no evidence metformin treats the neurological disease |
| 3 | Opsismodysplasia | 0.9940 | INPPL1/SHIP2 loss affects PI3K/AKT and insulin signalling; plausible pathway link but untested, and paediatric safety not assessed |
| 4 | Thiamine-responsive dysfunction syndrome | 0.9940 | Diabetes is a feature, but the defect is thiamine transport and the standard treatment is thiamine |
| 5 | Drug-induced localized lipodystrophy | 0.9906 | Most mechanistically plausible (metformin has been studied in other lipodystrophies), but unvalidated here |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

Only one registration is on record, and it is cancelled. Dosage form and approved indication text are not available.

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0314 | Metformin | Valid |

## Safety Considerations

- **Contraindication signals (knowledge-graph, not label text)**: The TxGNN knowledge graph links metformin to contraindications in the following areas:
  - Liver: liver failure, liver disease
  - Kidney and urinary tract: kidney disease, pyoureter
  - Digestive: pancreatitis, gallbladder disease
  - Cardiac: congestive heart failure
  - Endocrine: adrenocortical insufficiency, thymus gland disease, and multiple pituitary hormone deficiency conditions (hypopituitarism, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome, among others)
- **Drug Interactions**: 100 interactions were found in total; the first 20 returned include:
  - **Major**: Acetazolamide, Ethanol
  - **Moderate**: Dolutegravir, Abemaciclib, Phenylephrine, Ranitidine, Formoterol, Pseudoephedrine, Ketorolac, Nifedipine, Epinephrine, Ibuprofen, Ethinylestradiol, Hydrocortisone, Salbutamol, Hydrochlorothiazide, Acetohexamide
  - **Minor**: Acarbose, topical Hydrocortisone, topical Alclometasone

Package insert warnings and contraindications for the Philippines were not obtained. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications, and the mechanistic link to stiff-person spectrum disorders is speculative.

**To proceed, the following is needed:**
- Systematic literature and trial searches for metformin in stiff-person spectrum disorders
- Mechanism of action data (e.g. from DrugBank)
- Philippines package insert warnings and contraindications from the DOH-FDA Philippines website
- Preclinical or mechanistic studies to test whether any plausible link exists
- If any prediction is pursued, lipodystrophy is the most mechanistically plausible candidate to prioritise for evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

