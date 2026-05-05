---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the `txgnn-pipeline` skill to confirm context. Now I'll generate the evaluation report based on the Evidence Pack.

---

# Mupirocin: From Topical Skin Infection to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic used for skin infections such as impetigo and MRSA nasal decolonization, with no systemic formulation available.
The TxGNN model predicts it may be effective for **Pleural Empyema** with a score of **99.49%**,
however **zero clinical trials** and **zero publications** support this direction, and a critical route-of-administration incompatibility renders this a high-probability false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical skin infections (impetigo, MRSA decolonization) |
| Predicted New Indication | Pleural Empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Mupirocin is a topical antibiotic that works by inhibiting bacterial isoleucyl-tRNA synthetase (IleRS) — a target absent in human cells — thereby blocking protein synthesis in gram-positive bacteria. It shows particularly high activity against *Staphylococcus aureus* (including MRSA) and *Streptococcus milleri* group organisms.

Pleural empyema is a purulent infection of the pleural space most frequently caused by exactly these gram-positive pathogens — *S. aureus* and streptococcal species. The TxGNN knowledge graph almost certainly generated this high-scoring prediction by tracing an "antibiotic → gram-positive bacteria → bacterial infection" pathway, correctly identifying mechanistic compatibility between Mupirocin's target spectrum and empyema's causative organisms.

However, there is a fatal pharmacokinetic barrier: **Mupirocin exists only as a topical formulation** (skin ointment, nasal ointment). No oral, intravenous, or intrapleural formulation has been developed or approved. Topical application cannot achieve measurable drug concentrations in the pleural cavity. The knowledge graph model does not encode route-of-administration constraints, making this a **classic high-score false positive** — mechanistically plausible at the molecular level, but pharmacologically non-viable in current form.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score (99.49%), the complete absence of clinical or literature evidence combined with an irreconcilable route-of-administration mismatch — a topical-only drug cannot reach the pleural space — makes this repurposing hypothesis non-actionable under current formulation constraints.

**To proceed, the following would be needed:**
- Development of a novel intrapleural or systemic Mupirocin formulation (a significant pharmaceutical R&D undertaking)
- Preclinical proof-of-concept studies in animal empyema models using the novel delivery route
- MOA documentation from DrugBank to formally confirm antibacterial spectrum and IleRS inhibition profile
- TFDA/FDA Philippines package insert review to resolve the blocking safety data gap (DG001)
- Consideration of re-evaluating the second predicted indication (punctate epithelial keratoconjunctivitis) which shares a similar evidence gap but may be more route-compatible as an ophthalmic application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

