# GEMM / Linear

## Contract

For row-major tensors, compute signed or floating-point matrix multiplication:

```text
C[M,N] = A[M,K] x transpose(W[N,K])
```

The case record must distinguish the logical matrix from padded storage and
declare activation, weight, accumulation, and output types independently.

## Layout

- `src/`: reference and candidate kernels. Hardware-generated RTL and dependency
  checkouts remain external artifacts; only reproducible source/configuration
  and hashes belong here.
- `tests/`: deterministic shape cases, golden-result method, exact-match or
  tolerance rule, padding and guard checks.
- `bench/`: fixed-platform region-of-interest and metrics.

## Current implementation status

The imported SmolVLA suite uses signed INT8 activation and weights, native
row-major `[N,K]` weights, signed INT32 accumulation/output, and exact output
comparison. It includes every distinct action-expert `nn.Linear` shape captured
from the pinned SmolVLA-base workload. CADL pads M to a multiple of eight.

The current repository contains results and contracts, not the private server
dependency checkout. Portable build adapters are a follow-up item.
