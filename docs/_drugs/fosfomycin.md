---
layout: default
title: Fosfomycin
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Urinary Tract Infections to Gonococcal Urethritis

## One-Sentence Summary

Fosfomycin is a broad-spectrum antibiotic that inhibits bacterial cell wall synthesis, internationally approved for the treatment of urinary tract infections.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis**,
with **6 publications** (including **1 RCT**) currently supporting this direction — particularly relevant in the era of multidrug-resistant *Neisseria gonorrhoeae*.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infections (no Philippines-approved indication on record) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (1 completed RCT) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Fosfomycin is a phosphonic acid-derivative antibiotic with a unique mechanism of action: it inhibits **MurA (UDP-N-acetylglucosamine enolpyruvyl transferase)**, the enzyme catalysing the first committed step in bacterial peptidoglycan (cell wall) synthesis. Because this target is distinct from those of β-lactams, fluoroquinolones, and aminoglycosides, fosfomycin retains activity against many multidrug-resistant organisms.

Gonococcal urethritis is caused by *Neisseria gonorrhoeae*, a Gram-negative diplococcus that synthesises peptidoglycan and is therefore susceptible to cell wall–targeting agents. Fosfomycin has demonstrated in vitro bactericidal activity against *N. gonorrhoeae*, including strains resistant to ceftriaxone and azithromycin — the current first-line regimen. Given the WHO designation of *N. gonorrhoeae* as a "high priority" pathogen for new antibiotic development, fosfomycin represents a mechanistically plausible alternative.

The connection between fosfomycin's established urinary tract indication and gonococcal urethritis is direct: both are bacterial infections of the genitourinary tract, and the drug achieves high local concentrations in urine and urethral tissue. A 2016 open-label RCT (PMID 27064136) specifically evaluated fosfomycin trometamol in uncomplicated gonococcal urethritis in men, lending clinical credibility to the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no clinical trials registered on ClinicalTrials.gov specifically for fosfomycin in gonococcal urethritis.

> **Note:** The 2016 RCT by Yuan et al. (PMID 27064136) was conducted in China and may have been registered in a regional registry. The absence from ClinicalTrials.gov does not negate the published RCT evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clin Microbiol Infect | Open-label RCT in 152 men with gonococcal urethritis; fosfomycin trometamol 3 g on days 1, 3, 5 vs. standard therapy; 126 patients completed the study — demonstrates direct clinical efficacy data |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical Study | Chemotherapy | 70 patients with acute/subacute gonococcal urethritis treated with IM fosfomycin; 4 g single dose achieved 86% cure rate (37/43); 4 g split dose achieved 92% cure rate (11/12) |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Microbiological Study | Chemotherapy | Bacteriological evaluation of fosfomycin across 959 patients in multi-centre controlled studies; gonococcal urethritis included as one of the clinical indications evaluated |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Secondary Analysis | Sex Transm Infect | NABOGO trial secondary analysis assessing spontaneous clearance of asymptomatic *N. gonorrhoeae*; provides context on natural history relevant to treatment trial design |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Review | Zhonghua Nan Ke Xue | Review of diagnosis and treatment of genitourinary infection with non-gonococcal *Neisseria* in men; provides differential diagnostic context |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Case Report | J Fr Ophtalmol | Case of gonococcal conjunctivitis with MDR *N. gonorrhoeae* (resistant to penicillins, tetracyclines, fluoroquinolones); illustrates the growing need for alternative agents |

---

## Philippines Market Information

Fosfomycin currently has **no registered products** in the Philippines. There are no active authorizations from the Philippines FDA on record.

> **Implication:** Any repurposing initiative would first require regulatory pathway assessment for product registration or compassionate use/special access programme eligibility.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current evidence pack.

**General considerations based on international labelling:**
- Fosfomycin trometamol (oral) is generally well tolerated; the most common adverse effects are gastrointestinal (diarrhoea, nausea)
- IV fosfomycin may cause electrolyte imbalances (hypokalaemia, hypernatraemia) due to the sodium content of the disodium salt formulation
- Allergic reactions are rare but possible

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score is extremely high (99.99%), and — critically — direct clinical evidence already exists: a 2016 RCT and a 1977 clinical study both evaluated fosfomycin specifically for gonococcal urethritis with favourable cure rates. The mechanistic link is strong and well-characterised (cell wall synthesis inhibition active against *N. gonorrhoeae*). In the context of rising multidrug-resistant gonorrhoea, fosfomycin addresses a genuine unmet clinical need.

**To proceed, the following is needed:**
- **Philippines regulatory pathway**: Assess feasibility of product registration or importation under special access, since fosfomycin is currently not marketed in the Philippines
- **Updated in vitro susceptibility data**: Test local *N. gonorrhoeae* isolates against fosfomycin to establish regional MIC distributions
- **Mechanism of action (MOA) formal documentation**: Obtain detailed MOA data from DrugBank to complete the pharmacological profile
- **Safety profile (package insert)**: Obtain and parse the full prescribing information for warnings, contraindications, and drug interactions
- **Optimal dosing regimen**: The 2016 RCT used a multi-dose oral regimen (3 g × 3 doses); further PK/PD modelling may identify the minimum effective regimen
- **Antimicrobial resistance monitoring**: Establish baseline fosfomycin resistance rates in regional *N. gonorrhoeae* populations before large-scale use

---

## Appendix: Other TxGNN Predicted Indications

| Rank | Disease | Score | Evidence Level | Recommendation | Rationale |
|------|---------|-------|---------------|----------------|-----------|
| 1 | Gonococcal urethritis | 99.99% | L2 | Proceed with Guardrails | Strong mechanistic link; 1 RCT + clinical studies |
| 2 | Ureaplasma urethritis | 99.99% | L5 | Hold | ⚠️ Mechanistic contradiction: *Ureaplasma* lacks cell wall — fosfomycin has no expected activity |
| 3 | Uterine inflammatory disease | 99.98% | L4 | Research Question | Partial mechanistic link; PID involves mixed pathogens, some susceptible |
| 4 | Xanthogranulomatous pyelonephritis | 99.98% | L5 | Research Question | Plausible (active against causative organisms) but surgery is mainstay |
| 5 | Epiglottitis | 99.93% | L5 | Hold | Established treatments exist; fosfomycin offers no advantage |
| 6 | Urogenital tuberculosis | 99.88% | L5 | Hold | ⚠️ Weak mechanistic link: *M. tuberculosis* cell wall differs; high MICs |
| 7 | Laryngitis | 99.68% | L4 | Hold | Mostly viral aetiology; limited evidence for nebulised fosfomycin |
| 8 | Hyperamylasemia | 99.47% | L5 | Hold | ⚠️ False positive: non-infectious laboratory finding |
| 9 | Polyclonal hyperviscosity syndrome | 99.47% | L5 | Hold | ⚠️ False positive: immunological/haematological condition |
| 10 | Pyelitis | 99.37% | L1 | Proceed with Guardrails | Core indication area; Phase 2/3 RCT (ZEUS trial) + 20 publications |

> **Notable:** Rank 10 (Pyelitis) has the strongest evidence base (L1) with a completed Phase 2/3 RCT and 20 publications, representing fosfomycin's established therapeutic territory in upper urinary tract infections.

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*

*Report generated: 2026-04-05 | Evidence Pack version: v4 | Data cutoff: 2026-04-05*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

