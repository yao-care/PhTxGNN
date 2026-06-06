---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is an HIV-1 aspartyl protease inhibitor, originally developed for the treatment of HIV/AIDS in humans and widely used as a pharmacokinetic booster in combination antiretroviral regimens.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**,
with **1 indirectly related clinical trial** (a human HIV-1 study) and **no direct literature** supporting this veterinary indication — the mechanistic rationale rests entirely on structural homology between HIV and FIV proteases.
Two additional predictions were generated: simian immunodeficiency virus infection (L3, 12 publications) and a rare neurodevelopmental disorder (L5, no evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral therapy / pharmacokinetic booster) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ritonavir is a potent inhibitor of the HIV-1 aspartyl protease, an enzyme essential for cleaving polyprotein precursors into functional structural proteins and enzymes during viral maturation. Without active protease, only immature, non-infectious virions are produced. At sub-therapeutic antiviral doses, Ritonavir also strongly inhibits CYP3A4/2D6, making it the most widely used pharmacokinetic "booster" in HAART regimens to elevate plasma concentrations of co-administered protease inhibitors (e.g., lopinavir/r, darunavir/r).

Feline immunodeficiency virus (FIV) belongs to the same *Retroviridae* family as HIV-1 and is classified as a lentivirus. FIV protease shares active-site structural homology with HIV-1 protease, and in vitro data (see literature for the SIV indication, which is closely analogous) confirm that several HIV protease inhibitors retain measurable inhibitory activity against related lentiviral proteases. This phylogenetic and structural similarity is the biological foundation of the TxGNN model's prediction.

However, the substrate-binding pocket of FIV protease differs from HIV-1 in clinically important ways, reducing potency of most HIV PIs in feline systems. The only trial surfaced in this evidence pack (NCT02770508) is a human HIV-1 pharmacokinetic booster study in which Ritonavir plays no primary antiviral role. No veterinary clinical or preclinical studies in cats were identified, meaning the mechanistic link has not been clinically validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Ritonavir-boosted darunavir + lamivudine vs. standard HAART in ARV-naïve HIV-1 patients. Ritonavir functions as a PK booster only, not as a primary antiviral agent. **Relevance to feline AIDS is indirect**: association is based solely on HIV/FIV lentiviral mechanistic analogy, not on veterinary evidence. |

> No clinical trials in cats or other veterinary subjects were identified for this indication.

---

## Literature Evidence

Currently no related literature available for Ritonavir in feline acquired immunodeficiency syndrome.

---

## Philippines Market Information

Ritonavir is currently **not registered** with the Philippine FDA. No product authorizations were identified in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base consists of a single human HIV-1 pharmacokinetic trial with only indirect mechanistic relevance; there is no veterinary clinical or preclinical study in cats, no literature, and Ritonavir is not approved or marketed in the Philippines. The prediction is biologically plausible but remains entirely unvalidated at the species level.

**To proceed, the following is needed:**

- **In vitro FIV protease inhibition assay** using Ritonavir at clinically achievable feline plasma concentrations to confirm target engagement
- **Feline pharmacokinetic studies** — oral bioavailability, half-life, and CYP interaction profile differ substantially between humans and cats; cats lack functional CYP2D6 analogs and may be uniquely susceptible to CYP3A4-mediated drug interactions
- **Safety characterisation in cats** — Ritonavir's known hepatotoxicity and GI adverse effect profile in humans requires species-specific re-evaluation before any feline use
- **Literature review of lopinavir/ritonavir in FIV** — a small body of veterinary research has examined LPV/r in FIV-infected cats; retrieving and appraising this evidence would meaningfully refine the L4 rating
- **Regulatory pathway scoping** — Philippines veterinary drug approval falls under the Bureau of Animal Industry (BAI); a separate regulatory strategy from human drug registration applies
- **MOA data retrieval** (DrugBank API) and **Philippine FDA package insert** (TFDA/local PI equivalent) to resolve the two data gaps flagged in this pack (DG001, DG002) before progressing to formal safety screening (S1)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

