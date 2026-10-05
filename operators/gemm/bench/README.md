# GEMM benchmark contract

The benchmark reports logical and physical MACs, cycles, logical MAC/cycle,
physical MAC/cycle, padding work, memory traffic when available, and host
simulation time. Candidate speedup is computed only against a baseline with the
same logical shape, data, output, and region of interest.

Required shape classes are tiny smoke, tile-aligned, one-dimensional tails,
all-dimension tails, square attention projections, tall/skinny vision
projections, short/wide action projections, and captured real-model shapes.

The current SmolVLA Rocket/RoCC region includes command, DMA, accelerator
compute, and writeback while excluding initialization and validation.
