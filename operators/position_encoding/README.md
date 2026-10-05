# Position encoding

The initial target is RoPE over Q/K tensors with configurable base, position
index, head dimension, dtype, and interleaving convention. Tests must catch
layout and sign/order errors, not only aggregate numerical tolerance.
