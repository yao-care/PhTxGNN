---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (NSIAD) (evidence level L5). Approved use: Not recorded in the Philippines registration data (pharmacologicall…"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: From a Long-Acting Beta2-Agonist Bronchodilator to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an inhaled, ultra-long-acting beta2-adrenergic agonist, used as a bronchodilator for obstructive airway disease.
The TxGNN model predicts it may be useful for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines registration data (pharmacologically, an inhaled bronchodilator for asthma and COPD) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known pharmacology, indacaterol is an ultra-long-acting beta2-agonist. It raises intracellular cAMP and relaxes airway smooth muscle, and its efficacy in obstructive airway disease is established.

NSIAD is a rare condition caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*). It leads to excessive water retention and low blood sodium. Beta2-adrenergic agonism and vasopressin V2 signalling both act through cAMP, which may be why the model links them. This is speculation and no data supports it. A beta2-agonist would not be expected to block a receptor that is constitutively active, so the high score should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Philippines Market Information

| Authorization Number | Product Name | Status | Dosage Form | Approved Indication |
|---------|------|------|------|-----------|
| PNF-0247 | Indacaterol | Cancelled | Not recorded | Not recorded |

The only registration is cancelled, and no valid single-ingredient or combination registrations exist.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease edges in the TxGNN knowledge graph, not package insert text):
- Cardiovascular: hypertension, hypertensive disorder, coronary artery disease, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease
- Metabolic and endocrine: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, potassium deficiency (hypokalaemia), thyrotoxicosis, hyperthyroidism, Graves disease
- Neurological: epilepsy

**Drug Interactions** (100 interactions were retrieved; main ones are listed):
- **Moderate:** epinephrine, isometheptene, clarithromycin, famotidine
- **Moderate (antidiabetic drugs, since beta2-agonists can raise blood glucose):** acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, metformin, pioglitazone, saxagliptin
- **Minor (corticosteroids and others):** hydrocortisone, triamcinolone, dexamethasone, beclomethasone, betamethasone, budesonide, aprepitant

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical or literature support (L5) and no clear mechanism.
- The only Philippines registration is cancelled.
- The knowledge-graph contraindication signals (cardiac and metabolic) add caution.

**To proceed, the following is needed:**
- Mechanistic work testing whether a beta2-agonist can influence V2-receptor-driven water retention in NSIAD
- Preclinical or case-level evidence of any effect on antidiuresis or serum sodium
- The package insert warnings and contraindications, and the mechanism of action from DrugBank
- Clarification of the cancelled registration, the dosage form, and the original approved indication

**Note on other predictions:** Among the other top-10 predictions, only "bronchial disease" (rank 7) has substantial evidence, including Phase 3 asthma trials. It mostly confirms indacaterol's established respiratory use rather than a true repurposing, and much of that evidence is for combination products. The other predictions have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

