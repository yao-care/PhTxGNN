---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 2
---

# Iohexol
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

Using the `txgnn-pipeline` skill as context for this TxGNN repurposing report. Now generating the evaluation based on the Evidence Pack for Iohexol.

---

# Iohexol: From Contrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast medium used exclusively in diagnostic radiology procedures such as angiography, CT scanning, and myelography.
The TxGNN model predicts it may be effective for **Insomnia**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Despite a high prediction score (99.87%), the biological rationale is entirely absent — this is assessed as a knowledge graph false positive with no pharmacological basis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diagnostic contrast agent for medical imaging (no Philippines registrations on record) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on well-established pharmacology, Iohexol is a non-ionic, water-soluble iodinated compound used solely as a diagnostic contrast agent — it has no intrinsic pharmacological receptor activity. Its clinical utility derives entirely from X-ray attenuation by the iodine atoms it contains, not from any interaction with human receptors or enzymes.

Insomnia treatment relies on drugs acting at specific molecular targets: GABA-A receptors (benzodiazepines, z-drugs), melatonin MT1/MT2 receptors (ramelteon), orexin OX1/OX2 receptors (suvorexant, lemborexant), or histamine H1 receptors (doxylamine). Iohexol has no documented activity at any of these targets. The mechanistic gap between an imaging contrast agent and a sleep disorder is fundamental and has no biological bridge in current literature.

The high TxGNN score (99.87%) is best explained as a knowledge graph noise artefact. The model likely detected indirect graph connections — such as shared patient-population nodes, co-administration patterns in hospital datasets, or disease co-occurrence associations — rather than any true pharmacological relationship. The internal repurposing rationale in the Evidence Pack explicitly confirms this assessment: "TxGNN 高分為知識圖譜雜訊假陽性，無任何生物學合理性支持."

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Iohexol has no registered products in the Philippines. There are no FDA Philippines authorizations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Iohexol is a purely diagnostic contrast agent with no known pharmacological activity at any receptor system relevant to insomnia. The TxGNN prediction score is high, but this reflects a knowledge graph false positive, not a genuine drug–disease therapeutic relationship — there is zero supporting clinical trial evidence and zero supporting literature for this indication.

**To proceed, the following would be needed:**
- Mechanistic evidence demonstrating any Iohexol interaction with sleep-regulating pathways (GABA, melatonin, orexin, or histamine systems) — currently non-existent
- At minimum one preclinical study (animal sleep model or in vitro receptor binding assay) showing sleep-relevant biological activity
- Without such foundational evidence, clinical investigation is not scientifically warranted and should not be initiated
- MOA data from DrugBank (Data Gap DG002) and Philippines package insert safety data (Data Gap DG001) should be retrieved before any further review, though these are unlikely to change the Hold recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

