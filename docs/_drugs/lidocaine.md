---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-28
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not stated in local licence text. Relations recorded in the knowledge…"
---

# Lidocaine
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

## Lidocaine: From Local Anesthesia and Itch/Pain Conditions to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a local anesthetic whose relations recorded in the knowledge graph include dermatitis, neuralgia, hemorrhoid, scabies and postherpetic neuralgia.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis** (score 0.9999), but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in local licence text. Relations recorded in the knowledge graph (not approved indications): dermatitis, neuralgia, hemorrhoid, postherpetic neuralgia, scabies, and others |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Number of Approvals | 1 registration (PNF-0290) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lidocaine is generally known as a sodium channel blocker with topical anesthetic activity, which could relieve ocular surface pain and discomfort.

The prediction for punctate epithelial keratoconjunctivitis comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no evidence that lidocaine treats the underlying corneal or conjunctival disease.

There is also a concern: topical anesthetics can impair corneal epithelial healing, and prolonged use on a compromised cornea is generally avoided. This makes ocular surface toxicity a real risk for this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

For context, the lower-ranked prediction "conjunctival disorder" has two trials, but they test anesthesia delivery in surgery and do not address the predicted disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine gel vs subconjunctival injection for pain during pterygium excision |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | N/A | Completed | 34 | Two local anesthesia types for postoperative pain in ptosis surgery |

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0290 | Lidocaine | Not specified | Not specified |

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** hypertension, liver failure and liver disease, cirrhosis, epilepsy, kidney disease, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, herpes simplex virus keratitis, atopic dermatitis, osteoporosis, psychotic disorders, fungal infections, gastritis, and others.
- **Drug interactions (100 recorded):** Major: bupropion. Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid, sodium sulfate. Several others are minor or of unknown severity.
- **Ocular surface concern:** topical anesthetics can impair corneal healing, which is directly relevant to this prediction.
- **Other predicted diseases:** a retrieved case report describes methemoglobinemia with topical lidocaine, and a review describes frequent neuropsychiatric side effects with intravenous lidocaine.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials or publications on the disease itself (Evidence Level L5). A plausible benefit would be symptomatic only, and the risk of corneal toxicity with topical anesthetics argues against pursuing it.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic case beyond symptom relief
- Preclinical or clinical studies of lidocaine in punctate epithelial keratoconjunctivitis, including corneal safety
- Package insert warnings and contraindications from DOH-FDA Philippines, along with dosage form and approved indication for PNF-0290
- Confirmation of which ophthalmic routes and formulations are available locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

