---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 6
---

# Atorvastatin
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

# Atorvastatin: From Dyslipidemia to Familial Hypercholesterolemia

## One-Sentence Summary

Atorvastatin is a synthetic HMG-CoA reductase inhibitor (statin), globally established as a first-line treatment for primary hypercholesterolemia, mixed dyslipidemia, and cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)** — a hereditary disorder of LDL-C metabolism caused by mutations in LDLR, APOB, or PCSK9 genes — with **34 clinical trials** and **19 publications** currently supporting this direction.
Evidence quality is the highest possible at **L1**, anchored by multiple completed Phase 3 RCTs enrolling hundreds of participants across both heterozygous and homozygous FH subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Primary hypercholesterolemia / cardiovascular risk reduction (globally approved; no Philippines registration on file) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data was not retrieved from the drug database. Based on established pharmacology, Atorvastatin belongs to the HMG-CoA reductase inhibitor (statin) class, and its mechanism is among the best-characterized in modern medicine. It competitively blocks HMG-CoA reductase — the rate-limiting enzyme in hepatic cholesterol biosynthesis — reducing endogenous cholesterol production. The resulting intracellular cholesterol deficit triggers compensatory upregulation of LDL receptors on hepatocyte surfaces, which accelerates clearance of circulating LDL-C from the bloodstream. Atorvastatin also reduces triglyceride levels and modestly raises HDL-C through secondary pathways.

Familial hypercholesterolemia arises precisely from mutations that impair this LDL receptor pathway (LDLR loss-of-function, APOB ligand defects, or PCSK9 gain-of-function), resulting in severely elevated LDL-C from birth. Atorvastatin's mechanism directly targets this pathophysiology: even when receptor density or function is partially reduced (as in heterozygous FH), pharmacological upregulation of residual receptor expression still achieves clinically meaningful LDL-C reductions. This is why atorvastatin is already the cornerstone of FH therapy in international guidelines — making the TxGNN prediction a strong mechanistic match rather than a speculative extrapolation.

