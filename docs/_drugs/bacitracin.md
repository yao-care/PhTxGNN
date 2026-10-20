---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "Bacitracin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical polypeptide antibiotic, originally used for eye infections such as keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bacitracin is a topical polypeptide antibiotic with activity mainly against Gram-positive bacteria. Its use in ocular infections has been established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis if a bacterial component is present.

The predicted indication is closely related to the original ones (keratitis and keratoconjunctivitis), so the very high TxGNN score most likely reflects proximity to those indications in the knowledge graph rather than independent evidence.

There is an important caveat: punctate epithelial keratoconjunctivitis is frequently viral (e.g., adenoviral) or non-infectious, and an antibacterial would have limited benefit in those cases.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the predicted indication.

For reference, among other lower-ranked predictions, otitis externa has a small body of indirect literature (a 2007 double-blind trial of a polymyxin B + bacitracin ointment, older clinical reports, and a veterinary in vitro susceptibility study). This does not support the lead prediction.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0038 | Bacitracin | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so there is currently no valid marketed product in the Philippines.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The knowledge graph links bacitracin to contraindications in several areas:
  - Eye conditions: herpes simplex virus keratitis, viral eye infection, fungal infection of eye, open-angle glaucoma, ocular hypertension
  - Organ disease: kidney disease, liver disease, gallbladder disease
  - Neuromuscular and metabolic conditions: myasthenia gravis, epilepsy, diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency
  - Cardiac conduction: atrioventricular block
  - Other: respiratory failure, peripheral vascular disease, skin atrophy
  These should be verified against the official label.
- **Drug Interactions**: 84 interactions were identified. **Major** ones include:
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Deferasirox
  - Iodinated contrast agents: diatrizoate, iodipamide, iodixanol, iohexol

  Moderate ones include vancomycin, exenatide and the aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine). Many of these are relevant mainly to systemic use, given the nephrotoxicity and neurotoxicity concerns.

Package insert warnings and contraindications could not be obtained. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the high score likely reflects closeness to the original ophthalmic indications rather than new evidence. Many cases of this condition are viral or non-infectious, where an antibacterial is unlikely to help. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism of action data
- Clinical or literature evidence for bacitracin in punctate epithelial keratoconjunctivitis, including how often a bacterial cause is involved
- Clarification of the regulatory status and available ophthalmic formulations in the Philippines
- Of the other predictions, otitis externa (L4, indirect evidence mainly from combination products) may be the most promising for further study as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

