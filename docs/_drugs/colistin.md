---
layout: default
title: Colistin
parent: Model Prediction Only (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Colistin: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Escherichia coli infection, otitis externa, external ear disease"
monitor_inn: "Colistin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
---

# Colistin
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

## Colistin: From Gram-negative Infections (Escherichia coli Infection, Otitis Externa) to Postinfectious Vasculitis
{: .text-alpha }

## One-Sentence Summary

Colistin is a polymyxin antibiotic, originally used for *Escherichia coli* infection and ear conditions such as otitis externa.
The TxGNN model's top-ranked prediction is **postinfectious vasculitis**, but this prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.
The most evidence-backed candidate in the list is **sinusitis** (rank 8), with 1 case report, 1 pharmacokinetic study and several indirect or preclinical papers, but no controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Escherichia coli* infection, otitis externa, external ear disease (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (registration cancelled) |
| Number of Registrations | 1 (0 valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Colistin is a polymyxin antibiotic that disrupts the outer membrane of Gram-negative bacteria. Its efficacy in Gram-negative infections is established, so it is mechanistically relevant only to diseases in which such bacteria are the cause or a key contributor.

For the top-ranked prediction, **postinfectious vasculitis**, there is no established link. These conditions are typically immune-mediated sequelae rather than active bacterial infection, so an antibacterial mechanism is unlikely to help. Colistin's known nephrotoxicity and neurotoxicity also argue against its use here.

Other high-scoring predictions have similar problems:
- **Post-bacterial disorder / post-infectious syndrome**: vague categories with no supporting data.
- **Chagas cardiomyopathy**: caused by a protozoan, which colistin does not plausibly target.
- **Infection-related hemolytic uremic syndrome**: antibiotics are controversial in this condition, and colistin's kidney toxicity is a major concern.
- **Infective urethral stricture**: a structural, fibrotic problem; antibacterial action would at most address secondary infection.
- **Paratyphoid fever**: the pathogen is Gram-negative, so an in vitro link is theoretical, but polymyxins are not standard therapy and established agents are preferred.

The more plausible candidates are the **sinusitis group** (sinusitis, chronic rhinosinusitis, chronic ethmoidal sinusitis). *Pseudomonas aeruginosa* is a key pathogen in cystic fibrosis-related and refractory sinus disease, and colistin is active against it. Topical or nasal delivery is conceivable, which would also fit colistin's original use in ear infections. Rank 10 (chronic ethmoidal sinusitis) has no direct data of its own and could only be extrapolated from the broader sinusitis evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

No literature exists for the top-ranked prediction (postinfectious vasculitis). The table below covers the most relevant indication with literature, **sinusitis** (rank 8). All evidence is indirect, case-level or preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | Review of therapeutic options for chronic rhinosinusitis in cystic fibrosis, a condition that is often refractory and recurs after surgery |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | Pharmacokinetic study | J Antimicrob Chemother | Measured systemic absorption of nasally administered tobramycin and colistin (as colistin sulfomethate) in CF patients, using absorption as a surrogate for safety |
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Case report | Int J Hematol | IV colistin successfully treated sinusitis, orbital cellulitis and pneumonia from multidrug-resistant *P. aeruginosa* in a leukaemia patient |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Observational (indirect) | Int Forum Allergy Rhinol | Sinus surgery improved quality of life, lung infections and lung function in primary ciliary dyskinesia |
| [33155505](https://pubmed.ncbi.nlm.nih.gov/33155505/) | 2021 | Preclinical / delivery method | Acta Otolaryngol | Autologous fibrin sealant co-delivered with antibiotics as a topical treatment after sinus surgery in CF |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | In vitro | Int J Antimicrob Agents | Colistin's bactericidal effect on *P. aeruginosa* does not depend on hydroxyl radical formation |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | In vitro | Pharmaceutics | Ceragenins with ivacaftor prevented biofilm formation by rhinosinusitis bacteria (not colistin-specific) |

The only literature for paratyphoid fever (rank 7) is a 1964 observational paper ([14126225](https://pubmed.ncbi.nlm.nih.gov/14126225/)) on typhoid and paratyphoid fever, which does not demonstrate colistin efficacy.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0117 | Colistin | Not specified | Not specified (registration cancelled) |

---

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text)**: kidney disease, pyoureter, herpes simplex infection, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis (including adult-onset), neuromuscular junction disease, geniculate herpes zoster, and myringitis bullosa hemorrhagica.
- **Class concerns**: Colistin's nephrotoxicity and neurotoxicity are major concerns, especially in kidney-involving conditions such as HUS.
- **Systemic absorption**: Nasal or topical use would require evaluation of systemic absorption.

No drug interaction data were found. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, postinfectious vasculitis, has only a model score (L5), with no trials or literature, and no plausible mechanistic link. Colistin's nephrotoxicity and neurotoxicity add further concern. The Philippines registration is also cancelled, so there is no currently valid local product. The sinusitis group (L4, indirect evidence only) is the most credible direction and could be considered a research question rather than a candidate for adoption.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (not available in the compiled data)
- Mechanism of action data from DrugBank
- For the sinusitis direction: controlled clinical studies of topical or nasal colistin, particularly in CF-related chronic rhinosinusitis with *P. aeruginosa*, plus systemic absorption and safety data
- Confirmation of whether a topical or nasal formulation is available or could be registered in the Philippines
- A review of the reason for registration cancellation and the current regulatory pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

