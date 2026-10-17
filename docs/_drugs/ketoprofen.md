---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
---

# Ketoprofen
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

# Ketoprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and other joint disorders.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoprofen is a non-selective cyclooxygenase (COX) inhibitor in the NSAID class. Its efficacy in joint pain and inflammation (rheumatoid arthritis, osteoarthritis) is established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway. COX inhibition does not address this underlying biology, and no plausible mechanistic connection was identified. The high score most likely reflects the knowledge graph's proximity between this disease and musculoskeletal conditions such as arthropathy and osteoarthritis, rather than a true biological link. At most, an NSAID might offer symptomatic pain relief, not disease modification.

**Other predictions reviewed.** The top 10 predictions were all L5, with no trials or literature. Most are rare skeletal or developmental syndromes with no mechanistic rationale (e.g., brachyolmia, myosclerosis, WHIM syndrome). Two are biologically more plausible and flagged as research questions:
- **Spondyloarthropathy, susceptibility to** (score 99.86%): NSAIDs are first-line symptomatic therapy for spondyloarthritis, so this is likely a rediscovery of known class use rather than a novel repurposing.
- **Juvenile arthritis due to defect in LACC1** (score 99.74%): NSAIDs are commonly used for symptomatic control of juvenile arthritis, but the effect is unlikely to be disease-modifying.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0273 | Ketoprofen | Not specified | Not specified (registration status: cancelled) |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension/hypertensive disorder, liver failure, kidney disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular/heart disease, hemoglobinopathy, pyoureter.
- **Drug Interactions** (100 interactions found; examples below):
  - *Moderate*: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, naltrexone, potassium citrate/bicarbonate, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - *Minor*: famotidine, ranitidine, cimetidine, linaclotide

Please refer to the package insert for warnings and full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials or literature and no plausible mechanism for this rare genetic skeletal disorder. The only local registration has been cancelled, which further limits practical development.

**To proceed, the following is needed:**
- Mechanism of action data for ketoprofen (e.g., from DrugBank)
- Package insert warnings and contraindications (from DOH-FDA Philippines)
- A targeted literature search on NSAID use in spondyloarthropathy and LACC1-related juvenile arthritis, the two more plausible candidates, which would be better prioritised than the top-ranked prediction
- Clarification of whether a valid ketoprofen product is available in the Philippines, given the cancelled registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

