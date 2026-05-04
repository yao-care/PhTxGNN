---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

Amoxicillin is a broad-spectrum beta-lactam antibiotic with well-established activity against a wide range of bacterial pathogens, including *Helicobacter pylori* as part of standard eradication triple therapy.
The TxGNN model predicts it may be effective for **Monoclonal Gammopathy** — most specifically the immunoproliferative small intestinal disease (IPSID / α-heavy chain disease) subtype — with **1 clinical trial** and **11 publications** identified in support.
Among the 8 predicted indications in this multi-indication pack, monoclonal gammopathy carries the strongest evidence (L3) and the only actionable recommendation ("Proceed with Guardrails"), grounded in a recognised antibiotic-responsive disease mechanism codified in the WHO tumour classification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (penicillin-class antibiotic) |
| Predicted New Indication | Monoclonal Gammopathy (IPSID subtype) |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack (Data Gap DG002). Based on established pharmacology, Amoxicillin is an aminopenicillin that inhibits bacterial cell wall synthesis by covalently binding penicillin-binding proteins (PBPs), leading to bacteriolysis. Its reliable activity against *Helicobacter pylori* makes it a cornerstone of H. pylori eradication triple therapy (e.g., amoxicillin + clarithromycin + proton pump inhibitor), and this property forms the primary mechanistic bridge to its potential utility in monoclonal gammopathy.

Immunoproliferative Small Intestinal Disease (IPSID) — also known as α-heavy chain disease or Mediterranean lymphoma — is an extranodal marginal zone B-cell lymphoma (MALT-type) of the small intestine, driven by chronic mucosal infection, particularly *Campylobacter jejuni* and potentially *H. pylori*. Sustained bacterial antigenic stimulation promotes clonal proliferation of IgA-secreting B cells that produce truncated, non-functional α-heavy chains. Critically, in **Stage A (early) disease**, prolonged antibiotic regimens — including ampicillin, tetracycline, and amoxicillin-containing H. pylori eradication protocols — can induce durable complete remission without cytotoxic chemotherapy. This is not experimental: the strategy is explicitly recognised in the WHO Classification of Tumours of Haematopoietic and Lymphoid Tissues as a standard first-line approach for Stage A IPSID.

