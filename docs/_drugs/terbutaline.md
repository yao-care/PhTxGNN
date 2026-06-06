---
layout: default
title: Terbutaline
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
---

# Terbutaline
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

# Terbutaline: From Acute Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Terbutaline is a selective β2-adrenergic agonist bronchodilator widely used internationally for acute relief of bronchospasm in asthma and airway obstruction, though it currently holds no Philippines market registration.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** (encompassing COPD and asthma), with **48 clinical trials** and **20 publications** currently identified — including multiple large Phase 3 RCTs where Terbutaline serves directly as an active treatment arm or standard-of-care rescue bronchodilator.
This prediction is best understood as a high-confidence **validation** of an established pharmacological use rather than a discovery of novel utility, with the primary gap being formal Philippines market registration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm / acute asthma relief (no Philippines registration; inferred from established international use) |
| Predicted New Indication | Obstructive Lung Disease (COPD and asthma) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Terbutaline (commercially known as Bricanyl®) is a selective β2-adrenergic receptor agonist. It binds to β2-receptors on bronchial smooth muscle cells, activating the adenylyl cyclase–cAMP–PKA signaling cascade, which phosphorylates myosin light-chain kinase and leads to smooth muscle relaxation and airway dilation. This mechanism directly counteracts the bronchospasm that defines obstructive lung diseases. The mechanistic chain is complete and causally direct — this is the drug's original pharmacological design target. Detailed MOA data from DrugBank was not captured in this evidence pack, but the mechanistic basis is fully corroborated by the clinical trial evidence described below.

Obstructive lung disease encompasses both COPD and asthma, which share the hallmark of increased airway resistance due to smooth muscle contraction, mucus hypersecretion, and airway inflammation. Terbutaline's selective β2-agonism addresses the reversible bronchospasm component in both conditions. Importantly, Terbutaline appears as the reference standard for short-acting β2-agonist (SABA) rescue therapy in landmark Phase 3 trials including the SHARE study (n=1,970) and the Symbicort NOVEL studies (n=4,215 and n=3,850), confirming its established role in obstructive lung disease management globally.

