# A finite reference and an exactly conserving pair processor

The reference is a finite energy ladder. A single fixed unitary acts on it and a fresh pair of qubits in $|01\rangle$, approximately producing $|++\rangle$ while returning the reference. The unitary preserves total excitation exactly. [Sequential reuse](sequential_reuse.md) turns its one-use estimate into a bound on the entire output batch, including its correlations with the reference.

Throughout, $D(\rho,\sigma)=\frac12\Vert \rho-\sigma\Vert _1$. Energies are measured in units of the qubit excitation gap. The initial excitation supplied in each pair is one.

## Reference profile

Choose an integer $L\geq3$ and let the reference have $d=L-1$ levels,

$$
H_R=\sum_{r=0}^{L-2}r |r\rangle\langle r|.
$$

Prepare the pure state

$$
|R_L\rangle=\sum_{r=0}^{L-2}\sqrt{p_r} |r\rangle,
\qquad
p_r=\frac{8}{3L}\sin^4\left(\frac{\pi(r+1)}{L}\right).
$$

Set $p_r=0$ outside this range. The trigonometric sums and reflection symmetry give

$$
\sum_{r=0}^{L-2}p_r=1,
\qquad
E_L=\langle R_L|H_R|R_L\rangle=\frac L2-1.
$$

Indeed, $\sin^4x=(3-4\cos2x+\cos4x)/8$, and the two nonconstant discrete Fourier sums are $-1$ when $L\geq3$. The weights satisfy $p_r=p_{L-2-r}$, giving the stated mean. No reference levels below zero are used.

The amplitudes are positive in this choice of phase coordinates. Applying $e^{-itH_R}$ to the reference rotates the output qubits accordingly because the processor below commutes with total excitation; its controls do not supply an additional phase reference.

## Charge-sector alignment

The qubit-pair charge is

$$
Q_{12}=|1\rangle\langle1|_1+|1\rangle\langle1|_2.
$$

For each total charge $\ell$, denote its sector by

$$
\mathcal H_\ell=
\mathrm{span}\lbrace |r,b_1b_2\rangle:r+b_1+b_2=\ell\rbrace .
$$

Every sector has dimension at most four. On an occupied input sector, $1\leq\ell\leq L-1$, define

$$
|e_\ell\rangle=|\ell-1,01\rangle,
\qquad
q_k=\frac14(p_{k-1}+2p_k+p_{k+1}),
$$

and the normalized vector

$$
|v_\ell\rangle=
\frac{1}{2\sqrt{q_{\ell-1}}}
\sum_{\substack{r,b_1,b_2\\r+b_1+b_2=\ell}}
\sqrt{p_r} |r,b_1b_2\rangle.
$$

Its denominator is nonzero because $p_{\ell-1}>0$. This is the normalized projection of $|R_L\rangle|++\rangle$ onto $\mathcal H_\ell$.

Choose a real Householder block

$$
U_\ell=I_\ell-
2\frac{|w_\ell\rangle\langle w_\ell|}{\langle w_\ell|w_\ell\rangle},
\qquad
|w_\ell\rangle=|e_\ell\rangle-|v_\ell\rangle.
$$

If $w_\ell=0$, use $U_\ell=I_\ell$. Use the identity in sectors with no occupied input vector. Since $e_\ell$ and $v_\ell$ are real unit vectors, $U_\ell e_\ell=v_\ell$. The complete processor is

$$
U_L=\bigoplus_\ell U_\ell,
\qquad
[U_L,H_R+Q_{12}]=0.
$$

Thus the processor is a finite, exactly energy-conserving unitary. It contains no postselection, reference reset, measurement record, or discarded subsystem.

## Exact one-pair error

The initial vector has sector probabilities $p_k$, after centering the pair's initial charge at one. The desired product vector has sector probabilities $q_k$. The construction aligns the vectors within every occupied sector, so its overlap with the desired product is

$$
B(p,q)=\sum_{k\in\mathbb Z}\sqrt{p_kq_k}.
$$

The exact one-use error is therefore

$$
\varepsilon_L=
D\left(U_L(|R_L\rangle\langle R_L|\otimes|01\rangle\langle01|)U_L^\dagger,
|R_L\rangle\langle R_L|\otimes|++\rangle\langle++|\right)
=\sqrt{1-B(p,q)^2}.
$$