In homozygous FH, where LDLR-mediated pathways are severely or completely abolished, atorvastatin as monotherapy is insufficient, but it remains a necessary backbone of combination regimens (alongside ezetimibe and PCSK9 inhibitors), reinforcing its indispensable role across the entire FH spectrum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Double-blind RCT of alirocumab vs. placebo added on to stable atorvastatin-containing therapy in HeFH; primary endpoint LDL-C reduction at 24 weeks; validates atorvastatin as standard background therapy in HeFH |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | Torcetrapib/atorvastatin vs. maximally tolerated atorvastatin alone in HeFH; 24-month carotid B-mode ultrasound endpoint; largest FH-specific atorvastatin structural outcomes study |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg co-administered with atorvastatin or simvastatin in homozygous FH; high-quality combination therapy evidence for the most severe FH phenotype |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | 3-year open-label atorvastatin in children and adolescents (age 6–17) with HeFH; characterised sustained cholesterol reduction, growth, and developmental safety over long-term use |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab (PCSK9 inhibitor) on top of maximally tolerated statin therapy (primarily atorvastatin) in HeFH not at LDL-C goal; LDL-C reduction at 24 weeks |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Long-term open-label extension assessing alirocumab safety and efficacy in heFH patients whose background regimen included atorvastatin; multi-year follow-up data |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Head-to-head RCT: alirocumab add-on vs. ezetimibe add-on vs. atorvastatin dose escalation vs. switch to rosuvastatin in HeFH/high-CV-risk patients uncontrolled on atorvastatin |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Ezetimibe + atorvastatin combination in HeFH or CHD with primary hypercholesterolemia uncontrolled on atorvastatin 10 mg; supports step-up combination strategy |
| [NCT06632379](https://clinicaltrials.gov/study/NCT06632379) | Phase 4 | Recruiting | 76 | SPARK trial: double-blind RCT of atorvastatin 10 mg vs. placebo postpartum in individuals with hypertensive disorders of pregnancy; evaluates cardiovascular risk score improvement in a high-risk FH-adjacent population |
| [NCT06686615](https://clinicaltrials.gov/study/NCT06686615) | N/A | Recruiting | 2,000 | Large real-world observational study of bempedoic acid + ezetimibe + atorvastatin/rosuvastatin in primary hypercholesterolemia; provides real-world effectiveness and safety data for atorvastatin-containing combination regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [11058703](https://pubmed.ncbi.nlm.nih.gov/11058703/) | 2000 | Clinical Trial | Atherosclerosis | Atorvastatin (10–40 mg/day escalation) in 9 homozygous FH patients on LDL-apheresis; 5/9 responded with significant LDL-C reductions and suppressed cholesterol synthesis — first direct evidence in hoFH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical RCT | Ann Pharmacother | Review of pivotal clinical trial data establishing atorvastatin efficacy and safety in primary hypercholesterolemia and mixed dyslipidemias; documented dose-dependent LDL-C lowering up to 60% |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Clinical Trial | Nutr Metab Cardiovasc Dis | Atorvastatin vs. simvastatin in heterozygous FH; atorvastatin demonstrated superior LDL-C lowering and greater attainment of NCEP LDL-C goals, along with favourable effects on fibrinogen |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical Trial | J Clin Lipidol | 3-year open-label atorvastatin study in children aged 6–17 with HeFH; sustained LDL-C reduction over 3 years with no adverse effects on linear growth, body weight, BMI, or sexual maturation |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Systematic Review | Curr Atheroscler Rep | Comprehensive review of novel and established pharmacological therapies for homozygous FH; confirms statins (including atorvastatin) as the obligatory backbone of all combination regimens for LDL-C lowering in HoFH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guidelines | Endocr Pract | AACE/ACE Guidelines for dyslipidemia management and cardiovascular disease prevention; statins are designated first-line therapy for all FH subtypes, with atorvastatin as a preferred high-intensity agent |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Study | J Am Coll Cardiol | Statin therapy in heterozygous FH significantly reduces coronary artery disease events and all-cause mortality; provides the first population-level quantification of clinical survival benefit from statin use in FH |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Foundational pharmacology review of atorvastatin: HMG-CoA reductase inhibition, prolonged half-life of active metabolites (20–30h), dose-dependent reductions across all lipid fractions, and early efficacy data in hypercholesterolaemia |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Pharmacogenomic Study | Pharmacogenomics J | NGS strategy combining FH gene panel with statin pharmacogenomics; provides a practical framework for genotype-guided atorvastatin dosing in FH patients to optimise response and minimise adverse effects |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Cohort/Quality Improvement | J Am Coll Cardiol | Quality improvement framework for FH patient monitoring and care; underscores atorvastatin as cornerstone therapy requiring systematic LDL-C monitoring, family cascade screening, and long-term adherence support |

---

## Philippines Market Information

Atorvastatin currently has **no registered products** with the Philippines FDA. There are no authorization records on file, and the drug is not commercially marketed in the Philippines.

> This absence of local registration does not preclude access via hospital formulary procurement or compassionate use, but formal market authorization would be required before routine commercial availability and reimbursement can be established.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atorvastatin holds the strongest possible L1 evidence for familial hypercholesterolemia, with multiple completed Phase 3 RCTs spanning heterozygous and homozygous FH, paediatric and adult populations, and both monotherapy and combination therapy settings; international guidelines uniformly endorse it as first-line therapy, and its mechanism directly addresses FH pathophysiology. The central barrier for the Philippines is not efficacy or safety uncertainty, but rather the complete absence of local regulatory registration.

**To proceed, the following is needed:**

- **Philippines FDA registration**: Submit a new drug application using the existing global regulatory dossier (US FDA/EMA-approved labelling) for Atorvastatin in hypercholesterolemia and FH indications
- **Package insert documentation**: Obtain and localise the formal prescribing information to document approved dosing, warnings, contraindications, and drug interactions (currently unavailable in this evidence pack)
- **Drug–drug interaction review**: Characterise interactions between atorvastatin and medications commonly co-prescribed in the Philippines (including antiretrovirals, antifungals, and macrolide antibiotics relevant to the local disease burden), given atorvastatin's CYP3A4 and OATP1B1 metabolism
- **Paediatric FH programme**: Establish referral pathways for cascade screening and early statin initiation in children with confirmed FH, in alignment with international guidance recommending treatment from age 8–10
- **Local guideline alignment**: Engage the Philippine Heart Association and Philippine Lipid and Atherosclerosis Society to incorporate FH-specific atorvastatin recommendations into national cardiovascular disease prevention guidelines
- **Pharmacovigilance plan**: Define monitoring protocols for liver function tests, creatine kinase levels, and myopathy surveillance appropriate for the Philippine clinical setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

