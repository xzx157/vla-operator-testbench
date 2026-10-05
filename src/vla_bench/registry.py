"""Load and validate repository registries."""

from __future__ import annotations

import json
from pathlib import Path


VALID_STATUSES = {
    "planned",
    "running",
    "partial",
    "measured",
    "failed",
    "superseded",
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return value


def validate_operators(root: Path) -> list[str]:
    errors: list[str] = []
    registry = load_json(root / "registry" / "operators.json")
    operators = registry.get("operators")
    if not isinstance(operators, list) or not operators:
        return ["operator registry must contain a non-empty operators list"]
    seen: set[str] = set()
    for operator in operators:
        operator_id = operator.get("id")
        if not isinstance(operator_id, str) or not operator_id:
            errors.append("operator has no valid id")
            continue
        if operator_id in seen:
            errors.append(f"duplicate operator id: {operator_id}")
        seen.add(operator_id)
        if operator.get("status") not in VALID_STATUSES:
            errors.append(f"{operator_id}: invalid status {operator.get('status')!r}")
        path = root / str(operator.get("path", ""))
        if not path.is_dir() or not (path / "README.md").is_file():
            errors.append(f"{operator_id}: missing operator README at {path}")
    return errors


def validate_results(root: Path) -> list[str]:
    errors: list[str] = []
    registry = load_json(root / "registry" / "results.json")
    results = registry.get("results")
    if not isinstance(results, list):
        return ["result registry must contain a results list"]
    seen: set[str] = set()
    for result in results:
        result_id = result.get("id")
        if not isinstance(result_id, str) or not result_id:
            errors.append("result has no valid id")
            continue
        if result_id in seen:
            errors.append(f"duplicate result id: {result_id}")
        seen.add(result_id)
        if result.get("status") not in VALID_STATUSES:
            errors.append(f"{result_id}: invalid status {result.get('status')!r}")
        path = root / str(result.get("path", ""))
        if result.get("status") in {"measured", "partial", "failed", "superseded"}:
            if not path.is_file():
                errors.append(f"{result_id}: missing result file {path}")
            else:
                try:
                    load_json(path)
                except (OSError, ValueError, json.JSONDecodeError) as error:
                    errors.append(f"{result_id}: invalid result JSON: {error}")
    return errors


def validate_gemm_cases(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "operators" / "gemm" / "tests" / "cases.json"
    suite = load_json(path)
    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        return ["GEMM suite must contain a non-empty cases list"]
    seen: set[str] = set()
    for case in cases:
        case_id = case.get("id")
        if case_id in seen:
            errors.append(f"duplicate GEMM case id: {case_id}")
        seen.add(case_id)
        for key in ("m", "m_storage", "n", "k", "calls_per_action_chunk"):
            value = case.get(key)
            if not isinstance(value, int) or value <= 0:
                errors.append(f"{case_id}: {key} must be a positive integer")
        if isinstance(case.get("m"), int) and isinstance(case.get("m_storage"), int):
            if case["m_storage"] < case["m"]:
                errors.append(f"{case_id}: m_storage is smaller than logical m")
    return errors


def validate_repository(root: Path | None = None) -> list[str]:
    base = root or repository_root()
    return (
        validate_operators(base)
        + validate_results(base)
        + validate_gemm_cases(base)
    )
