# Related work and attribution

This project determines an optimal reference-energy budget for one specified state-preparation task. A deterministic covariant operation uses an initially independent reference of mean energy $E$ to prepare $N$ coherent qubits and return the reference, with half trace distance at most $\delta$ from the complete product target. For even $N\geq2$ and sufficiently small $\delta$, the optimal mean reference energy scales as

$$
E_{\min}(N,\delta)=\Theta\left(\sqrt{\frac{N}{\delta}}\right).
$$

The converse includes arbitrary mixed references, nonnegative reference Hamiltonians, finite mean energy without a variance or support bound, and arbitrary deterministic covariant channels. A finite pure ladder reference attains the order through repeated use of one fixed conserving processor on fresh balanced qubit pairs. Each input pair already contains one excitation. The theorem prices the coherent reference, rather than the total energy supplied to the qubits or the physical complexity of the controls.

Approximate catalytic coherence, reference reuse, quadratic reference longevity, correlation concerns, and covariant recovery are established subjects. The result here is the matching mean-energy law under this particular complete product-return criterion. The following comparisons identify what is inherited and why the statements concern different operational guarantees. Bibliographic records are in [references.bib](references.bib).

## Earlier coherence reservoirs and quadratic longevity

### Åberg: catalytic coherence

J. Åberg, *Catalytic Coherence*, Physical Review Letters **113**, 150402 (2014), [DOI](https://doi.org/10.1103/PhysRevLett.113.150402), [arXiv:1304.1060v3](https://arxiv.org/abs/1304.1060v3).

The conserving reservoir-shift construction and repeated coherent processing are prior foundations. The paper analyzes both doubly infinite and lower-bounded ladders; its repeatability property concerns the reservoir's ability to induce the same reduced operations. That property does not assert that the complete reservoir-plus-all-outputs state stays close to the original reservoir tensored with independent desired outputs. We do not claim to introduce coherence reuse, nor to contradict its reduced-operation statements. Our fixed balanced-pair source is state preparation with a stronger global error contract, rather than an implementation of an arbitrary gate on unknown inputs.

### Bartlett–Rudolph–Spekkens–Turner: reference degradation

S. D. Bartlett, T. Rudolph, R. W. Spekkens, and P. S. Turner, *Degradation of a quantum reference frame*, New Journal of Physics **8**, 58 (2006), [DOI](https://doi.org/10.1088/1367-2630/8/4/058), [arXiv:quant-ph/0602069v2](https://arxiv.org/abs/quant-ph/0602069v2).

Section IV, especially Eqs. (20)–(27) and Fig. 4, already supplies a lazy-walk phase-reference evolution and quadratic longevity versus mean photon number. Its score is the accuracy of a later hypothetical phase-comparison measurement after earlier measured systems and records are discarded. The hard-cutoff reference optimizes initial measurement quality; the paper explicitly distinguishes that objective from optimal longevity and from other energy constraints. Thus quadratic scaling and the random-walk picture are inherited. Our question asks whether such an order survives a global independent-output and returned-initial-reference guarantee, while optimizing over every finite-mean-energy mixed reference.

### Vaccaro–Croke–Barnett: correlations and repeatability

J. A. Vaccaro, S. Croke, and S. M. Barnett, *Is coherence catalytic?*, Journal of Physics A: Mathematical and Theoretical **51**, 414008 (2018), [DOI](https://doi.org/10.1088/1751-8121/aac112), [arXiv:1804.05154v1](https://arxiv.org/abs/1804.05154v1), [accepted manuscript](https://eprints.gla.ac.uk/161699/7/161699.pdf).

This work already makes the correlation and joint-repeatability issue explicit. For the flat-reservoir implementation it studies, Appendix B, Eq. (B.3), gives an approximately $(N-1)/L$ full trace-norm repeatability error in its stated $1\leq N\ll L$ regime. Its target compares the output register with the product of its one-qubit marginals; it is not our full returned-reference product target. The stated scaling is a property of that protocol, rather than a universal optimum over reference profiles and covariant operations. Our comparison is consequently an optimization under a specified global contract, not a claim that correlations were previously overlooked.

## Closest general framework: catalytic recovery

I. Marvian and S. Lloyd, *From clocks to cloners: Catalytic transformations under covariant operations and recoverability*, [arXiv:1608.07325v1](https://arxiv.org/abs/1608.07325v1) (2016), [DOI](https://doi.org/10.48550/arXiv.1608.07325).

This is a direct antecedent: Eqs. (1) and (3) already formulate approximate preparation of a joint product of the returned reference and a desired asymmetric state. Theorem 1, Eq. (18), bounds root fidelity by $2^{-\Delta\Gamma/2}$, with $\Delta\Gamma$ the relative-entropy-of-asymmetry increase. Equation (20) gives the covariant Petz map, up to the rotations in Eqs. (19) and (21). Section V.A treats preparation of one coherent qubit using a bounded clock. We inherit the task framework and covariant recovery perspective. An entropy-to-fidelity bound alone does not establish the present trace-distance dependence, but that observation is not a limitation on the best performance of the paper's explicit channel.

### Relationship of the sector construction to the Petz map

The relationship is explicit. Let $|r\rangle$ have energy probabilities $p_j$, and write a pure product target as

$$
|\Psi\rangle=|r\rangle\otimes|\psi\rangle
=\sum_K|\Psi_K\rangle,
\qquad q_K=\langle\Psi_K|\Psi_K\rangle,
\qquad |v_K\rangle=\frac{|\Psi_K\rangle}{\sqrt{q_K}}.
$$

Expand $|\psi\rangle=\sum_s c_s|s\rangle$ in an energy basis with energies $a_s$. Direct substitution into Marvian–Lloyd Eq. (20) gives, on $|r\rangle\langle r|$,

$$
\mathcal R_P(|r\rangle\langle r|)
=\sum_s |c_s|^2|\phi_{a_s}\rangle\langle\phi_{a_s}|,
\qquad
|\phi_a\rangle=\sum_K\sqrt{p_{K-a}} |v_K\rangle.
$$

Zero-weight sectors are omitted. A conserving unitary with a supplied sharp system-input energy $a_0$ can produce $|\phi_{a_0}\rangle$ by aligning its input vector with $|v_K\rangle$ within each total-energy sector. For a balanced pair, $a_0=1$. Thus normalized target-sector vectors and the recovery mechanism are not claimed as new conversion principles. The known Petz channel mixes these energy branches; the conserving construction here realizes the branch selected by the precharged input deterministically. No postselection is used. A sharper direct analysis of the Petz channel is compatible with the same upper order; no superiority over its optimized trace-distance performance is asserted.

## No-broadcasting and disturbance bounds

I. Marvian and R. W. Spekkens, *No-Broadcasting Theorem for Quantum Asymmetry and Coherence and a Trade-off Relation for Approximate Broadcasting*, Physical Review Letters **123**, 020404 (2019), [DOI](https://doi.org/10.1103/PhysRevLett.123.020404), [arXiv:1812.08766v2](https://arxiv.org/abs/1812.08766v2).

The finite-reference no-broadcasting and asymmetry-degradation principles are established here. Its quantitative Eq. (6) concerns a pure initial reference and trades output orbit asymmetry against recovery infidelity of the reference. Our proof also uses distinguishability of symmetry orbits, rather than introducing a new no-broadcasting principle. The mean-energy converse addresses a complete joint-product trace error and permits mixed references and unbounded energy support. Neither a variance bound nor return of a purification is assumed.

M. Lostaglio and M. P. Müller, *Coherence and Asymmetry Cannot be Broadcast*, Physical Review Letters **123**, 020403 (2019), [DOI](https://doi.org/10.1103/PhysRevLett.123.020403), [arXiv:1812.08214v2](https://arxiv.org/abs/1812.08214v2).

Its no-go results include finite-dimensional asymmetry broadcasting and weaker indefinitely repeated broadcasting. The present finite-error, finite-output optimization is consistent with those theorems. Taking an unlimited number of independent coherent outputs while keeping one fixed-energy reference within a fixed small global error is ruled out by our quantitative bound as well. Exact finite-dimensional catalysis and unrestricted repeated local functionality should not be identified with approximate joint return.

## Mean-energy requirements for unknown-input gates

G. Chiribella, Y. Yang, and R. Renner, *Fundamental Energy Requirement of Reversible Quantum Operations*, Physical Review X **11**, 021014 (2021), [DOI](https://doi.org/10.1103/PhysRevX.11.021014), [arXiv:1908.10884v3](https://arxiv.org/abs/1908.10884v3).

This work proves matching mean-battery-energy bounds for reversible operations that must work on every system input. Its main Eqs. (1)–(3) give the energy dependence, and Appendix D retains the inverse-square-root accuracy scaling for diamond error. It also shows that suitable circuit design can make the energy requirement independent of time complexity. Energy recycling, a mean-energy resource bound, and inverse-square-root accuracy are therefore not new by themselves. Our task fixes a balanced energy-eigenstate input and scores joint reference return together with all coherent outputs. The system's $N/2$ input excitations are separately supplied. The resulting $\sqrt N$ reference dependence is a statement for that restricted preparation task, not an improvement for universal gate implementation or a sublinear total-energy claim.

## Reversible dynamics with little reference disturbance

L. van Luijk, R. F. Werner, and H. Wilming, *Covariant catalysis requires correlations and good quantum reference frames degrade little*, Quantum **7**, 1166 (2023), [DOI](https://doi.org/10.22331/q-2023-11-06-1166), [arXiv:2301.09877v3](https://arxiv.org/abs/2301.09877v3).

Theorem 5 states that an induced system channel within unhalved diamond error $\epsilon$ of a unitary can be realized with the same system action and reference marginal disturbance at most $2\sqrt{2\epsilon}$. The paper also explains the role of correlations in exact covariant catalysis. It supplies the general reusable-reference principle; our account does not introduce that principle. Our optimized known-input preparation problem retains every output and requires one complete product approximation. A small reference marginal disturbance by itself does not supply that complete error bound or optimize its mean-energy dependence.

## Nearby conserving-control tasks

These related models clarify resource and return conventions.

| Scientific account | Different target and charged resource |
| --- | --- |
| [Quantum Control Coherence](https://github.com/GoGoKo699/Quantum-Control-Coherence) | A fixed gate on arbitrary unknown, reference-entangled inputs; optimal entropic coherence and dimension exponents from active transition rank. Battery return is not required. Its smooth-packet construction and reduced-channel quadratic error are relevant foundations, but do not impose the present complete return condition. |
| [Quantum Design Steering Cost](https://github.com/GoGoKo699/Quantum-Design-Steering-Cost) | Exact remote state 2-design preparation by a conserving measurement; initial reference QFI is minimized and the reference may be consumed. Mean energy and reusable product return are different optimizations. |
| [Quantum Borrowed Ancilla Cost](https://github.com/GoGoKo699/Quantum-Borrowed-Ancilla-Cost) | Approximate CCZ with arbitrary unknown borrowed qubits and complete-channel identity return under conserving two-qubit gates. The resource is borrowed width; no prepared asymmetric reference or coherent-output source is supplied. |

## What this theorem adds

The common foundations are finite references, covariant processing, known-state catalytic preparation, symmetry-orbit distinguishability, target-sector alignment, smooth ladder profiles, and accumulated-error arguments. The added conclusion is a matching coherent-output budget

$$
N=\Theta(\delta E^2)
$$

in the stated even-output, sufficiently small global-error regime: the lower bound optimizes over all finite-mean-energy mixed references and covariant deterministic channels, while a single fixed conserving balanced-pair processor attains the order and retains all previous outputs in the error account. The theorem does not optimize the leading constant, establish a universal gate, or price efficient preparation, native locality, operation time, or controller synthesis. These scope conditions accompany the result throughout the scientific account.
