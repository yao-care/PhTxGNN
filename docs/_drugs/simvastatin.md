---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 8
---

# Simvastatin
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a globally established HMG-CoA reductase inhibitor (statin) used for treating hypercholesterolemia and dyslipidemia, though it currently has no registered products in the Philippines.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**, with **19 clinical trials** and **18 publications** currently supporting this direction.
Evidence strength is rated L1, reflecting multiple completed Phase 3 RCTs with direct data on Simvastatin as a cornerstone treatment in FH patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Dyslipidemia (globally approved; no Philippines registration on file) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the repurposing rationale and the supporting literature, Simvastatin belongs to the statin drug class and acts by inhibiting HMG-CoA reductase — the rate-limiting enzyme in hepatic cholesterol biosynthesis. By reducing cholesterol production in the liver, the hepatocytes compensatorily upregulate LDL receptor expression on their surface, which in turn enhances the clearance of circulating LDL cholesterol from the bloodstream.

Familial Hypercholesterolemia (FH) is a monogenic disorder caused by mutations in the LDLR, APOB, or PCSK9 genes, resulting in structurally deficient or absent LDL receptors and severely elevated LDL-C from birth. In the heterozygous form (HeFH), residual receptor activity remains, and statins can further amplify this activity through compensatory upregulation — making Simvastatin mechanistically well-suited as a first-line treatment for HeFH. Even in homozygous FH (HoFH), statins are recommended as part of combination therapy. The mechanistic link is direct and well-supported by decades of biochemical research.

