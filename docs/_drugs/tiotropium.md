---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 337
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Tiotropium: predicted new indication Obstructive lung disease (evidence level L1). Approved use: Bronchitis, asthma, intrinsic asthma, allergic asthma…"
monitor_inn: "Tiotropium"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome", "COPD, severe early onset", "tracheal stenosis", "susceptibility to respiratory infections associated with CD8alpha chain mutation"]
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tiotropium: From Bronchitis, Asthma and Emphysema to Obstructive Lung Disease

## One-Sentence Summary

Tiotropium is a long-acting inhaled muscarinic antagonist, originally used for bronchitis, asthma and pulmonary emphysema.
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **39 clinical trials** and **20 publications** compiled for this prediction. Note that this prediction overlaps heavily with the drug's existing uses, so it is closer to an on-label category than a true repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, asthma, intrinsic asthma, allergic asthma, pulmonary emphysema (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the drug database. Based on general pharmacology, tiotropium is a long-acting muscarinic antagonist (LAMA). It blocks M3 receptors on airway smooth muscle, which produces sustained bronchodilation and reduces cholinergic tone and mucus secretion. It dissociates slowly from M1 and M3 receptors, which allows once-daily dosing.

Obstructive lung disease is the broad category that includes the drug's original indications (bronchitis, asthma, emphysema). The prediction is therefore mechanistically consistent, but it largely restates established use rather than identifying a new one. The same applies to the related predictions for COPD (rank 5) and severe early-onset COPD (rank 4).

Other predictions in the list are much weaker. Respiratory malformation, tracheal stenosis, hyperlucent lung, compensatory emphysema and interstitial emphysema involve structural or non-obstructive processes. Rienhoff syndrome and the CD8alpha-related infection susceptibility are rare conditions with no identified rationale. None of these has supporting evidence, and all are rated Hold.

---

## Clinical Trial Evidence

The table lists the most relevant trials, with Phase 3 and graded studies given priority.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00240435](https://clinicaltrials.gov/study/NCT00240435) | Phase 3 | Completed | 491 | Tiotropium Respimat 5 and 10 mcg vs placebo and ipratropium MDI in COPD; bronchodilator efficacy and safety |
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Phase 3 | Completed | 2,624 | 52-week tiotropium + olodaterol vs individual components in COPD (TOnado 1) |
| [NCT00877383](https://clinicaltrials.gov/study/NCT00877383) | Phase 3 | Completed | 1,142 | Indacaterol added to tiotropium vs tiotropium alone, 12 weeks, moderate-to-severe COPD |
| [NCT00900731](https://clinicaltrials.gov/study/NCT00900731) | Phase 3 | Completed | 1,598 | Indacaterol vs tiotropium over 12 weeks in moderate-to-severe COPD |
| [NCT01854645](https://clinicaltrials.gov/study/NCT01854645) | Phase 3 | Completed | 2,103 | Triple/dual MDI therapies vs placebo, with open-label tiotropium as active control, 24 weeks |
| [NCT01610037](https://clinicaltrials.gov/study/NCT01610037) | Phase 3 | Completed | 1,215 | 52-week long-term safety of QVA149 vs placebo and tiotropium |
| [NCT01525615](https://clinicaltrials.gov/study/NCT01525615) | Phase 3 | Completed | 404 | Tiotropium + olodaterol vs placebo on exercise endurance over 12 weeks |
| [NCT01316380](https://clinicaltrials.gov/study/NCT01316380) | Phase 3 | Completed | 465 | Tiotropium Respimat vs placebo in mild persistent asthma over 12 weeks |
| [NCT00772538](https://clinicaltrials.gov/study/NCT00772538) | Phase 3 | Completed | 459 | Tiotropium 5 mcg add-on to usual care in severe persistent asthma over 48 weeks |
| [NCT02172443](https://clinicaltrials.gov/study/NCT02172443) | Phase 3 | Completed | 50 | Tiotropium capsules vs ipratropium MDI in COPD (small, active-comparator design) |

The data set contains further trials, including Phase 2 dose-ranging, device comparison and pharmacokinetic studies. The 52-week combination study (NCT01431274) and the placebo- and active-controlled study (NCT00240435) were graded as direct efficacy evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Tested long-term tiotropium on lung function and its decline in mild-to-moderate COPD |
| [29779416](https://pubmed.ncbi.nlm.nih.gov/29779416/) | 2018 | RCT | Am J Respir Crit Care Med | SUNSET: de-escalation from triple therapy to indacaterol/glycopyrronium in COPD |
| [27724909](https://pubmed.ncbi.nlm.nih.gov/27724909/) | 2016 | Systematic Review | BMC Pulm Med | Compared tiotropium Respimat and HandiHaler in COPD |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Reviewed tiotropium + olodaterol for reducing COPD exacerbations |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Tiotropium as an anticholinergic bronchodilator with once-daily dosing and improved lung function in COPD |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | Review of the clinical development of tiotropium in COPD |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Efficacy and safety of ipratropium combined with tiotropium |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Mechanistic review | Life Sci | Mechanistic considerations and clinical profile of tiotropium in obstructive lung disease |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J Chron Obstruct Pulmon Dis | Real-world comparison of three LABA/LAMA combinations in Taiwan |
| [23728670](https://pubmed.ncbi.nlm.nih.gov/23728670/) | 2013 | Cochrane review | Cochrane Database Syst Rev | Inhaled steroid/LABA combination vs tiotropium in COPD |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0489 | Tiotropium | Not recorded | Not recorded (status: cancelled) |

The only registration is cancelled, so no valid registration currently exists in the Philippines.

---

## Safety Considerations

- **Contraindications / conditions of concern (from the knowledge graph, not label text)**: benign prostatic hyperplasia, impaired renal function, angle-closure (closed-angle) glaucoma, bladder neck obstruction.
- **Drug Interactions**: 100 interactions were found in the DDI screening. The main ones are additive anticholinergic effects with other antimuscarinic agents, rated Moderate: hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline and scopolamine. Other Moderate interactions include eluxadoline, prucalopride and inhaled rapid-acting insulin. Cimetidine is rated Minor.
- **Other signals from the literature**: ocular effects (an anterior chamber study, NCT06525051) and cardiovascular and mortality questions (PMID 32274526, PMID 21672999) are covered in the compiled publications.

Please refer to the package insert for the official warnings and contraindications, because label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and meta-analyses support tiotropium in obstructive lung disease and COPD, giving L1 evidence. However, this is established on-label use rather than true repurposing, and the only Philippines registration is cancelled. Predictions for the other eight conditions lack supporting evidence and should stay on Hold.

**To proceed, the following is needed:**
- Confirm the current regulatory and market availability of tiotropium in the Philippines, including which formulations (HandiHaler or Respimat) are available.
- Obtain the Philippine package insert to complete the warnings and contraindications review.
- Complete the mechanism of action data from DrugBank.
- Put anticholinergic safety monitoring in place (glaucoma, urinary retention, prostatic hyperplasia, renal impairment, cardiovascular events).
- Treat the COPD and obstructive lung disease predictions as confirmation of existing use rather than as new-indication findings.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

