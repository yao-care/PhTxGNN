---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 7
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cycloserine: From Multidrug-Resistant Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line antibiotic established as a key treatment for multidrug-resistant tuberculosis (MDR-TB), used when first-line agents have failed. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, yet **0 clinical trials** and **0 publications** currently support this direction. The prediction is based entirely on knowledge graph inference (Evidence Level L5), and the recommended decision is **Hold** pending any form of preclinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, cycloserine is a natural D-amino acid analogue antibiotic that inhibits bacterial cell wall synthesis by blocking two enzymes critical to peptidoglycan biosynthesis: D-alanine racemase and D-Ala-D-Ala ligase. Its established clinical role is as a second-line MDR-TB agent, used in combination regimens when isoniazid and rifampicin resistance is confirmed.

Beyond its antibiotic activity, the D-isomer (D-cycloserine) is also known to act as a partial agonist at the glycine co-agonist binding site of NMDA receptors in the central nervous system. Notably, NMDA receptors are also present throughout the enteric nervous system (ENS) — the network of neurons embedded in the gut wall (Auerbach's plexus and Meissner's plexus). In theory, D-cycloserine could modulate enteric neuronal excitability, potentially influencing gut motility, visceral pain signalling, and secretomotor function — all pathways implicated in IBS.

However, this mechanistic chain is highly indirect: TB antibiotic → NMDA receptor partial agonism → enteric nervous system modulation → IBS symptom relief. The TxGNN high prediction score most likely reflects multi-hop connectivity within the knowledge graph rather than any direct experimental evidence. No preclinical studies, animal models, or clinical trials investigating cycloserine specifically for IBS were identified. This prediction remains a purely computational hypothesis and should not be advanced without laboratory confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Cycloserine is currently **not registered** in the Philippines. No product authorizations were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Important Safety Signal Identified During Evidence Review**
>
> Evidence collected during evaluation of the "insomnia" indication (Rank 5 prediction) reveals a critical concern: the existing evidence direction shows that cycloserine **causes** insomnia and psychosis as adverse drug reactions — it is emphatically **not** a treatment for insomnia.
>
> - A 2022 case report (PMID [36712725](https://pubmed.ncbi.nlm.nih.gov/36712725/)) documents cycloserine-induced insomnia and psychosis in an MDR-TB patient.
> - Three clinical trials retrieved for the insomnia query (NCT03216356, NCT05395494, NCT03395392) all target psychiatric indications (PTSD, fibromyalgia, bipolar depression) via NMDA modulation — none target insomnia as a primary endpoint, and one has been withdrawn.
>
> This CNS toxicity profile — including insomnia, psychosis, seizures, depression, and peripheral neuropathy — represents a substantial safety barrier for any repurposing pathway in non-life-threatening conditions such as IBS.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting cycloserine for irritable bowel syndrome, and the drug's well-documented CNS adverse effect burden (insomnia, psychosis, seizures) makes the benefit-risk ratio unfavorable for a functional gastrointestinal disorder where safer therapeutic alternatives already exist.

**To proceed, the following is needed:**

- **MOA documentation**: Obtain formal DrugBank/primary source data on D-cycloserine's NMDA partial agonist activity and its pharmacological reach into the enteric nervous system
- **Preclinical studies**: In vitro and animal model experiments examining cycloserine's effects on gut motility, visceral hypersensitivity, and the ENS — specifically in IBS-relevant models (e.g., post-infectious IBS, stress-induced visceral pain)
- **CNS safety profiling**: Establish whether enteric-targeted dosing strategies (e.g., modified-release formulations) could achieve GI exposure while minimizing systemic CNS penetration
- **Comparative advantage analysis**: Clarify what clinical gap cycloserine could fill compared to established IBS treatments (antispasmodics, low-dose antidepressants, rifaximin for IBS-D), given that these already target relevant pathways with well-characterised safety profiles
- **Philippines regulatory pathway**: Since cycloserine is not registered in the Philippines, any clinical development would require a full new drug application — confirm whether compassionate use or research IND pathways are viable options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

