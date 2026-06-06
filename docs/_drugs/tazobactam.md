---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 2
---

# Tazobactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Tazobactam: From Beta-Lactamase Inhibitor to Pneumonia Treatment

## One-Sentence Summary

Tazobactam is a β-lactamase inhibitor that is always co-administered with partner β-lactam antibiotics (most notably piperacillin and ceftolozane) to protect them from enzymatic degradation by resistant bacteria; it has no registered standalone indication in the Philippines.
The TxGNN model predicts it may be effective for **Pneumonia**, with **50 clinical trials** and **20 publications** currently supporting this direction.
Evidence quality is exceptionally high, as numerous Phase 3 RCTs have already validated tazobactam-containing combinations (Pip/Taz and Ceftolozane/Taz) as standard-of-care regimens for hospital-acquired and ventilator-associated pneumonia worldwide.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No standalone registration; used as a β-lactamase inhibitor component in fixed-dose combination antibiotics |
| Predicted New Indication | Pneumonia (hospital-acquired / ventilator-associated) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs for tazobactam-containing regimens) |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tazobactam (DrugBank DB01606) is a penicillanic acid sulfone β-lactamase inhibitor. It does not kill bacteria on its own; instead, it irreversibly binds and inactivates a broad spectrum of β-lactamases — including Ambler class A enzymes such as TEM, SHV, and CTX-M extended-spectrum β-lactamases (ESBLs) — produced by Gram-negative pathogens. By shielding the co-administered β-lactam from hydrolysis, tazobactam restores and amplifies bactericidal activity against organisms that would otherwise be resistant.

Hospital-acquired pneumonia (HAP) and ventilator-associated pneumonia (VAP) are predominantly caused by Gram-negative pathogens (Pseudomonas aeruginosa, Klebsiella pneumoniae, Enterobacterales) that frequently produce β-lactamases. The biological rationale for the TxGNN prediction is therefore mechanistically straightforward: by inhibiting the primary resistance mechanism of these organisms, tazobactam enables its partner β-lactam to penetrate and destroy the offending pathogen in the lung. Piperacillin/tazobactam has been a guideline-endorsed empirical option for HAP/VAP for decades, and ceftolozane/tazobactam received FDA approval in 2019 specifically for ventilated nosocomial pneumonia caused by susceptible Gram-negative bacteria, including multidrug-resistant (MDR) Pseudomonas aeruginosa.

