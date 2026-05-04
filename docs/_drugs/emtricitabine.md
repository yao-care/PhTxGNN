---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) and a cornerstone of combination antiretroviral therapy (cART) for human HIV infection globally. The TxGNN model's top prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, with only **1 veterinary study** directly supporting this direction; the 4 retrieved clinical trials are all human HIV-1 trials that were incorrectly mapped and carry no direct relevance to FIV. This candidate is currently rated **L4 (animal/preclinical evidence only)** and carries a **Hold** recommendation pending species-specific data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (NRTI component of combination antiretroviral therapy) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, emtricitabine (FTC) is a synthetic fluorinated cytidine analogue. After intracellular phosphorylation to its active triphosphate form (FTC-TP), it acts as a competitive inhibitor of viral reverse transcriptase (RT) and causes premature termination of the growing viral DNA chain — halting viral replication at a critical enzymatic step. Its efficacy against HIV-1, HIV-2, and hepatitis B has been validated across decades of clinical use.

Feline Immunodeficiency Virus (FIV) and HIV are both members of the genus *Lentivirus* within family *Retroviridae*, and both cause progressive CD4⁺ T-cell depletion and immune failure. Like HIV, FIV is absolutely dependent on its reverse transcriptase for replication, which is why NRTI-based therapy is mechanistically applicable in principle. The 2023 study by Kim et al. directly tested a cART regimen including emtricitabine (40 mg/kg) in FIV-infected domestic cats, providing the first in vivo proof-of-concept in the target species.

That said, meaningful caveats remain: the RT amino acid sequences of FIV and HIV differ at key positions, potentially affecting drug-binding affinity. Pharmacokinetics in cats diverge substantially from humans — feline metabolism, renal handling, and volume of distribution must be independently characterized before any efficacy claim can be made. This prediction is mechanistically coherent but empirically immature.

---

## Clinical Trial Evidence

> ⚠️ **Mapping Alert**: All 4 trials below are human HIV-1 clinical trials. They contain emtricitabine as part of a combination regimen but were retrieved because the search engine matched on "emtricitabine + HIV" keywords rather than FIV-specific evidence. **None are designed for or applicable to Feline Acquired Immunodeficiency Syndrome.** They are listed solely for transparency and should carry zero evidentiary weight for this indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs Efavirenz/FTC/TDF (Atripla) in ART-naïve HIV-1 adults over 96 weeks — **human HIV-1 trial, not FIV-relevant** |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + 3TC vs darunavir + FTC/TDF in naïve HIV-1 patients — **human HIV-1 trial, not FIV-relevant** |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs Raltegravir with dual NRTI backbone (ABC/3TC or TDF/FTC) in HIV-1 naïve adults over 96 weeks — **human HIV-1 trial, not FIV-relevant** |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Once-daily dolutegravir dose-selection study with ABC/3TC or TDF/FTC in HIV-1 naïve adults — **human HIV-1 trial, not FIV-relevant** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal / Veterinary Study | *Viruses* | Evaluated pharmacokinetics and clinical outcomes of cART (**Dolutegravir 2.5 mg/kg + Tenofovir 20 mg/kg + Emtricitabine 40 mg/kg**) in FIV-infected domestic cats; assessed changes in CD4⁺/CD8⁺ T-cell immunophenotype — the only direct in vivo evidence for FTC use in FIV to date |

---

## Philippines Market Information

Emtricitabine is currently **not registered** in the Philippines. No product license or authorization records are available from the FDA Philippines database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one veterinary animal study directly supports this indication, and all 4 clinical trials retrieved were incorrectly mapped human HIV-1 studies with no bearing on FIV; the evidence base is insufficient to support any clinical, regulatory, or commercial action at this stage. Furthermore, this is a **veterinary indication** (domestic cats), which falls outside the scope of human medicine and the Philippines FDA's human drug registration pathway.

**To proceed, the following is needed:**

- **Species-specific studies**: Formal feline pharmacokinetic and pharmacodynamic studies to establish safe and effective FTC dosing in cats
- **Controlled veterinary trials**: Randomized controlled trials in FIV-infected cats with defined efficacy endpoints (viral load, CD4⁺ count, clinical progression)
- **MOA confirmation**: Retrieve emtricitabine mechanism of action data from DrugBank (DB00879) to document FIV RT binding affinity vs. HIV RT
- **Safety data**: Drug interactions and toxicity monitoring parameters specific to the feline species
- **Regulatory scoping**: If veterinary use is the intended pathway, engage the Bureau of Animal Industry (BAI) of the Philippines rather than FDA Philippines

> 📌 **Note on Other Predicted Indications**: The TxGNN model also predicted **Simian Immunodeficiency Virus (SIV) infection** at rank 2 (score 99.92%, L3 evidence, 20 primate publications including multiple Tier 1 macaque challenge studies directly using FTC/TDF regimens — a "Research Question" recommendation). This represents the stronger preclinical evidence base, as the SHIV macaque model is an FDA-recognized platform for HIV PrEP development and mechanistically translates more directly to human clinical research. A rank 3 prediction for a neurodevelopmental disorder (L5, no evidence) is currently speculative and does not warrant further evaluation.

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

