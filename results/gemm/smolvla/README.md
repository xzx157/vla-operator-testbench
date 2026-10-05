# SmolVLA GEMM results

These records preserve distinct experimental scopes.

| Record | Arithmetic/platform | What it establishes |
|---|---|---|
| `initial-gemm-baseline.json` | FP32 RV64GC/gem5 | initial hotspot and locality evidence |
| `cadl-v2-full-shape.json` | INT8/INT32 Rocket/RoCC | Aquas-generated CADL v2 full FFN shapes |
| `systolic-array-real-shapes.json` | INT8/INT32 standalone RTL | matched scalar versus 4x4 systolic compute core |
| `systolic-rocket-full-shapes.json` | INT8/INT32 Rocket/RoCC | full-system systolic FFN shapes including DMA |
| `action-gemm-suite-partial.json` | INT8/INT32 Rocket/RoCC | four of six matched native-layout CPU/CADL shapes |

## Important boundaries

The initial FP32 result and the later INT8 results are different experiments and
must not be used in a direct speedup ratio. The standalone systolic result
excludes Rocket and DMA, whereas the Rocket/RoCC records include system overhead.

The partial six-shape record reports an 8.35x call-weighted speedup only for the
four completed shapes. It is not the final six-shape number and is not an
end-to-end SmolVLA inference result. The final record requires completed,
validated native-layout CPU results for `gate_up` and `down`.

Linalg runs that exited without one complete `SMOL_GEMM_FULL` record are excluded
from published performance results even if the wrapper exit code was zero.
