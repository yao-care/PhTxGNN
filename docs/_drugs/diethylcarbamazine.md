---
layout: default
title: Diethylcarbamazine
parent: Model Prediction Only (L5)
nav_order: 107
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Diethylcarbamazine: predicted new indication Syndromic lymphedema (evidence level L5). Approved use: Filariasis and related conditions (elephantiasis, lymphedema, loiasis…"
monitor_inn: "Diethylcarbamazine"
predicted_indications: ["syndromic lymphedema", "primary lymphedema"]
---

# Diethylcarbamazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Diethylcarbamazine: From Filarial Lymphatic Disease to Syndromic Lymphedema
{: .text-alpha }

## One-Sentence Summary

Diethylcarbamazine (DEC) is an established antifilarial drug, originally used for filariasis, loiasis, onchocerciasis, filarial elephantiasis and tropical pulmonary eosinophilia.
The TxGNN model predicts it may be effective for **syndromic lymphedema** (the second-ranked prediction is primary lymphedema), but there are **no registered clinical trials** and **no publications that directly address this use**. Evidence rests on the model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Filariasis and related conditions (elephantiasis, lymphedema, loiasis, onchocerciasis, pulmonary eosinophilia). The Philippines license record has no indication text, so this comes from the knowledge graph. |
| Predicted New Indication | Syndromic lymphedema |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L4 (assessed as mechanism and background literature only; no trials) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, DEC is mainly a microfilaricide. It is thought to act on the parasite's neuromuscular system and to promote immune-mediated killing of the parasites.

The link to lymphedema is indirect. DEC treats filarial infection, which can damage the lymphatic system and cause secondary lymphedema (elephantiasis). Lymphedema is already among the drug's listed original indications. Syndromic lymphedema, however, is a genetic, non-infectious condition caused by developmental defects of the lymphatic system. Nothing in the available data suggests DEC could correct such defects.

The high TxGNN score most likely reflects the knowledge-graph proximity between DEC and filarial lymphedema, rather than a true mechanistic match. The same reasoning applies to the second prediction, primary lymphedema (score 99.25%), which is also a heritable lymphatic developmental disorder. Any benefit in either condition is speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The two publications retrieved for syndromic lymphedema concern filarial disease, not syndromic lymphedema itself. The table also lists the most relevant publications retrieved for primary lymphedema, chosen by study design (all still concern filariasis). None directly tests DEC in a genetic lymphedema.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40345209](https://pubmed.ncbi.nlm.nih.gov/40345209/) | 2025 | RCT | Lancet Infect Dis | Moxidectin combinations vs ivermectin combinations for clearing *W. bancrofti* microfilaremia in lymphatic filariasis; not a DEC study |
| [40380307](https://pubmed.ncbi.nlm.nih.gov/40380307/) | 2025 | Systematic review / network meta-analysis | BMC Infect Dis | Compares antifilarial regimens including ivermectin + DEC + albendazole (IDA); notes DEC can cause severe ocular events in people with onchocerciasis |
| [17954542](https://pubmed.ncbi.nlm.nih.gov/17954542/) | 2007 | Systematic review | JAMA | Oral drug therapy for multiple neglected tropical diseases |
| [20739055](https://pubmed.ncbi.nlm.nih.gov/20739055/) | 2010 | Review | Lancet | Lymphatic filariasis and onchocerciasis; parasite death drives inflammation causing lymphoedema and elephantiasis |
| [3297557](https://pubmed.ncbi.nlm.nih.gov/3297557/) | 1987 | Review | Ciba Found Symp | DEC is mainly a microfilaricide acting on the parasite neuromuscular system and promoting immune-mediated cytotoxicity |
| [1580599](https://pubmed.ncbi.nlm.nih.gov/1580599/) | 1992 | Review | Annu Rev Med | Tropical pulmonary eosinophilia, an immune hyperresponse to filarial parasites |
| [18383658](https://pubmed.ncbi.nlm.nih.gov/18383658/) | 2008 | Review | Prescrire Int | Oral DEC is the standard antiparasitic drug for adults with lymphatic filariasis |
| [24772754](https://pubmed.ncbi.nlm.nih.gov/24772754/) | 2013 | Case report | J Assoc Physicians India | Filarial chyluria with nephrotic-range proteinuria, treated with sclerotherapy and DEC; single patient with an infectious cause |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0143 | Diethylcarbamazine | Not stated | Not stated (status: cancelled) |

---

## Safety Considerations

Please refer to the package insert for safety information.

One point from the retrieved literature: a 2025 network meta-analysis notes that DEC can cause severe adverse ocular events in people with onchocerciasis, which limits its use where onchocerciasis or loiasis is present. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction appears to be an artifact of overlap with DEC's existing filarial indications. Syndromic and primary lymphedema are genetic, non-infectious conditions, and no trials or publications support DEC for them.
- The only Philippines registration is cancelled, and no package insert warnings or contraindications are available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Mechanism of action data for DEC (for example from DrugBank), to assess any plausible link to non-infectious lymphedema
- Package insert warnings and contraindications from the Philippines FDA
- Evidence that DEC has any effect in genetic lymphedema (preclinical or clinical); none was found
- Clarification of whether the cancelled registration can be reinstated or whether supply would depend on another route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

