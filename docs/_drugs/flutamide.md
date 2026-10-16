---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Flutamide: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a nonsteroidal androgen receptor antagonist, originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is **prostate cancer/brain cancer susceptibility**, but this is a genetic-susceptibility label that overlaps with the original indication rather than a new therapeutic use.
It has **0 clinical trials** and **0 publications** directly supporting it, so the evidence is **model prediction only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Flutamide blocks the androgen receptor, which prostate cancer cells rely on for growth. Detailed mechanism data were not available in the data compiled for this report, but this androgen-receptor antagonism is well established.

The predicted "indication" is a genetic susceptibility label that overlaps with the drug's existing use in prostate cancer, so it is not a distinct therapeutic opportunity. The very high TxGNN score reflects how close this label sits to prostate cancer in the knowledge graph, and it is not clinical evidence. No trials or literature were found for this specific prediction.

### Other Predictions Worth Noting

Several lower-ranked predictions have some supporting evidence, though none is strong:

- **Benign reproductive system neoplasm (rank 4, L3):** Small, dated (1990s) clinical studies exist. The most relevant is [PMID 1722793](https://pubmed.ncbi.nlm.nih.gov/1722793/), which examined flutamide in men with benign prostatic hyperplasia (effects on prostate volume, PSA and testosterone). Most other items are preclinical or histopathology studies.
- **Male reproductive organ cancer (rank 6, graded L1):** This category is dominated by prostate cancer, the original indication. The Phase 3 trials in it do not confirm flutamide as a specific arm, so the L1 grade should be verified. The most directly relevant study is [NCT00006214](https://clinicaltrials.gov/study/NCT00006214), a Phase 2 trial of flutamide for chemoprevention in men with prostatic intraepithelial neoplasia (63 participants, completed).
- **Fibroma of prostate, Brenner tumor, prostate leiomyoma, benign prostate phyllodes tumor, HIV infectious disease, feline AIDS and simian immunodeficiency virus infection:** These have no supporting trials or literature. The HIV-related predictions have no identified mechanistic link and likely reflect graph similarity only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0202 | Flutamide | Not recorded | Not recorded (status: cancelled) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal antiandrogen), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not a major recognised feature; confirm against the package insert) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (hepatotoxicity is a boxed-warning concern); methemoglobin levels where clinically indicated |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: Hepatotoxicity (boxed warning) is a major concern. Severe hepatic dysfunction has been reported in some treated patients, and toxic metabolites have been proposed as the cause.
- **Disease Contraindications (knowledge-graph derived, not label text)**: Liver failure, liver disease, gallbladder disease, methemoglobinemia, sulfhemoglobinemia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Drug Interactions**: 100 interactions were identified, and the first 20 are summarised here.
  - **Major:** Dolasetron, Cisapride.
  - **Moderate:** Famotidine, Loperamide, Bisacodyl, Clarithromycin, Picosulfuric acid, Polyethylene glycol (including 3350 with electrolytes), Palonosetron, Obeticholic acid, Sodium sulfate, Naltrexone, Levofloxacin, Lactitol, Lactulose, Ondansetron, Castor oil, Glycerin.
  - **Minor:** Metronidazole.

The label-based warnings and contraindications from the Philippines package insert were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a susceptibility label that duplicates the original prostate cancer indication, with no trials or literature behind it. The drug also carries a hepatotoxicity warning and an extensive interaction profile, and its only Philippines registration has been cancelled, since newer antiandrogens have largely replaced it.

**To proceed, the following is needed:**
- Re-evaluate more clinically meaningful candidates (for example, prostatic intraepithelial neoplasia chemoprevention or benign prostatic disease) with flutamide-specific evidence.
- Verify whether the Phase 3 trials in the male reproductive cancer category actually include a flutamide arm.
- Obtain the Philippines package insert to confirm warnings, contraindications and approved indications.
- Obtain detailed mechanism of action data.
- Develop a liver-safety monitoring and interaction management plan before any further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

