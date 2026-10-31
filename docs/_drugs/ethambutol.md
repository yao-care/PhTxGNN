---
layout: default
title: Ethambutol
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Ethambutol: predicted new indication Epiglottitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ethambutol: From Pulmonary Tuberculosis to Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Ethambutol is an anti-mycobacterial drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **epiglottitis**,
but there are **0 clinical trials** and only **1 publication** (a case series on laryngeal tuberculosis) behind this prediction, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ethambutol is an anti-mycobacterial agent used as part of multi-drug tuberculosis regimens, and its efficacy in pulmonary tuberculosis is established.

The only linked publication is a case series of 41 patients with laryngeal tuberculosis, in which the epiglottis was one of the affected sites. This points to tuberculous involvement of the upper airway, not to epiglottitis in general. Typical epiglottitis is bacterial (for example, *Haemophilus influenzae* type b), and there is no plausible mechanism by which ethambutol would act against it. The very high TxGNN score most likely reflects the network proximity of TB-related laryngeal disease and is not a validated signal. At best, the prediction applies to tuberculous epiglottic involvement, which is the approved anti-TB use at a different site rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case series | The European Respiratory Journal | 41 cases of laryngeal tuberculosis (1975–1985). All had current or prior pulmonary TB. The epiglottis was the second most frequently affected site. Patients were treated with isoniazid, rifampicin, ethambutol and other agents. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0178 | Ethambutol | Not specified | Not specified (status: valid) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not from label text): kidney disease, pyoureter, gout, diabetic retinopathy, diabetic cataract, optic neuritis.
- **Drug Interactions**: 100 interactions were identified in total. Those rated Moderate include metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin, tinidazole and aluminum hydroxide. Others, such as pantoprazole, omeprazole, lansoprazole, prednisone and morphine, have an unknown severity level.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, the only supporting literature is a single case series on laryngeal tuberculosis, and no plausible mechanism links ethambutol to typical (bacterial) epiglottitis. The high model score is not backed by evidence. In addition, ethambutol is currently marketed in the Philippines, with 1 valid licence of 1.

**To proceed, the following is needed:**
- Mechanism of action data for ethambutol
- Package insert warnings and contraindications from the Philippine regulator
- Clarification of whether the question is tuberculous epiglottic involvement (already covered by standard anti-TB regimens) or epiglottitis of other causes
- Controlled clinical evidence, if the indication is to be pursued at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

