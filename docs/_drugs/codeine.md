---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Codeine: From Opioid Analgesia to Nasal Cavity Disease

## One-Sentence Summary

Codeine is a well-established opioid analgesic and antitussive agent, widely used for mild-to-moderate pain relief and cough suppression via central μ-opioid receptor activation. The TxGNN model ranks **Nasal Cavity Disease** as its top predicted new indication (score 99.93%), alongside Acute Laryngopharyngitis, Trigeminal Autonomic Cephalalgia, and Allergic Urticaria. However, evidence review across all four predictions reveals a consistent pattern of **reverse (adverse) associations** — Codeine appears in the relevant literature as a *cause of* or *diagnostic probe for* these conditions rather than a therapeutic agent — with no supporting clinical trials and a uniform **Hold** recommendation across all indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid analgesia and antitussive (cough suppression) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Codeine is a naturally occurring opioid alkaloid and prodrug that is demethylated to morphine via CYP2D6, exerting its effects primarily through **μ-opioid receptor (MOR) agonism** in the central nervous system. Its antitussive action is mediated through opioid receptors in the nucleus tractus solitarius (NTS), while analgesia is achieved via modulation of pain signaling in the periaqueductal gray, spinal cord, and limbic system. It has no known anti-inflammatory, antihistaminic, or direct ENT disease-modifying mechanisms.

The TxGNN model's high prediction scores for all four indications — nasal cavity disease, acute laryngopharyngitis, trigeminal autonomic cephalalgia, and allergic urticaria — appear to reflect **knowledge graph co-occurrence bias rather than genuine therapeutic potential**. In each case, Codeine surfaces in the biomedical literature not as a treatment but through adverse or instrumental associations: opioid powder inhalation causing ischemic mucosal necrosis and rhinolithiasis ("opioma") in nasal cavity disease; suppression of protective cough reflexes raising concern in laryngopharyngitis; well-documented risk as a driver of medication overuse headache (MOH) in cluster headache, with international guidelines explicitly recommending against opioid use in trigeminal autonomic cephalalgias (TACs); and Codeine's direct, IgE-independent mast cell degranulation property, which makes it a standard positive control reagent in urticaria skin testing — not a therapeutic agent.

This case illustrates a critical limitation of knowledge-graph-based prediction models: high co-occurrence frequency in the biomedical literature does not distinguish between therapeutic associations and adverse/diagnostic ones. All four predicted indications are assessed as **false positives**, and the high TxGNN scores reflect the richness of Codeine's adverse and diagnostic literature rather than any repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the four predicted indications (nasal cavity disease, acute laryngopharyngitis, trigeminal autonomic cephalalgia, or allergic urticaria).

---

## Literature Evidence

### Nasal Cavity Disease (Rank 1 — 2 publications)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case Report | The Laryngoscope | Intranasal abuse of hydrocodone-acetaminophen causing ischemic necrosis of the nasal cavity and pharynx — documents **opioid-induced nasal damage**, not a therapeutic benefit |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case Report | Ear, Nose & Throat Journal | Rhinolithiasis ("opioma") formed around an impacted nasal foreign body of hardened codeine and opium — **adverse/abuse association**, not treatment |

> ⚠️ Both publications document Codeine as a *cause* of nasal cavity pathology. There is no positive therapeutic signal for this indication.

---

