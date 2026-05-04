---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Budesonide: From Asthma and Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a synthetic glucocorticoid widely established internationally for the treatment of asthma, allergic rhinitis, COPD, and inflammatory bowel disease, though it currently holds no Philippines market registration.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with a prediction confidence of **99.96%**.
Currently, **2 clinical trials** and **20 publications** have been identified in this direction, though the majority have limited direct relevance to budesonide as a specific dermatological agent for atopic eczema.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration on record; globally established for asthma, allergic rhinitis, COPD, and IBD |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, budesonide is a synthetic glucocorticoid receptor (GR) agonist with high topical anti-inflammatory potency and relatively low systemic bioavailability due to extensive first-pass metabolism. It suppresses pro-inflammatory gene transcription by inhibiting NF-κB and AP-1 pathways, reducing the production of cytokines, chemokines, and adhesion molecules responsible for immune cell recruitment.

Atopic eczema (atopic dermatitis) is driven primarily by Th2-skewed immune dysregulation, featuring elevated IL-4, IL-13, and IL-31 signaling, skin barrier dysfunction (reduced filaggrin and ceramide expression), and eosinophilic infiltration. Budesonide's GR agonist mechanism directly suppresses these Th2 cytokines and reduces eosinophilic skin infiltration — aligning closely with the core pathology of atopic eczema. It is important to note that topical corticosteroids (TCS) as a drug class are already the internationally endorsed first-line treatment for atopic dermatitis (NICE, AAD, EADV guidelines), placing budesonide in a mechanistically well-supported position.

A 2024 preclinical formulation study (PMID 38275852) specifically loaded budesonide into pH-sensitive polymeric nanoparticles embedded in hydrogel for local therapy of pediatric atopic dermatitis, demonstrating improved release kinetics and skin penetration — representing an active and promising research direction for budesonide-specific AD therapy. A critical safety note: multiple publications (PMID 35133669, 24603519) document budesonide's potential to act as a contact allergen in atopic dermatitis patients themselves, making pre-treatment patch testing an essential safety guardrail in this population.

---

## Clinical Trial Evidence

Both identified trials have low direct relevance to budesonide's efficacy specifically in atopic eczema, as neither evaluates budesonide as the primary intervention for this indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy (not budesonide) in high-risk atopic wheezing children aged 18 months–3 years to prevent asthma progression; budesonide, if used, served only as background therapy |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Observational characterization of severe paediatric asthma endotypes via immune, metabolomics, and microbiota profiling; not an atopic eczema intervention trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical / Formulation | *Gels (Basel)* | Budesonide-loaded Eudragit L 100 nanoparticles in pH-sensitive hydrogel for pediatric AD local therapy; improved dermal delivery and reduced adverse effects vs. conventional formulation |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT (Subgroup) | *Allergologia et Immunopathologia* | Budesonide response assessed in atopic vs. non-atopic infants with recurrent wheezing; confirms differential treatment response in the atopic subgroup |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | Randomized Controlled Trial (Veterinary) | *J Vet Pharmacol Ther* | 0.025% budesonide leave-on conditioner (Barazone) significantly reduced skin lesions and pruritus vs. placebo in canine atopic dermatitis (n=29, crossover RCT) — mechanistic proof-of-concept for topical budesonide in AD |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Observational (Safety) | *Dermatology (Basel)* | Topical glucocorticosteroids in children with AD assessed for systemic effects on IGF axis, bone and collagen turnover; relevant for growth-monitoring protocols in pediatric use |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | *Contact Dermatitis* | Asian AD patients show similar or higher rates of positive patch tests vs. non-AD population; important baseline for budesonide sensitization pre-screening |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cross-sectional | *Dermatitis* | Contact hypersensitivity to corticosteroids (including budesonide) documented in AD adolescents and adults; sensitization rate data relevant for clinical decision-making |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional | *J Am Acad Dermatol* | Corticosteroids identified as a common sensitizer in adults with AD using topical medications; supports mandatory patch-test screening protocol |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Observational | *Contact Dermatitis* | Italian multicenter budesonide patch-test data (2018–2019): decreasing trend of budesonide allergy over two decades, suggesting current sensitization risk may be lower than historical estimates |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational | *J Allergy Clin Immunol* | Cutaneous ceramide synthesis dysregulation in pediatric EoE mirrors AD barrier dysfunction; supports shared Th2/epithelial pathways relevant to budesonide's mechanism |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | *Neuroimmunomodulation* | Intranasal corticosteroids and HPA axis suppression; relevant safety monitoring framework for patients receiving multiple corticosteroid preparations (e.g., concurrent inhaled + topical) |

---

## Philippines Market Information

Budesonide currently has **no registered products** with the Philippines Food and Drug Administration. No authorized licenses, product names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note from published evidence:** Multiple studies (PMID 35133669, 24603519, 30053491, 33931866) document budesonide's capacity to act as a contact allergen in atopic dermatitis patients. Pre-treatment patch testing is strongly advisable before prescribing topical budesonide specifically to this population, as contact sensitization to the drug itself may worsen disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for budesonide in atopic eczema is well-grounded — topical corticosteroids are already guideline-endorsed first-line therapy for atopic dermatitis, and budesonide's GR agonist activity directly targets the Th2-mediated skin inflammation that defines this disease. Active 2024 formulation research using nanoparticle delivery systems demonstrates continued scientific interest. However, human clinical trial evidence for budesonide specifically as a dermatological agent in atopic eczema remains at the preclinical and observational level (L3), and the drug has no Philippines market registration, requiring regulatory groundwork before any clinical application.

**To proceed, the following is needed:**
- Package insert review (TFDA, EMA, or FDA label) to document key warnings and contraindications for safety screening
- Formal MOA documentation from DrugBank or primary literature to complete mechanistic profiling
- Prospective clinical trial(s) evaluating topical budesonide formulations (including nanoparticle hydrogel) specifically for human atopic dermatitis — this is the primary evidence gap
- Mandatory budesonide patch-test protocol for all AD patients prior to prescribing to screen for pre-existing contact sensitization
- Drug interaction (DDI) manual review, as the automated query returned no results
- Philippines regulatory filing strategy for initial market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

