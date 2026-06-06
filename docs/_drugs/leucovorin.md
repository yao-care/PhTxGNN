---
layout: default
title: Leucovorin
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 2
---

# Leucovorin
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

# Leucovorin: From Methotrexate Rescue to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid) is the metabolically active, reduced form of folic acid, clinically established as a rescue agent following high-dose methotrexate therapy, a modulator in 5-FU–based chemotherapy regimens, and a treatment for folate deficiency states.
The TxGNN model predicts it may be effective for **Primary Hyperoxaluria**, yet this direction is supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph inference.
Evidence level is **L5**; this candidate requires substantial preclinical work before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Methotrexate rescue; 5-FU potentiation in colorectal cancer; folate deficiency |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Leucovorin (5-formyl-tetrahydrofolate, 5-formyl-THF) enters the active tetrahydrofolate (THF) pool directly, bypassing the dihydrofolate reductase (DHFR) step that is blocked by methotrexate. It supports one-carbon transfer reactions central to thymidylate synthesis, purine biosynthesis, and amino acid interconversion — most notably the serine ↔ glycine equilibrium catalyzed by serine hydroxymethyltransferase (SHMT).

The proposed mechanistic link to **Primary Hyperoxaluria Type 1 (PH1)** is indirect and speculative. The hypothesized pathway runs: Leucovorin → replenishment of active folate → enhanced SHMT activity → increased serine→glycine flux → theoretically elevated glyoxylate-to-glycine conversion → reduced accumulation of oxalate precursors. However, the rate-limiting defect in PH1 is loss-of-function in **AGXT** (alanine:glyoxylate aminotransferase), an enzyme whose cofactor is pyridoxal-5-phosphate (vitamin B6), not folate. There is no direct biochemical connection between Leucovorin supplementation and AGXT activity or glyoxylate detoxification. Biological plausibility is rated **low**.

TxGNN most likely inferred this association via graph edges linking "folate metabolism ↔ one-carbon metabolism ↔ amino acid metabolism" within the knowledge graph — a path that is topologically adjacent but mechanistically distal from PH1 pathophysiology. The standard of care for PH1 already includes pyridoxine (B6) and, for severe cases, Lumasiran (an RNA interference therapy targeting LDHA/HOGA1), which holds regulatory approval. Leucovorin offers no apparent advantage over these established agents in this disease context.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Leucovorin is currently **not registered** in the Philippines (FDA Philippines). No active drug licenses were identified in the regulatory database for this candidate.

> **Note:** The absence of a Philippines registration means local pharmacovigilance data, approved labeling, and physician familiarity are unavailable. Any future clinical program would require de novo regulatory engagement with the FDA Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug–drug interactions) were not retrievable from available sources at the time of this report. Leucovorin is generally regarded as well-tolerated, but clinically important interactions with antifolate agents (methotrexate, trimethoprim, pyrimethamine) and antiepileptics (phenobarbital, phenytoin) have been documented in international prescribing information and should be reviewed before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a numerically high TxGNN score (99.41%), the proposed mechanism connecting Leucovorin to primary hyperoxaluria is biochemically distant — the PH1 defect lies in a B6-dependent enzyme (AGXT) with no direct folate dependency — and zero clinical or preclinical studies support this repurposing direction. Approved targeted therapies already exist for PH1, raising the bar for any new entrant.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro/in vivo studies in AGXT-deficient models to test whether folate supplementation measurably reduces glyoxylate accumulation or urinary oxalate levels
- **MOA documentation**: Query DrugBank API (DB00650) to obtain complete mechanism of action, pharmacokinetic parameters, and toxicity profile
- **Regulatory package**: Download Philippines FDA package insert (or equivalent international SmPC) to populate key warnings, contraindications, and DDI sections — currently all blocking data gaps
- **Comparative landscape review**: Map Leucovorin against current PH1 standard of care (pyridoxine, Lumasiran, conservative dietary measures, dialysis/liver transplant for end-stage disease) to identify any plausible adjunctive or niche role
- **Second prediction consideration**: The second TxGNN-ranked indication — **Congenital Intrinsic Factor Deficiency** (score 99.34%) — carries a more coherent mechanistic rationale (methylfolate trap bypass) but poses a documented clinical safety risk (masking of B12-dependent neurological deterioration). If resources allow, this indication warrants a parallel preclinical safety assessment before the primary hyperoxaluria pathway is pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

