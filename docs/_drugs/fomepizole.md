---
layout: default
title: Fomepizole
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 1
---

# Fomepizole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fomepizole: From Methanol/Ethylene Glycol Poisoning Antidote to Sclerosing Cholangitis

## One-Sentence Summary

Fomepizole is an alcohol dehydrogenase (ADH) competitive inhibitor, primarily used as an antidote for methanol and ethylene glycol poisoning. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but currently there are **no clinical trials** and **no publications** supporting this direction — the evidence relies entirely on computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methanol/Ethylene glycol poisoning antidote (no Philippines-registered indication) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fomepizole is a competitive inhibitor of alcohol dehydrogenase (ADH), and it also exhibits inhibitory activity against CYP2E1 and JNK pathways. By blocking ADH, Fomepizole prevents the conversion of methanol and ethylene glycol into their toxic metabolites (formic acid and glycolic acid/oxalic acid, respectively). In theory, ADH/CYP2E1 inhibition could reduce acetaldehyde production and oxidative stress, and oxidative stress has been implicated indirectly in bile duct injury.

However, the mechanistic link between Fomepizole and sclerosing cholangitis is **extremely weak and speculative**. Primary sclerosing cholangitis (PSC) is fundamentally an immune-mediated disease — its primary pathological drivers are autoimmune inflammation and progressive bile duct fibrosis, not alcohol metabolism or toxic metabolite accumulation. Current PSC drug development targets focus on bile acid pathways (e.g., FXR agonists), antifibrotic agents, and immune modulators, none of which involve the ADH pathway.

In summary, while the TxGNN model assigns a high computational score, the biological rationale connecting an ADH inhibitor to an immune-mediated cholangiopathy remains speculative with no established mechanistic basis. This prediction should be treated with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

> Searches were conducted on ClinicalTrials.gov and WHO ICTRP (query date: 2026-03-09) with no results found for the combination of Fomepizole and sclerosing cholangitis.

## Literature Evidence

Currently no related literature available.

> A PubMed search (query date: 2026-03-09) returned no publications linking Fomepizole to sclerosing cholangitis.

## Philippines Market Information

Fomepizole is currently **not registered** in the Philippines. There are no active marketing authorizations on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registrations found |

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are currently unavailable in this evidence pack and require retrieval from the TFDA official website or DrugBank API.

**Data gaps identified:**
- TFDA package insert warnings/contraindications (Blocking severity — required for Stage 1 safety assessment)
- Mechanism of action details (High severity — impacts mechanistic relevance analysis)
- No drug-drug interactions found in current database queries

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high computational score (99.28%), but this prediction has **zero external validation** — no clinical trials, no literature, and no established mechanistic rationale. Sclerosing cholangitis is an immune-mediated biliary disease with no known connection to alcohol dehydrogenase inhibition. Additionally, Fomepizole is not marketed in the Philippines, which poses regulatory and supply chain barriers. The evidence level is L5 (model prediction only), which is insufficient to justify advancing this candidate.

**To proceed, the following is needed:**
- Preclinical studies demonstrating Fomepizole's effect on bile duct inflammation or fibrosis models
- Mechanistic studies exploring whether ADH/CYP2E1/JNK inhibition has any relevance to PSC pathophysiology
- Complete safety profile retrieval (package insert warnings, contraindications)
- Assessment of regulatory pathway for introducing an unregistered drug for a new indication in the Philippines
- At minimum, observational or case-report evidence before this candidate warrants further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

