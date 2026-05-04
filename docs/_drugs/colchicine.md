---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Colchicine: From Gout and Autoinflammatory Disease to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is a plant-derived alkaloid that has served as the global standard of care for acute gout and Familial Mediterranean Fever (FMF), acting through microtubule depolymerization and inflammasome suppression.
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria** (top-ranked prediction, score 99.60%),
currently supported by **6 publications** — all in vitro or preclinical — with **no registered clinical trials** for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout; Familial Mediterranean Fever (established global standard of care; not currently registered in the Philippines) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (preclinical in vitro only) |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not captured in this Evidence Pack. Based on established pharmacology, Colchicine binds the colchicine-binding site on β-tubulin and inhibits microtubule polymerization. This leads to disruption of the mitotic spindle (M-phase arrest), inhibition of neutrophil chemotaxis and degranulation, and interference with NLRP3/Pyrin inflammasome assembly — the pharmacological basis for its efficacy in both gout and FMF.

*Plasmodium falciparum* is highly dependent on microtubule dynamics throughout its intraerythrocytic replication cycle, particularly during schizogony (nuclear division) and merozoite formation, where spindle apparatus assembly is essential. Compounds that target tubulin have demonstrated in vitro activity against the parasite: one study (PMID 2221861) found that Colcemid — a structural analogue of Colchicine — produced effects on parasite protein biosynthesis similar to tubulozoles, indirectly implicating the colchicine-binding site as a candidate antimalarial target. A subsequent screening study (PMIDs 2670249, 2655935) confirmed that multiple tubulin-binding substances active in mammalian systems show antiparasitic activity in vitro, while noting that plasmodial tubulins differ from human tubulins at the molecular level — which theoretically could allow selective targeting.

However, a fundamental limitation exists: no study has tested Colchicine itself directly against P. falciparum. All supporting literature uses surrogate compounds (tubulozoles, curcumin, Colcemid). The selectivity index — the difference in potency between parasite killing and human cell toxicity — has not been established for Colchicine in this context. Until direct in vitro data and an in vivo model confirm a viable therapeutic window, the prediction remains mechanistically plausible but clinically unvalidated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Colchicine in Plasmodium falciparum malaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro pharmacology | Antimicrob Agents Chemother | Tubulozole isomers reduced P. falciparum protein biosynthesis; Colcemid (colchicine analogue) produced a similar inhibitory effect, suggesting that colchicine-site ligands may have antimalarial potential |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro screening | Cell Biol Int Rep | Nine tubulin-binding compounds tested against intraerythrocytic P. falciparum; plasmodial tubulins found to differ from mammalian proteins at the molecular level, raising the possibility of selective targeting |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro screening | Cell Biol Int Rep | Cytoskeletal-targeting compounds active against P. falciparum in vitro; Tubulozole-T, inactive in mammalian systems, identified as a promising antimalarial candidate, illustrating species-level selectivity differences |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro mechanistic | PLoS One | Curcumin disrupts P. falciparum microtubule structure by binding tubulin and impairing mitotic spindle assembly; extends mechanistic rationale for tubulin-targeted antimalarials beyond the tubulozole class |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Clinical observational | Clin Exp Immunol | Anti-intermediate filament antibodies detected in 82% of acute malaria patients, compared to 8% of healthy donors; suggests significant cytoskeletal disruption occurs during P. falciparum infection, contextualizing cytoskeletal proteins as relevant targets |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro molecular | Mol Cell Biol | pfmdr1-encoded protein Pgh1 (ABC transporter) expressed in CHO cells increases chloroquine susceptibility; contextualizes parasite drug resistance mechanisms relevant to designing combination approaches |

---

## Philippines Market Information

Colchicine currently has **no registered products** with the Philippine FDA. No product authorizations on record as of the data cutoff (2026-04-04). A market entry assessment and regulatory registration pathway would be required before any clinical application in the Philippines.

---

## Safety Considerations

Philippine FDA package insert data (warnings, contraindications) were not collected in this Evidence Pack. Please refer to the package insert for complete safety information.

> **Note:** Retrieval of the full prescribing information from the Philippine FDA or an originator label (e.g., EMA SmPC or US FDA label) is required before this drug can be assessed in any clinical evaluation context (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire evidence base for Colchicine in P. falciparum malaria consists of in vitro pharmacology studies that tested structural analogues, not Colchicine itself. No clinical trials, no animal in vivo models, and no direct parasite IC₅₀/selectivity data for Colchicine have been generated. The prediction is mechanistically coherent but lacks the minimum preclinical validation threshold required to advance.

> **For context:** The second-ranked TxGNN prediction — Familial Mediterranean Fever (FMF, score 99.38%) — carries L1 evidence, with Colchicine universally recognized as first-line standard of care for FMF since the 1970s (Lancet, 1977; PMID 68234). This confirms that TxGNN's knowledge graph correctly captures Colchicine's pharmacological network, which increases confidence in the model's disease connectivity — but the antimalarial application remains at an early hypothesis stage.

**To proceed, the following is needed:**

- **Direct in vitro efficacy data**: IC₅₀/EC₅₀ for Colchicine against multiple P. falciparum strains, including chloroquine-resistant lines (e.g., Dd2, W2)
- **Selectivity index**: Mammalian cell cytotoxicity (CC₅₀ in human RBCs or HepG2) vs. parasite IC₅₀, to determine whether a therapeutic window exists
- **Life cycle stage mapping**: Identification of which intraerythrocytic stage(s) (ring, trophozoite, schizont) are sensitive to Colchicine
- **In vivo murine malaria model**: Peters' 4-day suppressive test with P. berghei as proof-of-concept
- **Safety data retrieval**: Philippine FDA or originator label for full warnings and contraindications (Data Gap DG001)
- **MOA characterization**: Full DrugBank API query to formally document mechanism of action (Data Gap DG002)
- **Philippines regulatory pathway**: Assess registration requirements with the Philippine FDA, given zero current approvals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

