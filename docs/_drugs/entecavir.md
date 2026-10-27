---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 125
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L3). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Entecavir"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
---

# Entecavir
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Entecavir: From Chronic Hepatitis B Virus Infection to Chronic Hepatitis C Virus Infection
{: .text-alpha }

## One-Sentence Summary

Entecavir is a nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection**, with **2 clinical trials** and **20 publications** linked to this prediction.
However, this evidence concerns HBV control in patients co-infected with HBV and HCV, not clearance of HCV itself, so the prediction is weakly supported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entecavir is a guanosine nucleoside analogue. It is converted inside cells to its active triphosphate form, which blocks HBV polymerase (priming, reverse transcription and DNA synthesis). Its efficacy in chronic hepatitis B is well established.

HCV is an RNA virus that replicates through a different enzyme, NS5B RNA-dependent RNA polymerase. Entecavir has no known direct activity against it. The two diseases are linked mainly through co-infection. Patients with both HBV and HCV can have their HBV reactivate when they receive direct-acting antivirals (DAAs) for HCV. Entecavir suppresses HBV in that setting, which benefits the HBV side only.

The high model score most likely reflects shared "viral hepatitis" and nucleoside-analogue patterns in the knowledge graph, not a real anti-HCV mechanism. The prediction should be read as a research question, not as evidence of anti-HCV efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAA treatment in HCV/HBV co-infected patients. It studied HBV reactivation during anti-HCV therapy and did not test entecavir as an HCV treatment. The sample is small. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Randomised, open-label, three-arm trial of prophylactic nucleos(t)ide analogue (12 vs 24 weeks) to prevent HBV reactivation during DAA therapy for HCV. It addresses HBV protection, not HCV activity. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | RCT | Clin Gastroenterol Hepatol | Entecavir prevented HBV reactivation during DAA treatment of HCV/HBV dual infection. The benefit is for HBV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV co-infection. These patients are at high risk of cirrhosis and hepatocellular carcinoma. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for hepatitis B and C, including entecavir, and their effects on kidney function. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation and viral load in 66 anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide analogue therapy. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | Risk of HBV reactivation in chronic hepatitis C patients with HBV infection treated with DAAs. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Not classified | Dig Dis | Incidence and clinical course of HBV reactivation in patients treated with DAAs for HCV. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Not classified | World J Hepatol | Management of hepatitis B and C around liver and kidney transplantation. Entecavir and tenofovir improved outcomes in HBV decompensated cirrhosis. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Not classified | Biomedicines | Therapy of chronic viral hepatitis. Nucleos(t)ide analogues have had a major impact on HBV-related liver disease. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Not classified | Clin Res Hepatol Gastroenterol | Management of hepatitis B and C in children. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Not classified | Wien Med Wochenschr | Treatment overview for chronic hepatitis B and C, covering interferon and lamivudine. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0166 (cancelled) | Entecavir | Not recorded | Not recorded |

There is no currently valid single-ingredient or combination registration. Dosage form and approved indication text are not available for the one cancelled registration.

---

## Safety Considerations

- **Contraindications / disease associations (from the TxGNN knowledge graph, not from label text)**: impaired renal function, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis.
- **Drug Interactions**: 44 interactions were identified, all of the sample listed being Moderate level. Main examples:
  - Nephrotoxic or renally cleared drugs: amphotericin B (including lipid, liposomal and cholesteryl sulfate forms), vancomycin, kanamycin, neomycin, polymyxin B.
  - Acid-suppressing H2 blockers: famotidine, ranitidine, cimetidine.
  - Other: metformin, levofloxacin, amoxicillin, orlistat, and the aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine).

For warnings and other safety details, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Entecavir has no known direct anti-HCV activity. The related trials and publications show only that it prevents HBV reactivation in HCV/HBV co-infected patients receiving DAAs, which is a benefit for HBV, not HCV.
- Effective DAAs already exist for HCV, and the product has no valid Philippines registration at present.
- The high model score is not supported by a mechanism or by HCV efficacy data.

**To proceed, the following is needed:**
- In vitro or preclinical data showing any anti-HCV activity of entecavir.
- Detailed mechanism of action data.
- If the co-infection setting is the real interest, reframe the question as "HBV reactivation prophylaxis during HCV DAA therapy" and assess it against the existing on-label HBV indication.
- Package insert warnings and contraindications, and the current regulatory status of any entecavir product in the Philippines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

