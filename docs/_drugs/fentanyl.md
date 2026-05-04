---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic μ-opioid receptor agonist, widely used clinically for pain management and anesthesia.
The TxGNN model assigns it a prediction score of **99.46%** for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)** — however, **no clinical trials or published literature** support this indication, and mechanistic analysis suggests Fentanyl's known pharmacology would likely **worsen** rather than treat NSIAD.
Both top predictions in this Evidence Pack are currently rated **Hold (L5)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid analgesia / Pain management |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Fentanyl is not available in the current Evidence Pack. Based on well-established pharmacology, Fentanyl is a potent synthetic full agonist at the μ-opioid receptor (MOR). Beyond its analgesic effects, it has documented neuroendocrine activity — including promotion of antidiuretic hormone (ADH/vasopressin) release from the posterior pituitary, producing a physiological state resembling SIADH (Syndrome of Inappropriate Antidiuretic Hormone Secretion).

NSIAD (Nephrogenic Syndrome of Inappropriate Antidiuresis) arises from gain-of-function mutations in the *AVPR2* gene, causing constitutive V2 vasopressin receptor activation independent of circulating ADH levels. The result is persistent antidiuretic signaling, renal water retention, and dilutional hyponatremia. Unlike SIADH, the problem in NSIAD is not elevated ADH — the receptor is simply locked "on" regardless of hormonal input.

Because Fentanyl promotes ADH secretion, administering it to an NSIAD patient would further amplify antidiuretic tone in a system already constitutively overactive. The high TxGNN score (99.46%) likely reflects pattern-level co-occurrences within the knowledge graph linking opioid signaling to fluid and electrolyte pathways — but the pharmacological directionality is counterproductive. No known mechanism supports Fentanyl as a therapeutic agent for NSIAD; mechanistic reasoning predicts harm rather than benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fentanyl in Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Literature Evidence

Currently no related literature available for Fentanyl in Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Philippines Market Information

Fentanyl currently has **no registered products** with the Philippine FDA (`市場狀態: 未上市`). No license authorization records are available for review. This absence of local registration also means that no locally approved indication text, dosage form data, or Philippine-specific prescribing information is on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Although Philippine FDA-specific warning data is not available in this Evidence Pack, Fentanyl's general safety profile is well characterised in international literature. Key concerns include: **respiratory depression** (potentially fatal, especially in opioid-naïve individuals), **central nervous system depression**, **opioid dependence and misuse potential**, and **risk of overdose**. These properties are especially relevant in evaluating any off-label repurposing proposal, as chronic use in conditions such as NSIAD or Tourette syndrome would require long-term exposure to a high-addiction-liability opioid agonist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high numerical score for Fentanyl in NSIAD reflects knowledge-graph association patterns, but mechanistic analysis reveals a direct pharmacological contradiction: μ-opioid receptor activation promotes ADH release, which would be expected to exacerbate the core pathophysiology of NSIAD (constitutive V2 receptor activation driving hyponatremia), not correct it. Zero clinical or preclinical evidence exists to offset this concern.

The second-ranked prediction, **Tourette Syndrome** (TxGNN score: 99.05%), is similarly untenable: opioid research in Tourette has focused on receptor **antagonists** (naltrexone, naloxone) — not agonists. Fentanyl's strong agonist profile, high addiction liability, and respiratory depression risk render it pharmacologically and clinically inappropriate for chronic neuropsychiatric treatment.

**To proceed, the following is needed:**

- A biologically plausible mechanistic hypothesis explaining how μ-opioid agonism could reduce constitutive V2 receptor activity or correct hyponatremia in NSIAD
- Preclinical data from *AVPR2* gain-of-function animal models demonstrating any therapeutic signal
- Retrieval of Philippine FDA registration records and full package insert (warnings, contraindications, drug interactions) to enable a complete safety evaluation
- Confirmation of Fentanyl's approved indications via DrugBank API to properly characterise the starting point for any repurposing rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

