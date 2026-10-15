---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Isosorbide Dinitrate: From an Established Nitrate Vasodilator to Alopecia

## One-Sentence Summary

Isosorbide dinitrate is a nitrate vasodilator that releases nitric oxide. The TxGNN model predicts it may be effective for **alopecia**, but **0 clinical trials** and **0 publications** currently support this prediction. The evidence rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Isosorbide dinitrate belongs to the organic nitrate class, which releases nitric oxide and relaxes vascular smooth muscle. Mechanistically, this could improve scalp blood flow, and that is the only theoretical link to hair loss.

No clinical or published evidence supports this link. The very high prediction score is not backed by any data, and the model may be reflecting network proximity to other hair disorders rather than a true therapeutic signal. The original indication is not recorded in the local registration data, so a direct comparison with the new indication cannot be made.

## Clinical Trial Evidence

Currently no related clinical trials registered for alopecia.

## Literature Evidence

Currently no related literature available for alopecia.

## Other Predicted Indications with Evidence

Alopecia is the top-ranked prediction, but two lower-ranked predictions have more supporting data. The other top-10 predictions (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, hypertrichosis, kyphoscoliotic heart disease, visceral calciphylaxis, venous thoracic outlet syndrome) have no trials or literature (L5, Hold).

| Predicted Indication | TxGNN Score | Evidence Level | Supporting Data | Assessment |
|------|------|------|------|------|
| Pulmonary hypertension | 99.98% | L3 | 0 trials; about 19 publications, mostly small, old hemodynamic or animal studies, plus a 2025 bolus study ([39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/)) | Research question. Plausible through the NO–cGMP pathway, but not confirmed in a Phase 2/3 RCT. Risks include worsened V/Q mismatch and hypoxemia in lung disease, and nitrate tolerance. |
| Vascular disease | 99.97% | L2 | 6 trials, including [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) (Phase 3, completed, n=68, ISDN spray plus chitosan in diabetic foot ulcers); about 20 publications | Research question. The category is very broad and overlaps with approved anti-anginal use. Most other listed trials do not test ISDN as the intervention. A specific indication such as diabetic foot ulcer should be assessed separately. |

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0265 | Isosorbide Dinitrate | Cancelled |

There are no currently valid single-ingredient or combination registrations. Dosage form and approved indication text are not recorded for this registration.

## Safety Considerations

- **Key Warnings and Contraindications:** Label-based warnings and contraindications were not available. Please refer to the package insert.
- **Knowledge-graph contraindication signals** (drug–disease links from the TxGNN knowledge graph, not label text): hypotensive disorder, hypertrophic cardiomyopathy, slow acetylation, coronary artery disease, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, hemoglobinopathy and anemia, hyperthyroidism (Graves disease, thyrotoxicosis), pseudotumor cerebri and intracranial hypertension, intracerebral hemorrhage, and Rowell syndrome. These signals need clinical verification before any use.
- **Drug Interactions:** 100 interactions were identified. Moderate-level examples include bupropion, morphine, opium, dronabinol, nabilone, sapropterin, rosiglitazone, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Omeprazole is rated minor. Several others, such as atropine, epinephrine, cimetidine, and amphotericin B, have an unknown severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction has the highest score but no trials, no literature, and only a speculative vasodilation rationale (L5). The product's only Philippines registration is cancelled, and label safety data is unavailable.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking nitrate therapy to hair follicle outcomes
- Mechanism of action data and the package insert warnings and contraindications
- Confirmation of the original approved indication and a current registration status in the Philippines
- Separate evaluation of the better-supported candidates, pulmonary hypertension and a defined vascular indication such as diabetic foot ulcer, ideally with a controlled trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

