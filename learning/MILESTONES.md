# Thirty milestones for understanding quantum coherence reuse

This is a common map of the project's scientific story. Its single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's posted manuscript. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant sections, translates conventions and supplies the project-specific steps absent from the book. Primary research papers remain sources for attribution and proof dependencies; they are not additional educational anchors.

The map allocates **12 milestones to background/preliminaries** and **18 to narrative/innovation**. The background develops individual states, operations and distances into the complete preparation-and-return contract. The narrative joins the converse and a finite pair processor, then explains their common resource law and its limits. The allocation follows those two proof routes rather than the textbook's chapter order. Specialist algebra remains in the canonical scientific files; these milestones do not claim to cover every lemma or nearby topic.

Throughout, $N\ge2$ is even, qubit excitation gaps equal one, and the main uniform theorem uses $0<\delta\le1/8$. Reference mean energy is measured above its spectral infimum. The input qubits separately contain $N/2$ excitations, and error concerns the returned reference **together with the entire product output**.

## Phase I — Background and preliminaries

### M01 — A coherent qubit and its energy

**Central question:** What distinguishes a coherent superposition from a classical uncertainty over energy levels?

**Understanding target:** Explain the states $|0\rangle$, $|1\rangle$, $|+\rangle$ and their density operators; distinguish a phase-sensitive off-diagonal term from mean excitation. Recognize that equal energy statistics do not imply equal quantum states.

**Dependencies and story role:** Dependencies: none. Story role: This introduces the smallest object the source must produce before adding registers or a reference.

**Conceptual connection:** State description and energy measurement are different pieces of information, which is why supplying energy alone cannot replace a phase reference.

