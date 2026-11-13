# Physical interpretation

The resource is the energy initially stored in a phase reference, rather than energy dissipated per use. A reference supplies a coherent relation between different excitation sectors. A processor that preserves total excitation can transfer that relation to fresh qubits while slightly changing the complete joint state.

## A finite coherent-output budget

For a small fixed joint tolerance, the number of coherent qubits that can be produced has quadratic order in the available reference mean energy. The tolerance itself matters: in the small-error regime the budget has order $\delta E^2$, with the even output size and integer rounding of the construction understood.

This statement includes the reference return and all outputs in one trace-distance comparison. It neither asserts exactly unchanged finite catalysis nor indefinite reuse. As the requested batch grows at fixed reference energy, its global error must eventually grow. Good local marginals or a good next-use score do not establish the required independent output batch.

## Drift and fluctuations

Each supplied pair starts with exactly one excitation. The desired $|++\rangle$ pair has the same mean excitation but has charge fluctuations. Relative to the input charge, its charge distribution has weights $1/4,1/2,1/4$ on shifts $-1,0,1$. This balance produces a second-difference change of a smooth reference profile. The sine-fourth probabilities are smooth enough at both finite boundaries to make the full joint trace error per pair quadratic in inverse ladder width.

This explains why balancing is useful without claiming a general law for every state-preparation or gate task. Starting all qubits in their ground state, requesting a different target, supplying a work buffer, or implementing a gate on unknown inputs changes the resource model and requires its own comparison.

## Why only a mean-energy assumption is substantial

A small probability on very high levels can make reference energy variance arbitrarily large at fixed mean. A variance-only or Fisher-information statement therefore need not bound the actual mean energy invested. The [converse](converse.md) instead uses the characteristic function and trace distinguishability of the reference's time orbit. Its first-moment estimate applies to mixed states and heavy energy tails without assuming a finite variance or a hard support cutoff.

The ideal product of the reference and a fresh pure coherent batch would carry more information about time translation than the reference alone. Covariant processing cannot create that extra distinguishability freely. The permitted global error and the initial mean energy quantitatively bound how much such approximate broadcasting is possible. The general information-disturbance and asymmetry framework is inherited; [related work](../references/RELATED_WORK.md) separates it from the optimal budget established here.

## What a user of the outputs receives

The full trace-distance guarantee is preserved by every later physical channel, including one acting jointly on all outputs and the reference. Thus the batch can be treated as an approximately independent coherent source within that global error allowance. This is a compositional consequence of trace distance; it is not an assumption that the actual intermediate reference or outputs are independent.

The [implementation-error budget](sequential_reuse.md#stability-under-preparation-and-channel-errors) makes the same point for imperfections. Errors of implemented pair channels must be controlled on correlated inputs, which is why a reference-assisted channel norm is used. Isolated-output tests do not establish that assumption.

## Boundaries of the result

The input qubit energy, the preparation of the reference state, the physical realization of number-selective blocks, the timing of contacts, locality, and hardware noise all remain charged or declared as separate resources. The finite processor has an explicit description, but no optimal gate-complexity or time result follows. The theorem is a sharp resource characterization for a specified known-state source, rather than a claim about arbitrary quantum computation or free coherent control.

[Resource accounting](resource_accounting.md) · [Exact model](model.md) · [Examples](examples.md)
