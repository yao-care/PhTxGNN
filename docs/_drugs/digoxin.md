---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used for atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are **no clinical trials** and only **1 loosely related publication**, which does not address digoxin in this condition.
This prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no valid registrations) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Digoxin is generally known as a Na+/K+-ATPase inhibitor with positive inotropic and vagotonic effects, which explains its use in atrial fibrillation.

Prinzmetal (vasospastic) angina is driven by coronary vasospasm and is usually treated with calcium channel blockers and nitrates. Digoxin may increase vascular tone and is not expected to relieve vasospasm. No credible mechanistic link between the original and the predicted indication has been established.

The high TxGNN score (0.998) is a model prediction based on knowledge-graph proximity. The only linked paper concerns chronopharmacology of antihypertensive treatment and does not study digoxin in Prinzmetal angina.

Other predicted indications were also reviewed (duodenal obstruction, duodenal ulcer, duodenogastric reflux, an obsolete ischemic stroke susceptibility term, and hypoalphalipoproteinemia). All are at evidence level L5 with no plausible mechanistic link, and none has supporting trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of chronopharmacology and antihypertensive treatment. It does not address digoxin or Prinzmetal angina. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0144 | Digoxin | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: kidney disease, pyoureter, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, cor pulmonale, Wolff-Parkinson-White syndrome, sick sinus syndrome, ventricular fibrillation, hypertrophic cardiomyopathy, atrioventricular block, myxedema, hypothyroidism, myocarditis, constrictive pericarditis, restrictive cardiomyopathy.
- **Drug Interactions**: 100 interactions were found; the 20 reviewed are mostly Moderate, with some Minor. Moderate examples include acarbose, rabeprazole, doxycycline, epinephrine, hydrocortisone, cholecalciferol, metformin, amphotericin B, bupropion, triamcinolone, acetylsalicylic acid, dexamethasone, betamethasone, tetracycline and calcium phosphate. Minor examples include albiglutide, hyoscyamine, atropine and glycopyrronium.

Please also refer to the package insert for label-based warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone: no trials, no relevant literature, and no plausible mechanism. Digoxin has no expected benefit in vasospasm. Its contraindication profile includes several cardiac conditions, and it has no valid registration in the Philippines.

**To proceed, the following is needed:**
- Mechanism-of-action data and a credible mechanistic rationale for coronary vasospasm
- Preclinical or clinical studies of digoxin in Prinzmetal angina
- Package insert warnings and contraindications from the Philippines FDA
- Clarification of the cancelled registration status if local use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

