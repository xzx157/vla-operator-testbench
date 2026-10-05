# GEMM correctness tests

Every case requires deterministic inputs, a wide reference accumulation,
logical-output comparison, padded-row validation, and leading/trailing memory
guards. INT8-to-INT32 cases require exact equality. Floating-point cases declare
absolute and relative tolerances and the accumulation order used by the golden
implementation.

The initial case set is in `cases.json`.
