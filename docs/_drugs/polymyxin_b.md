---
layout: default
title: Polymyxin B
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 3
---

# Polymyxin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Polymyxin B: From MDR Gram-Negative Infections to Bacterial Conjunctivitis

## One-Sentence Summary

Polymyxin B is a last-resort cyclic lipopeptide antibiotic primarily used against multidrug-resistant (MDR) gram-negative bacteria — including *Pseudomonas aeruginosa* and *Acinetobacter baumannii* — in critically ill patients.

The TxGNN model predicts efficacy across three indications: **Bronchitis** (Rank 1, 99.87%), **Laryngotracheitis** (Rank 2, 99.62%), and **Bacterial Conjunctivitis** (Rank 3, 99.06%). Despite ranking third by TxGNN score, the conjunctivitis indication carries the strongest clinical evidence — supported by **3 completed clinical trials** (including a Phase 4 RCT) and **20 publications** featuring multiple RCTs — making it the sole actionable candidate, while the bronchitis and laryngotracheitis predictions face significant mechanistic and safety barriers.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MDR gram-negative bacterial infections (systemic, last-resort antibiotic use) |
| Predicted New Indications | Bronchitis (Rank 1) · Laryngotracheitis (Rank 2) · Bacterial Conjunctivitis (Rank 3) |
| TxGNN Prediction Scores | 99.87% · 99.62% · 99.06% |
| Evidence Levels | Bronchitis: L3 · Laryngotracheitis: L5 · Conjunctivitis: L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Bronchitis: **Hold** · Laryngotracheitis: **Hold** · Conjunctivitis: **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Polymyxin B is a cyclic lipopeptide that binds to the lipid A component of lipopolysaccharide (LPS) in the outer membrane of gram-negative bacteria, disrupting membrane integrity and causing cell death. Its antibacterial spectrum is narrow — limited to gram-negative organisms — and it is used clinically as a last-resort agent when carbapenem-resistant strains leave few alternatives.

**Bronchitis (Rank 1 — Hold):** Bacterial bronchitis caused by MDR gram-negative pathogens represents a theoretical niche for Polymyxin B, particularly via aerosol delivery. However, this is where mechanism turns against the indication: inhaled Polymyxin B directly triggers mast cell degranulation and histamine release, inducing bronchoconstriction — precisely the opposite of what bronchitis treatment requires. The available literature is almost entirely restricted to ventilator-associated tracheobronchitis (VAT) in intubated ICU patients, which is a fundamentally different clinical context from outpatient or general bacterial bronchitis.

**Laryngotracheitis (Rank 2 — Hold):** The vast majority of laryngotracheitis (croup) cases are caused by Parainfluenza viruses, against which Polymyxin B has no activity whatsoever. Even in bacterial tracheitis — a rare, severe form — the dominant pathogen is *Staphylococcus aureus* (gram-positive), which is entirely outside Polymyxin B's spectrum. The TxGNN high score likely reflects knowledge graph proximity among respiratory tract diseases rather than a direct mechanistic link.

**Bacterial Conjunctivitis (Rank 3 — Proceed with Guardrails):** The Polymyxin B/Trimethoprim combination (Polytrim®) represents a pharmacologically coherent pairing: Polymyxin B disrupts the outer membranes of gram-negative conjunctival pathogens (*Haemophilus influenzae*, *Pseudomonas aeruginosa*), while Trimethoprim inhibits dihydrofolate reductase with broader gram-positive and gram-negative coverage. Together they address the two most common bacterial causes of pediatric conjunctivitis — *H. influenzae* and *Streptococcus pneumoniae*. Crucially, topical ophthalmic delivery achieves high local drug concentrations while systemic absorption remains negligible, yielding a favorable safety profile. This combination is already approved for bacterial conjunctivitis in the United States, Europe, and multiple Asian markets; introduction to the Philippines would represent a market entry rather than a novel repurposing.

---

## Clinical Trial Evidence

