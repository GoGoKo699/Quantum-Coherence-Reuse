# From Watrous to a reusable coherent-state source

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**, using the manuscript posted on the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The author's [current books page](https://jhwatrous.github.io/books-and-courses.html) also identifies the book and its manuscript. Use those authorized sources for the text; this repository does not reproduce or redistribute it. Section and theorem numbers below refer to that 2018 manuscript.

The book supplies the language of states, channels, measurements, distinguishability, and fidelity. The project supplies the symmetry condition, the first-moment energy estimate, the charge-sector construction, and the resulting resource theorem. Primary research papers in [related work](../references/RELATED_WORK.md) provide scientific attribution; they are not additional educational anchors.

The destination is the [joint-return theorem](../science/model.md): preparing $N$ independent coherent qubits while returning the initial reference costs mean reference energy of order $\sqrt{N/\delta}$ at global half trace error $\delta$. The input pairs already contain the output's mean energy. Reference energy and total supplied energy remain distinct.

## A compact source map

| Book location | Foundation to extract | Where it enters this project |
| --- | --- | --- |
| §§1.1.1–1.1.3, especially §1.1.3, *Operator decompositions and norms* | Tensor products, projections, spectral decompositions, trace norm, unitary invariance | One complete reference-plus-output state; total-charge blocks; exact pure-state error |
| §1.2.2, *Probability theory* | Probability vectors, expectation, elementary bounds | Reference energy probabilities and the binomial output charge law |
| §§2.1.2–2.1.3, *Quantum states of registers* and *Reductions and purifications of quantum states* | Density operators, partial trace, extensions, purification | Mixed reference states, complete product return, and a mathematical purification used only in the converse |
| §§2.2.1–2.2.2, channel definitions and representations | Complete positivity, trace preservation, unitary and environment descriptions | Covariant CPTP converse class and the narrower closed conserving construction |
| §§2.3.1–2.3.2, measurements | POVM effects, outcome probabilities, retained records | The Helstrom measurement used to prove the product distinguishability bound |
| §3.1.1 and Theorem 3.4, *Holevo–Helstrom theorem* | Binary discrimination and trace norm | Why the global error controls every joint test; the mixed-reference lower bound |
| §§3.2.1–3.2.3; Definition 3.11; Theorems 3.22, 3.27, 3.33 | Root fidelity, purification overlap, channel monotonicity, Fuchs–van de Graaf inequalities | Converting sector overlap to actual trace error and controlling the reference orbit |
| §§3.3.2–3.3.3, completely bounded trace norm and channel distances | Channel error stable under an untouched external register | Implementation errors when the reference is already correlated with older outputs |

Read this map together with the [30 project milestones](MILESTONES.md). The milestones follow the argument; this page explains the translations and the steps that the book alone does not provide.

## Notation and normalization

Watrous usually writes vectors as $u$ and their adjoints as $u^\ast$. Here $|u\rangle$ is the same vector, $\langle u|$ its adjoint, and $|u\rangle\langle u|$ the rank-one density operator $uu^\ast$. A density operator is positive semidefinite with trace one. The symbols $R$ and $S$ name registers; $\sigma_R$ and $\eta_N$ name their states.

| Quantity | Convention used here |
| --- | --- |
| State distance | $D(\rho,\tau)=\tfrac12\Vert \rho-\tau\Vert _1$; this is half the raw norm |
| Book fidelity | $F_{\mathrm W}(\rho,\tau)=\Vert \sqrt\rho\sqrt\tau\Vert _1$, the unsquared or root fidelity of Definition 3.11 |
| Squared fidelity, when used | $F_{\mathrm{sq}}=F_{\mathrm W}^2$; it is a different convention, not a second distance |
| Channel error | $\tfrac12\Vert \widetilde\Phi-\Phi\Vert _\diamond$; Watrous's completely bounded trace norm, written $\lVert\lVert\lVert\cdot\rVert\rVert\rVert_1$, is the unhalved diamond norm |
| Energy | $E=\mathrm{Tr}(H_R\sigma_R)$ with $H_R\geq0$, measured above its spectral infimum in units of the qubit gap |

For normalized pure vectors,

$$
F_{\mathrm W}(|u\rangle\langle u|,|v\rangle\langle v|)
=|\langle u|v\rangle|,
\qquad
D(|u\rangle\langle u|,|v\rangle\langle v|)
=\sqrt{1-|\langle u|v\rangle|^2}.
$$

For arbitrary states, Theorem 3.33 becomes

$$
1-F_{\mathrm W}(\rho,\tau)
\leq D(\rho,\tau)
\leq\sqrt{1-F_{\mathrm W}(\rho,\tau)^2}.
$$

A bound on $1-F_{\mathrm W}$ is therefore not automatically a bound of the same order on $D$. The construction computes its overlap directly and then uses the correct square root.

## From a compound register to the actual return condition

The compound-register framework of Chapter 2 makes the scored object unambiguous. The ideal final state is

$$
\tau_N=\sigma_R\otimes(|+\rangle\langle+|)^{\otimes N}.
$$

