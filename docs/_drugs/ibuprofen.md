---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Ibuprofen: From Arthritis and Pain Conditions to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, headache and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, but **no clinical trials and no publications** currently support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, headache disorder, patent ductus arteriosus (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ibuprofen is a non-selective COX inhibitor, and its anti-inflammatory and analgesic effects are established in arthritis-related conditions.

Acromesomelic dysplasia, Hunter-Thompson type, is a skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5, which affect cartilage formation. COX inhibition would not be expected to correct this genetic defect, so no mechanistic link is supported. The very high TxGNN score most likely reflects proximity in the knowledge graph to musculoskeletal and arthropathy terms rather than a biologically validated relationship.

At most, any benefit would be symptomatic, such as joint pain relief, and even that is not backed by data compiled for this report.

Other predicted indications show the same pattern. Their scores range from 99.60% to 99.71%, all are L5, and all are recommended Hold:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.71% | Genetic skeletal and enamel defect; no plausible mechanism |
| 3 | Myosclerosis | 99.68% | Muscle and tendon fibrosis; symptomatic relief conceivable but speculative |
| 4 | Brachyolmia | 99.67% | Heritable skeletal dysplasia; no plausible mechanism |
| 5 | Brachydactyly-syndactyly syndrome | 99.66% | Congenital limb malformation; no plausible mechanism |
| 6 | Pseudoachondroplasia | 99.66% | COMP mutation; symptomatic joint-pain overlap only |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.60% | Ultra-rare syndrome; no mechanistic rationale |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0240 | Ibuprofen | Not specified | Not specified (status: cancelled) |

The only registration found for the Philippines is cancelled, so there is currently no valid marketing authorization for ibuprofen based on the data compiled for this report.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text, so they must be verified against the package insert). Disease areas flagged include:
  - **Cardiovascular and cerebrovascular:** hypertension, hypotension, stroke, cerebrovascular disorder, cerebral infarction, myocardial infarction
  - **Gastrointestinal:** peptic ulcer disease, inflammatory bowel disease, gallbladder disease
  - **Liver and kidney:** liver failure, liver disease, kidney disease, pyoureter
  - **Blood and coagulation:** thrombocytopenia, blood coagulation disease
  - **Respiratory:** chronic obstructive pulmonary disease
  - **Endocrine and metabolic:** diabetes mellitus, diabetic ketoacidosis, hypothyroidism, potassium deficiency
  - **Other:** epilepsy, systemic lupus erythematosus, benign prostatic hyperplasia, substance abuse/dependence
- **Drug Interactions** (100 interactions recorded; the first 20 are shown in the data compiled for this report):
  - **Major:** acetylsalicylic acid (aspirin)
  - **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, aprepitant, balsalazide, fenfluramine, dexfenfluramine, kanamycin, levofloxacin
  - **Minor:** famotidine, ranitidine, cimetidine

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the proposed mechanism is not biologically plausible for a genetic skeletal dysplasia, and the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for ibuprofen (currently a data gap)
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently a blocking gap for safety screening)
- Preclinical or clinical evidence linking COX inhibition to the disease, or a clearly defined symptomatic goal (e.g., pain management) with supporting data
- Clarification of the regulatory situation, since the only registration is cancelled
- Reassessment of the other predicted indications; none has supporting evidence at present
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

