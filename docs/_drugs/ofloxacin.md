---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-23
description: "Ofloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Ofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ofloxacin: Polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ofloxacin is generally known as a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV.

Polyclonal hyperviscosity syndrome is driven by elevated serum immunoglobulins, not by bacterial infection. No plausible mechanistic link to ofloxacin's antibacterial action was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of benefit.

The data also include other predictions, all at L5 except plague:
- **Septicemic plague** is biologically plausible, with in vitro and animal data (mouse and monkey plague models, susceptibility studies of *Yersinia pestis*). It has no human trials, and its listed level is L4 as a research question. This is a better-supported lead than the top-ranked prediction.
- **Punctate epithelial keratoconjunctivitis** has only one case report about a vernal shield ulcer, which does not show an ofloxacin effect. Under the evidence rules, it is L5, not the L4 shown in the source data.
- Hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, monoclonal gammopathy, hematological disease with acquired peripheral neuropathy and congenital hematological disorder have no mechanistic rationale and no relevant evidence. Fluoroquinolones carry a peripheral neuropathy warning, so benefit in that last neuropathy-related condition is counterintuitive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0357 | Ofloxacin | Not specified | Not specified |

The registration is a single-ingredient product with valid status. No approved indication text is available in the data compiled for this report, so the approved uses in the Philippines cannot be confirmed. The infections listed above are relations recorded in the knowledge graph, not confirmed approved indications.

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (not label text): long QT syndrome, torsades de pointes, liver failure, drug-induced liver injury, epilepsy, kidney disease and impaired renal function, myasthenia gravis, peripheral neuropathy, tendinitis, rhabdomyolysis, diabetes mellitus, diabetic ketoacidosis, thrombocytopenia, leukopenia, anemia, potassium deficiency, *Clostridium difficile* colitis, and others.
- **Drug Interactions**: 100 interactions were found. The listed ones include:
  - **Major**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion, chlorpropamide.
  - **Moderate**: antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, calcium and potassium salts.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome has no clinical, literature or mechanistic support and is L5. Several knowledge-graph contraindications, including QT prolongation, neuropathy and liver and kidney disease, add caution.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking ofloxacin to immunoglobulin-driven hyperviscosity
- Mechanism of action data and the Philippines package insert (warnings, contraindications, approved indications)
- If a repurposing lead is wanted, consider re-prioritising toward septicemic plague, where in vitro and animal data exist; it would need human evidence and a review of the local regulatory position
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

