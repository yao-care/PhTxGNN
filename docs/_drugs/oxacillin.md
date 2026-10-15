---
layout: default
title: Oxacillin
parent: Model Prediction Only (L5)
nav_order: 265
evidence_level: L5
indication_count: 4
---

# Oxacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Oxacillin: From Staphylococcus aureus Infection to Epiglottitis

## One-Sentence Summary

Oxacillin is a penicillinase-resistant penicillin, originally used for staphylococcal infections such as *Staphylococcus aureus* infection, pharyngitis, staphylococcal pneumonia and sinusitis.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Staphylococcus aureus infection (the Philippines license record contains no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on general knowledge, oxacillin is a penicillinase-resistant beta-lactam antibiotic. Its efficacy against methicillin-susceptible staphylococci is established, and mechanistically it may be applicable to bacterial infections of the upper airway.

Epiglottitis is a bacterial infection of the upper airway, and the original indications (pharyngitis, sinusitis) are also upper respiratory infections, which gives the prediction some biological plausibility. However, the usual causes of epiglottitis, such as *Haemophilus influenzae* type b and streptococci, are not well covered by oxacillin. The link therefore holds only for the staphylococcal subset of cases.

Other predictions for this drug are weaker or similar in strength:
- **Laryngitis** (score 99.73%): mostly viral and self-limiting, so the antibacterial rationale is weak. Evidence level L5, Hold.
- **Bacterial arthritis** (score 99.50%): *S. aureus* is a leading cause, and oxacillin is a standard agent for methicillin-susceptible strains. This is largely an extension of the existing indication. Evidence level L4, Research Question.
- **Urinary tract infection** (score 99.03%): the main pathogens are Gram-negative and not covered by oxacillin. Evidence level L4, Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for epiglottitis.

For reference, the closest related prediction, bacterial arthritis, has some indirect literature (no RCTs):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28900682](https://pubmed.ncbi.nlm.nih.gov/28900682/) | 2017 | Review | Curr Top Microbiol Immunol | Overview of *S. aureus* treatment and the repeated emergence of resistance to each antistaphylococcal drug class |
| [24119927](https://pubmed.ncbi.nlm.nih.gov/24119927/) | 2014 | Review | J Infect | Nafcillin/oxacillin or cefazolin remains the antibiotic of choice for MSSA bone and joint infections |
| [25672426](https://pubmed.ncbi.nlm.nih.gov/25672426/) | 2015 | Cohort | Clinics (Sao Paulo) | Clinical and epidemiological differences in septic arthritis of the knee and hip caused by oxacillin-sensitive versus -resistant *S. aureus* |
| [29129411](https://pubmed.ncbi.nlm.nih.gov/29129411/) | 2017 | Case report | Presse Med | Oxacillin-induced DRESS syndrome (adverse event) |
| [860144](https://pubmed.ncbi.nlm.nih.gov/860144/) | 1977 | Case report | South Med J | Leukopenia and granulocytopenia after high-dose intravenous oxacillin, reversible on discontinuation |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0363 | Oxacillin | Not stated | Not stated (status: cancelled) |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions**: 41 interactions were identified in total. The main moderate-level ones are:
  - Doxycycline
  - Tetracycline
  - Minocycline
  - Picosulfuric acid
  - Iodide I-131
- Clarithromycin is a minor interaction. The rest, such as proton pump inhibitors, morphine, vancomycin, prednisone and metronidazole, have no assigned severity level.
- **Reported adverse events in the literature**: DRESS syndrome and reversible leukopenia/granulocytopenia.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials or publications for epiglottitis. The main causative organisms are poorly covered by oxacillin, and the only Philippines registration has been cancelled.

**To proceed, the following is needed:**
- Clinical or microbiological evidence for oxacillin in staphylococcal epiglottitis
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Confirmation of an available marketed product and dosage form in the Philippines
- A comparison against standard empirical therapy for epiglottitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

