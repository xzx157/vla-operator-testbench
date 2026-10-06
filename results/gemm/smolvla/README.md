# SmolVLA GEMM results

These records preserve distinct experimental scopes.

| Record | Arithmetic/platform | What it establishes |
|---|---|---|
| `initial-gemm-baseline.json` | FP32 RV64GC/gem5 | initial hotspot and locality evidence |
| `cadl-v2-full-shape.json` | INT8/INT32 Rocket/RoCC | Aquas-generated CADL v2 full FFN shapes |
| `systolic-array-real-shapes.json` | INT8/INT32 standalone RTL | matched scalar versus 4x4 systolic compute core |
| `systolic-rocket-full-shapes.json` | INT8/INT32 Rocket/RoCC | full-system systolic FFN shapes including DMA |
| `action-gemm-suite.json` | INT8/INT32 Rocket/RoCC | complete six-shape matched native-layout CPU/CADL suite |
| `action-gemm-suite-partial.json` | INT8/INT32 Rocket/RoCC | superseded four-shape intermediate record retained for audit |

## Important boundaries

The initial FP32 result and the later INT8 results are different experiments and
must not be used in a direct speedup ratio. The standalone systolic result
excludes Rocket and DMA, whereas the Rocket/RoCC records include system overhead.

The complete six-shape record reports 649,028,268,960 call-weighted native CPU
cycles and 45,019,123,680 CADL v2 cycles, a 14.417x isolated-GEMM projection.
Every CPU/CADL pair has an identical INT32 checksum, intact guards, and a normal
simulator exit. This is not an end-to-end SmolVLA inference result: it excludes
the non-GEMM operators and enclosing model execution.

The partial record reports an earlier 8.35x projection over only four shapes.
It remains solely as intermediate evidence and must not be used as the current
suite result.

Linalg runs that exited without one complete `SMOL_GEMM_FULL` record are excluded
from published performance results even if the wrapper exit code was zero.
