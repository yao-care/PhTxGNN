---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrheal disease, dysentery"
---

# Loperamide
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

# Loperamide: From Diarrheal Disease to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is an anti-diarrheal drug, originally used for diarrheal disease and dysentery.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**,
but there are **0 clinical trials** and **0 publications** supporting this prediction. The high score is most likely a computational artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dysentery |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Loperamide is a peripheral mu-opioid receptor agonist. It acts on the myenteric neurons of the gut to reduce motility. Detailed mechanism of action data is not otherwise available in the data compiled for this report.

No plausible mechanistic link was identified between this gut-acting mechanism and infectious conjunctivitis. Ocular exposure and relevance to the eye are unsupported. The high TxGNN score is most likely a graph-based artifact, probably driven by shared ontology neighbors among conjunctivitis-related terms.

The same pattern appears in the other top-ranked predictions, which are mostly conjunctivitis variants (conjunctivitis, pseudomembranous conjunctivitis, serous conjunctivitis except viral, conjunctival folliculosis, chronic follicular conjunctivitis, parasitic conjunctivitis and Angelucci syndrome). None has clinical or mechanistic support. For amebic dysentery and gastroduodenitis, the only available literature points to safety concerns rather than efficacy (see Literature Evidence).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (acute contagious conjunctivitis). The table below lists publications found for other high-ranking predictions, for context only. Both are safety signals rather than efficacy evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case Report | Journal of Travel Medicine | Fulminant amoebic colitis (toxic megacolon) in a patient with heavy loperamide use. Anti-motility agents may worsen invasive infectious diarrhea (amebic dysentery prediction). |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case Report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related GI inflammation. Inflamed mucosa may increase systemic absorption and central opioid effects (gastroduodenitis prediction). |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | The American Journal of Medicine | Review of non-fluid therapy and chemoprophylaxis for acute diarrhea. Not related to the predicted ocular indication (amebic dysentery prediction). |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0293 | Loperamide | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrheal disease, infectious diarrheal disease, intestinal infectious disease.
- **Drug Interactions**: 100 interactions were found. Examples of Major interactions: abiraterone, ranitidine, fosamprenavir, gemfibrozil. Examples of Moderate interactions: codeine, dihydrocodeine, tramadol, chlorpheniramine, cetirizine, salbutamol, ethanol, galantamine, alfuzosin.
- **Safety signals from the literature**: toxic megacolon with anti-motility use in invasive infection, and systemic opioid effects (respiratory depression) when the inflamed gut mucosa increases absorption.

Please also refer to the package insert for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials, no literature and no plausible mechanism for ocular use. The only registration in the Philippines is cancelled.

**To proceed, the following is needed:**
- A plausible mechanistic rationale for loperamide in ocular surface disease, plus preclinical data
- Detailed mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of the regulatory status, since the only registration is cancelled
- Consideration of other candidate indications or drugs with better evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

