---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Propranolol: From Cardiac Arrhythmia to Cardiomyopathy

## One-Sentence Summary

Propranolol is a well-established non-selective beta-adrenergic blocker with a long clinical history in cardiac arrhythmias, hypertension, and hypertrophic obstructive cardiomyopathy (HOCM), though original indication data is not available in this Evidence Pack.
This multi-indication TxGNN analysis identifies **6 new candidate indications**; among them, **cardiomyopathy** (broad category) is the most evidence-backed prediction with **3 registered trials** and **20 publications**, earning a **Proceed with Guardrails** recommendation.
The remaining five predictions — including cirrhotic cardiomyopathy, two rare myopathies, chondroma, and athlete's hypertrophic cardiomyopathy — currently range from **L4 to L5** evidence and are recommended to **Hold** pending further mechanistic or clinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack (propranolol is an established non-selective β-blocker for cardiovascular conditions) |
| Primary Predicted Indication | Cardiomyopathy (highest-evidence prediction among 6 candidates) |
| TxGNN Prediction Score | 99.12% (Rank 5,897 overall) |
| Evidence Level | L3 (observational studies + clinical series in HCM subtypes) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (cardiomyopathy) · **Hold** (all other 5 predictions) |

---

## All Predicted Indications

This is a multi-indication analysis (Candidate ID: TW-DB00571-multi). The table below summarizes all six TxGNN predictions ranked by score:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Distal myopathy, Tateyama type | 99.40% | L5 | Hold |
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | Hold |
| 3 | HCM due to intensive athletic training | 99.17% | L5 | Research Question |
| 4 | Chondroma | 99.14% | L5 | Hold |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L4 | Hold |
| 6 | Cardiomyopathy | 99.12% | L3 | **Proceed with Guardrails** |

> Ranks 5 and 6 share nearly identical TxGNN scores (0.99119 vs 0.99118) but differ substantially in evidence depth and clinical actionability.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, propranolol is a non-selective β1/β2 adrenergic receptor antagonist that competitively inhibits catecholamine binding, reducing heart rate, myocardial contractility, and cardiac oxygen demand. Its role in multiple cardiovascular conditions has been established over six decades of clinical use.

For **cardiomyopathy** — particularly hypertrophic obstructive cardiomyopathy (HOCM) — the mechanistic link is direct and historically confirmed: β1 receptor blockade reduces resting heart rate → prolongs diastolic filling time → decreases left ventricular outflow tract obstruction (LVOTO) dynamic gradients → alleviates symptoms. Propranolol also provides Class II antiarrhythmic protection, which is clinically relevant given the arrhythmia burden in HCM. Clinical studies published between 1980 and 1996 consistently documented hemodynamic and functional improvement in HOCM patients. However, the contemporary clinical trial landscape shows a striking reversal: all three currently registered trials are *deprescribing* studies, reflecting growing concern about beta-blocker utility in HFpEF and ATTR-CA subtypes. This nuance is critical — cardiomyopathy is not a single entity, and the evidence base is strongly subtype-dependent.

For **cirrhotic cardiomyopathy** (Rank 5), the mechanistic bridge runs through propranolol's existing first-line role in portal hypertension: while already used to prevent variceal hemorrhage in cirrhosis, it may simultaneously address the QT prolongation and sympathetic hyperactivation that define cirrhotic cardiomyopathy (CCM). A 2024 prospective clinical study (PMID 38738176) directly demonstrated QT-interval correction by propranolol in cirrhosis patients — the most current and mechanistically targeted evidence in this pack. However, a serious safety window problem exists: in advanced cirrhosis with refractory ascites, non-selective beta-blockers can impair renal perfusion and systemic hemodynamics (PMID 32446716), creating a risk–benefit conflict that currently prevents this candidate from advancing beyond S1 safety review.

For the four **Hold** indications, the high TxGNN scores almost certainly reflect graph topology proximity rather than genuine mechanistic relevance. Specifically: the two rare myopathies (CAV3 mutation, nebulin/ACTA1 defects) involve structural gene mutations unrelated to adrenergic signalling; chondroma is a low-activity benign cartilage tumour with negligible adrenergic receptor expression; and athlete's hypertrophic cardiomyopathy is a largely reversible adaptive response where the necessity of pharmacological intervention is questionable and propranolol's performance-impairing effects (banned substance in some sports) are a practical concern.

---

## Clinical Trial Evidence

