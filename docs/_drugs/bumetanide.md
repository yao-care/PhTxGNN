---
layout: default
title: Bumetanide
parent: Moderate Evidence (L3-L4)
nav_order: 52
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-15
description: "Bumetanide: predicted new indication Acute pulmonary heart disease (evidence level L4). Approved use: Congestive heart failure"
monitor_inn: "Bumetanide"
predicted_indications: ["acute pulmonary heart disease"]
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Bumetanide: From Congestive Heart Failure to Acute Pulmonary Heart Disease
{: .text-alpha }

## One-Sentence Summary

Bumetanide is a loop diuretic originally used to treat congestive heart failure and related oedema.
The TxGNN model predicts it may be effective for **acute pulmonary heart disease**,
but currently there are **no registered clinical trials** and only **5 publications** (mostly general reviews of heart failure and diuretics), so this prediction rests mainly on model inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congestive heart failure |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L4 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, bumetanide is a loop diuretic that inhibits the Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb of the loop of Henle. This produces rapid sodium and water excretion, which reduces venous congestion and cardiac preload.

Acute pulmonary heart disease (acute cor pulmonale, for example from massive pulmonary embolism) involves right ventricular overload and systemic congestion. Decongestive diuresis is therefore mechanistically plausible as **supportive therapy**.

There are important caveats. The benefit is indirect: it relieves congestion but does not treat the underlying cause (pulmonary vascular obstruction). Excessive preload reduction may even be harmful in preload-dependent acute right ventricular failure. The very high TxGNN score most likely reflects bumetanide's established heart failure indication and its proximity to related diseases in the knowledge network, not disease-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Small haemodynamic study | Br J Clin Pharmacol | IV bumetanide in 24 patients with coronary artery disease and acute or chronic heart failure: reduced cardiac index and pulmonary artery occluded pressure, but increased systemic blood pressure and vascular resistance |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Bumetanide is a potent loop diuretic for oedema in heart failure, hepatic and renal disease and acute pulmonary congestion; rapid onset with diuresis lasting 3–6 hours |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews treatment options for acute heart failure; most patients can be managed effectively with diuretics |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Compares pharmacokinetics, safety, efficacy and cost of loop diuretics, asking whether furosemide should be first line |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohort | Am J Emerg Med | Epidemiology of heart failure presentations to US emergency departments, 2016–2023; background data, not specific to bumetanide |

None of these publications directly studies bumetanide in acute pulmonary heart disease.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0060 | Bumetanide | Not specified | Not specified (status: valid) |

---

## Safety Considerations

- **Contraindications (not taken from package insert text; may reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence)**: liver disease, gallbladder disease, thrombocytopenia, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, hepatic coma, hepatic encephalopathy, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hearing disorders and auditory system disease.
- **Drug Interactions**: The interaction screening returned 100 interacting drugs; 20 are shown in the compiled data, and most are Moderate. Examples include:
  - Antidiabetic drugs (acarbose, alogliptin, albiglutide, metformin, acetohexamide)
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone)
  - Amphotericin B formulations
  - Proton pump inhibitors (omeprazole, rabeprazole)
  - Bupropion, morphine and bisacodyl

  Minor interactions were noted with doxycycline and acetylsalicylic acid.
- Package insert warnings were not obtained. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model-level support (Evidence Level L4): no clinical trials and no literature specific to acute pulmonary heart disease. The mechanism is plausible only as indirect decongestive support, and over-diuresis could harm patients with preload-dependent right ventricular failure. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Disease-specific clinical evidence (trials or observational studies) of bumetanide in acute cor pulmonale or acute right heart failure
- Clarification of the regulatory pathway, since the existing registration is cancelled
- Route and formulation compatibility assessment (IV availability is likely needed for acute settings)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

