---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azathioprine: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Azathioprine"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "osteoarthritis susceptibility", "WHIM syndrome", "inflammatory bowel disease", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "ulcerative colitis (disease)", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
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

# Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is an immunosuppressive purine antimetabolite, listed in the knowledge base for **rheumatoid arthritis**.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome.
There are **0 clinical trials** and **0 publications** behind this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (from the knowledge-graph indication record; the Philippine registration lists no indication text) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Azathioprine is known as an immunosuppressive purine antimetabolite. It inhibits purine synthesis in lymphocytes, which dampens immune activation. That is the basis of its use in rheumatoid arthritis and other immune-mediated diseases.

This mechanism has no identifiable link to the predicted condition. The condition is a rare developmental malformation syndrome that is not driven by immune activity. The score is extremely high (0.99999), but no trial or publication supports it. It most likely reflects an artifact of the knowledge graph rather than a real biological signal. We do not consider this prediction mechanistically plausible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0035 | Azathioprine | Cancelled |

This is the only registration on record. It is a single-ingredient product, and the data compiled for this report lists no dosage form, manufacturer or approved indication for it.

---

## Safety Considerations

Safety data from the package insert is not available; please refer to the package insert for warnings and contraindications.

- **Conditions flagged in the knowledge graph (not label text)**: pancreatitis, thrombocytopenia, anaemia (including macrocytic anaemia), impaired renal function, infectious disease (including fungal infection and dermatophytosis), lymphoma (including primary CNS lymphoma, lymphosarcoma and hepatosplenic T-cell lymphoma), and hepatic vein thrombosis / Budd-Chiari syndrome. These must be verified against the official label.
- **Drug Interactions**: 100 interactions were found in total, and the first 20 returned are summarised here.
  - Moderate: mesalazine, balsalazide, olsalazine, sulfasalazine.
  - Minor: zinc acetate, zinc gluconate, zinc sulfate.
  - Severity not classified: epinephrine, amphotericin B, acetylsalicylic acid, calcitriol, pantoprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, omeprazole, sucralfate, rosiglitazone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanism. The drug also has no currently valid registration in the Philippines.

**To proceed, the following is needed:**
- Any biological rationale connecting purine antimetabolite immunosuppression to this syndrome's pathology
- Mechanism of action data
- Package insert warnings and contraindications

**Note on other predictions in the same analysis:** Two other predicted indications, inflammatory bowel disease and ulcerative colitis, reached evidence level L1 with a "Proceed with Guardrails" recommendation. Both are established, guideline-supported uses of azathioprine rather than novel repurposing. Any follow-up should consider those candidates separately. Guardrails would include TPMT/NUDT15 genotyping, blood count and liver monitoring, and awareness of malignancy and infection risk.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

