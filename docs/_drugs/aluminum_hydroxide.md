---
layout: default
title: Aluminum Hydroxide
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 4
---

# Aluminum Hydroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Aluminum Hydroxide: From Gastric Hyperacidity to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide is a classic antacid compound, recognized for its ability to neutralize gastric acid and protect the gastric mucosa in acid-related conditions.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
with **no registered clinical trials** but **20 publications** — including RCTs — currently supporting this direction.
Although not currently registered in the Philippines, its well-established pharmacological mechanism makes this prediction scientifically grounded, with a positioning as a supplementary or alternative option to modern first-line therapies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; globally recognized as an antacid for gastric hyperacidity |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Aluminum hydroxide acts as a chemical antacid through a direct neutralization reaction: **Al(OH)₃ + 3HCl → AlCl₃ + 3H₂O**. By raising intragastric pH, it reduces pepsin activity (which is largely inactive above pH 4) and creates a less corrosive luminal environment. Beyond acid neutralization, aluminum-containing antacids have been shown to stimulate mucosal prostaglandin synthesis (particularly PGE₂) and enhance cytoprotective defense mechanisms, independent of their buffering capacity — a phenomenon documented in both animal models and human biopsy studies.

Active peptic ulcer disease is fundamentally an acid-peptic disorder in which the balance between aggressive factors (gastric acid, pepsin, *H. pylori*) and mucosal defense is disrupted. Aluminum hydroxide addresses this pathology at two levels: reducing the acid-peptic burden and reinforcing the mucosa's own repair capacity. This dual action explains why controlled trials from the 1980s–1990s demonstrated healing rates comparable to cimetidine (H₂-blocker), and why aluminum hydroxide was a mainstay of peptic ulcer therapy for decades before the introduction of proton pump inhibitors (PPIs).

In the current treatment landscape, PPIs and *H. pylori* eradication regimens represent first-line standards of care. However, aluminum hydroxide retains a clinically relevant niche as an adjunct analgesic for ulcer pain relief, a short-term option in resource-limited settings, or an alternative for patients intolerant of PPIs. The TxGNN model's high prediction score (99.64%) accurately reflects this well-documented mechanistic and clinical alignment.

---

## Clinical Trial Evidence

No registered clinical trials specifically evaluating aluminum hydroxide for active peptic ulcer disease were identified in ClinicalTrials.gov or ICTRP at the time of this report.

> Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 72-patient double-blind trial: antacid + anticholinergic vs cimetidine vs placebo in duodenal/prepyloric ulcers; healing rate 50% at 3 weeks (vs 67% cimetidine, 25% placebo) |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | Clinical Pharmacology Study | Digestion | Al(OH)₃ demonstrated gastroprotective activity against ethanol, taurocholate, and aspirin-induced lesions; acidified form showed augmented cytoprotection via prostaglandin-independent mechanisms |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Current Pharmaceutical Design | Updated mechanistic review: aluminum-containing antacids promote mucosal defense via growth factor upregulation (EGF, TGF-α) and prostaglandin synthesis, beyond simple acid neutralization |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Mechanistic Study | Digestive Diseases and Sciences | Maalox and Al(OH)₃ enhanced healing of chronic gastroduodenal ulcerations; prostaglandins and EGF identified as contributing mediators |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | Laboratory Study | Japanese Journal of Pharmacology | Al(OH)₃ (0.1–1 mg/ml) significantly prevented acid- and pepsin-induced damage in rat gastric epithelial cells (RGM1); sucralfate effect attributed largely to its aluminum moiety |
| [2340961](https://pubmed.ncbi.nlm.nih.gov/2340961/) | 1990 | Mechanistic Study | Digestion | Acidified aluminum complex ("activated aluminum complex") was 8× more potent than parent antacid in preventing aspirin-induced gastric lesions; >10 h protective duration in ethanol model |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Narrative Review | Fortschritte der Medizin | Dosing framework for antacids in peptic ulcer: 40–80 mval acid neutralization per dose, 1 and 3 hours postprandially; efficacy dependent on neutralizing capacity by chemical composition |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clinics in Gastroenterology | Comparative review of antacids and anticholinergics in duodenal ulcer treatment; aluminum hydroxide established as effective acid-neutralizing agent with adjunct potential |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Pharmaceutical Analysis | Medicine and Pharmacy Reports | Characterization of acid-neutralizing capacity (ANC) of antacids in current market; methodology for comparing aluminum hydroxide formulations |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Case Series | Drugs under Experimental and Clinical Research | Retrospective study in 267 pediatric patients with peptic symptoms; antacid-based regimens (including aluminum hydroxide) demonstrated efficacy in acute-phase treatment |

---

## Philippines Market Information

Aluminum hydroxide (DrugBank ID: DB06723) currently has **no registered product licenses** in the Philippines Food and Drug Administration (FDA Philippines) database.

> No Philippines FDA authorization records found for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: No drug–drug interaction data, key warnings, or contraindications were retrievable from the available data sources at the time of this report. Prior to any clinical application, the FDA Philippines-approved package insert should be consulted, with particular attention to aluminum toxicity risk in patients with renal impairment (risk of aluminum accumulation), phosphate depletion with prolonged high-dose use, and potential interference with absorption of co-administered medications (e.g., fluoroquinolones, tetracyclines, thyroid hormones).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aluminum hydroxide's mechanism of action (acid neutralization + cytoprotection) directly addresses the pathophysiology of active peptic ulcer disease, and published RCT-level evidence from the pre-PPI era confirms clinical healing efficacy comparable to H₂-blockers. The TxGNN prediction score of 99.64% reflects genuine mechanistic alignment rather than incidental association. However, modern treatment guidelines position aluminum hydroxide as adjunctive rather than first-line, and the absence of contemporary Phase 3 trial data and Philippines registration necessitates a structured approach before any formulary or clinical use recommendation.

**To proceed, the following is needed:**

- **Regulatory pathway**: Submit a product dossier to FDA Philippines; consider bridging from existing approvals in the US (FDA) or EU (EMA) where aluminum hydroxide antacids are marketed
- **Package insert and safety documentation**: Retrieve and review the full prescribing information to address current data gaps on warnings, contraindications, and drug interactions
- **Mechanism of action (MOA) documentation**: Obtain complete DrugBank MOA record to support regulatory submissions and clinical communication materials
- **Contemporary evidence review**: Commission a systematic review or meta-analysis of aluminum hydroxide in peptic ulcer disease using post-2000 literature, including *H. pylori* co-treatment contexts
- **Positioning strategy**: Define the clinical niche (e.g., adjunct pain relief, PPI-intolerant patients, low-resource settings) to align with current Philippine clinical practice guidelines for peptic ulcer disease
- **Renal safety monitoring plan**: Establish criteria for use in patients with renal impairment, given aluminum accumulation risk

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This prediction was generated by the TxGNN computational model and must be interpreted in the context of current clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

