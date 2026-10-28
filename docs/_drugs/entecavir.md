---
layout: default
title: Entecavir
parent: Model Prediction Only (L5)
nav_order: 125
evidence_level: L5
indication_count: 9
monitor_inn: "Entecavir"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
last_modified_at: 2026-10-28
description: "Entecavir: predicted new indication chronic hepatitis C virus infection (evidence level L5). Approved use: Not recorded in the local data"
---

# Entecavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Entecavir: nucleoside analogue (HBV polymerase inhibitor) → chronic hepatitis C virus infection
{: .text-alpha }

## One-Sentence Summary

Entecavir is a guanosine nucleoside analogue that inhibits hepatitis B virus (HBV) polymerase.
The TxGNN model predicts it may be relevant to **chronic hepatitis C virus infection**, with a score of **0.9998**.
The data compiled for this report include **2 clinical trials** and **20 publications**, but none shows entecavir treating hepatitis C itself; they concern HBV in people co-infected with HCV.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | chronic hepatitis C virus infection |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Entecavir is known to act on HBV polymerase, a DNA-virus enzyme.

Hepatitis C virus is an RNA virus that replicates with the NS5B RNA-dependent RNA polymerase. Entecavir has no known direct activity against it. The only link is indirect: in patients infected with both viruses, entecavir suppresses HBV and can prevent HBV reactivation during or after HCV direct-acting antiviral (DAA) therapy. That benefit is for HBV, not for clearing HCV.

The high model score probably reflects the two infections being closely associated in the literature, not a demonstrated antiviral effect on HCV.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAA treatment of HCV/HBV co-infection; studies HBV reactivation during anti-HCV therapy. Does not test entecavir against HCV. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Randomized trial of nucleos(t)ide analogue prophylaxis (12 vs 24 weeks) to prevent HBV reactivation in HCV/HBV co-infected patients on DAAs. HBV-directed. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Randomized trial | Clin Gastroenterol Hepatol | Entecavir prevents HBV reactivation during DAA treatment of HCV/HBV dual infection. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation and viral load in anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide analogues. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV co-infection. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and prospects for chronic hepatitis B and C. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Not classified | Clin Res Hepatol Gastroenterol | Management of viral hepatitis B and C in children. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | HBV reactivation risk during DAA therapy in HCV patients with HBV infection. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Not classified | Dig Dis | Incidence and course of HBV reactivation in patients treated with DAAs for HCV. |

## Philippines Market Information

The Philippines records list one registration for entecavir (PNF-0166), and the local data do not record an approved indication, dosage form or manufacturer for it.

## Safety Considerations

- **Drug Interactions**: 44 interactions were found. The ones listed are all of Moderate level, including famotidine, ranitidine, cimetidine, metformin, amphotericin B products, vancomycin, kanamycin, neomycin, polymyxin B, levofloxacin, amoxicillin, mesalazine, sulfasalazine, balsalazide, olsalazine and orlistat.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The cited studies address HBV in patients also infected with HCV, not HCV treatment with entecavir, and entecavir has no known anti-HCV mechanism. No study directly examines the predicted disease as a treatment target, so the evidence level is L5. Effective DAA therapy already exists for HCV.

**To proceed, the following is needed:**
- Laboratory or clinical evidence of anti-HCV activity, otherwise the prediction should not be pursued
- Mechanism of action data
- Package insert warnings and contraindications from the Philippines FDA
- If the co-infection setting is the interest, a separate question on HBV reactivation prophylaxis during DAA therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

