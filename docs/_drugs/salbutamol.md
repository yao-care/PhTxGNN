---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: From Asthma to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol is a globally established short-acting β2-adrenoceptor agonist (SABA), widely recognized as a first-line bronchodilator for asthma and acute bronchospasm — though it carries no registered indication in the Philippines.
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**,
with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on the model's graph-based inference from the drug–disease knowledge network.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / Bronchospasm (globally established; no Philippines registration on record) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.9964% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for Salbutamol was not retrievable in this evidence pack. Based on well-established global pharmacology, Salbutamol is a selective β2-adrenoceptor agonist: it binds β2 receptors on airway smooth muscle, elevates intracellular cAMP via adenylyl cyclase activation, and produces rapid bronchodilation within 3–5 minutes. This mechanism is the cornerstone of asthma rescue therapy worldwide.

The theoretical bridge to papillary conjunctivitis rests on the presence of β2-adrenergic receptors in conjunctival mast cells and epithelial cells. Stimulating these receptors could, in principle, stabilize mast cells and suppress histamine release — thereby reducing the itch, chemosis, and papillary hypertrophy that define this condition. Related ocular pharmacology studies (guinea pig model, PMID 3666475; in vitro permeability data, PMID 2906082) have shown that topical β2 agonists can suppress immediate allergic conjunctival reactions, lending a degree of biological plausibility.

However, this mechanistic link remains entirely speculative for human papillary conjunctivitis. No clinical translation data exists. The TxGNN graph model identified this connection through proximity in its drug–disease knowledge network — not through observed clinical efficacy — and the absence of any supporting literature or trial registration means this prediction cannot currently be acted upon.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Salbutamol has no registered products in the Philippines as of the data cutoff (2026-06-06). No license records, approved indications, or dosage form information are available from the Philippine FDA registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.9964%), there is zero clinical or translational human evidence to support Salbutamol for papillary conjunctivitis. A high graph-based score reflects structural proximity in the knowledge network, not demonstrated efficacy. With no trials, no publications, no Philippines registration, and no MOA or safety data on file, this indication cannot advance beyond hypothesis stage.

**To proceed, the following is needed:**
- Retrieve full mechanism of action data from DrugBank (DG002 data gap resolution) to confirm β2-receptor expression in ocular tissues
- Obtain and review the complete package insert (DG001) for key warnings and contraindications before any ophthalmic formulation work
- Commission in vitro human conjunctival mast cell studies to confirm histamine-suppression activity at clinically relevant concentrations
- Assess feasibility of a topical ophthalmic formulation (Salbutamol eye drops) and confirm route compatibility
- Conduct a targeted literature search specifically for β2-agonist topical ophthalmic use in human subjects to establish whether any analogous precedent exists
- Philippines regulatory pathway assessment: new registration would be required from scratch given zero existing licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

