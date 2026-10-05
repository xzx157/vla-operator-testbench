# Scale, mask, and softmax

Planned cases cover causal, prefix, padding, and cross-attention masks; extreme
logits; fully masked rows; stable max-subtraction; and FP32/BF16/FP16 behavior.
Benchmarks will sweep row width and valid-token density.
