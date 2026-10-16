---
layout: default
title: Clomifene
parent: Model Prediction Only (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clomifene: predicted new indication 46… (evidence level L5). Approved use: Female infertility"
---

# Clomifene
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

# Clomifene: From Female Infertility to 46,XY Disorder of Sex Development Due to Testicular Steroidogenesis Defect

## One-Sentence Summary

Clomifene was originally used to treat female infertility, mainly where ovulation fails because of deficient hormonal stimulation.
The TxGNN model predicts it may be effective for **46,XY disorder of sex development due to testicular steroidogenesis defect**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Female infertility (from the knowledge graph; the Philippines registration record has no indication text) |
| Predicted New Indication | 46,XY disorder of sex development due to testicular steroidogenesis defect |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general pharmacology, clomifene is a selective estrogen receptor modulator. It blocks estrogen feedback in the hypothalamus, which raises GnRH, LH and FSH. Its binding to estrogen receptor alpha (ESR1) is also recorded in the pharmacology data.

In theory, higher LH could stimulate any residual Leydig cell steroidogenesis in the testis. However, this condition is usually caused by a primary enzymatic or receptor defect in the testis (for example in *LHCGR*, *HSD17B3* or *CYP17A1*). Stimulating gonadotropins is therefore unlikely to restore function. The link is speculative, and no trials or literature support it.

The same applies to the other predicted indications. Several of them are structural or chromosomal conditions with no plausible mechanistic link:
- **Vaginal septa (transverse and longitudinal):** structural anomalies treated surgically.
- **Partial trisomy/tetrasomy of chromosomes 5, 12 and 18p:** chromosomal dosage imbalances.
- **Ovarian remnant syndrome:** clomifene could stimulate the remnant tissue, which is the opposite of the therapeutic goal.
- **Fragile X carrier symptoms and BPES (including the 3q23 form):** the only link is indirect, through associated ovarian insufficiency.

The high scores most likely reflect proximity to reproductive and infertility terms in the knowledge graph, not a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0108 | Clomifene | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text): the knowledge graph links clomifene to the following conditions as contraindications.
  - Liver and gallbladder disease
  - Thyroid disorders (hypothyroidism, hyperthyroidism)
  - Adrenal insufficiency
  - Thrombophlebitis
  - Endometrial cancer and endometriosis
  - Polycystic ovary syndrome
  - Ovarian cyst and ovarian hyperstimulation syndrome
  - Pituitary tumours
  - Vision disorders
  - Anxiety, neurotic and dysthymic disorders
- **Drug Interactions**: One major interaction was identified, with **bexarotene**. Pharmacology data also record binding to estrogen receptor alpha and to the volume-regulated anion channel (VRAC), but these are target interactions with no severity grading.
- **Additional concern for the predicted indications**: for ovarian remnant syndrome, stimulating gonadotropins could theoretically stimulate residual ovarian tissue.

Package insert warnings and contraindications for the Philippines have not been obtained. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or literature. The proposed mechanism is speculative, because the underlying testicular defect is usually primary and unlikely to respond to gonadotropin stimulation. The only Philippines registration is cancelled, and the package insert safety data have not been retrieved.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A systematic literature and trial search specific to this indication, including case reports in 46,XY DSD
- Clarification of the regulatory status, since the only registration (PNF-0108) is cancelled
- Review of the other nine predicted indications, several of which have no credible mechanism, before any is prioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

