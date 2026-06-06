---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
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

# Sofosbuvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide analogue inhibitor of the HCV NS5B RNA-dependent RNA polymerase (RdRp), widely approved globally as the backbone of direct-acting antiviral (DAA) regimens for chronic hepatitis C virus (HCV) treatment.
The TxGNN model predicts it may show activity against **Hepatitis B Virus (HBV) infection** with a prediction score of **99.77%**.
Currently, **1 completed Phase 2 pilot trial** (NCT03312023, n=21) and **multiple observational cohort studies** provide exploratory clinical evidence, though the mechanistic basis remains limited due to fundamental differences in HBV and HCV replication biology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (globally approved; no Philippines registration on file) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sofosbuvir is a prodrug metabolized intracellularly to its active triphosphate form (GS-461203), which acts as a non-obligate chain terminator of the HCV NS5B RNA-dependent RNA polymerase. This mechanism underpins its highly effective cure rates (>95%) across all HCV genotypes when used in combination regimens such as sofosbuvir/velpatasvir.

Hepatitis B virus, however, replicates via a fundamentally different pathway: HBV uses a reverse transcriptase (RT/DNA polymerase) encoded by the viral *pol* gene to convert pregenomic RNA (pgRNA) into viral DNA. Because Sofosbuvir targets an RdRp structurally distinct from HBV's reverse transcriptase, direct mechanistic overlap is weak. That said, the pgRNA intermediate in the HBV replication cycle represents a theoretical window in which an RdRp-type inhibitor could theoretically interfere — a hypothesis that motivated direct clinical testing.

The most scientifically compelling evidence comes from retrospective observations in HCV/HBV co-infected patients treated with ledipasvir/sofosbuvir, where modest reductions in hepatitis B surface antigen (HBsAg) were noted alongside HCV clearance. This signal prompted a formal Phase 2 pilot study (NCT03312023, PMID 36045503) directly testing ledipasvir/sofosbuvir in HBV monoinfected individuals, providing the only direct clinical dataset. Results showed some HBsAg reduction but fell short of functional cure endpoints. The TxGNN model's high prediction score likely reflects the close disease-network proximity between HCV and HBV (shared hepatotropic biology, frequent co-infection, overlapping clinical management) rather than confirmed pharmacological activity against HBV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Only direct pilot study of ledipasvir/sofosbuvir in HBV monoinfected patients; primary endpoints were HBsAg and HBV DNA decline at Week 12 from baseline; results published as PMID 36045503 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study on incidence, morbidity, and predisposing factors for HBV reactivation during DAA treatment in HCV/HBV co-infected patients; monitored HBV dynamics during Sofosbuvir-based HCV therapy |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL combined with prophylactic TAF for treatment-naïve HCV/HBV co-infected adults in China; evaluates whether prophylactic HBV antiviral coverage prevents HBV reactivation during Sofosbuvir-based HCV treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 Open Label | Journal of Medical Virology | Ledipasvir/sofosbuvir for 12 weeks in HBV monoinfected subjects; retrospective data suggested modest HBsAg reduction in HBV/HCV co-infected patients treated with LDV/SOF, leading to this prospective HBV monoinfection pilot; demonstrated some HBsAg decline but functional cure was not achieved |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort | Clinical Infectious Diseases | LDV/SOF for HCV/HBV co-infected patients in Taiwan with 108-week post-treatment follow-up; documented HBV reactivation patterns, timing, and clinical management during and after Sofosbuvir-based HCV therapy |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Transactions of the Royal Society of Tropical Medicine and Hygiene | SOF/daclatasvir-based therapy for chronic HCV and HCV/HBV co-infected patients in Egypt; tracked HBV status changes and safety outcomes alongside HCV SVR |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case Series | Medicine | HBV reactivation following successful HCV clearance with sofosbuvir + ribavirin; highlights clinically important immunological mechanism whereby HCV clearance releases suppression of HBV, resulting in HBV rebound — a safety signal rather than a therapeutic effect |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV/HBV co-infected patients with pretreatment HBeAg seroconversion; examines role of HBV antiviral therapy in reactivation episodes following Sofosbuvir-based HCV clearance |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | Journal of Clinical Gastroenterology | Risk of HBV reactivation in HBsAg-positive and anti-HBc-positive patients treated with ledipasvir-sofosbuvir for HCV; found clinically meaningful HBV reactivation rate in HBsAg-positive patients, informing screening and prophylaxis guidelines |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatrica | Review of chronic HBV and HCV treatment in children; contextualizes the evolving antiviral landscape and the burden of both infections in pediatric populations |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Antiviral medications for HBV and HCV treatment and their effects on renal function; compares available agents across both virus classes, relevant to safety profiling of Sofosbuvir in the HBV treatment context |

---

## Philippines Market Information

Sofosbuvir is not currently registered with the FDA Philippines. No product authorizations are on record. This drug is available and widely used in many other markets (United States, European Union, Taiwan, Japan, etc.) under brand names including Sovaldi® and Epclusa® (in combination with velpatasvir), but no Philippines-specific regulatory filings have been captured in this data cutoff.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Notable signal for this indication:** Multiple published studies have documented **HBV reactivation** as a clinically important consequence of Sofosbuvir-based HCV treatment in patients with HBV co-infection or occult HBV. This is a paradoxical safety concern — HCV suppression may unmask latent HBV — and is not evidence of therapeutic activity against HBV. Any investigation of Sofosbuvir as an HBV treatment would need to carefully distinguish between direct antiviral activity and reactivation-related phenomena.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Sofosbuvir against HBV is fundamentally weak — HBV relies on reverse transcriptase rather than RdRp — and the only direct clinical evidence (NCT03312023, n=21) demonstrated only modest HBsAg reduction without achieving functional cure. The TxGNN's high prediction score most likely reflects shared hepatotropic disease biology and frequent HCV/HBV co-infection patterns rather than true pharmacological repurposing potential. Given that the Philippines has no existing registration for this drug and safety data are unavailable locally, further regulatory and evidence work is needed before any advancement.

**To proceed, the following is needed:**

- **Full results analysis** of NCT03312023, including HBsAg seroconversion rates, HBV DNA kinetics, and long-term durability data
- **Mechanistic in vitro studies** confirming whether Sofosbuvir triphosphate (GS-461203) can inhibit HBV pgRNA-directed reverse transcription at clinically achievable intrahepatic concentrations
- **MOA data retrieval** for Sofosbuvir (currently flagged as Data Gap DG002; DrugBank query required)
- **Safety package insert data** acquisition from TFDA or global regulatory sources (Data Gap DG001, severity: Blocking)
- **Drug-drug interaction (DDI) assessment** for combination with established HBV antivirals (tenofovir alafenamide, entecavir) if a combination strategy is being considered
- **Philippines FDA registration pathway analysis** for Sofosbuvir as a prerequisite for any local clinical development or compassionate use program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

