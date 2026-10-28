---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). Approved use: Schizophrenia, bipolar disorder (including mania)…"
monitor_inn: "Risperidone"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
---

# Risperidone
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

## Risperidone: From Schizophrenia and Bipolar Disorder to Gaze Palsy, Familial Horizontal, with Progressive Scoliosis
{: .text-alpha }

## One-Sentence Summary

Risperidone is an antipsychotic originally used for schizophrenia, bipolar (manic) disorder and autism-related conditions.
The TxGNN model predicts it may be effective for **gaze palsy, familial horizontal, with progressive scoliosis**, a rare genetic disorder.
**No clinical trials and no publications** currently support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, bipolar disorder (including mania), autism spectrum disorder (the Philippines license record contains no indication text) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Risperidone is generally known as a dopamine D2 and serotonin 5-HT2A antagonist. Its efficacy in psychotic and mood disorders is established.

The predicted disease is a rare genetic disorder (ROBO3-related) of axon guidance and hindbrain development. It causes absent horizontal eye movements and progressive scoliosis. Blocking D2/5-HT2A receptors has no plausible role in correcting this structural neurodevelopmental defect, and no mechanistic link could be identified. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction should not be treated as a credible repurposing opportunity without independent supporting data.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0425 | Risperidone | Valid |

The record contains no dosage form or approved indication text. The drug is marketed in this country, with 1 valid license of 1.

## Safety Considerations

- **Contraindication-related conditions from the knowledge graph** (drug-disease contraindication links, not label text):
  - Cardiovascular and cerebrovascular: myocardial infarction, coronary thrombosis, heart conduction disease, sudden cardiac arrest, heart disease, stroke and cerebral infarction, orthostatic and other hypotension.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, obesity.
  - Haematological: neutropenia, agranulocytosis.
  - Hepatic and biliary: liver disease or failure, gallbladder disease.
  - Neurological: epilepsy, multiple system atrophy.
  - Other: postural orthostatic tachycardia syndrome, female breast carcinoma, hemoglobinopathy.
- **Drug Interactions**: 100 interactions were recorded.
  - **Major**: bupropion, morphine.
  - **Moderate**, among others: metformin, acarbose, alogliptin, canagliflozin, albiglutide (antidiabetic agents); epinephrine; hydrocortisone; amphotericin B; atropine, hyoscyamine, glycopyrronium, clidinium (anticholinergics); loperamide; lorcaserin; bisacodyl; famotidine.
  - **Minor**: ranitidine.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links risperidone to this structural genetic disorder. The drug is marketed in the Philippines, with 1 valid license of 1.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking risperidone to ROBO3-related axon guidance defects
- Mechanism of action data and package insert warnings and contraindications
- Confirmation of the regulatory status of the cancelled registration PNF-0425

**Other candidates in the compiled data:** Other predicted indications for risperidone have stronger support than this one. The strongest is **major affective disorder** (treatment-resistant major depression, adjunctive use). It is rated L1 and supported by two completed Phase 3 trials (NCT00095134, n=630; NCT00044681, n=258) and several meta-analyses. Its suggested decision is Proceed with Guardrails: metabolic monitoring, prolactin, extrapyramidal symptoms, QT considerations and the high interaction burden. This category partly overlaps with the existing bipolar indication, and trial outcomes should be confirmed from the primary publications. **Trichotillomania** (L3, case reports and small case series only) and **Phelan-McDermid syndrome** (L4, preclinical evidence) are best treated as research questions. A separate report on these candidates would be a more productive next step than pursuing the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

