---
layout: default
title: Isoflurane
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Isoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Philippines registration record (general anaesthesi…"
monitor_inn: "Isoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
---

# Isoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Isoflurane: From General Anaesthesia to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Isoflurane is a volatile (inhaled) general anaesthetic. The TxGNN model predicts it may be effective for **Prinzmetal angina**, its top-ranked prediction, but **no clinical trials and no publications** support this specific prediction. Of the other predictions, only migraine disorder (12 publications, mostly preclinical) and manic bipolar affective disorder (3 publications, indirect) have any literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration record (general anaesthesia is the known use of this drug class) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on general pharmacology, volatile anaesthetics such as isoflurane inhibit voltage-gated calcium channels and relax vascular smooth muscle. In theory this could counter the coronary vasospasm behind Prinzmetal angina.

This is a hypothesis only. No trials or literature were found to support it. Isoflurane is a general anaesthetic given by inhalation under monitored conditions, so it cannot be used for long-term management of a chronic condition like vasospastic angina.

**Other predictions reviewed**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Tourette syndrome | 0.9961 | L5 | Prediction only; no supporting data |
| Manic bipolar affective disorder | 0.9957 | L5 | Indirect evidence only (see below) |
| Trichotillomania | 0.9954 | L5 | Prediction only; no supporting data |
| Dysthymic disorder | 0.9927 | L5 | Prediction only; unsuitable for chronic use |
| Nephrogenic syndrome of inappropriate antidiuresis | 0.9909 | L5 | No plausible link (the disease arises from a vasopressin V2 receptor variant) |
| Migraine disorder | 0.9906 | L4 | Plausible preclinical rationale; flagged as a research question |

For **migraine**, inhaled anaesthetics suppress cortical spreading depression, the biological basis of migraine aura (PMID 8665587). Two case reports describe general anaesthesia for status migrainosus. This is the most mechanistically plausible of the predictions, but practical use would be limited to refractory, hospital-based settings, and recurrence after emergence would need to be addressed.

For **bipolar mania**, the only relevant human data is a small 1993 open-label study comparing burst-suppression isoflurane anaesthesia with electroconvulsive therapy in severe depression (PMID 8462536). This does not directly concern mania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top prediction (Prinzmetal angina). The tables below show the most relevant publications for the two predictions that have some.

**Migraine disorder (selected)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Preclinical | Cephalalgia | Inhaled anaesthetics inhibit cortical spreading depression, with relevance to migraine |
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case report | Braz J Anesthesiol | Status migrainosus treated with general anaesthesia (propofol/isoflurane act on GABA-A receptors) |
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | Case report | Rev Bras Anestesiol | Same case as above, published in another language |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Preclinical | J Pharmacol Exp Ther | NMDA receptor antagonists suppress cortical spreading depression in rats |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | Preclinical | J Headache Pain | The CGRP antagonist atogepant does not alter spreading depression susceptibility in rats |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Preclinical | J Neurosci | Susceptibility of the primary sensory cortex to spreading depolarizations |

The remaining migraine papers are preclinical migraine-model studies (CGRP, nitric oxide, topiramate, cannabinoids, passive smoking). They do not test isoflurane as a treatment.

**Manic bipolar affective disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | Open-label clinical study (12 patients) | Eur J Anaesthesiol | Burst-suppression isoflurane anaesthesia and ECT both markedly improved severe, treatment-refractory depression |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | Case report | AANA J | Differential diagnosis of malignant hyperthermia in a patient with manic-depressive illness; not an efficacy study |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | Animal study | Psychiatry Res | FDG-PET in a rat model of mania; isoflurane used only as the anaesthetic for imaging |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0263 | Isoflurane | Not recorded | Not recorded (status: valid) |

---

## Safety Considerations

**Contraindications (from the TxGNN knowledge graph, not label text)**

The knowledge graph links isoflurane with the following conditions:
- Malignant hyperthermia of anaesthesia and exercise-induced malignant hyperthermia
- Duchenne, Becker and other muscular dystrophies
- Liver disease and gallbladder disease
- Hypotensive disorders

**Drug Interactions**

38 interactions were identified. The main ones are:
- **Major:** Epinephrine
- **Moderate:** Morphine, Opium

The remaining interactions have no severity grade recorded. They include atropine, hydrocortisone, dexamethasone, mannitol, omeprazole, pantoprazole, ondansetron, metoclopramide and metronidazole, among others.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (Prinzmetal angina) rests on model score alone (L5), with no trials or publications.
- Isoflurane is an inhaled general anaesthetic, so chronic use for most predicted conditions is impractical.
- It is marketed in the Philippines, with 1 valid license out of 1.
- Migraine (refractory or status migrainosus) is the only prediction with a plausible mechanism and any clinical signal, but that signal is two case reports of one case. It is better treated as a research question than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism of action data (for example from DrugBank)
- For migraine: controlled clinical data in refractory or status migrainosus, with a risk-benefit assessment and a plan for post-emergence recurrence
- Clarification of the cancelled registration status and whether an inhaled anaesthetic can be supplied in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

