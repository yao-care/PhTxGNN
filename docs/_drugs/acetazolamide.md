---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma / Altitude Sickness to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor (CAI) with well-established global uses including glaucoma, altitude sickness prevention, epilepsy management, and periodic paralysis — though no Philippines market registration currently exists.
The TxGNN model's highest-evidenced prediction identifies **Cardiomyopathy** (specifically decompensated heart failure-related congestion) as a repurposing candidate, with **3 ongoing Phase 4 clinical trials** and **10 publications** currently supporting this direction.
Evidence quality reaches Level L2, and the overall recommendation is **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; globally established for glaucoma, acute mountain sickness, epilepsy (adjunct), and periodic paralysis |
| Predicted New Indication | Cardiomyopathy (decompensated / congestion-dominant) |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Acetazolamide inhibits the enzyme carbonic anhydrase (particularly the CA-II isoform in the renal proximal tubule). This blockade prevents bicarbonate reabsorption, increasing urinary excretion of sodium bicarbonate and free water — producing a diuretic effect that is mechanistically distinct from, and synergistic with, standard loop diuretics such as furosemide.

In cardiomyopathy and heart failure, acute decompensation is driven primarily by fluid overload (congestion). The mechanistic chain is well-defined: CA-II inhibition → blocked NaHCO₃ reabsorption → increased urinary sodium excretion → potentiation of loop diuretic response → reduced cardiac preload and tissue fluid retention → improvement of the congestive state. This pathway has been clinically validated in the landmark **ADVOR trial** (Phase 3 RCT), which demonstrated that adding acetazolamide to loop diuretics significantly improved decongestion in acute heart failure. Chloride's emerging role in heart failure pathophysiology further supports acetazolamide as a therapeutic adjunct targeting metabolic alkalosis and chloride depletion — common complications of loop diuretic therapy.

Multiple ongoing Phase 4 trials are directly evaluating acetazolamide in acute/decompensated heart failure populations. The oral bioavailability and the drug's decades-long safety record in other indications make it a practical candidate for structured repurposing investigation in cardiomyopathy management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for decompensated chronic heart failure (including cardiomyopathy); primary objective directly tests acetazolamide in CHF decompensation — the highest-relevance trial in this set |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Double-blind RCT comparing loop diuretic + acetazolamide vs. loop diuretic + metolazone vs. loop diuretic alone in acute heart failure with volume overload; largest enrollment in this group |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | NA | Recruiting | 466 | Urine sodium-guided tailored diuretic algorithm in acute decompensated heart failure; includes acetazolamide as an escalation option, evaluating real-world diuretic optimization strategy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Narrative Review | ESC Heart Failure | 2024 update on heart failure management; reviews 2023 ESC guideline updates, new agents (SGLT2i, finerenone), and evolving diuretic strategies in HF |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Narrative Review | Eur Heart J Cardiovasc Pharmacother | Comprehensive review of 2022 cardiovascular pharmacotherapy advances, including novel agents for obstructive hypertrophic cardiomyopathy (mavacamten) and HF management |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiol Cases | Acetazolamide used to correct hypochloremia (94 mEq/L) in an advanced HF patient with hypertrophic cardiomyopathy; highlights chloride manipulation as a therapeutic target in HF with urinary electrolyte monitoring |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Med J | Acetazolamide effects on ischemia-reperfusion injury in isolated rabbit hearts (2-week and 8-week-old); preclinical mechanistic data on cardiac CA inhibition |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurol Scand | Echocardiographic findings in hypokalaemic periodic paralysis families; documents cardiac muscle involvement and contextualizes acetazolamide use in patients with comorbid cardiomyopathy |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurol Scand | Heart muscle disease in familial hypokalaemic periodic paralysis; patient on 750–1000 mg/day acetazolamide developed exercise angina — important cardiac safety signal at higher doses |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report (Adverse Event) | Acute Med Surg | Non-cardiogenic pulmonary edema occurring 1 hour after IV acetazolamide in a dilated cardiomyopathy patient; critical safety signal for IV use in cardiac patients |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian J Ophthalmol | Oral acetazolamide for cystoid macular edema in Danon disease (LAMP2 cardiomyopathy + retinopathy); demonstrates use in a cardiomyopathy syndrome context |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | J Med Case Rep | Congenital hydrocephalus with coexisting congenital heart disease (trisomy 9p); describes complex acetazolamide use when cardiac disease complicates CSF management |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Observational | J Nucl Med | SPECT cerebral blood flow imaging in mitochondrial encephalomyopathy using acetazolamide vasodilatory challenge; illustrates systemic hemodynamic effects of CA inhibition relevant to cardiac patients |

---

## Philippines Market Information

Acetazolamide is currently **not registered** in the Philippines. No FDA Philippines product authorizations are on record (total licenses = 0). The drug is not available through any domestic regulated marketing channel.

---

## Safety Considerations

> Full safety data (package insert warnings, contraindications) is currently unavailable for this Evidence Pack. Please refer to the original package insert (SmPC / prescribing information) for comprehensive safety information.

**Key safety signal identified from literature:**

- **Adverse cardiac event (IV route)**: One case report (PMID [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/)) documents sudden non-cardiogenic pulmonary edema within 1 hour of intravenous acetazolamide in a dilated cardiomyopathy patient. IV administration in cardiac patients warrants heightened monitoring.
- **High-dose cardiac concern**: A case series (PMID [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/)) reports exercise-induced angina pectoris in a patient receiving 750–1000 mg/day acetazolamide for periodic paralysis; coronary artery disease was subsequently excluded, suggesting possible drug-related cardiac ischemic effects at high doses.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The cardiomyopathy/decompensated heart failure indication is supported by a well-defined and clinically validated mechanism (CA-II inhibition → natriuresis → loop diuretic synergy, confirmed in the ADVOR Phase 3 RCT), three actively recruiting Phase 4 trials, and a growing evidence base from observational and mechanistic literature. Evidence reaches L2, sufficient to proceed with structured investigation — while noting that the drug is not yet registered in the Philippines, and critical safety data gaps remain.

**To proceed, the following is needed:**

- **Mechanism of action (MOA) data**: Query DrugBank API for DB00819 to formally document CA isoform selectivity and pharmacodynamics
- **Philippines regulatory pathway**: Initiate FDA Philippines registration assessment; evaluate importation pathway or parallel import options given zero current licenses
- **Safety package**: Obtain and parse the full package insert (TFDA / EMA SmPC) to address the Blocking-severity data gap (DG001) covering warnings and contraindications
- **DDI profiling**: Investigate interactions with common co-medications in cardiomyopathy patients (loop diuretics, digoxin, ACE inhibitors, beta-blockers, SGLT2 inhibitors)
- **Electrolyte monitoring protocol**: Define monitoring plan for serum potassium, sodium, chloride, bicarbonate, and renal function — particularly critical given the documented ionic perturbation risks (hypokalemia, metabolic acidosis)
- **Route of administration decision**: Given the safety signal with IV administration in cardiac patients (PMID 29123889), define whether oral-only use is appropriate for the Philippines context
- **Trial outcome surveillance**: Monitor results of NCT05802849 (completion: Dec 2025) and NCT06166654 (completion: Sep 2027) for Phase 4 efficacy and safety data before committing to formal development

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before clinical application. This content follows YMYL standards — consult qualified healthcare professionals for medical decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

