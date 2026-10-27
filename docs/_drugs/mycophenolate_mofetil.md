---
layout: default
title: Mycophenolate Mofetil
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mycophenolate Mofetil: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not available in the Philippines registration data"
monitor_inn: "Mycophenolate mofetil"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "bone Paget disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "multiple sclerosis", "hemosiderosis", "Heiner syndrome", "African iron overload", "neonatal hemochromatosis"]
---

# Mycophenolate Mofetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Mycophenolate Mofetil: From Transplant Immunosuppression to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Mycophenolate mofetil (MMF) is an immunosuppressant drug. The data compiled for this report do not list an approved indication for it in the Philippines.
The TxGNN model predicts it may be effective for **HIV infectious disease**,
with **4 registered clinical trials** (none of which gives direct efficacy evidence) and **20 publications** currently linked to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Philippines registration data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 (per the data compiled for this report; see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* The L2 grade comes from the compiled scoring. Strictly applying the rules, no completed Phase 2/3 RCT directly tests MMF for HIV in the trials below. The one randomized study in the literature (PMID 15353978) was in treatment-naive patients and is only a small piece of supporting evidence. The practical strength of evidence is therefore lower than L2 suggests.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on the repurposing analysis, MMF inhibits inosine monophosphate dehydrogenase (IMPDH), which depletes guanosine nucleotide pools. This has two possible effects relevant to HIV:

- It reduces lymphocyte proliferation, which limits the pool of activated cells that HIV uses to replicate.
- It can strengthen nucleoside analogues such as abacavir and didanosine by shifting intracellular nucleotide ratios.

Small clinical studies support this biological plausibility. One case series (PMID 12352149) showed depletion of intracellular dGTP and a fall in plasma HIV-1 RNA when MMF was added to an abacavir-containing regimen. However, efficacy as an antiviral or reservoir-targeting agent is **not established**. MMF is also immunosuppressive, which raises infection-risk concerns in people with HIV.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Placebo-controlled pilot of DAPD vs DAPD plus MMF added to anti-HIV regimens in treatment-experienced patients; the main study drug is a different agent |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Safety and antiretroviral activity of MMF added to abacavir; withdrawn, so no data |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine and MMF for anti-erythropoietin-associated pure red cell aplasia; not an HIV study |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Stem cell transplant in HIV-positive patients with MMF as part of post-transplant immunosuppression; no direct evidence of antiviral efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | HAART with or without MMF in treatment-naive HIV-1 patients; effect on viral RNA decay and the latent cellular reservoir |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD study | Clin Pharmacokinet | Pharmacokinetics of low-dose MMF in HIV patients on abacavir, efavirenz and nelfinavir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Clinical short communication | AIDS Res Hum Retroviruses | No detrimental immunological effects of MMF plus HAART in treatment-naive patients |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Case series | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing therapy was linked to dGTP depletion and a drop in HIV-1 RNA in 5 patients |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Immunosuppressive drugs in HIV disease, targeting immune activation |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | Virostatics as a way of targeting HIV infection |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | Retrospective study | Am J Transplant | Kidney transplantation in 27 HIV-infected patients using MMF-based immunosuppression |
| [39396546](https://pubmed.ncbi.nlm.nih.gov/39396546/) | 2025 | Case report | Trop Doctor | Complete renal response of IgA vasculitis to steroid plus MMF in an HIV patient |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0334 | Mycophenolate Mofetil | Not stated | Not stated (status: cancelled) |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, active peptic ulcer disease, neutropenia, agranulocytosis, aplastic anaemia and related marrow failure syndromes (e.g., Fanconi anaemia, Diamond-Blackfan anaemia), cancer including lymphoma and skin cancer, and infections such as cytomegalovirus, herpes simplex, herpes zoster and progressive multifocal leukoencephalopathy. The infection-related signals are particularly relevant for people with HIV.
- **Drug interactions:** 92 interactions were found. Examples include:
  - **Major:** activated charcoal.
  - **Moderate:** proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, rabeprazole, dexlansoprazole), antibiotics (amoxicillin, clarithromycin, doxycycline, minocycline, tetracycline, vancomycin, kanamycin, paromomycin), and antacids or minerals (aluminium hydroxide, calcium carbonate, magnesium oxide).
  - **Minor:** zinc salts and iron.

Please refer to the package insert for warnings and formal contraindications.

## Other Predicted Indications (Context)

For comparison, the other top predictions are weaker or have different support:
- **Multiple sclerosis** (score 99.54%): several small Phase 2 trials and a Cochrane review exist, but there are no robust Phase 3 data. This is the better-supported of the candidates.
- **Pulmonary hemosiderosis:** only reviews and case-level reports.
- **All others** (neurodevelopmental disorder, Paget disease, feline and simian immunodeficiency, Heiner syndrome, African iron overload, neonatal hemochromatosis): prediction only, no clinical or literature support.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale for HIV is plausible, and a few small studies exist. However, no trial directly shows MMF efficacy in HIV: the relevant trial was withdrawn, and the others are indirect. MMF's immunosuppression also raises infection-risk concerns in this population. In the Philippines, the only registration is cancelled, and the package insert data are unavailable, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Philippines package insert warnings and contraindications
- Detailed mechanism of action data (MOA)
- A clear original indication from the Philippines registration
- A well-designed clinical study of MMF for HIV, including safety monitoring for opportunistic infections
- Review of whether multiple sclerosis, which has more clinical support, should be prioritised over HIV
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

