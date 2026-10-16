---
layout: default
title: Tacrolimus
parent: High Evidence (L1-L2)
nav_order: 323
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-15
description: "Tacrolimus: predicted new indication Seborrheic dermatitis (evidence level L2). Approved use: Atopic eczema / atopic dermatitis"
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor, originally used to treat atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
with **2 clinical trials** (one completed Phase 3, one completed Phase 4) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* The data compiled for this report assigns L1 to this prediction. However, only one completed Phase 3 trial (NCT02004860) is directly in seborrheic dermatitis, and the second trial is Phase 4. Under the stated criteria (≥2 completed Phase 3 RCTs for L1), this report conservatively rates it L2. Neither trial has published results in the data reviewed.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available. Based on the literature reviewed, tacrolimus inhibits calcineurin, which blocks T-cell activation and the release of pro-inflammatory cytokines such as IL-2, IFN-gamma and TNF-alpha.

Atopic dermatitis and seborrheic dermatitis are both chronic, relapsing inflammatory skin diseases. Seborrheic dermatitis involves an inflammatory response to *Malassezia* yeasts, and calcineurin inhibition can dampen this response. Some antifungal activity against *Malassezia* has also been proposed. The mechanism therefore overlaps with that of the approved indication, making the link plausible. Topical corticosteroids have long-term adverse effects, which makes a steroid-sparing maintenance option attractive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Tacrolimus ointment (Protopic) as maintenance treatment for severe facial seborrheic dermatitis in adults, aiming to reduce relapses and steroid use. Results not summarized in the data reviewed. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce exacerbations. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Reviews topical therapies (antifungals, keratolytics, corticosteroids) for facial seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clin Exp Allergy | Cochrane comparison of topical anti-inflammatory treatments for eczema |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors as a safe alternative to corticosteroids in seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Ann Parasitol | Sertaconazole 2% cream compared with tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | Evidence for off-label use of topical calcineurin inhibitors in dermatologic disorders |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opin Investig Drugs | New roles for topical tacrolimus beyond atopic dermatitis |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Tacrolimus ointment in atopic dermatitis and other inflammatory skin diseases |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Topical tacrolimus and pimecrolimus in psoriasis, seborrheic dermatitis and other conditions |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0468 | Tacrolimus | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from the drug-disease knowledge graph, not from label text): hypertension, long QT syndrome and torsades de pointes, liver failure, kidney disease, epilepsy, hyperglycemia and diabetes mellitus (including diabetic ketoacidosis), active or prior infections (including herpes simplex, herpes zoster, infectious mononucleosis and chronic Epstein-Barr virus infection), cancer and lymphoma (including primary CNS lymphoma), progressive multifocal leukoencephalopathy, posterior leukoencephalopathy syndrome, delirium, and some bone marrow failure syndromes. Many of these relate mainly to systemic tacrolimus and may not apply equally to topical use.
- **Malignancy signal for topical calcineurin inhibitors**: topical calcineurin inhibitors carry a boxed warning for malignancy and lymphoma. A 2023 systematic review and meta-analysis (PMID 36370744) examined cancer risk with topical tacrolimus and pimecrolimus in atopic dermatitis. Use should follow label restrictions (second-line, short-term or intermittent, not on infected skin, avoided in very young children).
- **Drug interactions**: 100 interactions were identified. Major-level interactions include amphotericin B (including the lipid complex), loperamide, mesalazine, omeprazole and balsalazide. Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, pioglitazone, famotidine, rabeprazole, aprepitant and metronidazole. These are mostly relevant to systemic exposure; minimal absorption is expected with topical use.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial and a completed Phase 4 trial directly test tacrolimus ointment in seborrheic dermatitis, supported by a clinical study and several reviews, and the mechanism is plausible. However, there are no published results from the Phase 3 trial in the data reviewed. The Philippines registration is cancelled, and the boxed warning on malignancy and lymphoma for topical calcineurin inhibitors requires careful management.

**To proceed, the following is needed:**
- Results of NCT02004860 and NCT01591070 (efficacy, relapse rates, safety)
- Package insert warnings and contraindications from DOH-FDA Philippines (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Clarification of the cancelled registration status and whether a topical product is available or can be registered in the Philippines
- A long-term safety monitoring plan consistent with the boxed warning (short-term or intermittent use, avoiding infected skin and very young children)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

