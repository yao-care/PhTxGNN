---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic originally used for bacterial infections (streptococcal and staphylococcal infections, anaerobic infections, aspiration pneumonia), acne, and vaginal conditions such as bacterial vaginosis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 clinical trials** and **0 publications** for this specific indication, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis, aspiration pneumonia (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Clindamycin is generally known as a lincosamide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in skin, soft tissue, anaerobic, and vaginal bacterial infections is established, so any benefit in a new indication would depend on a bacterial cause.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is commonly viral, toxic, or dry-eye related, so an antibacterial mechanism is a poor fit. Clindamycin is also not a standard topical ophthalmic agent. The high score (0.9997) is most likely a graph-based similarity signal rather than a mechanistic finding.

Other predictions in the same list show similar limits. Exposure keratitis has only indirect evidence, from papers on bacterial keratitis and ocular *S. aureus* infection, where clindamycin could at most address secondary infection. Epidemic keratoconjunctivitis is viral (adenovirus). Postmenopausal atrophic vaginitis is caused by estrogen deficiency. Neurotrophic keratopathy is a nerve and epithelial-healing disorder.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For context, the second-ranked prediction, exposure keratitis, has indirect literature only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective case review | PLoS One | Characteristics, antibiotic susceptibility, and outcomes of *S. aureus* keratitis, comparing MRSA and MSSA |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features, and antibiotic susceptibility of ocular MRSA vs MSSA infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis linked to a contaminated lens case |

None of these studies examines clindamycin treatment of exposure keratitis directly.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0105 | Clindamycin | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so there is currently no valid marketed clindamycin product under this record.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver failure, sunburn, Crohn disease, inflammatory bowel disease, Crohn's colitis, ulcerative colitis, atopic eczema/dermatitis, exfoliative dermatitis, diarrheal disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and vulvovaginal candidiasis.
- **Drug Interactions** (100 interactions recorded; main ones shown):
  - Moderate: balsalazide, clarithromycin, picosulfuric acid, attapulgite, kaolin.
  - Unclassified severity: amphotericin B, acetylsalicylic acid, amoxicillin, bupropion, pantoprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, omeprazole, sucralfate, rosiglitazone, lansoprazole, vancomycin.
- **Class-related concern**: Clindamycin is a recognized risk factor for *C. difficile* infection. The veterinary epidemiology papers retrieved for the "non-human animal disease" prediction point to this safety concern rather than to a therapeutic benefit.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no literature, and the antibacterial mechanism does not match the likely causes of punctate epithelial keratoconjunctivitis (viral, toxic, dry-eye). The only Philippines registration is cancelled, and clindamycin is not a standard ophthalmic agent.

**To proceed, the following is needed:**
- Evidence that a bacterial cause plays a meaningful role in the target condition
- Mechanism of action data and a clear mechanistic link to the new indication
- Route and formulation assessment (an ophthalmic preparation would be required)
- Package insert warnings and contraindications from the Philippines regulator
- Re-evaluation of the registration situation, since no valid license currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

