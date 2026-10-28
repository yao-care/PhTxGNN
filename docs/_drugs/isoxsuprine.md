---
layout: default
title: Isoxsuprine
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Isoxsuprine: predicted new indication benign prostatic hyperplasia (evidence level L5). Approved use: Cerebrovascular disorder, vascular disease, Raynaud disease"
monitor_inn: "Isoxsuprine"
predicted_indications: ["benign prostatic hyperplasia (disease)", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "blue toe syndrome", "atheroembolism of kidney", "hemangioendothelioma", "angiodysplasia of stomach", "respiratory failure", "neurogenic thoracic outlet syndrome", "idiopathic spontaneous coronary artery dissection"]
---

# Isoxsuprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Isoxsuprine: From Cerebrovascular and Peripheral Vascular Disorders to benign prostatic hyperplasia
{: .text-alpha }

## One-Sentence Summary

Isoxsuprine is a vasodilator originally used for cerebrovascular disorder, vascular disease, and Raynaud disease.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model's output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cerebrovascular disorder, vascular disease, Raynaud disease (from the TxGNN knowledge graph; no approved indication text is recorded in the Philippine registration) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, isoxsuprine is a beta-adrenergic agonist with direct vascular smooth muscle relaxant activity. Its efficacy in peripheral and cerebral vascular conditions is the basis of its original use.

A plausible link to BPH would be smooth muscle relaxation in the prostate and bladder neck. However, the established mechanism for this effect is alpha-1 adrenergic blockade, not beta-agonism or direct vasodilation. No trials or literature support the link, so the very high TxGNN score should be read as a network-based prediction only, not as evidence of efficacy.

Other predicted indications are also ranked highly by the TxGNN model (deep learning), including arterial thoracic outlet syndrome, blue toe syndrome, and respiratory failure. All have the same L5 evidence level. Several of them (venous and neurogenic thoracic outlet syndrome, hemangioendothelioma, angiodysplasia of the stomach) have weak or questionable mechanistic links, which suggests the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for benign prostatic hyperplasia.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0267 | Isoxsuprine | Not recorded | Not recorded (status: valid) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Hypotensive disorder. This is relevant because isoxsuprine's vasodilator effect can lower blood pressure.
- **Drug Interactions**: 20 interactions were identified, all rated Moderate. Main groups:
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Prostacyclin-pathway vasodilators: epoprostenol, iloprost, selexipag, treprostinil
  - Phenothiazine-type or antihistamine agents: promethazine, methdilazine, thiethylperazine, alimemazine
  - Others: amifostine, nitrous acid, pentoxifylline, brimonidine (ophthalmic and topical), topical minoxidil, ozanimod, procarbazine

  Many of these combinations are likely to add blood-pressure-lowering effects.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest model score but no clinical trial or literature support (L5). The mechanistic link to BPH is weak compared with established alpha-1 blockers. In addition, the only Philippine registration is cancelled, which limits practical feasibility.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Package insert warnings and contraindications from DOH-FDA Philippines (required before any safety screening)
- A systematic literature search specific to isoxsuprine and BPH or lower urinary tract symptoms
- Preclinical or mechanistic evidence showing a prostatic smooth muscle effect
- Clarification of why the Philippine registration was cancelled, and whether any product is currently available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

