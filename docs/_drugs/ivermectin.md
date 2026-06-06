---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 9
---

# Ivermectin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using `txgnn-pipeline` skill to orient context. The skill confirms this is a report generation task within the TxGNN pipeline. Now generating the evaluation report based on the Evidence Pack.

---

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is a broad-spectrum antiparasitic agent with established efficacy against strongyloidiasis, onchocerciasis, and scabies, acting by paralysing invertebrate nerve and muscle cells. The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis** with a score of 99.95%, yet this is supported by **no clinical trials** and **no published literature** on this specific indication. The mechanistic link is biologically weak, and the high prediction score is most likely an artifact of knowledge graph clustering rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parasitic infections (strongyloidiasis, onchocerciasis, scabies) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the sources queried. Based on established pharmacology, Ivermectin is a macrocyclic lactone antiparasitic that works by selectively binding to and opening glutamate-gated chloride (GluCl) ion channels found exclusively in invertebrate nerve and muscle cells. This causes hyperpolarisation, paralysis, and death of susceptible parasites (nematodes, arthropods). Mammals, including humans, are largely protected due to the blood-brain barrier and the absence of GluCl channels peripherally.

Vulvovaginal candidiasis is a fungal infection caused primarily by *Candida albicans*. Fungi lack the GluCl channel target that Ivermectin acts upon. Some in vitro studies have reported a weak inhibitory effect of Ivermectin on *Candida* biofilms—hypothesised mechanisms include membrane permeability disruption or efflux pump inhibition—but these findings have not been validated in any human clinical study. The mechanistic distance between Ivermectin's established antiparasitic action and antifungal activity is substantial.

A critical red flag in this Evidence Pack is that three distinct candidiasis-related indications (congenital candidiasis, *Candida glabrata*, and neonatal candidiasis) all receive an **identical** TxGNN score of 99.25%, strongly indicating that the model is reflecting knowledge graph node clustering rather than independent pharmacological evaluation. The top score for vulvovaginal candidiasis (99.95%) should be interpreted with the same caution. From the 9 predicted indications in this pack, the **anogenital HPV infection** (rank 3, L4) presents the most biologically plausible mechanistic link—Ivermectin has been proposed to inhibit importin α/β1-mediated nuclear import, which could impair viral protein trafficking—and warrants separate investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ivermectin in vulvovaginal candidiasis.

---

## Literature Evidence

Currently no related literature available for Ivermectin in vulvovaginal candidiasis.

---

## Philippines Market Information

Ivermectin is currently **not marketed** in the Philippines. There are no registered product licenses on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No registrations on file |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams:** Key safety warnings and contraindications for Ivermectin were not retrievable from available data sources at the time of this report (data gap DG001). Particular attention should be given to contraindications in pregnant women, children under 15 kg, and patients with compromised blood-brain barriers (e.g., neonates, patients with meningitis), as CNS toxicity is a known concern in these groups. Drug interaction data was also not found in the queried databases.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for vulvovaginal candidiasis is almost certainly driven by knowledge graph clustering artifacts—*Candida*-related nodes are densely interconnected in the graph, producing systematically inflated scores—rather than a real pharmacological relationship. Ivermectin's well-characterised mechanism targets invertebrate GluCl channels that are entirely absent in fungal pathogens, and no clinical or published literature evidence supports this repurposing direction.

**To proceed with any further evaluation, the following is needed:**

- **MOA verification:** Retrieve full DrugBank entry (DB00602) to document the confirmed mechanism of action and any secondary pharmacological activities
- **Philippines FDA safety data:** Download and parse the package insert (if available via FDA Philippines portal) for warnings, contraindications, and drug interactions
- **Antifungal activity validation:** Commission or identify in vitro studies assessing Ivermectin MIC against *C. albicans* biofilms before any clinical consideration
- **KG bias audit:** Flag the seven candidiasis-cluster predictions (ranks 1–2, 4–9) as likely KG artifacts; remove from active repurposing pipeline pending graph refinement
- **Separate HPV track:** Anogenital HPV infection (rank 3, L4, "Research Question") has a distinct and biologically plausible mechanism and should be evaluated independently with a dedicated evidence search

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

