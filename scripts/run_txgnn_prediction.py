#!/usr/bin/env python3
"""TxGNN Philippines Drug Repurposing Prediction - Deep Learning Method

This script uses the TxGNN pretrained model for deep learning prediction,
automatically detecting available compute devices (CUDA/CPU).
Supports checkpointing: if interrupted with Ctrl+C, re-running will resume from last checkpoint.

Prerequisites:
    1. Download and extract model_ckpt.zip to model_ckpt/ directory (or symlink)
    2. Set up conda environment (see below)

Usage:
    # Activate conda environment and run
    conda activate txgnn
    python scripts/run_txgnn_prediction.py

    # Ignore previous progress and restart
    python scripts/run_txgnn_prediction.py --restart

Environment setup:
    conda create -n txgnn python=3.11 -y
    conda activate txgnn
    pip install torch==2.2.2 torchvision==0.17.2
    pip install dgl==1.1.3
    pip install git+https://github.com/mims-harvard/TxGNN.git
    pip install pandas tqdm pyyaml pydantic ogb
"""

import argparse
import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from phtxgnn.predict.txgnn_model import (
    check_dependencies,
    detect_device,
    print_install_instructions,
    run_taiwan_drug_prediction,
)


def main():
    parser = argparse.ArgumentParser(description="TxGNN Philippines Drug Repurposing Prediction")
    parser.add_argument(
        "--restart",
        action="store_true",
        help="Ignore previous progress and restart prediction",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("TxGNN Philippines Drug Repurposing Prediction")
    print("=" * 60)
    print()

    # Detect device
    device = detect_device()

    # Check dependencies
    deps_ok, missing = check_dependencies()

    if not deps_ok:
        print(f"\nMissing required packages: {', '.join(missing)}")
        print_install_instructions(missing, device)
        print("\nPlease install the above packages and re-run this script.")
        sys.exit(1)

    print()

    # Run prediction (with checkpoint support)
    result = run_taiwan_drug_prediction(
        drug_mapping_path=Path(__file__).parent.parent / "data" / "processed" / "drugbank_mapping.csv",
        device=device,
        min_score=0.0,  # Keep all positive score results
        restart=args.restart,
    )

    if result is not None and len(result) > 0:
        print("\nPrediction complete!")
        print(f"Results file: data/processed/txgnn_dl_predictions.csv.gz")
        print(f"Checkpoint: data/processed/txgnn_checkpoint.csv")
    else:
        print("\nNo results generated, please check drug mapping data.")


if __name__ == "__main__":
    main()