The prediction score of 99.46% reflects the TxGNN knowledge graph's recognition that tazobactam's molecular interactions in the drug–disease network are tightly linked to respiratory bacterial infections, fully consistent with its real-world clinical trajectory. The absence of a Philippines registration is a market access gap rather than a scientific concern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | ASPECT-NP pivotal trial: ceftolozane/tazobactam non-inferior to meropenem for Day-28 all-cause mortality in ventilated nosocomial pneumonia (VABP/HABP) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP — confirmed PIP/TAZ as active comparator benchmark |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational RESTORE-IMI 2 China extension: IMI/REL non-inferior to PIP/TAZ for HABP/VABP by Day-28 all-cause mortality |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin 750 mg od vs piperacillin/tazobactam 4 g/500 mg q8h for mild-to-moderate HAP — non-inferiority demonstrated |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Pharmacokinetic comparison of 4-hour prolonged vs 1-hour standard infusion of ceftolozane/tazobactam 2 g TID for VAP due to Pseudomonas aeruginosa in ICU |
| [NCT04673175](https://clinicaltrials.gov/study/NCT04673175) | Phase 4 | Terminated | 17 | Ceftolozane/tazobactam plus rapid molecular diagnostics for MDR Pseudomonas bacteremia/pneumonia in haematological malignancy patients — terminated early due to low enrolment |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | PK, safety and tolerability of ceftolozane/tazobactam in paediatric patients with nosocomial pneumonia — supports dose extrapolation to children |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Multi-centre PK study defining individualised dosing regimens (including piperacillin/tazobactam) to maximise target attainment for ICU pneumonia |
| [NCT03897582](https://clinicaltrials.gov/study/NCT03897582) | N/A | Recruiting | 65 | Beta-lactam (including pip/taz) dosing optimisation for ICU pneumonia patients undergoing continuous renal replacement therapy — addresses a critical PK/PD gap |
| [NCT05102162](https://clinicaltrials.gov/study/NCT05102162) | Phase 4 | Terminated | 35 | Beta-lactam continuous vs intermittent infusion for severe Gram-negative pneumonia (meropenem, cefepime, piperacillin/tazobactam) — assessing bacterial resistance emergence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT (Phase 3) | The Lancet Infectious Diseases | ASPECT-NP: ceftolozane/tazobactam non-inferior to meropenem for Gram-negative nosocomial pneumonia; supports approval for VAP/HABP |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT (Phase 3) | Clinical Infectious Diseases | RESTORE-IMI 2: IMI/REL vs PIP/TAZ for HABP/VABP — piperacillin/tazobactam confirmed as valid reference standard with robust clinical data |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT (Phase 3) | International Journal of Infectious Diseases | IMI/REL non-inferior to PIP/TAZ in critically ill HABP/VABP patients — further validates pip/taz as guideline comparator |
| [10353303](https://pubmed.ncbi.nlm.nih.gov/10353303/) | 1999 | Review | Drugs | Comprehensive review of piperacillin/tazobactam: established efficacy for lower respiratory tract infections; broad Gram-positive, Gram-negative and anaerobic spectrum |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Review of Anti-infective Therapy | Ceftolozane/tazobactam for HAP: most active anti-pseudomonal agent including MDR/XDR strains; clinical/microbiological success >70–80% |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Revista Española de Quimioterapia | Ceftolozane/tazobactam in nosocomial pneumonia: MIC and MPC values narrow, reducing mutant selection; time-dependent pharmacokinetics favour extended infusion |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review / Network meta-analysis | Clinical Microbiology and Infection | Optimal empiric antibiotic regimens for non-VAP HAP: piperacillin/tazobactam among the best-supported options across RCTs |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Observational | Clinical Infectious Diseases | Resistance development in MDR Pseudomonas bacteremia/pneumonia: ceftolozane-tazobactam had lower resistance emergence (10%) vs ceftazidime-avibactam (40%) |
| [38936906](https://pubmed.ncbi.nlm.nih.gov/38936906/) | 2024 | Clinical study | In Vivo | Prophylactic mini-tracheostomy plus perioperative tazobactam/piperacillin significantly reduced pneumonia incidence in high-risk post-oesophagectomy patients |
| [34158237](https://pubmed.ncbi.nlm.nih.gov/34158237/) | 2021 | Retrospective cohort (PSM) | Journal of Infection and Chemotherapy | Aspiration pneumonia: ceftriaxone comparable to piperacillin/tazobactam or carbapenems — useful for de-escalation strategy context |

---

## Philippines Market Information

Tazobactam has **no registered products** with the Philippine FDA (FDA-Philippines). There are 0 active licenses on record. Any clinical use in the Philippines would require formal registration of a tazobactam-containing combination product (e.g., piperacillin/tazobactam or ceftolozane/tazobactam) before deployment.

---

## Safety Considerations

Full safety data (key warnings, contraindications, drug interactions) was not retrievable from the current data sources for this Evidence Pack. The DDI query returned no results, and FDA-Philippines package insert data was not available.

Based on general knowledge of tazobactam-containing combinations from global regulatory approvals:
- Tazobactam is generally well tolerated; adverse events are primarily attributable to the partner β-lactam.
- Common reactions with piperacillin/tazobactam include diarrhoea, nausea, skin rash, and elevated liver enzymes.
- Risk of *Clostridioides difficile*-associated disease exists, as with all broad-spectrum antibiotics.
- Renal dose adjustment is required for combinations (e.g., ceftolozane/tazobactam carries a warning for reduced efficacy in patients with creatinine clearance 30–50 mL/min due to acute kidney injury).

> Please refer to the current package insert of the relevant tazobactam-containing combination product for full prescribing information, warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for tazobactam in pneumonia is supported by the highest level of clinical evidence (L1): multiple completed Phase 3 RCTs have established tazobactam-containing combinations (piperacillin/tazobactam and ceftolozane/tazobactam) as standard-of-care reference arms or approved treatments for hospital-acquired and ventilator-associated bacterial pneumonia globally. The prediction reflects a mechanistically sound and clinically validated indication. The principal barrier to use in the Philippines is a registration gap, not a scientific one.

**To proceed, the following is needed:**

- **Philippines FDA registration** of a tazobactam-containing fixed-dose combination product (priority: piperacillin/tazobactam 4.5 g IV, and/or ceftolozane/tazobactam 1.5 g IV) via the FDA-Philippines Center for Drug Regulation and Research (CDRR)
- **Local package insert and prescribing information** for any combination product registered, including Filipino-language patient information if required
- **Mechanism of action documentation** (DrugBank API query for DB01606) to complete the pharmacological profile and support educational materials for Philippine prescribers
- **Safety monitoring plan** covering renal function monitoring (dose adjustment for CrCl < 50 mL/min), hepatic enzyme surveillance, and *C. difficile* surveillance protocols
- **Antimicrobial stewardship framework** for deployment in Philippine ICU/hospital settings, given the risk of selecting for carbapenem-resistant organisms if piperacillin/tazobactam is over-used in ESBL infections (per the MERINO trial signal, PMID 30208454)
- **Local resistance surveillance data** (Philippine antimicrobial resistance data from the Antimicrobial Resistance Surveillance Program, ARSP) to confirm that target pathogens in Philippine HAP/VAP remain susceptible to tazobactam-containing regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

