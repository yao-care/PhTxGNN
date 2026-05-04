---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a selective β1-adrenergic receptor blocker widely used in cardiovascular medicine for hypertension and heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** with a prediction score of **99.94%**,
however **no clinical trials** and **no targeted literature** have been identified for this specific indication to date — the case rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, heart failure (standard selective β1-blocker indications; no Philippines registration on file) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bisoprolol is a highly selective β1-adrenergic receptor antagonist. Its primary cardiovascular effects include reducing heart rate, lowering cardiac output, and decreasing systemic vascular resistance. Critically for this prediction, β1-blockade suppresses renin release from the juxtaglomerular apparatus of the kidney — the first step in the renin-angiotensin-aldosterone system (RAAS). By dampening RAAS activation, bisoprolol reduces circulating angiotensin II levels, which in turn lowers both systemic blood pressure and intraglomerular filtration pressure.

In malignant hypertensive renal disease, sustained extreme blood pressure drives accelerated fibrinoid necrosis of small renal vessels and progressive nephrosclerosis. The β1-blockade mechanism described above is pharmacologically relevant: reducing the sympathetic over-activation that contributes to renin hypersecretion and uncontrolled hypertension could theoretically slow the renal deterioration cascade. In addition to RAAS suppression, bisoprolol reduces the direct adrenergic stimulation of renal vasculature that exacerbates glomerular hypertension.

An important clinical caveat, however, is that in the setting of malignant hypertension with established renal impairment, the renal vasculature may have already lost pressure autoregulation. Overly rapid blood pressure reduction — including that achieved with β-blockers — risks precipitating renal ischemia. For this reason, bisoprolol in this context would need careful dose titration and close renal function monitoring, and would most likely serve as adjunctive therapy rather than monotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Malignant Hypertensive Renal Disease.

> **Note on evidence search:** A PubMed search pairing Bisoprolol with the top predicted indication (malignant hypertensive renal disease) returned zero results. A separate search for the rank-3 predicted indication (pulmonary hypertension owing to lung disease/hypoxia) returned 20 publications; however, upon review these papers address hypoxia biology broadly (neurodegeneration, tumor microenvironment, altitude physiology) and contain no direct evidence linking bisoprolol to pulmonary hypertension treatment. They are not included here as they do not support the primary prediction.

---

## Philippines Market Information

Bisoprolol currently has **no registered products** with the Philippines FDA. No authorization numbers, product names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data were not retrieved during this evaluation cycle. Known class-level concerns for selective β1-blockers include: risk of bronchospasm in reactive airway disease, masking of hypoglycaemia symptoms in diabetic patients, rebound effects upon abrupt withdrawal, and caution in patients with significant bradycardia or AV conduction disorders. Formal safety data should be sourced from the TFDA/FDA Philippines-approved prescribing information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.94%), and the β1-blockade → renin suppression → RAAS attenuation pathway provides a biologically coherent mechanistic basis for a role in malignant hypertensive renal disease. However, no clinical trials and no directly relevant published literature exist to validate this specific indication — the evidence level is L4 (mechanism only), which is insufficient to advance beyond the hypothesis-generation stage without additional data.

**To proceed, the following is needed:**

- **MOA data (High priority):** Retrieve complete DrugBank pharmacology record (DB00612) to formally document the mechanism of action and relevant targets (ADRB1).
- **Philippines regulatory safety data:** Download and parse the approved Philippines/TFDA package insert PDF to obtain complete warnings and contraindications; this is currently flagged as a blocking data gap (DG001).
- **Systematic literature review:** Conduct a targeted search combining bisoprolol (and other β-blockers as a class) with malignant hypertension and hypertensive nephrosclerosis/nephropathy to identify any indirect or class-level evidence.
- **Comparator context:** Assess how bisoprolol compares to first-line agents for malignant hypertension with renal involvement (e.g., ACE inhibitors, ARBs, IV nitroprusside) to establish whether a β-blocker would occupy a meaningful position in the treatment algorithm.
- **Prospective study design:** If mechanistic evidence is confirmed, consider a small-scale observational study or registry analysis in patients with malignant hypertension and renal involvement who are already receiving bisoprolol for co-existing indications (e.g., heart failure, atrial fibrillation).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

