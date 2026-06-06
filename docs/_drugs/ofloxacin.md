---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Septicemic Plague

## One-Sentence Summary

Ofloxacin is a second-generation fluoroquinolone antibiotic — the racemic precursor to levofloxacin — used for a broad spectrum of bacterial infections through inhibition of bacterial DNA gyrase and Topoisomerase IV.
The TxGNN model generated **10 predicted new indications**; the most evidence-supported actionable target is **Septicemic Plague**, backed by direct preclinical data with Ofloxacin itself and FDA approval of its active L-isomer (levofloxacin) for plague treatment under the Animal Efficacy Rule.
Of the 10 predictions, **2 reached "Proceed with Guardrails" status** (Evidence Level L3): septicemic plague (Rank #8) and punctate epithelial keratoconjunctivitis (Rank #10); the remaining 8 are assessed as Hold due to false-positive biological plausibility or known adverse-effect reversal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum fluoroquinolone antibiotic; no Philippines FDA registration on file) |
| Most Actionable Predicted Indication | Septicemic Plague (Rank #8 by actionable evidence) |
| TxGNN Prediction Score (Rank #8) | 99.79% |
| Evidence Level | L3 — preclinical animal studies + fluoroquinolone class FDA/CDC/WHO guideline endorsement |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (septicemic plague, PEK); **Hold** (8 of 10 predictions) |

---

## Prediction Summary: All 10 Indications

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Rationale |
|------|---------|-------------|----------------|----------|---------------|
| 1 | Hyperamylasemia | 99.91% | L5 | Hold | Fluoroquinolones are known to *induce* drug-related pancreatitis — the mechanism is adverse, not therapeutic |
| 2 | Polyclonal Hyperviscosity Syndrome | 99.91% | L5 | Hold | No biological link between antimicrobial mechanism and immunoglobulin-driven hyperviscosity |
| 3 | Congenital Analbuminemia | 99.90% | L5 | Hold | Monogenic (*ALB*) disorder; antibiotics cannot correct genetic albumin deficiency |
| 4 | Blood Group Incompatibility | 99.86% | L5 | Hold | Antigen–antibody immune reaction; 2 retrieved papers are unrelated to this indication |
| 5 | Premalignant Hematological Disease | 99.84% | L5 | Hold | Genetic/epigenetic origin (MDS, MGUS); no antimicrobial mechanism applicable |
| 6 | Monoclonal Gammopathy | 99.82% | L4 | Hold | 20 papers cover levofloxacin *infection prophylaxis* in myeloma patients — not disease-modifying treatment of gammopathy itself |
| 7 | Hematological Disease + Peripheral Neuropathy | 99.80% | L5 | Hold | ⚠️ **FDA Black Box Warning**: fluoroquinolones *cause* irreversible peripheral neuropathy — contraindicated direction |
| **8** | **Septicemic Plague** | **99.79%** | **L3** | **Proceed with Guardrails** | Direct preclinical evidence with Ofloxacin; levofloxacin (active isomer) FDA-approved for plague under Animal Efficacy Rule |
| 9 | Congenital Hematological Disorder | 99.72% | L5 | Hold | Hereditary structural defects (sickle cell, hemophilia, thalassemia); antibiotics cannot correct genetic dysfunction |
| **10** | **Punctate Epithelial Keratoconjunctivitis** | **99.57%** | **L3** | **Proceed with Guardrails** | FDA-approved Ofloxacin 0.3% ophthalmic formulation applicable to bacterial-etiology PEK |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Ofloxacin is a fluoroquinolone antibiotic — the racemic mixture containing equal parts of the active L-isomer (levofloxacin) and the largely inactive D-isomer. It kills bacteria by inhibiting two essential topoisomerases: DNA gyrase (GyrA/GyrB subunits) and Topoisomerase IV (ParC/ParE subunits), thereby blocking DNA replication, transcription, and repair. This dual-target mechanism is bactericidal across a wide range of Gram-negative and Gram-positive organisms.

**For Septicemic Plague:** The prediction is mechanistically direct. *Yersinia pestis*, the causative agent of all three forms of plague, is exquisitely susceptible to fluoroquinolones in vitro (MIC ≤ 0.06–0.08 µg/mL), with Ofloxacin demonstrating direct antibacterial activity against both antigen-complete and antigen-deficient strains (PMID 16127904). Because the drug's GyrA inhibition mechanism functions equivalently across susceptible Gram-negative pathogens, the leap from bacterial infections in general to *Y. pestis* specifically is mechanistically sound. Regulatory validation comes from the FDA's approval of levofloxacin — Ofloxacin's pharmacologically active isomer — for plague treatment under the Animal Efficacy Rule, and from CDC/WHO guidelines listing fluoroquinolones as first-line alternatives to streptomycin.

**For Punctate Epithelial Keratoconjunctivitis (PEK):** Ofloxacin 0.3% ophthalmic solution already holds FDA approval for bacterial conjunctivitis and bacterial corneal ulcers, establishing proof-of-concept for ocular antibacterial application. PEK caused by bacterial pathogens sits within that approved mechanism space. However, PEK is most commonly caused by adenoviral infection and drug/chemical toxicity — contexts where antibiotics are ineffective — so clinical use must be restricted to bacterial-etiology cases with microbiological support.

**Why Most Predictions Are Likely False Positives:** The TxGNN knowledge graph assigns high scores to eight indications that lack biological plausibility. Two carry a specific safety concern rather than a neutral null result: Rank #1 (hyperamylasemia) and Rank #7 (peripheral neuropathy) both represent conditions that fluoroquinolones are known to *cause*, not treat. Using Ofloxacin in those settings would risk harm.

---

## Clinical Trial Evidence

No registered clinical trials are available for Ofloxacin in either of the two actionable indications.

| Indication | Status | Reason |
|------------|--------|--------|
| Septicemic Plague | No trials registered | Plague is a rare, geographically limited BSL-3 pathogen; human efficacy trials are ethically and logistically impractical; FDA approved levofloxacin via Animal Efficacy Rule specifically because human trials cannot be conducted |
| Punctate Epithelial Keratoconjunctivitis | No trials registered | Ophthalmic use already established through approved bacterial conjunctivitis indication; no dedicated PEK repurposing trials identified |

---

## Literature Evidence

### Septicemic Plague (Rank #8 — Primary Actionable Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal Study | Antibiotiki i khimioterapiia | **Direct Ofloxacin evidence**: MIC 0.08 mg/L against *Y. pestis*; superior to pefloxacin and nalidixic acid; validated prophylactic and therapeutic efficacy in mouse model using both antigen-complete and antigen-deficient strains |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal Study | Antimicrob Agents Chemother | Ofloxacin active in vitro and in vivo against virulent *Y. pestis* strain 6/69M in mouse systemic infection model; efficacy comparable to reference standard streptomycin |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Regulatory Review | Clin Infect Dis | FDA Animal Efficacy Rule approval pathway for fluoroquinolones in plague; context for why Ofloxacin's isomer (levofloxacin) received approval without human trials |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal Study | Clin Infect Dis | Ciprofloxacin and levofloxacin ≥90% effective for pneumonic plague when administered within 2–6 hours of fever onset in African green monkey primate model |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal Study | PLoS Negl Trop Dis | Levofloxacin (Ofloxacin's active isomer) curative for experimental pneumonic plague in African green monkeys — strongest class-level efficacy evidence |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | Animal Study | Antimicrob Agents Chemother | Levofloxacin comparable to streptomycin for *Y. pestis* in in vitro pharmacodynamic model; lower resistance-selection risk than streptomycin |
| [37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/) | 2023 | Review | Am J Trop Med Hyg | Global plague epidemiology 2010–2019: 4,547 cases, 786 deaths (17%); streptomycin-resistant strains documented, reinforcing need for fluoroquinolone alternatives |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal Study | Antibiotiki i khimioterapiia | Levofloxacin, lomefloxacin, and moxifloxacin all highly active against *Y. pestis* FI+ and FI− strains in mouse model; ED50 5.5–14 mg/kg |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal Study | Antimicrob Agents Chemother | Aerosol mouse model of pneumonic plague: antibiotic comparison showing fluoroquinolones among the most effective drug classes tested |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal Study | Antibiotiki i khimioterapiia | Ofloxacin, ciprofloxacin, pefloxacin all effective for plague prophylaxis in mice; important caveat: these agents may suppress post-vaccination immunity from EV vaccine strain |

### Punctate Epithelial Keratoconjunctivitis (Rank #10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak Investigation | Am J Ophthalmol | Microsporidial keratoconjunctivitis outbreak from swimming pool contamination in Taiwan; Ofloxacin eye drops were included in the multi-drug treatment protocol used for affected cases |
| [16670489](https://pubmed.ncbi.nlm.nih.gov/16670489/) | 2006 | Case Report | Cornea | Vernal shield ulcer non-responsive to medical therapy including topical antibiotics; healed with surgical debridement — indirect evidence that antibiotic-only approaches for certain PEK subtypes are insufficient |

### Monoclonal Gammopathy (Rank #6) — Literature Context Note

> All 20 retrieved papers address **levofloxacin infection prophylaxis** in newly-diagnosed myeloma patients (landmark: TEAMM Phase 3 RCT, PMID 31668592), not treatment of monoclonal gammopathy itself. This evidence supports the antibiotic's utility in managing immunosuppression complications of plasma cell dyscrasias — a supportive-care role, not a repurposing indication. The Hold recommendation for Rank #6 stands.

---

## Philippines Market Information

Ofloxacin currently has **no active registrations** with the Food and Drug Administration of the Philippines and is not marketed in the country.

| Item | Status |
|------|--------|
| FDA Philippines Registrations | 0 |
| Market Status | Not Marketed |
| Approved Dosage Forms on Record | None |

Any repurposing pathway would require establishing Philippines FDA market authorization from the start. For the septicemic plague indication, an emergency use or compassionate access pathway may be more relevant given disease rarity.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level safety alert** (derived from mechanistic analysis within this Evidence Pack): The fluoroquinolone class, including Ofloxacin, carries multiple **FDA Black Box Warnings**: irreversible peripheral neuropathy, increased risk of aortic aneurysm and dissection, tendinitis and tendon rupture (including Achilles), serious CNS effects (seizures, psychiatric reactions), and *Clostridioides difficile*-associated colitis. These warnings directly determine the feasibility of several predicted indications: Rank #7 (hematological disease with peripheral neuropathy) represents a **contraindicated direction** where this drug could worsen the target condition. For any proceeding indication, full Black Box Warning review and pharmacovigilance planning are prerequisite.

---

## Conclusion and Next Steps

### For Septicemic Plague (Rank #8)

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic support is direct and strong — Ofloxacin inhibits DNA gyrase in *Yersinia pestis* with documented preclinical efficacy (PMID 16127904, 8203841), and its pharmacologically active isomer (levofloxacin) is FDA-approved for plague treatment. Fluoroquinolones are recognized in CDC and WHO guidelines as first-line alternatives for all forms of plague, including the septicemic form. The primary limitation is that levofloxacin is clinically preferred over the racemic Ofloxacin, and zero Philippines market authorization currently exists.

**To proceed, the following is needed:**
- Clarify whether to pursue Ofloxacin or position levofloxacin as the preferred fluoroquinolone for plague treatment in the Philippines — clinically, levofloxacin has stronger regulatory standing
- Philippines FDA registration strategy (currently 0 registrations; emergency/compassionate use pathway may be more practical given plague's rarity)
- Full MOA documentation (DrugBank API query recommended; DG002 gap remediation)
- TFDA package insert retrieval for complete Black Box Warning and contraindication review (DG001 gap remediation)
- Safety monitoring plan specifically addressing peripheral neuropathy surveillance during therapy, given the FDA Black Box Warning
- Assessment of BSL-3 handling requirements for any clinical use or trial setting

---

### For Punctate Epithelial Keratoconjunctivitis (Rank #10)

**Decision: Proceed with Guardrails**

**Rationale:**
Ofloxacin 0.3% ophthalmic solution is FDA-approved for bacterial conjunctivitis and corneal ulcers, providing a clear regulatory and mechanistic foundation for bacterial-etiology PEK. Evidence remains at case-series level (L3), and the indication is strictly etiology-dependent — most PEK is adenoviral or drug-toxic in origin.

**To proceed, the following is needed:**
- Philippines FDA registration for the ophthalmic dosage form
- Clinical protocol restricting use to microbiologically confirmed or strongly suspected bacterial PEK
- Patient selection criteria to exclude adenoviral and drug-toxicity PEK subtypes (most common causes)
- Pharmacovigilance plan monitoring for ocular fluoroquinolone resistance emergence

---

### For All Remaining Predictions (Ranks #1–5, #7, #9; and Rank #6 for disease-modifying use)

**Decision: Hold**

No sufficient mechanistic basis or evidence support warrants further development. Ranks #1 and #7 carry **active safety concerns** (drug-induced pancreatitis and peripheral neuropathy respectively) that make repurposing in those directions potentially harmful.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

