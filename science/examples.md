# Worked examples

These examples use the [finite conserving processor](construction.md) and half trace distance. The exact formulas concern ideal matrices; decimal values are finite floating-point evaluations.

## A three-level reference

Choose $L=4$. The reference has levels $r=0,1,2$ and state

$$
|R_4\rangle=\frac1{\sqrt6}|0\rangle+
\sqrt{\frac23}|1\rangle+\frac1{\sqrt6}|2\rangle.
$$

Its mean excitation is one. For a fresh $|01\rangle$ pair, the initial centered charge distribution is $p=(1/6,2/3,1/6)$. The desired product has centered total-charge probabilities

$$
(q_{-1},q_0,q_1,q_2,q_3)
=\left(\frac1{24},\frac14,\frac5{12},\frac14,\frac1{24}\right).
$$

At total charge $\ell=1$, the processor sends the occupied input vector $|0,01\rangle$ to

$$
|v_1\rangle=\sqrt{\frac23}|1,00\rangle+
\frac1{\sqrt6}|0,01\rangle+\frac1{\sqrt6}|0,10\rangle.
$$

At total charge $\ell=2$, it sends $|1,01\rangle$ to

$$
|v_2\rangle=
\frac1{\sqrt{10}}|0,11\rangle+
\sqrt{\frac25}|1,01\rangle+
\sqrt{\frac25}|1,10\rangle+
\frac1{\sqrt{10}}|2,00\rangle.
$$

The charge-three vector follows by reflection of the ladder and complementing both qubits. A Householder block maps each occupied input vector to its stated normalized output; identity blocks complete the unoccupied outer sectors. Every term within a block has the same total excitation.

The exact one-pair overlap and error are

$$
B=\frac1{\sqrt6}+\sqrt{\frac5{18}},
\qquad
\varepsilon_4=\sqrt{1-B^2}.
$$

The small reference illustrates the entire construction, including unavoidable weight in ideal total-charge sectors absent from the input. It is not intended as a small-error device. The analytical bound can be loose at these small sizes; the exact overlap remains available.

## Reusing the same finite processor

The verification program constructs the full unitary from its charge blocks and applies it repeatedly to a reference and fresh pairs, retaining every output. It evaluates the density-matrix difference directly rather than using the overlap formula to compute the sequential error.

| Reference choice | Initial reference mean excitation | One-pair joint error | Three-pair joint error | Three-use hybrid bound |
| --- | ---: | ---: | ---: | ---: |
| $L=8$, seven levels | 3 | 0.135544 | 0.325872 | 0.406631 |
| $L=16$, fifteen levels | 7 | 0.042408 | 0.115433 | 0.127224 |

The repeated processor may correlate the actual reference with earlier outputs. The [hybrid proof](sequential_reuse.md) nevertheless compares the complete state with the original reference tensor all six ideal coherent qubits. The bound need not equal the finite optimum.

## A conservative design choice

For even $N$ and desired global error $\delta$, the sufficient choice

$$
L=\left\lceil\sqrt{\frac{29N}{\delta}}\right\rceil,
\qquad
E_L=\frac L2-1
$$

comes directly from the uniform proof. For $N=100$ and $\delta=0.01$, it gives $L=539$ and reference mean excitation $268.5$. The qubit inputs separately contain 50 excitations. For $N=10^6$ at the same tolerance, it gives $L=53852$ and reference mean excitation $26925$, while the input register contains $500000$ excitations.

These are sufficient reference inventories using deliberately loose constants. They are not optimized finite-device energies or estimates of state-preparation work, control duration, or laboratory cost.

## What local output checks would miss

A batch can have good one-qubit marginals while its correlations differ substantially from an independent product. The theorem avoids inferring the joint result from such marginals: its target is the complete product with the returned reference. Contractivity then gives every reduced-state guarantee as a consequence, and every later joint measurement has outcome-distribution error at most $\delta$.

[Model](model.md) · [Construction](construction.md) · [Finite verification](../verification/README.md)
