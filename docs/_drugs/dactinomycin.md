---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 95
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Dactinomycin: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). Approved use: Ewing sarcoma, rhabdomyosarcoma, Wilms tumor…"
monitor_inn: "Dactinomycin"
predicted_indications: ["relapsing-remitting multiple sclerosis", "liver sarcoma", "upper aerodigestive tract neoplasm", "head and neck cancer"]
---

# Dactinomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Dactinomycin: From Ewing Sarcoma and Rhabdomyosarcoma to Relapsing-Remitting Multiple Sclerosis
{: .text-alpha }

## One-Sentence Summary

Dactinomycin is a cytotoxic chemotherapy drug, originally used for Ewing sarcoma, rhabdomyosarcoma, Wilms tumor, testicular germ cell tumors and gestational trophoblastic neoplasm.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **no clinical trials and no publications** currently support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ewing sarcoma, rhabdomyosarcoma, Wilms tumor, testicular germ cell tumors, gestational trophoblastic neoplasm (from the drug's recorded indications; the local registration has no indication text) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the compiled data. Dactinomycin is generally known as a cytotoxic transcription inhibitor. It intercalates into DNA and blocks RNA polymerase. Its efficacy in several paediatric and germ cell cancers is well established.

The link to multiple sclerosis (MS) is weak. MS is an immune-mediated disease of the central nervous system, and no mechanistic connection to dactinomycin's antitumour action has been shown. The very high TxGNN score (ranked 3,379th among the model's predictions) is probably a TxGNN model (deep learning) artefact rather than a real biological signal.

There is also a practical barrier. Dactinomycin causes serious systemic toxicity, including myelosuppression, liver injury and severe tissue damage if the drug leaks out of the vein. That is hard to justify in a chronic, non-malignant disease that already has safer disease-modifying treatments.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0127 | Dactinomycin | Valid |

Dosage form and approved-indication text are not recorded for this registration. The drug is marketed in the Philippines, with 1 valid licence of 1.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antitumour antibiotic, transcription inhibitor) |
| Myelosuppression Risk | High. Knowledge-graph contraindications include neutropenia, thrombocytopenia, leukopenia, anaemia, agranulocytosis and aplastic anaemia |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential, liver function (hepatopathy is reported with dactinomycin-containing regimens), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations. Extravasation (leakage from the vein) can cause severe tissue injury |

---

## Safety Considerations

**Contraindication signals (from the TxGNN knowledge graph, not package insert text):**
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic anaemia), aplastic anaemia
- Liver and vascular disorders: liver disease, gallbladder disease, hepatic vein thrombosis, Budd-Chiari syndrome
- Viral infections: varicella zoster infection, herpes zoster

**Drug Interactions** (100 interactions recorded; the 20 reviewed are summarised below):
- **Major:** deferiprone, samarium (153Sm) lexidronam
- **Moderate:** palifermin, strontium chloride Sr-89, fostamatinib, mercaptopurine, roflumilast, chloramphenicol
- **Minor:** levofloxacin
- The rest, including several antiemetics (ondansetron, granisetron, metoclopramide, dexamethasone), have no severity rating.

Package insert warnings and contraindications for the Philippines are not available. Please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). It has no plausible mechanism for MS, and dactinomycin's toxicity is a major barrier in a chronic non-oncologic condition. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- A credible biological rationale or preclinical data linking dactinomycin to MS pathology
- Mechanism of action data
- Package insert warnings and contraindications
- A benefit-risk comparison against existing MS disease-modifying therapies

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

