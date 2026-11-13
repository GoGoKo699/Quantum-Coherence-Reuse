# Finite verification

The analytical proofs are in [the construction](../science/construction.md), [sequential reuse](../science/sequential_reuse.md), and [the converse](../science/converse.md). This directory supplies reproducible finite diagnostics of the explicit processor and its error accounting.

Run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify_processor.py
```

The program writes [results.json](results.json), including the actual Python, NumPy, and SciPy versions. The numerical values are floating point.

## What is checked

| Check | Evidence supplied |
|---|---|
| Sine-fourth profile, every integer $3\leq L\leq129$ | Normalization, mean excitation, exact second-difference identity, the proved pointwise bound, and the Hellinger estimate with exterior boundary mass included. |
| Explicit finite processor | Every total-charge block is constructed as a Householder matrix. Full-matrix unitarity and its charge commutator are evaluated. |
| Full joint output after reuse | The same matrix is applied to fresh pairs while all earlier outputs remain in the state. Trace distance is computed from eigenvalues of the complete density-matrix difference. |
| Independent charge-sector benchmark | The convolution/Bhattacharyya expression is compared with the direct one-pair matrix result. It also gives a collective optimum at the same fixed pure reference, which is compared with sequential errors. |
| Energy/error rounding | The prescribed ceiling for $L$ is evaluated at twelve even batch-size/error-budget choices, and its analytical and one-pair hybrid bounds are compared. |
| Finite preparation and channel errors | A perturbed reference and a pair channel mixed with identity are evolved as complete density matrices; both nominal-reference and actual-prepared-reference product targets satisfy their error budgets. |

The direct matrix cases include the smallest allowed ladder, $L=3$, and three-pair reuse at $L=8$ and $L=16$. The global-state calculations do not infer independence from one-qubit marginals.

## Limits of the evidence

Passing these calculations corroborates the selected finite identities and implementations. It does not prove an asymptotic theorem, certify floating-point results by intervals, optimize constants, synthesize a physical number-selective controller, or validate a hardware noise model. The universal mixed-reference converse is an analytical statement, not an inference from a search over finite examples.
