---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 2
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-11-12
description: "Iodixanol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available in the Philippines licence record (indication text is e…"
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Iodixanol: From Contrast Imaging Agent to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Iodixanol is an iodinated, iso-osmolar radiographic contrast agent.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **0 clinical trials** and **5 publications**, none of which show a therapeutic effect. They describe iodixanol only as an imaging probe, so this prediction rests on the model alone.

<!-- review:begin ph-lic-20261106-iodixanol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Iodixanol is an iodinated, iso-osmolar radiographic contrast agent. It is registered in the Philippines, but the data compiled for this report contain no approved indication text." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-iodixanol-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Philippines licence record (indication text is empty) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9907 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is known as an iodinated, iso-osmolar radiographic contrast agent. It has no known disease-modifying activity in osteoarthritis.

The retrieved literature concerns iodixanol as a research and imaging tool. Examples include contrast-enhanced CT of cartilage, diffusion of solutes and nanoparticles through cartilage and the osteochondral interface, and in vitro compatibility with platelet-rich plasma. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It most likely reflects the repeated association of iodixanol with joint imaging, not a therapeutic effect. No mechanistic link to treating osteoarthritis is supported at this time.

A second prediction, rheumatoid arthritis (score 0.9900), has even weaker support. The only article found is a case report on desensitization to a different contrast agent (iohexol). It says nothing about iodixanol efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these studies tests iodixanol as a treatment for osteoarthritis. All are preclinical, computational or in vitro imaging studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Preclinical imaging study | Ann Biomed Eng | Nanoparticle diffusion imaging by CT, combined with finite element modelling, used to reveal cartilage function |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational modelling | J Biomech | Finite element model of neutral solute transport across the cartilage and subchondral bone interface, studied with CT |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Preclinical imaging study | Ann Biomed Eng | Dual-contrast agent in photon-counting CT to assess articular cartilage health |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Experimental transport study | J Biomech | Iodixanol used as a CT contrast agent to study permeability of the osteochondral interface in equine and human samples |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | J Exp Orthop | Iodine contrast agents did not affect platelet-rich plasma function at an early time point in vitro |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Iodixanol | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records. The listed examples are mostly rated Major and include:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Vancomycin
  - Aminoglycosides and polymyxins: kanamycin, neomycin, streptomycin, polymyxin B
  - Mannitol (Moderate)

  Several others, such as famotidine, acetylsalicylic acid, morphine, omeprazole and prednisone, have an unknown severity level.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. No clinical trial exists, and the literature shows iodixanol as an imaging agent, not a treatment for osteoarthritis. Evidence is therefore L5. The rheumatoid arthritis prediction has no relevant support either.

**To proceed, the following is needed:**
- Evidence that iodixanol has a therapeutic effect in osteoarthritis, from preclinical or clinical studies that directly study the disease
- Mechanism of action data from DrugBank
- The Philippines package insert, to confirm the approved indication, warnings and contraindications
- A review of the major drug interactions, particularly with nephrotoxic agents and metformin

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "It is registered in the Philippines, but the data compiled for this report contain no approved indication text" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

