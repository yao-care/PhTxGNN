---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefuroxime: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Infectious otitis media, bacterial pneumonia, bacterial meningitis…"
monitor_inn: "Cefuroxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Cefuroxime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for bacterial infections such as otitis media, pneumonia, meningitis, gonorrhea and Lyme disease.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this top-ranked prediction.
The prediction is graph-based only, and a more evidence-supported candidate (urinary tract infection) is described below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Infectious otitis media, bacterial pneumonia, bacterial meningitis, gonorrhea, Lyme disease and other bacterial infections (the licence record in the Philippines contains no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefuroxime is a cephalosporin, a class that kills bacteria by inhibiting cell-wall synthesis. Its efficacy in bacterial infections is established.

For polyclonal hyperviscosity syndrome, no plausible mechanistic link was identified. This condition involves abnormally thick blood caused by excess immunoglobulins, and an antibacterial has no known way of addressing it. The high score is most likely an artifact of the knowledge graph rather than a real pharmacological signal.

Other top-ranked predictions are similar. Hyperamylasemia, congenital analbuminemia, premalignant haematological disease and a haematological disease with peripheral neuropathy have no trials or literature, and no mechanistic basis.

The more credible candidates are infections:
- **Urinary tract infection (rank 6, L3):** cefuroxime is active against common uropathogens such as *E. coli*. This is an extension of its antibacterial use rather than a new mechanism.
- **Suppurative otitis media (rank 9, L4):** this overlaps substantially with the already-approved indication of infectious otitis media, so it is not novel repurposing.
- **Peptostreptococcus infection (rank 4, L4):** only a 1981 in-vitro study is available.

## Clinical Trial Evidence

The top-ranked prediction (polyclonal hyperviscosity syndrome) has no related clinical trials registered.

For the most evidence-supported candidate, urinary tract infection, the following trials were found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A (observational) | Completed | 973 | Outcomes of inappropriate cefuroxime therapy in adults hospitalised with pyelonephritis |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in the puerperium among women with recurrent UTI |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial prophylaxis before minimally invasive upper tract lithotomy |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Antibiotic prophylaxis for postpartum infections after caesarean section; no data |

None of these is a Phase 3 RCT testing cefuroxime for UTI treatment, and most concern prophylaxis.

## Literature Evidence

The top-ranked prediction has no related literature. For urinary tract infection, the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | Lancet Infect Dis | SIMPLIFY: de-escalation from antipseudomonal β-lactams in Enterobacterales bloodstream infection |
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Randomised comparison | Infection | Aztreonam vs cefuroxime in gram-negative upper urinary tract infections |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams for complicated UTI compared with TMP/SMX and fluoroquinolones |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil overview |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology and clinical efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime mechanisms, spectrum, pharmacokinetics and adverse reactions |

Several other UTI papers are resistance or susceptibility surveys that provide only indirect support.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0090 | Cefuroxime | Not specified | Not specified (status: cancelled) |

The only registration on record is cancelled, so cefuroxime currently has no valid single-ingredient or combination registration in the Philippines.

## Safety Considerations

- **Contraindications / disease associations (from the knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions:** 100 interactions were identified in total, and the 20 reviewed are all rated Moderate. Main groups:
  - Acid-suppressing drugs: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Antacids: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Aminoglycosides: kanamycin, neomycin
  - Other: balsalazide

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, polyclonal hyperviscosity syndrome, has no clinical or literature support and no plausible mechanism, so it is a model-only (L5) signal. The only candidates with real evidence are infections (UTI at L3, suppurative otitis media at L4). These are extensions of existing antibacterial use rather than true repurposing. The Philippines registration is cancelled, which adds a further barrier.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Mechanism of action data from DrugBank
- For UTI: a prospective comparative trial of cefuroxime treatment, together with local resistance data
- Confirmation of the cancelled registration status, and re-registration if a local indication is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

