---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 272
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Pantoprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Pantoprazole
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

## Pantoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease, esophagitis and Zollinger-Ellison syndrome.
This is effectively a confirmation of an already established use rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Published literature describes pantoprazole as a proton pump inhibitor that irreversibly binds the gastric H+/K+ ATPase in parietal cells. This blocks the final step of acid secretion, lowers gastric acid and allows ulcers to heal.

Active peptic ulcer disease is closely related to the drug's original indications, since all are acid-driven conditions. The prediction therefore matches pantoprazole's core pharmacology. The very high score is consistent with this overlap.

Other predicted indications are weaker:
- **Gastrojejunal (marginal) ulcer** and **peptic ulcer perforation**: mechanistically plausible, but there are no registered trials. Acid suppression is an adjunct, not a treatment of the perforation itself.
- **Duodenogastric reflux**: evidence is limited to small physiological and observational studies.
- **Duodenal obstruction**: no clear mechanistic link.
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
| PNF-0373 | Pantoprazole | Not listed | Not listed (registration status: valid) |

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
- Pantoprazole's efficacy in acid-related ulcer disease is supported by completed Phase 3 trials and RCTs. The prediction confirms an established use rather than a new one.

**To proceed, the following is needed:**
- Obtain the package insert warnings and contraindications
- Review the 100 listed drug interactions, especially the major ones (acalabrutinib, atazanavir)
- Plan long-term safety monitoring, including bone health (osteoporosis and fracture signals) and vitamin B12 status (pernicious anemia signal)
- Confirm the mechanism of action in an authoritative source such as DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

