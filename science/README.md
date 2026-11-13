# Scientific account

A reusable phase reference can prepare many coherent qubits, but accuracy must include both the returned reference and the complete output batch. This account determines the optimal reference mean-energy order under that joint requirement.

Read [the model and exact theorem](model.md) first. Two arguments then meet:

1. [The converse](converse.md) bounds the extra distinguishability carried by the desired pure output and controls the reference orbit using only its first energy moment. It permits arbitrary mixed references and general covariant operations.
2. [The finite construction](construction.md) aligns normalized charge-sector projections for one precharged pair. A sine-fourth probability profile gives a uniform second-difference estimate, including the ladder boundaries.
3. [Sequential reuse](sequential_reuse.md) repeats the identical processor and bounds the full reference-plus-batch trace error. It also supplies an implementation-error budget without assuming independent accumulated errors.

[Worked examples](examples.md) connect a three-level reference and direct finite-state checks to the theorem. [Resource accounting](resource_accounting.md) fixes energy units, ancillary assumptions, optimizer scope, total supplied energy and implementation limits. [Interpretation](interpretation.md) explains why balancing the fresh pairs and retaining all correlations matter.

[Related work](../references/RELATED_WORK.md) owns the source-by-source attribution. [Verification](../verification/README.md) explains the actual numerical calculations and their limits. Each scientific result has one authoritative proof home above.
