---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
---

# Erythromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a classic macrolide antibiotic with proven efficacy against gram-positive bacteria and atypical intracellular pathogens (including *Chlamydia trachomatis*), widely used globally for respiratory, skin, and sexually transmitted infections — though it is currently not registered in the Philippines.
The TxGNN model predicts potential efficacy across **5 new indications**, with the top-ranked prediction being **Punctate Epithelial Keratoconjunctivitis** (score: 99.89%).
Evidence strength varies considerably: two indications — **Lymphogranuloma Venereum** (1 clinical trial, 20 publications) and **Necrotizing Ulcerative Gingivitis** (5 publications with direct clinical records of erythromycin use) — reach L3 evidence with a **Proceed with Guardrails** recommendation, while the remaining three indications stand at L4–L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (macrolide antibiotic; not registered in the Philippines) |
| Predicted New Indication (Top Rank) | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## All Predicted Indications

| Rank | Disease | TxGNN Score | Trials | Publications | Evidence Level | Decision |
|------|---------|-------------|--------|--------------|----------------|----------|
| 1 | Punctate Epithelial Keratoconjunctivitis | 99.89% | 0 | 2 | L4 | Research Question |
| 2 | Acute Contagious Conjunctivitis | 99.55% | 0 | 0 | L5 | Hold |
| 3 | Exposure Keratitis | 99.50% | 0 | 8 | L4 | Research Question |
| 4 | Lymphogranuloma Venereum | 99.05% | 1 | 20 | L3 | **Proceed with Guardrails** |
| 5 | Necrotizing Ulcerative Gingivitis | 99.00% | 0 | 5 | L3 | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank dataset. Based on well-established pharmacological information, Erythromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit and blocking peptide chain translocation. It exhibits activity against gram-positive cocci (*Staphylococcus aureus*, *S. epidermidis*, *Streptococcus pneumoniae*), some gram-negative organisms (*Haemophilus influenzae*), and critically — atypical intracellular pathogens including *Chlamydia trachomatis* and *Mycoplasma pneumoniae*.

For the **top-ranked prediction (Punctate Epithelial Keratoconjunctivitis)**, the mechanistic rationale is plausible: common causative pathogens of this condition — *S. aureus*, *S. epidermidis*, and *C. trachomatis* — all fall within erythromycin's antibacterial spectrum. Furthermore, erythromycin 0.5% ophthalmic ointment is an approved dosage form in multiple countries (including for neonatal ophthalmia prophylaxis), confirming that ocular delivery is pharmacologically feasible. However, no clinical trials or literature specifically investigate erythromycin for punctate epithelial keratoconjunctivitis, placing evidence at **L4 (mechanistic support only)**.

The most evidence-supported prediction is **Lymphogranuloma Venereum (rank 4)**. LGV is caused by *C. trachomatis* serovars L1–L3 — an organism directly susceptible to erythromycin. Historical CDC and WHO guidelines have listed erythromycin (21-day oral course) as an alternative LGV treatment regimen, with doxycycline as the current first-line and azithromycin as an accepted alternative. A 1955 clinical case series directly documents erythromycin use in early LGV (PMID: 13239093), while a 1999 UK national guideline (PMID: 10616382) explicitly includes erythromycin as an alternative antibiotic. For **Necrotizing Ulcerative Gingivitis (rank 5)**, the causative fusospirochetal complex (*Fusobacterium nucleatum*, *Treponema vincentii*) is susceptible to macrolides; a 1953 clinical report (PMID: 13221896) directly documents erythromycin use for fusospirochetal oropharyngeal infections, and the drug remains a recognized penicillin-alternative in dental antibiotic guidelines.

---

## Clinical Trial Evidence

