---
layout: default
title: Tenofovir
parent: Model Prediction Only (L5)
nav_order: 329
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tenofovir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Tenofovir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Tenofovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tenofovir: From Chronic Hepatitis B and HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir is a nucleotide reverse transcriptase inhibitor, originally used to treat chronic hepatitis B virus infection, HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (feline AIDS, caused by FIV)**,
but there are **0 registered clinical trials** and only **2 veterinary publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infectious disease; AIDS (the Philippine registration record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 (animal studies only; no human trials) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tenofovir (and its analog PMPA) is a nucleotide reverse transcriptase inhibitor. Its efficacy in HIV and hepatitis B is established, and mechanistically it may be applicable to feline AIDS.

Feline immunodeficiency virus (FIV) is a lentivirus whose reverse transcriptase is homologous to that of HIV-1. This makes it plausible that the same mechanism carries over. Two publications describe antiviral treatment of FIV-infected cats with PMPA or an antiretroviral combination that included tenofovir, suggesting activity in the native host.

However, this is a veterinary indication. The data are preclinical or veterinary only, so relevance to human-oriented repurposing is limited. The missing mechanism-of-action data also weakens formal mechanistic validation.

Two other predictions were also generated. The second, **simian immunodeficiency virus infection**, is supported by many macaque studies of tenofovir-based prevention. It is essentially an animal model of the already approved HIV indication, not a new human disease. The third, a rare neurodevelopmental disorder with ataxic gait, has no mechanistic link, no trials and no literature. Its score (about 99.96%) is nearly identical to the others, so the score does not discriminate well between indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Veterinary in vivo study | Viruses | Evaluated pharmacokinetics and clinical outcomes of combination antiretroviral therapy (dolutegravir, tenofovir, emtricitabine) in FIV-infected domestic cats |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Veterinary in vivo study | Journal of Feline Medicine and Surgery | Treatment of naturally FIV-infected cats with PMPA (a tenofovir analog); notes that no antiviral is registered for FIV in cats and that human antivirals have caused serious adverse effects in cats |

## Safety Considerations

- **Disease-related cautions from the knowledge graph** (these are model-derived associations, not label text): the knowledge graph links tenofovir to contraindication-type concerns in several conditions, including kidney disease, Fanconi renotubular syndrome, liver disease, liver failure, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis, hypophosphatemia, osteomalacia, rickets, long QT syndrome and torsades de pointes, hepatitis C virus infection, and certain psychiatric and neurological conditions (such as epilepsy and anxiety disorder). These should be verified against an official package insert.
- The animal literature itself notes that human antivirals have caused serious adverse effects in cats.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is veterinary, with no registered clinical trials and only two animal studies. The only Philippine registration is cancelled, and package insert safety data and mechanism-of-action data are missing. The evidence does not support moving forward as a human drug repurposing candidate. The simian immunodeficiency virus prediction largely restates the existing HIV indication.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of whether a veterinary indication falls within the scope of this repurposing program
- Controlled veterinary efficacy and safety studies in FIV-infected cats, if the veterinary direction is pursued
- Confirmation of the current regulatory status of the cancelled Philippine registration (PNF-0475)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

