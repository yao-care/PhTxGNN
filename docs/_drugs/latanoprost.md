---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Latanoprost: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma, ocular hypertension"
monitor_inn: "Latanoprost"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
---

# Latanoprost
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

## Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Latanoprost was originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with a very high model score.
However, **0 clinical trials** and **0 publications** are currently available in the compiled data, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Latanoprost is a prostaglandin F2-alpha analogue. It lowers intraocular pressure (IOP) by increasing uveoscleral outflow of aqueous humour. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects general pharmacological knowledge of the drug class.

Open-angle glaucoma and hereditary glaucoma are both IOP-driven optic neuropathies, so there is a plausible overlap in how the drug might work. However, primary congenital and juvenile forms often involve developmental defects of the trabecular meshwork. It is not established that increasing uveoscleral outflow would be adequate in those cases.

No trials or literature were found for this specific indication. The high score should be treated as a hypothesis, not as proof of efficacy.

### Other Predicted Indications (for context)

All of the following are supported by model score only, with no trials or literature (Evidence Level L5):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Visceral calciphylaxis | 99.83% | No clear mechanistic link; topical ocular route unlikely to reach relevant tissue |
| 3 | Hypotrichosis simplex of the scalp | 99.81% | Biologically plausible, since prostaglandin analogues stimulate hair growth (eyelash hypertrichosis); structural follicle defects may limit benefit |
| 4–6 | Venous, arterial, neurogenic thoracic outlet syndrome | 99.78%, 99.78%, 99.72% | Mechanical compression disorders; no plausible link. The identical scores for the venous and arterial forms suggest a graph artefact |
| 7 | Congenital hypotrichosis milia | 99.71% | Similar hair-growth rationale, but congenital structural defect may limit benefit |
| 8 | Angiodysplasia of stomach | 99.70% | No plausible link; vasodilation could be unfavourable |
| 9 | Blue toe syndrome | 99.69% | Negligible systemic exposure from topical ophthalmic use |
| 10 | Lymphangiectasis | 99.67% | Speculative link only |

Among these, hypotrichosis (ranks 3 and 7) has the strongest biological rationale after hereditary glaucoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0280 | Latanoprost | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so there is currently no valid marketed product in the Philippines.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, conjunctivitis, and acute contagious conjunctivitis. These indicate that patients with active ocular inflammation or macular oedema need careful assessment.

**Drug Interactions:** The interaction screen returned 100 records, all with an unclassified severity level. The first 20 reviewed include calcitriol, glimepiride, doxycycline, clotrimazole, lansoprazole, cimetidine, atropine, pantoprazole, mesalazine, acarbose, morphine, metformin, omeprazole, sucralfate, rosiglitazone, vancomycin, lactulose, triamcinolone, prednisone and simvastatin. Because severity is unknown, their clinical significance cannot be judged from this data, and they should be checked against a reference source.

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hereditary glaucoma rests on a high model score and a plausible mechanism, but there are no trials or publications. The only Philippine registration is cancelled, and the package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism-of-action data (for example, from DrugBank)
- A literature and trial search for latanoprost in primary congenital and juvenile glaucoma
- Clarification of the regulatory situation, including why the registration was cancelled and whether a valid product is available
- Review of the severity of the drug interaction records
- If hypotrichosis is pursued, a separate assessment of topical formulation and route feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

