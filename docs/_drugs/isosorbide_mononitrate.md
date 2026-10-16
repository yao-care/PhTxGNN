---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Isosorbide Mononitrate: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not available"
monitor_inn: "Isosorbide mononitrate"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "alopecia", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pulmonary arterial hypertension"]
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Its Original Use to Hypertrichosis (Top Prediction), with Pulmonary Arterial Hypertension as the Most Plausible Candidate

## One-Sentence Summary

Isosorbide mononitrate is a nitric oxide (NO)-donating vasodilator. The data compiled for this report do not record an approved indication for it in the Philippines.
The TxGNN model's top prediction is **hypertrichosis (disease)**, but there are **0 clinical trials** and **0 publications** behind it.
Among the top 10 predictions, only **pulmonary arterial hypertension (PAH)** has any indirect support (**2 publications**, no clinical trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only registration has no indication text) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled records. Isosorbide mononitrate is generally known as an organic nitrate that releases NO, raises cGMP in vascular smooth muscle and causes vasodilation.

For **hypertrichosis**, no established mechanism links this drug to the condition. The only speculative link is that NO-mediated vasodilation might increase blood flow around hair follicles, and no data support it. The high score is a computational prediction, probably driven by network-level associations rather than pharmacology.

The other top-ranked predictions are mostly hair disorders (alopecia, hypotrichosis, alopecia areata, hair shaft abnormalities) and rare congenital malformation syndromes. Most are genetic or autoimmune structural conditions for which a vasodilator has no plausible role. Alopecia is the one exception with a hypothetical perfusion-based rationale, but it is also undocumented.

The most biologically coherent prediction is **pulmonary arterial hypertension** (rank 10, score 99.94%). PAH involves impaired NO–sGC–cGMP signalling, a validated drug target pathway (PDE5 inhibitors, sGC stimulators). Nitrates raise cGMP, so the link is plausible. However, nitrates are not guideline-recommended for PAH, and practical concerns include tolerance, systemic hypotension, ventilation/perfusion mismatch and a dangerous interaction with PDE5 inhibitors.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

Only the PAH prediction has any literature. Neither article is direct evidence for isosorbide mononitrate in PAH.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | The Journal of Sexual Medicine | Hemodynamic effects of sildenafil combined with isosorbide mononitrate in men with coronary artery disease and erectile dysfunction (not a PAH population) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical animal study | Life Sciences | Stimulating NO-sensitive soluble guanylate cyclase in monocrotaline-induced pulmonary hypertensive rats; examined whether NO-enhancing treatment can halt progression (not a nitrate study) |

No literature is available for hypertrichosis or the other top predictions.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0266 | Isosorbide Mononitrate | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph links the drug to contraindications in the following conditions:
  - Hypotensive disorder
  - Hypertrophic cardiomyopathy
  - Myocardial infarction and coronary thrombosis
  - Hemoglobinopathy and anemia (including macrocytic anemia)
  - Hyperthyroidism, Graves disease and thyrotoxicosis
  - Intracerebral hemorrhage
- **Drug Interactions**: 100 interactions were identified in total; 20 are listed in the compiled data.
  - Moderate: bupropion, morphine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, dronabinol, nabilone, opium, sapropterin, rosiglitazone
  - Minor: omeprazole
  - Unknown severity: calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, metformin, lansoprazole
- **Important class concern**: Combination with PDE5 inhibitors (e.g., sildenafil) can cause dangerous hypotension. This matters especially for any PAH use.

Package insert warnings and contraindications were not available. Please refer to the package insert for label-based safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Hypertrichosis and the other top-ranked predictions rest on model scores alone (Evidence Level L5), with no trials, no literature and no plausible mechanism.
- PAH is biologically plausible (Evidence Level L4, flagged as a research question), but the evidence is indirect, nitrates are not guideline-recommended, and the PDE5 inhibitor interaction is a serious concern.
- The only Philippines registration is cancelled, so there is no currently marketed product.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication and dosage form for the cancelled registration
- For PAH: a targeted literature review for direct nitrate data and a safety assessment of PDE5 inhibitor co-use
- For hair disorders: preclinical or pilot evidence for any perfusion-based benefit before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

