---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Autosomal Dominant Polycystic Kidney Disease to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Tolvaptan is a selective vasopressin V2 receptor (V2R) antagonist and currently the only FDA-approved disease-modifying therapy for autosomal dominant polycystic kidney disease (ADPKD) caused by PKD1/PKD2 mutations.
The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (PKD3) with or without Polycystic Liver Disease** — a rarer ADPKD subtype driven by GANAB or DNAJB11 mutations that shares the same cAMP-dependent cystogenesis mechanism.
This prediction is supported by **2 completed Phase 3 RCTs** and **20 publications**, including international consensus statements and clinical practice guidelines that directly endorse tolvaptan across the broader ADPKD spectrum.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Autosomal Dominant Polycystic Kidney Disease (ADPKD; PKD1/PKD2) |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tolvaptan works by selectively blocking the vasopressin V2 receptor (V2R) in renal collecting duct cells, thereby suppressing the arginine vasopressin (AVP)–cyclic AMP (cAMP) signaling cascade. Elevated intracellular cAMP is the central driver of cyst epithelial fluid secretion and abnormal cell proliferation in ADPKD. By blocking this pathway, tolvaptan directly slows cyst growth and preserves kidney function — an effect confirmed in the landmark TEMPO 3:4 trial (NEJM 2012) and replicated in later-stage patients in the REPRISE trial (NEJM 2017).

PKD3 refers to ADPKD variants caused by mutations in GANAB or DNAJB11 — genes encoding proteins involved in the post-translational processing of polycystin-1 and polycystin-2. Although the upstream genetic defect differs from classic PKD1/PKD2 ADPKD, the downstream pathological consequence is identical: unregulated cAMP-driven cystogenesis in renal tubular epithelium. This mechanistic equivalence means that the V2R antagonist strategy is pharmacologically applicable to PKD3 patients. International expert bodies — including the ERA Working Group on Inherited Kidney Disorders, ERKNet, and PKD International (consensus 2022) — have issued guidance covering the broader ADPKD genetic spectrum without restricting tolvaptan's use to PKD1/PKD2 genotypes.

PKD3 patients also frequently develop polycystic liver disease (PCLD), which involves cAMP-dependent biliary epithelial cyst expansion sharing similar cellular biology. The EASL Clinical Practice Guidelines (2022) specifically address management of ADPKD-associated PCLD, further supporting the clinical relevance of this repurposing prediction. The primary evidence gap is that no published trial has enrolled or analyzed PKD3 patients as a genotype-stratified subgroup — but the biologic rationale and indirect evidence base are strong.

---

## Clinical Trial Evidence

Currently no clinical trials specifically targeting polycystic kidney disease 3 with or without polycystic liver disease are registered.

> **Context note:** Tolvaptan has been studied in two large completed Phase 3 RCTs for the broader ADPKD population (TEMPO 3:4 and REPRISE). PKD3 patients carrying GANAB/DNAJB11 mutations are likely included in these cohorts without genotype-specific stratification, as routine ADPKD genotyping was not standard practice during those trial periods. No dedicated PKD3 trial has been registered to date.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | Phase 3 RCT (TEMPO 3:4) | N Engl J Med | Tolvaptan vs. placebo over 3 years: significantly slower total kidney volume growth and slower eGFR decline in ADPKD patients; vasopressin V2-receptor antagonism established as a disease-modifying mechanism |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | Phase 3 RCT (REPRISE) | N Engl J Med | Tolvaptan in later-stage ADPKD (eGFR 25–65 ml/min/1.73m²): confirmed meaningful slowing of eGFR decline; also characterized hepatotoxicity signal requiring monitoring |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrol Dial Transplant | ERA/ERKNet/PKDi consensus on tolvaptan use in ADPKD: patient selection criteria, risk stratification, hepatic monitoring, and long-term treatment management |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of all interventions for preventing ADPKD progression; evaluates tolvaptan's benefit-risk balance across the full evidence base |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review & Meta-analysis | Nefrologia | Meta-analysis confirming tolvaptan's efficacy (kidney volume, eGFR) and safety profile; provides pooled estimates across ADPKD trials |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic kidney/liver disease overview: explicitly states tolvaptan can slow renal function deterioration and cyst growth in ADPKD with concurrent PCLD |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Practice Guideline (EASL) | J Hepatol | EASL guidelines on cystic liver disease management, including ADPKD-associated polycystic liver disease; covers diagnosis, follow-up, and treatment thresholds |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive ADPKD review covering genetic heterogeneity (PKD1/PKD2/minor loci including GANAB/DNAJB11), epidemiology, and current treatment landscape with tolvaptan |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of polycystic kidney and liver diseases: describes PKD3-associated genes (GANAB, DNAJB11) and their phenotypic overlap with classical ADPKD |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Review of emerging ADPKD therapies beyond tolvaptan; confirms tolvaptan remains the only FDA-approved disease-modifying agent and frames the unmet need in broader PKD subtypes |

---

## Philippines Market Information

Tolvaptan is not currently registered in the Philippines. No product licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important**: Detailed Philippines FDA warnings, contraindications, and drug interaction data were not available in the Evidence Pack (Data Gaps DG001/DG002). Based on published trial data and international prescribing information, the following safety signals are known and should be reviewed before any clinical application:
> - **Hepatotoxicity**: Serious and potentially fatal liver injury has been reported; a Risk Evaluation and Mitigation Strategy (REMS) is required in the US. Liver function monitoring is mandatory.
> - **Aquaretic effects**: Polyuria, polydipsia, nocturia, and thirst are common dose-dependent effects from the mechanism of action.
> - **Hypernatremia**: Risk of rapid correction of hyponatremia and dehydration.
> - **Polycystic liver disease subpopulation**: Special caution is warranted as hepatotoxicity and pre-existing hepatic cysts may complicate monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
PKD3 shares the same AVP-cAMP-driven cystogenesis mechanism as classical ADPKD, and tolvaptan's efficacy targeting this pathway is backed by two completed Phase 3 RCTs and multiple international guidelines — meeting L1 evidence criteria. The key constraint is the absence of genotype-stratified efficacy and safety data specifically for the PKD3 subgroup, and the drug is not yet registered in the Philippines.

**To proceed, the following is needed:**

- **Genotype confirmation pathway**: Investigate whether existing TEMPO 3:4 or REPRISE biobank samples can be genotyped to identify PKD3 (GANAB/DNAJB11) subgroup outcomes
- **Regulatory access**: Assess compassionate use, special access scheme, or parallel import pathway with the Philippines FDA (Food and Drug Administration) given zero local registrations
- **Safety documentation (DG001)**: Obtain and parse the full prescribing information/package insert from Otsuka Pharmaceutical to document Philippine-relevant contraindications and hepatotoxicity monitoring protocol
- **MOA data gap (DG002)**: Retrieve complete DrugBank entry (DB06212) to confirm V2R pharmacology and known drug-drug interactions
- **Hepatic monitoring protocol**: Develop a structured liver function monitoring plan specifically for the polycystic liver disease subpopulation, given the compounding risk of hepatotoxicity on a background of hepatic cysts
- **Pediatric risk window**: If any PKD3 patients are children or adolescents, evaluate safety data from the pediatric tolvaptan trial (PMID 38091246) before inclusion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

