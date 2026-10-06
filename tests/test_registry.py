import json
import tempfile
import unittest
from pathlib import Path

from vla_bench.registry import (
    repository_root,
    validate_gemm_cases,
    validate_operators,
    validate_repository,
)


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository(), [])

    def test_all_registered_operators_have_unique_ids(self) -> None:
        root = repository_root()
        registry = json.loads(
            (root / "registry" / "operators.json").read_text(encoding="utf-8")
        )
        ids = [operator["id"] for operator in registry["operators"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_gemm_suite_contains_all_six_captured_shapes(self) -> None:
        root = repository_root()
        suite = json.loads(
            (root / "operators" / "gemm" / "tests" / "cases.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(suite["cases"]), 6)
        self.assertEqual(validate_gemm_cases(root), [])

    def test_complete_smolvla_gemm_result_has_six_exact_profiles(self) -> None:
        root = repository_root()
        result = json.loads(
            (
                root
                / "results"
                / "gemm"
                / "smolvla"
                / "action-gemm-suite.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(len(result["profiles"]), 6)
        self.assertEqual(
            result["correctness"],
            {
                "exact_int32_match_across_both_modes": True,
                "guards_intact": True,
                "normal_simulator_exit": True,
            },
        )
        self.assertAlmostEqual(
            result["call_weighted_metrics"]["speedup_cpu_over_cadl"],
            14.416723736635825,
        )

    def test_missing_operator_readme_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "registry").mkdir()
            (root / "registry" / "operators.json").write_text(
                json.dumps(
                    {
                        "operators": [
                            {
                                "id": "missing",
                                "status": "planned",
                                "path": "operators/missing",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            errors = validate_operators(root)
        self.assertTrue(any("missing operator README" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
