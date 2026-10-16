---
layout: default
title: Albendazole
parent: High Evidence (L1-L2)
nav_order: 17
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-15
description: "Albendazole: predicted new indication Alveolar echinococcosis (evidence level L2). Approved use: Cystic echinococcosis, cysticercosis…"
---

# Albendazole
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Albendazole: From Cystic Echinococcosis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is an anthelmintic originally used to treat cystic echinococcosis and cysticercosis.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis**,
with **3 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic echinococcosis, cysticercosis, Echinococcus granulosus infection |
| Predicted New Indication | Alveolar echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Albendazole is a benzimidazole that binds parasite beta-tubulin and blocks microtubule polymerization. This impairs glucose uptake and energy metabolism in the worm. Detailed mechanism-of-action data was not available in the data compiled for this report, so this description reflects the general known pharmacology of the drug class.

Alveolar echinococcosis is caused by *Echinococcus multilocularis*, a close relative of *Echinococcus granulosus*, which causes the drug's original indication. Because the parasites are closely related, the same mechanism applies. Albendazole is already the standard parasitostatic therapy for alveolar echinococcosis in consensus guidelines. It suppresses the parasite rather than curing it, so long-term or lifelong use is common after incomplete surgery.

This is better seen as an extension within the same disease family than as a true repurposing. The very high TxGNN score fits that picture.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole in early-stage alveolar echinococcosis found by ultrasound screening in Kyrgyzstan. Most direct evidence, but randomization and control arm are not stated. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Not applicable | Completed | 50 | EchinoVISTA: parasite viability and follow-up markers in hepatic alveolar echinococcosis patients treated with albendazole, to guide timing of treatment withdrawal. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | Not applicable | Unknown | 24 | Randomised trial of adjuvant albendazole vs placebo after pulmonary hydatid cyst resection. This is cystic disease, so only indirectly relevant. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Review | Acta Trop | Expert consensus on diagnosis, treatment and follow-up of cystic and alveolar echinococcosis |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21st-century advances in echinococcosis diagnosis and treatment |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Legeforen | Alveolar echinococcosis often needs surgical resection plus prolonged antiparasitic drug use |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Management of liver echinococcosis; surgery is the cornerstone |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Albendazole and mebendazole, and the search for further treatment options |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Trop | No non-surgical options yet replace albendazole and mebendazole |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Observational | J Antimicrob Chemother | 35 patients on mebendazole or albendazole followed for an average of 39 months |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Review | Parasitology | Albendazole is not parasiticidal and can cause severe adverse effects; repurposing candidates such as pyronaridine are being explored |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclinical | Antimicrob Agents Chemother | Solubilized albendazole formulations studied in a rat model of hepatic alveolar echinococcosis |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | Chin J Schistosomiasis Control | Albendazole may delay disease progression in patients who cannot have surgery |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0007 | Albendazole | Not specified | Not specified (status: cancelled) |

The only Philippines registration for this drug is cancelled, so there is currently no valid marketed product.

## Safety Considerations

- **Disease associations to watch (from a knowledge graph, not label text)**: liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), pancytopenia, and aplastic anaemia. Baseline and periodic liver function tests and blood counts are advisable, especially with prolonged use.
- **Drug Interactions**: 96 interactions were found. Examples at moderate level include aprepitant, cobicistat, deferasirox, alemtuzumab, amprenavir, anagrelide, apalutamide, bendamustine, bexarotene, binimetinib, boceprevir, and bosentan. Minor examples include cimetidine, dexamethasone, and lidocaine.

For warnings and contraindications from the label, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Albendazole is already the guideline-standard parasitostatic therapy for alveolar echinococcosis. A completed Phase 2 trial (n=194) supports it directly, and this is an extension within the same disease family. Because there is no valid Philippines registration and only one controlled-evidence trial of limited design, it should proceed only with safeguards.

**To proceed, the following is needed:**
- A valid Philippines registration, since the only one on record is cancelled
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism-of-action data
- Trial design details (randomization, control arm) and results for NCT07182305
- A monitoring plan for liver function and blood counts during long-term use
- A review of drug interactions against co-medications

## Other Predicted Indications (for reference)

- **Coenurosis (score 99.83%)**: Trial evidence is almost entirely in neurocysticercosis, which is already an original indication, so extrapolation to true coenurosis is unproven. The only direct clinical signal is a case report ([PMID 36548661](https://pubmed.ncbi.nlm.nih.gov/36548661/)). Neurological disease requires corticosteroid cover and anticonvulsants. Proceed only with guardrails.
- **Cestode infectious disease (score 99.74%)**: This is an umbrella category that overlaps existing uses and is not a distinct opportunity. The only linked trial is [NCT00004403](https://clinicaltrials.gov/study/NCT00004403) (neurocysticercosis). Classified as a research question; a specific disease entity should be named before further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

