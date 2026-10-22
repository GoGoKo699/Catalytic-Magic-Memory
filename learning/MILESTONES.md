# Thirty milestones for catalytic magic memory

This map follows the project's scientific dependencies through exactly 30 understanding targets. Phase I contains 13 background/preliminaries milestones: state and channel language, stabilizer resources, distinguishability, and complete memory accounting come together in the stationary-factory model. Phase II contains 17 narrative/innovation milestones: the converse mechanism and the inherited construction lead to the matched memory law and its scope.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md#targeted-reading-from-the-single-anchor) identifies the relevant sections and translates their conventions. Stabilizer-specific identities, catalytic conversions, and distillation codes are research dependencies identified in the canonical science and references. Full statements and proofs remain in [science/](../science/README.md).

The map covers the load-bearing ideas and their connections. Specialist calculations and additional technical detail remain in the linked scientific sources.

## Overview route

| Milestones | Local ingredients | Role in the complete account |
| --- | --- | --- |
| [M01–M04](#m01) | States, measurements, correlations, and channels | Describe a noisy input, an emitted state, and a deterministic physical process |
| [M05–M10](#m05) | Free states, source weight, resource monotones, and target overlap | Supply the objects that the converse compares |
| [M11–M13](#m11) | Quantum memory, classical controllers, and exact return | Integrate the background into the complete factory model |
| [M14–M22](#m14) | Reuse, a free-input comparison, and binary distinguishability | Establish finite and logarithmic memory necessity and its precise distinction from prior bounds |
| [M23–M29](#m23) | Batch distillation, a cyclic catalyst, and resource accounting | Establish achievability with the same source and return convention |
| [M30](#m30) | The lower and upper statements with their quantifiers aligned | Synthesize the matched theorem, physical meaning, and limitations |

## Phase I — Background/preliminaries

<a id="m01"></a>

### M01 — Pure targets and noisy density operators

**Central question.** What does it mean to supply a noisy quantum state while seeking a pure target?

**Understanding target.** Distinguish a pure-state projector, a density operator, and a convex mixture. Interpret a depolarized source as a physical input state whose mixture component is not automatically available as a classical label.

**Dependencies and story role.** No earlier milestone. This introduces the individual state objects from which the factory model is built.

**Conceptual connection.** Density operators let the same mathematical description include noisy sources, pure targets, and mixed catalysts.

**Sources.** [Source states and positive free components](../science/model.md#4-a-positive-free-component-in-the-source); [the explicit CCZ source](../science/construction.md#1-source-target-and-statement). Watrous §2.1.2, Definition 2.5; [state-language bridge](WATROUS_BRIDGE.md#states-registers-and-free-resources).

<a id="m02"></a>

### M02 — Measurements, infidelity, and error conventions

**Central question.** Which probability measures the quality of an emitted approximation to a pure target?

**Understanding target.** Interpret target overlap as the acceptance probability of a binary measurement. Distinguish this overlap from Watrous's root fidelity, and the project's half trace norm from the book's trace-distance naming convention. Explain why translating the error parameter matters.

**Dependencies and story role.** [M01](#m01). The target becomes an operational quality criterion rather than only a desired ket.

**Conceptual connection.** The same target projector defines output infidelity and later becomes the analytical test in the converse.

**Sources.** [Infidelity and trace distance](../science/construction.md#7-infidelity-and-trace-distance). Watrous §2.3.1, Definition 2.34; §3.2, Definition 3.11; Proposition 3.13; Theorem 3.33; [convention translation](WATROUS_BRIDGE.md#notation-and-error-conventions).

<a id="m03"></a>

### M03 — Marginals, correlations, and classical flags

**Central question.** What information is preserved, and what is lost, when only a subsystem's state is specified?

**Understanding target.** Distinguish a joint state from its reduced states and explain why fixed marginals do not imply a product. Recognize a genuinely classical–quantum joint state; a diagonal label marginal alone does not establish that structure.

**Dependencies and story role.** [M01](#m01). This extends the local state description to a source, memory, controller, and emitted systems.

**Conceptual connection.** Correlated catalysis and the phase-labelled construction both depend on retaining the correct joint-state description.

**Sources.** [Independent blocks and sequential reuse](../science/model.md#3-independent-fresh-blocks-and-sequential-reuse); [classical–quantum memory](../science/model.md#arbitrarily-large-classical-storage). Watrous §§2.1.3 and 2.2.3, especially Eq. (2.170); [state-language bridge](WATROUS_BRIDGE.md#states-registers-and-free-resources).

<a id="m04"></a>

### M04 — Channels, determinism, and discarded records

**Central question.** How does a channel represent a complete deterministic quantum process?

**Understanding target.** Explain complete positivity, trace preservation, and the inclusion of measurement outcomes and discarded registers in a channel. Distinguish an unconditional trace-preserving protocol from a success-conditioned operation.

**Dependencies and story role.** [M02](#m02), [M03](#m03). States and measurements are assembled into processes that can act within a larger correlated system.

**Conceptual connection.** Trace preservation supports repeated-use marginal arguments, while positivity supports the comparison of two different source inputs.

**Sources.** [Free states and operations](../science/model.md#1-free-states-and-operations); [a stationary call](../science/model.md#2-a-stationary-call). Watrous §§2.2.1–2.2.2, Definition 2.13 and Corollary 2.27.

<a id="m05"></a>

### M05 — Stabilizer operations and computational magic

**Central question.** Which states and operations are free in this factory, and what resource does a magic state supply?

**Understanding target.** Identify the convex stabilizer free set and the physical stabilizer-operation toolbox. Distinguish the explicitly defined computational T and CCZ targets from free states, and keep source magic and catalyst magic visible in the accounting.

**Dependencies and story role.** [M01](#m01), [M04](#m04). The generic channel framework acquires the resource restrictions relevant to fault-tolerant quantum computation.

**Conceptual connection.** A factory's limitation depends on both its supplied states and its allowed transformations.

**Sources.** [Free operations](../science/model.md#1-free-states-and-operations); [target conventions](../science/model.md#5-the-target-overlap-assumption). Watrous §§2.1.2 and 2.2.1 supply the general language; the stabilizer-specific bridge is in [states, registers, and free resources](WATROUS_BRIDGE.md#states-registers-and-free-resources) and [B2019](../references/related-work.md#b2019).

<a id="m06"></a>

### M06 — Positive free components of noisy sources

**Central question.** What does a positive free component say about a noisy input?

**Understanding target.** Interpret positive-semidefinite domination as a mixture containing a normalized free state. Explain why full rank supplies such a component and why its weight is neither a heralded branch nor a measure of the source's total magic.

**Dependencies and story role.** [M01](#m01), [M05](#m05). This identifies the input property that drives the converse.

**Conceptual connection.** A spectral property of one noisy state becomes an operator inequality that survives tensoring and positive maps.

**Sources.** [Source domination](../science/model.md#4-a-positive-free-component-in-the-source); [the inherited free-component method](../references/related-work.md#fl2022). Watrous §1.1.2, positive operators and operator order, and §2.1.2.

<a id="m07"></a>

### M07 — Free operations with retained reference systems

**Central question.** Why must the free-operation condition remain valid when other registers are retained?

**Understanding target.** Distinguish stabilizer preservation on an isolated input from complete stabilizer preservation with a reference. Explain why physical stabilizer operations satisfy the latter requirement and why old correlated outputs matter for sequential resource accounting.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M05](#m05). The operation class is made precise enough for a reusable device.

**Conceptual connection.** The role of a reference system in complete positivity has a resource-preservation counterpart, although the two conditions are distinct.

**Sources.** [Complete stabilizer preservation](../science/model.md#1-free-states-and-operations). Watrous §2.2.2, Theorem 2.22; [state and operation bridge](WATROUS_BRIDGE.md#states-registers-and-free-resources).

<a id="m08"></a>

### M08 — Relative entropy and data processing

**Central question.** How does relative entropy turn distinguishability into an inequality under a channel?

**Understanding target.** Interpret quantum relative entropy, its support condition, and its units. Explain why a channel or measurement cannot increase it, including when a quantum comparison is reduced to two classical outcomes.

**Dependencies and story role.** [M02](#m02), [M04](#m04). This provides the information-theoretic tool used in both resource monotonicity and the final binary test.

**Conceptual connection.** A lower bound on distinguishability after a simple test is also a lower bound before that test.

**Sources.** [Resource monotonicity](../science/converse.md#4-only-the-initial-catalyst-supplies-magic-in-the-comparison-run); [binary testing](../science/converse.md#5-a-binary-measurement-proves-the-finite-bounds). Watrous §5.2.1, Definition 5.18, and §5.2.3, Theorem 5.35.

<a id="m09"></a>

### M09 — Relative entropy of magic as a resource budget

**Central question.** How can distinguishability from the entire free set quantify stored magic?

**Understanding target.** Explain the minimization defining relative entropy of magic and derive its nonincrease under a free channel from data processing. Distinguish this monotonicity statement from additivity across two arbitrary resource states.

**Dependencies and story role.** [M05](#m05), [M07](#m07), [M08](#m08). The information measure becomes a resource budget attached to the catalyst.

**Conceptual connection.** The proof will charge a comparison experiment to its initial magic without needing a catalyst–target additivity theorem.

**Sources.** [Stored magic](../science/model.md#6-stored-magic-and-quantum-memory); [the monotonicity derivation](../science/converse.md#4-only-the-initial-catalyst-supplies-magic-in-the-comparison-run). Watrous §§5.2.1 and 5.2.3; [binary-test and memory bridge](WATROUS_BRIDGE.md#from-a-binary-test-to-quantum-memory).

<a id="m10"></a>

### M10 — Target tensor powers and stabilizer overlap

**Central question.** How well can a free state pass the test for many ideal target copies?

**Understanding target.** Interpret the maximum free overlap with a target tensor power and the known exponential rates for computational T and CCZ. Distinguish a single-copy overlap calculation, a tensor-power identity, and multiplicativity involving an arbitrary catalyst.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M05](#m05). This supplies the target-side input needed alongside the source's positive free component.

**Conceptual connection.** Stabilizer geometry makes a joint ideal-target test increasingly selective.

**Sources.** [Target overlap assumption](../science/model.md#5-the-target-overlap-assumption); [B2019](../references/related-work.md#b2019); [what finite enumeration establishes](../verification/README.md#stabilizer-enumeration). Watrous §1.1.2 on tensor-product operators and §2.3.1 on measurements.

<a id="m11"></a>

### M11 — Quantum memory with unrestricted classical storage

**Central question.** Can an arbitrarily large classical controller hide the quantum resource required by the factory?

**Understanding target.** Explain why relative entropy of magic is bounded by the number of quantum qubits even for a complete classical–quantum catalyst. Use the matching classical distribution and a maximally mixed quantum comparison state; identify coherently stored labels as quantum memory.

**Dependencies and story role.** [M03](#m03), [M09](#m09). Stored magic is connected to a concrete memory resource.

**Conceptual connection.** The classical label entropy cancels in the block-diagonal comparison, leaving the quantum contribution.

**Sources.** [Classical–quantum memory bound](../science/model.md#arbitrarily-large-classical-storage). Watrous §2.2.3, Eq. (2.170), and §5.2.1, Definition 5.18; [memory bridge](WATROUS_BRIDGE.md#from-a-binary-test-to-quantum-memory).

<a id="m12"></a>

### M12 — Exact correlated catalysis and the complete controller

**Central question.** What exactly must return unchanged for a catalyst to support the next call?

**Understanding target.** Distinguish exact marginal return from product return and from return only on success. Include the complete persistent controller and its correlations in the returned state, while separating temporary records that are discarded.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M07](#m07), [M11](#m11). The state, operation, and accounting foundations are joined in the catalytic interface.

**Conceptual connection.** A stationary density operator can include a classical phase that advances in each realization.

**Sources.** [Stationary call and complete controller](../science/model.md#2-a-stationary-call); [FL2026](../references/related-work.md#fl2026). Watrous §§2.1.3 and 2.2.3; [two-phase return example](WATROUS_BRIDGE.md#a-complete-two-phase-return-example).

<a id="m13"></a>

### M13 — The complete stationary-factory model

**Central question.** Which quantities and promises define the memory-minimization problem?

**Understanding target.** Assemble the independent source block, fixed input budget, pure target, allowed channel, exact complete marginal return, and output error into one model. Distinguish an accuracy-dependent catalyst family from a changing source or input budget, and recognize that a lower bound alone need not establish feasibility.

**Dependencies and story role.** [M06](#m06), [M10](#m10), [M11](#m11), [M12](#m12). This is the background phase's synthesis.

**Conceptual connection.** The meaning of the final asymptotic law comes from its fixed parameters and the resource being minimized.

**Sources.** [Model and resource accounting](../science/model.md); [the minimized quantity](../science/model.md#the-quantity-minimized-in-the-matching-law). Watrous §§2.1.2, 2.2.1, and 5.2.1 supply the state, process, and resource-measure language.

## Phase II — Narrative/innovation

<a id="m14"></a>

### M14 — Reuse without independent outputs

**Central question.** Why does every nominal emission retain its accuracy guarantee as correlations accumulate?

**Understanding target.** Explain the reuse induction using the reduced state of the fresh block and catalyst. Identify the two separate facts that fresh inputs are independent and that later trace-preserving operations leave earlier output marginals unchanged.

**Dependencies and story role.** [M04](#m04), [M12](#m12), [M13](#m13). This begins the converse with the operational consequence of exact stationarity.

**Conceptual connection.** Local marginal invariance is sufficient for repeated nominal accuracy despite a correlated global history.

**Sources.** [Sequential reuse proof](../science/converse.md#2-sequential-reuse-preserves-every-nominal-output-guarantee). Watrous §§2.1.3 and 2.2.1; [reuse-to-comparison bridge](WATROUS_BRIDGE.md#from-correlated-reuse-to-the-counterfactual).

<a id="m15"></a>

### M15 — From marginal accuracy to a joint target test

**Central question.** What joint guarantee follows from many individually accurate but correlated outputs?

**Understanding target.** Explain the commuting-projector union bound and its linear accumulation of worst-case infidelity. Distinguish this guaranteed joint overlap from an assertion that the outputs are independent.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M14](#m14). Separate emission guarantees become a single test of the whole retained stream.

**Conceptual connection.** Projectors on different output registers turn the classical union-bound principle into an operator inequality.

**Sources.** [Joint nominal accuracy](../science/converse.md#2-sequential-reuse-preserves-every-nominal-output-guarantee); [application to repeated use](../science/resources.md#6-correlations-and-repeated-use). Watrous §1.2.2, Eq. (1.246), and §2.3.1.

<a id="m16"></a>

### M16 — The all-free-input comparison

**Central question.** What does nominal accuracy imply when every fresh source block is replaced by a free state?

**Understanding target.** Follow tensor domination through the same positive sequential map and understand the resulting error amplification by the inverse all-free weight. Explain why the comparison is a mathematical consequence of linearity, not a heralded capability.

**Dependencies and story role.** [M06](#m06), [M07](#m07), [M15](#m15). This connects repeated accuracy to a counterfactual experiment with no fresh magic.

**Conceptual connection.** The small free component of each source becomes a rare but quantitatively constraining component of the whole input stream.

**Sources.** [Free-input comparison proof](../science/converse.md#3-replace-fresh-inputs-by-free-states-in-a-comparison-experiment). Watrous §1.1.2 on operator order and positive maps; [counterfactual bridge](WATROUS_BRIDGE.md#from-correlated-reuse-to-the-counterfactual).

<a id="m17"></a>

### M17 — Charging the comparison output to the initial catalyst

**Central question.** Which initial resource can account for the comparison experiment's accurate output?

**Understanding target.** Explain why appending free inputs, sequential free processing, and discarding define a free map from the initial catalyst to the emitted sequence. Identify that the comparison may consume or alter the catalyst completely.

**Dependencies and story role.** [M09](#m09), [M16](#m16). The comparison's output quality becomes a claim against a finite initial resource budget.

**Conceptual connection.** Nominal return enables repetition; resource monotonicity on a different run supplies the cost, without requiring return on that run.

**Sources.** [Initial-catalyst resource bound](../science/converse.md#4-only-the-initial-catalyst-supplies-magic-in-the-comparison-run). Watrous §5.2.3, Theorem 5.35; [counterfactual bridge](WATROUS_BRIDGE.md#from-correlated-reuse-to-the-counterfactual).

<a id="m18"></a>

### M18 — The finite binary and entropy converses

**Central question.** How does a binary target test turn the comparison experiment into a finite catalyst-resource bound?

**Understanding target.** Connect high comparison acceptance, small free-state acceptance, and relative-entropy data processing. Distinguish the conditions for the binary-divergence and entropy-form inequalities, and explain why the analytical test itself need not be a free stabilizer measurement.

**Dependencies and story role.** [M08](#m08), [M10](#m10), [M16](#m16), [M17](#m17). This integrates the converse's components into its finite theorem.

**Conceptual connection.** Target geometry supplies distinguishability, and distinguishability certifies stored magic.

**Sources.** [Finite theorem](../science/converse.md#theorem-1-finite-catalyst-resource-bound); [binary-test proof](../science/converse.md#5-a-binary-measurement-proves-the-finite-bounds). Watrous §§5.1.1 and 5.2.3, Theorem 5.35; [binary-test bridge](WATROUS_BRIDGE.md#from-a-binary-test-to-quantum-memory).

<a id="m19"></a>

### M19 — Finite-horizon guarantees versus exact stationarity

**Central question.** Which part of the converse actually requires a returned catalyst?

**Understanding target.** Separate a guaranteed-accuracy finite run from the stationary mechanism that certifies accuracy for every run length. Explain why the finite-horizon lemma permits an evolving controller but does not establish repeated accuracy from approximate one-call return.

**Dependencies and story role.** [M14](#m14), [M18](#m18). The proven mechanism's quantifiers are made explicit before taking an asymptotic limit.

**Conceptual connection.** An operational certificate of repeated accuracy and the resource bound conditional on that accuracy have different assumptions.

**Sources.** [Finite-horizon lemma](../science/converse.md#finite-horizon-lemma). Watrous §§2.1.3 and 2.2.1; [reuse-to-comparison bridge](WATROUS_BRIDGE.md#from-correlated-reuse-to-the-counterfactual).

<a id="m20"></a>

### M20 — Optimizing the horizon for logarithmic stored magic

**Central question.** Why does the useful repetition count grow logarithmically with inverse output error?

**Understanding target.** Explain the balance between accumulating target resource and amplifying the nominal error on the all-free comparison. Interpret the selected horizon, the leading logarithmic coefficient, and the dependence of the remainder on fixed source parameters.

**Dependencies and story role.** [M13](#m13), [M18](#m18), [M19](#m19). The finite theorem becomes the asymptotic necessity statement.

**Conceptual connection.** Exponential source-weight suppression and exponential target-overlap suppression meet at a logarithmic horizon.

**Sources.** [Horizon optimization](../science/converse.md#6-optimize-the-number-of-repetitions); [fixed-copy specialization](../science/converse.md#fixed-fresh-copy-count). Watrous §5.1.1 supplies the entropy and logarithm conventions; [memory bridge](WATROUS_BRIDGE.md#from-a-binary-test-to-quantum-memory).

<a id="m21"></a>

### M21 — Finite-memory error floors

**Central question.** What accuracy is impossible when the catalyst's stored resource is fixed?

**Understanding target.** Interpret the explicit positive error floor and the exclusion of exact pure-target output at finite stored resource. Translate the resource bound into a quantum-qubit bound while allowing arbitrary mixed catalysts and free classical storage.

**Dependencies and story role.** [M11](#m11), [M18](#m18), [M20](#m20). The asymptotic divergence is connected back to a finite device.

**Conceptual connection.** Choosing a horizon that demands more magic than the catalyst contains converts the finite inequality into a contradiction.

**Sources.** [Explicit error floor](../science/converse.md#7-an-explicit-error-floor); [quantum-memory consequences](../science/converse.md#8-consequences-for-quantum-memory). Watrous §§5.2.1–5.2.2; [memory bridge](WATROUS_BRIDGE.md#from-a-binary-test-to-quantum-memory).

<a id="m22"></a>

### M22 — Why total input magic does not remove the obstruction

**Central question.** What does this converse add when the fresh inputs already contain substantial total magic?

**Understanding target.** Distinguish a positive-free-component hypothesis from the strict input–target Rényi gap required by the closest catalyst-resource theorem. Explain what the two-input example establishes about theorem applicability, without treating it as an achievable two-input factory.

**Dependencies and story role.** [M06](#m06), [M09](#m09), [M18](#m18), [M20](#m20). This places the converse's scope and contribution alongside its predecessors.

**Conceptual connection.** Sufficient total resource and the ability to purify it with bounded reusable memory are different questions.

**Sources.** [Closest catalyst-resource bound](../references/related-work.md#rt2022); [explicit absence of the gap](../references/related-work.md#an-explicit-input-for-which-the-gap-is-absent). Watrous §5.2.1 supplies the relative-entropy foundation; the Rényi and magic-additivity ingredients are identified research dependencies.

<a id="m23"></a>

### M23 — A deterministic CCZ batch ingredient

**Central question.** What known batch process can supply accurate outputs at a constant input-to-output rate?

**Understanding target.** Identify the fixed noisy CCZ source, conversion cost, batch inputs, outputs, and correction radius. Explain why unsuccessful decoding still belongs to a deterministic channel and why source infidelity differs from its depolarizing mixture weight.

**Dependencies and story role.** [M04](#m04), [M05](#m05), [M13](#m13). This introduces the construction ingredient needed to complement the converse.

**Conceptual connection.** A constant-rate batch provides the raw material for a stationary one-output factory.

**Sources.** [Source and upper statement](../science/construction.md#1-source-target-and-statement); [inherited batch protocol](../science/construction.md#2-the-inherited-batch-protocol); [WHY2025](../references/related-work.md#why2025). Watrous §§2.2.1 and 2.3.1 supply the channel and measurement language; the code theorem is a research dependency.

<a id="m24"></a>

### M24 — Local stochastic errors and a global exponential bound

**Central question.** Why does the batch's whole-output error decrease exponentially below a fixed source threshold?

**Understanding target.** Connect independent faulty preparation groups, a decoding radius, and a union bound over uncorrectable patterns. Distinguish global batch infidelity from marginal infidelity and explain why passing the global bound to one marginal introduces no extra output-count factor.

**Dependencies and story role.** [M02](#m02), [M15](#m15), [M23](#m23). The batch's qualitative correction capability becomes a usable accuracy-versus-size relation.

**Conceptual connection.** A probabilistic bound on a classical error pattern controls overlap with the entire pure output target.

**Sources.** [Global exponential bound](../science/construction.md#3-a-global-exponential-error-bound). Watrous §1.2.2, Eq. (1.246), and §2.3.1; [batch-to-factory bridge](WATROUS_BRIDGE.md#from-a-batch-protocol-to-a-stationary-factory).

<a id="m25"></a>

### M25 — A fixed fresh-input budget and common block size

**Central question.** How can every call consume the same number of source states while the required batch grows?

**Understanding target.** Explain how the batch rate permits one accuracy-independent integer input budget. Account for discarded excess sources and free padding that makes a fresh source block and a padded output block have the same dimension.

**Dependencies and story role.** [M13](#m13), [M23](#m23). The variable-sized batch is recast into blocks suitable for a reusable interface.

**Conceptual connection.** Matching block dimensions enables the catalytic cycle without changing the charged source count.

**Sources.** [Fixed budget and padding](../science/construction.md#4-one-fixed-fresh-input-budget). Watrous §1.1.2 on tensor products and §2.2.1 on channels; [batch-to-factory bridge](WATROUS_BRIDGE.md#from-a-batch-protocol-to-a-stationary-factory).

<a id="m26"></a>

### M26 — The cyclic catalyst and exact phase-inclusive return

**Central question.** Why does a buffer whose phase advances nevertheless return its complete marginal exactly?

**Understanding target.** Interpret the mixture of raw-source prefixes, actual correlated batch-output prefixes, and classical phases. Follow how the wraparound branch and phase update restore the joint catalyst state, and why the emitted state is the average batch marginal with the inherited accuracy.

**Dependencies and story role.** [M03](#m03), [M12](#m12), [M24](#m24), [M25](#m25). This is the construction's central exact-return mechanism.

**Conceptual connection.** Stationarity of a mixed joint state can coexist with deterministic movement through its labelled components.

**Sources.** [Catalyst and exact return](../science/construction.md#5-the-catalyst-and-its-exact-return); [FL2026](../references/related-work.md#fl2026). Watrous §§2.1.3 and 2.2.3; [two-phase example](WATROUS_BRIDGE.md#a-complete-two-phase-return-example).

<a id="m27"></a>

### M27 — Initialization from the same noisy source

**Central question.** Can the required catalyst be prepared without an uncharged perfect magic seed?

**Understanding target.** Explain how one sampled phase, one actual noisy batch, and additional independent raw-source states prepare the catalyst mixture exactly. Separate exact preparation of that mixed state from perfect preparation of the target, and account for the one-time source cost.

**Dependencies and story role.** [M23](#m23), [M25](#m25), [M26](#m26). The formal catalyst becomes an operationally supplied resource.

**Conceptual connection.** An upper bound must account for the origin of its stored magic as well as its ongoing consumption.

**Sources.** [Exact initialization](../science/resources.md#2-exact-initialization-from-the-same-noisy-source). Watrous §§2.1.2 and 2.2.3; [batch-to-factory bridge](WATROUS_BRIDGE.md#from-a-batch-protocol-to-a-stationary-factory).

<a id="m28"></a>

### M28 — Bounded code-family gaps and every-accuracy achievability

**Central question.** Why does an available code family provide logarithmic memory for every sufficiently small error?

**Understanding target.** Explain why an exponential batch-error bound alone does not control gaps in the available code lengths. Use the bounded ratio of successive genera to relate the first adequate code to the requested accuracy and to the quantum, phase, and initialization costs.

**Dependencies and story role.** [M24](#m24), [M25](#m25), [M26](#m26), [M27](#m27). The construction is completed as an all-accuracy asymptotic upper bound.

**Conceptual connection.** Discrete code availability must be reconciled with a continuously varying target-error parameter.

**Sources.** [Choosing a batch for every accuracy](../science/construction.md#6-choosing-a-batch-for-every-target-accuracy); [initialization cost](../science/resources.md#2-exact-initialization-from-the-same-noisy-source). Watrous §5.1.1 supplies logarithm conventions; the code-family spacing argument is supplied by the canonical construction.

<a id="m29"></a>

### M29 — The complete resource ledger and verification limits

**Central question.** Which costs and guarantees are established by the logarithmic-memory construction?

**Understanding target.** Distinguish fresh input per call, initialization, persistent quantum memory, classical phase and decoder storage, peak workspace, and execution time. Explain the periodic full-batch cost and what finite overlap, cycle, and arithmetic checks establish relative to the analytical proofs.

**Dependencies and story role.** [M11](#m11), [M21](#m21), [M27](#m27), [M28](#m28). The upper construction is assessed as a complete resource statement.

**Conceptual connection.** Constant ongoing magic consumption is compatible with growing reusable storage and growing work on wraparound calls.

**Sources.** [Resource ledger](../science/resources.md#1-resource-ledger); [workspace and throughput](../science/resources.md#4-coherent-workspace-gate-count-and-throughput); [finite verification and its interpretation](../verification/README.md#interpretation). Watrous §§2.2.1 and 5.2.1 provide the ideal-channel and entropy foundations.

<a id="m30"></a>

### M30 — The matched memory theorem and its scope

**Central question.** What complete statement follows when necessity and achievability refer to the same factory model?

**Understanding target.** State the logarithmic minimum-memory law with a fixed permitted noisy CCZ source, a sufficient fixed input budget, physical stabilizer operations, and exact marginal return. Explain the stronger operation class of the converse, the inherited nature of the upper construction, and the limits concerning smaller budgets, approximate return, source drift, hardware noise, and timing.

**Dependencies and story role.** [M13](#m13), [M20](#m20), [M21](#m21), [M22](#m22), [M28](#m28), [M29](#m29). This is the narrative phase's synthesis and the global understanding target.

**Conceptual connection.** Constant fresh consumption and logarithmically increasing reusable quantum storage describe one matched resource tradeoff.

**Sources.** [The minimized quantity and matched law](../science/model.md#the-quantity-minimized-in-the-matching-law); [upper/lower alignment](../science/construction.md#8-relation-to-the-lower-bound); [scope of the resource law](../science/resources.md#7-boundary-of-the-matched-resource-law). Watrous §§2.2.1 and 5.2.3; [joining the learning route to the science](WATROUS_BRIDGE.md#joining-the-learning-route-to-the-science).