**Source pointers:** Watrous §§2.1.2 and 2.3.1; [registers, input and target](../science/model.md#registers-input-and-target); [Watrous bridge](WATROUS_BRIDGE.md).

### M02 — A product batch and its correlations

**Central question:** What does it mean for several coherent outputs to be independent?

**Understanding target:** Read a tensor-product state and a reduced state, and explain why specified one-qubit marginals do not determine the whole batch. Distinguish a genuine product target from a correlated state with the same local appearances.

**Dependencies and story role:** Dependencies: M01. Story role: Expands one output into multiple registers and introduces the global distinction that the final theorem must preserve.

**Conceptual connection:** Partial trace discards correlations; later joint processing can reveal information lost by local descriptions.

**Source pointers:** Watrous §2.1.3; [joint error and return](../science/model.md#joint-error-and-return); [what local output checks would miss](../science/examples.md#what-local-output-checks-would-miss).

### M03 — Balanced inputs and total excitation

**Central question:** Why does each fresh pair start in $|01\rangle$ rather than two ground states?

**Understanding target:** Add excitation across tensor factors and distinguish a sharp total charge from a mean charge. Explain that $|01\rangle$ and $|++\rangle$ each have mean excitation one, while only the latter has charge fluctuations and coherence.

**Dependencies and story role:** Dependencies: M01 and M02. Story role: Establishes the input energy account before introducing conserving dynamics.

**Conceptual connection:** Matching mean energy removes deterministic drift without removing the need to create a coherent distribution over charge sectors.

**Source pointers:** Watrous §§1.1.2 and 2.1.2; [registers, input and target](../science/model.md#registers-input-and-target); [drift and fluctuations](../science/interpretation.md#drift-and-fluctuations).

### M04 — Time translations and a phase reference

**Central question:** How can a change of time origin reveal coherence?

**Understanding target:** Interpret $e^{-itH}\rho e^{itH}$ as a state's time-translation orbit. Explain why an energy eigenstate is invariant and a coherent qubit rotates, and how a reference can carry a phase relation without assigning an absolute external phase to the processor.

**Dependencies and story role:** Dependencies: M01 and M03. Story role: Connects energy eigenstates to the symmetry that constrains the apparatus.

**Conceptual connection:** Coherence between energy levels becomes distinguishability between translated states, the quantity used in the converse.

**Source pointers:** Watrous §§1.1.2 and 2.2.3 for unitary channels; [allowed operations](../science/model.md#allowed-operations); [reference profile](../science/construction.md#reference-profile). The symmetry interpretation is supplied by the project.

### M05 — Channels that respect the symmetry

**Central question:** Which processes may use the reference without importing another phase standard?

**Understanding target:** Read the covariance equation and distinguish a general covariant channel from a closed energy-conserving unitary. Explain why auxiliary inputs must be jointly invariant and initially independent, and why covariance permits energy exchange with an invariant environment.

**Dependencies and story role:** Dependencies: M02 and M04. Story role: Builds an operational model from the state symmetry, including the larger class needed for the lower bound.

**Conceptual connection:** A resource restriction must apply to the whole preparation process; invariant local marginals do not exclude hidden asymmetric correlations.

**Source pointers:** Watrous §§2.2.1–2.2.2; [allowed operations](../science/model.md#allowed-operations); [scope of the converse](../science/converse.md#6-scope-of-the-converse).

### M06 — Trace distance as a statistical error

**Central question:** What can an observer detect when two quantum states are close?

**Understanding target:** Use half trace distance $D(\rho,\tau)=\|\rho-\tau\|_1/2$ and its equal-prior Helstrom interpretation. Explain the factor of two and why a joint measurement is allowed when interpreting this metric.

**Dependencies and story role:** Dependencies: M01 and M02. Story role: Supplies the operational accuracy criterion before comparing actual and ideal outputs.

**Conceptual connection:** The same metric both scores the source and bounds how much time-translation information its ideal output could add.

**Source pointers:** Watrous §§1.1.3 and 3.1.1, especially Theorem 3.4; [joint error and return](../science/model.md#joint-error-and-return).

### M07 — Moving an error through a protocol

**Central question:** Why does a global trace-distance bound remain useful after further processing?

**Understanding target:** Explain channel contractivity, invariance under a unitary or an unchanged tensor factor, and the triangle inequality. Distinguish an upper bound assembled through intermediate comparison states from an assumption that the actual errors are independent.

**Dependencies and story role:** Dependencies: M05 and M06. Story role: Turns an operational distance into a tool for comparing complete protocols.

**Conceptual connection:** Both the lower-bound orbit comparison and the upper-bound sequential hybrid use the same elementary distance calculus.

**Source pointers:** Watrous §§3.1.1 and 3.2.3; [orbit comparison](../science/converse.md#2-covariance-turns-return-error-into-an-orbit-bound); [sequential hybrid](../science/sequential_reuse.md#sequential-hybrid-bound).

### M08 — Pure overlaps and root fidelity

**Central question:** How does a vector overlap translate into a state error?

**Understanding target:** Keep Watrous's unsquared fidelity distinct from squared fidelity and from trace distance. For pure vectors, explain $D=\sqrt{1-|\langle a|b\rangle|^2}$; for a mixed state, understand why a purification gives a useful comparison without becoming an available laboratory resource.

**Dependencies and story role:** Dependencies: M02 and M06. Story role: Provides the metric bookkeeping used by both proof routes.

**Conceptual connection:** A good overlap does not automatically give a trace error of the same order; avoiding an unnecessary square-root loss matters to the achieved energy law.

**Source pointers:** Watrous §§2.1.3 and 3.2.1–3.2.3; [first-moment orbit estimate](../science/converse.md#3-a-first-moment-reference-orbit-estimate); [exact one-pair error](../science/construction.md#exact-one-pair-error).

### M09 — A mean-energy constraint without a cutoff

**Central question:** What does a finite first energy moment control when the reference has rare high-energy components?

**Understanding target:** Interpret $E=\operatorname{Tr}(H_R\sigma_R)$ above a nonnegative spectral lower bound. Distinguish mean energy from dimension, support width and variance, and recognize that finite mean need not imply finite second moment.

**Dependencies and story role:** Dependencies: M03 and M04. Story role: Fixes the resource constraint before a convenient finite ladder is introduced.

**Conceptual connection:** Probability over energy levels connects the physical inventory to a characteristic-function bound that remains valid for mixed and heavy-tailed references.

**Source pointers:** Watrous §1.2.2 for expectations and §2.1.2 for states; [reference model](../science/model.md#registers-input-and-target); [energy, width and dimension](../science/resource_accounting.md#energy-width-and-dimension). Infinite-spectrum spectral integration is supplied in the project.

### M10 — Conserving unitaries act within sectors

**Central question:** What freedom remains when total excitation is conserved exactly?

**Understanding target:** Decompose reference-plus-pair basis vectors by total charge and explain block-diagonal unitary action. Distinguish rotating a vector within one sector from changing the probabilities of different total-charge sectors.

**Dependencies and story role:** Dependencies: M03 and M05. Story role: Introduces the local building blocks of the attaining processor without assuming that every covariant channel has the same sector constraint.

**Conceptual connection:** Conservation permits substantial coherent control inside degenerate total-energy sectors even though it forbids arbitrary mixing of different sectors.

**Source pointers:** Watrous §1.1.3 for decompositions and §2.2.2 for unitary channels; [charge-sector alignment](../science/construction.md#charge-sector-alignment); [scope of the converse](../science/converse.md#6-scope-of-the-converse).

### M11 — Probability overlap and a lazy walk

**Central question:** How can ordinary probability distributions quantify a coherent state-preparation error?

**Understanding target:** Read a normalized probability vector, a convolution and the overlap $B(p,q)=\sum_k\sqrt{p_kq_k}$. Explain the unnormalized Hellinger convention $\mathsf H^2=2(1-B)$ and the pair's shift probabilities $1/4,1/2,1/4$.

**Dependencies and story role:** Dependencies: M03, M08 and M10. Story role: Connects finite charge-sector bookkeeping with the classical smoothing calculation needed for achievability.

**Conceptual connection:** Balanced quantum charge fluctuations induce a centered random-walk convolution; sector alignment turns its probability overlap into a quantum vector overlap.

**Source pointers:** Watrous §1.2.2 and §3.2.1 for classical expectations and fidelity; [exact one-pair error](../science/construction.md#exact-one-pair-error); [Watrous bridge](WATROUS_BRIDGE.md) for the project-specific Hellinger translation.

### M12 — The complete preparation-and-return contract

**Central question:** Which physical statement must the two proof routes ultimately establish?

**Understanding target:** Assemble the initially independent reference and balanced input, allowed covariant process, complete target $\sigma_R\otimes\psi_N$, error tolerance and optimized mean energy. Distinguish this known-state task from unknown-input gate synthesis and from marginal reference return.

**Dependencies and story role:** Dependencies: M02, M05, M07, M08 and M09. Story role: Integrates the background into one precise global problem; the remaining phase explains its solution.

**Conceptual connection:** The quantifiers and scored registers determine which conservation arguments, constructions and resource comparisons are relevant.

**Source pointers:** [Model and uniform theorem](../science/model.md); [resource accounting](../science/resource_accounting.md); Watrous §§2.1–2.3 and 3.1–3.2 as foundational tools.

## Phase II — Narrative and innovation

### M13 — A pure output amplifies distinguishability

**Central question:** Why would appending the desired coherent batch reveal more than the reference alone?

**Understanding target:** Explain the mixed-state product inequality $D(\rho\otimes a,\tau\otimes b)\ge d+(1-s)(1-d)$, with $d=D(\rho,\tau)$ and $s=|\langle a|b\rangle|^2$. Identify how an optimal Helstrom measurement and weighted pure-state blocks prove it.

**Dependencies and story role:** Dependencies: M06, M08 and M12. Story role: Isolates the first local inference in the converse before introducing a physical orbit.

**Conceptual connection:** The statistical information in a new pure state produces an explicit distance increment even when the original reference is mixed.

**Source pointers:** [Product distinguishability inequality](../science/converse.md#1-a-product-distinguishability-inequality); Watrous §3.1.1 for the inherited Helstrom tool.

### M14 — Covariance limits the extra orbit information

**Central question:** How does the source's joint return error constrain its time-translation orbit?

**Understanding target:** Follow the comparison of actual outputs from $\sigma_R$ and its translated state. Explain why invariant input and covariance bound their distance by $d_R(t)$, while two endpoint errors compare them with the ideal products.

**Dependencies and story role:** Dependencies: M04, M05, M07 and M13. Story role: Embeds the product inequality into the physical preparation task.

**Conceptual connection:** Data processing and approximate product return combine into $2\delta\ge[1-s_N(t)][1-d_R(t)]$; no reference-orbit measurement is being supplied as an extra control.

**Source pointers:** [Covariance and the orbit bound](../science/converse.md#2-covariance-turns-return-error-into-an-orbit-bound); [allowed operations](../science/model.md#allowed-operations).

### M15 — The target batch has a known orbit

**Central question:** How does increasing the number of coherent outputs change the target's response to a small time shift?

**Understanding target:** Derive the single-qubit overlap and its product form $s_N(t)=\cos^{2N}(t/2)$. Explain the small-shift dependence on $Nt^2$ and the orthogonality at $t=\pi$ without replacing the exact overlap by a global approximation.

**Dependencies and story role:** Dependencies: M01, M02, M04 and M14. Story role: Supplies the target side of the orbit-information comparison.

**Conceptual connection:** Independent coherent qubits accumulate time-translation distinguishability, which must be reconciled with the reference's limited orbit speed.

**Source pointers:** [Target-orbit overlap](../science/converse.md#2-covariance-turns-return-error-into-an-orbit-bound); [finite-energy lower bound](../science/converse.md#4-explicit-finite-energy-lower-bound).

### M16 — Mean energy controls the reference orbit

**Central question:** Why cannot a rare, arbitrarily high-energy tail defeat the converse?

**Understanding target:** Follow $|1-\operatorname{Tr}(\sigma_Re^{-itH_R})|\le |t|E$ and the purification-based bound $d_R(t)\le\sqrt{2|t|E}$ in its stated domain. Explain why neither a finite variance nor return of that mathematical purification is assumed.

**Dependencies and story role:** Dependencies: M08, M09 and M14. Story role: Supplies the reference side of the comparison for the broadest allowed input class.

**Conceptual connection:** A spectral expectation, rather than a variance or a support cutoff, converts initial mean energy into an operational limit.

**Source pointers:** [First-moment reference-orbit estimate](../science/converse.md#3-a-first-moment-reference-orbit-estimate); Watrous §§2.1.3 and 3.2.2–3.2.3 for the finite-dimensional purification and distance tools extended explicitly here.

### M17 — A uniform lower bound, including small energies

**Central question:** How do the two orbit estimates become a lower bound on the optimized reference energy?

**Understanding target:** Explain the time choice $t=1/[8(E+1)]$, the resulting exponential error bound and its inversion for $\delta\le1/8$. Explain separately why the $t=\pi$ constant-energy floor permits removal of the additive one uniformly over even $N\ge2$.

**Dependencies and story role:** Dependencies: M14, M15 and M16. Story role: Completes the converse route and makes its two-parameter scope explicit before achievability begins.

**Conceptual connection:** A useful asymptotic law must preserve its uniform constants and domain; subtracting one from an order statement without an energy floor would leave a gap.

**Source pointers:** [Explicit finite-energy lower bound](../science/converse.md#4-explicit-finite-energy-lower-bound); [removing the additive one](../science/converse.md#5-removing-the-additive-one-uniformly); [uniform theorem](../science/model.md#uniform-theorem).

### M18 — A finite smooth reference

**Central question:** What concrete reference family can attain the converse's energy order?

**Understanding target:** Describe the nonnegative ladder with $L-1$ levels and sine-fourth probabilities. Explain normalization, reflection symmetry and $E_L=L/2-1$, while keeping mean energy distinct from an arbitrary reference's dimension or width.

**Dependencies and story role:** Dependencies: M09, M10 and M11. Story role: Starts the constructive route with a finite resource whose energy is fully explicit.

**Conceptual connection:** Smooth probability weights and controlled boundaries are resources for reducing joint disturbance; a flat ladder is not imposed as an optimizer.

**Source pointers:** [Reference profile](../science/construction.md#reference-profile); [energy, width and dimension](../science/resource_accounting.md#energy-width-and-dimension).

### M19 — A balanced pair produces centered fluctuations

**Central question:** Which change of sector probabilities is required by one coherent output pair?

**Understanding target:** Relate the sharp input excitation one to the three output charges of $|++\rangle$. Explain why the desired product has $q_k=(p_{k-1}+2p_k+p_{k+1})/4$ and why its first-difference drift cancels.

**Dependencies and story role:** Dependencies: M03, M11 and M18. Story role: Identifies the local probability change that the processor must accommodate.

**Conceptual connection:** Matching mean charge leaves a second-difference smoothing problem, rather than a systematic reference translation.

**Source pointers:** [Charge-sector alignment](../science/construction.md#charge-sector-alignment); [drift and fluctuations](../science/interpretation.md#drift-and-fluctuations).

### M20 — Match the target within each sector

**Central question:** How much of the desired product can an exactly conserving unitary reproduce?

**Understanding target:** Identify each occupied input sector and its normalized target projection $v_\ell$. Explain why those directions can be aligned while their original sector probabilities remain fixed, including target weight in sectors absent from the input.

**Dependencies and story role:** Dependencies: M10, M18 and M19. Story role: Turns the probability description into a coherent vector construction.

**Conceptual connection:** Conservation fixes the weights between sectors, while degeneracy permits the useful rotations within them.

**Source pointers:** [Charge-sector alignment](../science/construction.md#charge-sector-alignment); [three-level example](../science/examples.md#a-three-level-reference).

### M21 — One finite unitary for every call

**Central question:** How are the sector alignments assembled into a deterministic processor?

**Understanding target:** Explain how a Householder block maps the occupied input vector to $v_\ell$ and how the direct sum defines a unitary commuting with total excitation. Distinguish the fixed reference–pair matrix from an operation requiring all future outputs at once.

**Dependencies and story role:** Dependencies: M05, M10 and M20. Story role: Completes the physical map that will be reused sequentially.

**Conceptual connection:** A finite block description proves algebraic implementability under conservation while leaving native synthesis and timing as separate questions.

**Source pointers:** [Charge-sector alignment](../science/construction.md#charge-sector-alignment); [implementation scope](../science/construction.md#implementation-scope); Watrous §§1.1.2–1.1.3 for the linear-algebra background.

### M22 — Exact one-pair error from sector overlap

**Central question:** Why can the one-use joint error be calculated without discarding the reference?

**Understanding target:** Explain the overlap $B(p,q)$ and the exact pure-state distance $\varepsilon_L=\sqrt{1-B^2}$. Distinguish its optimality among conserving unitaries for the fixed pure input from a claim about all covariant channels or all references.

**Dependencies and story role:** Dependencies: M08, M11, M20 and M21. Story role: Provides the local joint-error quantity needed for a composable upper bound.

**Conceptual connection:** Sectorwise Cauchy–Schwarz and pure-state distance tie the coherent construction to a classical probability overlap without changing the error metric.

**Source pointers:** [Exact one-pair error](../science/construction.md#exact-one-pair-error); [collective benchmark](../science/construction.md#a-sharper-collective-benchmark).

### M23 — Place sector alignment in its recovery ancestry

**Central question:** Which part of the processor is inherited from covariant recovery?

**Understanding target:** Explain the normalized-sector structure of the Marvian–Lloyd Petz channel and how the supplied sharp-charge pair realizes the relevant pure component by a closed unitary. Distinguish this deterministic realization from selecting a successful branch of a mixture.

**Dependencies and story role:** Dependencies: M05, M20 and M22. Story role: Establishes the construction's intellectual and operational relationship to its closest antecedent before interpreting the new budget.

**Conceptual connection:** A general recovery mechanism and its fidelity guarantee can be inherited while a specific conserving realization and a sharper trace-error analysis require their own proof.

**Source pointers:** [Relation to covariant recovery](../science/construction.md#relation-to-covariant-recovery); [related work](../references/RELATED_WORK.md), Marvian–Lloyd entry. The cited paper is a research attribution source, not a second educational anchor.

### M24 — Smoothness gives inverse-square joint error

**Central question:** Why does the finite sine-fourth profile give $\varepsilon_L=O(L^{-2})$?

**Understanding target:** Connect the centered second difference to the Hellinger estimate, including both exterior boundary masses. Explain why the profile's smooth boundary behavior matters and how the sufficient bound $\sqrt{98/3}\sin^2(\pi/L)$ controls the full one-pair trace error.

**Dependencies and story role:** Dependencies: M11, M18, M19 and M22. Story role: Establishes the quantitative local estimate that determines the final energy exponent.

**Conceptual connection:** A second-order change in probability weights can yield a second-order joint vector error after sector alignment; a generic fidelity-to-distance estimate can miss this sharper behavior.

**Source pointers:** [Uniform sine-profile estimate](../science/construction.md#uniform-sine-profile-estimate); [Watrous bridge](WATROUS_BRIDGE.md) for the Hellinger convention and missing intermediate steps.

### M25 — Reuse with all correlations retained

**Central question:** How can the same processor be reused when the actual reference changes and becomes correlated with previous outputs?

**Understanding target:** Follow the induction comparing the actual whole state $\rho_j$ with the ideal product $\tau_j$. Explain the bound $D(\rho_{j+1},\tau_{j+1})\le D(\rho_j,\tau_j)+\varepsilon_L$ without inserting a physical reset or assuming independent errors.

**Dependencies and story role:** Dependencies: M02, M07, M12, M21 and M24. Story role: Assembles local processor performance into a complete sequential source.

**Conceptual connection:** The reset reference appears only inside a mathematical comparison state. Contractivity carries the actual correlations through the induction.

**Source pointers:** [Sequential hybrid bound](../science/sequential_reuse.md#sequential-hybrid-bound); [reuse and independence](../science/resource_accounting.md#reuse-and-independence).

### M26 — Match the energy orders

**Central question:** How do the broad converse and the restricted pair protocol establish one uniform optimum?

**Understanding target:** Combine $N/2$ pair uses with $\varepsilon_L=O(L^{-2})$, choose an integer $L=\lceil\sqrt{29N/\delta}\rceil$, and translate $E_L=L/2-1$ into the upper bound. Compare its quantifiers with the mixed-reference lower bound to state $E_{\min}=\Theta(\sqrt{N/\delta})$ for even $N\ge2$, $0<\delta\le1/8$.

**Dependencies and story role:** Dependencies: M17, M18, M24 and M25. Story role: Joins the two proof routes into the central resource theorem.

**Conceptual connection:** An attaining restricted protocol can match an unrestricted lower bound in energy order without being the exact finite optimizer or an efficient implementation.

**Source pointers:** [Uniform theorem](../science/model.md#uniform-theorem); [constants from the finite construction](../science/model.md#constants-from-the-finite-construction); [reference-energy budget](../science/sequential_reuse.md#reference-energy-and-coherent-output-budget).

### M27 — Compose the source and budget imperfections

**Central question:** Which guarantees survive later joint use and imperfect processor calls?

**Understanding target:** Explain why downstream processing preserves the global state error, and why a per-call channel bound must include arbitrary correlated external systems. Distinguish nominal-reference and actually prepared-reference return targets, including the extra endpoint preparation error.

**Dependencies and story role:** Dependencies: M05, M07, M12 and M25. Story role: Extends the completed ideal argument to a precisely stated stability budget without turning it into a hardware theorem.

**Conceptual connection:** The diamond norm supplies the correlation-uniform channel error needed by the same hybrid logic; tests of isolated output marginals do not provide it.

**Source pointers:** Watrous §§3.3.2–3.3.3; [stability under preparation and channel errors](../science/sequential_reuse.md#stability-under-preparation-and-channel-errors); [what a user of the outputs receives](../science/interpretation.md#what-a-user-of-the-outputs-receives).

### M28 — Reconstruct a small complete example

**Central question:** What do the reference, processor, output error and verification look like in one finite device?

**Understanding target:** Trace the $L=4$ example from its three reference levels through sector vectors and exact one-pair overlap. Explain what the repeated-matrix checks at larger finite sizes verify, and why a finite numerical success neither proves the uniform converse nor optimizes every allowed protocol.

**Dependencies and story role:** Dependencies: M18, M20, M21, M22 and M25. Story role: Reconnects the integrated theorem to concrete objects and observed finite calculations.

**Conceptual connection:** Independent matrix evaluation can check that the advertised conserving processor realizes its stated mathematical model while analytical arguments carry the uniform claim.

**Source pointers:** [Worked examples](../science/examples.md); [verification and its scope](../verification/README.md); [construction](../science/construction.md).

### M29 — Read the resource and task boundaries together

**Central question:** What would change if the output inputs, energy accounting or return requirement changed?

**Understanding target:** Separate reference energy from the supplied $N/2$ qubit excitations, total preparation work, reference-state preparation and number-selective control costs. Explain the distinctions between finite-ladder achievability and arbitrary finite-mean converses, and between known-state preparation and unknown-input universal operations.

**Dependencies and story role:** Dependencies: M09, M12, M17, M21, M26 and M27. Story role: Places the theorem in its actual physical model before the final synthesis.

**Conceptual connection:** Matching a resource order requires matched inputs and accuracy conventions; a stronger or different task cannot inherit an advantage from a different baseline.

**Source pointers:** [Resource accounting](../science/resource_accounting.md); [what is optimized](../science/model.md#what-is-optimized-and-what-is-not); [boundaries of the result](../science/interpretation.md#boundaries-of-the-result).

### M30 — The complete coherent-output budget

**Central question:** What does the result add once its prior foundations, complete error contract and costs are all stated?

**Understanding target:** Explain the complete story: a mean-energy-limited reference cannot freely add the target's orbit information; a finite smooth reference and repeated balanced-pair processor attain the matching order; and the global output budget is of order $\delta E^2$ in its nontrivial regime. Retain the even-$N$, small-error, separately paid input-energy and control-scope qualifications. Credit catalytic coherence, quadratic reference longevity, correlation warnings and Petz recovery as inherited foundations rather than new principles.

**Dependencies and story role:** Dependencies: M12, M17, M23, M26, M27, M28 and M29. Story role: Integrates the entire narrative into a scientific conclusion whose significance and limits can be explained together.

**Conceptual connection:** The contribution connects approximate asymmetry broadcasting to an optimized, globally composable source budget; global independence and returned-reference accuracy are established rather than inferred from local repeatability.

**Source pointers:** [Scientific overview](../science/README.md); [uniform theorem](../science/model.md#uniform-theorem); [physical interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [Watrous bridge](WATROUS_BRIDGE.md).
