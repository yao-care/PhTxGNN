---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Etonogestrel: predicted new indication Amenorrhea (evidence level L5). Approved use: Not available"
monitor_inn: "Etonogestrel"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
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

# Etonogestrel: From an Unspecified Original Indication to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin, a hormonal agent whose original approved indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be associated with **amenorrhea**, but there are **0 clinical trials** and only **1 publication** (unrelated to this drug), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only registration has no indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Etonogestrel is a progestin and is known to suppress ovulation and thin the endometrium. This is the general pharmacology of the class, not data from the compiled records.

Amenorrhea is a well-recognised bleeding-pattern outcome of etonogestrel implants. It is an expected effect of contraception rather than a therapeutic indication, so the high model score (0.998) most likely reflects this known effect. It is not evidence that the drug treats amenorrhea. Treating amenorrhea generally means restoring menstruation, whereas etonogestrel tends to cause or maintain its absence.

The other top predictions are benign breast conditions: breast fibrocystic disease (99.61%), apocrine adenosis of breast (99.29%), blunt duct adenosis of breast (99.29%) and benign mammary dysplasia (99.21%). These share one theoretical idea, that progestins may counter estrogen-driven breast tissue proliferation. Hormonal contraceptives have mixed associations with benign breast conditions. The identical scores for the two adenosis conditions suggest they come from a shared neighbourhood in the model's knowledge graph rather than disease-specific evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol | Trials | Study protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia. It does not concern etonogestrel or amenorrhea and is a spurious match. |

No clinical trials are registered for the predicted indication. No relevant literature supports this prediction.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0180 | Etonogestrel | Not specified | Not specified (registration cancelled) |

## Safety Considerations

No package insert warnings or contraindications were available. Please refer to the package insert for safety information.

- **Contraindication signals from the knowledge graph** (these come from the TxGNN knowledge graph, not from label text, and need confirmation against the official label): hypertension, epilepsy, anxiety and neurotic disorders, dysthymic disorder, porphyria, kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridemia, hyperlipidemia, female breast carcinoma, thrombophlebitis, migraine, coronary artery disease and obesity.
- **Drug Interactions**: The interaction query returned 100 records. Those shown are all Moderate and are mostly antidiabetic agents: acarbose, metformin, glimepiride, chlorpropamide, the gliptins (alogliptin, saxagliptin), the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), the GLP-1 agonists (albiglutide, dulaglutide, semaglutide) and several insulins. Aprepitant, clarithromycin and linaclotide were also flagged.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). No clinical trials support it, and the one linked publication is unrelated. Amenorrhea is an expected effect of this drug rather than a treatable condition, and the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- A clear clinical rationale showing whether amenorrhea or a benign breast condition is a therapeutic target rather than an expected effect
- Mechanism of action data (from DrugBank)
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- A literature search specific to etonogestrel and the predicted conditions
- Clarification of the cancelled registration status and the original approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

