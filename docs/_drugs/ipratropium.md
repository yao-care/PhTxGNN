---
layout: default
title: Ipratropium
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Ipratropium
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

Skill noted — not applicable to report generation. Proceeding directly per the Report Prompt v5 instructions.

---

# Ipratropium: From COPD & Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Ipratropium (Atrovent®) is a well-established anticholinergic bronchodilator used globally for decades to treat bronchospasm in COPD and asthma, but is currently **not registered in the Philippines**.
The TxGNN model predicts it to be highly effective for **Obstructive Lung Disease** with a score of 99.97%, backed by **multiple completed Phase 3 RCTs** — including one conducted specifically in Filipino COPD patients — and **20 supporting publications**.
This is not a novel repurposing in the traditional sense, but a strong evidence-based case for introducing a proven drug to an underserved market.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD / Bronchospasm (established globally; no Philippines registration on file) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ipratropium competitively antagonizes muscarinic M3 receptors on bronchial smooth muscle, blocking vagally-mediated bronchoconstriction and producing sustained bronchodilation. It also inhibits M1/M3 receptors on submucosal glands, reducing pathological airway hypersecretion. This dual mechanism directly addresses the core pathophysiology of obstructive lung disease: excessive parasympathetic airway tone, dynamic airflow limitation, and mucus plugging — all hallmarks of COPD and related conditions.

Obstructive lung disease encompasses conditions — most prominently COPD — where persistent airflow limitation arises from both bronchospasm and structural airway remodeling. Because the cholinergic pathway is the dominant bronchomotor tone in human airways, M3 receptor antagonism provides a mechanistically targeted and predictable therapeutic effect. This is why ipratropium remains a cornerstone in global COPD guidelines (GOLD) and has been used clinically since the 1980s.

