---
layout: default
title: Codeine
parent: Moderate Evidence (L3-L4)
nav_order: 86
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
---

# Codeine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Codeine: From Rhinitis and Headache Symptom Relief to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid originally used for symptom relief in allergic rhinitis, vasomotor rhinitis, pharyngitis, the common cold, nasopharyngitis and headache disorders.
The TxGN model predicts it may be effective for **nasal cavity disease**, but there are **0 clinical trials** and only **1 publication** (a case report describing an adverse event), so the evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is an opioid that acts mainly through conversion to morphine and mu-opioid receptor agonism. It has central antitussive and analgesic effects, which explains its past use for symptomatic relief in cold-like and upper airway conditions.

The very high prediction score most likely reflects graph proximity to the existing rhinitis and nasopharyngitis indications rather than a distinct therapeutic mechanism. Nasal cavity disease is a broad category that overlaps with those original indications, so the prediction is largely a restatement of existing use rather than a new repurposing signal.

The only literature found is a case report of a rhinolith formed around a hardened mixture of codeine and opium. It describes an incidental or adverse event, not a therapeutic effect. Codeine's opioid activity offers no plausible disease-modifying role in nasal cavity pathology.

Other predictions in the model output were also reviewed:
- **Acute laryngopharyngitis** (score 99.92%): prediction only, with no trials or literature. It probably reflects the original pharyngitis and common cold indications.
- **Trigeminal autonomic cephalalgia** (score 99.43%): opioids are generally not recommended for cluster headache because of limited efficacy, risk of medication-overuse headache and dependence.
- **Allergic urticaria** (score 99.37%): the literature shows codeine as a *cause* of urticaria, since it directly triggers mast cell histamine release and is used as a positive control in skin tests. This is a safety signal, not a therapeutic one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A young man with unilateral nasal obstruction had a rhinolith formed around an impacted foreign body, which proved to be a hardened codeine and opium mixture. This is an adverse or incidental event, not evidence of benefit. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0115 | Codeine (cancelled) | Not specified | Not specified |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The model's knowledge graph lists contraindication links to the following conditions:
  - Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease
  - Liver and kidney: liver failure, liver disease, kidney disease
  - Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, psychotic disorders, schizoaffective disorder
  - Metabolic and endocrine: porphyria, hypothyroidism and myxedema
  - Gastrointestinal: pancreatitis, gallbladder disease, peptic ulcer disease, inflammatory bowel disease, gastritis
  - Other: thrombocytopenia, dermatitis herpetiformis

- **Drug Interactions:** The interaction query returned 100 records. Of the 20 shown, two are rated Major (**alvimopan** and **bupropion**). The rest are rated Moderate and include anticholinergics (atropine, glycopyrronium, hyoscyamine, dicyclomine, clidinium), antidiarrheals (loperamide, kaolin, attapulgite), cimetidine, dexamethasone, and 5-HT3 antagonists (granisetron, dolasetron).

- **Urticaria concern:** Codeine directly releases histamine from mast cells and can cause urticarial reactions, so use in allergic skin conditions is a safety concern.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The high TxGNN score is not supported by any clinical trial or relevant therapeutic literature. The only publication is a case report of an adverse event, and the prediction largely overlaps with existing rhinitis indications.
- The Philippines registration is cancelled, and no label safety information is available.

**To proceed, the following is needed:**
- Label warnings and contraindications from the DOH-FDA Philippines package insert (this is a blocking gap)
- Mechanism of action data from DrugBank
- Evidence of a true therapeutic effect in nasal cavity disease, such as controlled studies, beyond overlap with existing rhinitis symptom-relief uses
- A clear definition of which nasal cavity conditions are meant and which route of administration would apply
- A risk assessment covering opioid dependence, respiratory depression, the interaction profile and the disease associations above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

