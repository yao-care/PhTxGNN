---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

# Tiotropium: From COPD to Obstructive Lung Disease

## One-Sentence Summary

Tiotropium (Spiriva®) is a long-acting muscarinic antagonist (LAMA) globally approved for chronic obstructive pulmonary disease (COPD) and asthma, though it currently carries no registered approval in the Philippines.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** — a broader category encompassing COPD, asthma, and related airway obstruction conditions — with **over 30 clinical trials** and **20 publications** currently supporting this direction.
The prediction score of 99.99% is entirely consistent with tiotropium's established global clinical evidence base, making this one of the highest-confidence signals in the dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in the Philippines (globally: COPD and asthma) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tiotropium is a selective long-acting muscarinic antagonist that blocks M1 and M3 muscarinic acetylcholine receptors on airway smooth muscle and glands. The key pharmacological feature is its markedly slow dissociation from M3 receptors compared to M2 receptors — a kinetic subtype selectivity that produces sustained bronchodilation lasting over 24 hours with once-daily dosing, while minimising M2-mediated tachycardia. By blocking M3 receptors, tiotropium relaxes bronchial smooth muscle, reduces mucus hypersecretion, and decreases dynamic hyperinflation during exercise. These properties are well characterised in the literature, with foundational mechanistic work published as early as 1999 (PMID 10069510) and confirmed across decades of Phase 2 and Phase 3 clinical studies.

Obstructive lung disease is the pathophysiological umbrella covering conditions defined by chronic airflow limitation — primarily COPD (chronic bronchitis and emphysema) and asthma, including the asthma–COPD overlap syndrome. Across all these phenotypes, increased cholinergic tone is a key reversible component of airway obstruction, which makes M3 antagonism a mechanistically sound intervention. In COPD specifically, the Global Initiative for Chronic Obstructive Lung Disease (GOLD) guidelines endorse LAMA monotherapy as first-line maintenance treatment for Groups B, C, and D — directly aligning with tiotropium's mechanism. In asthma, tiotropium is FDA- and EMA-approved as add-on therapy for patients ≥6 years old who remain poorly controlled on inhaled corticosteroids.

