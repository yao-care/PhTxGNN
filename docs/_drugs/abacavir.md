---
layout: default
title: Abacavir
parent: Moderate Evidence (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Abacavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
---

# Abacavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Abacavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is an antiretroviral drug originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, a non-human primate disease.
Support is thin: **0 clinical trials** and **1 publication** (a 2004 in vitro susceptibility study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, abacavir is a nucleoside reverse transcriptase inhibitor (NRTI). It is converted inside cells to carbovir triphosphate, which terminates viral DNA chain elongation. Its efficacy in HIV infection is established.

SIV is a lentivirus closely related to HIV and uses a homologous reverse transcriptase, so activity is biologically plausible. The very high TxGNN score most likely reflects this close similarity to HIV, the original indication, rather than a new repurposing signal.

An important limitation is that SIV infection is a disease of non-human primates. It has no human clinical indication. The evidence is relevant to animal models, not to human therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Tested 16 approved anti-HIV drugs and one experimental drug (AMD3100) against HIV-2, SIV and SHIV strains, to inform treatment and post-exposure prophylaxis. This is indirect, non-clinical evidence. |

## Philippines Market Information

The only registration on record (PNF-0001, Abacavir, single-ingredient product) has been cancelled. No dosage form or approved indication text is available.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text):
  - Liver and biliary: liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, pancreatitis, gallbladder disease
  - Kidney and urinary: kidney disease, pyoureter
  - Blood: neutropenia, agranulocytosis, anemia, macrocytic anemia
  - Muscle: myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, dermatomyositis, myositis
  - Metabolic: lactic acidosis, hypertriglyceridemia, obesity disorder, monogenic obesity
- **Drug Interactions**: 93 interactions were identified. The main ones with a graded level are **Naltrexone** (Moderate) and **Orlistat** (Moderate). Many others are of unknown severity, including metformin, rosiglitazone, glimepiride, omeprazole, pantoprazole, lansoprazole, morphine, prednisone, hydrocortisone, vancomycin, amphotericin B and sulfasalazine.

Please also refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is an in vitro study in a non-human primate virus. SIV infection has no human clinical indication, and the high TxGNN score mostly reflects similarity to HIV. The sole Philippine registration is cancelled.

**To proceed, the following is needed:**
- Clarification of whether a veterinary or animal-model indication falls within the scope of human drug repurposing
- Detailed mechanism of action data
- Package insert warnings and contraindications for safety screening
- Current Philippine registration status, if human use is to be considered

---

### Other Predictions Considered

The data compiled for this report also contained two lower-ranked predictions. Neither changes the recommendation.

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Feline acquired immunodeficiency syndrome | 99.79% | L4 | Hold | One 2002 preclinical in vitro study (PMID [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/)) of a zidovudine, lamivudine and abacavir combination against feline immunodeficiency virus. Abacavir's individual contribution cannot be separated. This is a veterinary condition. |
| Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.78% | L5 | Hold | Model prediction only. There are no trials or literature, and no biological rationale can be derived. It should be treated as hypothesis-generating only. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

