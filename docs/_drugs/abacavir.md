---
layout: default
title: Abacavir
parent: Model Prediction Only (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "Abacavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Abacavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS"
---

# Abacavir
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

## Abacavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor, and HIV infectious disease and AIDS are its original uses.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition.
Support is thin: **0 clinical trials** and **1 publication**, an in vitro combination study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS (relations recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Abacavir belongs to the nucleoside reverse transcriptase inhibitor (NRTI) class. In general terms, it is converted inside cells to carbovir triphosphate, which stops viral DNA chain elongation.

Feline immunodeficiency virus (FIV) is a lentivirus whose reverse transcriptase is related to that of HIV-1. This gives a plausible mechanistic rationale. However, the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The only study is an in vitro test of a zidovudine, lamivudine and abacavir combination against FIV. It cannot separate the contribution of abacavir alone. The indication is also veterinary, so its relevance to human drug repurposing is limited.

Two other predictions were also reviewed:
- **Simian immunodeficiency virus infection** (score 0.9979): one in vitro susceptibility study, with no clinical development path in humans.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9978): no trials or literature, and no evident link to the antiviral mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Preclinical combination study (classified from the title) | Antiviral Research | Zidovudine, lamivudine and abacavir combination suppressed FIV replication in vitro. FIV in cats is used as an animal model for HIV. |

The evidence level is L5 because the cited study is an in vitro study of a combination and does not directly demonstrate the effect of abacavir alone, nor any clinical effect in the predicted disease.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0001 | Abacavir | Not specified | Not specified |

This is a single-ingredient record with valid status. The record contains no approved indication text.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists contraindication relations with liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, pyoureter, lactic acidosis, neutropenia, agranulocytosis, anemia, macrocytic anemia, hypertriglyceridemia, obesity disorder, monogenic obesity, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, dermatomyositis and myositis.
- **Drug Interactions:** 93 interactions were found. The main ones listed are:
  - Moderate: naltrexone, orlistat.
  - Unclassified: metformin, morphine, omeprazole, pantoprazole, lansoprazole, glimepiride, rosiglitazone, prednisone, hydrocortisone, vancomycin, amphotericin B, sulfasalazine and others.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single in vitro combination study in a veterinary model, and no clinical trials exist. The indication offers no human development path, so the evidence is insufficient to proceed.

**To proceed, the following is needed:**
- Studies of abacavir alone in the predicted disease
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from the Philippine regulator
- Clarification of whether a human or veterinary development goal is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

