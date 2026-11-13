# Converse for arbitrary mixed finite-mean references

This proof bounds the full [joint-return task](model.md). It uses time-translation covariance and an initial first moment of energy. It does not assume a charge cutoff, a finite variance, a pure reference, a conserving unitary dilation, or that the reference's purification is physically available.

## 1. A product distinguishability inequality

Let $\rho,\tau$ be arbitrary density operators, and let $a=|a\rangle\langle a|$ and $b=|b\rangle\langle b|$ be pure states. Put

$$
d=D(\rho,\tau),
\qquad
s=|\langle a|b\rangle|^2.
$$

Then

**(1)**

$$
\boxed{
D(\rho\otimes a,\tau\otimes b)
\ge d+(1-s)(1-d).
}
$$

To prove it, perform an optimal Helstrom measurement on the first register. Such a binary measurement exists for trace-class states, by taking the positive and negative spectral subspaces of $\rho-\tau$. Let $p_i,q_i$ be its outcome probabilities. They obey

$$
\frac12\sum_i|p_i-q_i|=d,
\qquad
\sum_i\min(p_i,q_i)=1-d.
$$

The measured product states are block diagonal in $i$. For each block, the two weighted pure states satisfy

$$
\Vert p_i a-q_i b\Vert _1
=\sqrt{(p_i-q_i)^2+4p_iq_i(1-s)}.
$$

For nonnegative $p,q$ and $0\le h\le1$, rationalizing the square root gives

$$
\sqrt{(p-q)^2+4pqh}-|p-q|
\ge2\min(p,q)h.
$$

Indeed, the denominator after rationalization is at most
$p+q+|p-q|=2\max(p,q)$. Zero probabilities follow by continuity. Sum the block inequalities, divide by two, and use contractivity under the Helstrom measurement to obtain (1).

This is a lower bound obtained by a particular discrimination procedure. It is not a formula for the trace distance of arbitrary mixed tensor products.

## 2. Covariance turns return error into an orbit bound

Write

$$
\sigma_t=e^{-itH_R}\sigma_R e^{itH_R},
\qquad
\psi_t=e^{-itQ_N}\psi_Ne^{itQ_N},
\qquad
d_R(t)=D(\sigma_R,\sigma_t).
$$

Let $\omega=\Lambda(\sigma_R\otimes\eta_N)$ be the actual output and let
$\omega_t=e^{-it(H_R+Q_N)}\omega e^{it(H_R+Q_N)}$. The input qubit state is invariant, so covariance gives

$$
\omega_t=\Lambda(\sigma_t\otimes\eta_N).
$$

Contractivity therefore implies $D(\omega,\omega_t)\le d_R(t)$. If the joint preparation error is at most $\delta$, unitary invariance also gives

$$
D(\omega_t,\sigma_t\otimes\psi_t)\le\delta.
$$

The triangle inequality followed by (1) yields

$$
D(\sigma_R\otimes\psi_N,\sigma_t\otimes\psi_t)
\le d_R(t)+2\delta.
$$

Therefore

**(2)**

$$
\boxed{2\delta\ge[1-s_N(t)][1-d_R(t)].}
$$

where the exact target-orbit overlap is

**(3)**

$$
s_N(t)=|\langle+|^{\otimes N}e^{-itQ_N}|+\rangle^{\otimes N}|^2
=\cos^{2N}(t/2).
$$

Only the initial reference is rotated in the input comparison. No unknown parameter is supplied to the controls, and no measurement of the mathematical reference orbit is assumed to be part of the preparation protocol.

## 3. A first-moment reference-orbit estimate

Let $H_R\ge0$ and $E=\mathrm{Tr}(H_R\sigma_R)\lt \infty$. The spectral theorem defines a probability measure $\mu$ on $[0,\infty)$ such that

$$
A(t)=\mathrm{Tr}(\sigma_Re^{-itH_R})
=\int_0^\infty e^{-itx} d\mu(x),
\qquad
\int_0^\infty x d\mu(x)=E.
$$

Because $|1-e^{-itx}|\le |t|x$,

$$
|1-A(t)|\le |t|E.
$$

