---
layout: default
title: Health News
nav_order: 8
description: "Monitoring health news related to drug repurposing."
permalink: /news/
---

# Health News

<div class="key-takeaway">
Automatic monitoring of Philippine health news related to PhTxGNN drugs and indications.
</div>

---

## Monitored Sources

| Source | Description | Frequency |
|--------|-------------|-----------|
| Philippine News | Health news from local sources | Every 6 hours |
| Google News PH | Philippine health and science news | Every 6 hours |

---

## Categories

### Drug-Related News

News mentioning drugs monitored by PhTxGNN:
- New therapeutic uses
- Clinical trial results
- Regulatory approvals

### Disease-Related News

News about predicted indications:
- Treatment advances
- Scientific discoveries
- New therapies

---

## How It Works

1. **Collection**: RSS feeds and news APIs are monitored every 6 hours
2. **Matching**: News is compared against drug and disease keywords
3. **Relevance**: Relevant news is highlighted
4. **Archive**: History maintained for reference

---

## Latest News

<div class="disclaimer">
News monitoring will be activated after model predictions are run and keywords are generated.
</div>

To configure monitoring:

```bash
# Generate keywords
uv run python scripts/generate_news_keywords.py

# Run news fetcher
uv run python scripts/fetchers/ph_news.py
```

---

## Alerts

You can track new findings through GitHub:

- **Automatic Issues**: Created when new evidence is found
- **Labels**: `auto-detected`, `needs-review`, `clinicaltrials`, `pubmed`

[View Open Issues](https://github.com/yao-care/PhTxGNN/issues?q=is%3Aopen+label%3Aauto-detected){: .btn .btn-primary }

---

## Disclaimer

<div class="disclaimer">
<strong>Notice</strong><br>
News is collected automatically and is not editorially verified. Always verify original sources before making any decisions based on this information.
</div>
