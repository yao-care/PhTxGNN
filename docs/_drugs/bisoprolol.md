---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Bisoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Bisoprolol
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

## Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Bisoprolol is a selective beta-1 blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. It rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, bisoprolol is a selective beta-1 adrenergic blocker. Its efficacy in hypertension is established, and it may lower blood pressure partly by reducing heart rate and cardiac output and by suppressing renin release from the kidney.

Malignant hypertensive renal disease is a severe kidney complication of very high blood pressure. It is therefore closely related to the original indication, and the prediction is biologically plausible. However, it is an extension of the existing hypertension use rather than a new mechanism. In malignant hypertension, management typically relies on parenteral agents and blockade of the renin-angiotensin system, with beta-blockers in a supportive role. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions for this drug are weaker:
- **Pulmonary hypertension** (two forms, score 0.9993): no direct mechanistic rationale, and beta-blockers may be harmful because they can reduce right-ventricular reserve.
- **Braddock syndrome** (score 0.9991): no mechanistic link could be established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top prediction. The only literature retrieved relates to the third-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia, and it is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Effects of beta-blockers on lung function in heart failure patients |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Comparative clinical study | Int J Cardiol | Carvedilol vs nebivolol vs bisoprolol in moderate heart failure (CARNEBI) |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Physiological study | J Am Soc Echocardiogr | Left ventricular adaptation to acute hypoxia, with and without beta-1 blockade |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Physiological study | Med Sci Sports Exerc | Beta-blockade and chemoreflex contributions to exercise capacity |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | In vitro/animal study | Fundam Clin Pharmacol | Bisoprolol protects myocardial cells from ischemia-reperfusion injury via PI3K/AKT/GSK3β |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | In vitro study | Nan Fang Yi Ke Da Xue Xue Bao | Bisoprolol pretreatment on hypoxia/reoxygenation injury in cardiomyocytes |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Animal study | Int Immunopharmacol | Diosmin plus bisoprolol attenuate cobalt chloride-induced cardiotoxicity |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Case report | Hypertens Res | Two cases of pheochromocytoma with tetralogy of Fallot |

None of these studies evaluates bisoprolol in patients with pulmonary hypertension or malignant hypertensive renal disease.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0053 | Bisoprolol | Not specified | Not specified (status: valid) |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The knowledge graph links bisoprolol with contraindications in several conditions, including asthma (intrinsic and allergic), diabetes mellitus and diabetic ketoacidosis, kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, systemic lupus erythematosus, psoriasis, gout, myasthenia gravis, anxiety and dysthymic disorders, and several metabolic disorders (potassium deficiency, hypercalcemia, hyperparathyroidism, phosphorus metabolism disease). These need verification against the official label. Kidney disease is directly relevant to the top predicted indication.
- **Drug Interactions**: 100 interactions were identified; the 20 listed in the compiled data are mostly Moderate, with a few Minor. Moderate examples include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, acetohexamide, and calcium salts. Minor examples include acetylsalicylic acid, aluminum hydroxide, and attapulgite.
- **Concern for pulmonary hypertension**: Beta-blockade may blunt compensatory cardiac output and exercise capacity in hypoxic or right-ventricle-dependent states.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by the computational score (L5), with no registered trials and no direct literature. The top prediction is essentially an extension of the existing hypertension indication, where beta-blockers play a supportive rather than primary role. Other predictions have weak or potentially unfavorable mechanistic links. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Detailed mechanism of action data (e.g., from DrugBank)
- Clinical or observational evidence for bisoprolol in malignant hypertensive renal disease or renovascular hypertension
- Safety review for kidney impairment and, for pulmonary hypertension, right-ventricular function
- Clarification of the registration status and dosage forms in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