The TxGNN model's prediction of "obstructive lung disease" as the top-ranked indication is pharmacologically rational and clinically validated. Multiple completed Phase 3 RCTs, two Cochrane systematic reviews, and GOLD guideline endorsement collectively represent the highest available evidence standard. Notably, at least one trial (NCT02172469, n=215) was conducted specifically in **Filipino patients** with COPD, providing directly applicable local evidence. The Philippines has not yet registered tiotropium despite its global approval in more than 100 countries, suggesting a registration gap rather than a clinical uncertainty.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00846586](https://clinicaltrials.gov/study/NCT00846586) | Phase 3 | Completed | 1,134 | 12-week RCT: indacaterol 150 µg once daily + open-label tiotropium 18 µg vs. tiotropium alone in moderate-to-severe COPD; establishes tiotropium as the backbone comparator in obstructive lung disease trials |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | 24-week multicenter double-blind RCT comparing GSK573719/GW642444 (umeclidinium/vilanterol) vs. tiotropium (HandiHaler) in COPD; tiotropium used as active control confirming its standard-of-care position |
| [NCT00793624](https://clinicaltrials.gov/study/NCT00793624) | Phase 3 | Completed | 906 | 48-week double-blind placebo-controlled RCT assessing olodaterol (BI 1744 CL) via Respimat in COPD patients; tiotropium's Respimat formulation evaluated as part of the trial design |
| [NCT01525615](https://clinicaltrials.gov/study/NCT01525615) | Phase 3 | Completed | 404 | TORRACTO: 12-week RCT comparing tiotropium + olodaterol FDC vs. placebo on exercise endurance in COPD; demonstrates functional benefit beyond spirometry |
| [NCT01294787](https://clinicaltrials.gov/study/NCT01294787) | Phase 3 | Completed | 85 | Crossover RCT assessing QVA149 (indacaterol/glycopyrronium) vs. tiotropium on exercise endurance in moderate-to-severe COPD |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | Completed | 215 | **Filipino patient study**: double-blind RCT comparing tiotropium 18 µg vs. ipratropium MDI in adults with COPD — directly applicable to Philippines regulatory context |
| [NCT00949975](https://clinicaltrials.gov/study/NCT00949975) | Phase 2 | Completed | 838 | Phase IIb dose-ranging RCT: AZD9668 (neutrophil elastase inhibitor) added to tiotropium background in symptomatic COPD; large sample size confirms tiotropium's role as stable background therapy |
| [NCT04780984](https://clinicaltrials.gov/study/NCT04780984) | Phase 2 | Completed | 116 | Randomised dose-ranging study of tiotropium bromide inhalation solution pharmacodynamics, bioavailability, and safety in COPD subjects |
| [NCT02175342](https://clinicaltrials.gov/study/NCT02175342) | Phase 2 | Completed | 202 | PK/PD dose-ranging study of tiotropium via Respimat device; established optimal once-daily dosing for the Respimat formulation |
| [NCT02567214](https://clinicaltrials.gov/study/NCT02567214) | Phase 4 | Completed | 50 | Head-to-head: indacaterol/glycopyrronium (Ultibro®) vs. tiotropium (Spiriva®) alone on exertional dyspnea in moderate-to-severe COPD; confirms tiotropium's clinical positioning |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Tiotropium improved lung function and reduced FEV1 decline in **mild-to-moderate (early-stage) COPD**; broadens indication evidence beyond severe disease |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Systematic Review | Respir Res | Comprehensive review of tiotropium's 20-year clinical development in COPD; confirms LAMA as first-line maintenance therapy across GOLD groups |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review/Meta-analysis | Curr Med Res Opin | Tiotropium + olodaterol FDC as initial and escalation COPD treatment reduces exacerbation risk per GOLD 2020 |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Cochrane Review | Cochrane Database Syst Rev | Tiotropium vs. placebo in stable COPD: significant improvements in lung function, exacerbation rates, and health-related quality of life |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane Review | Cochrane Database Syst Rev | Tiotropium vs. ipratropium in stable COPD: tiotropium demonstrated superior lung function and fewer exacerbations |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Pharmacology Review | Life Sciences | Foundational MOA paper: tiotropium's kinetic M3-receptor subtype selectivity provides the mechanistic rationale for once-daily bronchodilation in obstructive lung disease |
| [29670674](https://pubmed.ncbi.nlm.nih.gov/29670674/) | 2018 | Clinical Review | Can Respir J | Tiotropium for **asthma**: evidence for LAMA add-on therapy across obstructive lung disease phenotypes; patient selection for the asthma indication |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Drug Monograph | Drugs | Tiotropium 18 µg once daily vs. placebo: significant improvements in FEV1, dyspnea, exacerbations, and quality of life in COPD — early pivotal evidence |
| [11281822](https://pubmed.ncbi.nlm.nih.gov/11281822/) | 2001 | Drug Review | Expert Opin Investig Drugs | Phase II evidence: prolonged bronchodilation via slow M1/M3 receptor dissociation in human airways; established the pharmacological basis for development |
| [22562275](https://pubmed.ncbi.nlm.nih.gov/22562275/) | 2012 | RCT/Comparative | Pneumonol Alergol Pol | Comparative RCT of formoterol, formoterol + tiotropium, formoterol + ICS, and tiotropium monotherapy on lung function and exercise tolerance in COPD |

---

## Philippines Market Information

Tiotropium currently has **no registered drug products in the Philippines**. The FDA Philippines shows zero active licenses and a market status of "not marketed" as of the data cutoff (June 2026).

For context, tiotropium is globally marketed under the following brands:
- **Spiriva® HandiHaler®** (18 µg tiotropium bromide inhalation powder capsule)
- **Spiriva® Respimat®** (2.5 µg and 5 µg tiotropium bromide inhalation solution)

It is approved by the US FDA, EMA, PMDA (Japan), TFDA (Taiwan), and regulatory agencies in more than 100 countries. The Philippines registration gap represents an unmet need rather than an unresolved clinical question.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings, contraindications, and drug interaction data were not available in this evidence pack. Anticholinergic class effects relevant to clinical use — including dry mouth, urinary retention, constipation, paradoxical bronchospasm, and risk of acute angle-closure glaucoma — should be reviewed from the manufacturer's prescribing information for Spiriva® prior to any clinical or regulatory decision-making. Cardiovascular safety (particularly in patients with arrhythmias) has been specifically studied; a meta-analysis (PMID 32274526) found no significant increase in adverse cardiovascular events with tiotropium use in COPD patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tiotropium has the highest available level of clinical evidence (L1) for obstructive lung disease, supported by multiple completed Phase 3 RCTs, two Cochrane reviews, and inclusion in international treatment guidelines as first-line therapy. The 99.99% TxGNN score reflects a mechanistically direct and globally validated drug-disease match. Critically, one trial was already conducted in Filipino COPD patients (NCT02172469, n=215), providing locally applicable evidence that reduces the regulatory uncertainty typically associated with new drug applications.

**To proceed, the following is needed:**
- Submit a standard new drug application (NDA) to FDA Philippines with the existing global regulatory dossier (safety, efficacy, CMC data from US FDA or EMA approval packages)
- Obtain manufacturer authorisation from Boehringer Ingelheim for Philippines distribution rights
- Compile the Philippines-specific prescribing information including complete safety warnings, contraindications, and drug interaction data from the package insert
- Develop a local pharmacovigilance and adverse event monitoring plan as required by FDA Philippines
- Conduct a health technology assessment for COPD/asthma burden in the Philippines to support formulary listing and pricing negotiations
- Address mechanism of action documentation gap (DG002) by retrieving full DrugBank entry for tiotropium to complete the evidence dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

