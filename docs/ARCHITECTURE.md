# Testbench architecture

## Purpose

The testbench compares implementations without confusing four different
questions:

1. Is the operator numerically correct?
2. Is memory access safe and layout-compatible?
3. How fast is the isolated operator on a fixed platform?
4. How much does it change module, inference, and robot-loop latency?

Each result must state which question it answers.

## Liquid-dsp pattern retained

Each operator owns three neighboring areas:

```text
operators/<id>/src
operators/<id>/tests
operators/<id>/bench
```

`src` contains reference or candidate implementations. `tests` contains exact
correctness contracts and golden-data generation. `bench` contains shapes,
repetition rules, regions of interest, and reported metrics. A central registry
discovers them and a common harness validates their metadata and result files.

## Four test levels

| Level | Unit under test | Required output |
|---|---|---|
| L0 operator | GEMM, softmax, norm, RoPE, elementwise | numerical agreement, guards, cycles |
| L1 module | attention, gated FFN, transformer block | composed correctness and fusion benefit |
| L2 model scenario | one real model stage or action chunk | call-weighted latency and coverage |
| L3 system | complete inference and robot execution loop | wall time, throughput, deadline misses |

An L0 speedup is not an L2 or L3 speedup. Call-weighted projection may estimate
L2 impact, but it remains a projection until measured end to end.

## Stable interfaces

Every case declares:

- semantic operation and equations;
- tensor shapes, layout, dtype, accumulation dtype, and padding;
- deterministic input generation and golden-result method;
- correctness tolerance or exact-match rule;
- platform, compiler, simulator, and hardware revisions;
- region of interest and whether setup, transfer, and validation are included;
- counters and derived metrics;
- model/version provenance and real call count when model-derived.

## Adding an operator

1. Add an entry to `registry/operators.json`.
2. Add `operators/<id>/README.md` with the semantic contract.
3. Add correctness cases before candidate acceleration code.
4. Add benchmark cases with small, edge, and real-model shapes.
5. Mark the status `reference-ready` only after a runnable reference path and
   golden-result test exist.
6. Mark results `measured` only after all evidence checks in
   `docs/RESULTS_POLICY.md` pass.

## Future integration into vla-profiling

The standalone repository can later be integrated without rewriting history:

- Git subtree preserves this repository as a subdirectory and is the preferred
  option if the testbench keeps an independent release cycle.
- Git submodule preserves a hard repository boundary but adds clone/update
  friction.
- A history-preserving merge with `git subtree add` followed by normal in-tree
  development is appropriate if the testbench becomes inseparable from
  `vla-profiling`.

No source path in this repository depends on its current parent directory, so
all three options remain available.
