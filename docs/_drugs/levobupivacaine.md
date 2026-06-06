---
layout: default
title: Levobupivacaine
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 1
---

# Levobupivacaine
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

# Levobupivacaine: From Local Anesthesia to Gastroduodenitis

## One-Sentence Summary

Levobupivacaine is the S(-)-enantiomer of bupivacaine, a long-acting local anesthetic used for regional anesthesia and surgical pain management.
The TxGNN model predicts it may be effective for **Gastroduodenitis**, however there are currently **no clinical trials** and **no publications** specifically supporting this direction.
The evidence base is limited entirely to model prediction, and known systemic toxicity risks make this a low-priority repurposing candidate at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local/regional anesthesia (no Philippines registration on record) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Levobupivacaine is the S(-)-enantiomer of bupivacaine that blocks Nav1.x voltage-gated sodium channels, producing long-acting local anesthesia with a somewhat better cardiac safety profile than the racemic parent compound.

Three mechanistic hypotheses connect Levobupivacaine to gastroduodenitis: **(1) Anti-inflammatory effects** — local anesthetics as a class can suppress neutrophil chemotaxis and downregulate pro-inflammatory cytokines (IL-1β, TNF-α, IL-6), which might theoretically suppress gastroduodenal mucosal inflammation; **(2) Enteric sensory nerve modulation** — Nav channels are expressed throughout the enteric nervous system (ENS) and GI mucosal cells, and their blockade could reduce local hyperalgesia and neurogenic inflammation; **(3) Limited antibacterial activity** — local anesthetics have demonstrated in vitro inhibitory effects against *H. pylori* in MIC studies, though no in vivo data exist.

None of these pathways has advanced to clinical research for gastroduodenitis. More critically, systemic administration of Levobupivacaine carries well-established cardiotoxicity (QRS prolongation, ventricular fibrillation) and neurotoxicity with an extremely narrow therapeutic window. Without a viable local delivery mechanism to the gastroduodenal mucosa, the safety barrier for this repurposing direction is very high.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Levobupivacaine is not currently registered or marketed in the Philippines. No authorization records are on file (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, drug interactions) were not retrievable at the time of this Evidence Pack generation. The following are known from general pharmacological literature: systemic Levobupivacaine carries significant **cardiotoxic risk** (QRS prolongation, ventricular fibrillation) and **neurotoxic risk** at supratherapeutic doses. These risks are directly relevant to any proposed systemic repurposing use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This repurposing candidate rests solely on a TxGNN model prediction (Evidence Level L5) with zero supporting clinical trials or publications, and the known systemic toxicity profile of Levobupivacaine creates a substantial safety barrier that current evidence cannot overcome.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank API (Data Gap DG002)
- Obtain TFDA/FDA Philippines package insert to extract formal warnings and contraindications (Data Gap DG001)
- Establish a plausible safe delivery route (e.g., intraluminal or topical GI administration) that avoids systemic absorption
- Demonstrate preclinical in vivo efficacy in a gastroduodenitis animal model before any clinical consideration
- At minimum one observational study, case series, or mechanistic translational study is required to advance beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

