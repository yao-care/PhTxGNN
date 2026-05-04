---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is a first-generation oral ACE inhibitor, clinically established for treating hypertension and heart failure through competitive inhibition of the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **0 clinical trials** and **20 publications** currently supporting this direction.
Evidence is primarily observational and review-based, reflecting the mechanistically well-understood but formally underexplored nature of this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Heart Failure (regulatory record not available in Philippines database) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory database. Based on known clinical information, Captopril is a first-generation ACE (angiotensin-converting enzyme) inhibitor — it competitively blocks ACE (dipeptidyl carboxypeptidase), preventing the conversion of angiotensin I to the potent vasoconstrictor angiotensin II. The result is systemic vasodilation, reduced aldosterone secretion, lower blood pressure, and decreased cardiac afterload. Its efficacy in essential hypertension, heart failure, and diabetic nephropathy is well established, and the same RAAS-blocking mechanism is pathophysiologically central to malignant renovascular hypertension.

Malignant renovascular hypertension arises from renal artery stenosis causing severe, compensatory RAAS over-activation: reduced renal perfusion → elevated renin secretion → angiotensin II surge → extreme blood pressure elevation with progressive end-organ damage (renal failure, papilloedema, hypertensive encephalopathy). Captopril directly interrupts this causal chain, giving it an exceptionally high theoretical fit for this condition. This mechanistic relationship is so established that the **"captopril renography"** diagnostic test exploits it directly — captopril administration exaggerates perfusion asymmetry in stenotic kidneys, enabling non-invasive diagnosis of renovascular disease.

A critical clinical caveat applies: in patients with **bilateral renal artery stenosis** or **stenosis affecting a solitary functioning kidney**, ACE inhibitor-induced reduction of efferent arteriolar tone can precipitate acute kidney injury by collapsing glomerular filtration pressure. This risk — well-recognised in clinical practice — is the central "guardrail" for this indication and mandates systematic imaging-based screening before initiation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clin Sci (London) | Captopril-induced reactive hyper-reninaemia identifies renovascular HTN with high sensitivity; distinguishes renovascular from essential hypertension — foundational diagnostic evidence |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Observational | Biulleten' VK nauchnogo tsentra | Captopril use in arterial hypertension including stable and malignant course; clinical observation of treatment outcomes |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Experimental/Observational | Japanese Heart Journal | Neurohormonal profiling in 2K2C Goldblatt hypertension model (benign vs. malignant phases); quantifies RAAS activation pattern supporting Captopril's mechanistic rationale |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | J Pediatrics | Review of malignant hypertension including pathophysiology and management principles |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | Captopril renal scintigraphy in malignant hypertension without confirmed renal artery stenosis; illustrates diagnostic utility and potential false-positive findings |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review / Case Series | Endocrinol Metab Clin North Am | Renin-secreting JG cell tumors causing severe HTN; blood pressure drops with captopril; validates RAAS-directed ACE inhibition in high-renin renovascular states |
| [10477101](https://pubmed.ncbi.nlm.nih.gov/10477101/) | 1999 | Case Series | European J Radiology | Captopril renography in reninoma and page kidney; negative results highlight limitations of the test outside classic renal artery stenosis |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | NF1 children with renal artery stenosis-induced HTN; captopril test used to characterise and confirm renovascular involvement |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report + Review | Clinical Nephrology | Two renovascular HTN cases with neurofibromatosis; captopril provocation produced marked PRA rise confirming RAAS-mediated aetiology |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Narrative Review | Minerva Medica | Renovascular hypertension clinical concepts; treatment strategies including RAAS blockade and indications for revascularisation |

---

## Philippines Market Information

Captopril is currently **not registered in the Philippines**. No product authorisation records were found in the FDA Philippines database. Market entry would require a full registration application to the Philippines Food and Drug Administration (FDA PH).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Captopril's ACE-inhibitory mechanism aligns directly with the RAAS-driven pathophysiology of malignant renovascular hypertension, and its established role in captopril renography demonstrates its pharmacological centrality in this clinical context. Although no formal RCTs have been identified for this specific indication and current evidence is observational/review-based (L3), the mechanistic case is both strong and well-understood. The primary risk — acute kidney injury in bilateral renal artery stenosis — is a recognised, manageable hazard that demands structured patient selection protocols rather than precluding use outright.

**To proceed, the following is needed:**
- Obtain renal artery imaging (Doppler ultrasound or MR angiography) to screen for bilateral stenosis before initiation
- Establish a renal function monitoring protocol (serum creatinine, potassium, eGFR) at baseline and at 1–2 weeks after starting treatment
- Retrieve the Philippines FDA package insert (or international label) to document approved indications, black-box warnings, and contraindications — currently a blocking data gap
- Complete DrugBank MOA and pharmacokinetic data to support formal mechanism-of-action analysis
- Evaluate feasibility of Philippines market registration, given that Captopril is currently unlicensed locally
- Consider whether a second-generation, longer-acting ACE inhibitor (e.g., enalapril, ramipril) with a more established tolerability and evidence base might be preferred over Captopril for formal indication development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

