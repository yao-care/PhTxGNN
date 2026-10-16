---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 109
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Diltiazem: predicted new indication Obsolete susceptibility to ischemic stroke (evidence level L5). Approved use: Hypertension, atrial fibrillation, Prinzmetal angina…"
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Hypertension to Susceptibility to Ischemic Stroke (Obsolete Term)

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **susceptibility to ischemic stroke (an obsolete ontology term)**,
but **no clinical trials and no publications** currently support this prediction; it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved indication text is available for the Philippine registration) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diltiazem is a non-dihydropyridine calcium channel blocker. Its efficacy in hypertension and atrial fibrillation is established, and mechanistically it may be applicable to stroke risk reduction.

A plausible indirect rationale is that lowering blood pressure reduces a major stroke risk factor. Calcium channel blockade may also reduce cerebral vasospasm and calcium-mediated ischemic injury. These are hypotheses, not verified findings.

There are two important caveats:
- **Confounding:** Hypertension and atrial fibrillation are both established stroke risk factors. Any apparent stroke-prevention signal may reflect treatment of those conditions rather than a distinct repurposing effect.
- **Obsolete term:** The predicted disease is labelled "obsolete", suggesting a deprecated ontology entry. It may map poorly onto current stroke classifications and could inflate or distort the prediction.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0146 | Diltiazem | Not specified | Not specified (status: cancelled) |

The only registration found is cancelled, and no product is currently marketed under a valid single or combination license.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The drug-disease contraindication links include:
  - Cardiac conduction and rhythm: atrioventricular block, sick sinus syndrome (including familial), Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia (including catecholaminergic and infant forms)
  - Haemodynamic and structural: hypotensive disorder, aortic stenosis and related valve disease, hypertrophic cardiomyopathy, renal artery obstruction
  - Organ and blood: kidney disease, liver disease, gallbladder disease, neutropenia, agranulocytosis
  - Angioedema (acquired, hereditary, RAAS-blocker-induced, non-histaminic)
  - Connective tissue, bone and cartilage disease
- **Drug Interactions:** 100 interactions were found in total, and the data compiled for this report lists 20 of them, all moderate except one.
  - **Major:** loperamide
  - **Moderate (examples):** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), pioglitazone, bupropion, aprepitant, morphine, acetylsalicylic acid, canagliflozin, and several calcium salts (carbonate, chloride, citrate, acetate and others)

Please refer to the package insert for label warnings, as none were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high but rests on the model alone, with no trials or literature. The predicted disease term is obsolete, the benefit is confounded by existing hypertension and atrial fibrillation indications, and the only Philippine registration is cancelled.

**To proceed, the following is needed:**
- Mapping of the obsolete disease term to a current ischemic stroke classification
- A literature and clinical trial search focused on diltiazem and stroke prevention or outcomes, separating effects from blood pressure and rhythm control
- Mechanism of action data (from DrugBank)
- Package insert warnings and contraindications from the DOH-FDA Philippines, which are required before safety screening
- Clarification of the cancelled registration status and whether any valid product is available locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

