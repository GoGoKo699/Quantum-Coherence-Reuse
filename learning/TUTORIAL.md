# A worked route to the coherent-output budget

This tutorial develops the [30 milestones](MILESTONES.md) as one connected argument. Its single textbook anchor is John Watrous, *The Theory of Quantum Information* (2018); the [Watrous bridge](WATROUS_BRIDGE.md) gives section references and translates conventions. The symmetry assumptions and the particular reference-energy theorem are supplied here. Research papers cited through [related work](../references/RELATED_WORK.md) identify inherited scientific foundations.

The destination is a precise resource law: to prepare an even number $N$ of coherent qubits while approximately returning their phase reference, the optimal initial mean reference energy is

$$
E_{\min}(N,\delta)=\Theta\left(\sqrt{N/\delta}\right),
\qquad N\geq2,\quad 0<\delta\leq\tfrac18.
$$

The error $\delta$ concerns the reference and the **entire output batch together**. The qubits separately arrive with $N/2$ excitations. The theorem optimizes reference mean energy; it does not optimize the total work, time, or circuitry needed to build the source.

## 1. Energy statistics do not specify coherence

Route: [M01–M03](MILESTONES.md).

A density operator is a positive semidefinite matrix with trace one; it describes both pure states and mixtures. The symbol $I_d$ denotes the identity on a $d$-dimensional register. A qubit has energy eigenstates $|0\rangle$ and $|1\rangle$, with excitations zero and one. The coherent state

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}
$$

has density matrix $|+\rangle\langle+|$. Its diagonal entries are both $1/2$, but its off-diagonal entries are also $1/2$. The incoherent mixture $I_2/2$ has the same energy statistics and mean excitation, yet its off-diagonal entries vanish. Supplying the right average energy alone does not prepare $|+\rangle$.

For a batch, the intended density operator is

$$
\psi_N=(|+\rangle\langle+|)^{\otimes N}.
$$

The tensor product specifies independence as well as individual states. In general, marginal states cannot establish independence: the correlated state $(|00\rangle\langle00|+|11\rangle\langle11|)/2$ and the product $I_4/4$ have identical one-qubit marginals but different joint statistics.

The source processes fresh pairs initially in $|01\rangle$. Each input pair has **exactly** one excitation. The desired $|++\rangle$ pair also has mean excitation one, but its total charge takes values zero, one, and two with probabilities $1/4,1/2,1/4$. This distinction between a sharp charge and charge fluctuations drives the construction.

## 2. The phase reference and the allowed process

Route: [M04–M05](MILESTONES.md).

Let $R$ be the reference register, $H_R$ its Hamiltonian above its spectral infimum, and $\sigma_R$ its initial density operator. Thus $H_R\geq0$, and the charged resource is its mean energy

$$
E=\mathrm{Tr}(H_R\sigma_R)<\infty.
$$

The reference starts independently of the qubits. The qubit charge operator $Q_N$ adds their individual excitations. A time shift $t$ rotates a joint state by

$$
U_t=e^{-it(H_R+Q_N)}.
$$

An energy eigenstate is unchanged as a density operator by this rotation. The state $|+\rangle$ acquires a relative phase between its two components. The reference can carry the phase relation needed to produce such states.

A quantum channel is a linear, completely positive, trace-preserving map: it sends states to states and remains physically valid when an external register is retained. The complete preparation channel $\Lambda$ must be time-translation covariant:

$$
\Lambda(U_t\rho U_t^\dagger)
=U_t\Lambda(\rho)U_t^\dagger.
$$

Rotating the input and then processing therefore has the same effect as processing and then rotating the output. The apparatus cannot import an uncounted phase standard. Auxiliary inputs must be jointly invariant and initially independent; invariant individual marginals would not exclude asymmetric correlations.

A unitary commuting with total excitation gives a covariant channel. General covariant channels are a larger class: an invariant environment can exchange energy with the system. The lower bound covers that larger class, while the attaining processor will be closed and exactly conserving.

## 3. A distance that scores the whole source

