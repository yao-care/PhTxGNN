---
layout: default
title: Danazol
parent: Model Prediction Only (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Danazol"
predicted_indications: ["amenorrhea (disease)", "benign mammary dysplasia", "apocrine adenosis of breast", "blunt duct adenosis of breast", "fat necrosis of breast", "breast abscess", "lactation disease", "breast adenosis", "vulvovaginitis", "vulvitis"]
description: "Danazol: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Danazol
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

## Danazol: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Danazol is a synthetic steroid originally used for endometriosis and fibrocystic breast disease.
The TxGNN model predicts it may be effective for **Amenorrhea**, but there are **no registered clinical trials** and only **20 publications** (mostly older reviews and small studies), and the literature suggests this prediction may be a directional mismatch: danazol *causes* amenorrhea rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the literature, danazol suppresses the pituitary-ovarian axis (reducing the GnRH/LH/FSH midcycle surge) and creates an anovulatory, low-oestrogen, high-androgen state.

This is the key problem with the prediction. Amenorrhea is a known **pharmacological effect** of danazol, not a condition it treats. The literature supports inducing amenorrhea as an intended endpoint in endometriosis and in menstrual suppression (for example, in transgender individuals), not treating amenorrhea as a disease. The high TxGNN score likely reflects this strong drug–condition association, and the direction of the relationship appears reversed.

Other predicted indications are mostly benign breast conditions (benign mammary dysplasia, breast adenosis, and similar). These overlap with danazol's existing fibrocystic breast disease indication, so they are essentially aliases of an approved use rather than new repurposing opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2523321](https://pubmed.ncbi.nlm.nih.gov/2523321/) | 1989 | RCT | Fertility and Sterility | Gestrinone vs danazol in 39 infertile women with endometriosis; amenorrhea was the treatment target and dose was escalated if not achieved |
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | Double-blind randomized study | Fertility and Sterility | Nafarelin vs danazol in 82 women with endometriosis; both led to significant regression of active disease |
| [6210867](https://pubmed.ncbi.nlm.nih.gov/6210867/) | 1982 | Double-blind dose study | Obstetrics and Gynecology | Danazol 100–600 mg/day for 6 months in endometriosis; clinical improvement varied with dose |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Systematic review | Archives of Gynecology and Obstetrics | Safety and effectiveness of gestrinone (a related agent) in endometriosis, which induces amenorrhea |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Retrospective cohort | Women's Health | Danazol used for menstrual suppression in transgender individuals; induces amenorrhea with reversible androgenic effects |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Review | J Reprod Med | Danazol has diverse effects, including gonadotropin inhibition and suppression of gonadal steroidogenesis |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Review | Human Reproduction Update | Management of endometriosis; lesions regress during amenorrhoea or menopause |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Pharmacological therapy for abnormal uterine bleeding |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Therapeutic induction of amenorrhoea in female personnel |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Review | Prog Clin Biol Res | Danazol in endometriosis and infertility; suppresses ovarian function |

Most of these studies concern **inducing** amenorrhea. None shows danazol treating amenorrhea as a disease.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0128 | Danazol | Not specified | Not specified (status: valid) |


---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: epilepsy, porphyria (including inherited porphyria and porphyrin metabolism disease), kidney disease, liver disease, gallbladder disease, female breast carcinoma, migraine disorder, and familial combined hyperlipidaemia.
- **Drug Interactions**: 100 interactions were recorded. Examples include **Cisapride (Major)**. Moderate interactions include antidiabetic agents (acarbose, SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin, GLP-1 agonists such as exenatide and dulaglutide, sulfonylureas such as glipizide, glimepiride and glyburide, and insulins), budesonide, and eliglustat. The literature also reports potentiation of warfarin's anticoagulant effect with bleeding complications.
- **Pregnancy and lactation**: Danazol is generally avoided in pregnancy (risk of fetal virilization) and lactation.
- **Androgenic effects**: These include voice changes and hair pigmentation, which limit use.

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication appears to be a directional mismatch, because amenorrhea is an effect of danazol rather than a disease it treats. There are no clinical trials, and the evidence is at L4. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Confirm whether the prediction reflects a true therapeutic target or only the drug's known pharmacological effect (for example, by reviewing the TxGNN mapping of this indication)
- Consider re-evaluating the benign breast disease predictions (benign mammary dysplasia, breast adenosis), which have more supporting literature but overlap with the existing indication
- Obtain the package insert (warnings and contraindications) and mechanism of action data
- Clarify the regulatory pathway, since the only Philippines registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

