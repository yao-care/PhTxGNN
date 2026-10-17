---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis…"
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From Inflammatory and Musculoskeletal Pain Conditions to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for inflammatory and musculoskeletal conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis, tendinitis and migraine.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, migraine, osteoarthritis and related conditions (from the knowledge graph; no approved-indication text is available for the local registration) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology knowledge, naproxen is a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, which explains its anti-inflammatory, analgesic and antipyretic effects in its original indications.

Brachydactyly-syndactyly syndromes are congenital limb malformations, typically caused by developmental genetic defects (for example, variants in the HOX gene family). Blocking prostaglandin synthesis is not expected to correct a structural malformation that forms during development. The high TxGNN score (0.994, rank 4669) is a graph-based prediction and most likely reflects network proximity rather than biological plausibility.

In short, **no mechanistic link is supported by the available data**. At most, naproxen might be considered for symptomatic pain relief, which is not a disease-modifying repurposing rationale. NSAID exposure during pregnancy also carries fetal safety concerns.

Other predictions with the same pattern (high score, no evidence, no mechanistic link):

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.22% | L5 |
| 3 | Acromesomelic dysplasia, Hunter-Thompson type | 99.17% | L5 |
| 4 | Brachyolmia-amelogenesis imperfecta syndrome | 99.06% | L5 |

All four are rare congenital skeletal or developmental disorders of genetic origin. None has supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0341 | Naproxen | Not specified | Not specified (registration cancelled) |

## Safety Considerations

- **Contraindications / risk conditions flagged in the knowledge graph** (these come from the drug-disease network, not from package insert text): hypertension, congestive heart failure, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, liver disease and liver failure, kidney disease, blood coagulation disorders, anemia and hemoglobinopathy, diabetes mellitus and diabetic ketoacidosis, osteoporosis, epilepsy, gallbladder disease, benign prostatic hyperplasia, obesity, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were found in total, and the 20 listed are all rated Moderate. Main ones include:
  - Acid-suppressing drugs: famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Other drugs: acetylsalicylic acid, metformin, chlorpropamide, aprepitant, mesalazine, balsalazide, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes
- **Pregnancy**: NSAID exposure during pregnancy raises fetal safety concerns, which is particularly relevant for congenital developmental conditions.

Please refer to the package insert for label-level warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature (Evidence Level L5). The biological rationale is also weak, because COX inhibition is not expected to correct congenital limb malformations. The only local registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between COX inhibition and the target syndrome
- Preclinical or case-based evidence in the predicted disease
- Package insert warnings and contraindications for the local product, and an assessment of fetal safety
- Clarification of the current regulatory status in the Philippines, since the only registration (PNF-0341) is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

