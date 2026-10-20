---
layout: default
title: Biperiden
parent: Model Prediction Only (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Biperiden: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease and related parkinsonian and dystonic disorders"
monitor_inn: "Biperiden"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "paralysis agitans, juvenile, of Hunt", "Lewy body dementia", "attention deficit-hyperactivity disorder", "X-linked intellectual disability-ataxia-apraxia syndrome"]
---

# Biperiden
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

# Biperiden: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Biperiden is an anticholinergic drug, originally used to treat Parkinson disease and related parkinsonian and dystonic movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but this rests on the model score alone, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian and dystonic disorders (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, biperiden is a centrally acting anticholinergic (muscarinic antagonist). Its use in Parkinson disease and other movement disorders is established, and mechanistically it might be applicable to a focal inflammatory epileptic encephalopathy through modulation of cholinergic signalling.

This link is speculative. Rasmussen encephalitis is an immune-mediated disease driven by T-cell cytotoxicity, and biperiden has no known immunomodulatory action. The high TxGNN score (99.94%) is a model-derived prediction and is not backed by any clinical or literature evidence.

Other top-ranked predictions show the same pattern. Several (myelitis, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency) have no plausible mechanistic link. Others (juvenile parkinsonism, PLA2G6-associated neurodegeneration) mostly overlap with the existing parkinsonian indications. For Lewy body dementia, the mechanistic direction is opposed, because anticholinergic effects would be expected to worsen cognition.

## Safety Considerations

- **Contraindications and risk conditions (from the knowledge graph, not label text)**: The knowledge graph links biperiden with the following conditions, which should be treated as potential cautions:
  - Eye: open-angle, angle-closure and closed-angle glaucoma
  - Urinary tract and prostate: benign prostatic hyperplasia
  - Gastrointestinal: paralytic ileus, achalasia and megaesophagus, ulcerative colitis, inflammatory bowel disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, gastric ulcer, hiatus hernia
  - Cardiovascular: hypertension, hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Respiratory: chronic obstructive pulmonary disease
  - Organ disease: kidney, liver and gallbladder disease
- **Drug Interactions**: 75 interactions were identified. The main ones are:
  - **Major**: potassium chloride and potassium citrate
  - **Moderate**: other anticholinergic and antispasmodic agents (atropine, hyoscyamine, dicyclomine, glycopyrronium, clidinium, propantheline, methscopolamine, mepenzolate), opioids and antidiarrhoeals (morphine, opium, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), metoclopramide, and pramlintide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or publications for Rasmussen subacute encephalitis, so the prediction is model-only (L5). The proposed mechanism is speculative, since the disease is immune-mediated and biperiden has no known immunomodulatory action. The only local registration is cancelled, and the safety profile includes many anticholinergic cautions.

**To proceed, the following is needed:**
- Mechanism of action data for biperiden, and a clearer mechanistic hypothesis for Rasmussen encephalitis
- Preclinical or case-level evidence of benefit in Rasmussen encephalitis
- Package insert warnings and contraindications, which were not available for this report
- Clarification of the Philippines regulatory status, since the only registration is cancelled and no dosage form or approved indication is recorded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

