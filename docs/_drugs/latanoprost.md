---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the `txgnn-pipeline` skill for context. Now generating the Evaluation Report from the Evidence Pack.

---

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α analogue (FP receptor agonist) widely used to reduce intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 completed Phase 2 clinical trial** currently supporting this direction; no peer-reviewed literature was retrieved specifically for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (IOP reduction) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Latanoprost is a selective FP (prostanoid F2α) receptor agonist. Its primary mechanism of action is to increase uveoscleral outflow of aqueous humor from the eye, thereby reducing intraocular pressure (IOP). This IOP-lowering effect is the cornerstone of its established use in adult open-angle glaucoma and ocular hypertension.

Primary hereditary (congenital) glaucoma shares the same core pathophysiology: elevated IOP leads to progressive optic nerve compression and, if untreated, permanent vision loss. Because Latanoprost acts directly on the aqueous outflow pathway, its mechanism maps logically onto the disease mechanism driving hereditary glaucoma — making this TxGNN prediction mechanistically intuitive, not merely a statistical coincidence.

There is an important clinical nuance, however. Pediatric and congenital glaucoma subtypes often involve structural maldevelopment of the trabecular meshwork (e.g., goniodysgenesis, Barkan membrane obstruction), which can reduce the drug's IOP-lowering effect compared to adult open-angle disease. Surgical intervention (goniotomy, trabeculotomy) typically remains first-line in this population. Latanoprost may play a meaningful adjunctive role — particularly in eyes refractory to surgery — but disease-subtype-specific clinical data are still limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive efficacy and safety of latanoprost vs. dorzolamide in pediatric glaucoma patients refractory to surgical procedures; provides the most directly relevant clinical dataset for this indication |

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Philippines Market Information

Latanoprost currently has **no registered products** with the Philippine FDA (Food and Drug Administration). No licenses or authorization numbers are on record.

> **Note:** Latanoprost (brand name Xalatan and generics) is approved and widely available in many international markets (US FDA, EMA, Japan PMDA). A regulatory filing pathway for the Philippines would need to be initiated before any formal clinical or commercial use.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (warnings, contraindications, drug interactions) were not available in this Evidence Pack. Philippine FDA package insert data and DrugBank detailed warnings should be retrieved before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial directly investigates prostaglandin analogues including latanoprost in pediatric glaucoma refractory to surgery, and the FP receptor–IOP pathway provides a clear mechanistic rationale for efficacy in primary hereditary glaucoma. However, evidence remains limited to a single small trial (n=37), no supporting literature was retrieved, and structural trabecular abnormalities characteristic of hereditary congenital glaucoma may attenuate drug response compared to adult open-angle disease.

**To proceed, the following is needed:**

- **Safety data**: Retrieve Philippine FDA or WHO-prequalified package insert for warnings, contraindications, and drug interactions (currently a blocking data gap)
- **MOA confirmation**: Pull full DrugBank MOA record to document FP receptor pharmacology formally
- **Pediatric subtype analysis**: Confirm whether NCT01527682 enrolled patients specifically with hereditary/congenital glaucoma subtypes, or broader pediatric open-angle disease — this determines whether evidence grade should be upgraded or maintained
- **Expanded literature search**: Search PubMed using MeSH terms for "latanoprost AND congenital glaucoma" and "prostaglandin analogue AND primary congenital glaucoma" to identify additional supporting evidence
- **Philippine FDA registration pathway**: Assess options for registration, named-patient import, or compassionate use given zero current Philippines licenses
- **Ophthalmology specialist review**: Confirm drug's role as adjunct vs. primary treatment in the context of local clinical practice and pediatric ophthalmology capacity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

