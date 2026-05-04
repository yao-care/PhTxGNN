---
layout: default
title: Daclatasvir
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Daclatasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Daclatasvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Daclatasvir (DrugBank ID: DB09102) is a direct-acting antiviral NS5A replication complex inhibitor established in clinical practice for the treatment of chronic Hepatitis C virus (HCV) infection.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection** with a score of **99.80%**; however, the **35 clinical trials** and **19 publications** retrieved overwhelmingly reflect HCV treatment contexts and HBV safety monitoring in co-infected patients — not direct anti-HBV therapeutic evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Daclatasvir is a first-in-class, pangenotypic HCV NS5A replication complex inhibitor. By binding the NS5A protein — which is essential for HCV RNA replication, assembly, and virion release — daclatasvir disrupts the viral lifecycle across all major HCV genotypes. In combination with sofosbuvir or asunaprevir, it has achieved sustained virologic response (SVR12) rates exceeding 90% in interferon-free regimens. Detailed mechanism of action data from DrugBank could not be retrieved for this report (Data Gap DG002); however, its class pharmacology is well-characterized in the peer-reviewed literature.

The mechanistic bridge to Hepatitis B virus is fragile. HBV belongs to the Hepadnaviridae family and replicates via reverse transcription of a pregenomic RNA (pgRNA), a fundamentally different biology from HCV's RNA replicon system. Critically, the HBV genome encodes no NS5A homologue — daclatasvir's sole confirmed molecular target. The high TxGNN score (rank 1,859 overall) most likely reflects the dense co-occurrence of HCV and HBV nodes in the knowledge graph (co-infection pathways, shared hepatology ontology), rather than a true mechanistic repurposing signal.

