---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 7
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Felodipine is an L-type calcium channel blocker (CCB) used internationally for systemic hypertension, with no current Philippines registration on record.
The TxGNN model's highest-ranked prediction is **pulmonary hypertension with unclear multifactorial mechanism** (score 99.91%), yet this indication has **no supporting clinical trials or directly relevant publications**.
Critically, among all 7 ranked predictions in this multi-indication analysis, **Prinzmetal angina** (rank 7) represents a far stronger repurposing opportunity — backed by multiple direct clinical studies of Felodipine and Class I guideline support for CCBs in this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (international reference; no Philippines registration on record) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 — model prediction only, no direct studies |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacology, Felodipine is a second-generation dihydropyridine (DHP)-class L-type calcium channel blocker. It selectively inhibits voltage-gated L-type calcium channels in arterial vascular smooth muscle, producing arterial vasodilation, reduced peripheral vascular resistance, and lower systemic blood pressure — with notably high vascular selectivity and minimal cardiac depression compared to non-DHP CCBs such as diltiazem or verapamil.

The TxGNN prediction for pulmonary hypertension is mechanistically grounded at the class level: L-type CCBs can also relax pulmonary arterial smooth muscle and theoretically reduce pulmonary vascular resistance (PVR). In WHO Group 1 pulmonary arterial hypertension (PAH), specific CCBs — nifedipine, amlodipine, and diltiazem — are guideline-endorsed for patients who demonstrate a positive acute vasoreactivity test (AVT+). Felodipine shares this class mechanism and could, in principle, have a comparable hemodynamic effect.

However, the specifically predicted indication — "pulmonary hypertension with unclear multifactorial mechanism" — corresponds to WSPH Group 5 PH, a heterogeneous category encompassing rare systemic conditions (e.g., sarcoidosis, metabolic disorders, haematologic disease). CCBs have no established therapeutic role in Group 5 PH, and Felodipine has no published clinical trial data for any PH subtype. The TxGNN prediction most likely arises from knowledge-graph structural connections (shared cardiovascular phenotype nodes) rather than a direct evidence trail between this drug and this disease category.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension with unclear multifactorial mechanism.

---

## Literature Evidence

Currently no related literature available for Felodipine in pulmonary hypertension with unclear multifactorial mechanism.

---

## All Predicted Indications — Summary

This evidence pack covers 7 TxGNN-predicted indications for Felodipine, all cardiovascular in nature and consistent with the CCB mechanism. The table below provides a comparative overview:

| Rank | Indication | TxGNN Score | Evidence Level | Trials | Publications | Decision |
|------|-----------|------------|----------------|--------|--------------|----------|
| 1 | Pulmonary hypertension with unclear multifactorial mechanism | 99.91% | L5 | 0 | 0 | Hold |
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.91% | L5 | 0 | 20 (non-specific†) | Hold |
| 3 | Malignant hypertensive renal disease | 99.90% | L5 | 0 | 0 | Hold |
| 4 | Malignant renovascular hypertension | 99.90% | L5 | 0 | 1 (case report‡) | Hold |
| 5 | Braddock syndrome | 99.88% | L5 | 0 | 0 | Hold |
| 6 | Chronic pulmonary heart disease | 99.19% | L4 | 0 | 3 | Hold |
| **7** | **Prinzmetal angina** | **99.07%** | **L2** | **0** | **9** | **Proceed with Guardrails** |

† The 20 publications retrieved for Rank 2 are general hypoxia biology reviews (e.g., neurodegeneration, cancer, altitude physiology) — none address Felodipine in lung disease-related PH. Effective drug-specific evidence for this indication is absent.

‡ The single publication for Rank 4 (PMID 8893190) describes a post-adrenalectomy renovascular hypertension case with no relevance to Felodipine treatment.

---

## Best-Evidenced Indication: Prinzmetal Angina (Rank 7)

### Mechanistic Rationale

Prinzmetal (variant/vasospastic) angina arises from episodic coronary artery spasm causing transient transmural ischemia. The pathophysiological mechanism directly implicates smooth muscle L-type calcium channel activation. Calcium channel blockers therefore represent the **Class I, first-line pharmacotherapy** for this condition per ACC/AHA and ESC guidelines — their antivasospastic mechanism is the primary therapeutic basis, not a secondary or off-label extrapolation.

Felodipine, as a DHP-CCB with relatively high coronary vascular selectivity and a long-acting extended-release (ER) formulation enabling once-daily dosing, is particularly well-suited for continuous spasm suppression. Direct clinical studies confirm its efficacy specifically in Prinzmetal angina patients.