Route: [M06–M08](MILESTONES.md).

Use half trace distance, where $\Vert X\Vert _1$ is the sum of the singular values of $X$:

$$
D(\rho,\tau)=\tfrac12\Vert \rho-\tau\Vert _1.
$$

For equally likely alternatives, the best discrimination success probability is $(1+D)/2$. Thus $D\leq\delta$ means that every measurement event probability changes by at most $\delta$, including measurements on many registers together.

Three properties make this distance useful through a protocol: channels cannot increase it; an unchanged tensor factor does not change it; and the triangle inequality permits intermediate comparison states. These statements concern complete states, without an independence assumption about the actual errors.

Watrous uses **root fidelity**,

$$
F_{\mathrm W}(\rho,\tau)=\Vert \sqrt\rho\sqrt\tau\Vert _1.
$$

Some sources instead call $F_{\mathrm W}^2$ fidelity. For pure vectors $|a\rangle,|b\rangle$,

$$
F_{\mathrm W}=|\langle a|b\rangle|,
\qquad
D=\sqrt{1-|\langle a|b\rangle|^2}.
$$

Keeping the square is essential: an overlap deficit of order $x$ generally guarantees trace error only of order $\sqrt x$.

## 4. State the complete contract before optimizing energy

Route: [M09–M12](MILESTONES.md).

For even $N$, write the known qubit input as

$$
\eta_N=(|01\rangle\langle01|)^{\otimes N/2}.
$$

If $\omega=\Lambda(\sigma_R\otimes\eta_N)$ is the actual output, the scored error is

$$
D(\omega,\sigma_R\otimes\psi_N)\leq\delta.
$$

The same initial reference appears in the target, independently of all output qubits. This is stronger than inspecting its final marginal or inspecting each qubit alone. The reference is a known supplied state, not an unknown borrowed register that the processor must preserve for every possible input. No return of an inaccessible purification is required.

The optimization defining $E_{\min}$ permits any nonnegative reference Hamiltonian, mixed reference state of finite mean energy, and covariant preparation channel. A hard support cutoff, finite dimension, or finite variance is not imposed. Finite mean energy does not imply finite variance: a sufficiently small high-energy tail can keep the first moment finite while making the second moment diverge.

The upper-bound reference will be a convenient finite ladder. Its finite width is a feature of that example, not a hidden assumption in the lower bound.

## 5. Independent coherent outputs add orbit information

Route: [M13–M17](MILESTONES.md).

The converse compares the reference with its time-shifted state

$$
\sigma_t=e^{-itH_R}\sigma_Re^{itH_R},
\qquad d_R(t)=D(\sigma_R,\sigma_t).
$$

For the target batch, the exact squared overlap with its shifted vector is

$$
s_N(t)=\left|\frac{1+e^{-it}}2\right|^{2N}
=\cos^{2N}(t/2).
$$

There is a useful mixed-state discrimination inequality. If $d=D(\rho,\tau)$ and pure states $a,b$ have squared overlap $s$, then

$$
D(\rho\otimes a,\tau\otimes b)
\geq d+(1-s)(1-d).
$$

To see its source, perform the optimal Helstrom measurement on the first register. Let its outcome probabilities be $p_i,q_i$, so that $\sum_i\min(p_i,q_i)=1-d$. In each retained outcome block,

$$
\Vert p_i a-q_i b\Vert _1
=\sqrt{(p_i-q_i)^2+4p_iq_i(1-s)}.
$$

The square root is at least $|p_i-q_i|+2\min(p_i,q_i)(1-s)$. Summing the blocks proves the inequality. It is a lower bound on achievable discrimination, not an equality for arbitrary mixed tensor products.

Covariance and channel contractivity bound the distance between the two actual output orbits by $d_R(t)$. Each actual output is within $\delta$ of its ideal product. Two endpoint comparisons therefore give

$$
2\delta\geq[1-s_N(t)][1-d_R(t)].
$$

The ideal outputs would add time-translation information; a covariant source cannot add that information while returning the reference arbitrarily accurately.