This overlap is maximal among exactly conserving unitaries for this fixed pure reference and fixed input: sector probabilities cannot change, and Cauchy–Schwarz bounds each sector's overlap by $\sqrt{p_kq_k}$. This optimality statement concerns that unitary class. It is not an optimality claim over every covariant channel at fixed reference state.

### Relation to covariant recovery

The normalized-target-sector mechanism is inherited from covariant recovery. In [Marvian and Lloyd, *From clocks to cloners*, Section IV.B, Eq. (20)](https://arxiv.org/pdf/1608.07325), the unrotated Petz channel for a pure target decomposes into a mixture of vectors of the form

$$
|\phi_a\rangle=\sum_\ell\sqrt{p_{\ell-a}} |v_\ell\rangle,
$$

with weights given by the target system's charge distribution. The pair output constructed here is exactly $|\phi_1\rangle$: the supplied input pair has sharp charge one, and a closed conserving unitary realizes that sector alignment deterministically. No measurement of the Petz mixture, branch selection, or free successful outcome is assumed. The present use of this mechanism is its finite conserving pair realization and composable error estimate, together with the [mixed-reference mean-energy converse](converse.md); approximate catalytic coherence and the recovery principle themselves are prior work.

For the unnormalized Hellinger distance

$$
\mathsf H(p,q)=\left[\sum_k(\sqrt{p_k}-\sqrt{q_k})^2\right]^{1/2},
$$

normalization gives $\mathsf H^2=2(1-B)$ and hence

$$
\varepsilon_L\leq\mathsf H(p,q).
$$

## Uniform sine-profile estimate

The following elementary estimate supplies the required $L^{-2}$ trace error, including the finite-ladder boundary. Put

$$
\theta=\frac\pi L,
\quad a=\sin^2\theta,
\quad c=\frac{8}{3L},
\quad f(x)=\sin^4x.
$$

For the interior grid points $x=j\theta$, $1\leq j\leq L-1$, the exact second-difference identity is

$$
f(x-\theta)-2f(x)+f(x+\theta)
=2a\big[\cos2x-(1-a)\cos4x\big].
$$

Moreover,

$$
|\cos2x-\cos4x|
=|6\sin^2x-8\sin^4x|
\leq6\sin^2x,
\qquad a\leq\sin^2x.
$$

Consequently the absolute second difference is at most $14a\sin^2x$. On the supported sites, $p=c f(x)$ and $q-p$ is $c/4$ times that second difference. Therefore

$$
(\sqrt q-\sqrt p)^2
=\frac{(q-p)^2}{(\sqrt q+\sqrt p)^2}
\leq\frac{(q-p)^2}{p}
\leq\frac{196c}{16}a^2.
$$

There are $L-1$ supported sites. The two newly reached exterior sites contribute exactly $c a^2/2$ in total. Adding both contributions yields

$$
\mathsf H(p,q)^2
\leq c\left[\frac{196}{16}(L-1)+\frac12\right]a^2
=\left(\frac{98}{3}-\frac{94}{3L}\right)a^2
\leq\frac{98}{3}a^2.
$$

The final one-pair guarantee, valid for every integer $L\geq3$, is

$$
\boxed{\displaystyle
\varepsilon_L\leq
\min\left\lbrace 1,\sqrt{\frac{98}{3}}\sin^2\frac\pi L\right\rbrace .}
$$

The numerical constant is a convenient sufficient bound, not an optimized constant.

## A sharper collective benchmark

For an even batch size $N=2m$, a single conserving unitary on the reference and all input qubits can align total-charge sectors in the same way. Let $X$ have distribution $\mathrm{Bin}(N,1/2)-m$ and let $q^{(N)}=p*\mathrm{law}(X)$. Its optimal overlap within the fixed-reference conserving-unitary class is

$$
B_N=\sum_k\sqrt{p_kq_k^{(N)}},
\qquad
\varepsilon_{N,\mathrm{collective}}=\sqrt{1-B_N^2}.
$$

This is useful for finite comparisons. The sequential protocol has the same proved energy/error scaling and requires only repeated use of the pair processor; it need not attain this finite-batch optimum.

## Implementation scope

The construction specifies at most $L+1$ charge-sector blocks of size at most four and has an explicit finite matrix description. Every reuse employs the same matrix. Number-selective interaction synthesis, reference-state preparation, control accuracy, duration, and locality have not been optimized. Exact conservation of the specified matrix is an algebraic statement, not a hardware implementation certificate.

[Continue to sequential reuse and its error budget](sequential_reuse.md) · [Numerical verification](../verification/README.md)
