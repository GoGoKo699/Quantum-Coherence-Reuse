# Sequential reuse with a global error guarantee

A small error in every individual output does not by itself establish an independent output batch. The protocol here is instead compared directly with the full joint target: the initial reference tensor the complete pure output batch. No old output is traced out during the comparison.

Use the finite reference $|R_L\rangle$ and exactly conserving unitary $U_L$ from [the construction](construction.md). Let $N=2m$ be even. Supply $m$ fresh pairs in $|01\rangle$ and apply the **same** $U_L$ to the reference and each pair in turn. Earlier outputs are left untouched.

## Sequential hybrid bound

Write $\sigma_L=|R_L\rangle\langle R_L|$, $\psi_2=|++\rangle\langle++|$, and let $\rho_j$ be the actual joint state of the reference and the first $j$ processed pairs. Its ideal comparison state is

$$
\tau_j=\sigma_L\otimes\psi_2^{\otimes j}.
$$

At step $j+1$, append a fresh $|01\rangle$ pair to both states. Apply $U_L$ to that pair and the reference, and apply the identity to earlier outputs. Trace-distance contractivity bounds the distance between the resulting two states by $D(\rho_j,\tau_j)$. The evolution of $\tau_j$ factors from its earlier ideal output pairs, so its distance from $\tau_{j+1}$ is exactly the one-pair error $\varepsilon_L$. The triangle inequality gives

$$
D(\rho_{j+1},\tau_{j+1})
\leq D(\rho_j,\tau_j)+\varepsilon_L.
$$

Since $\rho_0=\tau_0$, induction proves

$$
D\!\left(\rho_m,\sigma_L\otimes|+\rangle\langle+|^{\otimes N}\right)
\leq m\varepsilon_L
\leq\frac{7N}{\sqrt6}\sin^2\!\frac\pi L
\leq\frac{7\pi^2}{\sqrt6}\frac{N}{L^2}.
$$

Every trace-distance bound can also be capped at one. The coefficient $7\pi^2/\sqrt6$ is less than $29$.

The proof allows the actual reference to become correlated with earlier outputs. It does not replace that correlated state by a reset reference or assume statistically independent errors. Approximate product return is the conclusion of the full comparison.

## Reference energy and coherent-output budget

For any $0<\delta\leq1$, choose

$$
L=\left\lceil\sqrt{\frac{29N}{\delta}}\right\rceil.
$$

For even $N\geq2$, this choice satisfies $L\geq3$ and gives global trace error at most $\delta$. The initial reference mean excitation is

$$
E_L=\frac L2-1,
\qquad
E_L+1\leq\frac12\sqrt{\frac{29N}{\delta}}+\frac12.
$$

Together with the [mean-energy converse](converse.md), this establishes the stated $\Theta(\sqrt{N/\delta})$ reference-energy law for small $\delta$. The resource is the reference's initial mean energy above its ground state. The $N/2$ excitation initially supplied in the qubit register is separate. Neither the reference nor the total preparation energy is zero cost.

Equivalently, the construction guarantees a coherent-output budget proportional to $\delta(E_L+1)^2$, with even output size and integer rounding understood. The identical processor can be used until that batch budget is reached. The theorem does not assert indefinite reuse at a fixed global error.

## Stability under preparation and channel errors

This deterministic stability statement makes no independence assumption about accumulated reference/output correlations. Let the actual initial reference state be $\widetilde\sigma_L$ with

$$
D(\widetilde\sigma_L,\sigma_L)\leq\eta.
$$

At use $j$, suppose the implemented pair channel $\widetilde{\mathcal U}_j$ differs from the ideal $\mathcal U_L(\cdot)=U_L(\cdot)U_L^\dagger$ by

$$
\frac12\|\widetilde{\mathcal U}_j-\mathcal U_L\|_\diamond\leq\zeta_j.
$$

The diamond norm includes arbitrary external systems, so this bound remains applicable when the reference is correlated with every earlier output. A channel hybrid and the preceding state hybrid give

$$
D\!\left(\widetilde\rho_m,
\sigma_L\otimes|+\rangle\langle+|^{\otimes N}\right)
\leq\eta+\sum_{j=1}^m\zeta_j+m\varepsilon_L.
$$

If the return target is the actual prepared state $\widetilde\sigma_L$ rather than the nominal $\sigma_L$, an additional endpoint comparison gives

$$
D\!\left(\widetilde\rho_m,
\widetilde\sigma_L\otimes|+\rangle\langle+|^{\otimes N}\right)
\leq2\eta+\sum_{j=1}^m\zeta_j+m\varepsilon_L.
$$

Thus a sufficient global error allocation is $\eta=O(\delta)$ and $\zeta_j=O(\delta/N)$ at each use, together with $L^2=\Omega(N/\delta)$. This is an error budget, not a control-synthesis theorem. Tests of isolated output marginals cannot replace the stated channel norm assumption.

The stability bound also applies to noncovariant implementation errors as an approximation statement. Such errors may supply extra asymmetry; the exact covariant converse cannot be applied to that enlarged resource model without charging it separately.

If preparation errors stay within the finite ladder, the mean-energy deviation obeys

$$
|\operatorname{Tr}H_R(\widetilde\sigma_L-\sigma_L)|
\leq(L-2)\eta.
$$

Trace distance alone does not control energy for leakage into an unbounded spectrum; that energy must be specified independently.

## What the result supplies

The protocol gives independent coherent outputs and reference return in one joint trace-distance statement. It uses finite reference energy, fixed pair-sized interactions, exact conservation in the ideal processor, and deterministic error accounting. The result concerns a known state-preparation task. It does not implement an arbitrary unknown-input gate or a universal measurement channel. Hardware time, control synthesis, reference preparation, and their energetic costs remain distinct implementation questions.

[Exact processor](construction.md) · [Mean-energy converse](converse.md) · [Finite verification](../verification/README.md)
