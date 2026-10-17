---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Hypertension, atrial fibrillation, hypertrophic cardiomyopathy…"
monitor_inn: "Propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
---

# Propranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Propranolol: From Hypertension and Cardiac Arrhythmias to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker, originally used for hypertension, atrial fibrillation, hypertrophic cardiomyopathy and infantile hemangioma-related conditions.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only signal, and the other top-ranked predictions are also thinly supported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, hypertrophic cardiomyopathy, hemangioma and related vascular conditions (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propranolol is a non-selective beta-adrenergic blocker with established use in cardiovascular disease. It lowers heart rate and contractility, and it also has an anti-angiogenic effect in infantile hemangioma.

For distal myopathy, Tateyama type, **no mechanistic link is supported by the data compiled for this report**. This is a rare distal myopathy reported to involve CAV3 variants, and nothing connects beta-blockade to its pathophysiology. The high score (0.994) reflects a knowledge-graph prediction only. It should be treated as a computational signal until shown otherwise.

Notably, the knowledge graph lists myopathy, muscular disease and skeletal muscle disease among propranolol's **contraindications**, which runs counter to this prediction.

### Other Top-Ranked Predictions (for context)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | No trials or literature; no evident mechanistic link |
| 3 | Hypertrophic cardiomyopathy due to intensive athletic training | 99.17% | L5 | Indirect plausibility via the existing HCM indication; athletic remodeling is physiological and generally not treated |
| 4 | Chondroma | 99.14% | L5 | No trials or literature; any link is speculative |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L4 | 3 observational reports with mixed signals (see below) |
| 6 | Cardiomyopathy | 99.12% | L3 | Largely overlaps with the existing HCM indication |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (distal myopathy, Tateyama type), or for any of the other five predictions listed above.

---

## Literature Evidence

Currently no related literature is available for the top-ranked prediction. The literature below relates to the lower-ranked predictions and is shown for context only.

**Cirrhotic cardiomyopathy (rank 5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Cohort/Observational (inferred from title) | Frontiers in Pharmacology | Suggests propranolol can correct prolonged QT intervals in patients with cirrhosis |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Observational (inferred from title) | PLoS One | Examined the effect of propranolol infusion on cardiac function across degrees of cirrhosis; blunted cardiovascular effects of beta-blockers, related to severity |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Observational (inferred from title) | Journal of Hepatology | Non-selective beta-blockers impaired circulatory homeostasis and renal function in refractory ascites |

**Cardiomyopathy (rank 6): selected studies**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical physiologic study | European Heart Journal | Effects of propranolol and verapamil on diastolic stiffness in hypertrophic cardiomyopathy (9 patients on propranolol) |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical hemodynamic study | British Heart Journal | Nifedipine plus propranolol appeared superior to nifedipine alone in 12 patients with hypertrophic obstructive cardiomyopathy |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical study | American Journal of Cardiology | Propranolol and arrhythmia in hypertrophic cardiomyopathy |
| [39355927](https://pubmed.ncbi.nlm.nih.gov/39355927/) | 2024 | Preclinical/Mechanistic | Circulation | Role of the RIα subunit of PKA in cardiac contractility and heart failure development |
| [28431779](https://pubmed.ncbi.nlm.nih.gov/28431779/) | 2017 | Review/Drug monograph | Profiles of Drug Substances, Excipients, and Related Methodology | General propranolol monograph covering hypertension, arrhythmias and hypertrophic cardiomyopathy |

Many other entries retrieved for this prediction are general "Propranolol" monographs with little evidential value.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0402 | Propranolol | Not specified | Not specified (status: cancelled) |

The only registration found has been cancelled, so there is currently no valid marketed product in the Philippines.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from graph relationships, not label text): bronchitis, anxiety and neurotic disorders, kidney disease, liver disease, pancreatitis, gallbladder disease, systemic lupus erythematosus, **myopathy, muscular disease and skeletal muscle disease**, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, gout and hyperuricemia, hyperparathyroidism, hepatic coma and encephalopathy, anuria, hypercalcemia, nephrocalcinosis, myasthenia gravis, and others.
- **Drug Interactions** (100 interactions identified; examples shown):
  - **Major:** Epinephrine
  - **Moderate:** hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, bupropion, morphine, atropine, hyoscyamine, methscopolamine, cimetidine, canagliflozin, chlorpropamide, lorcaserin, calcium salts
  - **Minor:** ascorbic acid, acetylsalicylic acid, magnesium oxide
- **Disease-specific concern:** In advanced cirrhosis, reports describe blunted cardiovascular effects and impaired circulatory and renal function with non-selective beta-blockers.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, distal myopathy, Tateyama type, rests only on a knowledge-graph score. It has no trials, no literature and no plausible mechanism, and the graph itself lists muscle disease as a contraindication. The only predictions with some supporting literature (cirrhotic cardiomyopathy and cardiomyopathy) either carry mixed safety signals or largely overlap with an existing indication. The sole Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data to assess any link between beta-blockade and the predicted disease
- Package insert warnings and contraindications for safety screening
- Preclinical or case-based evidence that beta-blockade affects CAV3-related or other myopathy pathology, and review of the myopathy contraindication signal
- For cirrhotic cardiomyopathy as an alternative research question: full-text review of the three observational studies and a benefit-risk analysis by disease severity
- Clarification of the regulatory and supply pathway in the Philippines, since no valid registration exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

