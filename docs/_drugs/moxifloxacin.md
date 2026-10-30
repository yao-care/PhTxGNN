---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 9
monitor_inn: "Moxifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
last_modified_at: 2026-10-30
description: "Moxifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections (streptococcal, staphylococcal, pneumonia…"
---

# Moxifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Moxifloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibacterial.
The TxGNN model predicts it may be useful for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal, pneumonia, peritonitis, conjunctivitis, plague), as recorded in the knowledge graph. The local licence record contains no approved indication text. |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Number of Approvals | 1 (single-ingredient registration) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Moxifloxacin is generally known as a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV.

For this prediction, no plausible mechanistic link was identified. Polyclonal hyperviscosity comes from excess immunoglobulin in the blood and is not an infectious process, so an antibacterial would not be expected to treat it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not a finding backed by clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials are registered for polyclonal hyperviscosity syndrome.

For context, other lower-ranked predictions had only indirectly related trials, none of which studied the predicted disease itself:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Moxifloxacin alone vs. ciprofloxacin plus amoxicillin/clavulanic acid for fever in low-risk neutropenic cancer patients (matched to monoclonal gammopathy and congenital hematological disorder; indirect only) |
| [NCT00324324](https://clinicaltrials.gov/study/NCT00324324) | Phase 3 | Terminated | 240 | Moxifloxacin vs. placebo to prevent bacterial infections after allogeneic stem cell transplant (infection prevention, not the predicted disease) |

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0332 | Moxifloxacin | Not specified | Not specified |

This is a single-ingredient registration. The record contains no approved indication text, so the indications listed above come from the TxGNN model (deep learning). The scores may reflect similarities the model learned between related diseases, not biological evidence, and the indications are not confirmed approvals.

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease, epilepsy, cirrhosis of liver, drug-induced liver injury, potassium deficiency disease, tendinitis, peripheral neuropathy and other peripheral nervous system disease, myasthenia gravis, neuromuscular junction disease, Clostridium difficile colitis and perinatal necrotizing enterocolitis.
- **Drug Interactions**: 100 interactions were found. Major-level ones among those listed include hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids), bupropion and chlorpropamide. Moderate-level ones include antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid and calcium or potassium salts.

Please also refer to the package insert for the full safety information, which was not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism. The evidence level is L5. The contraindication profile (QT prolongation, neuropathy, dysglycemia) argues against use in this setting.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking moxifloxacin to hyperviscosity from polyclonal immunoglobulin excess
- Mechanism of action data and Philippine package insert warnings and contraindications
- Preclinical or clinical studies that directly address this disease
- A benefit-risk review that takes the knowledge-graph contraindications into account
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

