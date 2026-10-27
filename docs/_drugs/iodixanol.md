---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Iodixanol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not available in the Philippines registration data"
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Iodixanol: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility
{: .text-alpha }

## One-Sentence Summary

Iodixanol is an iodinated X-ray contrast agent used in diagnostic imaging, and its Philippines registration is currently cancelled.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (also osteoarthritis and rheumatoid arthritis at lower ranks), but **no clinical trials** are registered and the **literature (5 publications for osteoarthritis)** covers diagnostic imaging use only, not treatment benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Philippines registration data (the data compiled for this report show no approved indication text; the drug is known as an iodinated contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iodinated, iso-osmolar contrast agent. It works by absorbing X-rays so that tissues and vessels can be visualized, and it is not known to have disease-modifying pharmacology.

The high TxGNN score (0.99) is a model prediction only. "Osteoarthritis susceptibility" is a genetic-risk phenotype rather than a treatable clinical condition, so a therapeutic indication is not well defined. The related predictions (osteoarthritis, rheumatoid arthritis) also lack therapeutic support. The prediction likely reflects iodixanol's frequent appearance in joint and cartilage imaging research rather than any treatment effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below were retrieved for the second-ranked prediction, osteoarthritis. All concern diagnostic or experimental use, not therapy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging method study | Annals of Biomedical Engineering | CT nanoparticle diffusion imaging used to reveal cartilage function, combined with finite element modelling |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging method study | Annals of Biomedical Engineering | Dual-contrast agent in photon-counting CT to assess articular cartilage health |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Experimental transport study | Journal of Biomechanics | Iodixanol (~1550 Da) used as a CT contrast agent to study permeability of the cartilage–subchondral bone interface |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational modelling | Journal of Biomechanics | Finite element and CT approach to neutral solute transport across the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | Journal of Experimental Orthopaedics | Iodine contrast agents did not affect platelet-rich plasma function at an early time point (a compatibility finding, not efficacy) |

For rheumatoid arthritis, the only retrieved paper ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, Cureus) is a case report on desensitization to a different contrast agent (iohexol) in a patient with rheumatoid arthritis-related amyloidosis. It is not evidence of therapeutic benefit and is likely a spurious match.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0253 | Iodixanol | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 potential interactions in total. Most of the listed ones are rated Major, including:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides (kanamycin, neomycin, streptomycin)
  - Vancomycin
  - Polymyxin B
  - Aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine)

  Mannitol is rated Moderate. Several others, such as famotidine, aspirin, morphine, omeprazole and prednisone, have an unknown severity level. Many of the Major interactions involve drugs with kidney-related toxicity, so renal function warrants attention.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (evidence level L5). No clinical trials exist, and the literature shows iodixanol only as an imaging tool, not as a treatment. "Osteoarthritis susceptibility" is also not a well-defined treatable condition, and iodixanol has no valid current registration in the Philippines.

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible biological link to joint disease
- Preclinical evidence of disease-modifying or symptom-relieving effects in osteoarthritis
- Clarification of whether a defined, treatable target indication exists, rather than a susceptibility phenotype
- Package insert warnings and contraindications for safety screening
- Clarification of the cancelled registration status and the available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

