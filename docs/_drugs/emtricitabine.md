---
layout: default
title: Emtricitabine
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 3
monitor_inn: "Emtricitabine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Emtricitabine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease"
---

# Emtricitabine
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

## Emtricitabine: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Emtricitabine is an antiretroviral drug whose use in HIV infectious disease and AIDS is recorded in the knowledge graph. The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**. This is supported by **0 clinical trials** and **18 publications**, mostly macaque studies of SHIV/SIV prevention and treatment, so the evidence is preclinical and indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (relations recorded in the knowledge graph; no approved indication text in the local licence record) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (the cited studies are mainly animal models using SHIV/SIV, or reviews; none directly studies the predicted disease in a clinical setting) |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Number of Approvals | 1 licence (single-ingredient) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI). After conversion to its active triphosphate form, it terminates proviral DNA chain elongation.

Simian immunodeficiency virus (SIV) is a lentivirus closely related to HIV and also depends on reverse transcriptase. This makes the mechanistic link plausible. Macaque studies show that emtricitabine combined with tenofovir (given orally or as a gel) protected animals from SHIV challenge, which supports the idea that the drug acts against these viruses.

However, SIV infection is mainly a veterinary and research-model disease. Its main value is as a translational model for HIV prevention and treatment, which is already the recorded use of the drug. The prediction therefore adds little independent repurposing value beyond HIV. Also, many of the cited studies use emtricitabine in combination with tenofovir, so the effect of emtricitabine alone is not isolated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 18 retrieved publications, the most relevant are listed below (animal studies and reviews; no human RCTs).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal study | J Infect Dis | Oral emtricitabine + tenofovir alafenamide protected macaques from repeated rectal SHIV exposure |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study | J Infect Dis | Emtricitabine/tenofovir DF prevented vaginal SHIV infection in macaques, even with Chlamydia and Trichomonas coinfection |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal study | J Infect Dis | Oral tenofovir alafenamide/emtricitabine or tenofovir alafenamide alone tested against vaginal SHIV in macaques |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study | AIDS Res Hum Retroviruses | Polyvalent virus-like particle vaccine plus partially protective oral PrEP prevented SHIV infection in macaques |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study | J Infect Dis | Emtricitabine/tenofovir DF PrEP tested against a tenofovir-resistant (K65R) SHIV in macaques |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Animal study | J Virol | Intermittent Truvada prophylaxis tested against an emtricitabine-resistant (M184V) SHIV in macaques |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Preclinical virology | J Virol | M184V-mutant SIV emerged in macaques treated with lamivudine or emtricitabine, with reduced viral fitness |
| [22964889](https://pubmed.ncbi.nlm.nih.gov/22964889/) | 2012 | Review | Curr Opin HIV AIDS | Review of animal models of antiretroviral prophylaxis for HIV prevention |
| [22918448](https://pubmed.ncbi.nlm.nih.gov/22918448/) | 2012 | Review | Curr Opin HIV AIDS | Considerations for antiretroviral chemoprophylaxis in men who have sex with men |
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Review of systemic pre-exposure prophylaxis for HIV infection |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0163 | Emtricitabine | Not specified | Not specified in the record |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** the knowledge graph links emtricitabine with contraindication relations for conditions including liver disease, liver failure, kidney disease, chronic hepatitis B and C virus infection, lactic acidosis, Fanconi renotubular syndrome, hypophosphatemia, osteomalacia, long QT syndrome and torsades de pointes, and several psychiatric disorders. These are model-derived relations and need verification against the official label.
- **Drug Interactions:** 20 interactions were found in the DDI database. The **Major** ones are **leflunomide** and **teriflunomide**. **Moderate** ones include orlistat, naltrexone, cobicistat, methotrexate, cladribine, clofarabine, epirubicin, idelalisib, interferon beta-1a/1b, peginterferon beta-1a, asparaginase, pegaspargase, brentuximab vedotin, cabozantinib, tioguanine and trabectedin. **Minor:** eribulin.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, but the supporting evidence comes only from macaque and other animal models, mostly using emtricitabine in combination with tenofovir. SIV infection is not a human disease, so the prediction offers little repurposing value beyond HIV, which is already the drug's recorded use. The package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data from DrugBank
- A clear decision on whether a non-human, model-organism disease is a worthwhile target; if not, the focus should return to HIV-related indications
- Approved indication text and dosage forms for licence PNF-0163
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

