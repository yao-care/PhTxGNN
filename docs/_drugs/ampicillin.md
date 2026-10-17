---
layout: default
title: Ampicillin
parent: Moderate Evidence (L3-L4)
nav_order: 27
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Ampicillin: predicted new indication Laryngitis (evidence level L4). Approved use: Urinary tract infection, infectious otitis media, bacterial pneumonia…"
monitor_inn: "Ampicillin"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a beta-lactam antibiotic originally used for infections such as urinary tract infection, otitis media, bacterial pneumonia, meningitis and staphylococcal or streptococcal infections.
The TxGNN model predicts it may be effective for **laryngitis**, with a very high model score of 99.97%.
However, there are **0 registered clinical trials** and only **literature of low quality** (mostly case reports, reviews and surveillance papers), so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, bacterial pneumonia, bacterial meningitis, staphylococcal and streptococcal infections, among others (the Philippines registration record contains no indication text) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ampicillin belongs to the beta-lactam class of antibiotics, which inhibit bacterial cell wall synthesis. Its efficacy in respiratory, ear and meningeal bacterial infections is well established.

Bacterial infections of the larynx and surrounding structures (for example epiglottitis, laryngeal abscess and deep neck infection) could plausibly respond to a beta-lactam, which explains why the prediction is mechanistically reasonable on the surface.

The supporting data are weak, however. The retrieved literature is largely case reports, reviews and surveillance-type papers. Several records are off-target (Whipple's disease, deep neck infections in dogs, experimental otitis media in chinchillas, croup differential diagnosis). Most of the more relevant papers concern epiglottitis, where ampicillin was used historically, but Haemophilus influenzae type b has since developed ampicillin resistance (one paper documents this). The high TxGNN score is not backed by any trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | 161 children with acute epiglottitis; 45 complications and 5 deaths; emphasizes airway management |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Review | Rev Infect Dis | Sulbactam/ampicillin for pediatric epiglottitis; notes up to 25% of Hib strains are beta-lactamase producing and ampicillin resistant |
| [3290661](https://pubmed.ncbi.nlm.nih.gov/3290661/) | 1988 | Case series | Monatsschr Kinderheilkd | 27 children with epiglottitis; ampicillin-resistant Hib emerged and changed treatment |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | Case series | Anesth Analg | 23 children with epiglottitis treated with ampicillin or chloramphenicol; study focused on intubation duration |
| [3322611](https://pubmed.ncbi.nlm.nih.gov/3322611/) | 1987 | Case series | Clin Otolaryngol | 19 adults with epiglottitis; bacteriology and treatment principles |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Review | West J Med | 9 adults with acute epiglottitis; diagnosis and airway issues |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report/Review | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess case and review |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngol Head Neck Surg | Perioperative antibiotic choice and laryngectomy complications (prophylaxis, not laryngitis treatment) |
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline review | CoDAS | Quality assessment of laryngitis and pharyngitis guidelines |
| [7487676](https://pubmed.ncbi.nlm.nih.gov/7487676/) | 1995 | Animal study | Auris Nasus Larynx | Ibuprofen plus ampicillin in experimental otitis media in chinchillas (off-target) |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, impaired renal function, pyoureter, hematologic disease, peptic ulcer disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome, acute urate nephropathy
- **Drug Interactions**: 61 interactions were identified. Moderate-level examples include doxycycline, minocycline, tetracycline, kanamycin, balsalazide, lansoprazole, dexlansoprazole and picosulfuric acid. Clarithromycin is minor. Others (e.g., morphine, vancomycin, prednisone, omeprazole) have an unknown severity level.

Please also refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and the literature is low-quality and partly off-target. The best-fitting indication (epiglottitis) is historical, and ampicillin resistance in *Haemophilus influenzae* type b has reduced its role. In the Philippines, the only registration is cancelled.

Of the other predictions, gonococcal urethritis has the strongest literature (several older randomized comparative studies, L3), but this reflects historical use, and resistance means ampicillin is no longer recommended. Ureaplasma urethritis and paranasal sinus neoplasm are mechanistically implausible. Chronic rhinosinusitis, chronic ethmoidal sinusitis, gingivitis, bacterial arthritis, conjunctivitis and pericoronitis have only indirect evidence (all L4).

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Current local resistance data (especially *H. influenzae*, *N. gonorrhoeae*) and comparison with current guideline-recommended agents
- Evidence of ampicillin treatment outcomes in laryngeal infections specifically (e.g., prospective or comparative studies)
- Clarification of the registration status in the Philippines, since no valid license currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

