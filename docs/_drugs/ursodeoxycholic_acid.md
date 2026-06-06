---
layout: default
title: Ursodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ursodeoxycholic Acid: From Cholestatic Liver Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a naturally occurring bile acid used clinically for cholestatic liver diseases such as primary biliary cholangitis (PBC) and gallstone dissolution.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
however **no clinical trials** and **no publications** specifically supporting this repurposing direction were identified at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cholestatic liver disease (primary biliary cholangitis, gallstone dissolution) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

UDCA is a hydrophilic bile acid that modulates bile composition and exerts hepatoprotective effects. Its primary mechanism involves altering the bile acid pool to reduce hepatotoxic bile acid exposure, and it has established interactions with nuclear receptors including FXR (farnesoid X receptor) and downstream signaling through the SHP axis — pathways that sit at the intersection of bile acid and cholesterol metabolism.

The theoretical bridge to HoFH lies in this bile acid–cholesterol metabolic crosstalk. UDCA may mildly suppress LDL-C through modulation of the FXR/SHP axis and by inhibiting intestinal cholesterol reabsorption. This is pharmacologically plausible in populations with functional LDL receptors, where upstream pathway modulation can influence hepatic cholesterol clearance.

However, the critical limitation is that HoFH is defined by **biallelic loss-of-function mutations in LDLR**, leaving essentially no functional LDL receptor activity. Any benefit UDCA could theoretically exert through upstream pathway modulation becomes clinically irrelevant when the downstream effector (LDLR) is entirely absent. The high TxGNN score (0.9987) most likely reflects the topological proximity between bile acid metabolism nodes and hypercholesterolemia nodes in the underlying knowledge graph, rather than direct clinical feasibility. This is a case where graph-level connectivity does not translate to mechanistic viability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ursodeoxycholic acid in Homozygous Familial Hypercholesterolemia.

---

## Literature Evidence

Currently no related literature available for Ursodeoxycholic acid in Homozygous Familial Hypercholesterolemia.

---

## Philippines Market Information

Ursodeoxycholic acid is currently **not registered** with the Philippine FDA. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score based on knowledge graph topology, but the core pathology of HoFH — complete biallelic LDLR loss-of-function — mechanistically precludes meaningful benefit from UDCA's bile acid–cholesterol pathway modulation. With zero supporting clinical trials and zero publications, evidence is insufficient to advance this candidate.

**To proceed, the following is needed:**

- **Mechanistic validation:** In vitro or in vivo studies in LDLR-null models to determine whether UDCA exerts any cholesterol-lowering effect independent of LDLR (e.g., via PCSK9 suppression, ABCG5/8 induction, or NPC1L1 inhibition)
- **Epidemiological signal search:** Retrospective data from PBC/cholestasis patients who also carry familial hypercholesterolemia mutations, to observe whether UDCA use correlates with LDL-C changes
- **MOA data retrieval:** Full DrugBank mechanism of action data to complete the mechanistic linkage analysis
- **Philippines regulatory pathway:** If evidence emerges, a named-patient or compassionate-use pathway would be required given zero current local registrations
- **Combination potential assessment:** Evaluate whether UDCA could serve as an adjunct to lomitapide or evinacumab (agents that work independently of LDLR) rather than as a standalone therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

