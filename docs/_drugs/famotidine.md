---
layout: default
title: Famotidine
parent: Model Prediction Only (L5)
nav_order: 137
evidence_level: L5
indication_count: 4
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-10-30
description: "Famotidine: predicted new indication duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Famotidine
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

## Famotidine: H2-receptor antagonist (acid suppression) → duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Famotidine is a drug that reduces stomach acid production. The TxGNN model predicts it may be relevant to **duodenal obstruction**, but there are **no registered clinical trials** and only **2 publications** (both surgical case reports that do not show famotidine efficacy), so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | duodenal obstruction |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this report. Famotidine is generally known as a histamine H2-receptor antagonist that suppresses gastric acid secretion.

The data compiled for this report do not show a clear mechanistic link between acid suppression and duodenal obstruction. Obstruction is a mechanical problem, and reducing acid does not relieve it. The two retrieved publications are surgical case reports (a giant marginal ulcer after gastroenterostomy and duodenal involvement in Crohn's disease). They describe obstruction as a complication of ulcer or inflammatory disease, and they do not support famotidine as a treatment. The high score most likely reflects the model's closeness to ulcer-related diseases rather than a true therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Case report | Surgical Endoscopy | Giant marginal ulcer, a complication of gastroenterostomy, which can cause obstruction among other problems; no famotidine efficacy data |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Case report (surgical) | Surgery Today | Duodenal Crohn's disease with persistent gastric outlet obstruction treated surgically; no famotidine efficacy data |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0185 | Famotidine | Not recorded | Not recorded |

## Safety Considerations

- **Disease conditions flagged for caution in the compiled data:** kidney disease and impaired renal function, liver disease, gallbladder disease, nephrolithiasis, hypercalcaemia and other calcium or phosphorus disorders, diarrhoeal disease, constipation, and gastric cancer or gastric neoplasm. These come from database relations, not from label text, so they need confirmation against the package insert.
- **Drug Interactions:** 100 interactions were found in the interaction database. Examples among those listed include Moderate-level interactions with abiraterone, acalabrutinib, tramadol, amiodarone, amitriptyline, aripiprazole and salbutamol, and Minor-level interactions with alendronic acid and aluminium hydroxide.

Package insert warnings and contraindications are not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting studies. The only literature is two surgical case reports that do not address famotidine treatment, and acid suppression has no plausible effect on mechanical duodenal obstruction.

**To proceed, the following is needed:**
- Any clinical or preclinical study directly testing famotidine in duodenal obstruction
- Detailed mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of the dosage form and approved indication for the local registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

