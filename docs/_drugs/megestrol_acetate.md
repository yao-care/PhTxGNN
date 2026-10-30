---
layout: default
title: Megestrol Acetate
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
description: "Megestrol Acetate: predicted new indication Hereditary breast ovarian cancer syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Megestrol Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Megestrol Acetate: Hereditary breast ovarian cancer syndrome
{: .text-alpha }

## One-Sentence Summary

Megestrol acetate is a synthetic progestin (hormonal agent) that is already linked to endometrial carcinoma as its original indication.
This is essentially the same disease family as the original indication, so it is not true repurposing.
Currently, **1 clinical trial** (a Phase 2 randomized study) and **no publications** specific to this prediction support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hereditary breast ovarian cancer syndrome |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, megestrol acetate is a synthetic progestin. It is thought to act through progesterone receptor signaling, promoting differentiation and suppressing proliferation of hormone-sensitive endometrial tumour cells.

The hormonal rationale is well supported. A randomized Phase 2 trial has also tested megestrol-containing hormonal therapy in advanced or recurrent disease.

This prediction should be read as confirmation of an existing use, not as a new therapeutic area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial of temsirolimus alone versus temsirolimus plus hormonal therapy (megestrol acetate and tamoxifen) in advanced, persistent or recurrent endometrial carcinoma. Results are not summarized in the data compiled for this report. |

Megestrol is part of a combination regimen in this trial, so its individual effect cannot be separated out.

---

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0306 | Megestrol | Valid |

Dosage form and approved indication are not recorded for this registration.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (progestin) therapy, not a conventional cytotoxic agent |
| Myelosuppression Risk | Generally low; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Generally low; please refer to the package insert warnings and precautions |
| Monitoring Items | Blood glucose, blood pressure, liver and renal function, and signs of adrenal suppression (reported with megestrol therapy in the literature) |
| Handling Protection | Please refer to the package insert warnings and precautions, and follow local institutional policy |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** Megestrol is linked to potential contraindications or cautions in hypertension, kidney disease, liver disease, gallbladder disease, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, adrenocortical insufficiency (including Addison disease), pyoureter, male hypogonadism, eunuchism, premature menopause and androgen insensitivity syndrome. These need confirmation against the official label.
- **Drug Interactions:** The interaction screening returned 100 interactions, and the 20 shown are all moderate. Most involve diabetes medicines, such as metformin, pioglitazone, sitagliptin, semaglutide, insulin products, sulfonylureas and SGLT2 inhibitors. Blood glucose control may need closer monitoring when used together. Others include aprepitant and clarithromycin.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed randomized Phase 2 trial in endometrial cancer and a plausible hormonal mechanism support this indication. However, megestrol was tested only within a combination regimen.

**To proceed, the following is needed:**
- The official package insert (warnings and contraindications), which is currently missing
- Detailed mechanism of action data
- Trial results isolating the contribution of megestrol, or monotherapy data
- Clarification of why the Philippines registration was cancelled, and of its dosage form and indication
- A glucose, blood pressure and adrenal function monitoring plan, especially for patients taking diabetes medicines

**Additional note:** Among the other predicted indications, ovarian cancer has the most supporting material, including Phase 2 studies of high-dose megestrol in previously treated disease. It shows only modest, limited activity, and is better treated as a separate research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

