---
layout: default
title: Oxacillin
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 4
---

# Oxacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxacillin: From MSSA Infections to Epiglottitis

## One-Sentence Summary

Oxacillin is an isoxazolyl penicillin antibiotic with established bactericidal activity against methicillin-susceptible *Staphylococcus aureus* (MSSA), widely used globally for serious staphylococcal infections despite having no current registration in the Philippines.
The TxGNN model predicts it may be effective for **epiglottitis**, with **0 registered clinical trials** and **3 case-level publications** currently available to support this direction.
The mechanistic rationale is conditional — Oxacillin covers only the *S. aureus* subset of epiglottitis pathogens, making single-agent use insufficient for empiric coverage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; globally used for MSSA infections (skin/soft tissue infections, bacteremia, endocarditis, osteomyelitis) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Oxacillin is a beta-lactamase–resistant isoxazolyl penicillin that exerts bactericidal activity by binding penicillin-binding proteins (PBPs) and blocking bacterial cell wall transpeptidation. Its resistance to staphylococcal beta-lactamase is its defining clinical advantage — it retains activity against MSSA in situations where ampicillin or amoxicillin would fail.

Acute epiglottitis is a potentially life-threatening upper airway infection. In the pre-vaccine era, *Haemophilus influenzae* type b (Hib) was the dominant pathogen. Following widespread Hib vaccination, the microbiological profile has shifted: *Staphylococcus aureus* and *Streptococcus* species now account for a growing proportion of adult cases. Because Oxacillin is specifically active against MSSA, the TxGNN prediction reflects this evolving epidemiology — it is mechanistically coherent for the MSSA subset of epiglottitis.

The critical limitation is spectrum. *H. influenzae* is intrinsically resistant to Oxacillin, and empiric management of epiglottitis typically requires broad-spectrum IV coverage (e.g., a 3rd-generation cephalosporin with or without antistaphylococcal coverage). Oxacillin as a single agent would only be clinically appropriate if *S. aureus* is microbiologically confirmed — a scenario requiring culture results that may not be available during the acute airway emergency. The prediction is mechanistically plausible but clinically narrow, and does not support empiric monotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Oxacillin in epiglottitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4999568](https://pubmed.ncbi.nlm.nih.gov/4999568/) | 1971 | Case Series | British Medical Journal | Retrospective review of epiglottitis in adults; describes clinical presentation, microbiology, and management in pre-vaccine era |
| [990756](https://pubmed.ncbi.nlm.nih.gov/990756/) | 1976 | Case Report | British Medical Journal | Adult epiglottitis requiring emergency tracheostomy; highlights severity and need for urgent airway management |
| [3380744](https://pubmed.ncbi.nlm.nih.gov/3380744/) | 1988 | Case Report | Pediatric Emergency Care | Epiglottitis in a child with asthma presenting as refractory respiratory failure; discusses differential diagnosis, sedation, paralysis, and intubation management |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Oxacillin in epiglottitis is limited to 3 older case-level publications (1971–1988) with no registered clinical trials, none of which directly evaluate Oxacillin efficacy. The mechanistic link is conditional on confirmed MSSA as the causative pathogen, which substantially limits applicability in the acute empiric setting where broad-spectrum coverage is required.

**To proceed, the following is needed:**

- **Microbiological prevalence data:** Establish what proportion of epiglottitis cases in the target population are caused by MSSA, to determine whether a narrow-spectrum agent like Oxacillin has a realistic clinical role
- **MOA data (DrugBank API):** Retrieve complete pharmacodynamic/pharmacokinetic profile to fully assess tissue penetration at the epiglottic site
- **Safety package:** Obtain Philippines-relevant package insert or equivalent (TFDA/EMA/FDA) to complete S1 safety screening before further development
- **Attention to higher-ranked indication:** Among the 4 TxGNN-predicted indications in this Evidence Pack, **bacterial arthritis (rank 3, L2 evidence, "Proceed with Guardrails")** carries substantially stronger clinical and trial-level support, including a completed Phase 4 RCT (NCT04563325) and literature directly comparing oxacillin-sensitive vs. resistant strains (PMID 25672426) — this indication may be a more productive near-term research priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

