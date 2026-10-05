# GEMM implementation adapters

Planned portable adapters:

- scalar host reference;
- scalar RISC-V native-layout baseline;
- compiler-generated baseline;
- Aquas-generated CADL candidate;
- handwritten systolic candidate.

Each adapter must expose the same logical `A x W^T -> C` contract and report
which transfer, command, compute, and writeback phases are inside the measured
region.
