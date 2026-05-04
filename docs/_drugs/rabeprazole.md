---
layout: default
title: Rabeprazole
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
---

# Rabeprazole
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

# Rabeprazole: From Acid-Related Disorders to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) widely used for acid-related disorders such as gastroesophageal reflux disease and peptic ulcers, suppressing gastric acid secretion by irreversibly inhibiting the H⁺/K⁺-ATPase enzyme in gastric parietal cells.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SSM)**,
however, **no clinical trials** and **no publications** currently support this direction, placing the evidence at the lowest level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acid-related disorders (GERD, peptic ulcer) — no Philippines registration on file |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Rabeprazole belongs to the proton pump inhibitor (PPI) class, and its efficacy in reducing gastric acid secretion has been well established across multiple acid-related conditions. However, the mechanistic bridge to Smouldering Systemic Mastocytosis requires careful interpretation.

Patients with systemic mastocytosis (including the smouldering subtype) have massively activated mast cells that release large amounts of histamine, which in turn stimulates excessive gastric acid secretion. PPIs such as Rabeprazole are therefore used as **supportive/symptomatic management** agents in mastocytosis patients to control gastrointestinal symptoms — not as a treatment targeting the underlying disease itself.

The root cause of SSM is the KIT D816V gain-of-function mutation that drives abnormal mast cell proliferation. Current first-line targeted therapies are midostaurin and avapritinib. Rabeprazole has no known direct inhibitory effect on KIT signalling, mast cell proliferation, or disease-modifying pathways in SSM. The high TxGNN score most likely reflects an **indirect knowledge graph path** (histamine → gastric acid → H⁺/K⁺-ATPase) rather than a genuine disease-modifying repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Rabeprazole currently has **no registered products** in the Philippines (FDA Philippines). No authorization numbers, product names, or approved indications are on file.

> Note: Rabeprazole (as various brand-name and generic formulations) is widely registered in other jurisdictions (e.g., Japan as Pariet, EU, US) for GERD, erosive esophagitis, peptic ulcer, and *H. pylori* eradication. Philippines registration data was not retrieved in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindication data, or drug-drug interaction data were available in this evidence pack. Full safety profiling should be completed before any clinical assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.44%) based on an indirect mechanistic pathway — PPI suppression of histamine-driven gastric acid — rather than any direct disease-modifying effect on the KIT-driven mast cell proliferation that defines SSM. With zero clinical trials, zero supporting publications, no Philippines market registration, and all safety data gaps unresolved, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**

- Resolve **DG001** (Blocking): Obtain full safety profile including warnings and contraindications from the Philippines FDA package insert or equivalent regulatory document
- Resolve **DG002** (High): Confirm Rabeprazole's complete mechanism of action from DrugBank or primary literature
- Conduct a **targeted literature search** specifically for PPI use in mastocytosis symptom management (broader search beyond SSM alone, e.g., indolent systemic mastocytosis or urticaria pigmentosa with GI symptoms)
- Perform an **expert clinical review** to determine whether the TxGNN prediction reflects a supportive-care role (symptom management) vs. a genuine disease-modifying repurposing signal
- Clarify the **regulatory pathway** for any future Philippines submission, given current absence of local registration
- If the intended use is symptom management only, consider re-framing this as a **supportive care indication** rather than a primary repurposing candidate, which would carry a substantially different evidence and regulatory burden

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