The following trials are associated with the **cardiomyopathy** indication (Rank 6):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Phase 4 | Enrolling by Invitation | 20 | N-of-1 deprescribing trial in ATTR cardiac amyloidosis (ATTR-CA); tests whether *stopping* beta-blockers improves patient-reported outcomes — evidence runs counter to initiation for repurposing |
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Phase 3 | Unknown | 90 | Propranolol + Gabapentin combination for paroxysmal sympathetic hyperactivity (PSH) in traumatic brain injury ICU patients; indication is neurological, not cardiac |
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Phase 4 | Completed | 9 | N-of-1 deprescribing trial in older adults with HFpEF; completed with small sample; evaluates functional impact of discontinuing beta-blockers — indirect reverse-direction evidence |

> **Critical Note**: None of the three identified trials test propranolol *initiation* for cardiomyopathy. All three investigate whether *stopping* beta-blockers is safe or beneficial in specific subtypes. This reflects a contemporary reassessment in cardiology, not a validation of new use.

Currently no related clinical trials registered for cirrhotic cardiomyopathy (Rank 5).

---

## Literature Evidence

### Cardiomyopathy (Rank 6) — Top 10 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical Trial (Crossover) | British Heart Journal | Nifedipine + propranolol in 12 HOCM patients; combination superior to nifedipine alone; heart rate reduction and improved LV pressure outcomes during pacing |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Clinical Trial (Comparative) | Cardiology | Propranolol vs. disopyramide in 19 HCM patients; radionuclide ventriculography at rest and exercise; crossover design comparing LV functional effects |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Clinical Study | Journal of Cardiac Failure | 56 dilated cardiomyopathy (DCM) patients given escalating propranolol doses on top of ACE inhibitors and diuretics; hemodynamic predictors of early intolerance and long-term response identified via catheterisation and RV biopsy |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Clinical Study | British Heart Journal | Propranolol 0.2 mg/kg IV in 13 HOCM patients during cardiac catheterisation; measured myocardial O₂ consumption, substrate extraction, coronary sinus flow, and LV pressures at multiple pacing rates |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical Study | European Heart Journal | Propranolol IV vs. verapamil IV in HCM; both agents assessed for diastolic stiffness effects via LV cineangiography and high-fidelity pressure measurements; propranolol group n=9 |
| [2920304](https://pubmed.ncbi.nlm.nih.gov/2920304/) | 1989 | Clinical Study | Canadian Journal of Cardiology | Disopyramide + propranolol combination in 15 HCM patients; echo and hemodynamic parameters including systolic anterior motion slope and LVOTO diameter |
| [3673167](https://pubmed.ncbi.nlm.nih.gov/3673167/) | 1987 | Clinical Trial | Zeitschrift für Kardiologie | 15 HCM patients treated with oral nifedipine + propranolol for 6–24 months; 12 were verapamil pre-treated; treatment discontinued in 5 cases due to deterioration or side effects |
| [15923319](https://pubmed.ncbi.nlm.nih.gov/15923319/) | 2005 | Animal Study | Am J Physiol Heart Circ Physiol | Propranolol vs. epinephrine in virus-infected BALB/c mice; propranolol reduced inflammatory cytokine expression and improved survival in both acute and chronic viral myocarditis |
| [36104228](https://pubmed.ncbi.nlm.nih.gov/36104228/) | 2022 | Case Report | International Heart Journal | Male infant with neonatal mitochondrial cardiomyopathy and LVOT stenosis; successfully managed with low-dose propranolol + cibenzoline combination; genetic analysis confirmed m.13513G>A mutation |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical Study | American Journal of Cardiology | Propranolol in arrhythmia management in HCM; clinical characterisation of antiarrhythmic effects in this population |

### Cirrhotic Cardiomyopathy (Rank 5) — All 5 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Prospective Clinical Study | Frontiers in Pharmacology | Propranolol corrects prolonged QT intervals in cirrhosis patients; direct prospective evidence for QT normalization as a mechanism of benefit in CCM — strongest positive signal in this pack |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical Observational Study | Journal of Hepatology | NSBBs impair global circulatory homeostasis and renal perfusion pressure in cirrhotic patients with refractory ascites; critical safety signal distinguishing patients with diuretic-responsive vs. refractory ascites |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Pharmacodynamic Study | PLoS One | Real-time propranolol infusion in varying-severity cirrhosis; cardiovascular effects are blunted in higher-severity disease, suggesting a disease-severity-dependent therapeutic window |
| [25250684](https://pubmed.ncbi.nlm.nih.gov/25250684/) | 2015 | Cohort Study (Pediatric) | J Pediatr Gastroenterol Nutr | CCM incidence and features in children with portal hypertension; establishes pediatric CCM as a distinct entity with limited data, including diastolic and electrophysiological disturbances |
| [15387011](https://pubmed.ncbi.nlm.nih.gov/15387011/) | 2004 | Observational Study | Ugeskrift for Laeger | Prolonged QTc interval and mechanical systole dyssynchrony in cirrhosis; foundational characterisation of CCM electrophysiology that motivates QT-targeted interventions |

---

## Philippines Market Information

Propranolol is **not currently registered** with the Philippine FDA. No marketing authorizations were identified in this Evidence Pack (0 licenses, market status: Not Marketed).

This is notable given propranolol's inclusion on the WHO Model List of Essential Medicines and its decades of global clinical use. The absence of Philippine registration represents both a regulatory gap requiring investigation and a potential prerequisite that must be addressed before any repurposing program can be formally pursued in the Philippines.

---

## Safety Considerations

No Philippine FDA-specific warnings or contraindications are available in this Evidence Pack; please refer to the package insert for complete safety information.

Based on evidence identified during this analysis, the following literature-derived signals are relevant:

- **Cirrhotic Cardiomyopathy — Renal and Hemodynamic Risk**: Non-selective beta-blockers including propranolol have been shown to impair global circulatory homeostasis and renal perfusion pressure in cirrhotic patients with refractory ascites (PMID 32446716, *J Hepatol* 2020). This safety signal is dose- and disease-severity-dependent and defines a critical therapeutic window; use in Child-Pugh C patients with refractory ascites is contraindicated in current guidelines.

- **Blunted Cardiovascular Response in Advanced Cirrhosis**: A 2022 pharmacodynamic study (PMID 35763518) found that propranolol's cardiovascular effects are attenuated in higher-severity cirrhosis, which may complicate both efficacy and dosing in CCM patients.

- **Neonatal and Obstetric Considerations**: Case report (PMID 565899) documents fetal effects in a parturient on high-dose propranolol for idiopathic hypertrophic subaortic stenosis; relevant for cardiomyopathy patients of childbearing age.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** — Cardiomyopathy (Rank 6)
**Decision: Hold** — Cirrhotic cardiomyopathy, Distal myopathy Tateyama type, Congenital myopathy with excess of thin filaments, Chondroma (Ranks 1–5)
**Decision: Research Question** — HCM due to intensive athletic training (Rank 3)

**Rationale:**
Propranolol's role in hypertrophic cardiomyopathy (specifically HOCM) is grounded in decades of clinical data, and the beta-blockade mechanism directly addresses the core pathophysiology of dynamic LVOTO. However, the active trial landscape reflects a contemporary trend toward *deprescribing* beta-blockers in HFpEF and ATTR-CA, requiring precise subtype definition before any repurposing claim is made. For cirrhotic cardiomyopathy, a 2024 direct mechanistic study is promising but the documented risk of renal impairment in advanced liver disease demands a formal safety-first approach before proceeding.

**To proceed, the following is needed:**

- **Data Gap DG001**: Retrieve propranolol package insert (Philippine FDA or international reference label) to complete S1 safety screening — currently blocking
- **Data Gap DG002**: Query DrugBank API for formal mechanism of action data to strengthen mechanistic rationale
- **Subtype Clarification**: Define the exact cardiomyopathy subtype targeted for repurposing (HOCM, DCM, HFpEF, CCM, ATTR-CA); evidence quality and risk–benefit profile differ substantially across subtypes
- **Philippines Registration Pathway**: Assess regulatory requirements and timeline for initial drug registration with the Philippine FDA, as current non-marketed status must be resolved before any repurposing application
- **Cirrhotic Cardiomyopathy Safety Protocol**: Conduct S1 safety review with hepatology expert input; define Child-Pugh scoring thresholds and mandatory renal function monitoring criteria if CCM indication is to advance
- **Modern RCT Gap**: The HCM clinical evidence base predates modern RCT standards (largely 1980–1996); consider whether a prospective registry or pragmatic trial design is needed to meet current regulatory evidentiary requirements for a new indication filing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

