# Result and evidence policy

## Status vocabulary

- `planned`: contract and intended experiment are defined; no measurement.
- `running`: an authorized experiment is active; no final number is published.
- `partial`: some declared cases are measured, with missing cases listed.
- `measured`: the declared scope completed and passed all acceptance checks.
- `failed`: the run completed abnormally or violated correctness requirements.
- `superseded`: preserved history that is no longer the comparison baseline.

## Acceptance checks

A hardware-simulation result is `measured` only when all of the following are
recorded:

1. exactly one complete machine-readable result line;
2. normal process exit and normal simulator finish;
3. zero reported runtime errors;
4. numerical agreement with the declared golden result;
5. intact leading, trailing, and padding guards when applicable;
6. source, executable, and log hashes where available;
7. an explicit region of interest;
8. platform and revision provenance.

Exit code zero alone is insufficient. A log that reaches the simulator maximum
cycle limit without a result line is not a successful measurement.

## Comparison rules

Speedups require the same semantic operation, input data, output contract, and
measurement boundary. Differences in dtype, layout, transfer inclusion, or
padding must be stated next to the result.

Model-level projections multiply each isolated-case cycle count by a measured
or source-derived call count. They are labeled projections and are not reported
as measured full-inference speedups.

## Public data policy

Concise JSON result records are committed. Large binaries, generated RTL,
waveforms, full logs, dependency checkouts, and private server configuration are
excluded. Result records may include non-sensitive host aliases and content
hashes, but never credentials or private connection details.
