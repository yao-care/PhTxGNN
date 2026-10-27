---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Methylene Blue: predicted new indication Bronchitis (evidence level L5). Approved use: Methemoglobinemia, sulfhemoglobinemia"
monitor_inn: "Methylene blue"
predicted_indications: ["bronchitis", "methemoglobinemia, alpha type", "methemoglobinemia due to deficiency of methemoglobin reductase"]
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Methylene Blue: From Methemoglobinemia to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Methylene blue was originally used to treat methemoglobinemia and sulfhemoglobinemia.
The TxGNN model predicts it may be effective for **bronchitis**, but the supporting evidence is very weak: **0 clinical trials** and **8 publications**, none of which evaluates methylene blue as a treatment for bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methemoglobinemia, sulfhemoglobinemia |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methylene blue is an established treatment for methemoglobinemia. It is reduced to leucomethylene blue by NADPH-dependent methemoglobin reductase, and this form then converts methemoglobin back to functional hemoglobin.

The link between this mechanism and bronchitis is not demonstrated. Any biological rationale, such as inhibition of nitric oxide/guanylate cyclase signalling or anti-inflammatory effects, is speculative. The high TxGNN score is likely driven by keyword co-occurrence. Methylene blue appears in the literature mainly as a diagnostic stain or laboratory marker in airway-related work, not as a therapy.

Two other predictions are worth noting. Both are subtypes of the drug's original indication, so they are confirmation of known use rather than new repurposing:
- **Methemoglobinemia, alpha type** (score 99.36%): mechanistically strong, but there are no specific trials, and the only publication retrieved concerns protein conformation studies, not treatment. Evidence level L4.
- **Methemoglobinemia due to methemoglobin reductase deficiency** (score 99.36%): methylene blue can bypass the impaired NADH-dependent pathway through the NADPH-dependent route. Support comes from veterinary reports of oral methylene blue in dogs with cytochrome b5 reductase deficiency (PMIDs 35202847, 36638001) and human case reports. Evidence level L4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (bronchitis), none of the retrieved publications tests methylene blue as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic staining study | Zhonghua Wai Ke Za Zhi | Methylene blue staining in bronchoscopy: 97.14% of central malignant bronchial tumours stained vs 8.33% of bronchitis cases. Diagnostic use only |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic staining study | Terapevticheskii Arkhiv | Chromoendoscopy with methylene blue to distinguish benign from malignant gastrointestinal and bronchial neoplasms |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodology | Am Rev Respir Dis | Methylene blue used as one of five markers to quantify intraalveolar fluid in lavage |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Preclinical pharmacology | Int J Clin Pharmacol Ther Toxicol | Methylene blue injection used as an indicator-dilution tool to measure circulation time in a beta-blocker study |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical (ex vivo) | J Ethnopharmacol | Plant essential oil relaxes guinea-pig trachea; unrelated to methylene blue |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical (animal) | J Ethnopharmacol | Antidepressant-like effects of a plant extract; unrelated |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical | Anal Chim Acta | Aptasensor for theophylline detection; unrelated |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case report | Mikrobiyol Bul | Moraxella catarrhalis endocarditis; unrelated |

For the related methemoglobinemia subtype (reductase deficiency), the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36638001](https://pubmed.ncbi.nlm.nih.gov/36638001/) | 2023 | Cohort (veterinary) | Am J Vet Res | Dogs with cytochrome b5 reductase deficiency treated long-term with oral methylene blue; changes in methemoglobin and CRP assessed |
| [35202847](https://pubmed.ncbi.nlm.nih.gov/35202847/) | 2022 | Case report (veterinary) | Top Companion Anim Med | Oral methylene blue in a dog with cytochrome b5 reductase deficiency |
| [29845943](https://pubmed.ncbi.nlm.nih.gov/29845943/) | 2018 | Case report | Neth J Med | Congenital methaemoglobinaemia with a novel CYB5R3 variant; short recurrence after methylene blue |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0318 | Methylene Blue | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so no valid product is currently registered.

---

## Safety Considerations

- **Disease-related cautions (from knowledge-graph contraindication links, not label text)**: G6PD deficiency (risk of haemolysis), hypertension, liver failure, kidney disease, congestive heart failure, diabetes mellitus, anaemia, coronary artery disease, heart conduction disease, myasthenia gravis, and blood coagulation disorders, among others.
- **Drug Interactions**: 100 interactions were identified. Major interactions include:
  - Serotonergic agents and related drugs: bupropion, ondansetron, granisetron, palonosetron, dolasetron, fenfluramine, dexfenfluramine, lorcaserin
  - Sympathomimetics and stimulants: isometheptene, ephedrine, phentermine, diethylpropion, mazindol
  - Opioids: morphine, opium
  - Moderate interactions: epinephrine (including topical and ophthalmic forms) and nasal ephedrine

Serotonin syndrome risk with serotonergic drugs is a key guardrail. Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The very high TxGNN score for bronchitis is not backed by any clinical trial or relevant publication; the apparent link is probably keyword co-occurrence. The methemoglobinemia subtypes are mechanistically sound but are extensions of the existing indication, not new repurposing. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Preclinical or clinical evidence that methylene blue treats bronchitis, if that indication is to be pursued
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Philippines regulator
- Confirmation of product availability (re-registration or import pathway) in the Philippines
- A safety plan covering G6PD screening and serotonergic drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

