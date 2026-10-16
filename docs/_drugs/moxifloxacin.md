---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Moxifloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (streptococcal, staphylococcal, pneumonia…"
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as pneumonia, peritonitis, conjunctivitis and plague.
The TxGNN model's top-ranked prediction is **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** supporting it, so this looks like a knowledge-graph artifact.
The only prediction with a coherent rationale is **bubonic plague**, which falls within the drug's existing indication family and is supported by **4 preclinical studies** (plus 1 unrelated adverse-event case report).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal, pneumonia, peritonitis, conjunctivitis, plague, among others) |
| Predicted New Indication | Hyperamylasemia (rank 1) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

Note: the registration record in the data compiled for this report contains no approved-indication text, so the original indication above is taken from the drug's knowledge-graph indication list.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, moxifloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is established.

**For the top prediction, hyperamylasemia, no plausible mechanistic link exists.** An antibacterial has no recognized role in lowering amylase, and there are no trials or publications. The high score most likely reflects graph proximity rather than a real therapeutic signal.

The other high-scoring predictions (polyclonal hyperviscosity syndrome, blood group incompatibility, congenital analbuminemia, premalignant and congenital hematological disorders, monoclonal gammopathy, hematopoietic and lymphoid neoplasm) share the same problem. Their links are indirect, such as infection prophylaxis in immunocompromised patients, or absent altogether.

**The one coherent prediction is bubonic plague (rank 10, score 99.41%).** Moxifloxacin inhibits bacterial DNA gyrase and topoisomerase IV and is active against *Yersinia pestis* in vitro and in animals. Plague and pneumonic plague are already among its original indications, so this is an extension within an existing indication family rather than true repurposing.

Because the sections below follow the rank 1 prediction, they show no trials or literature. The bubonic plague evidence is summarized in the Literature Evidence section as a point of reference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia.

For reference, the lower-ranked predictions include trials in which moxifloxacin was used only for supportive care or as a comparator:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00324324](https://clinicaltrials.gov/study/NCT00324324) | Phase 3 | Terminated | 240 | Placebo-controlled antibacterial prophylaxis after allogeneic stem cell transplant (indirect relevance) |
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Moxifloxacin alone vs ciprofloxacin plus amoxicillin/clavulanic acid for fever in low-risk neutropenic cancer patients (indirect relevance) |
| [NCT07023029](https://clinicaltrials.gov/study/NCT07023029) | Phase 1 | Completed | 33 | Etavopivat cardiac repolarisation study in healthy participants; moxifloxacin is likely the QT positive control |

None of these tests moxifloxacin for a predicted new indication.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For reference, the literature for the bubonic plague prediction (rank 10) is below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Preclinical (mouse) | Antibiotiki i khimioterapiia | Y. pestis strains highly susceptible; ED50 of levofloxacin and moxifloxacin 5.5–14.0 mg/kg in infected mice |
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Preclinical (mouse) | Int J Antimicrob Agents | Moxifloxacin and gatifloxacin protected mice in systemic and pneumonic plague models, compared with ciprofloxacin |
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | Preclinical (in vitro) | Antimicrob Agents Chemother | In vitro pharmacodynamic model used to derive a moxifloxacin regimen that kills Y. pestis and prevents resistance |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | Preclinical (in vitro) | Antimicrob Agents Chemother | Comparative efficacy of candidate antibiotics against Y. pestis in an in vitro model |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case report | Ther Adv Drug Saf | Moxifloxacin-induced tinnitus in an older adult (adverse event, not efficacy) |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0332 | Moxifloxacin | Not specified | Not specified (registration status: cancelled) |

The only registration on record is cancelled, so no currently valid moxifloxacin product was identified in the Philippines.

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

**Contraindication-related conditions from the knowledge graph (not label text):**
- **Cardiac:** long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease
- **Neurological and neuromuscular:** epilepsy, myasthenia gravis, neuromuscular junction disease, peripheral neuropathy
- **Musculoskeletal:** tendinitis, periarthritis, exostosis
- **Hepatic:** cirrhosis of liver, drug-induced liver injury
- **Gastrointestinal:** *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- **Metabolic:** potassium deficiency disease

**Drug interactions:** 100 interactions were found. The main **Major**-level ones among those listed are:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Bupropion
- Chlorpropamide

Moderate-level interactions include antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, aspirin, and calcium- and potassium-containing products.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, hyperamylasemia, has no clinical or literature support and no plausible mechanism, so it is best treated as a computational artifact. The other high-ranking predictions are likewise unsupported or only indirectly related.
- Moxifloxacin's known safety concerns (QT prolongation, tendon and neuropathy risks, dysglycemia) argue against speculative use. Its only registration in the Philippines is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Mechanism of action data from DrugBank
- For bubonic plague, which is already within the original indication family, a review of whether the preclinical evidence is sufficient. Human data would be needed, and a market-availability check should come first.
- Confirmation of a currently valid Philippines registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

