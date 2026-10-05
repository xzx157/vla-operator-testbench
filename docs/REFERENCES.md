# References

The initial operator scope was derived from the internal VLA survey dated
2026-09-24 and checked against public primary implementations.

- [liquid-dsp](https://github.com/jgaeddert/liquid-dsp): co-located source,
  correctness tests, benchmark files, generated registries, and JSON output.
- [Physical Intelligence openpi](https://github.com/Physical-Intelligence/openpi):
  pi0, pi0-FAST, and pi0.5 model implementations, flow matching, KV-cache use,
  RMSNorm, and AdaRMSNorm.
- [Hugging Face LeRobot SmolVLA](https://github.com/huggingface/lerobot/tree/main/src/lerobot/policies/smolvla):
  state/action projections, RMSNorm, RoPE, self/cross attention, KV cache, gated
  FFN, and flow-matching inference.
- [OpenVLA](https://github.com/openvla/openvla): autoregressive action-token VLA.
- [OpenVLA-OFT](https://github.com/moojink/openvla-oft): parallel continuous
  action heads, optional FiLM, proprioception projection, and action chunks.
- [NVIDIA Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T): multimodal policy,
  embodiment-specific state/action transforms, action chunks, and inference
  service boundaries.

Active branches can change. Every executable scenario must therefore pin model
code commits, checkpoint revisions, preprocessing configuration, and action
semantics before measurement.
