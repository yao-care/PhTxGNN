---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a broad-spectrum third-generation cephalosporin antibiotic recognized globally as a first-line agent for serious bacterial infections including meningitis, sepsis, and pneumonia, though it is not currently registered in the Philippines.
The TxGNN model predicts it may be effective for **Infectious Otitis Media** as the highest-evidence repurposing candidate in this dataset,
with **3 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (global use; no Philippines registration on record) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved in this evidence pack. Based on well-established pharmacological knowledge, Ceftriaxone belongs to the third-generation cephalosporin class and exerts bactericidal activity by binding to penicillin-binding proteins (PBPs) and inhibiting bacterial cell wall synthesis. Its unusually long half-life (~8 hours) enables once-daily or even single-dose intramuscular (IM) dosing — a distinct clinical advantage, particularly in pediatric patients who cannot tolerate oral therapy.

The primary causative pathogens in infectious otitis media — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — fall squarely within Ceftriaxone's antibacterial spectrum. When standard oral first-line agents (amoxicillin) fail or are not tolerated, a short IM Ceftriaxone course represents a well-validated rescue strategy. The drug's pharmacokinetic profile allows it to achieve therapeutic concentrations in the middle ear despite IV/IM-only delivery.

This prediction is best characterized as a **mechanistic validation** rather than a true novel repurposing: Ceftriaxone is already used in clinical practice worldwide for treatment-refractory acute otitis media (AOM) in children. Multiple RCTs have evaluated 1-day versus 3-day IM regimens specifically for nonresponsive AOM, and clinical guidelines from the U.S. and international bodies acknowledge IM Ceftriaxone as a rescue option. The TxGNN model's high score (99.26%) reflects this well-established pharmacological connection in the knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Evaluated short-course (5-day) vs. standard (10-day) antibiotic therapy in children aged 6–23 months with AOM; aimed to assess whether reduced treatment duration could limit antimicrobial resistance while maintaining clinical efficacy |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Compared tympanostomy tube placement vs. nonsurgical management for recurrent AOM over 2 years in children; provides clinical management context for refractory and recurrent cases |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing surveillance of Prevnar 13 (13-valent pneumococcal conjugate vaccine) on AOM incidence reduction in children; documents the epidemiological burden of *S. pneumoniae*-driven otitis media |

> **Note**: None of the three registered trials directly evaluate Ceftriaxone as the study intervention for infectious otitis media. Direct efficacy evidence for Ceftriaxone in AOM is primarily available through published literature (see below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective, randomized, single-blind trial directly comparing a single IM dose of Ceftriaxone vs. 10-day oral TMP-SMZ for AOM; one of the foundational RCTs establishing Ceftriaxone as a viable single-dose rescue option |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | Compared 1-day vs. 3-day IM Ceftriaxone regimens specifically for nonresponsive AOM; evaluated both bacteriologic eradication and clinical cure rates |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical Study | *Pediatric Infectious Disease Journal* | Assessed bacteriologic efficacy of 3-day IM Ceftriaxone for nonresponsive AOM in children; established the 3-day regimen as superior for resistant organisms |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Clinical Study | *Pediatric Infectious Disease Journal* | Compared 1-day vs. 3-day IM Ceftriaxone on pneumococcal nasopharyngeal carriage dynamics in nonresponsive AOM; 3-day regimen superior for eradicating resistant *S. pneumoniae* |
| [12750572](https://pubmed.ncbi.nlm.nih.gov/12750572/) | 1998 | Clinical Trial | *Le infezioni in medicina* | Compared amoxicillin, cefuroxime axetil, and single-dose IM Ceftriaxone (50 mg/kg) in 75 pediatric AOM patients aged 6 months–6 years; no statistically significant differences in clinical efficacy among the three regimens |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int J Pediatric Otorhinolaryngology* | Analyzed factors associated with IM Ceftriaxone use for AOM in a large U.S. academic primary care population; identified increasing utilization rates pre-pandemic as a potential antimicrobial resistance marker |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Clinical Guideline | *Otology & Neurotology* | Provided expert recommendations for prevention and antimicrobial treatment of AOM and meningitis in children with cochlear implants, explicitly addressing Ceftriaxone use |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Review | *Pediatrics* | Comprehensive review on managing surgical site infections, AOM, and meningitis in cochlear implant recipients; discusses vaccination and antibiotic strategies including Ceftriaxone |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review/Guideline | *JAMA Network Open* | Assessed appropriateness of pediatric outpatient antibiotic prescribing across conditions including AOM in the U.S.; approximately 50% of prescriptions found to be unnecessary or inappropriate, with implications for Ceftriaxone stewardship |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus | *Clinical Pediatrics* | Expert roundtable consensus recommendations for daily AOM management; addressed the role of Ceftriaxone as escalation therapy for amoxicillin treatment failures |

---

## Philippines Market Information

Ceftriaxone is currently **not registered** in the Philippines. No product authorization records were found in the Philippine FDA database.

> Ceftriaxone is included on the WHO Essential Medicines List and is widely registered and used worldwide. Its absence from the Philippine market registry is notable given its global clinical importance. Standard regulatory pathways (Philippine FDA registration) would be required before this drug can be made available locally.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Formal warnings, contraindications, and drug interaction data for Ceftriaxone were not retrieved in this evidence pack (data gaps identified for both TFDA package insert text and DrugBank MOA). Key safety considerations widely documented in global literature include: cephalosporin/penicillin cross-hypersensitivity reactions (including anaphylaxis), biliary sludge and cholelithiasis (especially in neonates and premature infants, and when co-administered with IV calcium-containing solutions — a contraindicated combination), and rare Ceftriaxone-induced immune hemolytic anemia. These items should be verified from the originator package insert before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs and clinical studies directly evaluating IM Ceftriaxone for nonresponsive acute otitis media provide L2-level evidence, and the drug's antibacterial spectrum cleanly covers the primary AOM pathogens — making this one of the most scientifically credible predictions in this dataset. The absence of Philippine registration is the primary practical barrier to local use.

**To proceed, the following is needed:**
- **Regulatory**: Initiate Philippine FDA registration for Ceftriaxone through standard new drug application pathways
- **Safety data**: Download and parse the originator or TFDA package insert PDF to extract full warnings, contraindications, and drug interaction data (currently a blocking data gap)
- **MOA confirmation**: Query DrugBank API for DB01212 to formally document mechanism of action for regulatory filing
- **Local epidemiology**: Obtain Philippines-specific data on AOM pathogen distribution and antibiotic resistance patterns to confirm that local *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis* strains remain susceptible to Ceftriaxone
- **Antimicrobial stewardship**: Define a prescribing protocol (patient criteria, dosing regimen, duration) to minimize contribution to antimicrobial resistance
- **Target population scoping**: Clarify whether the intended use is pediatric rescue therapy for nonresponsive AOM or a broader indication set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

