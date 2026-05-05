---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill as context. Now generating the report from the Evidence Pack:

---

# Naproxen: From Pain & Inflammation to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a well-established non-steroidal anti-inflammatory drug (NSAID) with a long history of use in pain relief and inflammatory conditions such as arthritis.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, a rare genetic skeletal malformation disorder.
Currently, there are **0 clinical trials** and **0 publications** supporting this direction — this is a model-inference-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Philippines regulatory data |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Naproxen is a non-steroidal anti-inflammatory drug (NSAID) whose primary mechanism involves inhibiting cyclooxygenase (COX-1 and COX-2) enzymes, thereby suppressing prostaglandin synthesis — particularly PGE2. Its analgesic, antipyretic, and anti-inflammatory effects have been clinically established for decades.

Brachydactyly-Syndactyly Syndrome is a rare congenital skeletal disorder caused by mutations in genes such as **HRAS** and **BMPR1B**, which govern limb bone patterning during embryonic development. While PGE2 is known to play a role in general bone formation and remodeling, this is a non-specific physiological function that does not intersect with the upstream genetic defects driving this syndrome.

The mechanistic connection is extremely weak. COX inhibition has no established role in correcting congenital bone malformations caused by fixed genetic mutations. The Evidence Pack's own repurposing rationale flags this as a **probable knowledge graph structural artifact** rather than a genuine therapeutic signal. This assessment applies to all four top TxGNN predictions for Naproxen, each of which involves a rare hereditary skeletal or developmental dysplasia with no plausible pharmacological link to NSAID therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Naproxen currently has **no regulatory registrations** with the Philippine FDA. It is not an approved product in the Philippines market and has no active licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications are rare hereditary skeletal/developmental disorders (Evidence Level L5 — model prediction only), with zero supporting clinical trials or literature. The mechanistic link between COX inhibition and congenital genetic malformations is biologically implausible, and the model predictions are most likely knowledge graph structural artifacts with no actionable therapeutic relevance.

**To proceed, the following is needed:**
- Retrieve Naproxen's full MOA data from DrugBank (currently a data gap) to confirm pharmacological class and known off-target effects
- Obtain Philippine FDA package insert warnings and contraindications (currently blocking-level data gap)
- Commission expert review by a clinical pharmacologist or medical geneticist to formally rule out any indirect PGE2/bone-remodeling rationale in these rare diseases
- Consider re-running TxGNN prediction filtering against Naproxen's established pharmacological class (NSAID/COX inhibitor), prioritising inflammatory, musculoskeletal, or pain-adjacent indications where evidence is substantially stronger and mechanistic plausibility is high
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

