---
layout: default
title: Pancuronium
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Pancuronium
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

# Pancuronium: From Surgical Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Pancuronium (Pavulon) is a non-depolarizing neuromuscular blocking agent widely used in surgical anesthesia and intensive care to achieve skeletal muscle relaxation and facilitate mechanical ventilation.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome** with a prediction score of 99.95%, however this is supported by **0 clinical trials** and **0 publications** — making it a model-only prediction.
Given the extremely weak mechanistic rationale and complete absence of supporting evidence, this prediction warrants significant caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; known clinically as a neuromuscular blocking agent for surgical anesthesia and ICU sedation/ventilation |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (Model prediction only — no supporting studies) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Pancuronium is a non-depolarizing neuromuscular blocking agent (NMBA) that acts as a competitive antagonist at nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction (NMJ). By preventing acetylcholine from binding, it produces temporary skeletal muscle paralysis. Additionally, Pancuronium exhibits a vagolytic effect through blockade of muscarinic m2 (mAChR) receptors, which causes mild tachycardia — a clinically relevant cardiovascular side effect.

Cauda equina syndrome (CES) results from compression of the lower lumbar and sacral nerve roots below the spinal cord, producing a lower motor neuron injury pattern. The fundamental pathology is mechanical compression and ischemia of nerve roots, not a disorder of the neuromuscular junction. While Pancuronium could theoretically reduce residual skeletal muscle spasm near the affected segment, it has no ability to relieve neural compression, restore nerve root function, or address the underlying structural pathology. Furthermore, in the setting of denervation — which is a hallmark of CES — the predictability and safety of NMJ blockade is significantly compromised.

In summary, the mechanistic link between Pancuronium and cauda equina syndrome is assessed as **extremely weak**. The high TxGNN score most likely reflects indirect network connections within the knowledge graph (e.g., neuromuscular → spinal cord → nerve root nodes) rather than genuine pharmacological plausibility. No biological rationale supports Pancuronium as a therapeutic agent for CES.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication (Cauda Equina Syndrome).

> **Note:** While 14 publications were retrieved for the rank-9 indication (Autonomic Nervous System Disease) and 1 publication for rank-4 (Neurocirculatory Asthenia), none of these constitute evidence supporting Pancuronium as a *treatment* for those conditions. The papers primarily describe Pancuronium used as a pharmacological tool agent during anesthesia in patients *who have* autonomic conditions — not as a therapeutic intervention targeting the disease itself. The single exception is [PMID 156745](https://pubmed.ncbi.nlm.nih.gov/156745/) (Buchanan et al., 1979), which describes Pancuronium use in tetanus-related autonomic storm — a specific emergency context, not a repurposing indication.

---

## Philippines Market Information

Pancuronium is **not currently registered or marketed in the Philippines**. No drug licenses were found in the regulatory database.

---

## Safety Considerations

Detailed Philippine regulatory package insert warnings and contraindications are not available for this drug (Data Gap: TFDA/Philippines label not retrieved). Clinicians should refer to the current package insert and international prescribing information.

**General safety considerations known from the literature and anesthesia practice:**

- Pancuronium causes complete skeletal muscle paralysis, including respiratory muscles — **mandatory mechanical ventilation support is required** during use.
- Its **vagolytic effect** (mAChR m2 blockade) can cause significant tachycardia and hypertension, which is particularly hazardous in patients with:
  - Mitral valve prolapse (MVP) — tachycardia can worsen regurgitation
  - Coronary artery disease or cardiac ischemia
  - Prolonged QT syndrome
- In patients with **pre-existing autonomic neuropathy** (e.g., diabetic autonomic neuropathy, Shy-Drager syndrome), haemodynamic responses to Pancuronium are unpredictable and potentially dangerous.
- Reversal agents (neostigmine + atropine, or sugammadex where applicable) are required to restore neuromuscular function post-procedure.
- No drug-drug interaction data was retrievable from the DDI database query for this analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Pancuronium are rated L5 (model prediction only), with the single partial exception of Autonomic Nervous System Disease (L4, indirect observational evidence). The top-ranked prediction — cauda equina syndrome — has zero clinical trials, zero supporting publications, and an extremely weak mechanistic rationale. Pancuronium is a short-acting paralytic agent used exclusively in controlled clinical settings (operating room, ICU) with mandatory ventilatory support; repurposing it as a stand-alone therapeutic agent for chronic neurological, gastrointestinal, or cardiac conditions is not biologically plausible based on currently available evidence.

**To reconsider, the following would be needed:**

- Retrieval and review of formal package insert (Philippines/international) to characterize safety profile, absolute contraindications, and known drug interactions
- Clarification of the confirmed original approved indications (not available in current dataset)
- A mechanistic hypothesis with at least preclinical (in vitro/animal) evidence demonstrating pharmacodynamic relevance to the predicted indication
- For any indication to progress past L5, a minimum of peer-reviewed preclinical studies or a case series specifically evaluating Pancuronium as a *therapeutic agent* (not as an anesthetic tool drug) for the target condition would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

