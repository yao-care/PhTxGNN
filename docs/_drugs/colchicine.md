---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 87
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "familial Mediterranean fever, autosomal dominant", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Colchicine: From Gout to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine was originally used to treat gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but there are **0 clinical trials** and only **2 preclinical publications** (neither shows colchicine efficacy against malaria), so this prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (the Philippines registration record has no approved indication text) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, colchicine is a microtubule polymerization inhibitor. Its anti-inflammatory effect is attributed to blocking neutrophil microtubule-dependent functions and inflammasome activation, which is why it works in gout and FMF.

The mechanistic link to malaria is theoretical: *P. falciparum* depends on tubulin and microtubules for division and morphology, so a microtubule-targeting drug could plausibly affect the parasite. However, the two retrieved papers do not test this. One studies curcumin, not colchicine, disrupting parasite microtubules. The other studies pfmdr1 expression in mammalian cells in the context of chloroquine susceptibility, which concerns drug resistance and transport, not therapeutic efficacy.

Colchicine also has a narrow therapeutic index and significant human toxicity, which argues against its use as an antimalarial. The high TxGNN score is a computational prediction only.

**Other predictions in the data (for context):**
- **Familial Mediterranean fever, autosomal dominant (score 99.38%, L4):** Colchicine is already the standard first-line FMF therapy, so this is a subtype or naming variant of an existing indication rather than true repurposing. Supporting literature is mostly reviews.
- **Dermatofibrosarcoma protuberans (score 99.37%, L5):** There is no clinical or literature support. The disease is driven by the COL1A1-PDGFB fusion and treated with surgery and imatinib, and colchicine's toxicity at antimitotic doses limits plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Preclinical in vitro | PLoS One | Curcumin (not colchicine) disrupts *P. falciparum* microtubules; shows parasite microtubules are druggable targets |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Preclinical in vitro | Mol Cell Biol | Expression of the plasmodial pfmdr1 gene in mammalian cells is linked to increased chloroquine susceptibility; relates to transporter and resistance, not colchicine efficacy |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0116 | Colchicine (status: cancelled) | Not specified | Not specified |

## Safety Considerations

- **Contraindication signals (from the knowledge graph, not label text):** liver failure, impaired renal function, hematologic disease (thrombocytopenia, leukopenia, agranulocytosis, neutropenia, aplastic anemia and congenital neutropenia syndromes), peptic ulcer disease, diarrheal disease, myopathy and rhabdomyolysis, and acute urate nephropathy.
- **Drug Interactions:** 100 interactions were found. Major-level interactions among those listed include aprepitant, clarithromycin, cobicistat, deferiprone, eliglustat, rolapitant, rosuvastatin and simvastatin. Moderate-level examples include chloroquine, cimetidine, metronidazole, ticagrelor, deferasirox and disulfiram. The chloroquine interaction is notable given the malaria context.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no direct evidence of colchicine activity against *P. falciparum*. Colchicine's narrow therapeutic index and toxicity, plus its cancelled registration in the Philippines, make it an unlikely antimalarial candidate despite the high model score.

**To proceed, the following is needed:**
- In vitro and in vivo data showing colchicine's antiplasmodial activity at clinically achievable, tolerable doses
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Philippine regulator
- A safety and therapeutic-index assessment against existing antimalarials
- Clarification of the cancelled registration status if any use in the Philippines is contemplated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