### Allergic Urticaria (Rank 4 — highest literature volume: 15 publications, selected below)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16461991](https://pubmed.ncbi.nlm.nih.gov/16461991/) | 2006 | Review | Clin Rev Allergy Immunol | Opiates including codeine directly activate mast cells via non-IgE pathways to induce urticaria — **Codeine is identified as a causative agent** |
| [3711548](https://pubmed.ncbi.nlm.nih.gov/3711548/) | 1986 | Clinical Study | J Allergy Clin Immunol | Intradermal codeine used to characterize urticaria-prone patients; urticaria-prone subjects showed heightened mast cell sensitivity — **Codeine used as a diagnostic provocation tool** |
| [17210040](https://pubmed.ncbi.nlm.nih.gov/17210040/) | 2007 | Controlled Clinical Study | Clin Exp Allergy | Codeine intradermal skin testing to evaluate IgE-mediated allergic disorders — **Codeine as diagnostic positive control**, not therapeutic agent |
| [17064652](https://pubmed.ncbi.nlm.nih.gov/17064652/) | 2006 | Review | Allergologia et Immunopathologia | Opioids cause adverse reactions in urticaria and asthma patients; increasing opioid use raises clinical concern — **Codeine is a risk factor** for urticaria patients |
| [8792922](https://pubmed.ncbi.nlm.nih.gov/8792922/) | 1996 | RCT | Allergy | Codeine used as a standard wheal-and-flare provocation model to test antihistamine (mizolastine) efficacy — **Codeine as a research pharmacological probe**, not under investigation as treatment |
| [2941218](https://pubmed.ncbi.nlm.nih.gov/2941218/) | 1986 | Case Report | Contact Dermatitis | Urticarial rash from delayed-type allergy to orally administered codeine — **Codeine-induced urticaria** case |

> ⚠️ The high publication count (15 papers) reflects Codeine's longstanding role as a **standard mast cell degranulation agent** in allergy research and skin testing. This is the opposite of a therapeutic signal.

---

### Trigeminal Autonomic Cephalalgia (Rank 3 — selected from 5 publications)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18563291](https://pubmed.ncbi.nlm.nih.gov/18563291/) | 2008 | Case Report | J Headache Pain | Codeine phosphate used as an **exceptional/last-resort** treatment in a cluster headache patient with Brugada ECG pattern when standard sodium-channel-blocking therapies were contraindicated — single case only, not generalizable |
| [19109043](https://pubmed.ncbi.nlm.nih.gov/19109043/) | 2009 | Case Series | Eur J Paediatr Neurol | Cluster headache characteristics in children — **does not support opioid therapy** |
| [41428068](https://pubmed.ncbi.nlm.nih.gov/41428068/) | 2026 | Case Report | Ann Biol Clin | Cocaine misuse in a cluster headache patient highlights high substance abuse risk in this population — **safety concern**, not therapeutic evidence |

> ⚠️ International Headache Society (IHS) and EHMTI guidelines explicitly advise **against** opioid use in TACs due to MOH risk and lack of efficacy. PMID 18563291 is a single exceptional case under specific contraindication circumstances.

---

## Philippines Market Information

Codeine (DrugBank: DB00318) currently has **no marketing authorization** registered with the FDA Philippines. There are no active, cancelled, or historical license records available.

---

## Safety Considerations

Please refer to the package insert for full safety information, as local prescribing data and TFDA monograph warnings are not yet available in this evidence pack (Data Gap DG001 — Blocking severity).

Based on evidence surfaced during this repurposing review, the following adverse associations are documented and directly relevant to the predicted indications:

- **Nasal Cavity Harm**: Long-term intranasal opioid abuse causes ischemic mucosal necrosis, septal perforation, and rhinolith formation ("opioma").
- **Mast Cell Degranulation**: Codeine triggers direct, non-IgE-mediated histamine release from cutaneous mast cells, causing urticaria and potentially anaphylactoid reactions. Codeine is a well-recognized **urticaria-inducing agent** and should be used with caution in atopic or urticaria-prone patients.
- **Medication Overuse Headache (MOH)**: Codeine is among the highest-risk analgesics for MOH in headache patients, particularly those with primary headache disorders including cluster headache (TAC).
- **Cough Reflex Suppression**: Opioid-induced suppression of productive cough in infectious airway conditions (e.g., laryngopharyngitis) may impair natural mucociliary clearance.

---

## Conclusion and Next Steps

**Decision: Hold** (applicable to all four predicted indications)

**Rationale:**
All four TxGNN top-ranked predictions for Codeine represent **reverse (adverse) or diagnostic associations**, not therapeutic opportunities. The knowledge graph has captured co-occurrence patterns in which Codeine is associated with these conditions as a causative agent, a risk factor, or a pharmacological research tool — not as a repurposable treatment. Proceeding with any of these indications would carry significant patient safety risks with no mechanistic or clinical trial support.

**To proceed with a valid repurposing evaluation for Codeine, the following is needed:**

- **Resolve DG001 (Blocking)**: Obtain Philippines FDA package insert PDF and extract full warnings, contraindications, and approved indications for safety baseline assessment
- **Resolve DG002 (High)**: Query DrugBank API for complete MOA data, receptor binding profiles, and pharmacokinetic parameters
- **Direction-Aware Model Re-query**: Re-interrogate TxGNN or supplementary models with filters that exclude adverse-direction associations, distinguishing "drug causes disease" from "drug treats disease" co-occurrences
- **Identify positive-direction candidates**: Explore Codeine's antitussive mechanism in the context of conditions with pathological cough (e.g., chronic refractory cough, pertussis) where the mechanistic direction is genuinely therapeutic
- **Pharmacogenomic profiling**: Given CYP2D6 variability in Southeast Asian populations, any future positive indication would require a population-specific metabolizer frequency assessment before Philippines-specific development planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

