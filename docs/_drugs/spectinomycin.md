---
layout: default
title: Spectinomycin
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Spectinomycin: predicted new indication Urethral disease (evidence level L5). Approved use: Acute gonococcal cervicitis"
---

# Spectinomycin
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

# Spectinomycin: From Gonorrhea to Urethral Disease

## One-Sentence Summary

Spectinomycin is an injectable antibiotic originally used to treat gonorrhea and acute gonococcal cervicitis.
The TxGNN model's top-ranked predictions are unusual non-infectious conditions with no supporting evidence. The best-supported prediction is **Urethral Disease** (rank 8), backed by **0 clinical trials** and **20 publications**. Most of these publications concern gonococcal urethritis, which is close to the drug's original use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute gonococcal cervicitis; gonorrhea (the Philippines license record lists no approved indication text) |
| Predicted New Indication | Urethral disease (the best-supported of the top 10 predictions; the rank 1 prediction is disease of uterine broad ligament, with no evidence) |
| TxGNN Prediction Score | 99.53% (urethral disease); 99.57% for the rank 1 prediction |
| Evidence Level | L3 (urethral disease); the other nine predictions are L4–L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, spectinomycin is an aminocyclitol antibiotic that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit. Its efficacy in gonorrhea is well established.

For **urethral disease**, the prediction is reasonable mainly because gonococcal urethritis is an infection of the urethra. This is largely a restatement of the original indication rather than true repurposing. A recent 2025 retrospective report of four cases suggests intramuscular spectinomycin may help in difficult-to-treat *Mycoplasma genitalium* urethritis. That would be a genuinely new use, but the evidence is very small.

The other top-ranked predictions have no plausible link to an antibacterial mechanism. They include disease of the uterine broad ligament, abdominal cystic lymphangioma, celiac trunk compression syndrome, abdominal ectopic pregnancy, lymph node palisaded myofibroblastoma, sacrum chordoma and embryonic cyst of the fallopian tube. They have no trials or literature, and their high scores likely reflect proximity in the knowledge graph rather than a real mechanism. "Disease of peritoneum" has only one 1979 review of gonococcal pelvic inflammatory disease, which relates to the original indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications retrieved for urethral disease are listed below, ranked by relevance and study type. Many of the remaining items are surveillance studies or papers on other antibiotics, and they offer only indirect support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [139565](https://pubmed.ncbi.nlm.nih.gov/139565/) | 1977 | Randomized comparison | N Engl J Med | 4,043 patients received spectinomycin or oral tetracycline. Cure rate for anogenital gonorrhea was at least 94% with either drug. Oropharyngeal infection responded poorly to spectinomycin in men. |
| [3156805](https://pubmed.ncbi.nlm.nih.gov/3156805/) | 1985 | Randomized comparison | Genitourin Med | 200 men with gonococcal urethritis received 2 g spectinomycin or 250 mg ceftriaxone. All followed-up patients in both arms were cured. |
| [6134959](https://pubmed.ncbi.nlm.nih.gov/6134959/) | 1983 | Comparative study | Lancet | Ceftriaxone cured 100% of men, and spectinomycin 2 g IM cured 97% of 58 men with uncomplicated urethral or anorectal gonorrhea. |
| [40714374](https://pubmed.ncbi.nlm.nih.gov/40714374/) | 2025 | Retrospective cohort (4 cases) | J Infect Chemother | Evaluated IM spectinomycin in difficult-to-treat *M. genitalium* urethritis, where previous options had failed. |
| [132888](https://pubmed.ncbi.nlm.nih.gov/132888/) | 1976 | Review | Ann Intern Med | A single 2 g IM dose is highly effective for uncomplicated anogenital gonorrhea. It is indicated for patients who cannot receive penicillin or probenecid. |
| [6231755](https://pubmed.ncbi.nlm.nih.gov/6231755/) | 1984 | Review | Urol Clin North Am | Reviews gonococcal urethritis therapy in light of penicillinase-producing strains and emerging resistance. |
| [19177762](https://pubmed.ncbi.nlm.nih.gov/19177762/) | 2009 | Review | Nihon Rinsho | Reviews *N. gonorrhoeae* infections, including urethritis, and rising antimicrobial resistance. |
| [6453520](https://pubmed.ncbi.nlm.nih.gov/6453520/) | 1981 | Review | Am Fam Physician | Penicillin cured 97–98% of cases. Spectinomycin was an alternative for penicillin-allergic patients. |
| [41138812](https://pubmed.ncbi.nlm.nih.gov/41138812/) | 2025 | Surveillance (indirect) | J Infect Chemother | Japanese national susceptibility surveillance of *N. gonorrhoeae* from male urethritis in 2021. |
| [39034819](https://pubmed.ncbi.nlm.nih.gov/39034819/) | 2024 | Epidemiology (indirect) | Ann Lab Med | Prevalence and susceptibility of pharyngeal gonorrhea in Korean men with urethritis. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0457 | Spectinomycin | Not recorded | Not recorded (status: cancelled) |

The only registration is cancelled, so the drug is not currently authorized in the Philippines.

---

## Safety Considerations

- **Drug Interactions**: One interaction is recorded, with picosulfuric acid (Moderate severity, DDInter).

For other safety information, such as warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predictions are non-infectious conditions with no trials or literature and no plausible antibacterial mechanism.
- The best-supported prediction, urethral disease (L3), mostly restates the original gonorrhea indication. The only truly new signal is a four-case *M. genitalium* report.
- The Philippines registration is cancelled, so the drug is not currently available.

**To proceed, the following is needed:**
- Confirmation of current availability, either through re-registration or special import.
- Mechanism of action data and package insert warnings and contraindications.
- Larger prospective studies of spectinomycin in *M. genitalium* urethritis, if a repurposing case is to be pursued.
- Review of current local resistance patterns and treatment guidelines for gonorrhea and non-gonococcal urethritis.
- Dropping the low-evidence, non-infectious predictions from further consideration unless independent supporting evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

