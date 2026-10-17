---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Carvedilol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carvedilol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a beta-blocker with additional alpha-1 blocking activity, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials** and **no relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carvedilol combines beta-blockade with alpha-1 blockade, which lowers blood pressure. Its efficacy in hypertension is established, so lowering blood pressure is mechanistically plausible in hypertensive renal disease.

However, this predicted indication is essentially an extension of the original hypertension indication, not a distinct repurposing signal. Malignant hypertension with kidney involvement is usually managed with intravenous agents and blockade of the renin-angiotensin system, and there is no direct support for carvedilol in this setting. The high TxGNN score (0.995) is a computational prediction only.

Other predicted indications (all L5 unless stated):
- **Malignant renovascular hypertension** (99.55%): beta-blockade reduces renin release, which is a theoretical rationale. It is again close to the labeled use and adds little novelty.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.54%): the possible link is modulation of sympathetic overactivation and right ventricular remodeling, but beta-blockers are controversial in pulmonary hypertension because they may reduce cardiac output and exercise tolerance.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.54%, L4): this is the only alternative with some indirect preclinical evidence (see below).
- **Braddock syndrome** (99.37%): no clear mechanistic link was identified.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication or any of the other predictions.

## Literature Evidence

No literature was retrieved for the top-ranked indication (malignant hypertensive renal disease). The only literature came from rank 4, pulmonary hypertension owing to lung disease and/or hypoxia. It is indirect, mostly preclinical, and not efficacy evidence in patients. Several retrieved papers are off-topic and are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Animal study | Eur J Pharmacol | Carvedilol reversed hypertension induced by chronic intermittent hypoxia in rats |
| [20508210](https://pubmed.ncbi.nlm.nih.gov/20508210/) | 2010 | Animal study | Am J Respir Crit Care Med | Adrenergic receptor blockade reversed right heart remodeling and dysfunction in pulmonary hypertensive rats |
| [16639551](https://pubmed.ncbi.nlm.nih.gov/16639551/) | 2006 | Animal study | Pflugers Arch | Carvedilol inhibited right ventricular hypertrophy induced by chronic hypobaric hypoxia |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Reviews respiratory effects of beta-blockers in heart failure; relevant to pulmonary safety, not efficacy |
| [24798657](https://pubmed.ncbi.nlm.nih.gov/24798657/) | 2014 | Crossover study (11 patients) | J Clin Hypertens | Compared nighttime nifedipine vs carvedilol on sleep blood pressure in hypertensive patients with sleep apnea |
| [25187802](https://pubmed.ncbi.nlm.nih.gov/25187802/) | 2014 | In vitro study | Exp Ther Med | Carvedilol reduced cardiomyocyte apoptosis after simulated ischemia/reperfusion via the TLR4/NF-κB pathway |
| [28862654](https://pubmed.ncbi.nlm.nih.gov/28862654/) | 2017 | Review | Nutrients | Antioxidant strategies for cardiovascular conditions associated with oxidative stress |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0080 | Carvedilol | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver failure, asthma (including intrinsic and allergic), bronchitis, pulmonary emphysema and other bronchial disease, diabetes mellitus and diabetic ketoacidosis, hypotensive disorder, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), atrioventricular block, sick sinus syndrome (including familial), Prinzmetal angina, anaphylaxis, and intraoperative floppy iris syndrome.
- **Drug Interactions** (100 interactions found; examples shown):
  - **Major:** Epinephrine
  - **Moderate:** hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, bupropion, morphine, atropine, hyoscyamine, lorcaserin, canagliflozin, acetohexamide, and several calcium salts
  - **Minor:** acetylsalicylic acid, aluminum hydroxide, attapulgite
- **Respiratory caution:** For the pulmonary hypertension predictions, bronchospasm and reduced exercise capacity would need to be addressed before any clinical step.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or relevant literature. The predicted indication is close to carvedilol's existing hypertension use and is not a distinct repurposing signal. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications
- Clinical or observational evidence of carvedilol in hypertensive renal disease, compared with standard care (IV agents and RAAS blockade)
- Clarification of the regulatory pathway, since there is no valid Philippines registration
- For the pulmonary hypertension predictions, a respiratory safety assessment and human efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

