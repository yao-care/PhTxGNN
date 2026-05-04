---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 2
---

# Heparin
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

# Heparin: From Anticoagulation Therapy to Thrombophilia Due to Protein C Deficiency

## One-Sentence Summary

Heparin is a well-established anticoagulant widely used for thrombosis prevention and treatment. The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency (Autosomal Recessive)**, with a high prediction score of 99.29%. Although no clinical trials or publications were directly captured in this dataset, real-world clinical practice already supports the use of heparin as bridging therapy in protein C-deficient patients initiating warfarin — indicating the TxGNN prediction aligns with established medical knowledge.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation (thrombosis prevention and treatment) — no Philippines registration on file |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (Model prediction; no formal studies captured in dataset) |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Heparin exerts its anticoagulant effect primarily by binding to **Antithrombin III (AT-III)**, dramatically accelerating AT-III's ability to inactivate thrombin (Factor IIa) and Factor Xa. This mechanism is independent of the Protein C anticoagulant pathway. In patients with **Protein C deficiency**, the natural Protein C/Protein S anticoagulant system is impaired, leading to an increased risk of venous thromboembolism. Because heparin operates through an entirely separate anticoagulant pathway (AT-III), it can effectively provide anticoagulation even when the Protein C pathway is non-functional.

The clinical relevance of this prediction is well-grounded. In current medical practice, heparin is already used as a **bridging anticoagulant** when initiating warfarin therapy in patients with known Protein C deficiency. This bridging is critical because warfarin initially reduces Protein C levels faster than procoagulant factors, creating a transient hypercoagulable state that can cause **warfarin-induced skin necrosis** — a dangerous complication. Heparin's role in this bridging protocol has been established for decades.

Therefore, the TxGNN model's high prediction score (99.29%) for this drug-disease pair is consistent with well-known pharmacological principles and established clinical practice. The absence of captured evidence in the dataset likely reflects the fact that heparin's use in Protein C deficiency is considered standard of care rather than a novel research question, and thus not the subject of recent dedicated clinical trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for "Thrombophilia due to Protein C Deficiency" with Heparin in the captured dataset.

> **Note:** The absence of registered trials likely reflects that heparin use in Protein C deficiency is already standard clinical practice (bridging therapy), rather than an untested hypothesis requiring prospective trial validation.

---

## Literature Evidence

Currently no related literature available specifically for this drug-disease combination in the captured dataset.

> **Note:** Established textbook-level evidence supports heparin bridging in Protein C deficiency. The lack of captured publications may indicate that this is considered settled medical knowledge rather than an active area of investigation.

---

## Philippines Market Information

Heparin is currently **not marketed** in the Philippines based on available regulatory data. No registration licenses were found on file.

| Item | Status |
|------|--------|
| Market Status | Not marketed |
| Total Licenses | 0 |

> **Note:** Heparin is a globally essential medicine (on the WHO Essential Medicines List) and is widely available in most countries. The absence of Philippines registration data may reflect a data gap rather than true unavailability.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important clinical notes for this specific indication:**
> - In patients with **Protein C deficiency**, careful monitoring of anticoagulation parameters (aPTT, anti-Xa levels) is essential
> - **Heparin-Induced Thrombocytopenia (HIT)** is a known serious adverse effect — platelet counts should be monitored regularly (baseline and every 2–3 days during the first 14 days of therapy)
> - Heparin should be used as a bridge and is not intended for long-term monotherapy in this patient population
> - Detailed warnings, contraindications, and drug interaction data were not available in the current dataset (Data gaps: TFDA package insert warnings/contraindications, MOA details)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction aligns strongly with established clinical practice. Heparin is already used as bridging anticoagulant therapy in Protein C-deficient patients. The mechanistic rationale is clear: heparin acts through the AT-III pathway, which is independent of the deficient Protein C pathway. While no formal clinical trials were captured in the dataset for this specific indication, this reflects settled medical knowledge rather than a lack of evidence.

**To proceed, the following is needed:**
- **Mechanism of Action (MOA) data**: Obtain detailed pharmacological data from DrugBank to formally document the AT-III pathway
- **Philippines regulatory pathway**: Investigate heparin's availability and registration status in the Philippines; if truly unregistered, explore regulatory pathways for this WHO Essential Medicine
- **Package insert safety data**: Obtain TFDA or FDA Philippines label information for formal safety assessment (warnings, contraindications, drug interactions)
- **Clinical practice guidelines**: Compile existing guidelines (e.g., ACCP, ASH) that already recommend heparin bridging in Protein C deficiency to substantiate the evidence base
- **Pharmacovigilance plan**: Establish HIT monitoring protocols specific to the target patient population

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

