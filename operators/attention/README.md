# Attention

Planned cases cover self- and cross-attention, MHA/GQA/MQA, cached and uncached
execution, and unequal query/key lengths. Correctness will separately check Q/K/V
projection, RoPE, score matmul, masking/softmax, probability-times-value, head
merge, and output projection before measuring fused modules.
