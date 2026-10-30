---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
monitor_inn: "Isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
last_modified_at: 2026-10-30
description: "Isosorbide Dinitrate: predicted new indication Alopecia (evidence level L5). Approved use: Not stated in the local registration record"
---

# Isosorbide Dinitrate
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

## Isosorbide Dinitrate: From a Nitrate Vasodilator to Alopecia
{: .text-alpha }

## One-Sentence Summary

Isosorbide dinitrate is an organic nitrate vasodilator that is registered and marketed in the Philippines. The local record does not state an approved indication.
The TxGNN model predicts it may be useful for **alopecia**, but **no clinical trials and no publications** currently support this prediction.
The link is a TxGNN model (deep learning) prediction only, and it may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local registration record |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Isosorbide dinitrate belongs to the organic nitrate class, which acts as a nitric oxide (NO) donor. In general, this raises cGMP and relaxes vascular smooth muscle.

A possible, unproven link is that NO-mediated vasodilation could increase scalp microcirculation. This is similar to the hypothesis behind minoxidil-type vasodilators. This is speculative.

No study in the compiled data tests isosorbide dinitrate in alopecia. The high TxGNN score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Related hair-disorder predictions (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, hypertrichosis) also rank highly with no supporting data. Several of these are genetic or autoimmune conditions that a vasodilator would not be expected to address.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0265 | Isosorbide Dinitrate | Not listed | Not listed |

This is a single-ingredient product with a valid status. The record does not include indication text, so no approved use can be described from local licence data.

---

## Safety Considerations

- **Contraindication-type relations in the knowledge graph (not label text):** The TxGNN knowledge graph records drug-disease contraindication relations for hypotensive disorder, hypertrophic cardiomyopathy, coronary artery disease, stroke and cerebrovascular disorders, myocardial infarction, intracerebral hemorrhage, intracranial hypertension, anaemia and haemoglobinopathy, hyperthyroidism and Graves disease, and slow acetylation. These come from graph data and must be checked against the official package insert.
- **Drug Interactions:** The interaction database lists 100 interacting drugs in total. Moderate-level interactions in the sample include:
  - bupropion
  - morphine and opium
  - dronabinol and nabilone
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - rosiglitazone
  - sapropterin

  Omeprazole is listed as minor.
- Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. No trials or publications address this disease, so the evidence level is L5. The mechanistic rationale (NO-mediated vasodilation) is speculative, and nothing links it to hair growth outcomes.

**To proceed, the following is needed:**
- Preclinical or exploratory clinical evidence that isosorbide dinitrate, probably topical, affects hair growth or scalp perfusion
- Mechanism of action data and the package insert (warnings, contraindications, indications, dosage forms)
- A safety assessment of hypotension and headache risks, especially if topical absorption is possible
- A review of other predictions with more existing data, such as pulmonary hypertension and vascular disease (including the Phase 3 diabetic foot ulcer trial NCT02789033). These may be better candidates for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

