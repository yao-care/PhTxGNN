---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Cefazolin: predicted new indication Infectious otitis media (evidence level L4). Approved use: Bacterial pneumonia, endocarditis, bacterial arthritis, cholangitis"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Cefazolin: From Bacterial Infections to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as bacterial pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but **no clinical trials** and only **2 publications** (a review and a case report, both of limited relevance) currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, endocarditis, bacterial arthritis, cholangitis (approved indication text not available in the Philippines registration record) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on known pharmacology, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs). It is active against Gram-positive organisms such as Streptococcus and methicillin-susceptible *Staphylococcus aureus*.

Its established uses are bacterial infections of the lung, bile ducts, heart valves and joints. Some of the pathogens involved in these infections can also cause middle ear infection, which is why the model links the two. The very high TxGNN score is consistent with this antibacterial class effect, but it is not independent clinical evidence.

There are important limits. Cefazolin has limited activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, two common otitis media pathogens. It is also given only by injection, so it is not a typical first-line choice for this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy in pediatric Gradenigo syndrome, a rare complication of acute otitis media |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Stevens-Johnson syndrome management; otitis media appears only as a background illness in the case described, so it gives little direct support |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0083 | Cefazolin | Not specified | Not specified (registration status: valid) |

---

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the data compiled for this report. The moderate-level ones are:
  - Kanamycin
  - Neomycin
  - Streptomycin
  - Picosulfuric acid

  The other listed interactions (for example calcitriol, epinephrine, amphotericin B, mannitol, aspirin, amoxicillin and metformin) have an unknown severity level.
- **Disease-level contraindication signals (from the knowledge graph, not label text)**: blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and congenital prothrombin deficiency.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and the general antibacterial class effect. No clinical trials exist, and the two publications are a case report and an unrelated review. Cefazolin is parenteral only and has limited coverage of key otitis media pathogens. The only registration in the Philippines is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Evidence that cefazolin offers an advantage over standard oral or topical otitis media treatment, such as a comparative clinical study
- Clarification of the regulatory situation, since the only Philippines registration is cancelled

**Note on other predicted indications:** Among the other predictions, bronchitis (L3), chronic otitis media (L3) and suppurative otitis media (L3) have some dated, limited human data, including a 1982 comparative study in suppurative otitis media in which cefazolin served as the comparator. They are better treated as research questions than as repurposing candidates. Middle ear disease (L4) rests on indirect veterinary and microbiological data. Otosalpingitis, non-suppurative otitis media and allergic otitis media (L5) have no supporting studies. The last two are not primarily bacterial conditions, so the antibacterial rationale is weak.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

