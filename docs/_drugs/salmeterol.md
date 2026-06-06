---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 7
---

# Salmeterol
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

# Salmeterol: From Asthma/COPD to Bronchitis

## One-Sentence Summary

Salmeterol is a globally established long-acting β2-adrenoceptor agonist (LABA), approved in the US, EU, Japan and many other markets for the maintenance treatment of asthma and COPD, but currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Bronchitis**, with **16 clinical trials** and **20 publications** currently supporting this direction.
The evidence base is particularly strong: multiple completed Phase 3 trials directly evaluate salmeterol in airway obstruction overlapping with chronic bronchitis, and salmeterol/fluticasone already holds regulatory approval for COPD associated with chronic bronchitis in the US and EU.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / COPD (globally approved; not registered in the Philippines) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Salmeterol acts as a selective, long-acting β2-adrenoceptor agonist on bronchial smooth muscle, producing sustained bronchodilation lasting more than 12 hours via elevation of intracellular cAMP. Beyond bronchodilation, salmeterol promotes **mucociliary clearance** — the airway's primary defence mechanism for removing excess mucus and trapped pathogens — and inhibits mast cell degranulation, thereby reducing the release of bronchoconstrictor mediators. PMID 15970448 provides the most direct evidence: in a controlled study of 14 patients with mild-to-moderate chronic bronchitis, salmeterol significantly improved both mucociliary clearance and cough clearance compared to placebo over a 2-hour observation period.

Chronic bronchitis and COPD share overlapping pathology: persistent airway inflammation, mucus hypersecretion, impaired mucociliary function, and progressive airflow obstruction. This mechanistic bridge is already reflected in regulatory precedent — the US FDA approves salmeterol/fluticasone propionate 250/50 mcg (Advair Diskus) specifically for COPD **associated with chronic bronchitis**, and the EU approval of Seretide 500 mcg covers severe COPD with a chronic bronchitis component. The TxGNN prediction therefore reflects a well-established clinical pathway, not a speculative extrapolation.

