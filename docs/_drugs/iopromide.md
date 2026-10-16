---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Iopromide: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: No approved indication text is available in the Philippines registrat…"
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
---

# Iopromide
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

# Iopromide: From Contrast Imaging Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent used for diagnostic imaging. The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but **no clinical trials and no publications** were found to support this prediction. It is a computational prediction only and should be treated as a low-confidence signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is available in the Philippines registration record (the drug is a diagnostic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is an iodinated, non-ionic contrast agent. It is used for imaging, not to treat disease, and it has no known pharmacological activity on cartilage or joint pathways.

The relationship between the original use and the predicted indication is weak. "Osteoarthritis susceptibility" describes a genetic risk concept rather than a treatable clinical condition. The high score (0.9957) most likely reflects network-topology patterns in the knowledge graph rather than a real drug effect.

The other top predictions point the same way. They include osteoarthritis, rheumatoid arthritis, rare skeletal dysplasias (brachyolmia, acromesomelic dysplasia, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy. All have scores above 0.99, none has any clinical evidence, and none has a plausible mechanistic link. Iodinated contrast agents also carry cautions in some hemoglobinopathies, such as sickle cell disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0256 | Iopromide | Not specified | Not specified (registration status: cancelled) |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total, and the main ones are listed below. Most are rated Major.
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, and the aminoglycosides and polymyxin (kanamycin, neomycin, streptomycin, polymyxin B).
  - **Moderate**: mannitol.
  - **Unknown severity**: clotrimazole, acetylsalicylic acid, bupropion, dexamethasone, pantoprazole.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, no mechanistic link, and the only Philippines registration is cancelled. Iopromide is a diagnostic imaging agent, so a therapeutic role in joint or skeletal disease is not credible on current data.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a documented biological rationale
- Package insert warnings and contraindications from DOH-FDA Philippines
- Any preclinical or clinical evidence in the predicted indication
- Clarification of whether a more clinically defined target (for example, osteoarthritis rather than "susceptibility") is meaningful for a contrast agent
- Confirmation of the registration status and original approved indication in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

