---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rifaximin: From Gastrointestinal Infections to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a minimally-absorbed oral antibiotic with established uses in traveler's diarrhea, hepatic encephalopathy, and irritable bowel syndrome with diarrhea (IBS-D). The TxGNN model predicts it may be effective for **Oral Candidiasis**, with **0 clinical trials** and **1 publication** identified — notably, the sole available study reports a **negative association**, suggesting rifaximin use may *promote* rather than treat Candida infections.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal infections (traveler's diarrhea, hepatic encephalopathy) |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Rifaximin is a rifamycin-derived, minimally-absorbed oral antibiotic (bioavailability <0.4%) that acts locally within the gastrointestinal lumen by inhibiting bacterial RNA polymerase. Its established indications — traveler's diarrhea, reduction of overt hepatic encephalopathy episodes, and IBS-D — all depend on gut-luminal bacterial suppression without meaningful systemic drug exposure.

Oral candidiasis (thrush) is a fungal infection caused by *Candida* species on the oral mucosa, managed with topical antifungals (nystatin, clotrimazole) or systemic azoles. Because rifaximin achieves negligible plasma concentrations and has no antifungal properties, it cannot reach therapeutically relevant concentrations in oral mucosal tissue. The only indirect mechanistic link — that prolonged antibiotic use disrupts normal microbiota, creating ecological space for *Candida* overgrowth — describes a **risk mechanism**, not a treatment mechanism.

Critically, the one publication retrieved runs **counter** to a therapeutic hypothesis. A 2021 retrospective cohort study in allogeneic hematopoietic stem cell transplant recipients found that rifaximin prophylaxis was associated with *increased* micafungin-resistant *Candida* infections, consistent with antibiotic-driven dysbiosis facilitating fungal opportunism. The TxGNN high confidence score most likely captures this bidirectional biological association rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Retrospective Cohort | Annals of Hematology | In allogeneic HSCT recipients receiving rifaximin as GvHD prophylaxis, rifaximin use was associated with **increased** incidence of micafungin-resistant *Candida* spp. infections — this is evidence of harm, not therapeutic benefit |

---

## Philippines Market Information

Rifaximin is currently **not registered** with the Philippine FDA. No product authorizations, brand names, or approved indications were found in the Philippine regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN score of 99.75%, rifaximin has no antifungal mechanism, cannot achieve effective concentrations at the oral mucosa, and the only available clinical evidence demonstrates that rifaximin use *increases* — not decreases — Candida infection risk. This prediction appears to reflect a statistically captured co-occurrence signal rather than a clinically actionable therapeutic relationship.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank API query pending; DG002)
- Philippine FDA package insert and approved indications (DG001 — currently blocking safety assessment)
- Reassessment of whether other TxGNN-predicted indications for Rifaximin (e.g., gut microbiome-mediated systemic conditions such as minimal hepatic encephalopathy or small intestinal bacterial overgrowth) represent more mechanistically credible repurposing candidates
- Review of TxGNN signal directionality methodology to determine whether high scores for drug–disease pairs with known adverse associations can be systematically flagged
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

