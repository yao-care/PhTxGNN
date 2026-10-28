---
layout: default
title: Ertapenem
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Ertapenem: predicted new indication Bacterial arthritis (evidence level L4). Approved use: Bacterial pneumonia, streptococcal pneumonia…"
monitor_inn: "Ertapenem"
predicted_indications: ["bacterial arthritis", "staphylococcus aureus infection"]
---

# Ertapenem
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

## Ertapenem: From Bacterial Pneumonia to Bacterial Arthritis
{: .text-alpha }

## One-Sentence Summary

Ertapenem is a carbapenem antibiotic, originally used for bacterial infections such as bacterial pneumonia, streptococcal pneumonia and Peptostreptococcus infections.
The TxGNN model predicts it may be effective for **bacterial arthritis**, but there are **no registered clinical trials** and only **10 publications** (mostly case reports and cohort studies) supporting this direction.
A second prediction, *Staphylococcus aureus* infection, has more support (**2 clinical trials** and **20 publications**) and is described in the notes below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, streptococcal pneumonia, Peptostreptococcus infectious disease (the Philippines registration record has no approved indication text) |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ertapenem is a broad-spectrum carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against many Enterobacterales, anaerobes and streptococci, which are common pathogens in bone and joint infections.

Bacterial pneumonia and bacterial arthritis are both bacterial infections, so the high prediction score is mechanistically plausible. This is mostly an extension of the drug's established antibacterial spectrum to a different infection site, not a new mechanism. Bone and joint penetration and optimal dosing are not established by the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered for bacterial arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohort | Antimicrob Agents Chemother | Retrospective study of 306 patients on long-term outpatient ertapenem; bone and joint infections were among the treated indications, alongside intra-abdominal infections and pneumonia |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohort | J Antimicrob Chemother | Subcutaneous suppressive β-lactam therapy for bone and joint infections in 10 patients, for cases where optimal surgery was not feasible |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case report | J Chemother | Klebsiella pneumoniae septic wrist arthritis treated successfully with ertapenem and levofloxacin |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case report | BMJ Case Rep | Citrobacter koseri osteomyelitis and septic arthritis in a diabetic foot treated successfully with ertapenem |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case report/Review | Anaerobe | First reported case of Clostridium paraputrificum shoulder septic arthritis and osteomyelitis |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case report/Review | J Investig Med High Impact Case Rep | Prevotella bivia septic arthritis in an immunocompetent adult |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohort | Clin Lab | Pathogen distribution and antimicrobial resistance in bone and joint infections in children under four |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro/Preclinical | Diagn Microbiol Infect Dis | Auranofin restored ertapenem susceptibility in carbapenem-resistant E. coli in laboratory tests |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Cohort | J Antimicrob Chemother | Temocillin evaluated as an alternative to carbapenems for bone and joint infections caused by third-generation cephalosporin-resistant Enterobacterales |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Review | JAMA | Hidradenitis suppurativa review; not directly relevant to this indication |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0174 | Ertapenem | Not recorded | Not recorded (status: valid) |

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (not taken from label text): epilepsy, kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions**: 38 interactions were found in total. The main one is **Bupropion (Major)**. **Moderate** interactions are with picosulfuric acid, polyethylene glycol (3350 with electrolytes) and sodium sulfate. The remaining listed interactions (for example vancomycin, metronidazole, metformin and omeprazole) have an unclassified severity.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bacterial arthritis prediction is mechanistically plausible, but it rests on case reports, small cohorts and in vitro work, with no registered trials. The only Philippines registration is cancelled, and the package insert safety data are missing.

**To proceed, the following is needed:**
- Prospective or comparative studies of ertapenem in bacterial arthritis, including bone and joint penetration and dosing data
- Confirmation of the regulatory status of PNF-0174, or a new registration
- The Philippines package insert warnings and contraindications
- Mechanism of action data from DrugBank

### Note on the second prediction: *Staphylococcus aureus* infection

The second predicted indication, *Staphylococcus aureus* infection (score 0.9928), has stronger support at Evidence Level L2, although its recommendation is "Research Question" rather than Go. Ertapenem would not be used alone. The evidence concerns **cefazolin plus ertapenem** for persistent methicillin-susceptible *S. aureus* (MSSA) bacteremia. The proposed mechanism is complementary penicillin-binding protein saturation, which gives synergistic killing.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | Cefazolin plus ertapenem for MSSA bacteremia (CERT), a sub-study of the SNAP platform trial; no results yet |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by invitation | 300 | Early dual versus single IV antibiotic therapy in *S. aureus* bacteremia; the data do not confirm ertapenem as the partner drug |

Key publications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Cohort/Case series | Clin Infect Dis | Cefazolin plus ertapenem salvaged 11 persistent MSSA bacteremia cases, with clearance within 24 hours in 8 |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Cohort | J Antimicrob Chemother | Carbapenem combination therapy compared with standard of care for persistent MSSA bacteremia |
| [41759962](https://pubmed.ncbi.nlm.nih.gov/41759962/) | 2026 | Cohort | Infect Dis Now | Multicenter case series of ertapenem with penicillin M or cefazolin |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | Am J Health Syst Pharm | Review of combination options for persistent MSSA bacteremia |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | In vitro/Case series | Antimicrob Agents Chemother | Cefazolin plus ertapenem synergy in vitro and in a mouse model, with clinical clearance of refractory bacteremia |

The clinical benefit is not yet proven. Prospective trial results are pending, and ertapenem is highly protein bound, so low albumin may reduce exposure (PMID 40448546).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

