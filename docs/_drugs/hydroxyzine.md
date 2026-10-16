---
layout: default
title: Hydroxyzine
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Hydroxyzine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Atopic eczema, allergic rhinitis, urticaria, angioedema…"
---

# Hydroxyzine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Hydroxyzine: From Allergic and Atopic Skin Conditions to Cold Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1 antihistamine, originally used for allergic and atopic conditions such as atopic eczema, allergic rhinitis, conjunctivitis, and urticaria.
The TxGNN model predicts it may be effective for **cold urticaria**, which has the strongest supporting evidence among the top predictions.
There are **no registered clinical trials** for this prediction, but **9 publications** were compiled, including one small 1984 randomized double-blind comparative study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema, allergic rhinitis, urticaria, angioedema, and related allergic conditions (the Philippines registration lists no indication text) |
| Predicted New Indication | Allergic urticaria (rank 1); cold urticaria is the best-supported prediction (rank 3) |
| TxGNN Prediction Score | 99.77% (allergic urticaria); 99.66% (cold urticaria) |
| Evidence Level | L4 (allergic urticaria); L3 (cold urticaria) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

**Other predictions in the top 5**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|------|
| 1 | Allergic urticaria | 99.77% | L4 | Close to an existing on-label use; literature is mostly about cetirizine |
| 2 | Rosacea conjunctivitis | 99.70% | L5 | No trials or literature |
| 3 | Cold urticaria | 99.66% | L3 | Some hydroxyzine-specific clinical data |
| 4 | Recalcitrant atopic dermatitis | 99.36% | L5 | No trials or literature |
| 5 | IgE responsiveness, atopic | 99.27% | L5 | Too nonspecific to define an endpoint |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, hydroxyzine is a first-generation H1-receptor inverse agonist. Its efficacy in allergic skin and airway conditions is established, and mechanistically it may be applicable to cold urticaria.

In cold urticaria, cold exposure triggers mast cell degranulation and histamine release, producing wheals and itching. Blocking H1 receptors is therefore mechanistically sound. This is closely related to the drug's original indications, since urticaria and angioedema are already among them.

Two caveats apply. First, allergic urticaria is close to an on-label use rather than true repurposing, and the very high TxGNN scores partly reflect existing disease associations. Second, modern guidelines favor second-generation antihistamines because first-generation agents cause sedation and anticholinergic burden.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 5 predictions.

---

## Literature Evidence

The table covers the cold urticaria prediction, the best-supported one.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | Randomized double-blind comparative study | J Am Acad Dermatol | Compared cinnarizine, cyproheptadine, doxepin, and hydroxyzine in idiopathic cold urticaria; doxepin was preferred in the trials, and hydroxyzine was one of the comparators |
| [11702618](https://pubmed.ncbi.nlm.nih.gov/11702618/) | 2001 | Evidence-based review | Am J Clin Dermatol | Antihistamines remain the mainstay of urticaria treatment |
| [32975301](https://pubmed.ncbi.nlm.nih.gov/32975301/) | 2020 | Review | Acta Dermatovenerol Alp Pannonica Adriat | Classification and features of physical and non-physical chronic inducible urticaria, including cold urticaria |
| [8341871](https://pubmed.ncbi.nlm.nih.gov/8341871/) | 1993 | Review | Sports Med | Physical allergies, including cholinergic urticaria, and their clinical implications |
| [475987](https://pubmed.ncbi.nlm.nih.gov/475987/) | 1979 | Clinical report (single patient) | Br J Dermatol | In one patient with severe cold urticaria, hydroxyzine plus cimetidine significantly suppressed erythema, and H1 antagonists suppressed wheals |
| [2662834](https://pubmed.ncbi.nlm.nih.gov/2662834/) | 1989 | Case report | Ann Allergy | Cold-induced cholinergic urticaria in a 9-year-old child |
| [6163290](https://pubmed.ncbi.nlm.nih.gov/6163290/) | 1980 | Case report | Acta Derm Venereol | Solar urticaria with a good response to hydroxyzine |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort/Epidemiology | Asian Pac J Allergy Immunol | Urticaria in 142 Thai children |
| [21217928](https://pubmed.ncbi.nlm.nih.gov/21217928/) | 2011 | Case report | Allergy Asthma Immunol Res | Chlorpheniramine hypersensitivity; notes that hypersensitivity to hydroxyzine has also been reported |

For allergic urticaria, the 19 publications supplied are mostly reviews of H1 antihistamines, chiefly cetirizine (the active metabolite of hydroxyzine). They contain no hydroxyzine-specific trial data. One of them (PMID 31582993, a 2019 Canadian society position statement) recommends newer-generation antihistamines over first-generation ones such as hydroxyzine because of safety.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0237 | Hydroxyzine | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

**Contraindication-related disease associations (from the knowledge graph, not label text)**

The knowledge graph links hydroxyzine to caution in these conditions:
- **Cardiovascular:** hypertension, coronary artery disease, myocardial infarction, sudden cardiac arrest, heart conduction disease, heart disease
- **Eye:** open-angle and angle-closure glaucoma
- **Neuropsychiatric:** epilepsy, psychotic disorders, schizophreniform and schizoaffective disorders, substance abuse/dependence
- **Endocrine and metabolic:** hypothyroidism, hyperthyroidism, diabetes mellitus, diabetic ketoacidosis
- **Other:** liver disease, gallbladder disease, peptic ulcer disease, benign prostatic hyperplasia, hemoglobinopathy

**Drug Interactions** (100 interactions found; examples below)
- **Major:** morphine, potassium citrate, dolasetron
- **Moderate:** famotidine, hyoscyamine, loperamide, atropine, clarithromycin, levofloxacin, dicyclomine, trospium, and others
- **Minor:** cimetidine

**General notes from the literature:** first-generation antihistamines such as hydroxyzine commonly cause sedation, cognitive impairment, dry mouth, dizziness, and orthostatic hypotension. They have also been associated with accidents, overdoses, and sudden cardiac death (PMID 31582993).

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predictions are mechanistically plausible, but the evidence is thin. Cold urticaria has only one small, old comparative study plus case reports, and no clinical trials are registered.
- Allergic urticaria is essentially an existing indication, and the other predictions (rosacea conjunctivitis, recalcitrant atopic dermatitis, atopic IgE responsiveness) have no supporting studies.
- In the Philippines the only hydroxyzine registration is cancelled, and the safety profile of first-generation antihistamines is less favorable than that of newer alternatives.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Clarification of why the Philippines registration was cancelled and whether a current marketed product exists
- Hydroxyzine-specific controlled studies in cold urticaria, ideally compared against second-generation antihistamines
- A risk-benefit assessment in view of sedation, anticholinergic burden, and cardiac risk (e.g., QT-related concerns)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

