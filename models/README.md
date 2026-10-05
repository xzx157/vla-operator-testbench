# Model scenario cards

Before adding results for a VLA model, record:

- model code commit, checkpoint revision, and paper/configuration relationship;
- image, text, state, action, padding, units, and reference frames;
- action horizon, execution length, flow/decode iterations, and token meanings;
- layer, hidden, FFN, head, and head-dimension configuration;
- activation, normalization, position encoding, attention mask, dtype, and layout;
- cache contents and invalidation conditions;
- operator shapes and calls per layer, iteration, action chunk, and inference.

Initial target cards: pi0, pi0.5, OpenVLA, OpenVLA-OFT, SmolVLA, and GR00T N1.x.
