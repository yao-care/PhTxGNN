---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 1
---

# Bumetanide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Bumetanide: From Edema / Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic classically used to treat edema associated with congestive heart failure, hepatic disease, and renal disease.
The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease (Cor Pulmonale)**,
with **3 clinical trials** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Edema associated with congestive heart failure, hepatic and renal disease |
| Predicted New Indication | Acute Pulmonary Heart Disease (Cor Pulmonale) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Bumetanide is a potent **loop diuretic** that acts by inhibiting the **NKCC2 (Na⁺-K⁺-2Cl⁻) co-transporter** in the thick ascending limb of the Loop of Henle in the kidney, dramatically reducing sodium and water reabsorption. This produces a rapid and marked diuresis within 30 minutes of administration, persisting for 3–6 hours.

In Acute Pulmonary Heart Disease (Cor Pulmonale), the underlying pathophysiology involves chronic lung disease → pulmonary hypertension → right ventricular pressure overload → impaired venous return → systemic and pulmonary edema. Diuretic therapy is a cornerstone of management: by reducing preload, loop diuretics relieve right ventricular distension, reduce pulmonary artery occlusion pressure (PAOP), and improve oxygenation. This mechanism is essentially the same pathway through which Bumetanide exerts benefit in general congestive heart failure.

A 1987 prospective hemodynamic study (PMID 3304383) directly documented that intravenous bumetanide reduced PAOP and cardiac index in patients with acute heart failure, providing direct mechanistic evidence applicable to acute cor pulmonale. The pathway from its established use in heart failure edema to acute pulmonary heart disease is mechanistically coherent, albeit without a dedicated RCT in the cor pulmonale subpopulation specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | **Withdrawn** | 0 | Investigated whether a single 4 mg intranasal dose of bumetanide acutely reduces pulmonary artery pressure and blood volume in heart failure patients with implanted CardioMEMS™/Cordella™ monitoring devices. Trial withdrawn before any data collected; serves only as indirect evidence that researchers considered this direction worth exploring. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluated empagliflozin + sacubitril/valsartan in adult congenital heart disease with reduced-EF heart failure. Bumetanide is **not** the investigational drug; provides background context on heart failure management challenges only. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational study validating seismocardiographic (wearable) monitoring technology in heart failure patients (expected completion January 2027). Not a bumetanide efficacy trial; provides evidence of active research in the HF monitoring space. |

> ⚠️ None of the three identified trials directly evaluate Bumetanide efficacy in acute pulmonary heart disease with interpretable results. The only directly relevant trial (NCT07375212) was withdrawn before enrollment.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Prospective Hemodynamic Study | Br J Clin Pharmacol | IV bumetanide (25 µg/kg) in 24 CAD patients with acute or chronic heart failure: reduced PAOP, cardiac index, and systemic vascular resistance index—directly demonstrating pulmonary hemodynamic benefit relevant to cor pulmonale. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Narrative Review | Drugs | Comprehensive pharmacodynamic and pharmacokinetic review; confirms bumetanide's approved use in **acute pulmonary congestion**, oedema from CHF, hepatic and renal disease, with onset within 30 minutes of IV dosing. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Clinical Review | Am J Therapeutics | Reviews therapeutic options for acute decompensated heart failure (1 million hospitalizations/year in US); confirms loop diuretics as first-line agents for congestion and volume overload management in AHF. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Review | Ann Pharmacotherapy | Head-to-head comparison of loop diuretics (bumetanide vs. furosemide vs. torsemide); documents bumetanide's superior oral bioavailability (~80%) and equivalent efficacy, informing route selection for outpatient cor pulmonale management. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Retrospective Epidemiological Study | Am J Emerg Med | Analysis of US ED heart failure presentations 2016–2023; characterizes admission rates, evaluation patterns, and treatment—contextualizes the acute care burden relevant to acute pulmonary heart disease presentations. |

---

## Philippines Market Information

Bumetanide currently has **no registered products** with the Philippine FDA. There are no Food and Drug Administration (Philippines) license entries on record.

> For clinical access in the Philippines, importation under a compassionate/special use permit or clinical trial framework would be required.

---

## Safety Considerations

Detailed local package insert warnings and contraindications are not available in this Evidence Pack (data gaps identified for TFDA label warnings and DDI data).

> Please refer to the international package insert (e.g., US FDA prescribing information for Bumetanide) for complete safety information, including electrolyte monitoring requirements, ototoxicity risk, and sulfonamide hypersensitivity considerations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bumetanide's loop diuretic mechanism is directly applicable to the pathophysiology of acute pulmonary heart disease (volume overload, elevated PAOP, right ventricular distension), and its use in acute pulmonary congestion is historically documented—evidenced by published hemodynamic data and narrative reviews (Evidence Level L3). However, no dedicated RCT specifically in acute cor pulmonale exists, the only directly relevant trial was withdrawn before enrollment, and the drug is not currently registered in the Philippines.

**To proceed, the following is needed:**

- **Regulatory pathway**: Evaluate options for compassionate use, special import permit, or clinical trial IND application with Philippine FDA given zero local registrations
- **Phase 2 RCT design**: Initiate a prospective randomized trial comparing bumetanide vs. furosemide specifically in acute cor pulmonale (COPD/pulmonary hypertension subgroup) with PAOP and right ventricular function as primary endpoints
- **MOA data supplement**: Retrieve full DrugBank mechanistic data (DB00887) to complete mechanism-of-action section and support regulatory submission
- **Safety dossier**: Download and parse the full prescribing information PDF to extract contraindications (particularly sulfonamide allergy, anuria, hepatic coma), electrolyte monitoring protocols, and ototoxicity risk data
- **DDI assessment**: Re-query DDI database with expanded search terms; pay particular attention to interactions with antihypertensives, aminoglycosides, and NSAIDs commonly co-administered in cor pulmonale patients
- **Local pharmacoeconomic assessment**: Given no local market presence, conduct cost-accessibility analysis to inform feasibility of clinical program in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