The TxGNN prediction is therefore a high-confidence confirmation from the knowledge graph rather than a speculative leap. Particularly notable is that one of the pivotal Phase 3 trials (NCT02172469) was conducted specifically in **Filipino patients with COPD**, providing direct population-level evidence for this exact clinical context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000568](https://clinicaltrials.gov/study/NCT00000568) | Phase 3 | Completed | N/A | Landmark Lung Health Study I & III: directly evaluated ipratropium's effect on FEV1 decline rate and cardiopulmonary morbidity/mortality in early COPD — highest-level direct evidence for this indication |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | Completed | 215 | Tiotropium vs Atrovent® MDI **specifically in Filipino COPD patients** — directly establishes ipratropium efficacy and safety benchmark in the Philippine population |
| [NCT02233881](https://clinicaltrials.gov/study/NCT02233881) | N/A | Completed | 4,222 | Large post-marketing surveillance of Atrovent® inhalets (n=4,222): real-world tolerability and efficacy in COPD daily practice |
| [NCT00846586](https://clinicaltrials.gov/study/NCT00846586) | Phase 3 | Completed | 1,134 | Double-blind RCT: indacaterol + tiotropium vs tiotropium alone in moderate-to-severe COPD; high-quality direct evidence for anticholinergic class |
| [NCT00400153](https://clinicaltrials.gov/study/NCT00400153) | Phase 3 | Completed | 1,480 | Combivent Respimat (ipratropium/salbutamol) vs COMBIVENT® MDI: demonstrated non-inferiority on FEV1 AUC over 12 weeks in COPD |
| [NCT01019694](https://clinicaltrials.gov/study/NCT01019694) | Phase 3 | Completed | 470 | Long-term safety and patient acceptability of Combivent Respimat vs Atrovent HFA in COPD; confirmed favorable long-term safety profile |
| [NCT02182713](https://clinicaltrials.gov/study/NCT02182713) | Phase 4 | Completed | 30 | Combivent (ipratropium + salbutamol) vs salbutamol alone against methacholine-induced bronchoconstriction: ipratropium combination confers additional protection |
| [NCT02182700](https://clinicaltrials.gov/study/NCT02182700) | Phase 3 | Terminated | 47 | Combivent aerosol + spacer in moderate-to-severe asthma crisis in ER; early termination limits interpretation, but directly involves ipratropium |
| [NCT02236715](https://clinicaltrials.gov/study/NCT02236715) | N/A | Completed | 1,039 | Post-marketing surveillance of Atrovent® Unit Dose Vial 500 µg in chronic obstructive airways disease: confirmed real-world tolerability |
| [NCT00274040](https://clinicaltrials.gov/study/NCT00274040) | Phase 3 | Completed | 141 | Tiotropium vs ipratropium MDI in COPD: ipratropium (Atrovent) used as active comparator, providing direct bronchodilator efficacy data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane Meta-analysis | Cochrane Database Syst Rev | Tiotropium vs ipratropium in stable COPD: tiotropium superior on FEV1, QoL, and exacerbations — confirms ipratropium as established active comparator with proven efficacy |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Cochrane Meta-analysis | Cochrane Database Syst Rev | Earlier Cochrane head-to-head comparison; ipratropium established as effective COPD treatment baseline |
| [16856113](https://pubmed.ncbi.nlm.nih.gov/16856113/) | 2006 | Cochrane Meta-analysis | Cochrane Database Syst Rev | Ipratropium vs LABAs for stable COPD: ipratropium effective bronchodilator with comparable symptom relief and favorable safety profile |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Systematic Review | Expert Opin Drug Metab Toxicol | Reviews mechanism, clinical efficacy, and safety of albuterol, ipratropium, and combination therapy in COPD; combination approved >15 years prior to publication |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | RCT | Medicine | Probiotics + budesonide + ipratropium in COPD (n=118): combination improves lung function and gut microbiota vs budesonide + ipratropium alone — recent real-world evidence |
| [8181328](https://pubmed.ncbi.nlm.nih.gov/8181328/) | 1994 | RCT | Chest | 85-day multicenter trial (COMBIVENT Study Group): ipratropium + albuterol combination more effective than either agent alone in COPD |
| [7813271](https://pubmed.ncbi.nlm.nih.gov/7813271/) | 1995 | RCT | Chest | Pirbuterol vs ipratropium in COPD: differential effects on gas exchange and ventilation distribution — ipratropium uniquely preserves V/Q matching |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Clinical Study | Ann Pharmacother | Evidence review of concomitant ipratropium + tiotropium in COPD: additive bronchodilation with acceptable safety |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clinical Pharmacy | Comprehensive review of ipratropium pharmacology, kinetics, and clinical efficacy in obstructive lung disease; foundational reference |
| [6448137](https://pubmed.ncbi.nlm.nih.gov/6448137/) | 1980 | Pharmacological Review | Drugs | Seminal characterization of ipratropium bromide: anticholinergic bronchodilator at least as effective as beta-2 agonists in chronic bronchitis |

---

## Philippines Market Information

Ipratropium currently has **no active drug authorizations in the Philippines** (0 registered products). The drug is widely approved in other major markets under brand names including Atrovent® (inhaler and unit-dose nebules) and Combivent® (combination with salbutamol).

This absence represents a clear regulatory gap given the high COPD burden in the Philippines and the availability of L1-level evidence including a dedicated Filipino patient cohort study.

---

## Safety Considerations

Full Philippines FDA package insert data (key warnings, contraindications) was not available in the current evidence pack.

> Please refer to the originator package insert for complete safety information. Based on the drug's well-characterized pharmacological class (quaternary ammonium anticholinergic), clinicians should be aware of anticholinergic class effects including risk of acute angle-closure glaucoma (particularly with nebulized formulation and eye exposure), urinary retention in patients with benign prostatic hyperplasia, and paradoxical bronchospasm. No drug interaction data was retrieved from the DDI database for this submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ipratropium meets L1 evidence criteria with multiple completed Phase 3 RCTs for obstructive lung disease — including a trial conducted in Filipino COPD patients — and a 99.97% TxGNN prediction score, making it one of the strongest repurposing candidates in this pipeline. The primary barrier to deployment is the absence of Philippines regulatory registration, not a lack of efficacy evidence.

**To proceed, the following is needed:**
- Submit Philippines FDA (FDA-PH) registration dossier, leveraging existing FDA USA / EMA approvals via abridged or mutual recognition pathway
- Obtain and translate full originator package insert (key warnings, contraindications, drug interactions) for Philippines labeling compliance
- Confirm supply chain and cold-chain logistics for inhaler formulations in the local distribution network
- Conduct pharmacoeconomic analysis for formulary inclusion (PhilHealth Essential Medicines List, DOH formulary)
- Establish post-marketing pharmacovigilance plan specific to the Philippine patient population
- Review NCT02172469 full dataset to extract Filipino-specific subgroup safety and efficacy data for the registration submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

