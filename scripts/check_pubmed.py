#!/usr/bin/env python3
"""Check PubMed for literature evidence.

Queries PubMed/NCBI for publications related to drug repurposing candidates.

Usage:
    uv run python scripts/check_pubmed.py [--drug DRUG] [--disease DISEASE]
    uv run python scripts/check_pubmed.py --batch

Examples:
    uv run python scripts/check_pubmed.py --drug metformin --disease cancer
    uv run python scripts/check_pubmed.py --batch --limit 10
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from phtxgnn.collectors.pubmed import PubMedCollector


def check_single(drug: str, disease: str | None = None, api_key: str | None = None) -> dict:
    """Check PubMed for a single drug-disease pair.

    Args:
        drug: Drug name
        disease: Disease name (optional)
        api_key: NCBI API key (optional)

    Returns:
        Search results
    """
    collector = PubMedCollector(max_results=20, api_key=api_key)
    result = collector.search(drug, disease)

    print(f"\nSearching PubMed for: {drug}" + (f" + {disease}" if disease else ""))
    print("-" * 60)

    if not result.success:
        print(f"Error: {result.error_message}")
        return result.to_dict()

    articles = result.data.get("results", [])
    print(f"Found {len(articles)} publications\n")

    for i, article in enumerate(articles[:10], 1):
        authors_str = ", ".join(article["authors"][:3])
        if len(article["authors"]) > 3:
            authors_str += " et al."

        print(f"{i}. {article['title'][:80]}...")
        print(f"   {authors_str} ({article['year']})")
        print(f"   {article['journal']}")
        print(f"   PMID: {article['pmid']} | {article['url']}")

        # Show publication types if relevant
        relevant_types = [pt for pt in article["pub_types"] if "Trial" in pt or "Review" in pt]
        if relevant_types:
            print(f"   Type: {', '.join(relevant_types)}")
        print()

    return result.to_dict()


def check_batch(limit: int = 50, api_key: str | None = None) -> list[dict]:
    """Check PubMed for all repurposing candidates.

    Args:
        limit: Maximum number of candidates to check
        api_key: NCBI API key (optional)

    Returns:
        List of results
    """
    base_dir = Path(__file__).parent.parent
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"Error: Candidates file not found: {candidates_path}")
        print("Please run run_kg_prediction.py first.")
        return []

    # Load candidates
    candidates_df = pd.read_csv(candidates_path)
    print(f"Loaded {len(candidates_df)} repurposing candidates")

    # Get unique drug-disease pairs
    pairs = candidates_df[["ingredient", "potential_indication"]].drop_duplicates()
    pairs = pairs.head(limit)
    print(f"Checking {len(pairs)} unique drug-disease pairs...\n")

    collector = PubMedCollector(max_results=10, api_key=api_key)
    results = []
    total_articles = 0

    for i, row in pairs.iterrows():
        drug = row["ingredient"]
        disease = row["potential_indication"]

        print(f"[{len(results)+1}/{len(pairs)}] {drug} + {disease}...", end=" ")

        result = collector.search(drug, disease)
        results.append(result.to_dict())

        if result.success:
            articles = result.data.get("results", [])
            n_articles = len(articles)
            total_articles += n_articles
            print(f"Found {n_articles} articles")
        else:
            print(f"Error: {result.error_message}")

        # Rate limiting (NCBI allows 3 req/sec without API key, 10 with)
        time.sleep(0.35 if api_key else 0.5)

    print(f"\nTotal: {total_articles} articles found across {len(pairs)} queries")

    # Save results
    output_dir = base_dir / "data" / "evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"pubmed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)

    print(f"\nResults saved to: {output_file}")

    # Generate summary
    summary = generate_evidence_summary(results)
    summary_file = output_dir / f"pubmed_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"Summary saved to: {summary_file}")

    return results


def generate_evidence_summary(results: list[dict]) -> dict:
    """Generate a summary of PubMed evidence.

    Args:
        results: List of search results

    Returns:
        Summary dictionary
    """
    summary = {
        "total_queries": len(results),
        "successful_queries": sum(1 for r in results if r["success"]),
        "total_articles": 0,
        "queries_with_evidence": 0,
        "publication_types": {},
        "top_journals": {},
        "year_distribution": {},
    }

    for result in results:
        if not result["success"]:
            continue

        articles = result["data"].get("results", [])
        if articles:
            summary["queries_with_evidence"] += 1
            summary["total_articles"] += len(articles)

            for article in articles:
                # Count publication types
                for pt in article.get("pub_types", []):
                    summary["publication_types"][pt] = summary["publication_types"].get(pt, 0) + 1

                # Count journals
                journal = article.get("journal", "Unknown")
                summary["top_journals"][journal] = summary["top_journals"].get(journal, 0) + 1

                # Count years
                year = article.get("year", "Unknown")
                summary["year_distribution"][year] = summary["year_distribution"].get(year, 0) + 1

    # Sort and limit
    summary["top_journals"] = dict(
        sorted(summary["top_journals"].items(), key=lambda x: -x[1])[:20]
    )
    summary["publication_types"] = dict(
        sorted(summary["publication_types"].items(), key=lambda x: -x[1])[:20]
    )

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Check PubMed for literature evidence"
    )
    parser.add_argument("--drug", type=str, help="Drug name to search")
    parser.add_argument("--disease", type=str, help="Disease name to search")
    parser.add_argument("--batch", action="store_true", help="Check all repurposing candidates")
    parser.add_argument("--limit", type=int, default=50, help="Max candidates to check in batch mode")
    parser.add_argument("--api-key", type=str, help="NCBI API key for higher rate limits")

    args = parser.parse_args()

    # Check for API key in environment
    api_key = args.api_key or os.environ.get("NCBI_API_KEY")

    print("=" * 60)
    print("PubMed Literature Evidence Checker")
    print("=" * 60)

    if api_key:
        print("Using NCBI API key for higher rate limits")
    else:
        print("No API key provided - using default rate limits")
        print("Set NCBI_API_KEY environment variable for faster queries")

    if args.batch:
        check_batch(args.limit, api_key)
    elif args.drug:
        check_single(args.drug, args.disease, api_key)
    else:
        # Demo mode
        print("\nDemo mode: Searching for 'metformin + cancer'")
        check_single("metformin", "cancer", api_key)


if __name__ == "__main__":
    main()
