---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Keratolytic Agent to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is a well-established keratolytic and mild anti-inflammatory agent, widely used in dermatology for conditions such as acne, warts, psoriasis, and calluses.
The TxGNN model predicts it may have activity in **Papillary Conjunctivitis**,
but with **0 clinical trials** and **0 publications** currently supporting this direction, the evidence base is minimal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Keratolytic agent (acne, warts, psoriasis, hyperkeratosis) — not registered in the Philippines |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, salicylic acid is a beta-hydroxy acid with keratolytic properties and weak anti-inflammatory activity. Its anti-inflammatory effects are thought to derive from inhibition of NF-κB signalling and suppression of prostaglandin synthesis — pathways relevant to inflammatory tissue responses more broadly.

Papillary conjunctivitis is an inflammatory condition of the conjunctiva characterised by papillary hypertrophy, often associated with mechanical irritation (e.g., contact lens wear) or allergic triggers. The theoretical mechanistic link lies in salicylic acid's ability to dampen local inflammatory mediator release, which could in principle reduce conjunctival inflammation and papillary proliferation.

However, this mechanistic bridge is highly speculative. Salicylic acid is primarily used topically on skin, and its application to the ocular surface raises significant safety concerns — in particular, corneal epithelial toxicity and mucosal irritation. No clinical or preclinical studies have investigated this indication, and the TxGNN prediction likely reflects indirect graph-proximity relationships in the knowledge graph rather than a validated pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data was found in the query log, and key warnings and contraindications were not available in this Evidence Pack. Before any ophthalmic use is considered, corneal and mucosal toxicity data must be established through preclinical studies.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this Evidence Pack are rated L5 — model prediction only, with no supporting clinical trials or published literature for any of them. The top indication (papillary conjunctivitis) has a plausible but unvalidated mechanistic link, while the remaining nine predictions (predominantly rare skeletal dysplasias and genetic developmental syndromes) have little to no mechanistic basis for salicylic acid intervention.

**To proceed, the following is needed:**

- **Preclinical ocular safety data**: Confirm whether salicylic acid is tolerable on the conjunctival surface at therapeutic concentrations (corneal toxicity, mucosal irritation)
- **MOA clarification**: Retrieve full DrugBank mechanism of action data (DG002 remediation) to assess anti-inflammatory pathway specificity
- **Regulatory baseline**: Confirm Philippines FDA registration status and retrieve any available package insert warnings (DG001 remediation)
- **Exploratory literature review**: Conduct a broader PubMed search using salicylate/salicylate derivatives and conjunctivitis/ocular inflammation to identify any proximal evidence
- **De-prioritise skeletal dysplasia predictions**: Ranks 2–9 involve structural genetic conditions (GDF5, COMP, FAM20A mutations) where small-molecule intervention is not feasible with current salicylic acid pharmacology — these should be deprioritised without further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

