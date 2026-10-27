---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acyclovir: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Herpes simplex infection, herpes zoster, chickenpox, herpes labialis…"
monitor_inn: "acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Acyclovir: From Herpes Simplex Infection to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Acyclovir is an antiviral originally used for herpes simplex infections, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but this has **0 clinical trials** and only **2 publications**, neither of which supports it.
The best-supported lead among the model's predictions is instead **common wart** (4 clinical trials and 19 publications, mostly small studies of intralesional injection), which is discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex infection, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes (the Philippines registration has no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (top-ranked); common wart is the best-supported alternative |
| TxGNN Prediction Score | 99.67% (common wart: 99.46%) |
| Evidence Level | L5 for the top-ranked prediction (common wart: L2) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold for the top-ranked prediction; common wart could be pursued as a research question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Acyclovir is a well-known antiviral. It is activated by viral thymidine kinase and then inhibits viral DNA polymerase, so it is mainly active against herpesviruses.

**Top-ranked prediction (punctate epithelial keratoconjunctivitis):** A mechanistic link is plausible only if the condition is herpesvirus-driven. The two publications retrieved concern microsporidial keratoconjunctivitis and drug-induced corneal lipidosis in AIDS. Neither involves herpetic disease or an acyclovir response. The prediction is therefore not supported by the available evidence.

**Common wart:** Warts are caused by HPV, a DNA virus without viral thymidine kinase, so acyclovir's usual activation pathway does not apply. Any benefit is probably indirect, such as a local immune response to intralesional injection. Several small randomized studies report clinical responses, but the mechanism is unclear and the studies are small and varied, often open-label.

**Other predictions of note:** Herpetic eye and periocular disease (listed as "disease of orbital region", rank 9) is essentially an extension of the existing herpes indications to ocular sites. Several other predictions (hepatitis C cirrhosis, vulvovaginal candidiasis, epidemic keratoconjunctivitis, eosinophilic pustular folliculitis, papular urticaria) have no plausible mechanism for acyclovir. Post-infectious neuralgia has no trials or literature.

---

## Clinical Trial Evidence

The top-ranked prediction (punctate epithelial keratoconjunctivitis) has no related clinical trials registered. The trials below are for **common wart**, the best-supported alternative.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Randomized trial of intralesional acyclovir vs cryotherapy in plantar warts; results not confirmed |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir vs Candida antigen in plantar warts |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 vs acyclovir in cutaneous warts; no results yet |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | Not applicable | Unknown | 44 | Intralesional vitamin D3 vs acyclovir in plantar warts |

For the broader "disease of orbital region" prediction, the relevant trials include [NCT06757907](https://clinicaltrials.gov/study/NCT06757907) (completed, n=20, topical ganciclovir vs systemic acyclovir in herpetic keratitis) and [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) (unknown status, n=30, oral acyclovir in viral uveitis). Both are small.

---

## Literature Evidence

**Top-ranked prediction (punctate epithelial keratoconjunctivitis):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Microsporidial keratoconjunctivitis; not herpetic or acyclovir-related |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case series | Am J Ophthalmol | Drug-induced corneal lipidosis in AIDS patients; no support for the prediction |

**Common wart (best-supported alternative):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir vs cryotherapy in plantar warts |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs 5-fluorouracil in recalcitrant warts |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs quadrivalent HPV vaccine in recalcitrant warts (60 patients) |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir vs hepatitis B vaccine in resistant plantar warts (48 patients) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review/network meta-analysis | Medicine | Comparison of treatment modalities for cutaneous warts, including intralesional acyclovir |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir vs PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir as a potential option for cutaneous warts |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after oral acyclovir given for herpes zoster |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0004 | Aciclovir | Not specified | Not specified (registration cancelled) |

The only registration is cancelled, so there is currently no valid registered acyclovir product in the Philippines according to the data compiled for this report.

---

## Safety Considerations

**Drug Interactions:** The interaction database lists 454 interacting drugs. The ones classified as moderate are:
- Balsalazide
- Mesalazine
- Olsalazine
- Sulfasalazine
- Trospium

Others, such as amphotericin B, mannitol, metformin, omeprazole, morphine and doxycycline, have an unclassified severity level.

**Contraindication signals from the knowledge graph:** These come from model-derived drug-disease links, not from label text, and should be verified against the package insert. They include kidney disease and impaired renal function, hemolytic-uremic syndrome, thrombocytopenic purpura, hypertension, diabetes and diabetic ketoacidosis, adrenocortical insufficiency, stroke and myocardial infarction, and peripheral vascular disease.

Package insert warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, punctate epithelial keratoconjunctivitis, has no trials and only unrelated literature, and the model score alone is not enough to justify moving forward (L5).
- The only credible lead is intralesional acyclovir for common/plantar warts (L2), supported by several small, heterogeneous studies with an unclear mechanism. This can be treated as a research question rather than a recommendation. The ocular herpes uses are largely an extension of existing indications.
- The sole Philippines registration is cancelled, which adds a regulatory hurdle.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippines FDA, which are required before safety screening
- Mechanism of action data, to support analysis of a mechanistic link
- Larger, blinded, adequately powered trials of intralesional acyclovir in warts, with confirmed results from the existing trials
- Review of the contraindication signals against the label, especially renal function
- A regulatory pathway for the cancelled registration, and an assessment of whether an injectable intralesional use fits an available product and route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

