# Normalization

Planned variants are LayerNorm, RMSNorm, AdaLN, and AdaRMSNorm. Tests will cover
epsilon, constant and near-zero inputs, affine parameters, condition-generated
scale/shift, and optional residual gates. Reductions and reciprocal-square-root
costs will be reported separately from affine work.