It is essential to emphasise that this rationale applies **exclusively** to the IPSID subtype of monoclonal gammopathy. Other subtypes — MGUS, multiple myeloma, Waldenström macroglobulinaemia, and light chain amyloidosis — have entirely distinct pathophysiology unrelated to bacterial infection, and there is no mechanistic or clinical basis for antibiotic therapy in those conditions. The high TxGNN score (99.22%) most likely reflects the model's knowledge graph linking the "antibiotic" drug class node to the "monoclonal gammopathy" disease node via the IPSID subtype relationship, rather than a generalised signal across all subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | N/A | Terminated | 351 | Oral empirical antibiotic therapy for febrile neutropenia in low-risk cancer patients: amoxicillin + ciprofloxacin vs. moxifloxacin monotherapy. Not a direct treatment trial for monoclonal gammopathy; supports the safety profile of amoxicillin in haematological malignancy patients and establishes tolerability in an immunocompromised oncology context. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1996 | Case Series + Narrative Review | *Internal Medicine* (Tokyo) | Mediterranean lymphoma (IPSID) treated with antibiotics; complete remission achieved with antibiotic monotherapy, supporting the antibiotic-first strategy in early-stage IPSID — directly relevant to repurposing rationale |
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Report | *Lancet* | Regression of IPSID following *H. pylori* eradication; demonstrates that eliminating the bacterial driver reverses B-cell clonal proliferation and tumour regression — key mechanistic evidence |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Report | *J Gastrointestinal Cancer* | Regression of IPSID after *H. pylori* eradication in a 20-year-old male; corroborates the infection-driven pathogenesis and antibiotic responsiveness |
| [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) | 2005 | Case Report | *Arch Pathol Lab Med* | Nonsecretory variant of IPSID with pathologic and molecular characterisation; broadens disease spectrum understanding, relevant for diagnosis and treatment staging |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case Report | *Front Public Health* | Disseminated nocardiosis in a patient with macroglobulinaemia; isolated strain susceptible to amoxicillin/clavulanic acid — confirms activity and tolerability in plasma cell dyscrasia patients |
| [22092390](https://pubmed.ncbi.nlm.nih.gov/22092390/) | 2012 | Retrospective Comparative Study | *J Oral Pathol Med* | Bisphosphonate-related osteonecrosis of the jaw (BRONJ) in multiple myeloma vs. breast cancer; amoxicillin used as adjunct antibiotic in the standardised management protocol — safety reference in myeloma patients |
| [20015614](https://pubmed.ncbi.nlm.nih.gov/20015614/) | 2010 | Retrospective Case Series | *Int J Oral Maxillofac Surg* | Surgical management of bisphosphonate-induced ONJ not responding to conservative treatment; amoxicillin incorporated in peri-operative antibiotic coverage — additional safety evidence in haematological malignancy setting |
| [18639371](https://pubmed.ncbi.nlm.nih.gov/18639371/) | 2009 | Retrospective Cohort | *Br J Oral Maxillofac Surg* | Bisphosphonate-associated ONJ following therapy discontinuation; amoxicillin part of supportive infection management in myeloma/metastatic cancer patients |
| [21908119](https://pubmed.ncbi.nlm.nih.gov/21908119/) | 2011 | Case Report | *Médecine et Maladies Infectieuses* | Pneumonia caused by *Rothia dentocariosa* in a haematology patient; indirect evidence of amoxicillin use in immunocompromised haematological malignancy patients |
| [20513124](https://pubmed.ncbi.nlm.nih.gov/20513124/) | 2010 | Retrospective Diagnostic Study | *Am J Hematol* | High false-positive rate of Aspergillus galactomannan test in multiple myeloma; antibiotic co-administration (including beta-lactams) noted as a confounding factor — contextualises antibiotic use in myeloma management |

---

## Philippines Market Information

Amoxicillin currently has **no registered products** in the FDA Philippines database according to this evidence pack.

> **Important caveat**: Amoxicillin is one of the most widely distributed generic antibiotics globally and is included on the WHO Essential Medicines List. The absence of registration records here likely reflects a data gap in the current dataset rather than actual market absence in the Philippines. Independent verification with the FDA Philippines online registry (https://www.fda.gov.ph) is strongly recommended before drawing conclusions about market availability.

---

## Safety Considerations

Safety data was not available in this evidence pack (DG001: Philippine FDA labelling data gap). Please refer to the package insert for complete warnings, contraindications, and precautions.

Based on established class-level knowledge for aminopenicillins, the following are known considerations for clinical reference:

- **Hypersensitivity**: IgE-mediated anaphylaxis and delayed hypersensitivity reactions are the most serious class risks; cross-reactivity with other beta-lactams applies
- **Superinfection**: Prolonged courses may lead to *Clostridioides difficile*-associated diarrhoea (CDAD), which is particularly relevant in the IPSID indication where long-term antibiotic treatment is required
- **Maculopapular rash**: Significantly elevated incidence in patients with infectious mononucleosis, lymphocytic leukaemia, or concurrent allopurinol use — relevant in haematological malignancy patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The IPSID (Stage A) subtype of monoclonal gammopathy has a well-characterised infection-driven pathogenesis in which amoxicillin-based antibiotic eradication of *H. pylori* / *C. jejuni* is a recognised, WHO-endorsed first-line treatment capable of inducing complete remission without chemotherapy. Observational case series and mechanistic literature (L3) support biological plausibility and provide clinical precedent, though no randomised controlled trials evaluating amoxicillin specifically for IPSID have been conducted.

**To proceed, the following is needed:**

- **Subtype confirmation is mandatory**: Restrict any clinical application strictly to IPSID (Stage A); MGUS, multiple myeloma, and Waldenström macroglobulinaemia subtypes do not benefit from antibiotics and should be excluded from this repurposing pathway
- **Retrieve complete MOA data** from DrugBank (DG002 remediation) to formalise mechanism documentation
- **Obtain Philippine FDA package insert** (DG001 remediation) for complete local warnings, contraindications, and dosage guidance
- **Pathogen prevalence assessment**: Evaluate regional prevalence of *H. pylori* and *C. jejuni* in the Philippine target population, as treatment success rates depend directly on pathogen eradication rates
- **Prospective registry or pragmatic trial**: Consider a registry study enrolling Stage A IPSID patients in the Philippines to document antibiotic response rates with locally available amoxicillin-based regimens
- **Endoscopy and staging protocol**: Confirm that local diagnostic capacity (upper GI endoscopy, immunohistochemistry, α-heavy chain immunofixation) is available to accurately stage IPSID before initiating antibiotic-only therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

