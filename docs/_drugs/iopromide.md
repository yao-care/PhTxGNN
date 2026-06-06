---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Iopromide
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

The `txgnn-pipeline` skill covers multi-country deployment and technical workflow — the report generation task here is governed directly by the system prompt specification. Proceeding with the report.

---

# Iopromide: From CT Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide (Ultravist®) is a non-ionic tri-iodinated benzene contrast medium used exclusively as a diagnostic imaging agent in CT scans, angiography, and urography — it has no inherent therapeutic pharmacological activity.
The TxGNN model predicts it may be relevant to **Osteoarthritis Susceptibility** with a score of **99.57%**,
however there are **0 clinical trials** and **0 publications** supporting this as a therapeutic indication, and all 10 top predictions are assessed as model artifacts attributable to co-occurrence bias in the training knowledge graph.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iodinated contrast agent for CT imaging, angiography, and urography |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

In short, **this prediction is not mechanistically reasonable.** Iopromide is an inert, water-soluble, non-ionic contrast agent that works by attenuating X-rays — it has no anti-inflammatory properties, no cartilage-protective activity, no synovial-modulating capacity, and no receptor binding relevant to any of the predicted indications. It is eliminated renally without metabolic transformation and exerts no pharmacodynamic effect on host tissue.

Osteoarthritis susceptibility is a complex polygenic trait driven by cartilage matrix degradation (MMP pathways), subchondral bone remodeling, and low-grade synovial inflammation. There is no plausible biological pathway by which passive X-ray attenuation could influence OA risk or progression. The same mechanistic vacuum applies across all 10 TxGNN-predicted indications in this pack — from rare skeletal dysplasias (brachyolmia, pseudoachondroplasia, Hunter-Thompson dysplasia) to rheumatoid arthritis and alopecia.

The most scientifically coherent explanation for TxGNN's uniformly high scores is **co-occurrence bias in the knowledge graph**: patients with osteoarthritis and other musculoskeletal or systemic conditions routinely undergo contrast-enhanced CT as part of diagnostic workup. This creates a strong statistical co-occurrence between Iopromide and these disease nodes in the training data — the model correctly identifies association but cannot distinguish *diagnostic use* from *therapeutic effect*. This is a recognized and well-documented limitation of graph neural network-based drug repurposing models when applied to imaging agents, excipients, or other non-therapeutic substances.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Contextual note on literature across all ranked indications:** A small number of publications were retrieved across the full top-10 prediction list, but none constitute therapeutic evidence. All retrieved papers use Iopromide as a *procedural tool* rather than an intervention:
>
> - **PMID [11419151](https://pubmed.ncbi.nlm.nih.gov/11419151/)** (2001) — CT-guided obturator nerve block: Iopromide used for anatomical localization, not OA treatment.
> - **PMID [9678042](https://pubmed.ncbi.nlm.nih.gov/9678042/)** (1998) — MRI cartilage volume accuracy study: Iopromide used as CT reference contrast, not a therapeutic agent.
> - **PMID [19435939](https://pubmed.ncbi.nlm.nih.gov/19435939/)** (2009) — Contrast-enhanced CT for rheumatoid arthritis evaluation: Iopromide used for synovitis visualization, not RA treatment.
> - **PMID [9094239](https://pubmed.ncbi.nlm.nih.gov/9094239/)** (1997) — Lymphangiography in Noonan's syndrome: unrelated to hemoglobinopathy treatment.
> - **PMID [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/)** (2006) — ⚠️ **Adverse event report**: cerebral vaso-occlusive event in sickle cell disease following low-osmolar IV contrast — a safety warning, not a treatment signal.

---

## Philippines Market Information

Iopromide is currently **not registered in the Philippines**. No active licenses or regulatory authorizations exist. There is no Philippines-specific approved indication text available for review.

---

## Safety Considerations

Specific package insert warnings and contraindications were not retrieved in this data collection cycle. Please refer to the manufacturer's package insert for complete safety information.

> ⚠️ **Notable Safety Signal (PMID [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/)):** A published case report documents a cerebral vaso-occlusive event in a patient with **sickle cell disease** following intravenous administration of a low-osmolar iodinated contrast agent. This represents a potential contraindication signal for patients with **hemoglobinopathy**. This finding is particularly relevant because hemoglobinopathy appears as rank 9 in TxGNN's predicted indications — the available literature points to a **safety risk**, directly contradicting any therapeutic use hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Iopromide is a diagnostic contrast agent with no therapeutic mechanism of action; all 10 TxGNN predictions carry L5 evidence (model prediction only), zero clinical trial support, and zero therapeutic literature. The high prediction scores are consistent with co-occurrence bias rather than genuine repurposing potential. Notably, for one predicted indication (hemoglobinopathy), available literature identifies a *safety contraindication*, making the prediction actively counterproductive.

**To change this decision, the following would be required:**
- Discovery of a novel, biologically plausible pharmacological mechanism for Iopromide beyond radiocontrast activity (currently none is known)
- At minimum one preclinical study demonstrating therapeutic activity in any predicted indication
- Formal safety review regarding use in patients with hemoglobinopathy (sickle cell disease) before any expanded indication work is considered
- Philippines FDA registration assessment if any future evidence emerges

> **For pipeline review:** This case is a high-value negative example for model calibration. Flagging Iopromide — and diagnostic agents as a class (iodinated contrasts, gadolinium chelates, technetium tracers) — as a known false-positive category in TxGNN co-occurrence filtering would improve precision across the entire prediction pipeline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

