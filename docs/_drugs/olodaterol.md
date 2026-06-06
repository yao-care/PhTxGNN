---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
---

# Olodaterol
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

# Olodaterol: From COPD Maintenance to Bronchitis

## One-Sentence Summary

Olodaterol (Striverdi® Respimat®) is a once-daily long-acting β2-adrenergic agonist (LABA) established as maintenance bronchodilator therapy for chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **Bronchitis**, with **3 clinical trials** and **2 publications** currently supporting this direction.
The mechanistic rationale is strong for the chronic obstructive bronchitis phenotype, though the overall evidence grade remains observational.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD maintenance bronchodilator therapy |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, olodaterol is a selective long-acting β2-adrenergic agonist (LABA). Its established mechanism involves β2 receptor activation → Gs-protein coupling → adenylyl cyclase stimulation → intracellular cAMP elevation → PKA activation → bronchial smooth muscle relaxation. Once-daily inhalation sustains 24-hour continuous bronchodilation. Olodaterol also exerts an auxiliary anti-inflammatory effect by suppressing mast cell mediator release.

The link between COPD and bronchitis is clinically well-recognised: chronic bronchitis is itself a defining phenotype of COPD (productive cough ≥3 months/year for 2 consecutive years with airflow obstruction). In this COPD–chronic bronchitis (COPD-CB) subtype, olodaterol's mechanism directly targets the hallmark features of excessive airway smooth muscle tone and progressive airflow limitation, making the mechanistic case compelling. By contrast, for acute infectious bronchitis — where mucosal infection and impaired mucociliary clearance dominate — the rationale is weaker.

The high TxGNN score (99.84%) reflects the close disease-class proximity between bronchitis and COPD within the knowledge graph. Multiple real-world studies that enrolled COPD patients specifically documented chronic bronchitis and emphysema as enrolled subtypes, demonstrating that the evidence base substantially overlaps with the target population. This cross-indication coherence supports the biological plausibility of the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A (PMS) | Completed | 1,335 | Post-marketing surveillance of Tiotropium/Olodaterol (Spiolto) in Japanese COPD patients; study population explicitly includes the chronic bronchitis and emphysema subtypes; assessed long-term safety and real-world effectiveness |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A (RWE) | Completed | 11,316 | Large real-world comparison of TIO/OLO versus FF/UMEC/VI (triple therapy) for disease burden, healthcare costs, and clinical outcomes in COPD; population overlap with chronic bronchitis diagnosis codes |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A (DUS) | Completed | 22,155 | Drug utilisation study of aclidinium bromide in European COPD patients including bronchitis subpopulations; primary drug is not olodaterol — indirect evidence for patient population characterisation only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Narrative Review | American Journal of Health-System Pharmacy | Comprehensive review of olodaterol pharmacology, pharmacokinetics, efficacy, and safety as a once-daily LABA; confirms established role in obstructive airway disease including chronic bronchitis subtype of COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Clinical Practice Guideline | Basic & Clinical Pharmacology & Toxicology | Finnish national COPD guideline covering diagnosis, risk stratification, and stepwise pharmacotherapy; addresses chronic bronchitis phenotype management and the role of long-acting bronchodilators |

---

## Philippines Market Information

Olodaterol currently has **no registered products in the Philippines**. No authorization number, product name, or indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting olodaterol specifically for bronchitis is limited to observational and post-marketing studies (L3), with no direct randomised controlled trials targeting bronchitis as a primary endpoint; combined with the absence of any Philippines registration and a complete gap in local safety and MOA documentation, the data is insufficient to support a go decision at this stage.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Retrieve the international package insert (FDA/EMA label for Striverdi® or Spiolto® Respimat®) to extract warnings, contraindications, and key drug interactions — this is a prerequisite for any safety evaluation
- **MOA documentation (High priority):** Query DrugBank API (DB09080) for complete mechanism of action and pharmacodynamic data to support the mechanistic rationale section
- **Population clarification:** Define the precise target: acute infectious bronchitis (olodaterol likely not beneficial) versus chronic obstructive bronchitis/COPD-CB phenotype (strong mechanistic and indirect clinical rationale)
- **Regulatory pathway assessment:** Evaluate Philippines FDA requirements for registering an inhaled bronchodilator not currently marketed locally; determine whether a new indication submission or a market entry application is required first
- **Direct clinical evidence:** If pursuing the COPD-CB phenotype indication, identify existing Phase 3 subgroup analyses reporting outcomes specifically in the chronic bronchitis population from the TonaDO or OTEMTO trial programs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

