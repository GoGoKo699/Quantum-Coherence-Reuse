# Quantum Coherence Reuse

**How much energy must a reusable phase reference initially contain to prepare many independent coherent qubits?**

Each fresh qubit pair starts in $|01\rangle$. The same energy-conserving processor interacts with the reference and one pair at a time, aiming to produce $|++\rangle$ and return the reference. Accuracy is measured on **the reference and every output together**, so good individual outputs cannot conceal accumulated correlations.

## Main result

Let $N\geq2$ be even and let $0<\delta\leq1/8$ be the allowed half trace distance from the complete ideal product. In units of the qubit energy gap, the minimum initial reference mean energy obeys

$$
\boxed{\displaystyle E_{\min}(N,\delta)=\Theta\left(\sqrt{\frac{N}{\delta}}\right).}
$$

The constants are uniform in $N$ and $\delta$ in this domain. The [precise theorem](science/model.md) distinguishes the unrestricted covariant optimization from the attaining sequential architecture.

| Direction | What is established |
| --- | --- |
| Necessary resource | Every deterministic time-translation-covariant protocol obeys the bound, allowing arbitrary mixed references with finite mean energy, sparse or unbounded spectra, and invariant ancillary resources. No variance bound is assumed. |
| Attaining resource | A finite reference with sine-fourth number probabilities and one fixed conserving pair unitary attain the scaling by repeated use. No reference reset or postselection is used. |
| Global accuracy | The returned reference and all coherent outputs are close to their complete ideal product; the analysis retains all accumulated correlations. |
| Implementation errors | Initial-reference mismatch and per-use channel errors admit an explicit accumulated error budget. Control synthesis, preparation cost and physical duration are separate resources. |

Every pair already supplies one excitation. Thus $N/2$ excitations are initially present in the qubit register, separately from the reference energy. The theorem characterizes the reference stock; it does not give a sublinear total preparation-energy claim.

## Why balancing the pair matters

The input $|01\rangle$ and desired $|++\rangle$ have the same mean excitation. The reference accommodates fluctuations without a systematic mean-energy transfer. A smooth reference profile then changes by a second difference under the relevant charge convolution, giving a one-pair joint trace error of order $L^{-2}$ for a reference of mean energy of order $L$. Reusing the same processor $N/2$ times gives a full joint error of order $N/L^2$.

The converse compares two time-translated reference states. Appending an independent pure coherent output makes their ideal products more distinguishable. Covariant processing cannot increase distinguishability, and a finite mean reference energy limits how rapidly its orbit can separate. This yields the matching resource requirement even when rare high-energy components make the variance large or infinite.

Quadratic reference longevity, catalytic state preparation, and the importance of output correlations are established ideas. The result here is the optimal mean-energy law with full joint product return, together with an explicit repeated conserving realization. The normalized charge-sector construction shares the covariant-recovery foundation of Marvian and Lloyd; [related work](references/RELATED_WORK.md) identifies the inherited methods and the surviving conclusion.

## Read the science

| Question | Authoritative account |
| --- | --- |
| What is supplied, returned and optimized? | [Model and exact theorem](science/model.md) |
| Why do mixed or heavy-tailed references still need enough mean energy? | [Mean-energy converse](science/converse.md) |
| How is a finite conserving processor built, including its boundaries? | [Reference and pair construction](science/construction.md) |
| Why does repeated use control the entire output batch? | [Sequential reuse and error budget](science/sequential_reuse.md) |
| What does a small complete example look like? | [Worked examples](science/examples.md) |
| Which costs and physical interpretations follow? | [Resource accounting](science/resource_accounting.md) and [interpretation](science/interpretation.md) |
| Which conclusions and mechanisms come from earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [science overview](science/README.md) gives the connected proof route. The [reading guide](llms.txt) maps technical questions to the same sources.

## Learn the project

The educational anchor is **Watrous, *The Theory of Quantum Information* (2018)**. The [learning route](learning/README.md) connects its state-discrimination and channel-distance tools to this problem.

Start with the [notation and source bridge](learning/WATROUS_BRIDGE.md), then follow the [worked tutorial](learning/TUTORIAL.md) and the [30-milestone map](learning/MILESTONES.md). Its 12 background and 18 narrative milestones build from individual states and channels to the complete resource law. The specialist proofs above remain authoritative.

## Reproduce

With Python 3.10 or later, run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_processor.py
```

The [verification guide](verification/README.md) distinguishes direct finite-unitary and full-state calculations from analytical proofs. The [recorded output](verification/results.json) includes conservation, unitarity, global error and sequential-reuse checks. Finite computations do not certify every parameter or an experimental implementation.

## Scope

The task prepares known coherent states from fresh precharged pairs. The reference is initially independent of the inputs, and all asymmetric controllers must be counted as part of it. The necessary bound allows general covariant channels; the attaining construction uses a finite exactly conserving unitary repeatedly. The result does not implement an arbitrary unknown-input gate or universal measurement channel, optimize finite-error constants, or establish indefinite reuse at fixed global error.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
