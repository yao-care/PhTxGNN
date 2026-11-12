---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-11-12
description: "Levothyroxine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Hypothyroidism"
---

# Levothyroxine
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

## Levothyroxine: From Hypothyroidism to Renal Hypodysplasia/Aplasia
{: .text-alpha }

## One-Sentence Summary

Levothyroxine is a thyroid hormone replacement, recorded in the knowledge graph for hypothyroidism and several thyroid conditions.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (relation recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Levothyroxine is a synthetic thyroid hormone. Scores on this page come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They are not approved indications confirmed by local label text.

A possible link is that thyroid hormone influences kidney development, and congenital hypothyroidism is associated with a higher rate of congenital kidney and urinary tract anomalies. However, this association does not show that levothyroxine treats or prevents renal hypodysplasia/aplasia. This is a structural developmental malformation, and postnatal hormone replacement is unlikely to reverse established defects. The prediction should be treated as a computational signal, not a therapeutic rationale.

The other top predictions point the same way:
- **Bilateral renal agenesis** (score 0.9960): congenital absence of both kidneys, with no plausible way for a hormone to restore absent organs.
- **Potter sequence** (score 0.9933): a speculative link through thyroid hormone's role in fetal lung maturation, but no evidence of benefit.
- **Carney complex** (score 0.9918): only a tenuous overlap with thyroid manifestations; the underlying PKA pathway defect is not addressed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Levothyroxine (as sodium/anhydrous sodium) | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph lists the following as contraindication relations: hypertension, pituitary hormone deficiencies and hypopituitarism (including growth hormone deficiency and Kallmann syndrome), osteoporosis (including postmenopausal), diabetes mellitus and diabetic ketoacidosis, coronary artery disease, myocardial infarction, and thymus gland disease. These need confirmation against the package insert.
- **Drug Interactions**: 100 interactions were found in the DDI query. The main ones listed are mostly moderate:
  - Antidiabetic drugs: acarbose, metformin, pioglitazone, alogliptin, albiglutide, dulaglutide, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin
  - Acid suppressants: omeprazole, rabeprazole and dexlansoprazole (moderate), cimetidine (minor)
  - Minerals and antacids: calcium phosphate, calcium acetate, magnesium oxide
  - Sympathomimetics: epinephrine, isometheptene, diethylpropion

Please refer to the package insert for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score. No clinical trial or publication studies this disease, so the evidence level is L5. Renal hypodysplasia/aplasia is a structural malformation that thyroid hormone replacement is not expected to correct, and the other top predictions are likewise not clinically actionable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Mechanism of action data for levothyroxine
- Any preclinical or clinical evidence that thyroid hormone affects kidney development in a way that could be treated
- A clear rationale for a disease where treatment is plausible, before any further evaluation

<!-- review:begin ph-lic-20261106-levothyroxine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Package insert warnings and contraindications from the DOH-FDA Philippines (the licence record has no indication, dosage form or manufacturer details)" Removed: its description of the Philippine products did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-levothyroxine-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "(the licence record has no indication, dosage form or manufacturer details)" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

