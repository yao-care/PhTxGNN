---
layout: default
title: Ciprofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 75
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Ciprofloxacin: predicted new indication Diffuse scleroderma (evidence level L4). Approved use: Bacterial infections (typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as typhoid fever, salmonellosis, bacterial pneumonia, anthrax, and shigellosis.
The TxGNN model predicts it may be effective for **diffuse scleroderma** (its top-ranked prediction), but the data compiled for this report contain **no registered clinical trials** and only **2 publications** for this indication, neither of which provides controlled clinical confirmation.
Among the other predictions, **septicemic plague** has the strongest supporting evidence (L2) and is discussed in the closing sections.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (typhoid fever, salmonellosis, paratyphoid fever, bacterial pneumonia, anthrax, shigellosis, and others) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ciprofloxacin are not available in the data compiled for this report. Based on known information, ciprofloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is well established. Whether this activity can be applied to scleroderma is uncertain.

Two possible links to diffuse scleroderma have been proposed:

1. **Antifibrotic effect in skin.** One publication (PMID 20507401) examined ciprofloxacin as an antifibrotic agent in scleroderma skin. A topoisomerase-related effect on fibroblasts or inhibition of collagen synthesis has been suggested, but this is a hypothesis.
2. **Indirect gastrointestinal benefit.** Ciprofloxacin treats small bowel bacterial overgrowth, a common gastrointestinal complication of systemic sclerosis (PMID 7728404). This addresses a complication, not the underlying disease.

Neither link is supported by controlled clinical data here. The very high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for diffuse scleroderma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Exploratory (the abstract describes a controlled, double-blind randomized trial, but the design could not be confirmed from the available text) | The Journal of Dermatology | Evaluates whether oral ciprofloxacin reduces scleroderma severity and acts as an antifibrotic in skin; results are not available in the compiled excerpt |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Diagnostic/Observational | British Journal of Rheumatology | 24 systemic sclerosis patients with malabsorption symptoms were assessed for small bowel bacterial overgrowth and treatment outcome; indirect relevance |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0102 | Ciprofloxacin | Not specified | Not specified (status: cancelled) |

The only registration found is cancelled, so no valid ciprofloxacin product is currently authorized in the data compiled for this report.

---

## Safety Considerations

- **Contraindications / diseases of concern (from knowledge-graph associations, not label text)**: long QT syndrome (including familial), torsades de pointes, epilepsy, kidney disease, potassium deficiency, tendinitis and other tendon or joint conditions (Achilles bursitis, periarthritis, heel spur, exostosis), peripheral neuropathy and peripheral nervous system disease, *Clostridium difficile* colitis, necrotizing enterocolitis, myasthenia gravis and other neuromuscular junction disease, and superinfection.
- **Drug Interactions**: 100 interactions were found. Examples of **Major** interactions include the corticosteroids hydrocortisone, dexamethasone, betamethasone, and triamcinolone, and bupropion. Many **Moderate** interactions were also listed, including antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide), famotidine, loperamide, alosetron, aprepitant, acetylsalicylic acid, and others.

Please also refer to the package insert for complete safety information. Of particular note for scleroderma patients, who are often treated with corticosteroids, is the Major interaction with this drug class (see above).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For diffuse scleroderma, evidence is limited to two publications without confirmed controlled results (L4), and the high TxGNN score is a prediction only. In addition, the only Philippine registration is cancelled.

**Other predicted indications:**
- **Septicemic plague** is the most strongly supported prediction (L2, Proceed with Guardrails). It is a direct extension of ciprofloxacin's antibacterial activity against *Yersinia pestis*. Supporting data include a randomized trial in bubonic plague (PMID 40768716), a non-inferiority trial (PMIDs 32807214, 38970065), non-human primate data (PMID 32435805), and biodefense guidelines (PMID 15677847). The trials target bubonic rather than septicemic plague, so extrapolation is needed. This is an extension within the anti-infective class rather than true repurposing, and no trials are registered for this indication in the compiled data.
- **Monoclonal gammopathy**: the evidence concerns infection prophylaxis in myeloma and transplant patients, not treatment of the gammopathy itself (L4, Hold). The one registered trial (NCT00062231, terminated) studied febrile neutropenia.
- **Hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, punctate epithelial keratoconjunctivitis**: no plausible mechanism or supporting evidence (L5, Hold). These are likely knowledge-graph artifacts.
- **Hematological disease associated with acquired peripheral neuropathy**: no supporting evidence (L5, Hold). Fluoroquinolones carry a recognized neuropathy risk, so this prediction is a safety concern rather than a therapeutic rationale.

**To proceed, the following is needed:**
- Full results of the controlled trial in PMID 20507401 and any confirmatory randomized trials in scleroderma
- Detailed mechanism of action data
- Package insert warnings and contraindications (not available in the compiled data)
- Clarification of the Philippine regulatory status, since the sole registration is cancelled
- For septicemic plague, evidence specific to the septicemic form and confirmation of local availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

