---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Hepatitis B Infection to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir (ETV) is a potent guanosine nucleoside analogue approved globally for chronic hepatitis B virus (HBV) infection, acting as a selective inhibitor of HBV DNA polymerase.
The TxGNN model predicts it may be effective for **Chronic Hepatitis C Virus Infection** with a score of **99.98%**;
however, of the retrieved evidence — 10 clinical trials and 20 publications — none directly study ETV in HCV treatment, and mechanistic analysis identifies this prediction as a knowledge-graph false positive driven by shared liver-disease nodes between HBV and HCV rather than any real pharmacological basis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis B (HBV) infection (globally approved; not registered in Philippines) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Entecavir is a cyclopentyl guanosine analogue that, after intracellular phosphorylation to its active triphosphate form, inhibits HBV DNA polymerase through three sequential steps: blocking viral DNA priming, reverse transcription of pre-genomic RNA to DNA, and synthesis of positive-strand HBV DNA. This triple inhibition gives ETV one of the highest genetic barriers to resistance among anti-HBV nucleoside analogues (resistance rate <1.2% at five years in treatment-naïve patients), making it a globally recommended first-line therapy for chronic HBV.

The TxGNN model's association of ETV with HCV most likely arises from knowledge-graph topology rather than pharmacology. HBV and HCV share multiple overlapping disease nodes in the graph — both cause chronic hepatitis, liver cirrhosis, hepatocellular carcinoma, and they frequently co-infect the same patients — creating indirect algorithmic pathways that the model interprets as a drug-disease association and assigns a high confidence score of 99.98%.

In reality, the mechanistic basis for this prediction does not hold. Hepatitis C virus is an RNA virus that replicates exclusively through its NS5B RNA-dependent RNA polymerase (RdRp) — an enzyme that is structurally and functionally unrelated to the HBV DNA polymerase targeted by ETV. No published data demonstrates any anti-HCV activity for ETV at clinically relevant concentrations. More critically, a 2022 cohort study (PMID 36146665) shows that anti-HBV nucleoside analogue therapy — including ETV-containing regimens — can actually *trigger HCV reactivation* in co-infected patients by removing HCV from viral interference suppression. This is a direct negative signal against the prediction. Furthermore, with modern direct-acting antivirals (DAAs) now curing HCV in over 95% of patients, there is no treatment gap in this indication for ETV to address.

---

## Clinical Trial Evidence

