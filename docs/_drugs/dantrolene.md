---
layout: default
title: Dantrolene
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Dantrolene: predicted new indication Malignant hyperthermia, susceptibility to (evidence level L5). Approved use: Malignant hyperthermia of anaesthesia"
monitor_inn: "Dantrolene"
predicted_indications: ["malignant hyperthermia, susceptibility to", "moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis, susceptibility to", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Dantrolene: From Malignant Hyperthermia of Anaesthesia to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene was originally used to treat malignant hyperthermia during anaesthesia and exercise-induced malignant hyperthermia.
The TxGNN model predicts it may be effective for **malignant hyperthermia, susceptibility to**, with **0 registered clinical trials** and **18 publications** (mainly guidelines and reviews) currently supporting this direction.
This predicted indication is closely related to the original one, so the prediction mostly confirms an established use rather than opening a new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant hyperthermia of anaesthesia; exercise-induced malignant hyperthermia |
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (guidelines and reviews; no registered trials) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for dantrolene was not available in the data compiled for this report. Based on the supporting literature, dantrolene inhibits calcium release through the skeletal muscle ryanodine receptor (RYR1) from the sarcoplasmic reticulum. One study (PMID 28373535) also reports that dantrolene requires magnesium to arrest malignant hyperthermia.

Malignant hyperthermia susceptibility is mainly caused by gain-of-function variants in RYR1 (rarely CACNA1S), which lead to uncontrolled calcium release in skeletal muscle when exposed to volatile anaesthetics or succinylcholine. The original indication (the acute crisis) and the predicted indication (the underlying susceptibility state) describe the same disease spectrum, and dantrolene acts directly on the defective pathway.

Formal randomised trials are not feasible for this emergency condition. The Association of Anaesthetists 2020 guideline and the European Malignant Hyperthermia Group consensus guidelines therefore form the core evidence. The "L3" level reflects the absence of Phase 3 data in the compiled data, not weak support.

### Other predicted indications (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Suggested Status |
|------|------|------|------|
| King-Denborough syndrome | 99.87% | L4 | Research question (best framed as MH prophylaxis/treatment in this population, not treatment of the myopathy itself) |
| Central core myopathy | 99.86% | L4 | Research question (supports MH risk management only) |
| Myopathy, centronuclear | 99.66% | L4 | Research question (indirect evidence; one 1998 case report of prophylactic dantrolene in central core disease) |
| Congenital multicore myopathy with external ophthalmoplegia | 99.87% | L4 | Hold (genetic association only) |
| Moderate multiminicore disease with hand involvement | 99.90% | L5 | Hold (model prediction only) |
| Hypokalaemic periodic paralysis | 99.78% | L5 | Hold (speculative link) |
| Thyrotoxic periodic paralysis (two entries) | 99.74% / 99.67% | L5 | Hold (speculative link) |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists 2020 guideline on malignant hyperthermia |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus guideline | Br J Anaesth | European MH Group consensus on perioperative management of suspected or susceptible patients; notes no interventional trial evidence exists |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | Overview of MH as a pharmacogenetic skeletal muscle disorder; incidence 1:10,000 to 1:250,000 anaesthetics |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative review of epidemiology and management of critically ill MH patients |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | MH is a rare, potentially lethal calcium release channel disorder; mortality has improved |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic study | PNAS | Dantrolene requires Mg2+ to arrest MH |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Dantrolene sodium described as the ultimate treatment for MH |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | MH as a pharmacogenetic disorder of skeletal muscle |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Review | Acta Anaesthesiol Scand | Scandinavian update; most cases linked to RYR1 mutations |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Review | Korean J Anesthesiol | Autosomal dominant inheritance with variable expression and incomplete penetrance |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0129 | Dantrolene | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: contraindication links were recorded for liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, lung disease and a rare pulmonary disease. These should be verified against the package insert.
- **Drug Interactions**: 72 interactions were identified. The major-level interactions in the list reviewed are **morphine** and **liposomal morphine**. Moderate-level interactions include dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol and promethazine. Several others (e.g. pantoprazole, omeprazole, metformin, simvastatin, clarithromycin, clopidogrel) have an unclassified severity level.

Package insert warnings and contraindications were not available; please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Dantrolene's use in malignant hyperthermia is well supported by guidelines, consensus statements and mechanistic work, and the predicted indication is essentially the same disease spectrum as the original one. However, there are no registered trials, and the only Philippines registration is cancelled, so this cannot proceed as a straightforward go.
- The other predicted indications (RYR1-related myopathies and periodic paralyses) rest on indirect or purely model-based evidence and should stay as research questions or on hold.

**To proceed, the following is needed:**
- Confirm the regulatory situation in the Philippines (reason for cancellation, and whether a new registration or emergency-use supply route is needed)
- Obtain and review the package insert (warnings, contraindications, dosage forms and routes)
- Obtain the mechanism of action from DrugBank to complete the mechanistic analysis
- Review the interaction list, especially with opioids and other central nervous system depressants, and the liver-related cautions
- For RYR1-related myopathies, define the intended use (MH prophylaxis vs. disease treatment) before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

