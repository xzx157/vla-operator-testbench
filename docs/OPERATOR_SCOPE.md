# Common VLA operator scope

The scope is organized by reusable computation, not model name. A model scenario
selects operators, shapes, layouts, dtypes, and call counts from this catalog.

## L0 atomic operator families

| Family | Representative computation | Why it is common |
|---|---|---|
| GEMM / Linear | `[M,K] x [K,N] -> [M,N]` | projections, FFN, action heads, adapters |
| Batched matmul | `QK^T` and `P V` | self- and cross-attention |
| Softmax + mask + scale | stable row reduction | attention probabilities and causal/prefix masks |
| Normalization | LayerNorm, RMSNorm | transformer and action-expert blocks |
| Conditional normalization | AdaLN, AdaRMSNorm | flow-time or condition injection |
| Activation and elementwise | GELU, SiLU, add, multiply, affine | FFN gates, residuals, condition gates |
| Position encoding | RoPE and position indexing | visual-language and action attention |
| Vision front end | patch convolution/linear projection, resize | image-to-token path |
| Tensor/data movement | reshape, transpose, concat, gather, cache update | head layout, prefix/suffix, KV reuse |
| Quantization | quantize, dequantize, requantize, saturate | integer accelerator boundaries |
| Flow update | Euler-style action update and timestep embedding | continuous flow/diffusion action generation |

## L1 composed modules

The first composed benchmarks will cover:

- attention projection + RoPE + score matmul + mask/softmax + value matmul +
  output projection;
- gated FFN with GELU or SiLU and down projection;
- pre-norm transformer block with residual paths;
- conditional action block with AdaLN/AdaRMSNorm;
- one flow-matching denoising/update step;
- vision patch embedding and projector;
- autoregressive action-token decode with KV-cache update.

## Model mapping

| Model family | Distinct path to preserve | Shared operators exercised |
|---|---|---|
| pi0 | VLM prefix plus action suffix, continuous flow | GEMM, attention, GELU gate, RMSNorm, RoPE, flow update |
| pi0.5 | state in prefix, conditional action normalization | pi0 set plus AdaRMSNorm and condition gate |
| OpenVLA | discrete autoregressive action tokens | vision path, attention, SiLU gate, RMSNorm, embedding/gather, KV cache |
| OpenVLA-OFT | parallel continuous action chunk and residual MLP head | OpenVLA backbone plus action reshaping and MLP head |
| SmolVLA | interleaved self/cross attention and compact flow expert | GEMM, attention, SiLU gate, RMSNorm, RoPE, cache, flow update |
| GR00T | independent action DiT and embodiment transforms | GEMM, self/cross attention, GELU, LayerNorm/AdaLN, flow update |

## Required shape axes

Cases must not be limited to one model checkpoint. Each operator family should
cover the dimensions that change its hardware behavior:

- batch size and sequence/query/key lengths;
- hidden, head, and intermediate widths;
- square, tall-skinny, short-wide, and irregular matrices;
- aligned and non-aligned tails;
- self-attention versus cross-attention;
- MHA, GQA, and MQA head ratios;
- cached versus uncached execution;
- FP32/BF16/FP16 and supported integer types;
- contiguous and model-native layouts;
- single call, layer aggregate, action chunk, and inference aggregate.

## Out of initial scope

Training-only gradient, optimizer, and loss kernels are excluded from the
inference testbench. Robot-control quality metrics remain model/dataset
evaluation; this repository measures numerical and execution behavior and does
not replace task-success benchmarks.
