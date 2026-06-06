---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Theophylline: From Bronchial Asthma / COPD to Thrombotic Disease

## One-Sentence Summary

Theophylline is a methylxanthine bronchodilator with over 80 years of clinical history in asthma and chronic obstructive pulmonary disease (COPD), though it currently holds no Philippines FDA registration.
The TxGNN model predicts it may have activity in **Thrombotic Disease**, theoretically through cAMP-mediated suppression of platelet aggregation via phosphodiesterase inhibition.
This prediction is supported by **0 clinical trials** and **19 publications** — the majority of which cite theophylline incidentally as a laboratory reagent to prevent ex vivo platelet activation, rather than as a direct antithrombotic therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration; globally established for bronchial asthma and COPD |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacology, theophylline is a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist. By inhibiting PDE3 and PDE4, it raises intracellular cAMP across multiple cell types — including platelets. Elevated platelet cAMP suppresses activation and aggregation, a mechanism directly analogous to the approved antiplatelet agent dipyridamole. In laboratory settings, this effect is so reliable that theophylline is routinely included in CTAD blood collection tubes specifically to prevent ex vivo platelet activation — a widely documented practice visible in several of the cited publications (PMID 749930, PMID 29220362, PMID 32824700).

The conceptual link between thrombotic disease and theophylline's original respiratory indication is indirect but not implausible. Both conditions share underlying adenosine receptor and cAMP signaling biology: adenosine receptor antagonism affects bronchoconstriction in the airways and platelet reactivity in the vasculature through parallel cAMP-dependent pathways. The TxGNN knowledge graph likely captured these shared pathway co-occurrences as an indirect association signal.

However, this prediction should be read as a mechanistic hypothesis rather than a clinical finding. No study has directly tested theophylline as a therapeutic antithrombotic agent in humans or in standard in vivo thrombosis models. The TxGNN high score most likely reflects the density of indirect graph connections — platelet cAMP biology, adenosine pathway nodes, vascular disease co-mentions — rather than an evidence base for clinical repurposing. Without dedicated preclinical and clinical validation, this indication cannot advance beyond the hypothesis stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for theophylline in thrombotic disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Thromboxane A₂ and prostacyclin antagonize each other in platelet aggregation; cAMP-elevating agents (mechanistic class of theophylline) can inhibit platelet clumping — provides background for theophylline's theoretical antiplatelet action |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Pharmacology | General Pharmacology | Milrinone (a selective PDE3 inhibitor, same enzymatic class as theophylline) reduces platelet aggregation and raises intraplatelet cAMP in human PRP and whole blood — class-level evidence for PDE inhibition as an antiplatelet strategy |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Basic Science | Journal of Nutrition | Agents raising cAMP via adenylyl cyclase or PDE inhibition decrease GPIIb/IIIa receptor activation and prevent platelet shape change — confirms cAMP pathway relevance to platelet inhibition |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methodology | British Journal of Haematology | PF4 radioimmunoassay requires theophylline + PGE1 + EDTA in collection tubes to block ex vivo platelet activation — direct documentation of theophylline's in vitro antiplatelet potency |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Methodology | PLoS ONE | CTAD anticoagulant (containing theophylline) shown to be essential for accurate measurement of platelet-stored molecules; theophylline's role is to suppress platelet degranulation during sample handling |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Methodology | Cells | Inappropriate anticoagulation without theophylline causes platelet activation and contaminates circulating microRNA signatures — reinforces theophylline's established in vitro antiplatelet mechanism |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Observational | Rheumatology (Oxford) | Platelet and neutrophil hyperactivation in Behçet's disease (a thrombotic vasculitis); disease severity and age effects documented — background context only, no theophylline treatment data |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Clinical Study | Inflammatory Bowel Diseases | Platelet-leukocyte aggregate formation elevated in IBD, associated with both inflammatory and thrombotic risk — establishes platelet activation as a relevant pathological endpoint |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Clinical Observation | Cor et Vasa | T-helper cell elevation in patients with myocardial infarction and thrombophlebitis; theophylline-resistant cell phenotyping used as a laboratory classification tool — theophylline appears as a reagent, not a treatment |
| [8318681](https://pubmed.ncbi.nlm.nih.gov/8318681/) | 1993 | Case Report | JASN | Post-transplant erythrocytosis managed with theophylline — demonstrates theophylline's vascular and hemostatic activity in a transplant context, though not specific to thrombotic disease |

---

## Philippines Market Information

Theophylline currently has **no Philippines FDA registrations**. There are no licensed products to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note:** No Philippines FDA safety data, DDI records, or formal contraindication list was available in this evidence pack. Theophylline is well-known globally to have a **narrow therapeutic index** (target serum level 10–20 µg/mL; toxicity above 20 µg/mL). Key concerns include seizures, cardiac arrhythmias, and nausea at supratherapeutic concentrations, as well as extensive drug interactions mediated by CYP1A2 (e.g., with fluoroquinolones, macrolides, cimetidine). Therapeutic drug monitoring is required. Any clinical use in the Philippines would require formal safety documentation prior to proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.62%) for theophylline in thrombotic disease, but the supporting evidence base is critically weak: zero clinical trials have tested this indication, and no publication has studied theophylline as a therapeutic antithrombotic agent. The 19 retrieved publications primarily reflect theophylline's use as a laboratory antiplatelet reagent or provide indirect mechanistic background — not clinical validation. This prediction cannot advance beyond a hypothesis without dedicated in vivo and clinical studies.

**To proceed, the following is needed:**
- Preclinical in vivo thrombosis studies (e.g., FeCl₃ arterial injury or laser-induced vessel injury models) to quantify theophylline's antithrombotic potency and compare it to established agents (aspirin, dipyridamole, clopidogrel)
- Mechanistic clarification of whether clinically achievable theophylline concentrations (10–20 µg/mL) produce meaningful platelet cAMP elevation in vivo
- Philippines FDA safety documentation (package insert, DDI profile) before any clinical evaluation can begin
- Consideration of prioritizing Philippines registration for theophylline's **established** indication first

> **Strategic note:** Among all 7 predicted indications in this evidence pack, **Obstructive Lung Disease** (TxGNN rank #5, score 99.48%) carries the strongest evidence — **L1 level** with multiple completed Phase 2/3 RCTs — and a "Proceed with Guardrails" recommendation. This reflects theophylline's globally established clinical role as a bronchodilator and anti-inflammatory agent in COPD and asthma. For the Philippines market, pursuing regulatory registration for this well-evidenced indication is likely the more actionable and lower-risk near-term pathway compared to pursuing the novel thrombotic disease hypothesis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

