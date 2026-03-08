#!/usr/bin/env python3
"""Philippine health news fetcher.

Fetches health-related news from Philippine news sources
using RSS feeds and web APIs.

Sources:
- DOH Philippines News
- Philippine Star Health
- Inquirer Health
- Rappler Health
- Manila Bulletin Health

Usage:
    uv run python scripts/fetchers/ph_news.py [--keyword KEYWORD]
    uv run python scripts/fetchers/ph_news.py --from-keywords
"""

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import feedparser
import requests
from bs4 import BeautifulSoup


@dataclass
class NewsArticle:
    """Represents a news article."""

    title: str
    url: str
    source: str
    published: str
    summary: str
    keywords_matched: list[str]
    article_id: str = ""

    def __post_init__(self):
        if not self.article_id:
            # Generate unique ID from URL
            self.article_id = hashlib.md5(self.url.encode()).hexdigest()[:12]


class PhilippineNewsFetcher:
    """Fetches health news from Philippine sources."""

    # RSS feeds for Philippine news sources
    RSS_FEEDS = {
        "doh": "https://doh.gov.ph/press-releases/feed",
        "philstar_health": "https://www.philstar.com/rss/lifestyle/health-and-family",
        "inquirer_health": "https://newsinfo.inquirer.net/category/inquirer-health/feed",
        "rappler": "https://www.rappler.com/section/life-and-style/health-and-fitness/feed",
        "mb_health": "https://mb.com.ph/category/lifestyle/health/feed",
    }

    # Backup: Google News search for Philippines health news
    GOOGLE_NEWS_URL = "https://news.google.com/rss/search?q={query}+site:ph&hl=en-PH&gl=PH&ceid=PH:en"

    def __init__(self, timeout: int = 30):
        """Initialize the fetcher.

        Args:
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; PhTxGNN/1.0; Health News Monitor)"
        })

    def fetch_rss(self, feed_url: str, source_name: str) -> list[NewsArticle]:
        """Fetch articles from an RSS feed.

        Args:
            feed_url: RSS feed URL
            source_name: Name of the news source

        Returns:
            List of NewsArticle objects
        """
        articles = []

        try:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:20]:  # Limit to recent articles
                article = NewsArticle(
                    title=entry.get("title", ""),
                    url=entry.get("link", ""),
                    source=source_name,
                    published=entry.get("published", entry.get("updated", "")),
                    summary=self._clean_html(entry.get("summary", entry.get("description", ""))),
                    keywords_matched=[],
                )
                articles.append(article)

        except Exception as e:
            print(f"Error fetching {source_name}: {e}")

        return articles

    def fetch_all_feeds(self) -> list[NewsArticle]:
        """Fetch articles from all configured RSS feeds.

        Returns:
            List of NewsArticle objects
        """
        all_articles = []

        for source, url in self.RSS_FEEDS.items():
            print(f"Fetching from {source}...", end=" ")
            articles = self.fetch_rss(url, source)
            print(f"Found {len(articles)} articles")
            all_articles.extend(articles)
            time.sleep(0.5)  # Rate limiting

        return all_articles

    def search_google_news(self, query: str) -> list[NewsArticle]:
        """Search Google News for Philippines health articles.

        Args:
            query: Search query

        Returns:
            List of NewsArticle objects
        """
        url = self.GOOGLE_NEWS_URL.format(query=quote(query))
        return self.fetch_rss(url, "google_news")

    def filter_by_keywords(
        self,
        articles: list[NewsArticle],
        keywords: list[str],
    ) -> list[NewsArticle]:
        """Filter articles that contain any of the keywords.

        Args:
            articles: List of articles
            keywords: List of keywords to match

        Returns:
            Filtered list of articles with matched keywords
        """
        filtered = []

        for article in articles:
            text = f"{article.title} {article.summary}".lower()
            matched = []

            for keyword in keywords:
                if keyword.lower() in text:
                    matched.append(keyword)

            if matched:
                article.keywords_matched = matched
                filtered.append(article)

        return filtered

    def _clean_html(self, text: str) -> str:
        """Remove HTML tags from text."""
        if not text:
            return ""
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text(separator=" ", strip=True)[:500]


def load_keywords(filepath: Path) -> list[str]:
    """Load keywords from keywords.json.

    Args:
        filepath: Path to keywords.json

    Returns:
        List of keyword patterns
    """
    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    keywords = []

    # Extract drug patterns
    for drug_data in data.get("drugs", {}).values():
        keywords.extend(drug_data.get("patterns", []))

    # Extract disease patterns
    for disease_data in data.get("diseases", {}).values():
        keywords.extend(disease_data.get("patterns", []))

    return list(set(keywords))


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Philippine health news"
    )
    parser.add_argument("--keyword", type=str, help="Search for specific keyword")
    parser.add_argument("--from-keywords", action="store_true",
                       help="Use keywords from keywords.json")
    parser.add_argument("--limit", type=int, default=50, help="Max articles to return")

    args = parser.parse_args()

    print("=" * 60)
    print("Philippine Health News Fetcher")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent
    fetcher = PhilippineNewsFetcher()

    # Fetch all articles
    print("Fetching from RSS feeds...")
    articles = fetcher.fetch_all_feeds()
    print(f"\nTotal articles fetched: {len(articles)}")

    # Filter by keywords if specified
    if args.keyword:
        keywords = [args.keyword]
        articles = fetcher.filter_by_keywords(articles, keywords)
        print(f"Articles matching '{args.keyword}': {len(articles)}")

    elif args.from_keywords:
        keywords_path = base_dir / "data" / "news" / "keywords.json"
        keywords = load_keywords(keywords_path)

        if not keywords:
            print("No keywords found. Run generate_news_keywords.py first.")
            return

        print(f"Filtering with {len(keywords)} keywords...")
        articles = fetcher.filter_by_keywords(articles, keywords)
        print(f"Articles matching keywords: {len(articles)}")

    # Limit results
    articles = articles[:args.limit]

    # Display results
    print()
    print("-" * 60)
    for i, article in enumerate(articles[:20], 1):
        print(f"{i}. [{article.source}] {article.title[:70]}...")
        print(f"   URL: {article.url}")
        if article.keywords_matched:
            print(f"   Keywords: {', '.join(article.keywords_matched[:5])}")
        print()

    # Save results
    output_dir = base_dir / "data" / "news" / "articles"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"ph_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            [asdict(a) for a in articles],
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
