---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
---

# Diltiazem
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

# Diltiazem: From Cardiovascular Conditions to Ischemic Stroke Susceptibility

## One-Sentence Summary

Diltiazem is a well-established L-type voltage-gated calcium channel blocker (CCB), widely used in clinical practice for hypertension, angina pectoris, and cardiac arrhythmias. The TxGNN model predicts it may be relevant to **susceptibility to ischemic stroke**, though this disease target carries an ⚠️ **"obsolete"** ontology designation indicating the classification has been deprecated. Currently, **no clinical trials** and **no publications** directly support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in Philippines FDA registry (drug is currently not marketed in the Philippines) |
| Predicted New Indication | Ischemic Stroke Susceptibility ⚠️ *(deprecated ontology term)* |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Diltiazem is a non-dihydropyridine L-type voltage-gated calcium channel blocker (VGCC). Although full MOA data was not retrieved in this evidence pack, Diltiazem's pharmacology is well-characterised in the literature: it inhibits calcium influx into vascular smooth muscle and cardiac cells, producing vasodilation, reduction in peripheral vascular resistance, and negative chronotropic/inotropic effects on the heart.

Two mechanistic pathways link Diltiazem to ischemic stroke risk: (1) inhibition of calcium influx in cerebrovascular smooth muscle promotes cerebral vasodilation and reduces ischemic risk indirectly through blood pressure lowering; and (2) inhibition of calcium-dependent platelet activation may theoretically reduce thromboembolic events. Supporting this class-level hypothesis, the structurally related CCB Nimodipine holds an approved indication for cerebral vasospasm, suggesting the broader CCB class has recognised cerebrovascular protective potential.

However, three critical caveats substantially weaken the case for this specific candidate. First, the above reasoning represents **class-effect inference**, not Diltiazem-specific direct evidence. Second, the predicted disease term carries an **"obsolete"** prefix in the disease ontology — the classification itself has been retired and no longer maps cleanly to a current clinical entity. Third, "susceptibility" targets operate at the level of genetic or biomarker-defined risk, not therapeutic treatment, creating a fundamental conceptual gap between the model's output and any actionable clinical indication. These factors collectively explain the **Hold** decision.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the Diltiazem–ischemic stroke susceptibility pair.

---

## Literature Evidence

Currently no related literature is available for this specific drug–disease pair.

---

## Philippines Market Information

Diltiazem is currently **not registered** with the Philippine Food and Drug Administration. No product authorisations were found in the Philippines FDA database.

---

## Safety Considerations

Full safety data (warnings, contraindications, drug interactions) was not retrievable in this evidence pack. Please refer to the drug's package insert for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at Evidence Level L5 — the lowest tier — with no supporting clinical trials or publications, a deprecated disease target term, and no Philippines regulatory footprint. The ontology and conceptual ambiguities around the target must be resolved before any further evaluation is meaningful.

**To proceed, the following is needed:**

- **Resolve the ontology issue**: Map "obsolete susceptibility to ischemic stroke" to a current, clinically actionable disease target (e.g., ICD-10 I63 Ischemic stroke, or a specific stroke-prevention indication) before re-running the evidence search
- **Retrieve full MOA data**: Query DrugBank for Diltiazem's complete mechanism of action to enable a rigorous mechanistic link assessment
- **Broader literature search**: Re-run PubMed with expanded terms (e.g., *"Diltiazem AND cerebrovascular"*, *"calcium channel blocker AND stroke prevention"*) to identify any indirect or class-level evidence
- **Clarify the repurposing objective**: Define whether the intended use is (a) primary prevention via blood pressure management, (b) acute stroke treatment, or (c) post-stroke neuroprotection — each requires a distinct evidence pathway
- **Philippines regulatory pathway**: If the indication is later validated, assess the FDA Philippines registration requirements given the current zero-registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

