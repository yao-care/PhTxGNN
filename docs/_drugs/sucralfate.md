---
layout: default
title: Sucralfate
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate was originally used to treat duodenal ulcer.
The TxGNN model predicts it may be effective for **duodenogastric reflux** (alkaline reflux gastritis), but there are **no registered clinical trials**. Support comes from **10 publications**, including 2 randomized trials of small size.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (from the TxGNN knowledge graph; no approved indication text is available in the Philippines registration) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 (see note below) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

*Evidence level note: no completed Phase 2/3 trial is registered. The L2 rating rests on small published randomized studies, so it should be read as a cautious, provisional level.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, sucralfate is a mucosal protectant. It binds to damaged gastric and esophageal mucosa and forms a protective barrier. It is also known to adsorb bile salts and pepsin.

Duodenogastric reflux (alkaline reflux gastritis) injures the stomach lining through bile and pancreatic secretions flowing back from the duodenum. A drug that shields the mucosa and binds bile salts could plausibly reduce this injury. This is consistent with its original use in duodenal ulcer, where mucosal protection is also the goal.

This link is based on general knowledge, not on a mechanism record in the compiled data, and the published study results cannot be fully verified from the available abstracts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Double-blind study of sucralfate 6 g/day vs placebo in 23 post-gastric-surgery patients with alkaline reflux gastritis symptoms; 6 weeks of blinded treatment followed by 6 weeks of open sucralfate. Outcome details are not available in the abstract excerpt. |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Sucralfate vs rabeprazole vs no treatment for post-cholecystectomy alkaline reactive gastritis, assessing dyspeptic symptoms and endoscopic/histological signs. Results not shown in the abstract excerpt. |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Clinical study | Minerva Gastroenterol Dietol | 18 patients with dyspepsia from duodenogastric reflux gastritis, comparing cisapride 30 mg/day with sucralfate 4 g/day for two months. |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Cohort / case series | Rev Esp Enferm Apar Dig | 50 cases of gastritis from postsurgical biliary reflux treated with sucralfate (no abstract available). |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Randomized trial (reported as review) | Scand J Gastroenterol Suppl | Half-year sucralfate vs placebo trial in patients with symptomatic, macroscopic gastritis, relating gastritis to duodenogastric reflux. |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Committee statement | Am J Gastroenterol | Notes that a role for sucralfate in gastritis, esophagitis and stomatitis is promising but not clearly established. |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Duodenogastric reflux-induced esophagitis; best medical treatment is described as proton-pump inhibitors, and treatment is difficult. |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Overview of alkaline reflux gastritis and esophagitis: causes, features and pathophysiology. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Cohort | Eur J Pediatr | Six children with primary duodenogastric reflux unresponsive to classical antacid therapy; background on the condition. |
| [2186496](https://pubmed.ncbi.nlm.nih.gov/2186496/) | 1990 | Clinical study | Ter Arkh | 72 patients with gastroduodenal erosive and ulcerous injury treated with sucralfate (Antepsin); shows benefit in ulcer disease, not reflux. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0462 | Sucralfate | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: hyperglycemia, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure.
- **Drug Interactions**: 100 interactions were found in the DDI database; the first 20 are summarized here.
  - **Major**: dolutegravir, bictegravir.
  - **Moderate**: acarbose, doxycycline, tetracycline, albiglutide, alogliptin, pioglitazone, alendronic acid, risedronic acid, ibandronate, allopurinol, ascorbic acid, baloxavir marboxil, calcifediol.
  - **Minor**: acebutolol, atenolol, betaxolol, bisoprolol, anagrelide.

Please refer to the package insert for label warnings, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high and the mechanism is plausible, but there are no registered trials, the randomized studies are small and about 20-40 years old, and the only Philippines registration is cancelled. The evidence is not strong enough to proceed.

**To proceed, the following is needed:**
- Full-text review of the two randomized trials (PMID 3839973 and 12923369) to confirm actual outcomes
- Confirmed mechanism of action data from DrugBank
- Package insert warnings and contraindications from the DOH-FDA Philippines
- A valid Philippines registration or a plan to re-register the product
- A safety plan for patients with kidney disease or diabetes, and for interactions (especially with integrase inhibitors, tetracyclines and bisphosphonates)

*Note on the second prediction: "duodenal obstruction" (TxGNN score 99.30%) was also reviewed. No credible mechanistic link or supporting evidence was found, because obstruction is a structural problem a mucosal protectant would not be expected to relieve. It is rated L5 with a Hold recommendation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