Only mean energy is needed to control the reference side. Let $\mu$ be the spectral energy distribution of $H_R$ in $\sigma_R$. Its characteristic function obeys

$$
A(t)=\int e^{-itx} d\mu(x),
\qquad |1-A(t)|\leq |t|\int x d\mu(x)=|t|E.
$$

The inequality integrates $|1-e^{-itx}|\leq|t|x$; it never differentiates the characteristic function or invokes a second moment. A mathematical purification has overlap $A(t)$ with its rotated vector. Pure-state distance and partial-trace contractivity then imply

$$
d_R(t)\leq\sqrt{1-|A(t)|^2}
\leq\sqrt{2|t|E},\qquad |t|E\leq1.
$$

This use of purification supplies a bound, not an extra laboratory system or a return requirement.

Choose $t=1/[8(E+1)]$. The reference distance is at most $1/2$, while $\cos x\leq e^{-x^2/2}$ gives

$$
\boxed{
\delta\geq\frac14
\left(1-e^{-N/[256(E+1)^2]}\right).
}
$$

For $\delta\leq1/8$, inversion yields

$$
E+1\geq\frac1{32\sqrt2}\sqrt{N/\delta}.
$$

Removing the additive one requires a separate check. At $t=\pi$, the target orbit states are orthogonal, so $d_R(\pi)\geq1-2\delta$. If $\pi E\leq1$, the same reference estimate gives $E\geq(1-2\delta)^2/(2\pi)$. If $\pi E>1$, that energy floor already holds. In the stated error domain this floor exceeds $1/16$, hence $E+1\leq17E$. This supplies a uniform lower bound on $E$ itself. The [complete converse](../science/converse.md) retains all constants and quantifiers.

## 6. A smooth finite reference and a conserving processor

Route: [M18–M24](MILESTONES.md).

Choose $L\geq3$ and reference energies $r=0,\ldots,L-2$. Define

$$
|R_L\rangle=\sum_{r=0}^{L-2}\sqrt{p_r}|r\rangle,
\qquad
p_r=\frac{8}{3L}\sin^4\frac{\pi(r+1)}L.
$$

The probabilities sum to one, and their reflection symmetry gives mean energy $E_L=L/2-1$.

The initial pair has charge one. The desired $|++\rangle$ pair has centered charge shifts $-1,0,1$ with weights $1/4,1/2,1/4$. Consequently its product with the reference has centered total-charge probabilities

$$
q_k=\frac14(p_{k-1}+2p_k+p_{k+1}),
$$

where $p_k=0$ outside the finite ladder. This is one step of a centered lazy random walk.

An exactly conserving unitary cannot change the initial probabilities of total-charge sectors. It can, however, rotate the occupied vector **within** each sector. In sector $\ell$, write $|e_\ell\rangle=|\ell-1,01\rangle$ for the input vector and map it onto the normalized projection $|v_\ell\rangle$ of $|R_L\rangle|++\rangle$ into that sector. Both vectors are normalized. A Householder reflection implements the map, with $I_\ell$ the identity on that sector:

$$
U_\ell=I_\ell-
2\frac{|w_\ell\rangle\langle w_\ell|}{\langle w_\ell|w_\ell\rangle},
\qquad w_\ell=e_\ell-v_\ell.
$$

Use the identity if the difference is zero or the input sector is unoccupied. The direct sum $U_L=\bigoplus_\ell U_\ell$ is unitary and commutes with total excitation. Each block has dimension at most four.

Sector alignment gives overlap and one-pair joint error

$$
B(p,q)=\sum_k\sqrt{p_kq_k},
\qquad \varepsilon_L=\sqrt{1-B(p,q)^2}.
$$

Cauchy–Schwarz in each sector shows that this overlap is optimal among conserving unitaries for the **fixed** pure reference and fixed input. It does not optimize every covariant channel or reference.

