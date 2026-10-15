---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Cardiac Decompensation (Inotropic Support) to Alopecia

## One-Sentence Summary

Dobutamine is a beta-1 adrenergic agonist inotrope. The original indication is not recorded in the Philippine registration data compiled for this report, but the drug is conventionally used as short-term intravenous cardiac support.
The TxGNN model predicts it may be effective for **alopecia**, but there are **0 clinical trials** and no literature that actually supports this direction. The one publication retrieved concerns minoxidil toxicity in a cat, not dobutamine efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippine registration data |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, dobutamine is a beta-1 adrenergic agonist that increases the strength of heart contraction, and it is used as an intravenous inotrope.

**The prediction is not mechanistically plausible.** Dobutamine has no known effect on hair follicle biology. The high TxGNN score most likely reflects a knowledge-graph artifact: dobutamine shares vasoactive and cardiovascular neighbours with minoxidil, a vasodilator used for hair loss. The only literature hit describes heart failure caused by minoxidil intoxication in a cat. In that report dobutamine was merely used to treat hypotension, so it says nothing about dobutamine treating alopecia.

The other top predictions do not change this picture:
- **Hair disorders** (hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata, hypertrichosis): no mechanistic rationale and no evidence. Alopecia areata is autoimmune, and dobutamine has no relevant immunomodulatory action.
- **Glaucoma** (open-angle, primary hereditary): at most a speculative link, and a systemic short-acting IV drug is poorly suited to chronic eye use.
- **Raynaud disease, headache disorder, migraine disorder**: the retrieved papers are diagnostic, safety or unrelated drug studies and do not show efficacy. Headache is more likely an adverse effect of dobutamine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (alopecia), only one publication was retrieved, and it does not support efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | A cat developed heart failure from minoxidil intoxication; dobutamine was used only to manage hypotension. No evidence of benefit in alopecia. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0152 | Dobutamine | Not recorded | Not recorded (registration status: cancelled) |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease links from the TxGNN knowledge graph, not from product label text): hypertension and hypertensive disorder, potassium deficiency, atrial fibrillation, aortic stenosis (including aortic valve disease and supravalvular aortic stenosis), myocardial infarction and coronary thrombosis, hemoglobinopathy, and hypertrophic cardiomyopathy (including the familial form).
- **Drug interactions**: 100 interactions were found, and the 20 shown in the data are all rated Moderate. They include:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, repaglinide, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin.
  - Incretin therapies: DPP-4 inhibitors (alogliptin, linagliptin), GLP-1 agonists (albiglutide, dulaglutide, liraglutide, semaglutide), and insulins (aspart, degludec).
  - Others: cimetidine, vancomycin, and the anorectics diethylpropion and phentermine.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but it appears to be a graph artifact. There are no clinical trials, no supporting literature, and no plausible mechanism linking dobutamine to alopecia or to any of the other top predictions. The only Philippine registration is cancelled, and the drug is an IV inotrope that is not suited to chronic hair-loss therapy. All predictions remain at evidence level L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence that beta-1 adrenergic signalling affects hair follicle biology
- Detailed mechanism of action data
- The product label warnings and contraindications from the Philippine FDA, and the original approved indication and dosage form of the cancelled registration
- A route-of-administration assessment, since a systemic IV drug would need a different delivery approach for any dermatological use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