The same initial $\sigma_R$ appears at the end, and every output qubit remains in the comparison. A partial trace discards information, so closeness to $\tau_N$ implies closeness of every marginal. The converse implication fails: for instance,

$$
\frac12|00\rangle\langle00|+\frac12|11\rangle\langle11|
\quad\text{and}\quad \frac{I_4}{4}
$$

have identical one-qubit marginals but different joint statistics. This example explains why checking only the reference or one emitted qubit cannot prove independent outputs. The [sequential proof](../science/sequential_reuse.md) retains the complete compound register at every step.

## From channels to the symmetry restriction

Chapter 2 defines a channel by complete positivity and trace preservation. Symmetry is an additional project assumption:

$$
\Lambda(U_t\rho U_t^\dagger)
=U_t\Lambda(\rho)U_t^\dagger,
\qquad U_t=e^{-it(H_R+Q_N)}.
$$

This says that rotating the input phase and then processing has the same effect as processing and then rotating the output. The known input $|01\rangle^{\otimes N/2}$ is unchanged as a density operator by that rotation.

A closed unitary commuting with $H_R+Q_N$ defines such a channel. More general covariant channels can exchange energy with an invariant environment, so covariance alone does not preserve the total-energy distribution on $RS$. The [converse](../science/converse.md) uses the larger channel class; the [attaining construction](../science/construction.md) is a member of the narrower closed-unitary class. Channel representation theorems justify the language, while the actual symmetry and resource restrictions are specified in [the model](../science/model.md).

## From discrimination to the mixed-reference converse

For equally likely alternatives, the Holevo–Helstrom theorem gives optimal guessing probability $(1+D(\rho,\tau))/2$. Thus a global error at most $\delta$ limits the change of every measurement event probability to at most $\delta$. It also makes it possible to compare how much extra phase information the desired outputs would carry.

The project needs a product inequality beyond the book's basic discrimination theorem. Let $d=D(\rho,\tau)$ and let $a,b$ be pure states with squared overlap $s$. A Helstrom measurement on the first register produces probabilities $p_i,q_i$ with

$$
\frac12\sum_i|p_i-q_i|=d,
\qquad \sum_i\min(p_i,q_i)=1-d.
$$

In each resulting classical block, the operator $p_i a-q_i b$ acts on at most a two-dimensional space. Its trace and determinant give

$$
\Vert p_i a-q_i b\Vert _1
=\sqrt{(p_i-q_i)^2+4p_iq_i(1-s)}.
$$

Rationalizing the square root bounds this by $|p_i-q_i|+2\min(p_i,q_i)(1-s)$ from below. Summing the blocks and using measurement contractivity proves

$$
D(\rho\otimes a,\tau\otimes b)
\geq d+(1-s)(1-d).
$$

This is a guaranteed discrimination performance, not an asserted equality for arbitrary mixed tensor products.

Now compare a reference with its phase rotation $\sigma_t$ and write $d_R(t)=D(\sigma_R,\sigma_t)$. Contractivity of the preparation channel bounds the actual output-orbit distance by $d_R(t)$. Two endpoint errors of at most $\delta$ compare those actual outputs with their ideal products. The preceding inequality then gives

$$
2\delta\geq[1-s_N(t)][1-d_R(t)],
\qquad s_N(t)=\cos^{2N}(t/2).
$$

This connects Chapter 3's discrimination tools to the quantitative problem: independent coherent outputs would increase orbit distinguishability, while returning the reference leaves little room to do so accurately.

## Where the infinite-dimensional first-moment argument is supplied

Watrous formulates the book using finite-dimensional complex Euclidean spaces. The attaining ladder here is finite and fits that framework. The converse deliberately permits infinite-dimensional trace-class reference states and unbounded positive Hamiltonians, so the relevant extension is proved here rather than attributed to the book.

For a self-adjoint $H_R\geq0$, its spectral projections define a probability measure $\mu$ through the state $\sigma_R$. Finite mean energy means $\int x d\mu(x)=E<\infty$. Therefore

$$
A(t)=\mathrm{Tr}(\sigma_Re^{-itH_R})
=\int e^{-itx} d\mu(x),
\qquad |1-A(t)|\leq |t|E.
$$

The last inequality follows by integrating $|1-e^{-itx}|\leq|t|x$. It uses no derivative at zero and no second moment.

For a trace-class state, a spectral expansion gives a finite or countable purification $|\Omega\rangle=\sum_a\sqrt{\lambda_a}|u_a\rangle|a\rangle$. Rotating only its first factor gives overlap $A(t)$. The two-pure-state formula above, followed by partial trace, yields

$$
d_R(t)\leq\sqrt{1-|A(t)|^2}
\leq\sqrt{2|t|E}\qquad(|t|E\leq1).
$$

The pure-state formula remains a two-dimensional calculation even when the ambient space is infinite. Contractivity on Hermitian trace-class differences follows directly from their positive and negative parts: a positive trace-preserving map sends $X_+-X_-$ to a difference whose trace norm is at most $\mathrm{Tr}X_++\mathrm{Tr}X_-=\Vert X\Vert _1$. These observations supply the extension used here. The purification is a proof device, not a free processor input or a system that the task requires to return.

