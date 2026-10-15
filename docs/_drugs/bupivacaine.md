---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Bupivacaine: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a local amide anesthetic. In the knowledge graph used for this report, its original indication is recorded as dermatitis.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text in the local registration record) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Generally, bupivacaine is known as a local amide anesthetic that blocks voltage-gated sodium channels. Its recorded original indication here (dermatitis) likely reflects a symptomatic, skin-related association rather than a disease-modifying effect.

Acrodermatitis chronica atrophicans is the late skin stage of Lyme borreliosis and is treated with antibiotics. A local anesthetic has no plausible role in treating the underlying infection. The high score (0.992) is most likely driven by the drug's link to dermatitis in the knowledge graph, and no clinical or literature evidence supports it.

Other top predictions show the same pattern, and none has trial or literature support:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Neonatal dermatomyositis | 99.15% | L5 | No disease-modifying mechanism. At most symptomatic or procedural analgesia. Neonatal use raises cardiotoxicity and systemic toxicity concerns. |
| 3 | Secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.11% | L5 | No anti-inflammatory or antifibrotic action. The score likely reflects network proximity to related diseases. |
| 4 | Amyopathic dermatomyositis | 99.03% | L5 | Predominantly a cutaneous, immune-mediated disease. Bupivacaine could at best relieve symptoms such as pain or pruritus. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0061 | Bupivacaine | Not specified | Not specified (status: cancelled) |

There is currently no valid registration for bupivacaine in the Philippines according to the data compiled for this report.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease contraindication edges, not package insert text): hypertensive disorder, hypertension, hypotensive disorder, liver failure, liver disease, kidney disease, gallbladder disease, epilepsy, COPD (including severe early-onset), respiratory failure, hypothyroidism, myxedema, congenital hypothyroidism, inflammatory bowel disease, potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, atrial fibrillation, coronary artery disease, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, hemoglobinopathy, substance abuse/dependence, pyoureter, and angle-closure glaucoma.
- **Drug Interactions**: 56 interactions were found in total. Those with a stated severity are **moderate**: aprepitant and liposomal morphine. The others are listed without a severity grade, including pantoprazole, omeprazole, lansoprazole, vancomycin, atropine, corticosteroids (triamcinolone, prednisone, prednisolone, hydrocortisone, dexamethasone), simvastatin, potassium chloride, ranitidine, famotidine, ondansetron, metoclopramide, metronidazole and naloxone.
- Package insert warnings and contraindications could not be obtained. Please refer to the package insert for full safety information.
- Neonatal use (relevant to the neonatal dermatomyositis prediction) would require special attention because of systemic and cardiac toxicity risks.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions rest on model scores alone (L5), with no clinical trials or publications. No plausible disease-modifying mechanism links a local anesthetic to the predicted conditions. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Evidence that the prediction has real clinical meaning (for example, a symptomatic benefit such as local analgesia, rather than treatment of the underlying disease)
- Clarification of the current registration status and available dosage forms and routes in the Philippines
- A review of the knowledge-graph contraindication list against official labelling before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