A purification of $\sigma_R$ has overlap $A(t)$ with the vector obtained by acting with $e^{-itH_R}$ on its reference component. Pure-state trace distance and partial-trace contractivity give

$$
d_R(t)\le\sqrt{1-|A(t)|^2}.
$$

For $|t|E\le1$, it follows that

**(4)**

$$
\boxed{
d_R(t)\le\sqrt{2|t|E-(|t|E)^2}
\le\sqrt{2|t|E}.
}
$$

The purification is used only to upper-bound a distance. It is not an auxiliary system supplied to the processor, and its state is not required to be returned. Equation (4) remains valid for continuous spectra and heavy energy tails because only the integrable function $x$ is used. No derivative in $t$, energy variance, or finite-dimensional approximation is invoked.

## 4. Explicit finite-energy lower bound

Choose

$$
t_E=\frac1{8(E+1)}.
$$

Then $t_EE\lt 1/8$, so (4) implies $d_R(t_E)\le1/2$. Also $0\lt t_E/2\le1/16$. The elementary inequality $\cos x\le e^{-x^2/2}$ on this interval, together with (3), gives

$$
s_N(t_E)
\le\exp\left[-\frac{N}{256(E+1)^2}\right].
$$

Substitution into (2) proves

**(5)**

$$
\boxed{
\delta\ge\frac14
\left(1-\exp\left[-\frac{N}{256(E+1)^2}\right]\right).
}
$$

This is positive for every finite $E$ and every $N\ge1$. Thus an infinite Hilbert space with a finite first moment does not permit exact independent coherent output with exact joint return.

For $0\lt \delta\lt 1/4$, rearranging (5) gives

**(6)**

$$
E+1\ge
\sqrt{(N)/(256[-\ln(1-4\delta)])}.
$$

When $\delta\le1/8$, the inequality
$-\ln(1-4\delta)\le4\delta/(1-4\delta)\le8\delta$ yields

**(7)**

$$
E+1\ge\frac1{32\sqrt2}\sqrt{N/\delta}.
$$

Every admissible witness obeys this bound, so its infimum obeys it as well. This proves the lower half of the first theorem in [the model](model.md#uniform-theorem).

Equation (5) also gives the uniform error form

$$
\delta\ge
\frac{1-e^{-1}}{1024}
\min\left\lbrace 1,\frac{N}{(E+1)^2}\right\rbrace .
$$

Its constants are deliberately loose; no exact optimal prefactor is asserted.

## 5. Removing the additive one uniformly

A separate constant-energy floor prevents an invalid subtraction of one from a small asymptotic lower bound. At $t=\pi$, the target states are orthogonal:

$$
s_N(\pi)=0.
$$

Equation (2) gives $d_R(\pi)\ge1-2\delta$. If
$E\lt (1-2\delta)^2/(2\pi)$, then $\pi E\lt 1$ and (4) contradicts this inequality. Therefore

**(8)**

$$
E\ge\frac{(1-2\delta)^2}{2\pi}
\quad\text{for }0\le\delta\lt 1/2.
$$

In particular, $\delta\le1/8$ implies
$E\ge9/(32\pi)>1/16$. Hence $E+1\le17E$. Combining this with (7) gives

$$
E\ge\frac1{544\sqrt2}\sqrt{N/\delta}
\gt\frac1{1024}\sqrt{N/\delta}.
$$

The same small-error domain works for all even $N\ge2$. Removing the additive one therefore needs neither an unmentioned large $N$ limit nor a stronger accuracy restriction.

## 6. Scope of the converse

The proof allows an arbitrary covariant CPTP operation on the whole output block. It does not infer unchanged total-charge probabilities for an open covariant process: an invariant environment can exchange charge. The exactly conserving unitary construction is a valid, narrower achieving class, not a premise of this lower bound.

The known qubit input enters only through invariance. Its balanced energy is needed by the particular low-drift closed-unitary upper bound, not by the orbit-discrimination argument. Initial reference–input correlations or an uncounted asymmetric environment change the input resource and are outside the model.

The information-disturbance and no-broadcasting framework is inherited from the literature discussed in [related work](../references/RELATED_WORK.md). The role of this proof is the stated first-moment quantitative bound with its mixed-reference and joint-error quantifiers.
