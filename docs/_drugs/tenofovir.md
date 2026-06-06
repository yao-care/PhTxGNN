---
layout: default
title: Tenofovir
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 3
---

# Tenofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tenofovir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir is a nucleotide reverse transcriptase inhibitor (NtRTI) with established use in treating HIV infection and chronic hepatitis B in humans, though it carries no current Philippines regulatory registration.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**, supported by **2 direct animal studies** — including one that administered PMPA (the free-acid parent compound of Tenofovir) to naturally FIV-infected cats.
Mechanistic plausibility is strong given the shared lentiviral reverse transcriptase biology between FIV and HIV-1, but this application sits entirely within the veterinary domain with limited translational pathway to human medicine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV Infection / Chronic Hepatitis B (no Philippines registration on record) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on established pharmacology, Tenofovir (as its free-acid form, PMPA — 9-[2-(R)-(phosphonomethoxy)propyl]adenine) is a nucleotide analogue that competitively inhibits reverse transcriptase, the enzyme retroviruses use to convert viral RNA into DNA. By mimicking the natural substrate and incorporating into the growing DNA chain, Tenofovir causes chain termination, blocking viral genome integration and replication.

Feline Immunodeficiency Virus (FIV), the causative agent of feline AIDS, is a lentivirus with high structural and mechanistic homology to HIV-1. Both viruses rely on an RNA-dependent DNA polymerase (reverse transcriptase) during replication, making nucleotide reverse transcriptase inhibitors such as Tenofovir pharmacologically applicable across both host species. PMID 24782459 directly tested PMPA in six naturally FIV-infected cats, providing in vivo validation of this cross-species mechanistic link.

The prediction is further consistent with the broader antiretroviral pharmacology literature: Tenofovir and its prodrugs (TDF, TAF) have been extensively validated in non-human primate models of SIV and SHIV infection (the next-ranked TxGNN prediction), confirming the drug's activity is conserved across primate lentiviruses. However, it is critical to note that this is a **veterinary** application — pharmacokinetics, dosing requirements, and the safety profile in domestic cats may differ substantially from human data.

---

## Clinical Trial Evidence

No clinical trials directly evaluating Tenofovir for feline acquired immunodeficiency syndrome (FIV) are currently registered on ClinicalTrials.gov. The four trials retrieved by the evidence pipeline target **human HIV-1**, with Tenofovir serving as a backbone agent in combination regimens; they are not applicable to this veterinary indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs. Atripla (TDF/FTC/EFV) in HIV-1 treatment-naïve adults over 96 weeks; Tenofovir present only in the comparator arm |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. TDF/FTC or TDF/3TC in HIV-1 naïve patients; human indication only |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. Raltegravir, both administered with TDF/FTC or ABC/3TC backbone, in HIV-1 naïve adults over 96 weeks |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-ranging study of Dolutegravir co-administered with ABC/3TC or TDF/FTC in HIV-1 treatment-naïve adults |

> **Note:** All four retrieved trials address human HIV-1 and do not directly support the FIV repurposing hypothesis. They confirm Tenofovir's safety and tolerability in human antiretroviral backbone regimens, which may inform safety expectations in feline use, but this is indirect at best.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Animal Study (In Vivo, Feline) | J Feline Med Surg | PMPA (free-acid Tenofovir) administered to 6 naturally FIV-infected cats; reported direct antiviral activity against FIV in vivo with concurrent assessment of tolerability and adverse effects — the most directly relevant study for this indication |
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal Study (In Vivo, Feline) | Viruses | Combination cART (Dolutegravir 2.5 mg/kg + Tenofovir 20 mg/kg + Emtricitabine 40 mg/kg) evaluated in FIV-infected domestic cats; assessed pharmacokinetics, CD4/CD8 immunophenotype, and clinical outcomes — demonstrates contemporary multi-drug ART use in FIV model |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Tenofovir has solid mechanistic plausibility for FIV treatment — both viruses share lentiviral reverse transcriptase biology, and two direct feline animal studies confirm in vivo activity. However, this is a **veterinary** application with no established pathway to human clinical use in the Philippines, no Philippines regulatory registration exists, no safety data is available in the current evidence pack, and the clinical trial evidence retrieved is entirely from human HIV studies with no cross-over to FIV.

**To proceed, the following is needed:**

- Clarify the intended use context: veterinary (feline AIDS treatment) or human medicine repurposing — these require entirely different regulatory and development pathways
- Obtain feline-specific pharmacokinetic data (oral bioavailability, renal clearance, and appropriate dosing in cats; human-derived dosing cannot be directly extrapolated)
- Assess feline-specific safety risks: renal tubular toxicity and decreased bone mineral density are known Tenofovir adverse effects in humans and should be characterized in cats
- Retrieve formal MOA documentation from DrugBank (DB14126) to populate the mechanism of action gap
- Determine Philippines regulatory pathway: if veterinary, consult the Bureau of Animal Industry (BAI); if human repurposing is the intent, note that the top TxGNN prediction is for a non-human disease and reconsider whether the second-ranked indication (simian immunodeficiency virus model — an established HIV PrEP research platform) better supports a translational development strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

