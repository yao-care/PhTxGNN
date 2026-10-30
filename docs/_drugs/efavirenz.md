---
layout: default
title: Efavirenz
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 3
monitor_inn: "Efavirenz"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Efavirenz: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease and AIDS"
---

# Efavirenz
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

## Efavirenz: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Efavirenz is an antiretroviral drug originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary disease.
There are **no clinical trials** and only **1 publication** (an in vitro biochemical and structural study) directly addressing this disease, so the evidence is limited to model prediction and indirect laboratory data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relation recorded in the knowledge graph; the local licence record has no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Number of approvals | 1 licence (single-ingredient product, registration no. PNF-0162) |
| Recommended Decision | Hold |

*Note on evidence level: the only publication on this disease is an in vitro biochemical and structural comparison of reverse transcriptase inhibitors. It is not a clinical or in vivo study of the drug in feline disease, and the data compiled for this report contain no clinical trial for it. By the evidence ceiling rule, the level is therefore L5, although the earlier automated scoring listed L4.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) of HIV-1. Feline immunodeficiency virus (FIV) is also a lentivirus and has a reverse transcriptase, which is the likely reason the model links the two diseases.

The link is weak, however. NNRTIs are generally poor inhibitors of FIV reverse transcriptase because the NNRTI binding pocket differs structurally from that of HIV-1. The one retrieved 2023 study compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus enzymes in the laboratory. It does not show that the drug works in infected cats. The high TxGNN score probably reflects target similarity and not demonstrated activity. The disease is also veterinary, so its value for human drug repurposing is limited.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | Journal of Veterinary Science | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus reverse transcriptases to assess their potential for treating FIV; no in vivo efficacy shown |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0162 | Efavirenz | Not stated | Not stated in the licence record |

The licence is for a single-ingredient product and is currently valid. The record has no indication text or dosage form, so the approved use cannot be confirmed from it.

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (from the knowledge graph, not from label text): liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, chronic hepatitis B and C virus infection, kidney disease, Fanconi renotubular syndrome, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, delusional disorder, paranoid schizophrenia, gallbladder disease, hypertriglyceridemia, obesity disorder, hypophosphatemia, osteomalacia, rickets, lactic acidosis, and others.
- **Drug Interactions**: 100 interactions were found in the DDInter database. The only major one among the 20 listed is **dolasetron**. Moderate interactions include acarbose, famotidine, rabeprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, pioglitazone, loperamide, bupropion, aprepitant, clarithromycin, saxagliptin, dronabinol and minocycline.

Please refer to the package insert for label warnings and contraindications, as these were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a single in vitro study. No clinical trials exist, and NNRTIs are generally weak against FIV reverse transcriptase. The target disease is veterinary, so translation to human use is unlikely.

**To proceed, the following is needed:**
- In vivo efficacy data in FIV-infected cats, if the veterinary direction is of interest
- Detailed mechanism of action data for efavirenz
- Label text for the Philippine licence (indication, dosage form, warnings and contraindications)

---

### Other predictions noted (not evaluated in detail)

- **Simian immunodeficiency virus infection** (score 0.9980): The retrieved studies are mostly rhesus macaque work using RT-SHIV, an engineered virus carrying HIV-1 reverse transcriptase. Wild-type SIV is intrinsically resistant to NNRTIs, so this supports the existing HIV use and not a new indication. No clinical trials. Direct evidence for wild-type SIV is absent, so the level is L5. Hold.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9977): No trials and no literature. Level L5. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

