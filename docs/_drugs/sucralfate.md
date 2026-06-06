---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Sucralfate: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate is a cytoprotective agent widely used for the treatment of gastric and duodenal ulcers (peptic ulcer disease), protecting the gastric mucosa against acid and enzymatic damage.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux (DGR)**, with **0 registered clinical trials** but **13 publications** — including 1 double-blind RCT and 1 controlled clinical trial — currently supporting this direction.
The biological rationale is well-grounded: sucralfate's bile acid–binding and cytoprotective properties address the core pathophysiology of DGR-associated alkaline gastritis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease (gastric and duodenal ulcer) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data from DrugBank is not available for this report. Based on well-established pharmacological knowledge, sucralfate acts primarily as a **mucosal protective (cytoprotective) agent**. It forms a viscous, paste-like barrier by binding to damaged or ulcerated mucosal surfaces, shielding them from acid, pepsin, and bile salts. It also stimulates prostaglandin E₂ synthesis and increases mucus secretion, reinforcing the stomach's natural defences.

The connection to duodenogastric reflux (DGR) is mechanistically direct. In DGR, alkaline duodenal contents — particularly bile salts — flow retrograde into the stomach and cause mucosal injury (alkaline/bile reflux gastritis). Sucralfate's ability to **bind bile acids** reduces their direct cytotoxic effect on the gastric epithelium, while its cytoprotective properties promote mucosal repair in the same tissue layer that DGR injures. This constitutes a biologically plausible mechanism with strong face validity.

Sucralfate's original indication (peptic ulcer) and DGR-associated gastritis share the same end-organ — the gastric mucosa — and involve overlapping injury pathways (mucosal barrier disruption, inflammatory infiltration). In clinical practice, alkaline reflux gastritis is often encountered alongside or as a consequence of prior gastric surgery (Billroth procedures), which similarly damages the pyloric barrier. The published literature, including a double-blind RCT, directly tests sucralfate in post-surgical alkaline reflux gastritis patients, providing translational continuity from the original indication to the new one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for sucralfate in duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT (double-blind) | Am J Medicine | Sucralfate 6 g/day vs. placebo in 23 post-surgical alkaline reflux gastritis patients (Billroth I/II, vagotomy+pyloroplasty); evaluated symptoms, endoscopic findings, and histology over 6 weeks |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Controlled Clinical Trial | Minerva Gastroenterol | Sucralfate 4 g/day vs. cisapride in 18 patients with DGR-associated dyspeptic gastritis; 2-month comparative trial |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | Randomized Trial | Eur J Gastroenterol Hepatol | Sucralfate vs. rabeprazole vs. no treatment in post-cholecystectomy alkaline reactive gastritis; assessed dyspeptic symptoms and endoscopic/histological response |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Prospective RCT | Scand J Gastroenterol Suppl | 6-month prospective randomized trial of sucralfate vs. placebo in patients with symptomatic and macroscopic gastritis, with comparison of gastroesophageal and duodenogastric reflux subgroups |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Cohort/Observational | Eur J Pediatrics | 6 pediatric patients (age 4.5–16.5 yr) with primary DGR unresponsive to antacids; 24-h gastric bilimetry documented excess bile exposure |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treatment Gastroenterol | Medical and surgical management of duodenogastroesophageal reflux (DGER); reviews role of mucosal protective agents including sucralfate in alkaline esophagitis |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | J de Chirurgie | Comprehensive review of DGR pathophysiology, 24-hour intraluminal bile monitoring, and therapeutic management including pharmacological options |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Ann Rev Medicine | Pathophysiology of alkaline reflux gastritis post gastric surgery; clinical features (epigastric pain, bilious vomiting, iron-deficiency anemia) and treatment rationale |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterology | American College of Gastroenterology review of sucralfate's non-ulcer uses; cytoprotective properties in gastritis and esophagitis assessed as promising but requiring further study |
| [2186496](https://pubmed.ncbi.nlm.nih.gov/2186496/) | 1990 | Review | Terapevticheskii Arkhiv | Clinical efficacy of sucralfate (antepsin) in 72 patients with erosive/ulcerous gastroduodenal injuries; therapeutic efficacy coefficient 2.67 for duodenal ulcer, 2.1 for gastric ulcer |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of sucralfate in duodenogastric reflux–associated gastritis has direct mechanistic support (bile acid binding, mucosal cytoprotection) and is backed by at least one published double-blind RCT and one controlled clinical trial, placing this at Evidence Level L2. The drug acts precisely on the pathological target of DGR — bile salt–induced gastric mucosal injury — making this a biologically coherent and clinically investigated repurposing candidate. The absence of a Philippines registration, while noted, does not preclude further evaluation.

**To proceed, the following is needed:**

- **Formal MOA documentation** from DrugBank or the Philippines FDA package insert to complete mechanistic risk assessment
- **Philippines FDA safety data** (key warnings, contraindications, and drug interactions from the local prescribing information) — currently a blocking data gap
- **RCT outcome data** from PMID 3839973 and 12923369 (full-text review to confirm effect size, patient population, and safety signals)
- **Route and formulation assessment**: confirm that oral sucralfate suspension or tablet formulation is viable for the DGR patient population in the Philippines context
- **Market access plan**: given 0 current Philippines registrations, a regulatory pathway or import/compassionate-use framework will be required before clinical deployment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

