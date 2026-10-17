---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aztreonam: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, Pseudomonas aeruginosa infection…"
monitor_inn: "Aztreonam"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
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

# Aztreonam: From Bacterial Infections (Urinary Tract Infection and Others) to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used for gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection, peritonitis and E. coli infection.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support it, and the link appears to be a graph-based artifact.
Among the top 10 predictions, only **gonococcal urethritis** has meaningful supporting literature (6 publications, including a 2020 single-arm open-label trial), and that is largely an extension of existing anti-infective use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, rhinoscleroma, E. coli infection, endometritis (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, aztreonam is a monobactam antibiotic that inhibits bacterial cell wall synthesis by binding penicillin-binding protein 3 (PBP3), with activity against gram-negative aerobes.

For the top-ranked prediction, polyclonal hyperviscosity syndrome, **no plausible mechanistic link exists**. It is a haematological/protein disorder with no bacterial target, so the high score (99.73%) appears to be a graph-based artifact. The same applies to other highly ranked predictions such as hyperamylasemia, congenital analbuminemia, blood group incompatibility and premalignant haematological disease. Ureaplasma urethritis is mechanistically unfavourable because Ureaplasma has no cell wall.

A few lower-ranked predictions are biologically coherent because they are infections within aztreonam's spectrum:
- **Gonococcal urethritis** (rank 4): aztreonam has shown in vitro and clinical activity against *Neisseria gonorrhoeae*, including penicillinase-producing strains. This is a pathogen-matched extension of existing anti-infective use rather than true repurposing.
- **Xanthogranulomatous pyelonephritis** (rank 10): an extension of the existing urinary tract infection use, though management is mainly surgical.
- **Epiglottitis** (rank 8): *Haemophilus influenzae* is within the spectrum, but the evidence is indirect and modern practice relies on other agents.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction, polyclonal hyperviscosity syndrome, or for any other predicted indication in the top 10.

---

## Literature Evidence

No literature is available for the top-ranked prediction (polyclonal hyperviscosity syndrome). The table below shows the most relevant publications retrieved for the best-supported prediction, **gonococcal urethritis**.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single-dose intramuscular aztreonam 2 g tested in men with gonorrhea, motivated by the threat of ceftriaxone-resistant gonococci |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM: no failures with either; satisfactory for uncomplicated urethral gonorrhea in men |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical study | Genitourin Med | Single 1 g IM dose cleared infection at all sites in 61 men and 26 women (except one pharyngeal site); well tolerated |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Clinical/epidemiologic study | Hinyokika Kiyo | Clinical study of single-dose aztreonam therapy for gonorrheal infections, with epidemiologic data |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro/clinical efficacy study | J Infect Dis | Effectiveness against penicillin-resistant gonococci |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance/microbiology study | J Infect Chemother | Report of cephem- and aztreonam-high-resistant, non-β-lactamase-producing *N. gonorrhoeae* |

Publications retrieved for other predictions are indirect or irrelevant: epiglottitis (PMID 3766490, a 1986 pediatric gram-negative infection series), monoclonal gammopathy (PMID 4079014, infections in haematologic disorders, not the gammopathy itself), and blood group incompatibility (PMID 34956120, a keyword mismatch concerning antimicrobial resistance genes).

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0037 | Aztreonam | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so there is currently no valid marketed aztreonam product in the Philippines.

---

## Safety Considerations

- **Knowledge-graph contraindication associations** (from drug-disease relationships in the knowledge graph, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, bronchial disease.
- **Drug Interactions**: 27 interactions were identified. The ones graded Moderate are **picosulfuric acid, dicoumarol and warfarin** (anticoagulant interactions are especially relevant for monitoring). Others, such as vancomycin, amikacin, amphotericin B, tacrolimus, heparin, metronidazole, fluconazole, acyclovir, morphine, proton pump inhibitors and corticosteroids, are listed without a severity grade.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, polyclonal hyperviscosity syndrome, has no clinical or literature support and no plausible mechanism, and the evidence level is L5 (model prediction only). The only biologically coherent signal, gonococcal urethritis, is an extension of existing antibacterial use, is limited by resistance reports and standard-of-care alternatives, and the Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- If pursuing gonococcal urethritis as a research question: current susceptibility data and a comparison with standard-of-care regimens
- A valid Philippines registration or supply route, since the only licence is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