The normalized-target-sector mechanism is inherited from covariant recovery. In Marvian–Lloyd's explicit Petz map, the pure components have the form $\sum_\ell\sqrt{p_{\ell-a}}|v_\ell\rangle$. The precharged input pair permits the $a=1$ component to be realized deterministically by this conserving unitary. It is not obtained by measuring the Petz mixture or selecting a successful branch. [Related work](../references/RELATED_WORK.md#relationship-of-the-sector-construction-to-the-petz-map) explains that ancestry; neither approximate catalytic coherence nor a new general conversion principle is being introduced.

The quantitative step is a boundary-inclusive smoothness estimate. Define the unnormalized Hellinger distance

$$
\mathsf H(p,q)^2=\sum_k(\sqrt{p_k}-\sqrt{q_k})^2=2(1-B).
$$

Then $\varepsilon_L\leq\mathsf H(p,q)$. Put $\theta=\pi/L$ and $a=\sin^2\theta$. For $f(x)=\sin^4x$, its centered second difference satisfies

$$
f(x-\theta)-2f(x)+f(x+\theta)
=2a[\cos2x-(1-a)\cos4x].
$$

At the supported grid points its absolute value is at most $14a\sin^2x$. Dividing the squared probability change by $p$ bounds the interior Hellinger contribution. The two exterior sites, where the initial probability is zero, contribute an additional $4a^2/(3L)$. Including both parts gives

$$
\mathsf H(p,q)^2\leq\frac{98}{3}\sin^4\frac\pi L,
\qquad
\varepsilon_L\leq\sqrt{(98)/(3)}\sin^2\frac\pi L.
$$

The centered charge balance cancels first-order drift. The smooth profile also controls the finite boundaries. Together they give a full joint error of order $L^{-2}$, rather than merely small individual output errors.

## 7. Reuse without deleting old correlations

Route: [M25–M26](MILESTONES.md).

Apply the same $U_L$ to the reference and each fresh $|01\rangle$ pair. Let $\rho_j$ be the actual reference plus its first $j$ output pairs. Compare it with

$$
\tau_j=|R_L\rangle\langle R_L|
\otimes(|++\rangle\langle++|)^{\otimes j}.
$$

Append the same fresh pair to both states and apply the next processor. Their distance cannot increase. Acting on the ideal state introduces at most the one-pair error $\varepsilon_L$. Thus

$$
D(\rho_{j+1},\tau_{j+1})
\leq D(\rho_j,\tau_j)+\varepsilon_L.
$$

Starting from zero error and taking $j=N/2$ gives

$$
D(\rho_{N/2},\tau_{N/2})
\leq\frac N2\varepsilon_L
\leq\frac{7\pi^2}{\sqrt6}\frac N{L^2}
<29\frac N{L^2}.
$$

The original reference in $\tau_j$ is a mathematical comparison state. It is not physically reset between uses. Actual correlations with all older outputs remain in $\rho_j$ throughout.

Choose $L=\lceil\sqrt{29N/\delta}\rceil$. This gives error at most $\delta$ with $E_L=L/2-1=O(\sqrt{N/\delta})$. The broad mixed-reference converse supplies the matching lower order. A fixed pair interface therefore attains the global optimum in mean-energy **order**, without claiming the exact optimal finite error or an efficient hardware controller.

## 8. Imperfections need a correlation-uniform budget

Route: [M27](MILESTONES.md).

Suppose the actual initial reference $\widetilde\sigma_L$ differs from its nominal state $\sigma_L$ by $D(\widetilde\sigma_L,\sigma_L)\leq\eta$. At call $j$, suppose the implemented channel differs from the ideal pair channel by half diamond norm at most $\zeta_j$.

The diamond norm permits an untouched external register. Here those external registers are the older outputs, which may already be correlated with the reference. Repeating the hybrid comparison gives

$$
D(\widetilde\rho_{N/2},\sigma_L\otimes\psi_N)
\leq\eta+\sum_{j=1}^{N/2}\zeta_j+\frac N2\varepsilon_L.
$$

