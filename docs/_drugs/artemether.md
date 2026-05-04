---
layout: default
title: Artemether
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From Malaria Treatment to Acquired Angioedema

## One-Sentence Summary

Artemether is a lipid-soluble artemisinin derivative, used as the backbone of artemisinin-based combination therapy (ACT) — most notably artemether-lumefantrine (Coartem) — and is globally established for treating uncomplicated and severe malaria caused by *Plasmodium falciparum*.
The TxGNN model ranks **Acquired Angioedema** as its top novel predicted indication, with a score of 99.90%;
however, **no clinical trials** and **no published literature** currently support this repurposing direction, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (*Plasmodium falciparum* and other species) |
| Predicted New Indication | Acquired Angioedema |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on known pharmacology, Artemether is a methyl ether derivative of dihydroartemisinin. Its core antimalarial activity stems from the endoperoxide bridge reacting with intraparasitic ferrous heme iron (Fe²⁺) to generate reactive oxygen species (ROS) and carbon-centered radicals, which selectively alkylate parasite proteins — including PfATP6 (a sarcoplasmic/endoplasmic reticulum Ca²⁺-ATPase) and histone proteins — disrupting membrane integrity and inducing oxidative death in asexual *P. falciparum* stages (trophozoites and schizonts). Beyond its antiparasitic activity, preclinical literature suggests that artemisinin-class compounds can also suppress NF-κB signaling and modulate complement activation.

Acquired angioedema is mechanistically driven by deficiency or dysfunction of C1-inhibitor (C1-INH), which leads to uncontrolled activation of the contact pathway, excessive kallikrein activity, and accumulation of bradykinin — ultimately causing episodic, self-limiting subcutaneous or submucosal edema. This pathway is pharmacologically distinct from any established target of artemether.

The proposed mechanistic hypothesis linking the two involves: artemether's NF-κB inhibitory activity → reduced downstream pro-inflammatory mediators (IL-1β, TNF-α) → theoretical attenuation of vascular permeability; and a secondary hypothesis that artemisinin compounds may inhibit Factor XII or kallikrein-kinin pathway components. Both hypotheses remain entirely unvalidated experimentally. The high TxGNN score most likely reflects broad "inflammation" node connectivity within the knowledge graph rather than a disease-specific mechanistic link to acquired angioedema.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Artemether in acquired angioedema.

---

## Literature Evidence

Currently no related literature available for Artemether in acquired angioedema.

---

## Philippines Market Information

Artemether is not currently registered with the FDA Philippines. No product authorizations are on record (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported by computational graph inference alone (L5); there is no clinical trial, no published literature, and no validated mechanistic pathway connecting artemether to acquired angioedema's core pathophysiology (C1-INH deficiency → bradykinin excess). The drug is also not registered in the Philippines, adding an additional regulatory barrier.

**To proceed, the following is needed:**
- In vitro mechanistic studies to determine whether artemether or its active metabolite dihydroartemisinin affects C1-INH activity, Factor XII activation, or kallikrein-kinin pathway components
- A systematic literature review on artemisinin-class compounds and complement/bradykinin system interactions
- Animal model validation (e.g., C1-INH-knockout or bradykinin-induced edema models) before any human studies
- Full safety characterization relevant to the acquired angioedema population, including interactions with current standard-of-care agents (C1-INH concentrates, icatibant, lanadelumab)
- Philippines FDA registration strategy if preclinical findings prove favorable

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

