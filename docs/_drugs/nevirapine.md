---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

Using the `txgnn-pipeline` skill to confirm context. The skill confirms this is a standard TxGNN pipeline report. Now generating the evaluation report from the Evidence Pack.

---

# Nevirapine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) developed for the treatment of HIV-1 infection in humans.
The TxGNN model predicts it may have potential against **Feline Acquired Immunodeficiency Syndrome (FIV-AIDS)** as its top indication, supported by only **0 clinical trials** and **1 publication** — a single biochemical structural comparison study.
Importantly, all three top-ranked predictions are either veterinary diseases or research-model conditions rather than conventional human indications, and Nevirapine currently has no registered products in the Philippines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (no Philippines registration on record) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Nevirapine is an NNRTI class antiretroviral whose efficacy in HIV-1 infection is well established; mechanistically it targets the reverse transcriptase (RT) enzyme, and may in principle be applicable to other lentiviral infections that depend on the same enzyme.

Feline Immunodeficiency Virus (FIV) causes an immunodeficiency syndrome in cats that is broadly analogous to human HIV-AIDS. Both FIV and HIV-1 belong to the genus *Lentivirus* and depend on reverse transcriptase for replication, which forms the theoretical basis for the TxGNN knowledge-graph prediction.

However, there is a fundamental structural barrier: the NNRTI binding pocket (NNIBP) of FIV RT differs from that of HIV-1 RT at key residues (Y181, K103, and others), significantly reducing the affinity of HIV-1 NNRTIs — including Nevirapine — for FIV RT. The only available publication (PMID 38031646) is a biochemical and structural comparison study; no antiviral activity against FIV has been confirmed in cell-based assays. Additionally, this is a veterinary indication, which falls outside the conventional scope of human drug repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*(Top-ranked indication: Feline Acquired Immunodeficiency Syndrome)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro / Structural Biochemistry | Journal of Veterinary Science | Biochemical and structural comparison of HIV NNRTIs — including Nevirapine (NVP) and efavirenz (EFV) — against FIV and HIV RT. Investigates whether NNRTIs approved for HIV could inhibit FIV reverse transcriptase; no confirmed antiviral activity against FIV reported. |

---

## Philippines Market Information

Nevirapine currently has **no drug registrations** in the Philippines. No authorization numbers, product names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN top-ranked predictions fall outside the applicable scope of human drug repurposing: the top two are veterinary/non-human primate research conditions where Nevirapine's biological activity is structurally limited or unconfirmed, and the third (a rare genetic neurodevelopmental white matter disorder) has no biological plausibility and is assessed as a model false positive. Evidence is at the preclinical structural-comparison level only (L4), with no cell-based antiviral activity data and zero clinical trials. The drug is also absent from the Philippines market entirely.

**To proceed, the following is needed:**

- **Redirect prediction scope**: Re-run TxGNN with a filter excluding veterinary and non-human primate indications to surface human-relevant repurposing candidates.
- **FIV antiviral activity confirmation**: If the FIV indication remains of research interest, cell-based antiviral activity assays against FIV are required before any further investment.
- **MOA and safety data**: Retrieve complete mechanism of action and Philippines-relevant safety/warning information from DrugBank and the package insert (currently data gaps DG001 and DG002).
- **Regulatory pathway assessment**: If a viable human indication is identified, a full Philippines FDA registration strategy would be needed given zero existing market presence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

