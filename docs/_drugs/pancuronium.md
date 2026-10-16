---
layout: default
title: Pancuronium
parent: Model Prediction Only (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pancuronium: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the Philippines registration data"
monitor_inn: "Pancuronium"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "obsolete neurogenic bladder (disease)", "neurocirculatory asthenia", "migraine disorder", "migraine with brainstem aura", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "autonomic nervous system disease", "MVP1"]
---

# Pancuronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pancuronium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Pancuronium is a non-depolarizing neuromuscular blocker. No approved indication is on record in the data compiled for this report.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The score is purely computational and the evidence level is L5.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines registration data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Pancuronium is generally known as a non-depolarizing neuromuscular blocker. It antagonizes nicotinic acetylcholine receptors at the motor end plate and has vagolytic activity.

For cauda equina syndrome, the relationship is hard to justify. It is a compressive neurological emergency that requires surgical decompression. Blocking neuromuscular transmission has no plausible therapeutic effect on it. The high TxGNN score (rank 654) reflects proximity in the knowledge graph, not pharmacological reasoning.

The other top-ranked predictions (irritable bowel syndrome, neurogenic bladder, neurocirculatory asthenia, migraine, mitral valve prolapse and autonomic nervous system disease) also lack a credible mechanistic link. The only one with any literature is autonomic nervous system disease, and that literature is indirect (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome, or for any of the other top 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

Among the other predictions, two have retrieved papers. None of them shows therapeutic benefit from pancuronium:

| Predicted Indication | PMID | Year | Type | Journal | Key Findings |
|------|------|-----|------|---------|---------|
| Neurocirculatory asthenia | [2633661](https://pubmed.ncbi.nlm.nih.gov/2633661/) | 1989 | Other | Ann Fr Anesth Reanim | Haemodynamics in liver transplantation with a veno-venous shunt; does not address the disease |
| Autonomic nervous system disease | [7793215](https://pubmed.ncbi.nlm.nih.gov/7793215/) | 1995 | Clinical physiology | Acta Anaesthesiol Scand | Haemodynamic effects of vecuronium vs pancuronium in diabetic patients with autonomic neuropathy during vitrectomy |
| Autonomic nervous system disease | [156745](https://pubmed.ncbi.nlm.nih.gov/156745/) | 1979 | Clinical observational | Intensive Care Med | Autonomic dysfunction in tetanus; morphine efficacy and sympathetic effects of three muscle relaxants including pancuronium |
| Autonomic nervous system disease | [24558930](https://pubmed.ncbi.nlm.nih.gov/24558930/) | 2014 | Review | Masui | Anesthetic management of patients with arrhythmogenic right ventricular cardiomyopathy |
| Autonomic nervous system disease | [2677433](https://pubmed.ncbi.nlm.nih.gov/2677433/) | 1989 | Case report | Masui | Anesthesia in a patient with Shy-Drager syndrome |

These papers describe anesthetic and haemodynamic management in patients who already have autonomic dysfunction. They are indirect, safety-oriented evidence only.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0372 | Pancuronium | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 71 interactions were identified. Examples of the main ones:
  - **Major**: paromomycin, kanamycin, neomycin. These aminoglycosides can potentiate neuromuscular blockade.
  - **Moderate**: doxycycline, tetracycline, minocycline, vancomycin, amphotericin B, magnesium sulfate, magnesium chloride, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), metoclopramide, mannitol and trospium.
  - **Minor**: ranitidine.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN network score. There are no clinical trials or direct literature, and no plausible mechanism links neuromuscular blockade to cauda equina syndrome. Systemic paralytic dosing would also be unsuitable for any chronic condition. The only registration in the Philippines is cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Direct preclinical or clinical evidence for the predicted indication
- A clear rationale for why a neuromuscular blocker would suit any of the predicted conditions
- Confirmation of the regulatory and availability status in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

