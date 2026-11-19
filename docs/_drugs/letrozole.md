---
layout: default
title: Letrozole
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
monitor_inn: "Letrozole"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Letrozole: predicted new indication Nipple carcinoma (evidence level L5). In the Philippines: 1 PNF entry"
---

# Letrozole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Letrozole: Nipple carcinoma
{: .text-alpha }

## One-Sentence Summary

Letrozole is an aromatase inhibitor, a hormone-modulating drug that lowers estrogen production.
The TxGNN model predicts it may be relevant for **nipple carcinoma**, but no clinical trials are registered and the 8 publications found are case reports and reviews that do not test letrozole in this disease. The evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nipple carcinoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for letrozole: "The growth of some cancers of the breast is stimulated or maintained by estrogens. Treatment of breast cancer thought to be hormonally responsive (i.e., estrogen and/or progesterone receptor positive or receptor unknown) has included a variety of efforts to decrease estrogen levels (ovariectomy, adrenalectomy, hypophysectomy) or inhibit estrogen effects (antiestrogens and progestational agents). […] Letrozole is a nonsteroidal competitive inhibitor of the aromatase enzyme system; it inhibits the conversion of androgens to estrogens." ([DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406), label version 2026-06-11; accessed 2026-11-19.) Letrozole belongs to the aromatase inhibitor class, which blocks the conversion of androgens to estrogens. This is the general rationale for using it in estrogen-driven tumours.

If a nipple carcinoma is hormone-receptor-positive, aromatase inhibition is plausible by extension from breast carcinoma. This remains a hypothesis. The publications gathered concern rare breast tumour case reports (for example solid papillary carcinoma in situ of the nipple, accessory breast cancer, tall cell carcinoma). None of them tests letrozole in nipple carcinoma, and some involve unrelated entities.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33120755](https://pubmed.ncbi.nlm.nih.gov/33120755/) | 2020 | Cohort/case report | Medicine | Neoadjuvant endocrine therapy in poorly differentiated neuroendocrine carcinoma of the breast; a rare cancer with no standard treatment |
| [41607681](https://pubmed.ncbi.nlm.nih.gov/41607681/) | 2026 | Case report | Clinical Case Reports | Nipple-originating solid papillary carcinoma in situ in a 73-year-old woman; diagnostic and treatment evidence is limited |
| [34495428](https://pubmed.ncbi.nlm.nih.gov/34495428/) | 2021 | Case report | Surgical Case Reports | Rare accessory breast cancer in the inframammary region |
| [40395253](https://pubmed.ncbi.nlm.nih.gov/40395253/) | 2025 | Case report | Cureus | Axillary recurrence in breast cancer presenting with bloody nipple discharge |
| [39682607](https://pubmed.ncbi.nlm.nih.gov/39682607/) | 2024 | Case report | Diagnostics (Basel) | Synchronous metastatic infra-mammary accessory breast cancer and ipsilateral breast cancer |
| [42040393](https://pubmed.ncbi.nlm.nih.gov/42040393/) | 2026 | Case report | Clinical Case Reports | Tall cell carcinoma of the breast with reverse polarity and IDH1 R132 mutation |
| [42305961](https://pubmed.ncbi.nlm.nih.gov/42305961/) | 2026 | Case report | Frontiers in Medicine | Synchronous accessory breast cancer, papillary thyroid carcinoma and nasal papilloma |
| [42416948](https://pubmed.ncbi.nlm.nih.gov/42416948/) | 2026 | Case report | Cureus | Ultrasound findings in florid lobular carcinoma in situ |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Letrozole | Oral, Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified. The only one with a stated severity is aprepitant (Moderate). Others, whose severity is not classified, include calcitriol, glimepiride, lansoprazole, dolasetron, granisetron, famotidine, acetylsalicylic acid, pantoprazole, morphine, metformin, omeprazole, rosiglitazone, simvastatin and prednisone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. No study tests letrozole in nipple carcinoma, and the literature consists of case reports, some about unrelated entities. The prediction rests on the model score of 0.9976 alone.

**To proceed, the following is needed:**
- Studies or case series that directly assess aromatase inhibition in nipple carcinoma, including hormone-receptor status
- Package insert warnings and contraindications for the Philippines licence
- Mechanism of action data
- A safety plan covering the listed drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

