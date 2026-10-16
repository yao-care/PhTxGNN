---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Terazosin: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension"
monitor_inn: "Terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
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

# Terazosin: From Hypertension and Benign Prostatic Hyperplasia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker, originally used to treat hypertension and benign prostatic hyperplasia (BPH).
The TxGNN model ranks **hypotrichosis simplex of the scalp** as its top prediction, but there are **0 clinical trials** and **0 publications** supporting it.
The more credible repurposing signals in the data are for **Raynaud disease** and **migraine disorder**, which each have a small number of older publications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; benign prostatic hyperplasia (from the knowledge graph, as the Philippines registration has no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, terazosin is an alpha-1 adrenergic blocker. Its efficacy in hypertension and BPH is established, and it works by relaxing vascular and prostatic smooth muscle.

For the top-ranked prediction, hypotrichosis simplex of the scalp, the link is speculative. A hair-growth effect through alpha-1 blockade or vasodilation is conceivable, but nothing in the data supports it. This is a rare hereditary condition, and the high score most likely reflects the model's proximity to other hair-loss terms in the knowledge graph rather than a real pharmacological signal. The same applies to the other hair-related predictions (congenital hypotrichosis milia, diffuse alopecia areata, Ambras-type hypertrichosis) and to manic bipolar affective disorder and kyphoscoliotic heart disease. All of these are prediction-only.

Two predictions have a more plausible biological rationale and some published support:
- **Raynaud disease** (score 99.83%): Alpha-1 blockade reduces sympathetic vasoconstriction in digital vessels. A 1997 publication reports fewer and milder vasospastic attacks with terazosin.
- **Migraine disorder** (score 99.92%): Older reports suggest alpha-1 blockers may help prevent migraine through effects on adrenergic and vascular tone.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction or for any of the other nine predictions.

---

## Literature Evidence

Currently no related literature is available for the top-ranked prediction (hypotrichosis simplex of the scalp). The table below lists the publications found for other predicted indications.

| PMID | Year | Type | Journal | Predicted Indication | Key Findings |
|------|-----|------|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical study (design unverified) | Minerva Cardioangiologica | Raynaud disease | In patients with idiopathic and secondary Raynaud's phenomenon, terazosin reduced the number, intensity and duration of vasospastic attacks, with improved thermographic and ultrasound findings. |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Open clinical study | La Clinica Terapeutica | Migraine disorder | Open trial in 46 patients with migraine without aura. Terazosin was given to 10 patients, buflomedil to 29, and both to 7, to assess prophylaxis. It is small, early-stage and dated. |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review / case series | Headache | Migraine disorder | In 10 neurology-practice patients on terazosin or doxazosin, migraine frequency or severity decreased in all but 1. Five patients stopped the drug because of side effects. |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Current Cardiology Reviews | Alopecia | General review of extracardiac effects of cardiovascular drugs, with minoxidil as the hair-growth example. Its specific claims about terazosin could not be verified, so this is indirect evidence. |

The 1994 migraine paper concerns migraine without aura, so it does not match the "migraine with brainstem aura" subtype.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0476 | Terazosin | Not specified | Not specified (status: cancelled) |

Terazosin has no currently valid registration in the Philippines, so any new use would require a new registration or a variation of the existing one.

---

## Safety Considerations

- **Contraindications / disease associations (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, priapism, intraoperative floppy iris syndrome.
- **Drug Interactions**: The interaction query found 100 potential interactions. Most of those listed are of Moderate severity. Examples include corticosteroids (hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone, prednisolone), opioids (morphine, opium), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), cannabinoids (dronabinol, nabilone), and bupropion. A few (calcitriol, pantoprazole, glimepiride) have an unknown severity level.

Please refer to the package insert for warnings and label contraindications, as these are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypotrichosis simplex of the scalp, is supported only by the model score, with no trials or literature, so the evidence level is L5. The registration in the Philippines is cancelled, and the package-insert safety data is missing. Raynaud disease and migraine disorder have limited, dated, small-scale publications (evidence level L3, flagged as research questions) and could be considered for follow-up, but they are not sufficient to proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippine FDA
- Detailed mechanism-of-action data
- For Raynaud disease or migraine: a systematic literature review and, if justified, a controlled study, compared against established alternatives such as calcium channel blockers
- Clarification of the Philippines registration status (cancelled) and the dosage form
- Rationale or biological validation for the hair-related predictions before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

