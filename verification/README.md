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

## Learning and navigation checks

Run `python3 verification/check_structure.py` from the repository root. This standard-library script checks relative reader links and source heading fragments, the selected educational-anchor identity, exactly thirty milestone records with required fields and earlier prerequisites, and narrow private-workflow leakage indicators. It inventories every Markdown page for the separate hosted review. These checks do not establish scientific correctness, pedagogical quality, bibliography completeness, or rendered mathematics and visual quality.

## Actual GitHub rendering

The read-only [hosted mathematics workflow](../.github/workflows/hosted-math.yml) checks the exact proposed commit. Its [collector](hosted_math/capture_hosted_math.cjs) opens every tracked Markdown page on GitHub at widths 1440 and 760, comparing actual accessible MathML with the source expression structure and checking bounded geometry. Captured reports, HTML and full-page screenshots are retained as workflow artifacts for fourteen days. A passing automated comparison still requires visual inspection of equations, tables and navigation. It supplies no scientific proof or guarantee about future GitHub rendering.

The capture runtime uses Node.js 22, Playwright 1.56.1 and MathJax 3.2.1; these browser dependencies are installed outside the source tree. A local invocation with the same dependencies is:

```bash
NODE_PATH=/absolute/capture-runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/repository --repository GoGoKo699/Quantum-Coherence-Reuse \
  --revision FULL_COMMIT_SHA --output /absolute/new-capture-directory
```

Use a new output directory and an actual full commit SHA. A [single-page probe](hosted_math/probe_hosted_math.cjs) with exactly one `--page` is an early diagnostic, not a complete review. Failed captures remain diagnostic evidence and do not become passing evidence when a later source revision is repaired.
