---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using `txgnn-pipeline` for context — this is a PhTxGNN report generation task. Now producing the evaluation report:

---

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line anti-tuberculosis drug, widely used for the treatment and prophylaxis of active and latent tuberculosis infection.
The TxGNN model predicts it may be effective for **Conjunctivitis**, with **1 clinical trial** and **20 publications** currently returned in the evidence search — though the connection is indirect, passing through tuberculosis-related ocular pathology rather than direct conjunctival treatment.
The overall evidence base remains preclinical/mechanistic (L4), and this prediction is best interpreted as a research hypothesis requiring further validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis / Latent Tuberculosis Infection (inferred from drug class and clinical evidence) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank record. Based on well-established pharmacology, Isoniazid is a prodrug activated by the mycobacterial catalase-peroxidase enzyme (KatG) into reactive intermediates that inhibit InhA — an enzyme required for mycobolic acid biosynthesis. This action is bactericidal against *Mycobacterium tuberculosis* and has no direct anti-inflammatory or antimicrobial effect on conjunctival tissue.

The connection to conjunctivitis in the TxGNN prediction follows three indirect pathways: (1) *M. tuberculosis* directly invading conjunctival tissue, causing primary tuberculous conjunctivitis; (2) mycobacterial antigens triggering a Type IV hypersensitivity reaction known as phlyctenular keratoconjunctivitis; (3) BCG immunotherapy-induced immune complex deposition causing ocular manifestations. In all three pathways, mycobacterium serves as the common bridge, and Isoniazid achieves ocular symptom resolution by reducing pathogen or antigen burden — not by acting on the conjunctiva itself.

The high TxGNN score (0.9936) therefore reflects the strength of the knowledge graph connection within this causal chain. It should not be interpreted as support for Isoniazid as a primary treatment for non-tuberculous conjunctivitis. The prediction is mechanistically plausible in a narrow, infection-specific context, but is far from a broad conjunctivitis indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Pragmatic RCT comparing 3HP (rifapentine + isoniazid, 12 weeks) vs 1HP (daily rifapentine + isoniazid, 28 days) for latent tuberculosis infection. Primary endpoint was systemic drug adverse reaction rate. Conjunctivitis is neither a treatment target nor a study endpoint — this trial provides no direct evidence for isoniazid in conjunctivitis treatment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Study | Am Rev Respir Dis | Isoniazid prophylaxis in Alaskan Eskimo children with phlyctenular keratoconjunctivitis — the most directly relevant historical study linking INH to a conjunctivitis-related condition |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Study | Ann Oculist | Local use of isoniazid in treating ocular tuberculosis; provides mechanistic precedent for INH reaching ocular tissue |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis; anti-TB regimen including INH resolved ocular symptoms |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket — illustrates rarity of direct conjunctival TB but confirms INH as standard treatment component |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clin Pediatrics | Unexpected cause of conjunctivitis in an adolescent; context suggests mycobacterial etiology |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | *M. tuberculosis* presenting as chronic red eye / conjunctival TB; treated with standard anti-TB therapy |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva — early case series establishing TB as a direct conjunctival pathogen |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Review of systemic drugs causing ocular adverse effects; notes conjunctivitis and blepharoconjunctivitis associated with various drug classes — contextual background only |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Case Series / Review | Rev Rhum | Review of 26 BCG-induced arthropathy cases with associated conjunctivitis; isoniazid discussed as salvage therapy for refractory BCG complications |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case Report | Rev Rhum | Refractory BCG-induced arthropathy with ocular involvement; isoniazid used as rescue treatment — supports indirect immunological pathway |

---

## Philippines Market Information

No current drug registrations were found for Isoniazid in the Philippines database. This drug has **0 active licenses** on record.

> Note: Isoniazid is a WHO Essential Medicine and is widely available globally for tuberculosis treatment. The absence of records may reflect a data gap in the current regulatory snapshot rather than actual unavailability.

---

## Safety Considerations

Safety data for this report is unavailable — the package insert warnings, contraindications, and drug interaction records were not retrieved in this evidence collection cycle.

> Please refer to the package insert and the WHO/Philippine DOH tuberculosis treatment guidelines for safety information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high score reflects a real knowledge graph connection between Isoniazid and conjunctivitis, but the mechanism is entirely indirect — operating through tuberculosis pathology rather than direct conjunctival action. The sole clinical trial (NCT04094012) is graded C relevance (LTBI regimen comparison, not a conjunctivitis study), and the 20 literature items are predominantly old case reports about tuberculous conjunctivitis treated with anti-TB regimens. There is no controlled evidence supporting Isoniazid as a treatment for conjunctivitis as a primary indication.

**To proceed, the following is needed:**

- **Clarify the exact indication scope**: "Tuberculous conjunctivitis" treated with standard anti-TB therapy (which already has clinical precedent) is fundamentally different from "conjunctivitis" as a standalone indication. The repurposing hypothesis should be refined before any further investment.
- **Retrieve full safety data**: Obtain the TFDA/PhilFDA package insert to extract key warnings, hepatotoxicity risk, peripheral neuropathy, and DDI profile (especially rifampicin co-administration).
- **Systematic literature review**: Commission a formal review specifically on phlyctenular keratoconjunctivitis and BCG-associated ocular disease treated with isoniazid, to establish whether case report evidence is consistent enough to support an observational study design.
- **Confirm Philippines regulatory pathway**: Verify actual market availability via direct PhilFDA inquiry — the 0-license record may be a data gap.
- **MOA documentation**: Retrieve full DrugBank MOA record to complete the mechanistic link analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

