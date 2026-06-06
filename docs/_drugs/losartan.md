---
layout: default
title: Losartan
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 8
---

# Losartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Losartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Losartan is an angiotensin II type 1 receptor (AT1) blocker widely established as a first-line treatment for hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with **0 clinical trials** and **1 publication** currently supporting this direction — all at the preclinical/animal model level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Diabetic Nephropathy |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacology, Losartan is an angiotensin II type 1 receptor (AT1) blocker — the first oral ARB to reach the market. Its proven efficacy in lowering blood pressure and reducing proteinuria in diabetic nephropathy is well-established, and these same mechanisms make it a biologically plausible candidate for malignant hypertensive renal disease.

Malignant hypertensive renal disease is characterized by extreme and sustained elevation of blood pressure with end-organ damage to the kidneys. Its core pathology centers on hyperactivation of the renin–angiotensin–aldosterone system (RAAS): excess Ang II drives AT1-mediated glomerular hypertension, afferent arteriole vasoconstriction, and downstream NF-κB–mediated tubulo-interstitial inflammation leading to nephrosclerosis and accelerated renal failure. Since Losartan directly blocks the AT1 receptor, the mechanistic link is both direct and highly plausible.

The one available animal study (PMID 30809002) confirms this pathway: rats exposed to an NF-κB inhibitor during lactation develop adult-onset hypertension, and uninephrectomy combined with salt overload unmasks latent renal dysfunction with hallmarks of malignant nephrosclerosis driven by Ang II and NF-κB signaling. This validates the target mechanism but does not constitute clinical evidence for Losartan in this specific phenotype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical / Animal Model | Hypertension Research | Ang II and NF-κB activation are central drivers of nephrosclerosis in a rat model of malignant hypertensive renal disease; uninephrectomy + salt overload unmasks latent renal dysfunction, establishing the RAAS/AT1 pathway as a pathogenic target |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Losartan's AT1 blockade and malignant hypertensive renal disease is biologically direct and well-grounded, but the evidence base is limited to a single preclinical animal study with no registered clinical trials anywhere in the world for this specific indication. L4-level evidence is insufficient to support a clinical development decision without further human data.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data sourced from DrugBank API to complete the mechanistic analysis
- Philippine FDA package insert to fill safety gaps: key warnings, contraindications, and drug–drug interactions
- Systematic review or retrospective cohort study examining ARB use outcomes specifically in malignant hypertensive nephrosclerosis (not general CKD or diabetic nephropathy)
- At minimum a Phase 2 proof-of-concept study targeting this renal phenotype, with biomarkers such as serum creatinine, proteinuria, and renal biopsy histology as endpoints
- Assessment of route compatibility and dosing adequacy for this higher-severity indication (malignant hypertension typically requires urgent BP control that oral agents alone may not achieve)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

