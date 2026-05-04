---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir (ABC) is a nucleoside reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral therapy for HIV-1 infection in humans.
The TxGNN model predicts it may be effective against **Simian Immunodeficiency Virus (SIV) Infection** — a primate lentiviral disease mechanistically related to HIV-1 —
with **no registered clinical trials** and **1 preclinical publication** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy; inferred from clinical context — not yet registered in the Philippines) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Abacavir is a carbocyclic synthetic nucleoside analogue whose intracellular active metabolite — carbovir triphosphate (CBV-TP) — competitively inhibits HIV-1 reverse transcriptase and terminates viral DNA chain elongation, blocking viral replication.

SIV and HIV-1 are both primate lentiviruses (family *Retroviridae*) that share the same RNA-dependent DNA polymerase (reverse transcriptase) replication mechanism. The amino acid sequence homology between SIV RT and HIV-1 RT is approximately 80%, suggesting that CBV-TP could competitively occupy the SIV RT catalytic site and terminate proviral DNA synthesis in an analogous manner. In vitro susceptibility data further supports cross-species applicability of NRTIs at this homology level. This is the most likely basis for TxGNN's high prediction score.

It should be noted that SIV infection primarily affects non-human primates and is not a direct human clinical disease. The practical relevance of this prediction therefore lies more in supporting primate HIV research models than in direct clinical repurposing. If the research objective is a human indication, a closer analogue would be HIV-2 — also covered by the same preclinical study identified below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abacavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro / Preclinical susceptibility assay | *Antiviral Therapy* | Evaluated 16 approved antiretrovirals (including Abacavir) against HIV-2 (ROD, EHO), SIV (mac251, B670) and SHIV strains; provides comparative susceptibility data across primate lentivirus species with implications for treatment and post-exposure prophylaxis design |

---

## Philippines Market Information

Abacavir currently has **no product registrations** with the Philippine Food and Drug Administration (FDA-PH). There are no active licenses, approved indications, or marketed formulations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Philippines FDA-registered package insert data (warnings, contraindications) was not available in this evidence pack (Data Gap: DG001). Drug interaction data was also not retrieved. These gaps must be resolved before any clinical decision-making can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically coherent — SIV and HIV-1 share ~80% RT sequence homology, making Abacavir's NRTI mechanism theoretically applicable — but the predicted indication is a non-human primate disease with no direct human clinical target, Abacavir is not registered in the Philippines, and critical safety data is absent from this pack.

**To proceed, the following is needed:**

- **Clarify research objective:** Determine whether the goal is (a) supporting non-human primate HIV research models, (b) exploring cross-species antiretroviral activity for veterinary use, or (c) identifying a related *human* indication (e.g., HIV-2, which shares the same preclinical evidence)
- **Retrieve MOA data:** Query DrugBank API for Abacavir mechanism of action, target binding data, and resistance profile (Data Gap: DG002)
- **Retrieve safety data:** Download and parse the Philippines FDA (or FDA-approved) package insert for warnings, contraindications, and known drug interactions (Data Gap: DG001)
- **Expand literature search:** Conduct a structured review of Abacavir *in vivo* activity against SIV strains — current evidence is limited to a single in vitro susceptibility assay
- **Consider re-ranking for human indication:** If human clinical repurposing is the goal, evaluate whether Rank 2 (feline AIDS) or other TxGNN predictions with more direct human disease biology warrant promotion to primary candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

