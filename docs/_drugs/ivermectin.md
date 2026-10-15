---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 191
evidence_level: L5
indication_count: 9
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Ivermectin: From Strongyloidiasis and Onchocerciasis to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an antiparasitic drug originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Strongyloidiasis, onchocerciasis (the Philippines license record has no indication text) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ivermectin is known as an antiparasitic that acts on glutamate-gated chloride channels in invertebrates. Its efficacy in strongyloidiasis and onchocerciasis is established.

These channels are not present in fungi, and the data compiled for this report show no mechanistic link between ivermectin and *Candida* or vulvovaginal candidiasis. The high score (99.95%) appears to be a graph-based association only. Other candidiasis and vaginitis entries in the prediction list score similarly high, which suggests the model is picking up on disease-network proximity rather than a pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction, vulvovaginal candidiasis.

Two publications were linked to lower-ranked predictions. Neither supports antifungal efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case report | BMJ Case Reports | Disseminated strongyloidiasis after prolonged corticosteroid treatment. This is the drug's original indication, not candidiasis (linked to esophageal candidiasis). |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case report | Australasian Journal of Dermatology | Two immunocompromised children with crusted scabies were treated successfully with oral ivermectin. One child had chronic mucocutaneous candidiasis, but the report does not show an antifungal effect (linked to congenital candidiasis). |

## Philippines Market Information

The Philippines registration record lists one authorization, which has been cancelled. It carries no dosage form or approved-indication text. There are no currently valid single-ingredient or combination registrations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0269 | Ivermectin | Not recorded | Not recorded |

## Safety Considerations

- **Disease-level contraindications (from the knowledge graph, not label text)**: loiasis and filariasis.
- **Drug Interactions**: 100 interactions were identified. The main ones rated Moderate are:
  - Aprepitant
  - Clarithromycin
  - Ethanol
  - Cobicistat
  - Deferasirox
  - Warfarin
  - Dicoumarol
  - Fostamatinib
  - Radioactive iodide (I-123, I-131)
  - Abametapir (topical)

  Other interactions have no severity rating, including omeprazole, lansoprazole, prednisone, prednisolone, dexamethasone, ranitidine, famotidine, ursodeoxycholic acid and heparin.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or relevant literature, and no plausible antifungal mechanism is evident. The drug has no valid Philippines registration at present. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Detailed mechanism of action data, and any in vitro evidence of activity against *Candida* species
- Preclinical or early clinical studies in vulvovaginal candidiasis
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of the regulatory status of the cancelled registration, and the route and formulation that would be needed
- A review of whether established antifungal treatments already meet the clinical need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