### Literature Evidence for Prinzmetal Angina

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1746458](https://pubmed.ncbi.nlm.nih.gov/1746458/) | 1991 | Comparative RCT | Am J Cardiology | Felodipine 10–20 mg once daily vs. nifedipine 20 mg QID in 30 Prinzmetal angina patients; demonstrated comparable antiischemic efficacy with once-daily dosing advantage |
| [8013514](https://pubmed.ncbi.nlm.nih.gov/8013514/) | 1994 | Clinical Provocation Study | European Heart Journal | Extended-release felodipine 20 mg effectively prevented ergonovine-induced myocardial ischemia at both 4 h and 24 h post-dose in 14 Prinzmetal angina patients |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Clinical Provocation Study | Am J Cardiology | Felodipine significantly reduced hyperventilation-induced ischemic attacks in variant angina; demonstrated 24-hour protective coverage |
| [7744087](https://pubmed.ncbi.nlm.nih.gov/7744087/) | 1995 | Double-blind RCT | European Heart Journal | Felodipine ER 10 mg improved exercise duration by 66 s vs. placebo (vs. 50 s for nifedipine SR); benefits sustained to end of dosing interval (24 h) |
| [7728649](https://pubmed.ncbi.nlm.nih.gov/7728649/) | 1995 | Focused Review | Can J Cardiology | CCBs as first-choice therapy in Prinzmetal's angina; Felodipine specifically reviewed for its vascular selectivity and sustained 24-hour antianginal coverage |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Review | Herz | Differential CCB therapy across indications including vasospastic angina; Felodipine's clinical profile discussed |
| [3345765](https://pubmed.ncbi.nlm.nih.gov/3345765/) | 1988 | Case Series | European Heart Journal | Exercise-induced ST-elevation patterns in Prinzmetal's angina; contextual clinical background |
| [19052677](https://pubmed.ncbi.nlm.nih.gov/19052677/) | 2008 | Case Report | Can J Cardiology | Vasospasm-induced polymorphic ventricular tachycardia; CCB management context |
| [15222138](https://pubmed.ncbi.nlm.nih.gov/15222138/) | 2004 | Case Report | Orvosi Hetilap | Nicergoline-induced Prinzmetal angina episode; CCB as rescue management |

---

## Supporting Evidence: Chronic Pulmonary Heart Disease (Rank 6, L4)

For chronic pulmonary heart disease (cor pulmonale), two older Felodipine-specific hemodynamic studies exist and are worth noting:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2838319](https://pubmed.ncbi.nlm.nih.gov/2838319/) | 1988 | Clinical Hemodynamic Study | European Respiratory Journal | Felodipine infusion (0.9 mg/h) in 11 advanced COLD patients reduced PVR by 18% and SVR by 33%, increased cardiac output by 32%, and improved biventricular ejection fraction — however, long-term outcome data are absent |
| [2487551](https://pubmed.ncbi.nlm.nih.gov/2487551/) | 1989 | Acute Hemodynamic Study | Cardiovascular Drugs Therapy | Felodipine in 10 chronic congestive heart failure patients; acute assessment of central hemodynamics and regional blood flow distribution |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovascular Drugs Therapy | CCB comparative efficacy across hypertension and minor cardiovascular indications; class-level context |

> ⚠️ Clinical caution: Despite these hemodynamic signals, CCBs in COPD-related pulmonary hypertension (WSPH Group 3) carry meaningful risks — particularly abolishing hypoxic pulmonary vasoconstriction (HPV) and worsening ventilation-perfusion mismatch. Current guidelines do not recommend CCBs for Group 3 PH. These older studies should not be interpreted as sufficient justification for clinical use without further investigation.

---

## Philippines Market Information

Felodipine is **not currently marketed or registered in the Philippines**. No FDA-Philippines (FR number) authorizations are on record in this evidence pack. This represents a primary regulatory barrier for any local repurposing pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Rank 1 Indication) | Proceed with Guardrails (Prinzmetal Angina, Rank 7)**

**Rationale:**
The top TxGNN-ranked prediction — pulmonary hypertension with unclear multifactorial mechanism — has no clinical evidence (L5) and carries mechanistic contraindications in the relevant WSPH Group 5 context; a Hold is clearly appropriate. By contrast, Prinzmetal angina (rank 7, score 99.07%, L2) is supported by multiple direct Felodipine clinical studies, aligns with Class I guideline recommendations for CCB use in vasospastic angina, and represents a biologically coherent and clinically meaningful repurposing opportunity warranting systematic evaluation.

**To advance the Prinzmetal angina repurposing pathway, the following steps are required:**

- **Regulatory registration**: Felodipine is not registered in the Philippines — an NDA or supplemental indication filing with FDA-Philippines is a prerequisite for any local clinical or commercial pathway
- **Safety documentation**: Retrieve complete package insert (PI/SmPC) for warnings, contraindications, and drug interactions; this data was unavailable in the current evidence pack (blocking gap DG001)
- **MOA data**: Query DrugBank API (DB01023) to retrieve the full mechanism of action profile (gap DG002), supporting both regulatory submissions and risk-benefit documentation
- **Guideline confirmation**: Verify current ACC/AHA and ESC guideline standing for CCB use in vasospastic angina to document Class I recommendation
- **Competitive landscape**: Map existing CCBs registered in the Philippines (e.g., amlodipine, nifedipine) for vasospastic angina; assess whether Felodipine's once-daily ER formulation offers meaningful clinical differentiation
- **Formulation availability**: Confirm the extended-release (ER) oral formulation is accessible locally, as the pivotal clinical studies used Felodipine ER

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

