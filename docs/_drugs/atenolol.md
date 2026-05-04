---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective β1-adrenergic receptor blocker widely used for hypertension, angina pectoris, and cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction**,
with **0 clinical trials** and **1 publication** currently supporting this specific disease subtype.

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris, cardiac arrhythmias |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Atenolol is a selective β1-adrenergic receptor antagonist. By competitively blocking catecholamines at cardiac β1 receptors, it reduces heart rate, myocardial contractility, and blood pressure, leading to decreased cardiac output and substantially lower myocardial oxygen demand. This anti-ischemic mechanism is the foundation of beta-blocker use across all ischemic heart disease presentations.

Posteroinferior myocardial infarction is an anatomically specific MI subtype involving the territory supplied primarily by the right coronary artery (RCA). The high TxGNN prediction score (99.87%) reflects a strong biological plausibility: Atenolol's ability to reduce heart rate and limit ischemic zone expansion is mechanistically consistent regardless of which coronary artery territory is affected. Beta-blockers as a class have well-established cardioprotective effects in acute MI, supported by landmark trials such as ISIS-1.

That said, the current evidence retrieved for this *specific* posteroinferior subtype is thin — only one small crossover study from 1985. While the mechanistic rationale is compelling, subtype-specific evidence is needed before a firm recommendation can be made, particularly given that Atenolol has no registered products in the Philippines.

> Currently, detailed mechanism of action data was not retrieved in this evidence pack. The pharmacological description above is based on established clinical knowledge of Atenolol's drug class.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Atenolol in posteroinferior myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Randomized Crossover (Single-blind) | La Revue de medecine interne | Atenolol 200 mg vs diltiazem 240 mg in 23 post-MI patients (including posteroinferior MI) assessed for anti-ischemic activity by computerized bicycle ergometer; both agents evaluated 4 weeks after infarction in patients with residual ischemia |

---

## Philippines Market Information

Atenolol currently has **no registered products** with FDA Philippines and is not marketed in the country. No license records are available.

If clinical development or importation is considered, a full Philippines FDA registration dossier would be required prior to any use.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not retrieved in this evidence pack. Remediation requires downloading the TFDA/FDA Philippines package insert PDF and querying the DrugBank API for interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Atenolol's cardioselective β1-blocking mechanism is biologically plausible for posteroinferior MI — and beta-blockers are standard of care for MI broadly — the evidence specifically retrieved for this anatomical subtype is extremely limited (one single-blind crossover study, 1985, n=23). Combined with the absence of registered clinical trials and zero Philippines market authorization, the evidence base is insufficient to support a formal repurposing recommendation at this time.

**To proceed, the following is needed:**

- **Expand evidence search**: Review landmark beta-blocker MI trials (e.g., ISIS-1, COMMIT, CAPRICORN) for subgroup data on posteroinferior MI specifically
- **Retrieve MOA data**: Query DrugBank API (DB00335) for complete mechanism of action and pharmacodynamic profile
- **Retrieve safety data**: Download Philippines FDA / TFDA package insert PDF to extract key warnings, contraindications, and boxed warnings
- **DDI data**: Run drug-drug interaction search via a structured DDI database (currently returned "not found")
- **Philippines registration**: Initiate FDA Philippines pre-submission inquiry if repurposing development is planned
- **Consider higher-ranked supporting indication**: Indication #9 (Chronic Pulmonary Heart Disease, L3, "Proceed with Guardrails") has stronger evidence support — 1 active Phase 4 RCT (NCT03278509, n=5,000) and 15 publications — and may be a more actionable near-term target, though β-blocker use in COPD comorbidity requires careful patient selection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

