# Resource accounting and interpretation

The [uniform theorem](model.md) optimizes the initial mean energy of a supplied phase reference. It is a statement about how much reference resource suffices for a globally accurate supply of coherent states. The costs below are part of the task definition and delimit that interpretation.

## Supplied resources and charged quantities

| Resource | Treatment |
| --- | --- |
| Output qubits | $N$ unit-gap qubits, with even $N\ge2$ |
| Initial qubit state | Known $|01\rangle^{\otimes N/2}$; its $N/2$ excitations are supplied separately |
| Reference state | Known and initially independent; all initially supplied asymmetry is included in $R$ |
| Charged reference energy | $E=\mathrm{Tr}(H_R\sigma_R)$ above the reference spectral infimum |
| Error | Half trace distance to the same reference tensored with the complete $N$-qubit product target |
| Other ancillary states | Invariant under their own time translations; no free coherent phase standard |
| Converse controls | Arbitrary time-translation-covariant CPTP protocols, with unrestricted complexity |
| Attaining controls | Repeated identical exactly conserving unitary on the reference and one fresh balanced qubit pair |
| Records and old outputs | No postselection or removal of old outputs from the joint error score |

## Reference energy and total energy

Both the input qubits and the desired product output have mean energy $N/2$. Balancing the supplied input therefore removes a macroscopic mean-energy drift from the closed conserving construction. The reference still needs a coherent energy distribution, and its required mean energy is $\Theta(\sqrt{N/\delta})$.

The initial total mean energy of the attaining protocol is

$$
E_{\mathrm{total}}=\frac N2+E_L,
\qquad
E_L=\frac L2-1.
$$

The sublinear dependence on $N$ at fixed error concerns the **reference term**. Total supplied energy is already at least $N/2$. Starting every input qubit in $|0\rangle$ would require another source of the output's mean energy; it is a different accounting problem. The result gives no work, heat or thermodynamic efficiency optimum.

For the closed-unitary upper bound, total energy is conserved exactly. The returned reference need only be close in trace distance, not identical in mean energy. Nevertheless the bounded qubit observable obeys

$$
\left|\mathrm{Tr}(Q_N\omega_S)-\frac N2\right|
\le N\delta,
$$

so exact total-energy conservation also bounds the actual reference mean-energy change by $N\delta$. This additional conclusion uses the achieving unitary. Covariance alone, as assumed in the converse, does not prohibit energy exchange with an invariant environment.

## Energy, width and dimension

The converse constrains a first moment and permits an infinite reference. A finite dimension, a hard energy cutoff or a finite variance is not silently substituted for that condition. A rare high-energy tail is covered by the [spectral-integral orbit estimate](converse.md#3-a-first-moment-reference-orbit-estimate).

The explicit upper bound uses a particular finite ladder:

$$
\dim R=L-1,
\qquad
\mathrm{spec}(H_R)=\lbrace 0,1,\ldots,L-2\rbrace ,
\qquad
E_L=\frac L2-1.
$$

Thus this family has dimension and energy width of order $\sqrt{N/\delta}$. These are properties of the attaining family. The theorem does not optimize dimension over arbitrary spectra, and a charge-width bound must not be relabelled a dimension bound when levels can be sparse or degenerate.

The converse covers normal states on infinite-dimensional Hilbert spaces with finite mean energy; the upper bound needs only finite-dimensional references. Infinite-mean states are not assigned a finite resource value, and the theorem does not certify singular ideal phase eigenstates as physical references.

## Reuse and independence

For one chosen finite ladder and reference state, the same pair unitary can be called repeatedly on fresh $|01\rangle$ inputs. It acts only on the reference and the next pair; previous pairs are untouched. The [hybrid proof](sequential_reuse.md) compares the actual whole state after each call with the original reference times all ideal previous outputs. It accumulates errors without assuming an unchanged actual reference at intermediate times, a reset, or independent actual errors.

Consequently the result supplies globally approximate independent outputs and an approximately returned reference. It does not follow merely from a long-lived next-use measurement accuracy. That distinction is essential when old outputs may later be processed together.

The energy-order optimum is against the broader global covariant model. The fixed pair processor attains that order, but neither its exact finite error nor its native gate cost is claimed optimal. In the nontrivial many-output regime the law is equivalently an output budget of order $\delta E^2$ at joint error $\delta$; for parameter values that cannot support even one pair, this asymptotic shorthand should be replaced by the explicit theorem.

## Control and preparation costs that remain separate

The reference is supplied in its specified coherent state. Its initial mean energy is counted; the physical work, time and apparatus needed to prepare that state are not optimized. Preparing it from entirely invariant inputs would itself require an asymmetry resource.

The pair unitary uses number-selective rotations within total-energy sectors. Those rotations conserve energy and therefore do not logically require an extra phase reference. Their synthesis on a particular device can still require substantial control bandwidth, interaction time, gate count or calibration. A finite block description is not an efficient hardware implementation. The result imposes no native locality constraint and gives no bound on the strength or duration of those controls.

Finally, the source prepares one specified family of known pure states. It does not implement arbitrary gates on unknown inputs, recover an unknown borrowed register, or promise an adaptive quantum comb for arbitrary future input choices. Reusing the known reference is established here under the stated balanced-pair interface and full joint-output score. The relevant stronger and weaker tasks are compared in [related work](../references/RELATED_WORK.md).
