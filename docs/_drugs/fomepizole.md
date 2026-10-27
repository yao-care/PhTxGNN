---
layout: default
title: Fomepizole
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Fomepizole: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not listed in the Philippines registration record"
monitor_inn: "Fomepizole"
predicted_indications: ["sclerosing cholangitis"]
---

# Fomepizole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fomepizole: From Toxic Alcohol Poisoning to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Fomepizole is an alcohol dehydrogenase inhibitor, generally known as an antidote for ethylene glycol and methanol poisoning. The local registration record in the data compiled for this report does not list an approved indication.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Philippines registration record |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fomepizole inhibits alcohol dehydrogenase, which blocks conversion of toxic alcohols into their harmful metabolites. Its use in poisoning is established, but this has not been linked in the available data to any bile duct disease.

A speculative link could involve alcohol dehydrogenase-related oxidative stress, or aldehyde and bile acid metabolism in the cells lining the bile ducts. This is a hypothesis only, and nothing in the data supports it.

The high score (0.993) may reflect connections in the knowledge graph, such as shared alcohol-metabolism or liver-related genes and pathways, rather than a validated biological relationship. The prediction should be treated as a research lead, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0205 | Fomepizole | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: Ethanol, rated **Major** (source: DDInter). Fomepizole and ethanol both act on alcohol dehydrogenase, so combined use needs careful clinical consideration.
- **Disease-related cautions from the knowledge graph**: The TxGNN knowledge graph links fomepizole to contraindication edges for kidney disease, pyoureter, liver disease and gallbladder disease. These come from graph relationships, not from label text, and need verification. Liver and gallbladder disease are especially relevant to a bile duct indication.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no clinical trials or publications, no mechanism data, and no currently valid Philippines registration. The knowledge graph also flags liver and gallbladder disease as contraindications, which conflicts with a hepatobiliary use.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) and a plausible biological link to sclerosing cholangitis
- A literature and trial search, including preclinical studies, for fomepizole in cholestatic or bile duct disease
- The Philippines package insert, to confirm warnings, contraindications and the original indication
- Clarification of the cancelled registration status and the available dosage forms and routes
- A safety review of the knowledge-graph contraindications (liver and gallbladder disease) and the major ethanol interaction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

