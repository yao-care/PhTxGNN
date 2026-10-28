---
layout: default
title: Mecobalamin
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Mecobalamin"
predicted_indications: ["sclerosing cholangitis", "multiple endocrine neoplasia", "bone Paget disease"]
description: "Mecobalamin: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Mecobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Mecobalamin: Sclerosing cholangitis
{: .text-alpha }

## One-Sentence Summary

Mecobalamin (methylcobalamin, the active form of vitamin B12) has no original indication recorded in the Philippines registration data compiled for this report.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

Two other predictions also scored high, and neither has supporting evidence:
- Multiple endocrine neoplasia (0.9934)
- Bone Paget disease (0.9931)

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mecobalamin is known as an active form of vitamin B12. It takes part in one-carbon metabolism, homocysteine remethylation and methylation reactions, and it may have neuroprotective and anti-inflammatory effects.

A link to cholestatic or immune-mediated bile duct injury is speculative. No direct data supports it, and because the original mechanism of action is missing, mechanistic plausibility cannot be verified. The high score is best treated as a hypothesis-generating signal, not as evidence of efficacy.

For the other two predicted indications, the rationale is weaker:
- **Multiple endocrine neoplasia** is driven by germline mutations (for example MEN1 and RET). No plausible mechanism connects vitamin B12 supplementation to these pathways, so this prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Bone Paget disease** has only an indirect link. Homocysteine and B12/folate status have been loosely associated with bone turnover. Nothing connects mecobalamin to the osteoclast-driven remodeling abnormality of Paget disease, and standard bisphosphonate therapy works through a different mechanism.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0302 | Mecobalamin | Not specified | Not specified (registration status: valid) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (from drug-disease relationships in the TxGNN knowledge graph, not from label text): potassium deficiency disease, chronic atrophic gastritis, and Leber hereditary optic neuropathy.
- **Drug Interactions** (13 recorded):
  - **Moderate:** arsenic trioxide and chloramphenicol.
  - **Minor:** acid-suppressing drugs, namely famotidine, ranitidine, ranitidine (bismuth citrate), cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, and rabeprazole.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has only a model score behind it (Evidence Level L5), with no clinical trials or literature for any of the three top predicted indications.
- The only Philippines registration is cancelled, and neither its original indication nor its dosage form is recorded.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data for mecobalamin, to assess biological plausibility
- A literature and trial search specific to sclerosing cholangitis and vitamin B12 or methylcobalamin
- Clarification of the original approved indication and dosage form, and of why the registration was cancelled
- A route-of-administration and formulation compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

