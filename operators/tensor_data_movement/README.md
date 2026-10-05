# Tensor and data movement

Planned cases include reshape, transpose, concatenate, split, gather/embedding,
head packing, prefix/suffix assembly, padding, and KV-cache append/read. Views
that change only metadata must be distinguished from operations that physically
move bytes.
