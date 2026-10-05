# SmolVLA scenario

The first scenario contributes the six distinct dense GEMM shapes executed by
the SmolVLA-base action expert. It is intentionally narrower than full SmolVLA
inference. Attention, normalization, activation, RoPE, flow-update, VLM, vision,
cache, and asynchronous robot-loop measurements remain planned.

The complete model card must later pin the effective camera/text masks,
checkpoint, valid and padded state/action dimensions, action normalization,
flow-step count, cache behavior, and full operator call trace.