> ⚠️ **Important**: None of the retrieved trials directly study Entecavir for HCV treatment. All trials below target HBV infection or use ETV as a background/comparator agent. They are presented as retrieved evidence but do **not** support repurposing Entecavir for chronic HCV.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|------|---------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA therapy for HCV in HBV/HCV co-infected patients; monitors HBV reactivation during HCV treatment. ETV used to manage HBV, not as the HCV treatment |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | 3-arm RCT evaluating whether prophylactic nucleoside analogues (NUC) can prevent HBV reactivation in HCV/HBV co-infected patients receiving DAA therapy for chronic HCV; ETV role is HBV prophylaxis only |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Randomized study of Arabinoxylan rice bran (MGN-3/Biobran) for HCC and hepatitis B and C infection; ETV is not the primary investigational agent |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Double-blind RCT evaluating TQA3810 tablets combined or uncombined with nucleoside analogues in HBV patients; indication is HBV, not HCV |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Prospective ETV trial in HBV-related HCC patients after radiofrequency ablation; not an HCV study |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys+ETV vs ETV alone in HBeAg-positive chronic HBV; references HCV/HIV treatment concepts as background rationale but exclusively targets HBV |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Drug-drug interaction study of Morphothiadine Mesilate/Ritonavir combined with ETV or TDF in healthy subjects; pharmacokinetics only, not a therapeutic efficacy trial |
| [NCT05484466](https://clinicaltrials.gov/study/NCT05484466) | Phase 2 | Unknown | 90 | ZM-H1505R+ETV vs ETV monotherapy in CHB patients on long-term ETV; exclusively an HBV study |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Phase 3 RCT comparing ETV vs adefovir for early viral-load reduction in nucleoside-naïve HBV adults; not an HCV trial |
| [NCT05423106](https://clinicaltrials.gov/study/NCT05423106) | Phase 1 | Terminated | 60 | First-in-human study of JNJ-64457744 in healthy volunteers and HBV patients; terminated early; not an ETV–HCV efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | **Negative signal**: HCV reactivation observed in anti-HCV antibody-positive CHB patients after nucleoside analogue therapy (including ETV); ETV treatment of HBV may paradoxically promote, not suppress, HCV replication |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica | Comparative review of antivirals for HBV and HCV and their renal effects; ETV discussed exclusively as an HBV agent with no anti-HCV activity mentioned |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | HBV/HCV coinfection treatment; ETV manages the HBV component while DAAs address HCV — mechanisms are entirely separate |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics in Research in Hepatology | HBV/HCV dual infection as a therapeutic challenge; ETV used for the HBV component of co-infection, separate agents required for HCV |
| [28538267](https://pubmed.ncbi.nlm.nih.gov/28538267/) | 2017 | Cohort | European Journal of Gastroenterology & Hepatology | Cirrhosis does not impair ETV efficacy in CHB; uses HCV cohort data for contextual comparison only — no ETV-HCV treatment data |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | Historical review of HBV and HCV treatment options; ETV presented only as an HBV agent |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clinics in Research in Hepatology | Pediatric management of viral hepatitis B and C; ETV approved for HBV in children, entirely separate agents used for HCV |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World Journal of Hepatology | HBV and HCV management before and after liver/kidney transplantation; ETV used for HBV prophylaxis, distinct treatment pathway for HCV |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World Journal of Gastroenterology | HBV and alcoholic liver disease expected to become leading HCC causes in the post-DAA era; ETV discussed for HBV only |
| [39351520](https://pubmed.ncbi.nlm.nih.gov/39351520/) | 2024 | Review | World Journal of Hepatology | Metabolomics as an emerging diagnostic tool in liver disease; ETV referenced in HBV context with no pharmacological connection to HCV |

---

## Philippines Market Information

Entecavir currently has **no registered products with the Philippines FDA**. The drug is not marketed in the Philippines and carries no local authorization numbers. Any clinical use in the Philippines would require a full regulatory submission to the Philippines FDA (Food and Drug Administration).

For reference, the drug is commercially available internationally under brand names including Baraclude® (Bristol-Myers Squibb) and numerous generic formulations, all approved for chronic hepatitis B treatment.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Critical co-infection warning (from the Evidence Pack mechanistic analysis):** Entecavir must not be used as the sole antiviral agent in HIV/HBV co-infected patients who are not on fully suppressive antiretroviral therapy. ETV monotherapy in HIV-positive individuals can select for the M184V/I resistance mutation in HIV reverse transcriptase, permanently compromising the efficacy of lamivudine and emtricitabine in future antiretroviral regimens. Patients with HIV/HBV co-infection must receive a complete antiretroviral regimen before ETV is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction is a knowledge-graph false positive. Entecavir targets HBV DNA polymerase and has no pharmacological mechanism to inhibit HCV NS5B RNA-dependent RNA polymerase. Published cohort data (PMID 36146665) demonstrate the opposite effect — ETV-based HBV suppression can promote HCV reactivation in co-infected patients. With DAA regimens already curing HCV in over 95% of cases, there is no clinical or scientific basis to pursue ETV for this indication.

**Contextual observations from the full TxGNN prediction ranking:**

| Rank | Indication | Evidence Level | Recommendation | Note |
|------|----------|---------|---------|------|
| 2 | Hepatitis B virus infection | L1 | Proceed with Guardrails | ETV's globally approved indication; the Philippines non-registration is an **access gap**, not a repurposing question |
| 3 | HIV infectious disease | L3 | Hold | ETV has demonstrated partial HIV-1 reverse transcriptase inhibition in small clinical studies (PMID 17582071; PMID 18453854), but cannot be used as standalone HIV therapy due to M184V resistance risk |

**To proceed with the HBV Philippines market access opportunity, the following is needed:**
- Prepare and submit a Philippines FDA registration dossier for Entecavir (tablet formulation)
- Obtain official package insert with translations; ensure HIV co-infection warning and CKD dose-adjustment guidance are clearly communicated
- Engage local hepatology and infectious disease societies to align treatment guidelines with WHO and regional HBV prevalence data
- Establish pharmacovigilance protocols for long-term HBV suppression, with particular attention to renal function monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

