---
layout: default
title: Levothyroxine
parent: Moderate Evidence (L3-L4)
nav_order: 208
evidence_level: L3
indication_count: 10
---

# Levothyroxine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Levothyroxine: From Hypothyroidism to Endemic Goiter

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone, originally used to treat hypothyroidism and other thyroid conditions.
The TxGNN model predicts it may be effective for **endemic goiter**,
with **no registered clinical trials** but **20 publications** (mostly 1988–2004 clinical studies and reviews) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (other original indications in the knowledge graph include myxedema, congenital hypothyroidism, goiter, Hashimoto thyroiditis and thyroid cancer) |
| Predicted New Indication | Endemic goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levothyroxine is a thyroid hormone replacement, its efficacy in hypothyroidism is established, and mechanistically it may be applicable to endemic goiter.

Endemic goiter is mainly caused by iodine deficiency. Low iodine raises thyroid-stimulating hormone (TSH), and TSH drives thyroid growth. Levothyroxine suppresses TSH and can reduce thyroid volume. This sits close to levothyroxine's existing thyroid indications, so it is a modest repurposing step.

In practice, the literature suggests iodine alone, or iodine combined with levothyroxine, is generally preferred. Levothyroxine alone leaves the iodine deficiency within the thyroid unchanged, and goiter may relapse after stopping it.

## Clinical Trial Evidence

Currently no related clinical trials registered for endemic goiter.

For reference, the third-ranked prediction (nodular goiter) has two completed trials: [NCT00277589](https://clinicaltrials.gov/study/NCT00277589) (Phase 4, n=1024, TSH-adapted therapy vs placebo) and [NCT00941551](https://clinicaltrials.gov/study/NCT00941551) (n=150, lobectomy with or without postoperative levothyroxine).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2515973](https://pubmed.ncbi.nlm.nih.gov/2515973/) | 1989 | Multicentre randomized trial | Eur J Clin Invest | 166 patients randomized to levothyroxine, iodine, or a combination for 12 months |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Multicenter study | Dtsch Med Wochenschr | 74 patients: levothyroxine alone vs levothyroxine plus iodide for 6 months, then iodide prophylaxis |
| [7900936](https://pubmed.ncbi.nlm.nih.gov/7900936/) | 1993 | Clinical study | Clin Endocrinol | Effect of levothyroxine or iodine on thyroid size and growth-stimulating immunoglobulins |
| [8676600](https://pubmed.ncbi.nlm.nih.gov/8676600/) | 1996 | Clinical study | Klin Padiatr | Adolescents: iodine vs iodine plus levothyroxine, with lipid parameters |
| [9011485](https://pubmed.ncbi.nlm.nih.gov/9011485/) | 1996 | Clinical study | Dtsch Med Wochenschr | Iodide vs levothyroxine in middle-aged and elderly patients |
| [24393641](https://pubmed.ncbi.nlm.nih.gov/24393641/) | 1998 | Supplementation study | Asia Pac J Clin Nutr | 100 µg/day levothyroxine over 1.5 years in an iodine-deficient indigenous population |
| [11256036](https://pubmed.ncbi.nlm.nih.gov/11256036/) | 2001 | Dose comparison | Dtsch Med Wochenschr | Two doses of levothyroxine-iodide combination in euthyroid diffuse goiter |
| [8147031](https://pubmed.ncbi.nlm.nih.gov/8147031/) | 1993 | Review | Z Gesamte Inn Med | Iodine should be part of therapy; levothyroxine alone does not correct intrathyroidal iodine deficiency and relapse is common |
| [1789063](https://pubmed.ncbi.nlm.nih.gov/1789063/) | 1991 | Double-blind clinical study | Acta Endocrinol | Thyroid iodine concentration with iodine alone vs iodine plus levothyroxine |
| [1577353](https://pubmed.ncbi.nlm.nih.gov/1577353/) | 1992 | Observational | Fortschr Med | Goiter responds less well to levothyroxine in the elderly than in younger patients |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0289 | Levothyroxine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): hypertension, pituitary hormone deficiency and hypopituitarism, hypogonadotropic hypogonadism (including Kallmann syndrome), osteoporosis, diabetes mellitus and diabetic ketoacidosis, coronary artery disease, and myocardial infarction.
- **Drug Interactions**: 100 interactions were found, mostly of moderate severity. Main ones include:
  - Antidiabetic drugs: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide, dulaglutide, chlorpropamide
  - Acid suppressants: omeprazole, rabeprazole, dexlansoprazole (cimetidine is minor)
  - Minerals and antacids: calcium acetate, calcium phosphate, magnesium oxide
  - Sympathomimetics: epinephrine, isometheptene, diethylpropion
- **Related safety context from the literature**: long-term TSH suppression carries risks of subclinical hyperthyroidism, bone loss and cardiac effects, including atrial fibrillation.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several clinical studies, including randomized multicentre trials, support levothyroxine for endemic goiter, and the indication is close to its existing thyroid uses. However, the evidence is old (1988–2004), no trials are registered, and iodine alone or iodine plus levothyroxine is generally preferred. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data
- Current clinical trial or recent randomized evidence for endemic goiter
- A decision on regulatory status, since the only Philippines registration (PNF-0289) is cancelled
- A TSH monitoring plan and screening for cardiac, bone, and diabetes comorbidities

**Other predictions in the list:**
- Nodular goiter and nontoxic goiter have comparable or stronger evidence, but levothyroxine suppression has limited efficacy and carries cardiac and bone risks; radioiodine and surgery are often preferred.
- Substernal goiter, lingual goiter and dyshormonogenic goiter are research questions only.
- Renal hypodysplasia/aplasia, bilateral renal agenesis, Potter sequence and Carney complex have no supporting evidence and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

