---
layout: default
title: Hydrocortisone
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydrocortisone: predicted new indication Alopecia areata (evidence level L5). Approved use: Adrenocortical insufficiency, Addison disease, autoimmune disease…"
monitor_inn: "Hydrocortisone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "idiopathic steroid-sensitive nephrotic syndrome"]
---

# Hydrocortisone
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

# Hydrocortisone: From Adrenocortical Insufficiency and Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a corticosteroid used for adrenocortical insufficiency, autoimmune and inflammatory conditions such as Crohn disease, and several other diseases.
The TxGNN model predicts it may be effective for **alopecia areata**, with **1 clinical trial** and **about 20 publications** compiled, most of them old case series or case reports.
The only trial used hydrocortisone as the weaker comparator, so it does not show that hydrocortisone itself works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical insufficiency, Addison disease, autoimmune disease, Crohn disease and inflammatory bowel disease, and others (the Philippines registration has no indication text) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 by the formal rule (one completed Phase 3 RCT), but effectively weaker because hydrocortisone was the comparator arm and the trial was small |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, hydrocortisone is a corticosteroid that suppresses inflammation and immune activity. Its efficacy in autoimmune and inflammatory diseases is established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is a T-cell-mediated autoimmune disease in which the immune system attacks hair follicles. This overlaps with the autoimmune and inflammatory conditions hydrocortisone is already used for, and it explains the high TxGNN score. Historical reports from the 1950s to 1970s describe hair regrowth after intralesional hydrocortisone injection, but these were uncontrolled.

There is an important caveat. In the one randomized trial, hydrocortisone 1% cream was the low-potency comparator against clobetasol propionate 0.05%. That design shows relative efficacy, probably in favor of clobetasol, and does not show that hydrocortisone is effective on its own. Higher-potency corticosteroids are the more plausible choice for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomized trial of clobetasol propionate 0.05% cream vs hydrocortisone 1% cream in children with alopecia areata (2002–2003). Hydrocortisone was the active control, and the small sample limits conclusions about its absolute efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Clobetasol 0.05% vs hydrocortisone 1% for alopecia areata in children (published report of the trial above) |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | J Am Acad Dermatol | Four cases of congenital alopecia areata treated with minoxidil and a range of topical therapies |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Historical clinical series | Medical Times | Treatment of alopecia areata with cortisone, hydrocortisone and analogs |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case series | Der Hautarzt | Hair regrowth in alopecia areata after intracutaneous hydrocortisone injection |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review | J Med Soc New Jersey | Clinical overview of alopecia areata and other common scalp problems |
| [19289325](https://pubmed.ncbi.nlm.nih.gov/19289325/) | 2009 | Case report | Endocr Pract | Alopecia universalis in a patient with autoimmune polyglandular syndrome type 3 |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0232 (cancelled) | Hydrocortisone | Not specified | Not specified |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links hydrocortisone to possible contraindications in hypertension, epilepsy, gastric ulcer, kidney disease, liver disease, gallbladder disease, hyperglycemia, and several viral or infectious conditions (anogenital HPV infection, common wart, measles, herpes simplex keratitis). It also flags pituitary and growth hormone deficiency disorders.
- **Drug Interactions:** A total of 100 interactions were found. Among those listed, **adalimumab** is rated Major. Many others are Moderate, including zidovudine, isotretinoin, acarbose, acebutolol, acetazolamide, ketorolac, nifedipine, ibuprofen, ethinylestradiol, acetohexamide, albiglutide, aldesleukin, alefacept, alemtuzumab, and some vaccines (tetanus toxoid, adenovirus type 4). Formoterol and salbutamol are Minor.

Please also refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single Phase 3 trial used hydrocortisone as the low-potency comparator, so it supports clobetasol rather than hydrocortisone. The remaining literature is mostly uncontrolled and historical. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- A controlled study with hydrocortisone as the investigational arm, or a comparison against a placebo or a higher-potency steroid, in alopecia areata
- A rationale for choosing hydrocortisone over higher-potency corticosteroids already used for alopecia areata
- Mechanism of action data and the package insert warnings and contraindications
- A valid local registration or product pathway, with a suitable dosage form (topical or intralesional) confirmed
- A review of the major interaction with adalimumab and of the disease associations listed above

**Other predicted indications:** The remaining nine predictions (alopecia mucinosa, telogen effluvium, folliculitis decalvans, and others) are all rated Hold. They rest on model prediction or weak case-level evidence. The antibody deficiency and nephrotic syndrome predictions mainly reflect hydrocortisone's existing role in replacement or adrenal support, not a new indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