The only biological hypothesis connecting daclatasvir to HBV comes from a single 2023 computational study (PMID 36838792), which used virtual docking to propose that daclatasvir may bind the ε stem-loop of HBV pregenomic RNA — an attractive but entirely unvalidated target. Notably, several case reports and cohort studies document HBV reactivation in HCV/HBV co-infected patients receiving daclatasvir-containing regimens (PMID 26297529, 27329484, 29194858) — these are safety warnings, not efficacy signals, and in fact argue that daclatasvir suppresses HCV while leaving HBV unchecked.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study monitoring HBV reactivation incidence, morbidity, and predisposing factors in HCV/HBV co-infected patients receiving direct anti-HCV DAA treatment; most directly relevant trial for HBV safety context |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large real-world safety study of DAA medications in HCV patients; likely captures HBV reactivation as an adverse event endpoint, providing broad safety signal data |
| [NCT02159352](https://clinicaltrials.gov/study/NCT02159352) | Phase 1 | Completed | 49 | Assessed pharmacokinetic effect of Darunavir/ritonavir or Lopinavir/ritonavir on daclatasvir exposure; informs dosing in HIV/HCV/HBV triple co-infection scenarios |
| [NCT02565888](https://clinicaltrials.gov/study/NCT02565888) | Phase 1 | Completed | 16 | Drug-drug interaction study of daclatasvir with Atazanavir/ritonavir or Atazanavir/cobicistat; relevant to antiretroviral co-administration in co-infected patients |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: ABT-493/ABT-530 vs. SOF+daclatasvir in HCV genotype 3 adults; large Phase 3 active-controlled HCV trial, primary endpoint SVR — no HBV data |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 adjunctive to daclatasvir ± ribavirin for HCV genotype 2/3; terminated early before completion — limited data, no HBV relevance |
| [NCT00874770](https://clinicaltrials.gov/study/NCT00874770) | Phase 2 | Completed | 74 | Phase 2a dose-finding study of daclatasvir + peginterferon alfa-2a + ribavirin for HCV genotype 1; foundational efficacy and safety data for the drug |
| [NCT02104843](https://clinicaltrials.gov/study/NCT02104843) | Phase 1 | Completed | 18 | PK interaction of daclatasvir/asunaprevir/BMS-791325 triple combination on rosuvastatin exposure; characterizes transporter/CYP interactions |
| [NCT00546715](https://clinicaltrials.gov/study/NCT00546715) | Phase 1/2 | Completed | 95 | First-in-human single ascending dose study of BMS-790052 (daclatasvir) in chronic HCV; established safety, tolerability, and antiviral activity profile |
| [NCT01830205](https://clinicaltrials.gov/study/NCT01830205) | Phase 1 | Completed | 58 | Single-dose daclatasvir pharmacokinetics in renal impairment; no HBV data, but informs dosing in patients with renal comorbidities common in chronic hepatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir therapy in Egyptian HCV patients and HCV/HBV co-infected patients; demonstrated high DAA efficacy with safety data in co-infected population |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | J Viral Hepat | Low HBV reactivation incidence in 25 HBV co-infected and 765 resolved-HBV patients during IFN-free DAA therapy (including asunaprevir + daclatasvir in 160 patients); quantified reactivation risk |
| [30833515](https://pubmed.ncbi.nlm.nih.gov/30833515/) | 2019 | Cohort | Antiviral Ther | HBV reactivation risk specifically in HBV/HCV co-infected patients on haemodialysis receiving DAA treatment; highlights need for monitoring in renal failure patients |
| [28555436](https://pubmed.ncbi.nlm.nih.gov/28555436/) | 2017 | Cohort | Indian J Gastroenterol | HBV infection linked to 43% HCC recurrence rate (10/23 patients) after DAA-mediated HCV eradication; suggests HBV contributes to oncological risk even after HCV clearance |
| [27329484](https://pubmed.ncbi.nlm.nih.gov/27329484/) | 2016 | Case Report | Clin J Gastroenterol | 83-year-old HCV patient developed acute hepatitis B after daclatasvir/asunaprevir therapy; raises HBV screening and prophylaxis imperative before initiating DAA therapy |
| [26297529](https://pubmed.ncbi.nlm.nih.gov/26297529/) | 2016 | Case Report | Hepatol Res | HBV DNA reactivation (increase) during interferon-free daclatasvir/asunaprevir in an HBV/HCV co-infected patient; confirms DAAs do not suppress HBV and may paradoxically allow HBV rebound |
| [36838792](https://pubmed.ncbi.nlm.nih.gov/36838792/) | 2023 | Computational | Molecules | Virtual screening identifies daclatasvir as a candidate binder of HBV pregenomic RNA ε stem-loop — the only study proposing direct anti-HBV activity; no cell or animal model validation |
| [40578045](https://pubmed.ncbi.nlm.nih.gov/40578045/) | 2025 | Implementation | Int J Drug Policy | Decentralized triple prevention/treatment model for HBV, HCV, and HIV in PWID in Pretoria, South Africa; daclatasvir used for HCV component in co-infected patients |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Comprehensive review of DAA agents targeting HCV NS3/4A, NS5B, and NS5A; explicitly distinguishes HCV (curable) from HBV (not curable by current DAAs) |
| [27311286](https://pubmed.ncbi.nlm.nih.gov/27311286/) | 2016 | Review | Rinsho Byori | Japanese review of viral hepatitis treatment advances; discusses IFN-free DAA efficacy for HCV and HBV reactivation as a recognized complication requiring prophylaxis |

---

## Philippines Market Information

Daclatasvir currently has **no registered products** with the FDA Philippines. The drug has not obtained market authorization, is not commercially available in the Philippines, and has no recorded licensing history in the regulatory database. Any clinical use would require special compassionate access or investigational new drug procedures.

---

## Safety Considerations

Please refer to the package insert for safety information, as detailed warnings and contraindications were not available in this Evidence Pack (Data Gap DG001).

Based on the available literature, the following safety concern is specifically relevant to the predicted indication:

- **HBV Reactivation Risk**: Multiple case reports (PMID 26297529, 27329484) and cohort studies (PMID 29194858, 30833515) document HBV DNA reactivation in HBV/HCV co-infected patients receiving daclatasvir-based HCV treatment. All patients receiving daclatasvir should be screened for HBV surface antigen (HBsAg) and core antibody (anti-HBc) prior to initiating therapy. HBsAg-positive patients may require prophylactic antiviral therapy (e.g., entecavir or tenofovir) to prevent reactivation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Daclatasvir's established mechanism — HCV NS5A inhibition — has no direct biological counterpart in HBV, which lacks an NS5A homologue. The available evidence identifies HBV reactivation as a safety risk during daclatasvir therapy rather than as a therapeutic target. The sole computational hypothesis (virtual HBV pgRNA docking) requires experimental validation before any translational consideration is warranted.

**To proceed, the following is needed:**

- **Primary validation step**: In vitro anti-HBV activity assay (HepG2.2.15 cells or covalently closed circular DNA [cccDNA] model) to determine whether daclatasvir has any measurable effect on HBV replication endpoints (HBsAg, HBeAg, HBV DNA, cccDNA)
- **Mechanism clarification**: Obtain full DrugBank mechanism of action data (Data Gap DG002) and confirm whether any off-target RNA-binding activity could plausibly inhibit HBV pgRNA
- **Safety baseline**: Retrieve TFDA package insert warnings and contraindications (Data Gap DG001) to enable S1 safety screening before any repurposing pathway is opened
- **Animal model confirmation**: Replicate the computational pgRNA-binding hypothesis in a validated HBV animal model (e.g., HBV-infected humanized liver mice or AAV-HBV mouse model) before any human study is considered
- **Regulatory pathway scoping**: Given zero Philippines registrations, a full regulatory strategy including an IND equivalent filing would be required before any local clinical investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

