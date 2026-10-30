---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Tranexamic Acid: predicted new indication amenorrhea (evidence level L4). Approved use: Endometriosis (endometriosis of uterus)"
monitor_inn: "Tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Tranexamic Acid: From Endometriosis to amenorrhea
{: .text-alpha }

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic drug. The amenorrhea prediction (score 0.9919) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **amenorrhea**, but this rests on a model score only:
there are **0 registered clinical trials** and **2 review articles** (indirectly related), so direct supporting evidence is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (endometriosis of uterus) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9919 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tranexamic acid is an antifibrinolytic that inhibits plasminogen activation and reduces fibrinolysis-driven endometrial bleeding. Its role in bleeding control is plausible, but its efficacy in the original indication (endometriosis) has not been confirmed by the data compiled for this report.

The link to amenorrhea is **indirect**. Tranexamic acid reduces heavy menstrual bleeding but does not by itself induce amenorrhea (absence of menses). The literature found concerns management of abnormal uterine bleeding and menses suppression or prophylaxis in hematologic cancer patients, where tranexamic acid may be one option for bleeding control. It is not a treatment for amenorrhea as a disease.

The high TxGNN score (0.9919) is a model prediction and is not backed by clinical evidence. The prediction should be read as a bleeding-related signal rather than proof of benefit in amenorrhea.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of drug therapy for abnormal uterine bleeding. Nonhormonal options such as NSAIDs reduce bleeding by 25–35%. Choice depends on cause, bleeding amount, contraception and fertility needs, and menopausal status. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Approach to menses prophylaxis and suppression in pre-menopausal women with hematologic cancer. Notes few comparative data for these therapies in the cancer setting. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0495 | Tranexamic Acid | Not specified | Not specified (registration valid) |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (model-derived associations, not label text): hypertension, anxiety and neurotic disorders, porphyria, liver disease, gallbladder disease, diabetes and hyperglycemia, diabetic ketoacidosis, hyperlipidemia and hypertriglyceridemia, brain edema, breast carcinoma, endometrial cancer and other uterine corpus cancers, thrombophlebitis, migraine, coronary artery disease, obesity, stroke and cerebrovascular disorders.
- **Drug Interactions**: 35 interactions were found, and the data compiled shows 20 of them. Most are rated Major, and the **Major** ones are:
  - Estrogens and hormonal agents: ethinylestradiol, estradiol (including topical), conjugated estrogens (including topical), esterified estrogens, diethylstilbestrol, dienestrol (topical), estrone, estrone sulfate (including topical), estramustine, norethisterone, drospirenone, etonogestrel
  - Procoagulant products: anti-inhibitor coagulant complex, Factor IX complex (human)
  - Carfilzomib
  - **Moderate**: alteplase and anistreplase (thrombolytics)

  Many of the Major interactions involve estrogen or progestogen products, which are the usual choices for menstrual suppression. Any combination in this setting would need careful thrombotic risk assessment.

Please refer to the package insert for label-based warnings and contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials and only two indirectly related reviews. Tranexamic acid reduces bleeding rather than treating amenorrhea, so the mechanistic link is weak. The only Philippines registration is cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Clarify whether the intended use is really amenorrhea or bleeding control and menses suppression, and re-define the target indication accordingly
- Mechanism of action data (e.g., from DrugBank)
- Philippines package insert warnings and contraindications from the DOH-FDA Philippines website
- Clinical evidence, such as controlled studies in the redefined indication
- Review of the regulatory status, since the sole registration is cancelled, and of available dosage forms and routes
- Thrombotic risk assessment, particularly for use alongside hormonal agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

