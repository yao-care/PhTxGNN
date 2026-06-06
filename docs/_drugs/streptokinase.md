---
layout: default
title: Streptokinase
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Streptokinase
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

# Streptokinase: From Thrombolytic Therapy to Myocardial Infarction

## One-Sentence Summary

Streptokinase is a first-generation thrombolytic agent with decades of global clinical use for dissolving blood clots in acute thrombotic emergencies; it is currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Myocardial Infarction**, supported by **multiple completed Phase 3 and Phase 4 clinical trials** and **20 publications** — representing some of the strongest evidence encountered in this analysis.
This is less a case of drug repurposing than one of introducing a well-established global standard of care into the Philippines market, where supply and registration gaps remain.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the Philippines (no local licenses on record) |
| Predicted New Indication | Myocardial Infarction |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Streptokinase works by binding endogenous plasminogen to form an activator complex, which then converts free plasminogen into plasmin — the enzyme that cleaves fibrin within blood clots. This mechanism is directly and precisely relevant to ST-elevation myocardial infarction (STEMI), where acute occlusion of a coronary artery by a fibrin-rich thrombus is the immediate cause of myocardial injury. By dissolving the obstructing clot, streptokinase restores coronary blood flow (TIMI flow), salvages ischemic myocardium, and reduces mortality.

The evidence linking streptokinase to myocardial infarction is not theoretical — it is foundational. Landmark randomized trials beginning in the early 1980s (ISAM, GISSI, ASSET, ISIS-2) established that intravenous streptokinase significantly reduces short- and long-term mortality in acute MI. The GUSTO trial series further refined fibrinolytic strategy, situating streptokinase as the reference comparator against newer agents. In environments where primary percutaneous coronary intervention (PCI) is unavailable or delayed, streptokinase remains a WHO Essential Medicine and a guideline-endorsed reperfusion option.

