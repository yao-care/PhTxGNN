---
layout: default
title: Diclofenac
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Diclofenac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Diclofenac: From Arthritis and Actinic Keratosis to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a nonsteroidal anti-inflammatory drug (NSAID) used for conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and actinic keratosis.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare genetic hair disorder.
This prediction is supported by **0 clinical trials** and **0 publications**, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, actinic keratosis (the Philippine registration lists no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. As an NSAID, diclofenac is generally understood to inhibit COX-1 and COX-2 enzymes and so reduce prostaglandin-mediated inflammation and pain. This explains its use in arthritis and inflammatory skin lesions.

That mechanism does not link well to the predicted disease. Hypotrichosis simplex of the scalp is a rare inherited hair disorder, and COX inhibition has no established role in its development. The high score (99.69%) appears to reflect proximity within the knowledge graph rather than a pharmacological rationale. No data compiled for this report support a mechanistic connection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0141 | Diclofenac | Cancelled |

This is the only registration, and it is cancelled. No valid single-ingredient or combination registrations exist. Dosage form and approved indication are not recorded.

## Safety Considerations

- **Contraindications / conditions of concern (from the knowledge graph, not label text):**
  - Cardiovascular: hypertension, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, other cardiovascular and heart disease.
  - Gastrointestinal and hepatic: active peptic ulcer disease, inflammatory bowel disease, liver disease and liver failure, drug-induced liver injury, gallbladder disease.
  - Haematological: blood coagulation disorders, anaemia (including macrocytic), haemoglobinopathy.
  - Respiratory: asthma (intrinsic and allergic).
  - Metabolic: diabetes mellitus, diabetic ketoacidosis.
  - Other: substance abuse/dependence, keratitis.
- **Drug Interactions:** The interaction query returned 100 records, and the 20 reviewed here include these main ones.
  - Moderate: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, sulfonylureas (glimepiride, glipizide, chlorpropamide, acetohexamide), exenatide, aprepitant, and mesalazine and balsalazide.
  - Minor: H2 blockers (famotidine, ranitidine, cimetidine).

Warnings and contraindications from the official Philippine package insert were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials or publications, no supported mechanism, and the Philippine registration is cancelled.

Of the top 10 predictions, only juvenile idiopathic arthritis (rank 9, TxGNN score 99.25%) has any supporting literature, at evidence level L3. It consists of small, older paediatric studies from 1978 to 1990, including a 28-child crossover comparison with naproxen and tolmetin and open-label diclofenac cohorts. This use is already within standard NSAID practice, so it is not a true repurposing opportunity. It would be the better candidate for any follow-up.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA).
- The package insert for warnings and contraindications.
- Any preclinical or clinical evidence linking COX inhibition to hair-follicle biology.
- Clarification of the cancelled registration status and the availability of any current Philippine product.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

