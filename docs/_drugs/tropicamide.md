---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting anticholinergic eye drop, originally used to produce cycloplegia (temporary paralysis of focusing muscles) and pupil dilation for eye examinations.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tropicamide is a muscarinic receptor antagonist. Pharmacology records list it as acting on the M2, M3, M4 and M5 receptors. It is used as a short-acting mydriatic to allow better examination of the lens, vitreous humor and retina.

Cauda equina syndrome can cause bladder dysfunction, such as detrusor overactivity or urinary retention. Antimuscarinic drugs are sometimes used to control such symptoms, which gives the prediction a loose mechanistic basis.

The link is speculative, however. Tropicamide is only used topically in the eye, and no systemic or urological use is documented. Cauda equina syndrome is a surgical emergency whose main treatment is decompression. A symptomatic anticholinergic would not address the underlying condition. The high model score (0.995) is the only support.

**Other predictions in the data (all L5, all Hold):**
- **Obsolete neurogenic bladder** (score 99.13%): Antimuscarinics such as oxybutynin and tolterodine are standard therapy, but tropicamide has no clinical data here and no oral or intravesical formulation. The disease term is also obsolete in the ontology.
- **Irritable bowel syndrome** (score 99.12%): Antispasmodic anticholinergics are used for IBS cramping, but there is no evidence for tropicamide itself, and established alternatives exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0501 | Tropicamide | Not specified | Not specified (registration cancelled) |

The only registration is cancelled, and no valid single-ingredient or combination registrations exist.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from model relationship data, not label text):
  - Eye: open-angle glaucoma, angle-closure glaucoma, closed-angle glaucoma, ocular hypertension
  - Cardiovascular: hypertension, hypertensive disorder, myocardial ischemia, coronary artery disease, sudden cardiac arrest, heart conduction disease
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- **Drug Interactions**: 14 records were found. Ten were drug-level interactions, all with an unclassified severity: atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole and brimonidine. The other four are muscarinic receptor targets (M2 to M5). Atropine is another anticholinergic, so additive effects are plausible, but this has not been verified.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5). Tropicamide is a topical ophthalmic agent with no documented systemic or urological use. Its only Philippines registration is cancelled. Established antimuscarinic alternatives exist for the bladder and bowel indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Evidence of efficacy, such as preclinical or clinical data, in the predicted indication
- Assessment of whether a suitable systemic or intravesical formulation could exist
- Comparison against established antimuscarinic therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

