---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic widely used as a perioperative surgical prophylactic agent and for the treatment of gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **1 clinical trial** and **3 publications** currently supporting this direction — though significant mechanistic coverage gaps substantially limit its direct applicability to this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections / Surgical prophylaxis (first-generation cephalosporin; no Philippines registration on record) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and triggering autolytic cell death. It demonstrates strong bactericidal activity against gram-positive organisms — particularly *Staphylococcus aureus* (MSSA), Group A/B *Streptococci*, and *Streptococcus pneumoniae*.

The mechanistic link to infectious otitis media is partial. *S. pneumoniae*, one of the three primary causative organisms in acute otitis media (AOM), falls within cefazolin's spectrum. However, the other two major AOM pathogens — *Haemophilus influenzae* and *Moraxella catarrhalis* — are gram-negative organisms that cefazolin cannot reliably cover. This means effective pathogen coverage is limited to the subset of AOM cases attributable to susceptible gram-positive bacteria, which represents only a fraction of real-world AOM presentations.

An important practical constraint compounds this mechanistic gap: cefazolin is available only as an intravenous or intramuscular formulation, making it unsuitable for standard outpatient AOM management. The strongest evidence niche across all 8 TxGNN-predicted indications in this pack is **perioperative prophylaxis for otologic surgery** (Middle Ear Disease, rank 3, L2 evidence, "Proceed with Guardrails"), where IV administration is clinically appropriate and gram-positive surgical site infection prevention is the primary goal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter, randomized, double-blind, placebo-controlled trial comparing 5-day vs. 10-day antimicrobial therapy for AOM in children aged 6–23 months; the trial was terminated early before reaching its endpoints, leaving efficacy conclusions incomplete and substantially reducing the evidential weight |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Series | Ann Otol Rhinol Laryngol | Ceftazidime–cefazolin combination used as empiric therapy for pediatric Gradenigo Syndrome (petrous apicitis secondary to AOM); demonstrates cefazolin's potential role in severe otitis-related complications requiring IV antibiotics |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | South Med J | Review of cephalosporin use in pediatric infections, noting efficacy against gram-positive organisms and utility as an alternative in penicillin-hypersensitive patients |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Case report and review of Stevens-Johnson syndrome in a child; IV cefazolin was used as part of treatment for concurrent otitis media and upper airway infection, providing indirect evidence of clinical use in this context |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Cefazolin covers only *S. pneumoniae* among the three major AOM pathogens, lacks coverage against *H. influenzae* and *M. catarrhalis*, is formulated exclusively for IV/IM use, and the only relevant clinical trial was terminated early — together these factors leave the infectious otitis media indication without a viable clinical pathway.

**To proceed, the following is needed:**
- Retrieve mechanism of action data from DrugBank API (currently flagged as a High-severity Data Gap)
- Obtain the Philippines FDA package insert to assess local safety warnings, contraindications, and approved indications
- If the repurposing interest shifts toward otologic surgery prophylaxis rather than acute AOM treatment, pivot the evaluation to the **Middle Ear Disease** indication (rank 3, L2 evidence, "Proceed with Guardrails"), which has a substantially stronger mechanistic and clinical justification under ASHP/IDSA surgical prophylaxis guidelines
- Should an AOM-focused development path remain of interest, prospective clinical data targeting gram-positive AOM subpopulations in hospital settings (where IV administration is feasible) would be required to establish proof of concept
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

