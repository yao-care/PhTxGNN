---
layout: default
title: Metoclopramide
parent: Moderate Evidence (L3-L4)
nav_order: 232
evidence_level: L3
indication_count: 5
last_modified_at: 2026-10-15
description: "Metoclopramide: predicted new indication Gastric ulcer (evidence level L3). Approved use: Gastroesophageal reflux disease, esophagitis, peptic esophagitis"
monitor_inn: "Metoclopramide"
predicted_indications: ["gastric ulcer (disease)", "gastroduodenitis", "peptic ulcer disease", "gastrojejunal ulcer", "peptic ulcer perforation"]
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

# Metoclopramide: From Gastroesophageal Reflux Disease to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug, originally used for gastroesophageal reflux disease and reflux esophagitis.
The TxGNN model predicts it may be useful for **gastric ulcer**,
but the support is thin: **1 clinical trial** (on a procedural use, not ulcer treatment) and **20 publications**, mostly older reviews and preclinical studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease, esophagitis, peptic esophagitis |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist that speeds gastric emptying and raises lower esophageal sphincter tone. This explains its use in reflux disease.

Reflux disease and gastric ulcer both belong to upper gastrointestinal acid-peptic disorders, which is likely why the model links them. Mechanistically, however, the link is weak. Metoclopramide does not suppress acid and does not promote mucosal healing. At most it could help with coexisting symptoms such as delayed emptying, nausea or dyspepsia. Any benefit would be adjunctive and symptomatic, not disease-modifying. A 1981 study in healthy volunteers found no significant change in gastrin levels or acid secretion. Standard ulcer care (proton pump inhibitors, *H. pylori* eradication, endoscopic hemostasis) does not rely on it.

The high TxGNN score should therefore be read as a knowledge-graph association, not as evidence of ulcer-healing efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind, single-center RCT of metoclopramide premedication in upper GI bleeding. Tests whether it reduces repeat endoscopy, radiology intervention or surgery and improves visualization. Procedural use only; no results available. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT (double-blind) | Am J Gastroenterol | Efficacy of IV metoclopramide for gastric visualization before endoscopy in active upper GI bleeding. Procedural use, not ulcer healing. |
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | RCT (triple-blind) | Rev Gastroenterol Mex | High-dose metoclopramide vs placebo for endoscopic visualization in acute upper GI bleeding. Its usefulness is described as controversial. |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use of metoclopramide, including easing emergency endoscopy in upper GI haemorrhage. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology and clinical application: antiemetic effect and GI smooth muscle stimulation. |
| [1551349](https://pubmed.ncbi.nlm.nih.gov/1551349/) | 1992 | RCT (double-blind) | Dig Dis Sci | In 20 patients with erosive reflux esophagitis, metoclopramide and domperidone raised lower esophageal sphincter pressure but did not improve esophageal peristalsis or acid clearance. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomized crossover (healthy volunteers) | MMW Munch Med Wochenschr | No significant change in serum gastrin or gastric acid secretion with metoclopramide or domperidone. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Ulcer-protective and antisecretory effects in rat aspirin-induced and pylorus-ligated ulcer models. Preclinical only. |
| [42127996](https://pubmed.ncbi.nlm.nih.gov/42127996/) | 2026 | Guideline | Endoscopy | ESGE 2026 guideline on peptic ulcer bleeding. Covers bleeding management, not a metoclopramide ulcer indication. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgrad Med | Strategies for refractory peptic lesions and reflux esophagitis. |
| [1441547](https://pubmed.ncbi.nlm.nih.gov/1441547/) | 1992 | Review | Wiad Lek | Non-ulcer dyspepsia; the authors favor prokinetics including metoclopramide. This is a different condition from ulcer. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0322 | Metoclopramide | Not specified | Not specified (status: cancelled) |

## Safety Considerations

**Contraindications and cautions suggested by the knowledge graph** (taken from the knowledge graph, not from label text):
- Neurological: Parkinson disease and parkinsonian disorders, epilepsy, tardive dyskinesia, torsion dystonia, neuroleptic malignant syndrome
- Cardiovascular and endocrine: hypertension, pheochromocytoma and related adrenal or paraganglioma tumours
- Gastrointestinal and organ function: active peptic ulcer disease, cirrhosis of liver, impaired renal function
- Psychiatric: anxiety disorder, dysthymic disorder
- Metabolic: porphyria, methemoglobinemia due to methemoglobin reductase deficiency, pyruvate dehydrogenase E3 deficiency

Prokinetics are also generally avoided where perforation or obstruction is suspected, because increased motility could be harmful.

**Drug interactions:** The interaction screening returned 100 interacting drugs; the main ones are:
- **Major:** tramadol, amisulpride
- **Moderate:** opioids (fentanyl, alfentanil, codeine, dihydrocodeine), sedating antihistamines (chlorpheniramine, cetirizine), alprazolam, amitriptyline, amobarbital, ethanol, amantadine, abiraterone
- **Minor:** acetaminophen

Many of the moderate interactions involve additive central nervous system depression.

Please also refer to the package insert for full warnings. Label-based warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered trial and the most recent randomized studies concern a procedural use (endoscopic visualization in GI bleeding), not ulcer treatment. Mechanistically, metoclopramide offers no acid suppression or mucosal healing. The knowledge graph also lists active peptic ulcer disease among its contraindications. The model score therefore looks like a knowledge-graph association rather than a true therapeutic signal. In addition, the only Philippine registration is cancelled.

The other predictions are also weak:
- Gastroduodenitis: 99.90%, L3, research question only
- Peptic ulcer disease: 99.85%, L4, hold
- Gastrojejunal ulcer: 99.78%, L4, hold
- Peptic ulcer perforation: 99.78%, L5, hold. The score is likely a knowledge-graph artifact, and the drug is contraindicated in suspected perforation.

**To proceed, the following is needed:**
- A well-designed trial or systematic review showing benefit in ulcer symptoms or healing, as an adjunct to standard therapy
- Clarification of the "active peptic ulcer disease" contraindication signal against the official label
- Package insert warnings and contraindications from DOH-FDA Philippines (currently missing, and a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Confirmation of the regulatory pathway, since the Philippine registration is cancelled and has no recorded dosage form or indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

