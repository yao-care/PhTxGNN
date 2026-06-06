---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a classic mood-stabilizing agent with decades of clinical use, most notably for bipolar disorder and related psychiatric conditions.
The TxGNN model predicts it may be effective for **Pseudoachondroplasia** — a rare genetic skeletal dysplasia — with a prediction score of **99.98%**.
However, **no clinical trials** and **no dedicated publications** currently support this specific repurposing direction, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in current data pack (Lithium carbonate is widely established for bipolar disorder) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Lithium carbonate's primary known mechanism is inhibition of **GSK-3β (Glycogen Synthase Kinase-3 beta)**, a serine/threonine kinase that serves as a critical negative regulator of the **Wnt/β-catenin signalling pathway**. By suppressing GSK-3β, lithium stabilises β-catenin, allowing it to translocate to the nucleus and activate downstream genes involved in cell proliferation and differentiation — including chondrocyte development. This mechanistic foundation is what likely drives the TxGNN graph-based inference.

Pseudoachondroplasia is a rare autosomal dominant skeletal dysplasia caused by mutations in the **COMP (Cartilage Oligomeric Matrix Protein)** gene. Mutant COMP protein misfolds and accumulates in the endoplasmic reticulum of chondrocytes, triggering ER stress, premature cell death, and disrupted growth plate architecture. The TxGNN model appears to infer a connection through the **COMP → ECM remodelling → Wnt/β-catenin** node network: dysregulated ECM-integrin signalling in COMP-mutant chondrocytes intersects with Wnt pathway activity, and lithium's modulation of this axis could theoretically reduce chondrocyte apoptosis or normalise proliferation in the growth plate.

That said, this remains a **purely computational prediction**. No animal model study, in vitro experiment, or clinical observation has directly tested lithium in pseudoachondroplasia. The mechanistic chain (COMP mutation → ECM stress → Wnt dysregulation → GSK-3β inhibition as rescue) is several nodes long and each step would require independent validation. The prediction should be interpreted as a hypothesis-generating signal, not an actionable therapeutic lead at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lithium carbonate in pseudoachondroplasia.

---

## Literature Evidence

Currently no related literature available for Lithium carbonate in pseudoachondroplasia.

---

## Philippines Market Information

Lithium carbonate is currently **not registered** with the Philippine FDA. No product authorizations were found in the data pack.

> Note: Despite its long history of clinical use globally (bipolar disorder, mood stabilization), no marketed formulations are on record in the current Philippine regulatory dataset. This represents a significant market access barrier if any repurposing program were to advance.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) were not available in the current evidence pack.

> Please refer to the package insert for full safety information. Clinicians should note that lithium has a **narrow therapeutic index** — serum level monitoring is required in standard clinical use. This characteristic would be a critical safety consideration for any investigational repurposing program.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based entirely on knowledge graph inference (L5), with no supporting clinical trials, no targeted preclinical studies, and no literature specific to lithium in pseudoachondroplasia. Additionally, lithium carbonate is not currently registered in the Philippines, creating both a regulatory and a safety data gap that must be resolved before any further evaluation is meaningful.

**To proceed, the following is needed:**

- **Mechanism validation**: In vitro studies in COMP-mutant chondrocyte cell lines or organoids to test whether GSK-3β inhibition reduces ER stress or restores growth plate signalling
- **Animal model data**: A mouse model of pseudoachondroplasia (e.g., COMP p.T585M knock-in) tested with lithium to assess skeletal phenotype rescue
- **MOA documentation**: Formal retrieval of lithium carbonate's full mechanism profile from DrugBank (currently flagged as Data Gap)
- **Safety profile retrieval**: Taiwan/Philippines package insert data, including warnings, contraindications, and DDI profile — required before any S1 safety screen
- **Regulatory pathway assessment**: Given zero Philippines registrations, a new drug application or compassionate use pathway would need to be scoped before any clinical translation
- **Literature sweep expansion**: A broader PubMed search using related terms (GSK-3β inhibitor + COMP + chondrocyte; lithium + skeletal dysplasia) may surface indirect mechanistic evidence not captured in the current evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

