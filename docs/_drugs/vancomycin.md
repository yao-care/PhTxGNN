---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Vancomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Vancomycin: From Gram-Positive Bacterial Infections to Streptococcal Pneumonia

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic with decades of proven clinical use against serious gram-positive bacterial infections, most notably methicillin-resistant *Staphylococcus aureus* (MRSA), enterococcal endocarditis, and *Clostridioides difficile* colitis.
Among the 10 TxGNN-predicted indications, **Streptococcal Pneumonia** (prediction rank 9) is the only mechanistically sound and clinically actionable candidate — supported by **3 clinical trials** and **20 publications** — while the remaining 9 top-ranked predictions are identified as likely graph-embedding artifacts with no plausible mechanistic basis.
This report focuses on streptococcal pneumonia, which carries an evidence level of **L3** and a **Proceed with Guardrails** recommendation.

> **Note on TxGNN ranking:** The highest-scored prediction (#1, diffuse scleroderma, score 99.92%) is flagged as a false positive — the sole supporting publication (PMID 31541072) is a sepsis case report with no relevance to scleroderma, and vancomycin has no known immunomodulatory or antifibrotic mechanism. Predictions #2–8 and #10 are similarly implausible (gram-negative organisms, metabolic/genetic disorders, or immune-mediated conditions mechanistically unrelated to antibiotics). Streptococcal pneumonia, despite its lower TxGNN rank, is the only prediction aligned with vancomycin's established mechanism of action.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious gram-positive bacterial infections (MRSA, enterococcal infections, C. difficile) |
| Predicted New Indication | Streptococcal Pneumonia (TxGNN rank 9 — highest clinically actionable prediction) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (Streptococcal Pneumonia) |

---

## Why is This Prediction Reasonable?

Vancomycin inhibits bacterial cell wall biosynthesis by binding with high affinity to the D-Ala–D-Ala terminus of nascent peptidoglycan precursors (lipid II), blocking both transglycosylation and transpeptidation. This mechanism is inherently specific to gram-positive organisms: the absence of an outer lipopolysaccharide membrane in gram-positive bacteria allows vancomycin to directly access the peptidoglycan synthesis machinery. This also explains why vancomycin is mechanistically inactive against gram-negative pathogens such as *Salmonella* and *S. typhi* — a fact that exposes predictions #2, #3, and #7 as false positives.

*Streptococcus pneumoniae* is a gram-positive diplococcus and the most common cause of community-acquired pneumonia (CAP) worldwide. Vancomycin retains full bactericidal activity against all *S. pneumoniae* strains, including those resistant to penicillin (PRSP). International guidelines — including the IDSA/ATS CAP guidelines and IDSA pneumococcal meningitis guidelines — already recommend vancomycin as a second-line or combination agent for patients with confirmed or suspected PRSP in high-resistance settings, or for penicillin-allergic patients.

This prediction is therefore not speculative: it represents a direct, mechanistically grounded extension of vancomycin's established gram-positive spectrum to an organism that is inherently susceptible. In the Philippines context, where penicillin resistance in *S. pneumoniae* has been documented in pediatric and immunocompromised populations, formalizing a local indication would directly support rational antibiotic stewardship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT05395520](https://clinicaltrials.gov/study/NCT05395520) | N/A | Unknown | 146 | Evaluates whether AUC-guided vancomycin therapeutic drug monitoring (TDM) is appropriate for serious gram-positive infections **beyond MRSA**, including streptococcal infections; directly relevant to dosing optimization and safety in streptococcal pneumonia management |
| [NCT04464291](https://clinicaltrials.gov/study/NCT04464291) | N/A | Completed | 500 | Epidemiological survey of circulating *S. pneumoniae* serotypes in Russia (post-PCV introduction, ages ≥18); provides disease burden and serotype shift context relevant to antibiotic selection |
| [NCT02538211](https://clinicaltrials.gov/study/NCT02538211) | N/A | Completed | 63 | Examined how vancomycin-induced gut microbiome depletion affects rotavirus vaccine immune responses; mechanistic context only — not directly relevant to pneumonia treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10712318](https://pubmed.ncbi.nlm.nih.gov/10712318/) | 2000 | RCT | Am J Respir Crit Care Med | Prospective randomized trial of quinupristin/dalfopristin vs. **vancomycin** for gram-positive nosocomial pneumonia (n=298); establishes vancomycin as the gold-standard comparator for gram-positive pneumonia treatment |
| [36028454](https://pubmed.ncbi.nlm.nih.gov/36028454/) | 2022 | Retrospective Cohort | Indian J Med Microbiol | Antibiotic resistance rates and penicillin MIC distribution in streptococcal pneumonia patients (2013–2019); documents the clinical scenarios requiring vancomycin escalation |
| [10501315](https://pubmed.ncbi.nlm.nih.gov/10501315/) | 1999 | Review | Semin Respir Infect | Comprehensive review of pneumococcal pneumonia treatment; explicitly recommends vancomycin as the agent of choice when penicillin resistance precludes standard β-lactam therapy |
| [11028185](https://pubmed.ncbi.nlm.nih.gov/11028185/) | 2000 | Review | Rev Med Suisse Romande | Reviews pneumococcal antibiotic resistance mechanisms and their clinical implications; contextualizes vancomycin's salvage role in PRSP management |
| [27929242](https://pubmed.ncbi.nlm.nih.gov/27929242/) | 2016 | Clinical Review | Am Fam Physician | Evidence-based CAP diagnosis and management guidelines; references vancomycin for empirical coverage of suspected drug-resistant *S. pneumoniae* in hospitalized patients |
| [21661712](https://pubmed.ncbi.nlm.nih.gov/21661712/) | 2011 | Clinical Review | Am Fam Physician | Updated CAP management in adults; supports vancomycin use for drug-resistant *S. pneumoniae* in select high-risk inpatients |
| [16735146](https://pubmed.ncbi.nlm.nih.gov/16735146/) | 2006 | Review | Am J Med | Broad review of antimicrobial resistance in gram-positive bacteria; reinforces vancomycin as a cornerstone agent against resistant streptococci and staphylococci in hospital settings |
| [35794077](https://pubmed.ncbi.nlm.nih.gov/35794077/) | 2022 | Observational | J Perinat Med | Evaluates vancomycin prescribing compliance for GBS (Group B *Streptococcus*) prophylaxis per ACOG 2019 guidelines; extends evidence of vancomycin use across clinically important streptococcal species |
| [9404765](https://pubmed.ncbi.nlm.nih.gov/9404765/) | 1997 | Review | Chest | Discusses penicillin dosing for pneumococcal pneumonia and cautions against routine vancomycin overuse — supporting its judicious reserve role specifically for genuinely resistant strains |
| [10720803](https://pubmed.ncbi.nlm.nih.gov/10720803/) | 2000 | Review | Int J Antimicrob Agents | Viridans streptococcal sepsis and pneumonia in immunocompromised/neutropenic hosts; documents vancomycin efficacy across *Streptococcus* species including in oncology patients |

---

## Philippines Market Information

Vancomycin currently has **no Philippine FDA registrations** (0 approved licenses, not marketed). This is clinically significant given vancomycin's WHO Essential Medicine status and its irreplaceable role in treating multidrug-resistant gram-positive infections. Local regulatory gaps may expose Filipino patients to delays in accessing this drug for confirmed MRSA or PRSP infections. A formal registration submission to the Philippine FDA (Food and Drug Administration) should be considered as a priority action.

---

## Safety Considerations

Detailed local safety data (package insert warnings, contraindications, drug interaction records) were not available in the current evidence dataset.

Please refer to the vancomycin package insert for complete safety information. Based on the published literature, clinicians should be aware of the following well-documented safety signals with intravenous vancomycin:

- **Nephrotoxicity**: Risk increases with high trough levels, prolonged therapy, or co-administration of other nephrotoxic agents; AUC-guided TDM is now preferred over trough-only monitoring
- **Ototoxicity**: Auditory and vestibular toxicity, particularly at high doses or in patients with pre-existing hearing impairment
- **Red Man Syndrome**: Histamine-mediated infusion reaction (flushing, erythema, hypotension) mitigated by slowing the infusion rate to ≥60 minutes
- **Renal monitoring**: Serum creatinine and vancomycin AUC/MIC ratio should be monitored during therapy

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Streptococcal Pneumonia only)*

---

**Overall Prediction Landscape — Summary of Hold Decisions:**

| Rank | Disease | Reason for Hold |
|------|---------|----------------|
| 1 | Diffuse scleroderma | No immune/antifibrotic MOA; sole publication is an unrelated sepsis case report; likely graph-embedding false positive |
| 2 | Paratyphoid fever | Gram-negative pathogen (*Salmonella* Paratyphi); vancomycin mechanistically inactive due to outer membrane barrier |
| 3 | Salmonellosis | Gram-negative organism; vancomycin has no intrinsic activity; statistical co-occurrence artifact in TxGNN |
| 4 | Congenital analbuminemia | Genetic metabolic disorder (ALB mutation); albumin replacement is standard of care; no mechanistic link |
| 5 | Polyclonal hyperviscosity syndrome | Immunoglobulin-mediated disorder; no mechanism by which an antibiotic would reduce immunoglobulin overproduction |
| 6 | Hyperamylasemia | Vancomycin nephrotoxicity may **worsen** amylase clearance — this is a potential adverse effect direction, not a therapeutic one |
| 7 | Typhoid fever | *Salmonella typhi* is gram-negative; standard treatment is fluoroquinolones or ceftriaxone; no evidence base |
| 8 | Blood group incompatibility | ABO/Rh immune-mediated hemolysis; requires exchange transfusion or immunosuppression; antibiotics are irrelevant |
| 10 | Premalignant hematological disease | Vancomycin may be used prophylactically in immunosuppressed hematology patients, but this is supportive care, not a repurposing indication |

---

**Rationale for Streptococcal Pneumonia (Proceed with Guardrails):**
Vancomycin's mechanism of action directly targets *S. pneumoniae* cell wall synthesis, and its role in penicillin-resistant pneumococcal pneumonia is already established in international clinical guidelines. The Philippines market gap — currently no registered vancomycin products — represents a critical unmet need and a clear regulatory pathway for submission.

**To proceed, the following is needed:**

- **Philippine FDA registration dossier**: Initiate a full or abbreviated registration submission; leverage WHO Essential Medicine status to support expedited review
- **Local resistance epidemiology**: Obtain Philippine Antimicrobial Resistance Surveillance System (ARSP) data on PRSP prevalence to quantify clinical need and define target patient populations
- **TDM infrastructure assessment**: AUC-guided monitoring (supported by NCT05395520) requires trained clinical pharmacists and local laboratory capacity — assess readiness before widespread deployment
- **Complete MOA and safety documentation**: Retrieve full pharmacology and safety data from DrugBank and the Philippine FDA's reference product dossier to support the registration submission
- **Antibiotic stewardship framework**: Define clear criteria for vancomycin initiation (culture-confirmed PRSP, penicillin allergy with anaphylaxis risk) to prevent overuse, consistent with IDSA and WHO stewardship recommendations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

