---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Bacitracin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bacitracin: From Bacterial Skin Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic used topically for the prevention and treatment of bacterial skin infections and wound care, with activity concentrated against gram-positive organisms.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** (TxGNN rank #29, score 99.999%),
though **0 clinical trials** and **0 publications** were identified for this specific indication — the prediction is supported by mechanistic plausibility and the existing availability of Bacitracin ophthalmic formulations in other markets.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical bacterial skin infections and wound prophylaxis |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on established pharmacology, Bacitracin is a polypeptide antibiotic that inhibits bacterial cell wall synthesis by interfering with the dephosphorylation of the lipid carrier (undecaprenyl pyrophosphate) required for peptidoglycan precursor transport. This mechanism confers bactericidal activity predominantly against gram-positive organisms — particularly *Staphylococcus aureus*, streptococcal species, and *Corynebacterium* — while having limited effect against gram-negative bacteria. Because it is poorly absorbed through intact skin and mucosa, it is used almost exclusively as a topical agent.

Punctate epithelial keratoconjunctivitis (PEK) is characterized by multifocal, fine erosions of the corneal and conjunctival epithelium. While its aetiology is multifactorial (viral, toxic, dry-eye associated), secondary bacterial colonization — especially staphylococcal blepharoconjunctivitis — is a well-recognized trigger and perpetuating factor. Bacitracin ophthalmic ointment is already commercially available in the United States (e.g., brand *AK-Tracin*) as a topical ocular antibiotic for susceptible bacterial conjunctivitis and blepharitis, providing an established formulation and ocular safety precedent.

The TxGNN knowledge graph likely captures this association through shared disease-pathogen nodes linking gram-positive ocular bacterial infections to PEK. The high prediction score (99.999%, global rank #29) reflects strong graph-level structural support, though no dedicated clinical evidence for PEK as a primary indication has been retrieved. Prospective validation is required before drawing clinical conclusions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

---

## Philippines Market Information

Bacitracin is **not currently registered** with the Philippine FDA. No product licenses were identified in the regulatory database (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. Key regulatory data — including package insert warnings, contraindications, and drug interaction profiles — are not available in this evidence pack. Retrieval from the Philippine FDA official database and DrugBank is required before initiating any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is exceptionally high and a mechanistic link between Bacitracin's gram-positive antibacterial activity and bacterial-associated PEK is biologically plausible, there is currently no clinical trial or published study specifically supporting this indication, and Bacitracin has no existing market authorization in the Philippines.

**To proceed, the following is needed:**
- Retrieve the full package insert (MOA, warnings, contraindications) via DrugBank API and Philippine FDA official sources to complete the S1 safety pre-screen
- Conduct a targeted literature search (PubMed/EMBASE) using terms: *Bacitracin AND (keratoconjunctivitis OR conjunctivitis OR blepharitis OR ocular infection)* to assess indirect supporting evidence
- Confirm the availability and regulatory pathway for importing or locally manufacturing an ophthalmic-grade Bacitracin formulation in the Philippines
- Evaluate whether evidence from otitis externa (rank #4, L3, 6 publications including one RCT-class trial) represents a more clinically actionable repurposing target in the near term
- Design a prospective case series or observational study as the first clinical evidence step if the safety screen is passed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

