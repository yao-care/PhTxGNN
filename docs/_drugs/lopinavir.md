---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lopinavir is an antiretroviral protease inhibitor, originally developed as a component of the Lopinavir/Ritonavir combination (Kaletra) for the treatment of HIV infection and AIDS.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (Feline AIDS)**,
with **no clinical trials** and **no published literature** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection / AIDS (antiretroviral drug class; not registered in Philippines) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological classification, Lopinavir is a peptidomimetic HIV-1 and HIV-2 protease inhibitor. It works by competitively binding the active site of the HIV aspartyl protease enzyme, blocking the cleavage of viral polyprotein precursors (Gag and Gag-Pol) into the functional proteins required for viral maturation. Clinically, it is always co-administered with low-dose ritonavir, which acts as a pharmacokinetic booster by inhibiting CYP3A4-mediated metabolism of Lopinavir.

Feline Acquired Immunodeficiency Syndrome is caused by Feline Immunodeficiency Virus (FIV), which — like HIV — belongs to the Lentivirus genus. All lentiviruses share a protease-dependent maturation cycle, and the TxGNN knowledge graph likely identified this taxonomic and topological proximity as the basis for the high prediction score (0.9990).

However, the structural homology between FIV protease and HIV protease is limited; the binding pockets differ at key residues where Lopinavir makes critical contacts, and no published study has demonstrated inhibitory activity of Lopinavir against FIV protease. Moreover, this is a **veterinary indication** — cats are not a target population for human drug repurposing pipelines. The high TxGNN score almost certainly reflects graph topology proximity rather than translatable biological activity, and should be treated as a likely false-positive for human clinical purposes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Lopinavir is not currently registered with the Philippines Food and Drug Administration. There are zero product licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication — feline acquired immunodeficiency syndrome — is a veterinary condition with no direct human clinical repurposing value, and is unsupported by any clinical trial or published literature. The prediction is likely a knowledge-graph topological artifact rather than a biologically actionable signal.

**Supplementary note on Rank 2 (Simian Immunodeficiency Virus Infection, L4):**
The second-ranked prediction carries more scientific grounding: three non-human primate (NHP) studies demonstrate that Lopinavir/Ritonavir HAART suppresses viral replication in macaques infected with SIV or SHIV chimeric viruses. While this remains preclinical evidence and not a human indication, it does confirm that Lopinavir's protease inhibition mechanism is active across lentiviral species boundaries under controlled conditions. If the research question is "can Lopinavir serve as a scaffold or comparator in primate HIV-model research," the answer is supported by existing NHP data.

**To proceed on any future direction, the following is needed:**

- **MOA data** — Retrieve full mechanism of action from DrugBank (DB01601) to enable formal mechanistic link analysis
- **Package insert warnings and contraindications** — Download and parse the TFDA or originator prescribing information to complete safety evaluation (currently Blocking gap DG001)
- **Reframe the research question** — Confirm whether the goal is human drug repurposing (in which case feline/simian indications are out of scope) or preclinical model validation (in which case rank 2 NHP data becomes the relevant starting point)
- **Philippines registration pathway** — If a human HIV-adjacent indication is pursued, assess whether co-packaging with ritonavir would be required for Philippines regulatory submission, as Lopinavir is not approved as monotherapy anywhere globally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

