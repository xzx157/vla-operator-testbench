"""Command-line entry point for repository inspection and validation."""

from __future__ import annotations

import argparse
import json

from .registry import load_json, repository_root, validate_repository


def list_operators() -> int:
    root = repository_root()
    registry = load_json(root / "registry" / "operators.json")
    for operator in registry["operators"]:
        print(
            f"{operator['id']:<24} {operator['status']:<10} "
            f"{operator['name']}"
        )
    return 0


def show_results() -> int:
    root = repository_root()
    registry = load_json(root / "registry" / "results.json")
    print(json.dumps(registry, indent=2))
    return 0


def validate() -> int:
    errors = validate_repository()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: operator registry, GEMM cases, and result index are valid")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(prog="vla-bench")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list", help="list registered operators")
    subparsers.add_parser("results", help="print the result registry")
    subparsers.add_parser("validate", help="validate repository metadata")
    args = parser.parse_args()
    status = {
        "list": list_operators,
        "results": show_results,
        "validate": validate,
    }[args.command]()
    raise SystemExit(status)