Note: Detailed mechanism of action data from DrugBank was not retrieved in this evidence pack (flagged as a High-severity data gap). The mechanistic description above is based on the established pharmacology of salmeterol as a LABA and the mechanistic rationale documented in the evidence review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | Completed | 584 | 6-month double-blind, three-arm comparison: Tiotropium vs. Salmeterol vs. Placebo in COPD. Core head-to-head trial directly evaluating salmeterol bronchodilator efficacy and safety in airway obstruction including chronic bronchitis. |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | Completed | 130 | 13-week double-blind study comparing salmeterol/fluticasone 50/500 mcg vs. placebo in COPD; primary endpoint was **bronchial anti-inflammatory activity** — directly measures airway inflammation highly relevant to chronic bronchitis. |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | Completed | 150 | 18-week COPD comparison study assessing lung function and daily symptom diary outcomes; salmeterol-containing arm is a core treatment group. |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | Completed | 639 | Randomized double-blind 29-week study comparing fluticasone/salmeterol 250/50 vs. salmeterol 50 mcg alone on COPD exacerbation rates following hospitalization for acute exacerbation. |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | Completed | 247 | 12-week double-blind comparison of fluticasone/salmeterol HFA MDI vs. DISKUS in COPD; the approved US indication for this product specifically covers **COPD associated with chronic bronchitis**. |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | Completed | 457 | Dose-finding trial of fluticasone/formoterol vs. fluticasone/salmeterol in COPD; salmeterol serves as the reference comparator, providing dose-response context for chronic bronchitis management. |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | 12-week double-blind multi-center COPD study with salmeterol as an active treatment arm; assesses bronchodilator effect and safety in patients with chronic obstructive airway disease. |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | Unknown | 20 | Single-center UCLA comparison of nebulized arformoterol vs. salmeterol dry-powder inhaler in COPD; evaluates inspiratory capacity and HRCT changes in small airways. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22,155 | Large European drug utilization study characterizing real-world use patterns among COPD/chronic bronchitis patients starting bronchodilator therapy; provides population-level background. |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month open-label randomized COPD safety study comparing arformoterol vs. salmeterol; cross-LABA long-term safety comparison relevant to chronic bronchitis maintenance therapy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | Experimental | Pulm Pharmacol Ther | **Most direct evidence**: Salmeterol vs. placebo in 14 chronic bronchitis patients; salmeterol significantly improved whole-lung mucociliary clearance and cough clearance over a 2-hour period using radiolabeled aerosol imaging. |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | Fluticasone/salmeterol Diskus vs. placebo and individual agents in COPD; fluticasone/salmeterol combination improved FEV1, health status, and morning peak flow with acceptable safety profile. |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | RCT | Clin Ther | Open-label comparison of inhaled salmeterol 50 mcg BID vs. oral theophylline in mild-to-moderate stable COPD; salmeterol improved symptoms and quality of life with superior tolerability. |
| [31852314](https://pubmed.ncbi.nlm.nih.gov/31852314/) | 2020 | RCT | J Int Med Res | Systematic review and meta-analysis comparing fluticasone/formoterol vs. fluticasone/salmeterol in pediatric asthma over 12 weeks; provides efficacy comparison across the LABA class. |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Database Study | Curr Med Res Opin | Retrospective database analysis of fluticasone/salmeterol vs. other inhaled therapies initiated in **chronic bronchitis** patients; salmeterol combination significantly reduced hospitalization and emergency department visits. |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Cohort | Ther Adv Respir Dis | 12-month safety assessment of arformoterol vs. salmeterol in COPD; no evidence of tolerance development or increased exacerbation frequency with salmeterol over extended use. |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Review | Drugs Today | COPD management review focusing on the chronic bronchitis phenotype; contextualizes bronchodilator and anti-inflammatory combination strategies including salmeterol. |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish national COPD clinical guideline; LABAs including salmeterol are recommended first-line maintenance bronchodilators across disease severity stages. |
| [20649375](https://pubmed.ncbi.nlm.nih.gov/20649375/) | 2010 | Review | Expert Rev Respir Med | Review of roflumilast for COPD with chronic bronchitis phenotype; contextualizes combination bronchodilator and anti-inflammatory strategies; salmeterol referenced as standard background therapy. |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Meta-analysis | Respir Res | Meta-analysis of salmeterol 50 mcg BID vs. placebo/usual therapy across multiple COPD studies; pooled estimates demonstrate significant improvements in FEV1, symptom scores, exacerbation rates, and health status. |

---

## Philippines Market Information

Salmeterol is currently **not registered** in the Philippines. FDA Philippines has issued no market authorization for any salmeterol-containing product (0 licenses on record). This represents a market access gap rather than a safety or efficacy concern, given the drug's extensive global regulatory history.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Important note for prescribers**: Although full safety data was not retrieved in this evidence pack, a well-known FDA Black Box Warning exists for LABA class agents: long-acting beta2-agonists such as salmeterol **increase the risk of asthma-related death when used as monotherapy in asthma**. Current international guidelines (GINA, FDA) mandate that LABAs be used only in combination with inhaled corticosteroids (ICS) for asthma management. This restriction would need to be reflected in any Philippines registration dossier and prescribing information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 clinical trials directly support salmeterol's efficacy in airway obstruction and chronic bronchitis (L1 evidence level), and the drug already holds regulatory approval for COPD associated with chronic bronchitis in the US and EU — making the Philippines market gap a registration and access issue rather than an efficacy uncertainty.

**To proceed, the following is needed:**

- **Blocking — Safety data**: Obtain and review the full prescribing information (package insert) to document key warnings, contraindications, and drug interactions. Currently a Blocking data gap preventing S1 safety evaluation.
- **High priority — MOA confirmation**: Retrieve full DrugBank mechanistic data to complete the mechanistic rationale section and strengthen the regulatory submission dossier.
- **Regulatory pathway**: Conduct a Philippines FDA registration assessment for a new drug application (NDA) or Certificate of Product Registration (CPR) — determine whether mutual recognition of existing US/EU approvals is applicable.
- **Formulation and supply chain**: Confirm availability of dry-powder inhaler (Diskus/Accuhaler) or HFA MDI device supply in the Philippine market, including device training materials in local language.
- **ICS co-registration requirement**: Given the LABA monotherapy Black Box Warning, evaluate whether a combination product (salmeterol/fluticasone) rather than salmeterol monotherapy would be the more appropriate registration strategy for the Philippines.
- **Pharmacovigilance plan**: Develop a local pharmacovigilance protocol, particularly monitoring for cardiovascular adverse events (tachycardia, QTc prolongation) and asthma-related serious adverse events as required for LABA class products.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