The clinical evidence strongly corroborates this prediction. The landmark ENHANCE trial (NCT00552097, n=720) directly compared high-dose Simvastatin monotherapy versus ezetimibe/Simvastatin combination in HeFH patients, and multiple Phase 3 RCTs have used Simvastatin as the backbone of FH treatment arms. Current major international guidelines (AACE/ACE, 2017) explicitly endorse statins including Simvastatin as the cornerstone of FH pharmacological management. The TxGNN score of 99.63% and L1 classification are fully consistent with Simvastatin's globally recognized role as standard-of-care for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE Trial: Head-to-head comparison of high-dose Simvastatin alone vs. ezetimibe + Simvastatin in HeFH patients; evaluated carotid intima-media thickness (cIMT) progression as primary endpoint — the definitive Phase 3 trial using Simvastatin as the reference arm |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Evaluated efficacy and safety of ezetimibe co-administered with atorvastatin or Simvastatin in homozygous FH patients; Simvastatin used as a primary treatment backbone in this rare, high-severity population |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label extension of NCT03884452; assessed sustained safety and tolerability of ezetimibe + Simvastatin in hoFH over 2 years |
| [NCT01414192](https://clinicaltrials.gov/study/NCT01414192) | N/A | Completed | 3,215 | MOBS bridging study: Large French real-world cohort tracking Inegy® (ezetimibe/simvastatin) use, LDL-C goal attainment, and cardiovascular morbidity over 6 years — provides robust real-world effectiveness data |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2,089 | Japanese regulatory re-examination of VYTORIN (ezetimibe/simvastatin) in routine clinical practice; confirmed simvastatin component safety and effectiveness in a large post-marketing cohort |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Randomized controlled trial of ezetimibe co-administration with Simvastatin in adolescents (ages 10–17) with HeFH; evaluated LDL-C reduction and safety in the pediatric FH population |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy (potentially including Simvastatin) in HeFH or high-CV-risk patients; confirmed statin background as the standard of care for this population |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam add-on to pediatric statin monotherapy (including Simvastatin) in HeFH patients aged 10–17; validated Simvastatin's role as the essential lipid-lowering foundation in this age group |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab (PCSK9 inhibitor) in HeFH inadequately controlled on LMT; statin background treatment (including Simvastatin) confirmed as necessary baseline across all enrolled patients |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Six-week open-label comparison of rosuvastatin vs. Simvastatin in Fredrickson Type IIa/IIb dyslipidemia including HeFH; assessed renal effects and comparative lipid efficacy of both statins |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | ENHANCE trial: Simvastatin 80 mg ± ezetimibe in FH; greater LDL-C reduction with combination but no incremental reduction in carotid IMT at 2 years — pivotal high-quality trial directly evaluating Simvastatin in FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocrine Practice | AACE/ACE guidelines for dyslipidemia and cardiovascular disease prevention; statins including Simvastatin endorsed as cornerstone pharmacotherapy for FH with explicit LDL-C targets |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Systematic Review | Expert Opin Drug Safety | Comprehensive benefit-risk assessment of Simvastatin specifically in FH patients; reviewed long-term safety including myopathy, hepatotoxicity, and teratogenicity; confirmed favorable benefit-risk profile for chronic FH treatment |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane SR | Cochrane Database Syst Rev | Cochrane systematic review of statins for children with familial hypercholesterolemia; concluded statins are effective (significant LDL-C reduction) and safe in pediatric HeFH, supporting early initiation |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Observational Study | J Am Coll Cardiol | Large cohort study quantifying statin-induced reduction in coronary artery disease events and all-cause mortality in HeFH patients; demonstrated statins reduce mortality risk toward general population levels |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort Study | J Clin Med | Cross-sectional study assessing innate and acquired cellular immunity in children with FH treated with Simvastatin 10 mg for ≥26 weeks; confirmed no significant adverse immunological effects in pediatric FH population |
| [2083515](https://pubmed.ncbi.nlm.nih.gov/2083515/) | 1990 | Narrative Review | Drugs | Foundational pharmacological review: Simvastatin 10–40 mg once daily reduces total and LDL-C by 30–45% in heterozygous familial and nonfamilial hypercholesterolaemia; established the pharmacological basis for statin use in FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of Simvastatin specifically in familial hypercholesterolaemia; highlighted LDL-C reduction and cardiovascular risk benefit alongside tolerability data from long-term FH treatment |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Review | Pharmacogenomics J | Novel NGS strategy combining FH genetic diagnosis with statin pharmacogenomics panel; proposes genotype-guided statin selection to optimize treatment in FH — positions Simvastatin within precision medicine framework |
| [32800790](https://pubmed.ncbi.nlm.nih.gov/32800790/) | 2020 | Case Report | J Clin Lipidology | Decade-long management of a child with compound heterozygous FH (LDL-C 17.4 mmol/L at age 5); Simvastatin used as part of an escalating combination regimen — illustrates real-world clinical management trajectory in severe pediatric FH |

---

## Philippines Market Information

Simvastatin currently has **no registered products** in the Philippines (Philippine FDA total licenses: 0). No authorization records are available for tabulation.

This absence of local registration is a key operational gap. Simvastatin is widely registered and used globally (including the United States, European Union, Japan, and Taiwan) for hypercholesterolemia and related indications. Registration in the Philippines would require a formal New Drug Application or bioequivalence submission to the Philippine FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Simvastatin is globally recognized as a first-line standard-of-care treatment for familial hypercholesterolemia, backed by L1 evidence including the landmark ENHANCE trial (n=720), multiple Phase 3 RCTs using Simvastatin as the treatment backbone, Cochrane-level systematic reviews, and major international clinical guidelines (AACE/ACE 2017). The TxGNN prediction score of 99.63% is consistent with this well-validated, mechanistically sound indication. The primary barrier to clinical deployment is the absence of Philippine FDA registration, not evidence insufficiency.

**To proceed, the following is needed:**
- **Philippines FDA registration**: Submit a New Drug Application or bioequivalence filing for Simvastatin to the Philippine FDA, as no products are currently registered locally
- **Package insert retrieval**: Download and parse the official Philippine or reference country (e.g., FDA US, EMA) package insert PDF to formally document key warnings, contraindications, and dosing instructions (currently flagged as blocking data gap DG001)
- **MOA documentation**: Query DrugBank API (DB00641) to retrieve structured mechanism of action data to complete the pharmacological rationale (data gap DG002)
- **DDI assessment**: Establish a systematic drug-drug interaction screening protocol, with special attention to CYP3A4 inhibitors (azole antifungals, macrolide antibiotics, HIV protease inhibitors) which can dramatically elevate Simvastatin plasma exposure and increase myopathy/rhabdomyolysis risk
- **FH genotype stratification**: Define separate LDL-C treatment targets and monitoring schedules for HeFH vs. HoFH, as homozygous patients have limited LDL receptor response to statins and typically require combination therapy or LDL apheresis
- **Baseline safety monitoring plan**: Define pre-treatment and on-treatment monitoring parameters (liver function tests, CK levels) prior to initiating Simvastatin in FH patients in the Philippine clinical setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

