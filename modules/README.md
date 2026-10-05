# Composed module benchmarks

Modules combine validated L0 operators without erasing their contracts. Planned
modules are gated FFN, attention, pre-norm transformer block, conditional action
block, one flow-matching step, and one autoregressive action-token decode step.

Each module result records its component cases, fusion boundaries, intermediate
checks, and the difference between the sum of isolated cycles and measured
composed cycles.