Scoring return to $\widetilde\sigma_L$ instead of $\sigma_L$ adds another $\eta$. Reserve separate constant fractions of the total tolerance for preparation, channel errors, and the ideal processor; use the allocated ideal-error tolerance in the choice of $L$. Preparation error of order $\delta$ and per-use channel errors of order $\delta/N$ are then sufficient, with the same reference-energy order. These are declared calibration requirements, not a demonstration that a particular apparatus achieves them. Tests on an isolated qubit or an uncorrelated reference do not establish the diamond-norm premise.

## 9. Work through a three-level reference

Route: [M28](MILESTONES.md).

Set $L=4$. There are three reference energies, zero, one, and two, with

$$
|R_4\rangle=\frac1{\sqrt6}|0\rangle+
\sqrt{2/3}|1\rangle+\frac1{\sqrt6}|2\rangle.
$$

Its mean reference energy is one. After centering the input pair's charge at one, the initial and desired sector probabilities are

| Centered sector index $k$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Initial $p_k$ | $0$ | $1/6$ | $2/3$ | $1/6$ | $0$ |
| Desired $q_k$ | $1/24$ | $1/4$ | $5/12$ | $1/4$ | $1/24$ |

The two outer target sectors have no initial weight. A conserving unitary cannot create that weight, so an exact product target is impossible for this finite reference.

At total charge one, the occupied input vector $|0,01\rangle$ is mapped to

$$
|v_1\rangle=\sqrt{2/3}|1,00\rangle+
\frac1{\sqrt6}|0,01\rangle+
\frac1{\sqrt6}|0,10\rangle.
$$

Every term has total excitation one. At total charge two, $|1,01\rangle$ is mapped to

$$
\begin{aligned}
|v_2\rangle={}&\frac1{\sqrt{10}}|0,11\rangle
+\sqrt{2/5}|1,01\rangle\\
&+\sqrt{2/5}|1,10\rangle
+\frac1{\sqrt{10}}|2,00\rangle.
\end{aligned}
$$

The charge-three sector follows by reflection and qubit complementation. Householder blocks complete these vector maps to one unitary on every input direction.

The exact overlap is the sum over the three occupied sectors:

$$
B=\frac1{\sqrt6}+\sqrt{5/18}
\approx0.935295,
\qquad
\varepsilon_4=\sqrt{1-B^2}\approx0.353870.
$$

This small device illustrates the complete mechanism; it is not a small-error design. At larger finite sizes, the [verification program](../verification/README.md) constructs and reuses the actual full matrix, retains the reference and all outputs, and evaluates their density-matrix difference directly. Such checks test the specified finite processor. They do not prove the mixed-reference converse or the uniform scaling theorem.

## 10. Read the budget with its physical qualifications

Route: [M29–M30](MILESTONES.md).

The main optimum can be read as a coherent-output budget of order $\delta E^2$ in the nontrivial even-output regime. Its reference energy is distinct from several other quantities:

| Quantity | What the theorem supplies |
| --- | --- |
| Initial reference mean energy | Optimized to matching order $\sqrt{N/\delta}$ |
| Input qubit energy | $N/2$ excitations supplied separately |
| Initial total mean energy in the construction | $N/2+E_L$ |
| Reference preparation and phase calibration | Specified resource state and error requirements; preparation work is not optimized |
| Pair control | Explicit exactly conserving finite blocks; native synthesis, locality, strength, and duration are not optimized |
| Output quality | One full product approximation, preserved by every later joint channel |

The finite ladder has dimension $L-1$ and width $L-2$, but the lower bound is about mean energy across arbitrary spectra. It must not be relabelled an unrestricted dimension theorem. Trace distance controls energy differences on a bounded ladder; leakage into an unbounded high-energy tail needs separate energy accounting.

Approximate catalytic coherence, quadratic reference longevity, warnings about correlations, and Petz recovery are inherited foundations. The result established here is the matching globally composable mean-energy budget under the stated task and return criterion. A known coherent-state source is different from a gate on arbitrary unknown inputs, indefinite reuse at fixed error, or a free source of the qubits' mean energy.

[Milestone map](MILESTONES.md) · [Watrous source bridge](WATROUS_BRIDGE.md) · [Complete scientific account](../science/README.md)