The near-perfect TxGNN prediction score (99.96%) reflects this tight mechanistic alignment. Rather than revealing a surprising new application, this prediction validates Terbutaline's core pharmacological identity and reinforces the opportunity for formal Philippines market entry in the obstructive lung disease indication — a therapeutic area where the drug has robust Level 1 clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4,215 | Terbutaline Turbuhaler used as the 'as-needed' rescue inhaler control arm vs. Symbicort 'as-needed' in mild asthma; large-scale, rigorous comparison directly establishing Terbutaline's efficacy benchmark |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3,850 | Three-arm study: Symbicort 'as-needed' vs. Terbutaline 'as-needed' vs. Pulmicort + Terbutaline in mild-to-moderate asthma; Terbutaline serves as active standard-of-care comparator |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Completed | 2,100 | AHEAD study: Symbicort flexible dosing vs. Seretide + Terbutaline as-needed over 6 months in persistent asthma; 6-month multinational evaluation with Terbutaline as rescue SABA |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2,091 | Symbicort SMART vs. Symbicort + Terbutaline 0.4 mg as-needed over 12 months; Terbutaline arm represents conventional SABA-supplemented maintenance therapy |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Completed | 1,970 | SHARE study: real-world health economics and asthma control over 12 months; Terbutaline included as rescue SABA in conventional ICS + SABA comparator arm |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | Completed | 1,600 | Symbicort SMART vs. conventional best practice (per German guidelines) over 26 weeks in persistent asthma; large multinational real-practice validation |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | AIFA-sponsored Italian study: as-needed budesonide/formoterol vs. regular ICS/LABA + Terbutaline as-needed in mild-to-moderate persistent asthma |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Completed | 250 | β2-agonists alone (nebulized) vs. β2-agonists + ipratropium bromide in acute COPD exacerbation in emergency department; establishes role of β2-agonists as COPD exacerbation mainstay |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | Direct head-to-head comparison: IV magnesium sulfate vs. **Terbutaline** in children with acute asthma exacerbations; provides direct evidence for Terbutaline as active treatment |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Pharmacodynamic study comparing two formulations of Bricanyl® Turbuhaler® (M3 vs. M2) against methacholine-induced bronchoconstriction in stable asthma; directly evaluates Terbutaline bronchodilator efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Academic Emergency Medicine | Randomized double-blind trial: nebulized Terbutaline + ipratropium vs. Terbutaline alone in AECOPD requiring NIV; evaluates whether adding anticholinergic to Terbutaline improves hypercapnic COPD outcomes |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | RCT | Annals of Palliative Medicine | N-acetylcysteine combined with Terbutaline sulfate in elderly COPD patients; demonstrates clinical benefit on lung function and apoptosis/anti-apoptosis mechanisms |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | British Journal of Diseases of the Chest | Double-blind randomized crossover trial: oral Terbutaline 2.5 mg TID for 1 week in normocapnic moderate-to-severe COPD; Terbutaline increased peak inspiratory mouth pressure and transdiaphragmatic pressure vs. placebo |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Double-blind 2-week RCT: clenbuterol vs. Terbutaline sulfate 5 mg TID in chronic obstructive lung disease; compared FEV1, specific airway resistance, and MEF50% as bronchodilator endpoints |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Clinical Study | Cellular & Molecular Immunology | Atomization inhalation of Terbutaline + budesonide in AECOPD; showed improvement in immunity markers and lung function parameters including airway hyperreactivity |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | Clinical Study | Chest | Double-blind crossover study of β-blockers (metoprolol, propranolol) combined with Terbutaline in 35 COPD patients with ischemic heart disease or hypertension; characterizes drug interaction profile |
| [3044105](https://pubmed.ncbi.nlm.nih.gov/3044105/) | 1988 | Clinical Study | American Journal of the Medical Sciences | Double-blind randomized crossover trial of oral Terbutaline in 10 COPD patients; demonstrated augmentation of right and left ventricular ejection fractions, supporting cardiopulmonary benefit |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Clinical Study | Respiratory Medicine | Double-blind placebo-controlled crossover study of Terbutaline via Turbuhaler in COLD patients; evaluated FEV1, FVC, walking distance, and dyspnoea during exercise |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | Clinical Study | Lung | Double-blind placebo-controlled randomized crossover study: single-dose Terbutaline (Bricanyl Turbuhaler) in 26 patients with FEV1 40–70% predicted COLD; measured resting lung function and exercise capacity |
| [20004090](https://pubmed.ncbi.nlm.nih.gov/20004090/) | 2010 | Pharmacokinetic Study | Respiratory Medicine | Compared emitted dose and lung deposition of inhaled Terbutaline from Turbuhaler in healthy subjects vs. COPD patients; characterized bioavailability differences relevant to dosing optimization in obstructive disease |

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug-drug interactions) were not retrieved in this evidence pack. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Terbutaline has robust Level 1 evidence for obstructive lung disease, with multiple completed large-scale Phase 3 RCTs (combined enrollment exceeding 15,000 patients) where Terbutaline is used as an active treatment or standard-of-care rescue bronchodilator. The TxGNN prediction validates an established pharmacological mechanism rather than proposing a novel indication. The primary barrier is the absence of Philippines market registration, not scientific uncertainty.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Submit Philippines FDA registration application (this drug is internationally established; priority review may be applicable for unmet need)
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB00871) for submission dossier — Terbutaline's β2-agonist mechanism is well-characterized but needs formal sourcing
- **Safety dossier**: Obtain and parse the full prescribing information / package insert (international SmPC for Bricanyl®) covering warnings, contraindications, and key drug interactions (particularly with β-blockers, MAOIs, and cardiac medications)
- **Local dosage form decision**: Confirm which formulations (inhaler, nebulizer solution, injection, oral tablet) are most relevant for the Philippines market and align with available manufacturing partnerships
- **Pharmacovigilance plan**: Establish local adverse event monitoring consistent with Philippines FDA post-marketing requirements prior to launch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

