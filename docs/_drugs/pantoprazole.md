---
layout: default
title: Pantoprazole
parent: High Evidence (L1-L2)
nav_order: 272
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-15
description: "Pantoprazole: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction"]
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **6** 
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

# Pantoprazole: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease, esophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **1 directly relevant clinical trial** and **20 publications** listed for this top prediction.
This is effectively a confirmation of an already established use rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, Zollinger-Ellison syndrome (the Philippine registration record has no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Published literature describes pantoprazole as a proton pump inhibitor that irreversibly binds the gastric H+/K+ ATPase in parietal cells. This blocks the final step of acid secretion, lowers gastric acid and allows ulcers to heal.

Active peptic ulcer disease is closely related to the drug's original indications, since all are acid-driven conditions. The prediction therefore matches pantoprazole's core pharmacology. The very high score is consistent with this overlap.

Other predicted indications are weaker:
- **Gastrojejunal (marginal) ulcer** and **peptic ulcer perforation**: mechanistically plausible, but there are no registered trials. Acid suppression is an adjunct, not a treatment of the perforation itself.
- **Duodenogastric reflux**: evidence is limited to small physiological and observational studies.
- **Duodenal obstruction**: no clear mechanistic link. The high score likely reflects graph proximity to duodenal ulcer.
- **Duodenal ulcer**: well supported by Phase 3 trials and RCTs, and again an on-label confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomized, double-blind comparison of ilaprazole vs pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients |

For the related indication of duodenal ulcer, further trials were identified (for example, [NCT00374101](https://clinicaltrials.gov/study/NCT00374101), Phase 3, n=450, PPI after endoscopic therapy for bleeding peptic ulcers, and [NCT00843063](https://clinicaltrials.gov/study/NCT00843063), Phase 4, n=161, pantoprazole vs famotidine for preventing recurrent aspirin-induced ulcers).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review / Network Meta-analysis | Am J Gastroenterol | Compares P-CABs and PPIs for healing Los Angeles grade C/D esophagitis |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut Liver | Tegoprazan for endoscopic resection-induced artificial ulcers (active-controlled) |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole binds the proton pump irreversibly; few drug interactions reported |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Review | Med Arh | PPIs in GERD management; healing depends on intragastric pH |
| [10450061](https://pubmed.ncbi.nlm.nih.gov/10450061/) | 1999 | Review | Pharmacology | PPIs show similar dose-response relationships at equal milligram doses |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | Clinical study | Aliment Pharmacol Ther | Three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Review | Eur J Gastroenterol Hepatol | Pantoprazole mechanism: accumulates in the parietal cell and is acid-activated |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical | Inflammopharmacology | Pantoprazole plus mesenchymal stem cells in a rat gastric ulcer model |

For the related duodenal ulcer prediction, RCTs also support efficacy, including [7569755](https://pubmed.ncbi.nlm.nih.gov/7569755/) (pantoprazole vs ranitidine in acute duodenal ulcer) and [8180294](https://pubmed.ncbi.nlm.nih.gov/8180294/) (pooled analysis showing better healing than ranitidine at 2 and 4 weeks).

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0373 | Pantoprazole | Not listed | Not listed (registration status: cancelled) |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: osteoporosis, postmenopausal osteoporosis, bone fracture, pernicious anemia.
- **Drug Interactions**: 100 interactions were found. Examples include:
  - Major: acalabrutinib, atazanavir
  - Moderate: hydrochlorothiazide, atorvastatin, fenofibrate, bosutinib, bumetanide, amphotericin B, amikacin, alpelisib, apalutamide, armodafinil, amphetamine
  - Minor: acetylsalicylic acid, cyanocobalamin, axitinib, bortezomib, brivaracetam

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Pantoprazole's efficacy in acid-related ulcer disease is supported by completed Phase 3 trials and RCTs. The prediction confirms an established use rather than a new one. The only Philippine registration is cancelled, so availability is the main practical barrier.

**To proceed, the following is needed:**
- Verify product availability and registration status in the Philippines, since the only licence is cancelled
- Obtain the package insert warnings and contraindications
- Review the 100 listed drug interactions, especially the major ones (acalabrutinib, atazanavir)
- Plan long-term safety monitoring, including bone health (osteoporosis and fracture signals) and vitamin B12 status (pernicious anemia signal)
- Confirm the mechanism of action in an authoritative source such as DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

