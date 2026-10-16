---
layout: default
title: Tolvaptan
parent: Model Prediction Only (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tolvaptan: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Inappropriate ADH syndrome"
---

# Tolvaptan
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

# Tolvaptan: From Inappropriate ADH Syndrome to Polycystic Kidney Disease 3 (With or Without Polycystic Liver Disease)

## One-Sentence Summary

Tolvaptan is a vasopressin V2 receptor antagonist, originally listed for inappropriate ADH syndrome (SIADH), nephrogenic syndrome of inappropriate antidiuresis and polycystic kidney disease.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**.
There are **no registered clinical trials** for this exact subtype, but **19 publications** (including two pivotal RCT reports, TEMPO 3:4 and REPRISE) support the closely related ADPKD setting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inappropriate ADH syndrome; nephrogenic syndrome of inappropriate antidiuresis; polycystic kidney disease (the Philippines licence record has no indication text) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on the TEMPO 3:4 and REPRISE RCT reports in ADPKD; not specific to PKD3) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, tolvaptan is a selective vasopressin V2 receptor antagonist. In polycystic kidney disease, raised cAMP signalling in collecting duct cells drives cyst growth and fluid secretion. Blocking the V2 receptor lowers cAMP and may slow cyst expansion.

The listed original indication already includes polycystic kidney disease, so this is closer to on-label or near-label use than true repurposing. That is consistent with the very high prediction score.

One important caveat: the PKD3 subtype (GANAB-related) has not been specifically tested. The evidence comes from ADPKD (PKD1/PKD2) trials, and extending it to PKD3 is an assumption.

## Clinical Trial Evidence

Currently no related clinical trials registered. The pivotal trials (TEMPO 3:4 and REPRISE) appear only through the publications below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (TEMPO 3:4) | N Engl J Med | Tolvaptan in ADPKD; V2 antagonists inhibit cyst growth and slow decline in kidney function in preclinical studies |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (REPRISE) | N Engl J Med | Tolvaptan in later-stage ADPKD; earlier trial showed slower kidney volume growth and eGFR decline but more liver enzyme elevations |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for preventing ADPKD progression |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD overview: the most common inherited kidney disorder, 5–10% of kidney failure in the US and Europe |
| [41771281](https://pubmed.ncbi.nlm.nih.gov/41771281/) | 2026 | Review | Lancet | Strong evidence base for tolvaptan as disease-modifying treatment, supporting early use in high-risk patients |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic kidney/liver disease; tolvaptan can slow renal function decline in ADPKD |
| [40844441](https://pubmed.ncbi.nlm.nih.gov/40844441/) | 2025 | Review (core curriculum) | Am J Kidney Dis | Risk stratification identifies patients for whom disease-modifying therapy is recommended |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Tolvaptan remains the only FDA-approved therapy targeting disease progression; new therapies emerging |
| [32392574](https://pubmed.ncbi.nlm.nih.gov/32392574/) | 2021 | Review | Pediatr Res | Tolvaptan use in adolescents and young adults with rapidly progressing ADPKD |
| [33376103](https://pubmed.ncbi.nlm.nih.gov/33376103/) | 2020 | Commentary | Clin J Am Soc Nephrol | Long-term safety of tolvaptan in ADPKD |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0492 | Tolvaptan | Not specified | Not specified (status: cancelled) |

The only registration on record is cancelled, and no currently valid licence was found. This may reflect a specific product or formulation rather than overall availability.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver failure, cirrhosis of liver, substance abuse/dependence, active peptic ulcer disease, demyelinating disease.
- **Hepatotoxicity**: the ADPKD trials reported more aminotransferase and bilirubin elevations, so liver monitoring is needed.
- **Aquaresis-related adverse effects** are expected given the mechanism.
- **Drug Interactions**: 100 interactions were found. Examples from the first 20 listed:
  - **Major**: clarithromycin.
  - **Moderate**: aprepitant, dexamethasone, empagliflozin, loperamide, miconazole, naltrexone, rifaximin, rolapitant, and potassium salts (citrate, bicarbonate, chloride, gluconate).
  - **Minor**: fidaxomicin, naloxegol, prucalopride.

Package insert warnings were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two pivotal RCT reports and multiple reviews support tolvaptan in ADPKD, and polycystic kidney disease is already among its listed indications. However, the specific PKD3 subtype is untested, and the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism-of-action data (e.g. from DrugBank)
- Evidence specific to PKD3 (GANAB-related) disease, or a justification for extrapolating from ADPKD
- A liver monitoring plan and a review of high-risk drug interactions (especially strong CYP3A inhibitors such as clarithromycin)
- Clarification of why the Philippines registration was cancelled and whether a valid product can be sourced

---

**Other predicted indications (for reference):** The remaining nine predictions are all rated Hold.
- **Thoracic malformation** (L4): only a neonatal case report where the effect reflects fluid management, not the malformation itself.
- **Joubert syndrome with renal defect** (L5): the only article is a genetics review with no tolvaptan data. Polyuria from concentrating defects may be worsened by aquaretic therapy.
- **Renal-hepatic-pancreatic dysplasia, karyomegalic interstitial nephritis, adult familial nephronophthisis-spastic quadriparesia syndrome, Dandy-Walker-associated syndromes, and the odontal/periodontal malformation syndrome** (all L5): prediction only, with no evidence retrieved.
- **Ambras-type hypertrichosis universalis congenita and hypertrichosis** (both L5): no plausible mechanism, and the scores are likely graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

