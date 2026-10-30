---
layout: default
title: Mycophenolic Acid
parent: Model Prediction Only (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Mycophenolic Acid: predicted new indication Hemoglobinopathy (evidence level L3). Approved use: Not available in the registration data"
monitor_inn: "Mycophenolic acid"
predicted_indications: ["hemoglobinopathy", "migraine disorder", "migraine with brainstem aura", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "pyropoikilocytosis, hereditary", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells", "rheumatoid arthritis", "antithrombin deficiency type 2"]
---

# Mycophenolic Acid
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

## Mycophenolic Acid: From an Immunosuppressant to Hemoglobinopathy
{: .text-alpha }

## One-Sentence Summary

Mycophenolic acid is an immunosuppressant that inhibits lymphocyte proliferation. Its original approved indication is not recorded in the Philippine registration data compiled for this report.
The TxGNN model predicts it may be useful for **hemoglobinopathy**, but the evidence is thin: **1 indirectly related clinical trial** and **1 pharmacokinetic study** (mycophenolate mofetil, a prodrug of mycophenolic acid, in pediatric thalassemia patients undergoing stem cell transplantation).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled drug record. From the supporting literature, mycophenolic acid inhibits inosine monophosphate dehydrogenase (IMPDH), an enzyme needed for guanine nucleotide synthesis. This suppresses the proliferation of T and B lymphocytes.

Hemoglobinopathies such as thalassemia are not directly treated by this mechanism. The plausible link is indirect. Patients with thalassemia major who receive allogeneic stem cell transplantation are at risk of graft-versus-host disease (GVHD), and mycophenolate is a common component of GVHD prevention. A 2025 pharmacokinetic study explored off-label dosing in this population. This supports the idea that the drug is used *around* the disease (in transplant care), not that it treats the underlying blood disorder.

The very high TxGNN score should therefore be read as a computational signal, not as proof of benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | Completed | 205 | Basiliximab for preventing acute GVHD in unrelated allogeneic stem cell transplantation for thalassemia major. Mycophenolic acid is not the tested intervention, so relevance is indirect. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Cohort | Eur J Drug Metab Pharmacokinet | Population pharmacokinetic model and dosing recommendations for off-label mycophenolate mofetil in pediatric thalassemia patients undergoing stem cell transplantation. It addresses dosing, not efficacy. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0335 | Mycophenolic Acid | Not recorded | Not recorded (registration valid) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Those listed below are from the first 20 reviewed.
  - **Major**: Activated charcoal
  - **Moderate**: Doxycycline, amoxicillin, clarithromycin, minocycline, tetracycline, levofloxacin, metronidazole, vancomycin, kanamycin, paromomycin, and antacids/minerals (magnesium oxide, magnesium hydroxide, magnesium carbonate, magaldrate, aluminum hydroxide, calcium carbonate)
  - **Minor**: Zinc sulfate, zinc acetate, iron

  Many of these are antibiotics and mineral-containing products, which may alter absorption or gut-flora-dependent handling of the drug.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The link to hemoglobinopathy is indirect. The only related trial tests a different drug (basiliximab), and the only related publication is a dosing study of the prodrug in transplant patients. There is no efficacy evidence for treating the blood disorder itself. The product is also no longer validly registered in the Philippines.

**To proceed, the following is needed:**
- Efficacy and safety data for mycophenolate-based GVHD prophylaxis specifically in thalassemia or other hemoglobinopathy transplant populations
- Clarification of the original approved indication and mechanism of action data
- Package insert warnings and contraindications, which are needed before any safety screening
- Review of the regulatory status, since the only Philippine registration (PNF-0335) is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