The absence of Philippines registration most likely reflects historical market and supply chain factors, not a scientific concern. The TxGNN model's top-ranked prediction (score 99.83%) is therefore entirely consistent with decades of global clinical consensus. Bringing streptokinase into the Philippines for STEMI care represents a public health opportunity, particularly for institutions without 24-hour cath lab access.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00302419](https://clinicaltrials.gov/study/NCT00302419) | Phase 4 | Completed | 95 | Intracoronary streptokinase adjunct to primary PCI in acute MI; hypothesis that it improves microvascular perfusion by dissolving microvascular thrombus beyond the culprit lesion |
| [NCT00627809](https://clinicaltrials.gov/study/NCT00627809) | Phase 4 | Completed | 53 | Low-dose intracoronary streptokinase + standard PCI vs PCI alone in AMI; evaluated late infarct size and LV volumes at 6 months post-procedure |
| [NCT00000507](https://clinicaltrials.gov/study/NCT00000507) | Phase 3 | Completed | N/A | ISAM-era pivotal study of IV streptokinase in acute transmural MI to limit myocardial damage; 1983–1994 follow-up |
| [NCT00000505](https://clinicaltrials.gov/study/NCT00000505) | Phase 3 | Completed | N/A | TIMI I & II trials: IV rt-PA vs IV streptokinase in acute MI; established comparative thrombolytic activity and set the framework for reperfusion strategy |
| [NCT01305226](https://clinicaltrials.gov/study/NCT01305226) | Phase 3 | Completed | 120 | Recombinant staphylokinase (THR-100) vs streptokinase in AMI; direct head-to-head fibrinolytic comparison using double-bolus dosing |
| [NCT02182011](https://clinicaltrials.gov/study/NCT02182011) | Phase 3 | Completed | 49 | Open-label randomized comparison of procoagulant effects of TNK-tPA, alteplase, and streptokinase in AMI; measured TAT, D-dimers, F1+2 at 2, 6, 24 hours |
| [NCT00245648](https://clinicaltrials.gov/study/NCT00245648) | Phase 3 | Completed | N/A | GUSTO-V substudy: sex-based differences in death and bleeding outcomes among fibrinolytic-treated AMI patients |
| [NCT01930682](https://clinicaltrials.gov/study/NCT01930682) | Phase 4 | Completed | 344 | EARLY-MYO trial: pharmaco-invasive strategy with half-dose fibrinolysis vs primary PCI in STEMI within 6 hours; non-inferiority design for real-world transfer delays |
| [NCT03677466](https://clinicaltrials.gov/study/NCT03677466) | N/A | Completed | 60 | Frequency and intensity of intramyocardial haemorrhage in primary STEMI with different reperfusion strategies, including pharmacological thrombolysis |
| [NCT00000503](https://clinicaltrials.gov/study/NCT00000503) | Phase 3 | Completed | N/A | Early randomized trial of non-surgical coronary reperfusion; assessed streptokinase effect on infarct size in acute MI (1982–1987) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2146913](https://pubmed.ncbi.nlm.nih.gov/2146913/) | 1990 | RCT / Meta-analysis | Ann Intern Med | Meta-analysis of IV streptokinase effect on early mortality stratified by infarct location (anterior vs inferior); significant mortality reduction demonstrated |
| [481511](https://pubmed.ncbi.nlm.nih.gov/481511/) | 1979 | Clinical Trial | N Engl J Med | European multicentre controlled trial in 512 AMI patients; 24h streptokinase infusion vs glucose; significantly lower 6-month mortality (P<0.01) in treated group |
| [2868343](https://pubmed.ncbi.nlm.nih.gov/2868343/) | 1986 | Clinical Trial | Lancet | Landmark streptokinase trial in acute MI; part of the evidence base establishing routine thrombolysis for STEMI |
| [21070617](https://pubmed.ncbi.nlm.nih.gov/21070617/) | 2012 | Review | Cardiovasc Ther | Comprehensive narrative review tracing the history of thrombolytics in MI from streptokinase discovery through modern tPA-based agents; summarizes mortality benefit data |
| [8005961](https://pubmed.ncbi.nlm.nih.gov/8005961/) | 1993 | Review / RCT Summary | J Assoc Physicians India | Summary of major RCT evidence for streptokinase in acute MI from an emerging-market perspective; relevant to lower-resource settings like the Philippines |
| [4934187](https://pubmed.ncbi.nlm.nih.gov/4934187/) | 1971 | Clinical Trial | BMJ | European Working Party multicentre controlled trial: 730 AMI patients (<24h onset) randomized to streptokinase vs heparin; early evidence for thrombolysis benefit |
| [3985460](https://pubmed.ncbi.nlm.nih.gov/3985460/) | 1985 | Clinical Study | Ann Emerg Med | 30 consecutive AMI patients treated with high-dose IV streptokinase (1.5 MU/30 min) in an emergency setting; assessed feasibility and reperfusion timing |
| [3308411](https://pubmed.ncbi.nlm.nih.gov/3308411/) | 1987 | Review | Drugs | Pharmacology and clinical use of APSAC (anisoylated plasminogen streptokinase activator complex); highlights fibrin-selective advantages over conventional streptokinase |
| [2955892](https://pubmed.ncbi.nlm.nih.gov/2955892/) | 1987 | Review | Cardiovasc Clinics | Review of thrombolysis with streptokinase and tPA in acute MI; comparative pharmacodynamics and clinical implications |
| [481517](https://pubmed.ncbi.nlm.nih.gov/481517/) | 1979 | Early Clinical | N Engl J Med | Early clinical characterization of streptokinase use in myocardial infarction; foundational literature establishing feasibility |

---

## Philippines Market Information

Streptokinase currently has **no registered products with the FDA Philippines**. No authorization numbers, product names, or approved indications are on record. This is consistent with the `market_status: "未上市"` (Not marketed) designation in the regulatory data.

This absence is notable given that streptokinase appears on the WHO Model List of Essential Medicines for use in acute MI and other thromboembolic conditions, and is available in neighbouring countries including India, Bangladesh, and parts of Southeast Asia at relatively low cost.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack (designated as data gaps requiring TFDA package insert review and DrugBank query). As a thrombolytic agent, streptokinase carries well-known class risks including hemorrhage (including intracranial bleeding), allergic and anaphylactic reactions (due to bacterial origin), and reperfusion arrhythmias — these should be reviewed against the manufacturer's current labelling before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Streptokinase for myocardial infarction carries L1-level evidence — the strongest evidence tier in this framework — based on multiple completed Phase 3 and Phase 4 trials and a broad literature base spanning more than four decades. The TxGNN prediction score of 99.83% reflects what global clinical practice already confirms. The key barrier in the Philippines is not scientific: it is regulatory access, supply chain, and cold-chain logistics for a temperature-sensitive biologic.

**To proceed, the following is needed:**
- Initiate Philippines FDA registration or identify a compassionate use / unregistered drug access pathway
- Confirm cold-chain storage and logistics feasibility (streptokinase requires refrigeration at 2–8°C)
- Obtain the full manufacturer package insert to document contraindications, key warnings, and dosing protocols for the Philippines clinical context
- Develop a STEMI treatment protocol defining which patients should receive streptokinase vs. be transferred for primary PCI, based on time-to-balloon estimates at referring hospitals
- Establish a pharmacovigilance plan covering hemorrhagic complications and allergic reactions, with clear escalation pathways
- Assess cost-effectiveness relative to locally available alternatives (e.g., tenecteplase, urokinase) in the Philippines healthcare system
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

