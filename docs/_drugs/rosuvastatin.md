---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hypercholesterolemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Rosuvastatin is a potent HMG-CoA reductase inhibitor, globally recognized for the treatment of hypercholesterolemia and dyslipidemia, though it is currently not registered with the Philippines FDA.
The TxGNN model predicts it may be effective for **Cholesterol-Ester Transfer Protein (CETP) Deficiency**, with a prediction score of 99.54%.
Currently, **no dedicated clinical trials** and only **2 case reports** — from mechanistically related but distinct lipid disorders — support this direction, indicating this is a hypothesis-generating signal rather than a validated repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Dyslipidemia (globally approved; not registered in Philippines) |
| Predicted New Indication | Cholesterol-Ester Transfer Protein Deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question (Hold) |

---

## Why Is This Prediction Reasonable?

Rosuvastatin is a liver-selective, competitive HMG-CoA reductase inhibitor — the enzyme that catalyzes the rate-limiting step in endogenous cholesterol biosynthesis. By blocking this pathway, rosuvastatin reduces hepatic cholesterol output and triggers compensatory upregulation of LDL receptors on hepatocyte surfaces, accelerating LDL-C clearance from the bloodstream. The net effect is an LDL-C reduction of 45–63%, a 20–35% drop in triglycerides, and a modest 5–10% rise in HDL-C, making it the most potent statin currently available and the cornerstone treatment for multiple lipid disorders worldwide.

CETP deficiency is a rare autosomal condition in which the cholesterol ester transfer protein — normally responsible for bidirectional exchange of cholesterol esters and triglycerides between HDL and VLDL/LDL particles — is absent or severely dysfunctional. The resulting lipid phenotype is paradoxically elevated HDL-C with mildly reduced LDL-C. In most carriers, this phenotype is associated with neutral or even favorable cardiovascular outcomes, not a state requiring active lipid-lowering therapy. The proposed mechanistic link to rosuvastatin is therefore constrained: while rosuvastatin could reduce the hepatic cholesterol ester supply available for redistribution, this does not translate into a meaningful therapeutic benefit in patients who already lack functional CETP.

The two identified publications are case reports of ApoA-I deficiency and Hepatic Lipase deficiency — conditions that share metabolic overlap with CETP deficiency (all affecting HDL particle metabolism) but are mechanistically and genetically distinct. The TxGNN prediction most likely captures this network-level lipid metabolism connectivity within the knowledge graph, rather than a validated drug-disease relationship. It is worth noting that other TxGNN predictions for rosuvastatin — particularly **Familial Hypercholesterolemia** (Rank 2, L1 evidence with multiple completed Phase 3 RCTs) and **Hyperlipidemia** (Rank 10, L1 evidence) — reflect rosuvastatin's established therapeutic territory and carry substantially stronger clinical support.

---

## Clinical Trial Evidence

Currently no clinical trials related to Rosuvastatin in cholesterol-ester transfer protein deficiency are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case Report / Literature Review | Journal of Clinical Lipidology | A novel APOA1 nonsense mutation causing complete ApoA-I deficiency in an Iraqi Mandaean family; markedly varied cardiovascular presentation (one sibling with xanthelasmas but minimal cardiac findings) despite identical homozygous genotypes |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case Report | BMJ Case Reports | First report measuring CETP activity and mass in a Middle-Eastern male with Hepatic Lipase deficiency; elevated HDL-C coexisted with premature atherosclerosis, highlighting the complexity of HDL function beyond simple concentration |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The high TxGNN score reflects lipid metabolism network connectivity in the knowledge graph, but the mechanistic case for treating CETP deficiency with rosuvastatin is weak — the two conditions have opposing lipid phenotypes (rosuvastatin lowers LDL-C and the cholesterol ester pool, while CETP deficiency already results in reduced LDL-C and excess HDL-C), and standard clinical reasoning does not support LDL-lowering therapy as a treatment goal for CETP deficiency. No dedicated clinical trial or direct mechanistic study exists to bridge this gap.

**To proceed, the following is needed:**
- Clarify the clinical question: is rosuvastatin being considered for a CETP-deficient patient who also has co-existing elevated LDL-C requiring statin therapy, or as a direct intervention for CETP deficiency pathophysiology? These are fundamentally different scenarios.
- Commission pre-clinical mechanistic studies examining rosuvastatin's effect on cholesterol ester dynamics in CETP-null or CETP-knockdown models.
- Obtain full MOA documentation from DrugBank to formally characterize pharmacological targets and off-target effects.
- Obtain Philippines package insert (or equivalent regional label) for complete key warnings, contraindications, and drug interaction data.
- Prioritize higher-ranked TxGNN predictions with L1 clinical evidence for Philippines market development: **Familial Hypercholesterolemia** (multiple completed Phase 3 RCTs including pediatric populations) and **Hyperlipidemia** (OTC switch data, head-to-head comparator trials) represent far stronger near-term repurposing and market entry opportunities.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

