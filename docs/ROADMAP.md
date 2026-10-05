# Roadmap and missing experiments

## Phase 0: repository foundation

- [x] Define the model-independent operator catalog.
- [x] Preserve the liquid-dsp-style source/test/benchmark organization.
- [x] Add machine-readable registries and a dependency-free validator.
- [x] Import completed SmolVLA GEMM evidence without relabeling projections as
  end-to-end measurements.

## Phase 1: finish the GEMM baseline

- [ ] Finish the two large native-layout CPU simulations for `gate_up` and
  `down`; do not substitute incomplete Linalg logs.
- [ ] Produce the complete six-shape matched CPU/CADL record and call-weighted
  action-expert GEMM projection.
- [ ] Add repeated-run variance or document why deterministic cycle simulation
  makes one run sufficient.
- [ ] Add boundary shapes around tile sizes and irregular M/N/K tails.
- [ ] Measure full action-expert, full policy inference, and robot-loop latency.
- [ ] Add resource/area/timing data so cycle speedup is not the only hardware
  metric.

## Phase 2: transformer primitives

For each item below, add a host reference, deterministic cases, exact/tolerant
comparison rule, compiler baseline, and fixed-hardware measurement:

- [ ] RMSNorm, LayerNorm, AdaRMSNorm, and AdaLN;
- [ ] GELU, SiLU, residual add, gate multiply, scale, and affine modulation;
- [ ] RoPE;
- [ ] stable softmax with causal, prefix, padding, and cross-attention masks;
- [ ] `QK^T` and probability-times-value batched matmul;
- [ ] layout transforms and KV-cache append/read.

## Phase 3: composed modules

- [ ] Gated FFN for pi0/Gemma and SmolVLA/Llama variants.
- [ ] Self-attention and cross-attention with MHA/GQA/MQA cases.
- [ ] One pre-norm transformer block.
- [ ] One conditional action-expert block.
- [ ] One flow-update step with timestep embedding and action-array update.
- [ ] One autoregressive action-token decode step.

## Phase 4: vision and complete VLA scenarios

- [ ] Patch embedding and vision projection.
- [ ] Image resize/normalization and token compression where compute-relevant.
- [ ] Pinned pi0/pi0.5, OpenVLA/OFT, SmolVLA, and GR00T scenario cards.
- [ ] Per-model operator coverage and call-count extraction.
- [ ] Full-inference measurements with cache lifetime and observation reuse.
- [ ] Synchronous and asynchronous robot-loop measurements, including action
  queue depth, replanning interval, deadline misses, and throughput.

## Required content before a planned row becomes measured

Every placeholder must eventually receive:

1. a pinned source/checkpoint/configuration card;
2. real tensor shapes captured from execution;
3. input and golden-output provenance;
4. a runnable reference and candidate implementation;
5. compile and run commands;
6. complete correctness evidence;
7. cycles, memory traffic, and relevant hardware counters;
8. model call counts and a clear aggregation boundary;
9. concise JSON results and human-readable interpretation.
