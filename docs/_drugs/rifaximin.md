---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rifaximin: Oral candidiasis
{: .text-alpha }

## One-Sentence Summary

Rifaximin is a gut-restricted oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **oral candidiasis**,
but there are **0 clinical trials** and only **1 publication**, and that publication points to a possible *risk* rather than a benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is an oral, minimally absorbed antibiotic that acts mainly in the gut. Its efficacy in hepatic encephalopathy is attributed to reducing gut bacteria.

For oral candidiasis, a mechanistic link is hard to support. Rifaximin has no known antifungal activity. The only publication found (PMID 34180023) is a cohort study in allogeneic stem cell transplant recipients. It suggests rifaximin use was associated with **micafungin-resistant Candida infections**. This points to a possible safety concern, likely through disruption of the gut microbiome, rather than a therapeutic benefit.

The high prediction score therefore appears to reflect network similarity in the model rather than a validated biological rationale. The related prediction for general candidiasis (score 0.9915) shows the same pattern. Its two observational studies also suggest increased risk, not benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin prophylaxis was associated with micafungin-resistant *Candida* infections. This is a safety signal, not evidence of benefit. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0423 | Rifaximin | Not specified | Not specified (status: valid) |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: *Clostridium difficile* colitis; perinatal necrotizing enterocolitis.
- **Drug Interactions**: 69 interactions were identified. One is Major: live cholera vaccine (*Vibrio cholerae* CVD 103-HgR). The sample reviewed also included Moderate interactions with warfarin, cyclosporine, tolvaptan, apalutamide, darolutamide, cabozantinib, encorafenib, and the hepatitis C antivirals daclatasvir and ledipasvir, among others.
- **Infection risk signal**: The published literature links rifaximin use to resistant *Candida* infections in transplant recipients. This is directly relevant to the proposed indication.

Please refer to the package insert for further safety information, such as warnings and labelled contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by a plausible mechanism or by clinical evidence. The only available study suggests a possible harm (resistant *Candida* infections). The Philippines registration is also cancelled, with no indication or dosage form on file.

**To proceed, the following is needed:**
- Mechanism of action data, to assess whether any biological link to oral candidiasis exists
- Package insert warnings and contraindications from the Philippines regulator (the current registration is cancelled)
- Further analysis of the *Candida* resistance signal, ideally with controlled data that accounts for underlying disease
- Preclinical or in vitro evidence of any benefit in oral candidiasis before considering clinical studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

