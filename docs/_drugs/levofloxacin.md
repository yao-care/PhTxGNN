---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic with well-established bactericidal activity against gram-positive and gram-negative organisms, used globally for respiratory, urinary, and ophthalmic bacterial infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **1 publication** currently supporting this direction.
Notably, a higher-ranked evidence opportunity — **Monoclonal Gammopathy infection prophylaxis** — is supported by a Phase 3 RCT (TEAMM, Lancet Oncology 2019) and is addressed in the Conclusion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (fluoroquinolone antibiotic) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Levofloxacin is a third-generation fluoroquinolone that achieves bactericidal activity by concurrently inhibiting two bacterial type II topoisomerases — DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE). This dual-target mechanism prevents DNA replication and transcription in susceptible bacteria, and its 0.5% ophthalmic formulation has regulatory approval in multiple countries for treating bacterial conjunctivitis and corneal ulcers caused by a broad panel of ocular pathogens.

Punctate epithelial keratoconjunctivitis (PEK) is a diffuse corneal surface disorder characterized by superficial epithelial defects. The condition is most frequently caused by viral agents (adenovirus, herpes simplex), toxic reactions, or immune-mediated mechanisms — all of which fall outside the spectrum of activity of fluoroquinolones. Bacterial etiology accounts for a minority of PEK cases, and even in those, the role of an antibiotic would be adjunctive rather than disease-modifying.

The sole supporting literature (PMID 30055152) describes an epidemiological investigation of a microsporidial keratoconjunctivitis outbreak linked to swimming pool contamination in Taiwan, in which Levofloxacin was used as part of a multi-drug regimen targeting bacterial superinfection — not the primary microsporidial pathogen. The mechanistic link between Levofloxacin and PEK is therefore indirect and weak. This TxGNN prediction most likely reflects the drug's general ophthalmic antibacterial profile rather than a specific therapeutic opportunity in PEK.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Epidemiological Case Series | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis from swimming pool contamination in Taiwan; Levofloxacin used as adjunctive bacterial co-infection treatment, not primary therapy for microsporidial infection |

---

## Philippines Market Information

Levofloxacin is currently **not registered** with the Philippine Food and Drug Administration (FDA Philippines). No active product authorizations or license records are on file in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinically Important Signals Noted in This Evidence Pack:**
> - **Black Box Warning (FDA):** Serious and potentially irreversible peripheral neuropathy — onset can occur within hours to days of initiation. Levofloxacin is **contraindicated** in the context of pre-existing neuropathy (see Rank #8 prediction flag in Evidence Pack).
> - **Rare Adverse Event:** Acute pancreatitis has been documented with Levofloxacin use, making the Rank #3 prediction (Hyperamylasemia as a therapeutic target) a likely false-positive and pharmacovigilance concern rather than a repurposing opportunity.

---

## Conclusion and Next Steps

**Decision: Hold** (for Punctate Epithelial Keratoconjunctivitis)

**Rationale:**
The top-ranked TxGNN prediction (PEK, Score 99.92%) is not supported by adequate clinical evidence — the only available publication describes Levofloxacin as an adjunctive agent in a bacterial superinfection scenario unrelated to PEK pathogenesis. With an evidence level of L4 and no registered clinical trials, clinical development for this indication is premature.

---

### ⚠️ Higher-Priority Repurposing Opportunities in This Evidence Pack

The TxGNN score ranking does not reflect clinical evidence strength. Two lower-ranked predictions carry substantially more actionable evidence:

| TxGNN Rank | Indication | Evidence Level | Key Evidence | Recommendation |
|-----------|-----------|---------------|-------------|----------------|
| #7 | Monoclonal Gammopathy (Multiple Myeloma — infection prophylaxis) | **L1** | TEAMM Phase 3 RCT (Lancet Oncology, 2019, n=977); Retrospective cohort studies; Comparative RCT vs ciprofloxacin | **Proceed with Guardrails** |
| #9 | Septicemic Plague | **L2** | FDA Animal Rule approval (2012); NHP model studies; In vitro MIC data (MIC₉₀ ≤ 0.03 µg/mL) | **Proceed with Guardrails** |
| #1 | Punctate Epithelial Keratoconjunctivitis | L4 | 1 case series (adjunctive role only) | Hold |

---

### Monoclonal Gammopathy — Priority Assessment

The TEAMM trial (PMID 31668592, Lancet Oncology 2019) is a multicentre, double-blind, placebo-controlled Phase 3 RCT demonstrating that **Levofloxacin prophylaxis significantly reduces febrile episodes and infection-related hospitalizations** in newly diagnosed myeloma patients during induction chemotherapy. Multiple myeloma patients suffer immunoparesis (suppressed normal immunoglobulin production) and chemotherapy-induced neutropenia, creating profound susceptibility to gram-positive organisms (S. pneumoniae, H. influenzae) and gram-negative bacteria (E. coli). Levofloxacin's dual inhibition of DNA gyrase and topoisomerase IV provides broad bactericidal coverage with high oral bioavailability — a critical advantage for outpatient prophylaxis.

**To advance the Monoclonal Gammopathy indication in the Philippines, the following is needed:**
- Confirm Philippines FDA registration pathway for Levofloxacin oral formulation (currently unregistered)
- Review local antimicrobial resistance patterns for fluoroquinolone-resistant gram-negative organisms, which may limit prophylaxis efficacy
- Assess applicability of TEAMM trial data to Philippine patient populations (Asian populations underrepresented in original trial)
- Evaluate pharmacoeconomic case: cost of prophylaxis vs. cost of infection-related hospitalizations in Philippine oncology setting
- Review antibiotic stewardship implications with Philippine infectious disease guidelines

**To advance the Septicemic Plague indication:**
- Levofloxacin is FDA-approved under the Animal Efficacy Rule for plague — regulatory precedent exists
- Assess WHO essential medicine list applicability for Philippines biodefense formulary
- No Philippine-specific regulatory barrier anticipated given FDA (US) approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

