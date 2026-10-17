---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Acute lymphoblastic leukemia"
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Methotrexate: From Acute Lymphoblastic Leukemia to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is an established antifolate chemotherapy and immunosuppressant, used for acute lymphoblastic leukemia, lymphomas, rheumatoid arthritis and psoriasis.
The TxGNN model predicts it may be effective for **pulmonary blastoma**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (the Philippines registration record has no indication text, so this comes from the drug's known indications) |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, methotrexate is a dihydrofolate reductase (DHFR) inhibitor. It blocks folate-dependent DNA synthesis, so it is most active against rapidly dividing cells. Its efficacy in leukemia and lymphoma is well established.

Pulmonary blastoma is a rare, aggressive lung tumor made of rapidly proliferating cells. In principle, an antifolate could act on it. However, the only support for this link is the high TxGNN score (0.994). There are no trials or publications specific to pulmonary blastoma, so the mechanistic argument is general and untested for this tumor.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0316 | Methotrexate | Not specified | Not specified (status: cancelled) |

The only registration found has been cancelled, so no valid methotrexate product is currently registered in the Philippines.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate class) |
| Myelosuppression Risk | High (leukopenia, thrombocytopenia and anemia are recognized risks; the safety data also lists these as contraindicated conditions) |
| Emetogenicity Classification | Low to moderate (higher at high doses) |
| Monitoring Items | CBC with differential, liver function, renal function (renal clearance is critical for methotrexate), and pulmonary symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please also refer to the package insert warnings and precautions. |

---

## Safety Considerations

- **Conditions flagged as contraindications (from knowledge-graph associations, not label text):** liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, leukopenia, anemia (including macrocytic anemia), interstitial lung disease, pulmonary fibrosis, peptic and gastric ulcer, ulcerative colitis, inflammatory bowel disease, stomatitis, immune system disease, substance abuse/dependence, and pyoureter. Notably, the lung-related items (interstitial lung disease, pulmonary fibrosis) matter for a lung tumor indication.
- **Drug Interactions:** 100 interactions were recorded, and the 20 reviewed include these major ones:
  - Rabeprazole (Major)
  - Amoxicillin (Major)
  - Acetylsalicylic acid (Major)
  
  Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), tetracyclines (doxycycline, tetracycline), clarithromycin, amphotericin B, mesalazine, balsalazide, pioglitazone, acarbose and bupropion.
- Label-based warnings and contraindications from the Philippines package insert were not available. Please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no tumor-specific mechanistic evidence for pulmonary blastoma. The only Philippines registration is cancelled, and methotrexate has significant toxicity, including pulmonary toxicity.

**To proceed, the following is needed:**
- Case reports, series or preclinical data on methotrexate in pulmonary blastoma, or a clear mechanistic rationale for this tumor
- Detailed mechanism of action data (MOA) from a curated source
- The Philippines package insert (warnings and contraindications) and the status of any valid methotrexate registration
- A review of other predicted indications that have more evidence, such as Hodgkin lymphoma and rhabdomyosarcoma (both L2), which may be better candidates to pursue first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

