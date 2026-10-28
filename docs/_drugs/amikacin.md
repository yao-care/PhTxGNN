---
layout: default
title: Amikacin
parent: Model Prediction Only (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "meningococcemia"]
description: "Amikacin: predicted new indication Paratyphoid fever (evidence level L5). Approved use: Not recorded in the local data"
---

# Amikacin
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

## Amikacin: Paratyphoid fever
{: .text-alpha }

## One-Sentence Summary

Amikacin is an aminoglycoside antibiotic originally used for serious gram-negative bacterial infections such as bacterial pneumonia, *Pseudomonas aeruginosa* infection, and bacterial meningitis.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**, but the supporting evidence is weak: **no clinical trials** and **8 publications**, mostly surveillance and susceptibility studies without amikacin efficacy data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, amikacin is an aminoglycoside that binds the 30S ribosomal subunit and inhibits bacterial protein synthesis. It has activity against gram-negative Enterobacterales, including *Salmonella*.

Paratyphoid fever is a gram-negative bacterial infection, so an antibacterial rationale exists, and this is likely why the model ranks it highly. The link is plausible in vitro but weak clinically. Aminoglycosides reach poor concentrations inside cells, where *Salmonella* persists, and they are not standard therapy for enteric fever. The retrieved literature is mostly epidemiology and antibiogram surveys, with no efficacy data for amikacin.

Other top predictions show a similar pattern. Typhoid fever (0.9977) and salmonellosis (0.9974) have only in vitro, observational, or indirect evidence. Several others, such as diffuse scleroderma, congenital analbuminemia, and polyclonal hyperviscosity syndrome, have no plausible mechanism and no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatric Hematology and Oncology | Child with leukemia and acalculous cholecystitis due to *S. paratyphi* B, successfully treated with cefepime, amikacin, and granulocyte support |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Clinical report | Mikrobiyoloji Bulteni | Treatment and antibiogram results in 48 patients with paratyphi B infection resistant to classical therapy |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective cohort | J Indian Med Assoc | Clinical profile and antibiotic sensitivity of *S. typhi* and *S. paratyphi* in 145 children |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observational | Med J Armed Forces India | Susceptibility pattern of *S. typhi* and *S. paratyphi* A isolates, including re-emerging chloramphenicol sensitivity |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Surveillance | Indian J Pathol Microbiol | 280 *S. typhi* strains; multidrug-resistant strains remained sensitive to aminoglycosides, including amikacin, and to ciprofloxacin |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Surveillance | New Microbiologica | Occurrence of *S. typhi* and *S. paratyphi* in Jordan |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Antibiogram | JNMA | Blood culture isolates and antibiograms at a teaching hospital |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological study | Pak J Biol Sci | Isolation and identification of *S. paratyphi* from enteric fever patients in Quetta |

For the closely related typhoid fever prediction, one small clinical study (PMID 2598731) reported a clinical effective rate of 36.4% with amikacin (11 patients) versus 100% with ofloxacin.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0014 | Amikacin | Not specified | Not specified (status: valid) |

## Safety Considerations

Safety information from the compiled data is limited. Package insert warnings and contraindications were not available; please refer to the package insert.

- **Contraindication-related conditions (from a knowledge graph, not label text)**: kidney disease, pyoureter, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, central nervous system origin vertigo, myasthenia gravis (including adult-onset), neuromuscular junction disease, parkinsonian disorder, and Parkinson disease.
- **Drug Interactions**: The interaction query returned 100 records; the first 20 are shown to the extent available.
  - **Major**: magnesium sulfate, mannitol.
  - **Moderate** (examples): amphotericin B (including lipid and liposomal forms), other aminoglycosides (kanamycin, neomycin), proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), acetylsalicylic acid, mesalazine, balsalazide, olsalazine, and exenatide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence consists of surveillance, susceptibility, and case-level reports with no efficacy trials for amikacin. Aminoglycosides are not standard therapy for paratyphoid or enteric fever, because of poor intracellular penetration and the availability of better-established agents. The only Philippine registration is cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism of action data (for example from DrugBank)
- Comparative clinical data on amikacin in enteric fever, ideally prospective, against current standard therapy
- Clarification of the current registration status and available formulations in the Philippines
- A safety monitoring plan covering nephrotoxicity, ototoxicity, and neuromuscular effects, given the contraindication-related conditions and major interactions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

