# VLA Operator Testbench

VLA Operator Testbench is a model-independent framework for validating and
benchmarking operators that recur across vision-language-action (VLA) models.
It keeps implementation, correctness tests, benchmark definitions, and result
records next to each operator, following the organization used by
[liquid-dsp](https://github.com/jgaeddert/liquid-dsp).

The repository starts with measured SmolVLA integer GEMM experiments, but
SmolVLA is a scenario, not the repository boundary. The operator registry also
covers the common paths found in pi0/pi0.5, OpenVLA/OFT, SmolVLA, and GR00T.

## What is available now

- A versioned registry of common VLA operators and their implementation status.
- A validated six-shape SmolVLA action-expert INT8 GEMM case set.
- Imported results for the existing scalar, CADL/Aquas, and systolic-array
  experiments, with measured, partial, and pending states kept distinct.
- A dependency-free validator and unit tests for registry, case, and result
  integrity.
- Explicit work plans for non-GEMM operators. Empty measurements are marked
  `planned`; they are never represented as completed experiments.

## Repository layout

```text
operators/<operator>/
  src/       reference and candidate implementations
  tests/     correctness contracts, cases, and golden-data rules
  bench/     benchmark shapes and measurement contracts
modules/     composed kernels such as attention and gated FFN
models/      model/version cards and operator-to-model mappings
scenarios/   reproducible model-derived workloads
results/     concise, immutable measurement records
registry/    machine-readable operator and result indexes
src/         common validation and reporting harness
tests/       repository-level regression tests
docs/        architecture, scope, result policy, and roadmap
```

## Quick start

Python 3.11 or newer is sufficient.

```bash
python -m pip install -e .
vla-bench list
vla-bench validate
python -m unittest discover -s tests -v
```

`vla-bench validate` checks structure and provenance. It does not claim that a
planned hardware experiment has run.

## Current GEMM evidence

The initial public records include:

- the original FP32 RV64GC/gem5 scalar baseline used to locate SmolVLA GEMM
  hotspots;
- the Aquas-generated CADL v2 full-shape Rocket/RoCC measurements;
- the matched standalone 4x4 systolic-array comparison;
- complete Rocket/RoCC systolic measurements for the two full FFN shapes;
- the complete six-shape matched native-layout CPU versus CADL suite, with a
  14.417x call-weighted isolated-GEMM projection.

See [the GEMM result notes](results/gemm/smolvla/README.md) for the exact scope
of each number.

## Design documents

- [Architecture](docs/ARCHITECTURE.md)
- [Common VLA operator scope](docs/OPERATOR_SCOPE.md)
- [Result and evidence policy](docs/RESULTS_POLICY.md)
- [Roadmap and missing experiments](docs/ROADMAP.md)
- [Research sources](docs/REFERENCES.md)

## License

Code and documentation in this repository are released under the MIT License.
Imported result records remain subject to the licenses of the tools and models
identified by their provenance fields.
