---
layout: default
title: Imiglucerase
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
monitor_inn: "Imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
description: "Imiglucerase: predicted new indication Hurler syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Imiglucerase: Hurler syndrome
{: .text-alpha }

## One-Sentence Summary

Imiglucerase is a recombinant enzyme replacement therapy originally used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**,
but there are **0 clinical trials** and only **1 general review article** behind this prediction, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, imiglucerase is a recombinant glucocerebrosidase (beta-glucosidase) that breaks down glucosylceramide, and its efficacy in Gaucher disease is established.

Hurler syndrome (MPS I) is a different disease. It is caused by a deficiency of alpha-L-iduronidase, which leads to accumulation of glycosaminoglycans (dermatan and heparan sulfate). Imiglucerase acts on a different enzyme substrate, and nothing in the available data shows that it has activity against these compounds. The only link is that both diseases are lysosomal storage disorders treated with the enzyme replacement therapy (ERT) concept.

The high TxGNN score most likely reflects closeness within the lysosomal disease network rather than a true therapeutic mechanism. A disease-specific ERT (laronidase) already exists for this condition, which makes repurposing imiglucerase hard to justify.

**Other predictions reviewed (all Hold):**
- **Scheie syndrome** (score 0.9929, L4): an attenuated form of MPS I with the same reasoning as above. The only evidence is the same general ERT review, which does not report imiglucerase use in this disease.
- **Benign neoplasm of adrenal gland** (0.9928, L5): no trials or literature, and no identified mechanistic basis.
- **Autosomal ichthyosis syndrome with fatal disease course** (0.9924, L5): there is a theoretical link through glucosylceramide and the skin barrier, but no data. Systemically given imiglucerase is unlikely to reach the epidermis effectively.
- **Cholesteryl ester storage disease** (0.9912, L5): caused by a different enzyme deficiency (lysosomal acid lipase). Sebelipase alfa is the disease-specific ERT.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of enzyme replacement therapy in lysosomal storage diseases. It describes the development of imiglucerase for Gaucher disease and ERT for Fabry disease. It does not report imiglucerase use in Hurler syndrome. |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Imiglucerase | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

No approved indication is recorded for it.

<!-- review:begin ph-lic-20261106-imiglucerase-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Imiglucerase has one registration in the Philippines (PNF-xxxx), and it is **valid**. No dosage form or approved indication is recorded for it. The drug is marketed, with 1 valid licence out of 1." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. "PNF-xxxx" stands for a code an earlier version of this site's software assigned to the record; the PNF has no entry numbers, so the code is not shown. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-imiglucerase-2 -->

## Safety Considerations

- **Drug Interactions**: One interaction was identified, with **miglustat** (Moderate level). Miglustat is also used in Gaucher disease, so combined use needs review.

For other safety information (warnings and contraindications), please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single general review and no clinical trials. The mechanism does not fit, since imiglucerase targets glucosylceramide rather than the glycosaminoglycans that accumulate in Hurler syndrome. An approved, disease-specific therapy already exists.

<!-- review:begin ph-lic-20261031-imiglucerase-1 -->

> **Review correction (2026-10-31)**: Originally stated: "An approved, disease-specific therapy already exists. In addition, the only Philippines registration is cancelled." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-imiglucerase-1 -->

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Preclinical evidence that glucocerebrosidase has any activity on dermatan or heparan sulfate substrates
- Package insert safety information (warnings and contraindications) from the Philippines regulator
- A comparison against laronidase, the approved therapy for MPS I, to show any added value

<!-- review:begin ph-lic-20261106-imiglucerase-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Package insert safety information (warnings and contraindications) from the Philippines regulator / Clarification of the regulatory status of the cancelled registration" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-imiglucerase-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "In addition, the only Philippines registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "Imiglucerase has one registration in the Philippines (PNF-xxxx), and it is **valid**. dosage form or The drug is marketed, with 1 valid lice" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "Clarification of the regulatory status of the cancelled registration" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

