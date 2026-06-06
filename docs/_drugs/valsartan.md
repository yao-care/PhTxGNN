---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 7
---

# Valsartan
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II type 1 (AT1) receptor blocker (ARB) internationally established for hypertension, heart failure, and post-myocardial infarction — but not currently registered in the Philippines.
The TxGNN model assigns its highest prediction score to **Malignant Hypertensive Renal Disease** (99.97%),
supported by **0 clinical trials** and **1 background publication** that studied a different drug (avosentan), making direct Valsartan-specific evidence essentially absent for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Philippines registry (Valsartan is not registered locally; internationally indicated for hypertension and heart failure) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on known pharmacological information, Valsartan is an angiotensin II type 1 (AT1) receptor blocker that reduces angiotensin II-mediated vasoconstriction, aldosterone secretion, and sympathetic activation. Through AT1 blockade, it decreases intraglomerular pressure by dilating the efferent arteriole — a mechanism central to renal protection in hypertensive states.

Malignant hypertensive renal disease involves severe, rapidly progressive glomerular injury driven by uncontrolled arterial hypertension. The RAAS system plays a pivotal role in sustaining the malignant cycle: elevated angiotensin II causes afferent arteriolar vasoconstriction and glomerular hyperperfusion. The ARB drug class has established renal protection in landmark trials (RENAAL, IDNT) for diabetic nephropathy, suggesting biological plausibility for Valsartan in hypertensive nephropathy more broadly.

However, the only literature retrieved for this specific indication (PMID 24368192) investigates **avosentan** — an endothelin receptor antagonist — in a double-transgenic rat model, not Valsartan. This substantially weakens the direct evidence base. The high TxGNN score likely reflects structural proximity in the knowledge graph between ARB-class nodes and hypertensive renal disease nodes, rather than Valsartan-specific validated clinical data for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Valsartan in malignant hypertensive renal disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Animal / Preclinical | Pharmacological Research | Avosentan (endothelin receptor antagonist, not Valsartan) demonstrated renal protection in double transgenic rats overexpressing human renin and angiotensinogen at sub-fluid-retention doses. Provides indirect evidence for RAAS-related renal protection but does not directly validate Valsartan in this indication. |

---

## Philippines Market Information

Valsartan is not currently registered with the Philippine FDA (Food and Drug Administration Philippines). No authorization records or product licenses are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level safety note for ARBs**: Although formal Philippines FDA labeling data is unavailable for this report, ARB drugs including Valsartan carry well-recognized class-specific risks that must be reviewed before clinical application: acute renal failure risk in patients with bilateral renal artery stenosis or solitary functioning kidney, hyperkalemia (especially with concomitant potassium-sparing diuretics or ACE inhibitors), and absolute contraindication in pregnancy (fetotoxicity). These considerations are especially relevant given that malignant hypertensive renal disease patients may have underlying renovascular compromise.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the AT1 receptor blockade mechanism of Valsartan is biologically plausible for malignant hypertensive renal disease, there are no registered clinical trials and the only retrieved literature examines a structurally unrelated drug (avosentan). The L4 evidence level is insufficient to support advancement beyond a hypothesis-generation stage.

**To proceed, the following is needed:**
- Identification of Valsartan-specific (or ARB-class) human observational or interventional data for malignant hypertensive renal disease
- Retrieval of full MOA documentation from DrugBank API (currently flagged as DG002)
- Download and parsing of Philippines FDA package insert to populate key warnings and contraindications (currently flagged as DG001)
- Subgroup analysis review of established ARB trials (RENAAL, IDNT, VALIANT) for malignant hypertension endpoints
- Clarification of the AT1 blockade safety boundary in renovascular hypertension (bilateral renal artery stenosis risk)

---

> **Additional Signal — Chronic Pulmonary Heart Disease (Rank 6):** While not the top-ranked TxGNN prediction, this indication carries the strongest evidence in this pack: 2 Grade-A trials (including a completed Phase 4 RCT of Sacubitril/Valsartan in HFrEF, NCT02768298) and 20 publications including post-hoc RCT analyses from PARADIGM-HF and PARAGON-HF. Evidence level L3 with a "Proceed with Guardrails" recommendation — this indication warrants a dedicated evaluation report.

---

*This report is generated for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

