---
layout: default
title: Drug Repurposing Predictions — Philippines
description: "TxGNN drug repurposing reports for 348 medicines in the Philippine National Formulary, with evidence levels L1–L5 from clinical trials and literature."
last_modified_at: 2026-11-04
nav_order: 1
---

# PhTxGNN Drug Repurposing Reports

Philippine drug repurposing predictions using the TxGNN graph neural network.

{: .warning }
> **Disclaimer**: These predictions are for research purposes only. They do not constitute medical advice and require clinical validation before any clinical application.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Philippines: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines in the [Philippine National Formulary](https://www.doh.gov.ph/philippine-national-formulary) Essential Medicines List (Philippines).

### Philippine medicine data

| Item | Detail |
|------|--------|
| Dataset | Philippine National Formulary Essential Medicines List, 8th Edition (2022) |
| Publisher | Department of Health Philippines, Pharmaceutical Division |
| Source | <https://www.doh.gov.ph/philippine-national-formulary> |
| Nature of the data | A national formulary (essential medicines list), not a registration database: FDA Philippines registration status is not included |
| Update | The list is a fixed edition and is not re-downloaded automatically. Every Monday an automated workflow checks PhilHealth advisories (philhealth.gov.ph/advisories/&lt;year&gt;/) for new formulary notices and opens an issue for review |

Details: [Data Sources]({{ '/sources/' | relative_url }}).

Reports by evidence level:

| Evidence level | Reports | Share |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

10 predicted drug–disease pairs on this site appear on no other of the 30 TxGNN sites.

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |
| [Ketamine](/drugs/ketamine/) | L1 |
| [Diazepam](/drugs/diazepam/) | L2 |
| [Mycophenolate Mofetil](/drugs/mycophenolate-mofetil/) | L2 |
| [Clozapine](/drugs/clozapine/) | L2 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L2 |
| [Prednisolone](/drugs/prednisolone/) | L2 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Interferon Alfa](/drugs/interferon-alfa/) | L5 |
| [Physostigmine](/drugs/physostigmine/) | N/A |

<!-- local-home:end -->

## Overview

PhTxGNN analyzes drugs from the Philippine National Formulary (PNF) using the TxGNN graph neural network to identify potential new therapeutic uses for existing medications.

### Key Statistics

| Metric | Value |
|--------|-------|
| PNF Drugs Analyzed | 529 |
| DrugBank Mapping Rate | 88.7% |
| Predicted New Indications (known uses excluded) | {{ site.data.site_stats.indications }} |
| Drug Reports | {{ site.data.drug_stats.total_drugs }} |
| Unique Diseases | {% assign dz = "" | split: "" %}{% for d in site.drugs %}{% unless d.noindex or d.layout == "id_redirect" %}{% if d.predicted_indications %}{% assign dz = dz | concat: d.predicted_indications %}{% endif %}{% endunless %}{% endfor %}{{ dz | uniq | size }} |

## Data Sources

- **Philippine National Formulary (PNF)**: Essential Medicines List, 8th Edition (2022)
- **TxGNN**: Graph neural network trained on a knowledge graph; predicts drug-disease relationships (known uses already in the graph are excluded)
- **DrugBank**: Drug identifier mapping

## Quick Links

- [FHIR API](/fhir/metadata) - Access predictions via FHIR R4 API
- [SMART App](/smart/launch.html) - Launch SMART on FHIR application

## How It Works

1. **Drug Extraction**: Extract drug names from PNF-EML 2022
2. **DrugBank Mapping**: Map drug names to standard DrugBank identifiers
3. **TxGNN Prediction**: Use the TxGNN graph neural network (score ≥ 0.99) to find potential new indications, excluding known uses
4. **FHIR Export**: Generate FHIR R4 resources for interoperability

## Contact

For questions or feedback, please open an issue on GitHub.

---

*Last updated: {{ page.last_modified_at | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.
