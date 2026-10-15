---
layout: default
title: Montelukast
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 5
---

# Montelukast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Montelukast: From Allergic Rhinitis and Asthma to Bronchitis

## One-Sentence Summary

Montelukast is a leukotriene receptor antagonist originally used for allergic rhinitis, vasomotor rhinitis, and asthma (intrinsic and allergic).
The TxGNN model predicts it may be effective for **bronchitis**, but the supporting studies mostly address related conditions (bronchiolitis, post-bronchiolitis wheeze, bronchiolitis obliterans syndrome), with **17 clinical trials** and **20 publications** compiled, only a few of which directly concern bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, intrinsic asthma, allergic asthma (from the knowledge-graph indication list; the Philippines registration has no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 (as assigned in the compiled data; see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

*Note on the evidence level:* The compiled data assigns L2 to this prediction, but the studies are mostly in related diseases, small, or non-randomized. The direct bronchitis evidence is limited to one Phase 4 trial of recurrent obstructive bronchitis in children (status unknown) and one trial in nonasthmatic eosinophilic bronchitis. I therefore treat the practical strength as modest and recommend Hold.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, montelukast blocks the cysteinyl leukotriene receptor 1 (CysLT1). This reduces airway inflammation, bronchoconstriction, mucus secretion, and eosinophil-driven airway hyperreactivity, which is the basis of its use in asthma and allergic rhinitis.

Bronchitis shares airway inflammation and cough or wheeze features with asthma. Leukotriene signalling is also implicated in viral bronchiolitis and in bronchiolitis obliterans syndrome after transplantation, supported by a rat transplant model (PMID 28545478). Eosinophilic forms of bronchitis may be especially relevant.

The link is indirect and population-specific, however. Most listed trials address bronchiolitis, not bronchitis in the strict sense. The prediction is best read as a research question, not an established new use.

---

## Clinical Trial Evidence

Trials most relevant to bronchitis and closely related bronchiolitis conditions (10 of 17 shown):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Montelukast for prevention and treatment of recurrent obstructive bronchitis in children aged 1-7 years; randomized into 2 groups. |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomized, double-blind, placebo-controlled add-on montelukast to inhaled budesonide in nonasthmatic eosinophilic bronchitis; primary endpoint is cough severity. |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1125 | Randomized, double-blind, placebo-controlled comparison of 2 doses of montelukast in RSV-induced bronchiolitis in children 3-24 months. |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | NA | Completed | 141 | Randomized, double-blind, placebo-controlled; daily montelukast and duration of illness in infants with first-time bronchiolitis. |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | NA | Completed | 146 | Montelukast in acute bronchiolitis and post-bronchiolitis wheezing in infants 3-12 months. |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | NA | Completed | 51 | Double-blind, placebo-controlled trial in acute RSV bronchiolitis, with clinical progress and cytokine profiles. |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Montelukast for bronchiolitis obliterans after stem cell transplantation; small, likely single-arm. |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Fluticasone + azithromycin + montelukast combination for bronchiolitis obliterans after transplant; montelukast's contribution cannot be isolated. |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Randomized, double-blind, placebo-controlled montelukast for bronchiolitis obliterans syndrome after lung transplantation. |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Cough counts after montelukast or prednisolone in chronic cough with raised exhaled NO. |

Several other listed trials are small Phase 2 safety/PK studies in infants (e.g., NCT00394160, NCT00394069) or studies where montelukast is background therapy (e.g., NCT05922761, NCT01432080), and give little direct evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25773054](https://pubmed.ncbi.nlm.nih.gov/25773054/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Reviews leukotriene inhibitors such as montelukast in infants and young children with bronchiolitis. |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Systematic review | Pediatr Allergy Immunol | Montelukast for preventing wheezing after RSV bronchiolitis. |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | Clinical study | Chin Med J | Add-on montelukast to budesonide in nonasthmatic eosinophilic bronchitis; assessed airway inflammation, cough, and quality of life. |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Ther Adv Respir Dis | Therapeutic potential and possible mechanisms of montelukast in bronchiolitis obliterans syndrome after lung or stem-cell transplantation. |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Guideline | Eur Respir J | ERS/EBMT guidelines on treating pulmonary chronic GVHD in adults. |
| [29704475](https://pubmed.ncbi.nlm.nih.gov/29704475/) | 2018 | Expert panel report | Chest | CHEST panel on chronic cough after acute viral bronchiolitis in children. |
| [28662986](https://pubmed.ncbi.nlm.nih.gov/28662986/) | 2017 | Systematic review | J Heart Lung Transplant | Therapy options for chronic lung allograft dysfunction/BOS. |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal study | J Cardiothorac Surg | LTB4 and montelukast in transplantation-related bronchiolitis obliterans in rats. |
| [40702225](https://pubmed.ncbi.nlm.nih.gov/40702225/) | 2025 | Mechanistic | Lung | Mast cells and cough hypersensitivity in eosinophilic bronchitis. |
| [40926299](https://pubmed.ncbi.nlm.nih.gov/40926299/) | 2025 | Consensus statement | Br J Haematol | Taiwan consensus on pulmonary chronic GVHD. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0330 | Montelukast | Not specified | Not specified (registration status: cancelled) |

The only registration on record is cancelled, so no valid Philippines marketing authorization currently exists in the data compiled for this report.

---

## Safety Considerations

- **Neuropsychiatric events**: The US FDA added a boxed warning on neuropsychiatric adverse events in 2020. Systematic review and cohort data (PMIDs 37758273, 36948487, 39836401, 40491164) support particular attention in children.
- **Eosinophilic granulomatosis with polyangiitis (EGPA)**: Rare induction has been reported (PMID 39959324).
- **Contraindication-related conditions (knowledge graph, not label text)**: anxiety disorder, neurotic disorder, dysthymic disorder, anxiety, hypereosinophilic syndrome, and cutaneous vasculitis.
- **Drug interactions** (100 recorded; examples at Moderate level): dexamethasone, metronidazole, miconazole, nateglinide, nitisinone, troglitazone. Other listed pairs (e.g., pantoprazole, omeprazole, metformin, morphine) have an unknown severity level.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Most supporting studies concern bronchiolitis or transplant-related bronchiolitis obliterans, not bronchitis, and many are small or of uncertain design. The directly relevant bronchitis trials (recurrent obstructive bronchitis in children, nonasthmatic eosinophilic bronchitis) are small and have limited reported results. The Philippines registration is cancelled, and no label-based safety data are available.

**To proceed, the following is needed:**
- Results and outcome data from the bronchitis-specific trials (NCT04613180, NCT01121016), ideally confirmed in a larger randomized trial
- A defined target population (e.g., eosinophilic bronchitis or pediatric recurrent obstructive bronchitis)
- Detailed mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of registration status, since the only registration is cancelled
- A neuropsychiatric safety monitoring plan, especially for children

---

**Other predicted indications (brief note):** Atopic eczema has Phase 4 trials (including a double-blind placebo-controlled study, n=20) and a Cochrane review, but the clinical benefit appears modest and inconsistent. Asthma and obstructive lung disease largely validate the existing indication rather than representing new repurposing. "Asthma-related traits, susceptibility to" is a genetic trait phenotype, not a treatable indication, and has no supporting trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

