---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fosfomycin: predicted new indication Gonococcal urethritis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "Fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome"]
---

# Fosfomycin
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

# Fosfomycin: From Urinary Tract Infection to Gonococcal Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic originally used to treat urinary tract infection. The TxGNN model predicts it may be effective for **gonococcal urethritis**. Support is limited: **0 registered clinical trials** and **6 publications**, of which only 3 test fosfomycin in gonococcal infection (one 2016 randomized trial and two 1977 clinical studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (one randomized trial in the literature; open-label, with no registered trial) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase), which blocks the first step of bacterial peptidoglycan (cell wall) synthesis. This kills bacteria, and the mechanism is plausibly active against *Neisseria gonorrhoeae*. The detailed mechanism-of-action record for this drug was not available in the data compiled for this report, so this explanation rests on the known pharmacology of the drug class.

Urinary tract infection and gonococcal urethritis are both bacterial infections of the lower genitourinary tract. Fosfomycin reaches high concentrations in urine, which supports its use at this site. Rising gonococcal resistance to standard agents also makes alternative options worth studying.

The clinical signal comes from a 2016 randomized trial of oral fosfomycin trometamol in men with uncomplicated gonococcal urethritis and from older 1977 studies using intramuscular fosfomycin. From the available abstracts, the design, comparator and efficacy details cannot be fully verified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT (open-label) | Clin Microbiol Infect | Fosfomycin trometamol 3 g orally on days 1, 3 and 5 for uncomplicated gonococcal urethritis in men. 152 men enrolled and 126 completed. Efficacy results are not in the available excerpt. |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical study | Chemotherapy | 70 patients with acute or subacute gonococcal urethritis treated with intramuscular fosfomycin. A 4 g total dose over several injections gave 11 cures in 12 patients (92%). A single 4 g dose gave 37 cures in 43 patients (86%). |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Clinical / bacteriological study | Chemotherapy | Bacteriological evaluation in 959 patients across many infection types, including gonococcal urethritis, at Spanish hospitals. Gonococcal-specific results are not separated in the excerpt. |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Review | Zhonghua Nan Ke Xue | Genitourinary infection with non-gonococcal Neisseria in men. Indirect relevance. |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Secondary analysis | Sex Transm Infect | Spontaneous clearance of asymptomatic gonorrhoea in the NABOGO trial. Not specific to fosfomycin. |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Case report | J Fr Ophtalmol | Gonococcal conjunctivitis with corneal perforation, caused by a strain resistant to penicillins, tetracyclines and fluoroquinolones. Not specific to fosfomycin. |

## Philippines Market Information

| Authorization Number | Product Name | Type | Status |
|---------|------|------|-----------|
| PNF-0208 | Fosfomycin | Single-ingredient | Cancelled |

This is the only registration. It is cancelled, so no valid registration currently exists. No dosage form or approved indication text is recorded for it.

## Safety Considerations

- **Contraindication signals (from the drug-disease knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions** (3 found):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the package insert for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one open-label randomized trial (2016) and two decades-old studies (1977) support this indication. There are no registered trials, and the Philippines registration is cancelled. The evidence is best treated as a research question rather than a basis for a repurposing decision.

For comparison, a separate prediction for this drug, pyelitis (upper urinary tract infection), has much stronger support. It includes the Phase 2/3 ZEUS trial of IV fosfomycin and is largely an extension of the existing urinary indication. It may be a more practical candidate to prioritize.

**To proceed, the following is needed:**
- Full text of the 2016 randomized trial (comparator, cure rates, microbiological endpoints) and confirmation of its design.
- Current gonococcal susceptibility data for fosfomycin, and resistance-emergence data.
- Confirmation of the formulation and route to be used (oral trometamol vs. intramuscular), and whether a registered product is available locally.
- Package insert warnings and contraindications, since no label-based safety data are available.
- Detailed mechanism-of-action data from a primary source.
- Comparison against current guideline-recommended gonorrhoea regimens.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