One registered clinical trial was identified, relevant to **Lymphogranuloma Venereum (rank 4)**. No trials were registered for the remaining four indications.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03608774](https://clinicaltrials.gov/study/NCT03608774) | Phase 4 | Completed | 177 | Randomized double-blind trial comparing azithromycin vs. doxycycline for rectal *Chlamydia trachomatis* in men who have sex with men (United States). The test drug is azithromycin — a related macrolide — rather than erythromycin. Both drugs share the same 50S ribosomal target and class-level antichlamydial activity, providing indirect support for erythromycin in LGV. Direct erythromycin efficacy data was not assessed in this trial. |

---

## Literature Evidence

### Punctate Epithelial Keratoconjunctivitis (Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Clinical Review | J Pediatr Ophthalmol Strabismus | Diagnosis and management of chronic blepharokeratoconjunctivitis in children; discusses treatment approaches for overlapping keratoconjunctival inflammatory conditions — indirect contextual support |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis diagnosed by metagenomic deep sequencing in an immunocompetent adult; highlights pathogen diversity and diagnostic complexity in keratoconjunctivitis |

### Exposure Keratitis (Rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective Cohort | PLoS One | Prevalence and antibiotic susceptibility of MRSA vs. MSSA in ocular infections; documents erythromycin susceptibility patterns relevant to secondary bacterial infection management in exposure keratitis |
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective Review | PLoS One | *S. aureus* keratitis clinical features, antibiotic susceptibility, and outcomes; characterizes the primary pathogen of secondary infection in exposure keratitis |
| [21902780](https://pubmed.ncbi.nlm.nih.gov/21902780/) | 2012 | Review | Clin Exp Ophthalmol | Non-tuberculous mycobacteria ocular infections: epidemiology, risk factors, and in vitro susceptibilities; macrolide antibiotics discussed as a treatment class |
| [3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/) | 1985 | Case Report | Am J Ophthalmol | Child with conjunctivitis-related erythema multiforme treated with erythromycin 0.5% ophthalmic ointment and systemic corticosteroids; documents real-world ocular application of erythromycin ointment |

### Lymphogranuloma Venereum (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [13239093](https://pubmed.ncbi.nlm.nih.gov/13239093/) | 1955 | Clinical Case Series | Antibiotic Med Clin Ther | **Direct evidence**: Erythromycin–sulfonamide combination for early LGV treatment — earliest documented clinical use of erythromycin specifically for LGV |
| [10616382](https://pubmed.ncbi.nlm.nih.gov/10616382/) | 1999 | Clinical Guideline | Sex Transm Infect | UK national guideline for LGV management; erythromycin explicitly listed as an alternative antibiotic regimen |
| [3545650](https://pubmed.ncbi.nlm.nih.gov/3545650/) | 1987 | Review | Clin Pharm | Recognition and treatment of chlamydial infections; erythromycin cited as a first-line treatment option for genital *C. trachomatis* infections |
| [2246945](https://pubmed.ncbi.nlm.nih.gov/2246945/) | 1990 | Review | Med Clin North Am | Comprehensive *C. trachomatis* infection review; erythromycin discussed as a treatment for LGV and other chlamydial syndromes including neonatal infection |
| [22760150](https://pubmed.ncbi.nlm.nih.gov/22760150/) | 2012 | Case Report | Rev Soc Bras Med Trop | LGV case in a 17-year-old directly treated with erythromycin; subsequent diagnosis of non-Hodgkin lymphoma highlighted a diagnostic pitfall in the inguinal region |
| [33462582](https://pubmed.ncbi.nlm.nih.gov/33462582/) | 2021 | Retrospective Case Series | Clin Infect Dis | Weekly azithromycin 1 g × 3 weeks demonstrated efficacy for LGV proctitis in MSM in Europe; provides macrolide class-level support for erythromycin |
| [40815293](https://pubmed.ncbi.nlm.nih.gov/40815293/) | 2025 | Observational Study | Sex Transm Dis | LGV prevalence and treatment outcomes in gay/bisexual MSM attending STI clinics in Alberta, Canada (2018–2022); real-world macrolide treatment data |
| [25870512](https://pubmed.ncbi.nlm.nih.gov/25870512/) | 2015 | Review | Infect Drug Resist | LGV diagnostic and treatment challenges; reviews antibiotic regimens and emerging difficulties with standard doxycycline therapy |
| [30518587](https://pubmed.ncbi.nlm.nih.gov/30518587/) | 2018 | Systematic Review | BMJ Open | Systematic review of non-standard treatments for uncomplicated *C. trachomatis* infections; evaluates alternatives to first-line therapy including macrolides |
| [22335265](https://pubmed.ncbi.nlm.nih.gov/22335265/) | 2012 | Review | Am Fam Physician | Diagnosis and management of genital ulcers including LGV; treatment algorithm with antibiotic options |

### Necrotizing Ulcerative Gingivitis (Rank 5)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [13221896](https://pubmed.ncbi.nlm.nih.gov/13221896/) | 1953 | Clinical Case Series | J-Lancet | **Direct evidence**: Erythromycin (Ilotycin) for fusospirochetal infections of the oropharynx — earliest clinical documentation of erythromycin efficacy for the NUG causative organism complex |
| [4981637](https://pubmed.ncbi.nlm.nih.gov/4981637/) | 1969 | Clinical Report | Chir Dent Fr | Erythromycin ethyl succinate chewable tablets in dentistry; documents clinical value for oral and dental infections |
| [6589179](https://pubmed.ncbi.nlm.nih.gov/6589179/) | 1984 | Review | Dent Clin North Am | Antibiotics in dental practice; erythromycin listed as first-choice alternative for penicillin-allergic patients treating typical dental infections |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | Eur J Transl Myol | Antibiotic use in endodontic treatment during pregnancy; erythromycin identified as a safe alternative for penicillin-allergic pregnant patients with odontogenic infections |
| [1254998](https://pubmed.ncbi.nlm.nih.gov/1254998/) | 1976 | Review | J Laryngol Otol | Overview of oral vesiculobullous and ulcerative lesions; contextualizes oral bacterial infection management including antibiotic options for acute necrotizing gingivitis |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Lymphogranuloma Venereum and Necrotizing Ulcerative Gingivitis)
**Research Question** (Punctate Epithelial Keratoconjunctivitis and Exposure Keratitis)
**Hold** (Acute Contagious Conjunctivitis)

**Rationale:**
Erythromycin has well-established activity against the causative pathogens of LGV (*C. trachomatis*) and NUG (fusospirochetal complex), supported by direct clinical case series dating to 1953–1955, inclusion in historical treatment guidelines, and indirect evidence from macrolide-class trials — sufficient to proceed with a structured research protocol. The three ocular indications are mechanistically plausible given erythromycin's approved ophthalmic formulation globally, but they lack direct clinical trial evidence and require formal investigation before proceeding. Acute contagious conjunctivitis has zero supporting literature and should be deferred. The critical cross-cutting barrier is that erythromycin has **no current Philippines market registration**, which must be resolved before any clinical deployment.

**To proceed, the following is needed:**

- **Philippines regulatory pathway**: Investigate Philippine FDA registration requirements for erythromycin — particularly oral formulations (for LGV/NUG) and 0.5% ophthalmic ointment (for ocular indications)
- **Safety profile retrieval**: Obtain package insert to assess key warnings, contraindications, and drug interactions — currently unavailable and flagged as a blocking data gap
- **MOA documentation**: Retrieve complete DrugBank pharmacology and mechanism of action data to strengthen mechanistic rationale across all five indications
- **LGV clinical study** (Rank 4, L3 → target L2): Design a randomized trial comparing erythromycin to doxycycline for LGV in the Philippine context, with particular focus on populations where doxycycline is contraindicated (e.g., pregnancy)
- **NUG clinical study** (Rank 5, L3 → target L2): Conduct a prospective cohort study evaluating erythromycin vs. metronidazole ± amoxicillin for NUG in penicillin-allergic patients in Philippine dental clinics
- **Ophthalmic indications** (Ranks 1 & 3, L4 → target L3): Confirm ophthalmic formulation availability and supply chain in the Philippines; design a pilot clinical trial for punctate epithelial keratoconjunctivitis with microbiological confirmation of susceptible pathogens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

