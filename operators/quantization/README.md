# Quantization boundaries

Planned tests cover symmetric and asymmetric quantization, per-tensor and
per-channel scales, saturation, zero points, requantization, accumulator width,
and dequantization. Quantized kernels must be compared with both an exact integer
golden result and an accuracy-oriented floating-point reference.
