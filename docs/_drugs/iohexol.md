---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Iohexol: predicted new indication insomnia (disease) (evidence level L5). Approved use: Not stated in the Philippines registration record (iohexol is general…"
monitor_inn: "Iohexol"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Iohexol: From Diagnostic Contrast Imaging to insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Iohexol is a non-ionic, iodinated contrast agent used as a diagnostic imaging aid. The TxGNN model predicts it may be effective for **insomnia**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The evidence is model prediction only, and the score most likely reflects a TxGNN model (deep learning) artifact rather than real biology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration record (iohexol is generally used as a diagnostic contrast agent) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iohexol is a non-ionic, iodinated contrast agent. It is pharmacologically inert, is not metabolised, and is excreted unchanged by the kidneys.

**No mechanistic link to insomnia was identified.** Iohexol has no known activity on sleep-regulating pathways (GABAergic, orexinergic, histaminergic, or melatonergic). The very high TxGNN score (0.9987) most likely reflects TxGNN model (deep learning) artifacts, such as shared drug-drug interaction neighbours or network proximity, rather than a biological rationale. The prediction should therefore be treated as a computational signal only.

The second-ranked prediction, **anxiety** (score 0.9925), is also unsupported. Iohexol has no anxiolytic pharmacology. The four publications retrieved for it concern iohexol as a diagnostic agent or are unrelated papers. Anxiety appears at most as a procedural or adverse-event context, not as a therapeutic outcome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for insomnia. For the second-ranked prediction (anxiety), four publications were retrieved, but none is repurposing evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Double-blind comparison of iodixanol and iohexol in extremity phlebography (efficacy, safety, injection discomfort). Not related to anxiety treatment. |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohort | Neuroradiology | Side effects in 200 patients after lumbar iohexol myelography. Headache, nausea and dizziness were common, and minor mental symptoms (such as anxiety or depression) were reported as adverse effects. |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Physiological study | Acta Neurochirurgica | Concurrent two-vessel Doppler monitoring of cerebral haemodynamics during cerebral angiography. Not related to anxiety treatment. |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Review | Nutrients | Nutrition and physical activity in onco-nephrology. Not related to iohexol as an anxiety treatment. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0254 (cancelled) | Iohexol | Not stated | Not stated |

---

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interactions in total. Most of those listed are rated Major. Examples include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Metformin
- Nephrotoxic or ototoxic agents: amphotericin B (including lipid complex), vancomycin, kanamycin, neomycin
- Levofloxacin
- Bupropion
- Metoclopramide
- Morphine
- Mesalazine and balsalazide
- Appetite suppressants and related agents: diethylpropion, phentermine, dronabinol

Mannitol is rated Moderate.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or supporting literature, and no plausible mechanism. The drug is marketed in the Philippines, with 1 valid licence of 1. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanistic evidence linking iohexol to sleep regulation (none is currently known)
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data from DrugBank
- Preclinical or clinical studies in insomnia, if the hypothesis is still pursued
- A valid local registration and route compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

