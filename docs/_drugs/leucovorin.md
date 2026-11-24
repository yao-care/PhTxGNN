---
layout: default
title: Leucovorin
parent: Model Prediction Only (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Leucovorin: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Megaloblastic anemia"
monitor_inn: "Leucovorin"
predicted_indications: ["primary hyperoxaluria", "congenital intrinsic factor deficiency"]
---

# Leucovorin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Leucovorin: From Megaloblastic Anemia to Primary Hyperoxaluria
{: .text-alpha }

## One-Sentence Summary

Leucovorin (folinic acid) is a reduced folate originally used for megaloblastic anemia.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Megaloblastic anemia |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for leucovorin: "High-Dose Methotrexate Therapy Leucovorin is a mixture of the diastereoisomers of the 5-formyl derivative of tetrahydrofolic acid (THF). The biologically active compound of the mixture is the (-)- l isomer, known as Citrovorum factor or (-)-folinic acid." ([DailyMed: Vykoura (leucovorin calcium) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d122b875-435e-4e00-b945-7a0546df95c2), label version 2026-03-12; accessed 2026-11-19.) Based on known information, leucovorin is a reduced folate that acts as a cofactor in one-carbon metabolism and bypasses dihydrofolate reductase. Its use in megaloblastic anemia is established, but a mechanistic link to primary hyperoxaluria is not supported by the data compiled for this report.

Primary hyperoxaluria is an inherited disorder of glyoxylate metabolism (AGXT, GRHPR, HOGA1 defects) that causes oxalate overproduction. A folate-related connection is conceivable only through vitamin B6 (pyridoxine)-dependent AGT function or general one-carbon metabolism, and this is speculative. The high TxGNN score is a model output only and has no clinical or literature corroboration.

**A second prediction worth noting:** *congenital intrinsic factor deficiency* (score 0.9934, also L5, Hold). It has a more plausible rationale, because leucovorin is already used in megaloblastic anemia and this condition produces a similar blood picture. However, leucovorin does not correct vitamin B12 deficiency itself and may mask hematologic signs while neurological damage progresses. Standard care is parenteral B12 replacement. This prediction is also unverified.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Calcium Folinate (leucovorin calcium) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindications** (from drug–disease contraindication links, not label text): vitamin B12 deficiency and pernicious anemia. Folate can correct the anemia while neurological damage from B12 deficiency continues.
- **Drug Interactions**: 100 interactions were found in the DDInter database. Those with a graded severity:
  - Pancrelipase: Moderate
  - Sulfasalazine: Minor
  
  Many others (e.g., calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole) have no assigned severity level.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5).

<!-- review:begin ph-lic-20261031-leucovorin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The prediction is supported only by the model score (L5). There are no clinical trials or publications, the mechanistic link is speculative, and the only Philippines registration is cancelled." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The Quick Overview and the PNF entry table under Philippines Market Information show the current number of PNF entries. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-leucovorin-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Literature and trial searches on folate/one-carbon metabolism in primary hyperoxaluria
- Package insert warnings and contraindications
- Confirmation of whether any valid Philippines registration exists or re-registration is feasible
- For congenital intrinsic factor deficiency, a review of the risk of masking B12 deficiency and of how leucovorin would fit alongside standard B12 therapy

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "There are no clinical trials or publications, the mechanistic link is speculative, and the only Philippines registration is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vykoura (leucovorin calcium) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d122b875-435e-4e00-b945-7a0546df95c2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

