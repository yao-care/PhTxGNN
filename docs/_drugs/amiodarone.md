---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a well-established multi-class antiarrhythmic agent used globally for life-threatening ventricular and supraventricular arrhythmias, though it currently holds no Philippines regulatory approval.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited arrhythmia triggered by adrenergic stress,
with **no registered clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines (no approved indication data available) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiodarone is a uniquely broad-spectrum antiarrhythmic, exerting effects across all four Vaughan Williams classes simultaneously. It blocks Ikr/Iks potassium channels to prolong the action potential duration and effective refractory period (Class III), inhibits sodium channels to slow conduction velocity (Class I), non-competitively blocks beta-adrenergic receptors to reduce sympathetic drive (Class II), and blocks L-type calcium channels (Class IV). This quadruple ionic mechanism provides comprehensive suppression of both reentrant circuits and automatic or triggered ventricular arrhythmias.

CPVT is caused by gain-of-function mutations in RYR2 (ryanodine receptor type 2) or loss-of-function mutations in CASQ2 (calsequestrin 2), leading to uncontrolled calcium release from the sarcoplasmic reticulum during adrenergic stimulation. This calcium overload drives delayed afterdepolarizations (DADs) and triggered activity, precipitating ventricular tachycardia during exercise or emotional stress. Amiodarone's Class II (beta-blockade) and Class IV (L-type calcium channel blockade) effects can indirectly attenuate this catecholamine-driven calcium overload, forming the mechanistic basis of TxGNN's prediction.

However, this mechanism is indirect — amiodarone cannot repair the underlying SR calcium leak at its molecular source. Clinically, beta-blockers and flecainide (which directly suppresses RYR2-mediated calcium sparks) are the accepted first-line treatments for CPVT. Amiodarone appears in the literature primarily as a salvage or adjunctive agent in refractory cases, ICD storm management, and acute resuscitation scenarios. The TxGNN high score likely reflects amiodarone's broad antiarrhythmic coverage and its documented co-use in patients with life-threatening CPVT episodes unresponsive to standard therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amiodarone in catecholaminergic polymorphic ventricular tachycardia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of advances in pharmacological treatment of ventricular arrhythmias; discusses amiodarone's role in refractory CPVT and other inherited arrhythmia syndromes, noting its use when beta-blockers and flecainide are insufficient |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Retrospective Cohort | Life (Basel) | Systematic review of CPVT patients in China; characterizes RYR2/CASQ2 mutation spectrum, clinical presentations, and arrhythmic outcomes; highlights differences from Western CPVT cohorts in treatment response |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective Cohort | Reviews in Cardiovascular Medicine | CPVT cohort from a Chinese city; describes clinical characteristics, genetic basis, healthcare utilization, and costs; reinforces beta-blocker dominance in treatment but documents use of add-on antiarrhythmics in refractory cases |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | PACE | 14-year-old with CPVT (CASQ2 mutation) developed ICD storm; flecainide successfully suppressed the arrhythmic cascade after prior antiarrhythmic agents (including amiodarone) failed to terminate the storm — illustrates amiodarone's limitations in CPVT ICD storm |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Revista Española de Cardiología | Arrhythmic storm triggered by ICD discharge in a CPVT patient; amiodarone was included in the acute pharmacological management protocol for electrical storm suppression |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Reports | Young child in out-of-hospital cardiac arrest with recurrent pulseless VT/VF requiring 40 defibrillation shocks; ultimately diagnosed with CPVT; amiodarone administered as part of resuscitation when standard guidelines failed — highlights rescue use in acute CPVT arrest |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Frontiers in Cardiovascular Medicine | Teenager with refractory CPVT ultimately resolved by right cardiac sympathetic denervation after failed left cardiac sympathetic denervation; documents the escalating treatment ladder including antiarrhythmic drugs |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | 9-year-old child with CPVT due to RYR2 c.7580T>G mutation; delayed diagnosis of 6 years; case highlights diagnostic challenges and underlines importance of genetic testing in atypical pediatric presentations |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | 2-year-old presenting with sudden cardiac arrest subsequently diagnosed with CPVT; describes acute resuscitation and initiation of antiarrhythmic therapy |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesthesia and Analgesia | Neonate with compound long QT mutation and refractory VT; multimodal pharmacotherapy with amiodarone, esmolol, and lidocaine alongside ventricular pacing — underscores amiodarone's place in neonatal refractory arrhythmia management |

---

## Philippines Market Information

Amiodarone is currently **not registered** with the FDA Philippines. There are no approved product licenses, authorized brand names, or approved indications on record. The drug is unavailable through official Philippines regulatory channels.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for amiodarone specifically in CPVT consists entirely of case reports, retrospective cohort studies, and reviews (L3) with no dedicated clinical trials. Beta-blockers and flecainide remain the established standard of care for CPVT, and amiodarone's documented role is limited to refractory, rescue, and acute resuscitation scenarios. Combined with the absence of Philippines market authorization and unresolved safety data gaps, there is insufficient basis to advance amiodarone as a new CPVT indication at this stage.

**To proceed, the following is needed:**
- Philippines FDA safety data: package insert (warnings, contraindications, and drug interactions) must be retrieved before any safety screening can be completed
- Mechanism of action (MOA) data from DrugBank to formally confirm the indirect calcium-modulating and adrenergic-blocking rationale specific to CPVT pathophysiology
- Prospective observational registry or controlled pilot data in CPVT patients receiving amiodarone as adjunctive therapy
- Drug interaction assessment, particularly with beta-blockers, flecainide, and other CPVT standard-of-care agents that are likely to be co-administered
- Review of amiodarone's approved international indications (FDA USA, EMA) to assess whether CPVT or related inherited arrhythmias are within current label scope
- Given the absence of Philippines registration, a regulatory pathway assessment (new drug application vs. expanded access) would be required before any local clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