### Bacterial Conjunctivitis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Single-blinded RCT directly comparing Polytrim (Polymyxin B/Trimethoprim) vs. Moxifloxacin for treatment of acute pediatric bacterial conjunctivitis — core head-to-head efficacy trial |
| [NCT01227863](https://clinicaltrials.gov/study/NCT01227863) | Phase 3 | Unknown | 70 | RCT comparing two branded Polymyxin B/Neomycin/Dexamethasone products (Maxinom® vs. Maxitrol®) in acute bacterial conjunctivitis; involves Polymyxin B but as a three-drug combination — Polymyxin B's individual contribution cannot be isolated |
| [NCT01809483](https://clinicaltrials.gov/study/NCT01809483) | Phase 3 | Completed | 32 | Corneal erosion management trial in which Polymyxin B may be used as adjunct infection prophylaxis — not a direct conjunctivitis efficacy trial; low relevance |

### Bronchitis

Currently no clinical trials registered specifically for Polymyxin B in bronchitis.

### Laryngotracheitis

Currently no clinical trials registered for Polymyxin B in laryngotracheitis.

---

## Literature Evidence

### Bacterial Conjunctivitis (Priority Indication — L1)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2540136](https://pubmed.ncbi.nlm.nih.gov/2540136/) | 1989 | Comparative RCT (pooled) | J Antimicrobial Chemotherapy | Pooled analysis of 4 RCTs (528 patients): Trimethoprim-Polymyxin B vs. Chloramphenicol ointment for bacterial conjunctivitis — efficacy and safety comparable across all four studies |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | RCT | Current Medical Research & Opinion | 42-patient double-blind RCT: Trimethoprim-Polymyxin B sulphate ointment vs. Chloramphenicol — both effective and well tolerated, no statistically significant differences |
| [2370842](https://pubmed.ncbi.nlm.nih.gov/2370842/) | 1990 | RCT | Medical Letter on Drugs & Therapeutics | Early pivotal RCT establishing Trimethoprim-Polymyxin B as first-line therapy for bacterial conjunctivitis |
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT | Journal of Pediatrics | Single-blinded RCT comparing Polymyxin B-Trimethoprim vs. Moxifloxacin for acute pediatric conjunctivitis — establishes non-inferiority to newer fluoroquinolone |
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatric Ophthalmology & Strabismus | Moxifloxacin vs. Polymyxin B/Trimethoprim in pediatric bacterial conjunctivitis — comparative clinical and bacteriological outcomes |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | Multicenter RCT | J Pediatric Ophthalmology & Strabismus | Multicenter trial on speed of clinical efficacy: Polymyxin B/Trimethoprim vs. Moxifloxacin 0.5% ophthalmic solution |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | Randomized Clinical Study | J Antimicrobial Chemotherapy | 230-patient multicentre trial: Trimethoprim-Polymyxin B vs. Neomycin-Polymyxin B-Gramicidin vs. Chloramphenicol — all three effective with minimal adverse events |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey/Retrospective | Clinical Therapeutics | Survey of pediatric patients treated with Trimethoprim-Polymyxin B; supports empiric use against *H. influenzae* and *S. pneumoniae* — the two primary pediatric conjunctivitis pathogens |
| [26922212](https://pubmed.ncbi.nlm.nih.gov/26922212/) | 2016 | Safety Report | Annals of Allergy, Asthma & Immunology | Case report of anaphylaxis to Polymyxin B-Trimethoprim eye drops — important rare safety signal requiring pharmacovigilance monitoring |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | Comparative review of 16 topical ophthalmic antibacterial preparations; Polymyxin B characterized as gram-negative selective, complementary to trimethoprim's broader coverage |

### Bronchitis (Rank 1 — L3, Hold)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Comparative Observational | Infection | Polymyxin B vs. other antimicrobials in ventilator-associated pneumonia and tracheobronchitis caused by *P. aeruginosa* or *A. baumannii* — ICU/ventilated patients only, not generalizable to community bronchitis |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Retrospective Cohort | Diagnostic Microbiology & Infectious Disease | 19 patients treated with inhaled Polymyxin B for MDR gram-negative respiratory infections (14 pneumonia, 5 tracheobronchitis); limited sample, no control arm |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case Series | Journal of the Kansas Medical Society | Systemic gentamicin + Polymyxin B aerosol in Pseudomonas tracheobronchitis — early case series with no comparator |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Safety Report | Annals of Internal Medicine | Documents hazards of Polymyxin B inhalation — critical safety signal showing direct bronchoconstriction risk via aerosol route |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Experimental/Case Series | Chest | Early experimental observations on endobronchial Polymyxin B administration in chronic bronchitis — foundational but methodologically dated |

---

## Philippines Market Information

Polymyxin B is currently **not registered** with the FDA Philippines. There are **no existing product licenses**, no approved dosage forms, and no authorized indications on record.

Any clinical development or commercialization of Polymyxin B in the Philippines — for any indication — would require initiation of a full new drug registration process. For the conjunctivitis indication specifically, reference to approved products in markets such as the United States (Polytrim®) or the European Union could support a bridging registration strategy.

---

## Safety Considerations

**No DDI data is available** from queried sources (query returned 0 results). Key safety signals identified from the literature review:

- **Inhalation Route — Bronchoconstriction Risk**: Inhaled Polymyxin B directly induces mast cell degranulation and histamine release, causing bronchoconstriction. This represents a serious hazard for the bronchitis indication and is documented in safety literature (PMID [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/)).
- **Ophthalmic Route — Anaphylaxis**: Rare anaphylaxis to Polymyxin B/Trimethoprim ophthalmic drops has been reported (PMID [26922212](https://pubmed.ncbi.nlm.nih.gov/26922212/)). Post-marketing surveillance for hypersensitivity reactions is warranted.
- **Systemic Use**: Well-documented nephrotoxicity and neurotoxicity (peripheral neuropathy, neuromuscular blockade) with intravenous Polymyxin B are not relevant to the topical ophthalmic formulation.

Warnings and contraindications from the Philippines FDA package insert (local label) could not be retrieved and should be consulted before any clinical or regulatory decision.

---

## Conclusion and Next Steps

### Indication 1 — Bronchitis

**Decision: Hold**

**Rationale:**
Existing evidence is limited to observational studies in ICU-ventilated patients with ventilator-associated tracheobronchitis — a context fundamentally different from general bacterial bronchitis. More critically, the delivery route required for direct bronchial antimicrobial action (inhalation) carries a documented safety risk of bronchoconstriction in the target patient population.

**To proceed, the following is needed:**
- Safety data specifically evaluating inhaled Polymyxin B formulations in non-intubated bronchitis patients
- Randomized controlled trial data in community-acquired or non-VAT bacterial bronchitis
- Pharmacokinetic data for aerosol delivery with bronchoconstriction mitigation strategies (e.g., pretreatment with bronchodilators)

---

### Indication 2 — Laryngotracheitis

**Decision: Hold**

**Rationale:**
No clinical evidence exists for Polymyxin B in laryngotracheitis. The dominant etiology (Parainfluenza virus-driven croup) is entirely outside Polymyxin B's antibacterial spectrum, and the drug lacks activity against gram-positive bacteria (*S. aureus*) that cause the more severe bacterial tracheitis subtype.

**To proceed, the following is needed:**
- Any preclinical or clinical feasibility data linking Polymyxin B to laryngotracheitis pathogens
- Identification of a gram-negative MDR bacterial tracheitis patient population where Polymyxin B may offer incremental benefit

---

### Indication 3 — Bacterial Conjunctivitis

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed RCTs — including a Phase 4 head-to-head trial and pooled analysis of four trials with 528 patients — demonstrate that Polymyxin B/Trimethoprim (Polytrim®) is effective and well-tolerated for bacterial conjunctivitis, with efficacy comparable to both chloramphenicol and newer fluoroquinolones. This combination is already approved and widely used in major international markets.

**To proceed, the following is needed:**
- Initiation of FDA Philippines new drug registration for Polymyxin B/Trimethoprim ophthalmic solution, utilizing existing international RCT data as primary evidence
- Local antibiogram data confirming susceptibility of Philippine conjunctivitis-associated pathogens (*H. influenzae*, *S. pneumoniae*, *P. aeruginosa*) to Polymyxin B
- Pharmacovigilance plan monitoring for rare hypersensitivity/anaphylaxis reactions in the local population
- Formal MOA documentation (DrugBank API query recommended) for the regulatory submission dossier
- Local clinical specialist review (ophthalmology, infectious disease) before product launch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

