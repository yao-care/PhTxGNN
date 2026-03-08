#!/usr/bin/env python3
"""Batch collect evidence bundles for all repurposing candidates.

Collects evidence from multiple sources (ClinicalTrials.gov, PubMed)
for each drug-indication pair and bundles them together.

Usage:
    uv run python scripts/batch_collect_bundles.py [--limit N]

Output:
    data/evidence/bundles/{drug}-{indication}.json
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

from phtxgnn.collectors.clinicaltrials import ClinicalTrialsCollector
from phtxgnn.collectors.pubmed import PubMedCollector


def collect_evidence_bundle(
    drug: str,
    disease: str,
    ct_collector: ClinicalTrialsCollector,
    pubmed_collector: PubMedCollector,
) -> dict:
    """Collect evidence bundle for a drug-disease pair.

    Args:
        drug: Drug name
        disease: Disease/indication name
        ct_collector: ClinicalTrials.gov collector
        pubmed_collector: PubMed collector

    Returns:
        Evidence bundle dictionary
    """
    bundle = {
        "drug": drug,
        "disease": disease,
        "collected_at": datetime.now().isoformat(),
        "sources": {},
        "summary": {
            "total_trials": 0,
            "total_publications": 0,
            "evidence_level": "L5",  # Default: expert opinion / knowledge graph
        },
    }

    # Collect from ClinicalTrials.gov
    try:
        ct_result = ct_collector.search(drug, disease)
        if ct_result.success:
            trials = ct_result.data or []
            bundle["sources"]["clinicaltrials"] = {
                "success": True,
                "count": len(trials),
                "data": trials[:10],  # Limit stored data
            }
            bundle["summary"]["total_trials"] = len(trials)

            # Upgrade evidence level based on trials
            if any(t.get("phase", "").lower() in ["phase 3", "phase 4"] for t in trials):
                bundle["summary"]["evidence_level"] = "L2"  # RCT evidence
            elif any(t.get("phase", "").lower() in ["phase 1", "phase 2"] for t in trials):
                bundle["summary"]["evidence_level"] = "L3"  # Early phase trials
        else:
            bundle["sources"]["clinicaltrials"] = {
                "success": False,
                "error": ct_result.error_message,
            }
    except Exception as e:
        bundle["sources"]["clinicaltrials"] = {"success": False, "error": str(e)}

    # Rate limiting
    time.sleep(0.3)

    # Collect from PubMed
    try:
        pubmed_result = pubmed_collector.search(drug, disease)
        if pubmed_result.success:
            articles = pubmed_result.data.get("results", [])
            bundle["sources"]["pubmed"] = {
                "success": True,
                "count": len(articles),
                "data": articles[:10],  # Limit stored data
            }
            bundle["summary"]["total_publications"] = len(articles)

            # Check for systematic reviews / meta-analyses
            has_sr = any(
                "Systematic Review" in a.get("pub_types", []) or
                "Meta-Analysis" in a.get("pub_types", [])
                for a in articles
            )
            if has_sr and bundle["summary"]["evidence_level"] > "L1":
                bundle["summary"]["evidence_level"] = "L1"
        else:
            bundle["sources"]["pubmed"] = {
                "success": False,
                "error": pubmed_result.error_message,
            }
    except Exception as e:
        bundle["sources"]["pubmed"] = {"success": False, "error": str(e)}

    return bundle


def main():
    parser = argparse.ArgumentParser(
        description="Batch collect evidence bundles for repurposing candidates"
    )
    parser.add_argument("--limit", type=int, default=100, help="Max candidates to process")
    parser.add_argument("--api-key", type=str, help="NCBI API key")

    args = parser.parse_args()

    print("=" * 60)
    print("Batch Evidence Bundle Collection")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"Error: Candidates file not found: {candidates_path}")
        print("Please run run_kg_prediction.py first.")
        return

    # Load candidates
    candidates_df = pd.read_csv(candidates_path)
    print(f"Loaded {len(candidates_df)} repurposing candidates")

    # Get unique drug-disease pairs
    pairs = candidates_df[["ingredient", "potential_indication"]].drop_duplicates()
    pairs = pairs.head(args.limit)
    print(f"Processing {len(pairs)} unique drug-disease pairs...\n")

    # Initialize collectors
    api_key = args.api_key or os.environ.get("NCBI_API_KEY")
    ct_collector = ClinicalTrialsCollector(max_results=10)
    pubmed_collector = PubMedCollector(max_results=10, api_key=api_key)

    # Output directory
    bundle_dir = base_dir / "data" / "evidence" / "bundles"
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # Collect bundles
    summary_stats = {
        "total_processed": 0,
        "with_trials": 0,
        "with_publications": 0,
        "evidence_levels": {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0},
    }

    for i, row in pairs.iterrows():
        drug = row["ingredient"]
        disease = row["potential_indication"]

        print(f"[{summary_stats['total_processed']+1}/{len(pairs)}] {drug} + {disease}...", end=" ")

        bundle = collect_evidence_bundle(drug, disease, ct_collector, pubmed_collector)
        summary_stats["total_processed"] += 1

        if bundle["summary"]["total_trials"] > 0:
            summary_stats["with_trials"] += 1

        if bundle["summary"]["total_publications"] > 0:
            summary_stats["with_publications"] += 1

        evidence_level = bundle["summary"]["evidence_level"]
        summary_stats["evidence_levels"][evidence_level] = (
            summary_stats["evidence_levels"].get(evidence_level, 0) + 1
        )

        # Print progress
        print(f"Trials: {bundle['summary']['total_trials']}, "
              f"Pubs: {bundle['summary']['total_publications']}, "
              f"Level: {evidence_level}")

        # Save bundle
        slug = f"{drug.lower().replace(' ', '-')}-{disease.lower().replace(' ', '-')[:30]}"
        bundle_file = bundle_dir / f"{slug}.json"
        with open(bundle_file, "w", encoding="utf-8") as f:
            json.dump(bundle, f, indent=2, ensure_ascii=False)

        # Rate limiting
        time.sleep(0.5)

    # Print summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total processed: {summary_stats['total_processed']}")
    print(f"With clinical trials: {summary_stats['with_trials']} "
          f"({summary_stats['with_trials']/summary_stats['total_processed']*100:.1f}%)")
    print(f"With publications: {summary_stats['with_publications']} "
          f"({summary_stats['with_publications']/summary_stats['total_processed']*100:.1f}%)")
    print()
    print("Evidence Level Distribution:")
    for level, count in sorted(summary_stats["evidence_levels"].items()):
        print(f"  {level}: {count} ({count/summary_stats['total_processed']*100:.1f}%)")

    # Save summary
    summary_file = base_dir / "data" / "evidence" / "bundle_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary_stats, f, indent=2)

    print(f"\nBundles saved to: {bundle_dir}")
    print(f"Summary saved to: {summary_file}")


if __name__ == "__main__":
    main()