Choosing $t=1/[8(E+1)]$ keeps the reference orbit distance at most $1/2$; the target orbit has $s_N(t)\leq e^{-Nt^2/4}$. Substitution gives the [explicit lower bound](../science/converse.md#4-explicit-finite-energy-lower-bound). A separate constant-energy floor removes the additive one uniformly. The final theorem concerns every even $N\geq2$ and $0<\delta\leq1/8$, not only one fixed $N$ limit.

## From spectral blocks and fidelity to an attaining processor

The spectral-decomposition tools of Chapter 1 split the reference-plus-pair space into total-charge sectors. The initial pair $|01\rangle$ has sharp charge one. Within a sector, the construction maps its one occupied input vector onto the normalized projection of $|R_L\rangle|++\rangle$. Such a unit-vector map extends to a unitary on that sector; the explicit [Householder block](../science/construction.md#charge-sector-alignment) gives the extension, including all unused directions.

Let the initial and desired sector probabilities be $p_k$ and $q_k$. A unitary cannot change the initial sector weights. Cauchy–Schwarz bounds the overlap contribution from each sector by $\sqrt{p_kq_k}$, and alignment attains their sum:

$$
B(p,q)=\sum_k\sqrt{p_kq_k},
\qquad \varepsilon_L=\sqrt{1-B(p,q)^2}.
$$

Here $B$ is the root fidelity of the corresponding diagonal states. Define the unnormalized Hellinger distance by

$$
\mathsf H(p,q)=\Vert \sqrt p-\sqrt q\Vert _2,
\qquad \mathsf H(p,q)^2=2(1-B(p,q)).
$$

Then $\varepsilon_L\leq\mathsf H(p,q)$. The profile $p_r\propto\sin^4[\pi(r+1)/L]$ has mean energy $L/2-1$. Its smoothness makes the one-pair lazy-walk change $q-p$ a small second difference. The [boundary-inclusive estimate](../science/construction.md#uniform-sine-profile-estimate) proves $\mathsf H(p,q)=O(L^{-2})$; that estimate, not fidelity notation alone, supplies the useful power of $L$.

For completeness, Hellinger contraction under a classical channel $K$ follows from Cauchy–Schwarz:

$$
\sqrt{(Kp)_i(Kq)_i}\geq\sum_jK_{ij}\sqrt{p_jq_j}.
$$

Summing gives $B(Kp,Kq)\geq B(p,q)$. Combining this with the Euclidean triangle inequality gives $\mathsf H(p,P^mp)\leq m\mathsf H(p,Pp)$ for the lazy walk $P$. This connects probability vectors to the collective benchmark; sequential operation still needs the whole-state argument below.

## From contractivity to honest sequential reuse

Let $\rho_j$ be the actual reference and first $j$ output pairs, and let $\tau_j=\sigma_L\otimes|++\rangle\langle++|^{\otimes j}$. Append the same fresh $|01\rangle$ to both and apply the same next processor. Their distance does not increase. The evolved ideal state is within one-pair error $\varepsilon_L$ of $\tau_{j+1}$. Hence

$$
D(\rho_{j+1},\tau_{j+1})
\leq D(\rho_j,\tau_j)+\varepsilon_L,
\qquad D(\rho_{N/2},\tau_{N/2})\leq\frac N2\varepsilon_L.
$$

Earlier outputs remain present, even when correlated with the actual reference. No reset or independent-error model appears. Together with $\varepsilon_L=O(L^{-2})$ and $E_L=\Theta(L)$, this yields the upper reference-energy order.

Sections 3.3.2–3.3.3 explain why a channel error must allow an untouched external register. In reuse, those external registers are the old outputs. If the initial preparation error is $\eta$ and use $j$ has half-diamond error at most $\zeta_j$, a channel hybrid gives

$$
D(\widetilde\rho_{N/2},\tau_{N/2})
\leq\eta+\sum_{j=1}^{N/2}\zeta_j+\frac N2\varepsilon_L.
$$

Scoring return to the actual prepared reference rather than the nominal one adds another $\eta$. These are deterministic error bounds; an isolated-input or marginal test cannot replace the diamond-norm premise.

## From bounded observables to the resource limits

On the finite ladder, $0\leq H_R\leq(L-2)I$. The same measurement-distance interpretation gives

$$
|\mathrm{Tr}[H_R(\rho-\tau)]|
\leq(L-2)D(\rho,\tau).
$$

There is no analogous energy-continuity bound from trace distance alone on an unbounded spectrum: a probability $\eta$ placed at energy $M$ can add order $\eta M$ mean energy while changing the state by at most $\eta$. This is why the broad converse states its first-moment assumption explicitly, and why implementation leakage needs separate energy accounting.

The [resource account](../science/resource_accounting.md) completes the bridge: all asymmetric inputs belong to the counted reference; the balanced qubits separately supply $N/2$ excitations; and number-selective control, preparation work, time, locality, and gate synthesis are not optimized by the mean-reference-energy theorem. These qualifications explain the physical quantity that the mathematical optimum measures.
