---
layout: default
title: Nevirapine
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Nevirapine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Nevirapine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Nevirapine
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

## Nevirapine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition,
but there are **0 clinical trials** and only **1 relevant publication** (an in vitro biochemical and structural study), so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is an NNRTI that binds allosterically to HIV-1 reverse transcriptase. Its efficacy in HIV infection is established, and the predicted indication involves a related lentivirus, feline immunodeficiency virus (FIV), which also uses a reverse transcriptase.

However, the mechanistic link is weak. FIV reverse transcriptase is generally reported to respond poorly to many NNRTIs because the NNRTI binding pocket differs structurally from that of HIV-1. The one relevant study (a 2023 biochemical and structural comparison of NNRTIs against feline and human immunodeficiency viruses) examined nevirapine, efavirenz and rilpivirine, but the information available does not allow the specific result for nevirapine to be confirmed. The high TxGNN score is a computational prediction, most likely reflecting similarity to the existing HIV indication, and it is not backed by clinical data. This is also a veterinary indication with no direct human clinical relevance.

The other top predictions show the same pattern:
- **Simian immunodeficiency virus infection** (score 0.9985, L4): the literature is preclinical and model-based. Wild-type SIV is naturally resistant to NNRTIs, and the chimeric SHIV viruses carrying HIV-1 reverse transcriptase are used only as research models. No clinical trials exist.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9982, L5): no trials, no literature, and no identifiable mechanistic link. This is a prediction-only signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | Journal of Veterinary Science | Compared the NNRTIs nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency viruses to assess their potential for treating FIV infection. The specific result for nevirapine cannot be confirmed from the available information. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0345 | Nevirapine | Not specified | Not specified (registration valid) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (derived from the TxGNN/PrimeKG drug-disease network, not from label text): liver failure, liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B virus infection, chronic hepatitis C virus infection, hepatitis C virus infection, exanthem, Stevens-Johnson syndrome, toxic epidermal necrolysis, Lyell syndrome, rhabdomyolysis, and nodular fasciitis. These signals are consistent with known nevirapine concerns about hepatotoxicity and severe skin reactions.
- **Drug Interactions**: 100 interactions were identified in total. The 20 listed in the compiled data are all rated **Moderate**, including rabeprazole, bupropion, aprepitant, clarithromycin, the corticosteroids (dexamethasone, betamethasone, budesonide, prednisolone, triamcinolone), ondansetron, granisetron, cisapride, naltrexone, saxagliptin, linagliptin, and eliglustat.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and one in vitro study. There are no clinical trials, the predicted indication is veterinary, and FIV (like SIV) is expected to respond poorly to NNRTIs. In the Philippines, the only registration is cancelled.

**To proceed, the following is needed:**
- Confirmation of the nevirapine-specific findings in the 2023 FIV study (PMID 38031646), including potency against FIV reverse transcriptase
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from DOH-FDA Philippines, which are needed before any safety screening
- A clear decision on whether a veterinary indication falls within the scope of this repurposing programme
- Clarification of the regulatory status of nevirapine in the Philippines, since the only registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

