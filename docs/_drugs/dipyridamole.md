---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Thromboembolism Prevention to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a well-established antiplatelet and coronary vasodilator drug used globally for thromboembolic prevention, particularly in combination with aspirin or warfarin, though it has no registered products in the Philippines.
The TxGNN model ranks **Prinzmetal Angina** as its top predicted new indication (score: 99.99%), with **no clinical trials** and **15 publications** currently associated with this direction.
⚠️ **Critical Safety Note**: Published literature indicates dipyridamole is used clinically as a *pharmacological provocateur* to **trigger** coronary vasospasm for diagnostic purposes — suggesting a potential contraindication rather than a therapeutic opportunity in this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thromboembolism prevention / Antiplatelet therapy (no Philippines regulatory data available) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacology, Dipyridamole inhibits phosphodiesterase enzymes (raising platelet cAMP and vascular smooth muscle cGMP) and blocks adenosine reuptake by red blood cells — resulting in coronary vasodilation and inhibition of platelet aggregation. The vasodilatory component appears mechanistically relevant to Prinzmetal angina, a condition driven by episodic coronary artery spasm, because relaxing coronary vascular tone could theoretically suppress spasm.

However, clinical evidence reveals a far more complicated relationship. Dipyridamole induces maximal vasodilation in normal coronary segments, while vessels prone to spasm respond differently — creating a relative underperfusion through the **coronary steal phenomenon**. This is precisely why dipyridamole is used as a pharmacological stress test agent to *provoke* ischemia for diagnostic purposes, not to treat it. A 1988 mechanistic case series (PMID 3421166) explicitly documented that dipyridamole stress testing followed by aminophylline reversal can actively trigger coronary vasospasm in variant angina patients. The earliest clinical report (PMID 633593, 1978) further confirms that dipyridamole not only failed to suppress angina attacks in Prinzmetal patients but tended to aggravate them.

In summary, TxGNN has detected a real biological association between dipyridamole and Prinzmetal angina, but the direction of effect is *provocation*, not *treatment*. The model reflects connectivity in the knowledge graph without distinguishing causality or clinical intent. This constitutes a critical safety signal that warrants a Hold decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dipyridamole in Prinzmetal Angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Early Clinical Report | Japanese Circulation Journal | In 26 patients with angina at rest (including Prinzmetal's variant), dipyridamole 50 mg not only failed to suppress attacks but tended to aggravate them in all Prinzmetal cases |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Mechanistic Case Series | American Journal of Cardiology | ⚠️ Dipyridamole stress testing followed by aminophylline reversal triggers coronary vasospasm in variant angina via sudden withdrawal of vasodilation — confirms use as a provocateur, not a treatment |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Observational | British Heart Journal | Exercise test reproducibility in 25 patients with ST elevation; dipyridamole echocardiography used as diagnostic tool to stratify vasospasm vs. fixed stenosis |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Echocardiography Study | Journal of the American College of Cardiology | Myocardial echodensity changes during ischemic episodes of varying severity and duration induced by dipyridamole and other mechanisms — characterizes ischemic response patterns |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic Study | Japanese Circulation Journal | Dipyridamole-loading thallium imaging in 38 CAD patients; diagnostic sensitivity 66%, improved to 87% when combined with exercise stress imaging |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Cohort Study | Portuguese Journal of Cardiology | 3-year prognosis assessment of suspected CAD patients with normal dipyridamole-thallium scintigram; favorable outcomes in truly normal scans |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological basis for noninvasive coronary stenosis evaluation; discusses coronary steal mechanism underlying dipyridamole stress testing |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Case Series | Zhonghua Xin Xue Guan Bing Za Zhi | Clinical characteristics of typical vs. atypical coronary artery spasm; dipyridamole referenced in the diagnostic workup context |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case Report | Clinical Nuclear Medicine | Patient with documented variant angina, migraine, and asthma; dipyridamole scintigraphy confirmed inferior/posterior wall ischemia during exercise |
| [6125623](https://pubmed.ncbi.nlm.nih.gov/6125623/) | 1982 | Review | Kardiologiia | Diagnostic and therapeutic challenges in stenocardia including variant angina; reviews role of pharmacological testing agents |

---

## Safety Considerations

**Key Warnings (derived from literature evidence):**
- Dipyridamole can **precipitate coronary vasospasm** in patients with Prinzmetal (variant) angina through the coronary steal phenomenon. This effect is well-documented and forms the clinical basis for dipyridamole stress testing (PMID 3421166).
- The 1978 clinical report (PMID 633593) confirms dipyridamole may **aggravate** rather than suppress variant angina attacks — this is mechanistically consistent with coronary steal.
- Aminophylline (an adenosine antagonist) should always be available to reverse dipyridamole-induced vasodilation in clinical settings where this drug is administered.

Please refer to the package insert for complete safety information, including all warnings and contraindications. Philippines TFDA package insert PDF review is recommended as a critical next step (currently a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dipyridamole's mechanism — potentiation of coronary vasodilation via adenosine accumulation — is associated with *provoking* rather than *treating* Prinzmetal angina. The literature clearly establishes it as a stress test provocateur in this condition, and there are zero clinical trials supporting therapeutic use. Advancing without resolving this safety signal would pose an unacceptable risk to patients.

**Important Context — Stronger Evidence Exists for Other Ranked Indications:**
While rank 1 (Prinzmetal angina) is blocked, the Evidence Pack contains substantially stronger support for **stroke disorder** (rank 2, 31 clinical trials including completed Phase 3/4 RCTs such as PRoFESS, JASAP, and ESPRIT — qualifying for **L1** evidence) and **transient ischemic attack** (rank 5, 15 trials, multiple Cochrane reviews — also **L1**). The aspirin + extended-release dipyridamole combination (Aggrenox) is an internationally guideline-endorsed secondary stroke prevention therapy. These indications represent far higher-value repurposing targets for Philippines registration consideration.

**To proceed, the following is needed:**
- Download Philippines TFDA (or reference FDA) package insert PDF to extract official warnings and contraindications (currently a Blocking data gap)
- Query DrugBank API to obtain full mechanism of action data (currently a High-severity data gap)
- Formally reassign primary repurposing focus to **stroke disorder** (rank 2) or **TIA** (rank 5), which have robust international RCT evidence and established clinical guidelines
- Assess Philippines regulatory pathway for new indication registration of aspirin + dipyridamole for secondary stroke prevention
- Conduct local clinical expert consultation regarding feasibility and unmet need in the Philippines cerebrovascular disease population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

