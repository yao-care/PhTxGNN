---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

Using the `txgnn-pipeline` skill to confirm reporting context, then proceeding to generate the evaluation report based on the Evidence Pack.

---

# Metronidazole: From Anaerobic & Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole (DB00916) is a nitroimidazole antibiotic with established activity against anaerobic bacteria and protozoa, widely used for infections such as bacterial vaginosis, amebiasis, giardiasis, and trichomoniasis.
The TxGNN model predicts it may be effective for **Pneumocystosis** with a score of **99.99%** (Rank 180); however, all 10 retrieved publications are low-grade contextual references, no relevant clinical trials were found, and this prediction is assessed as a **knowledge graph false positive** with no mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; known primary use: anaerobic & protozoal infections |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, metronidazole is a prodrug that is reduced by anaerobic or microaerophilic organisms to generate cytotoxic reactive intermediates, which disrupt DNA structure and inhibit nucleic acid synthesis. This reductive activation is the cornerstone of its selectivity — only organisms capable of reducing the nitro group can activate the drug. It therefore has no meaningful activity against aerobic bacteria, fungi, or aerotolerant organisms.

Pneumocystosis is caused by *Pneumocystis jirovecii*, an organism that was historically classified as a protozoan but has been firmly established as a fungus since the 1990s. Fungi do not possess the nitroreductase pathways needed to activate metronidazole, making the drug pharmacologically inert against *P. jirovecii*. The established standard of care for PCP is trimethoprim-sulfamethoxazole (TMP-SMX), with pentamidine or atovaquone reserved for intolerant patients.

The high TxGNN prediction score almost certainly reflects a **historical knowledge graph artifact**: PCP shared "protozoal infection" classification nodes with diseases for which metronidazole genuinely works (amebiasis, giardiasis, trichomoniasis) for decades before reclassification. This legacy linkage creates a spurious repurposing signal. **The prediction does not reflect a real pharmacological opportunity and should not be advanced.**

---

## Clinical Trial Evidence

All 10 clinical trials retrieved by the database query are entirely unrelated to pneumocystosis or metronidazole — topics include mindfulness-based primary care interventions, chronic kidney disease decision support, and Alzheimer's care navigation. This is consistent with database retrieval noise rather than genuine evidence.

Currently no related clinical trials registered for metronidazole in pneumocystosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | HIV-related opportunistic infections update; PCP discussed with standard TMP-SMX treatment; metronidazole not mentioned as a PCP therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Review of AIDS infectious complications; PCP is the most common life-threatening process, treated with TMP-SMX or pentamidine; metronidazole not indicated |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | Antiparasitic agents overview; TMP-SMX for PCP; metronidazole listed for amebiasis/trichomoniasis only |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Drug-of-choice summary: TMP-SMX for PCP; metronidazole for amebic colitis and trichomoniasis — no overlap |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetic rationale for antiprotozoal therapy; metronidazole discussed for protozoal (not fungal) infections |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Rev Respir Dis | PCP case in a man previously treated with metronidazole for diarrhea; metronidazole was not used to treat PCP and did not prevent it |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | AIDS patients in Japan developing PCP; metronidazole used earlier for amebic dysentery — confirms it is ineffective against PCP |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formosan Med Assoc | HIV patient with ameba colitis and CMV infection; metronidazole used for amebiasis, not for any pneumocystis component |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Drugs for protozoal infections in humans; categorically separates PCP treatment from antiprotozoal coverage |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Antimicrobial prophylaxis critique; metronidazole discussed in surgical/anaerobic context only |

> **Important:** None of the 10 publications provide evidence that metronidazole is active against *Pneumocystis jirovecii*. Several explicitly contrast metronidazole's antiprotozoal role against TMP-SMX as the correct PCP treatment, reinforcing that this is a false-positive TxGNN prediction.

---

## Philippines Market Information

Metronidazole is **not currently registered** with the Food and Drug Administration (FDA) Philippines. No product licenses or approved indications are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is mechanistically implausible. *Pneumocystis jirovecii* is a fungus that lacks the nitroreductase pathways required to activate metronidazole; the drug has no pharmacological activity against PCP. The 99.99% TxGNN score is a knowledge-graph artifact from outdated protozoal taxonomy and should not be interpreted as clinical signal.

**To proceed with the broader Metronidazole repurposing program, the following is needed:**

- **Retrieve MOA data from DrugBank** (DG002 — currently blocking mechanism-linkage analysis)
- **Download Philippines FDA package insert** (DG001 — blocking safety pre-screening for all candidates)
- **Redirect focus to higher-priority candidates with real biological rationale:**
  - **Cap polyposis** (Rank 9, L4, *Proceed with Guardrails*) — only indication with a publication directly studying metronidazole as treatment (PMID 12141801); dual antibiotic + anti-inflammatory mechanism plausible; rare disease with unmet need
  - **Ulcerative proctosigmoiditis** (Rank 3, L4, *Research Question*) — indirect evidence via Crohn's/pouchitis precedent; anaerobic dysbiosis mechanism applicable
  - **Ulceration of vulva** (Rank 10, L4, *Research Question*) — pathogen-specific evidence for vulvar amebiasis (PMID 6835740, 8840708) and vulvar Crohn's disease; cause-dependent recommendation needed
- **Formally document the pneumocystosis false-positive** as a KG noise case to inform model retraining
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

