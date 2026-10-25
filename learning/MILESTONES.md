# Understanding catalytic magic cost

This map organizes the scientific account into exactly 30 milestones. Its question is how much magic and memory a reusable factory must retain when a fixed noisy source supplies a fixed number of fresh inputs for each increasingly accurate output. The map identifies conceptual dependencies and authoritative sources. Detailed proofs and specialist calculations remain in the scientific pages. Use this map alongside the [Chitambar–Gour bridge](CHITAMBAR_GOUR_BRIDGE.md).

## Allocation and reading structure

The **background/preliminaries phase, M01–M12**, moves from individual states, operations, and accuracy criteria to the complete factory model. Twelve milestones are needed because the argument joins physical stabilizer control, geometric and entropic resource measures, operator comparison, and correlated catalysis. M12 integrates these ingredients into one precise question.

The **narrative/innovation phase, M13–M30**, follows two complementary arguments. M13–M21 assemble local reuse and comparison steps into the retained-resource converse and its distinction from earlier bounds. M22–M27 assemble an imported batch protocol into an exactly reusable CCZ factory with complete accounting. M28–M30 combine the arguments, identify their common scope, and state the contribution as a whole. The larger allocation to this phase reflects the project's central work: connecting an impossibility mechanism to a construction that attains its asymptotic order.

The single educational anchor is Eric Chitambar and Gilad Gour, [*Quantum Resource Theories*](https://doi.org/10.1103/RevModPhys.91.025001), Reviews of Modern Physics **91**, 025001 (2019), with the [arXiv version](https://arxiv.org/abs/1806.06107v3) available openly. Anchor section labels below follow the PDF's lettered subsections; the HTML edition renders these as numbered subsections. For example, III.A corresponds to III.1, IV.A.5 to IV.1.5, and V.C to V.3.

Anchor pointers supply background, not the later research results. In particular, the review uses root fidelity and describes product-return catalysis in V.C. This project uses squared fidelity and permits correlations while returning the catalyst marginal exactly. Those distinctions are explicit understanding targets. Research citations in the project remain proof dependencies rather than additional educational anchors.

## Phase I: Background/preliminaries

<a name="m01"></a>

### M01: States, noise, and retained registers

**ID and phase:** M01; background/preliminaries.

**Central question:** What physical objects are supplied, emitted, and retained by a magic-state factory?

**Understanding target:** Distinguish a quantum register from its density operator, a pure target from a noisy input, and a joint state from its marginals. Identify the source register, output register, and catalyst register without assuming their final joint state is a product.

**Dependencies and story role:** No earlier milestones. Establishes the local objects used throughout both phases.

**Conceptual connection:** The division into supplied, emitted, and retained registers makes the later division between consumed and stored resources precise.

**Source pointers:** [Factory model](../science/model.md), “Source, target and one round”; [interpretation](../science/interpretation.md), “Three costs.” C&G §II provides state and subsystem notation.

<a name="m02"></a>

### M02: Deterministic channels and operator order

**ID and phase:** M02; background/preliminaries.

**Central question:** Which mathematical properties let a comparison of input states survive physical processing?

**Understanding target:** Explain complete positivity, trace preservation, positive-semidefinite order, and expectation values of positive measurement operators. Distinguish a normalized deterministic output from a conditioned successful branch.

**Dependencies and story role:** M01. Supplies the local channel facts behind both the converse and the deterministic construction.

**Conceptual connection:** A positive operator inequality can become a bound on an observable failure probability after a physical channel.

**Source pointers:** [Factory model](../science/model.md), “Free states and operations”; [reuse converse](../science/reuse_converse.md), “2. Compare with free source inputs”; [interpretation](../science/interpretation.md), “Heralding and source variation.” C&G §§II and V.A supply channel and conversion background.

<a name="m03"></a>

### M03: A composable free-operation model

**ID and phase:** M03; background/preliminaries.

**Central question:** What must remain free when a protocol is embedded inside a larger sequence of operations?

**Understanding target:** Identify free states and deterministic free channels, and explain the roles of composition, identity extension, free ancillas, and discarding. Distinguish preservation of free states on an isolated system from a closure assumption that permits correlated spectator systems.

**Dependencies and story role:** M01–M02. Builds a framework in which one-round operations can be composed into the experiments used later.

**Conceptual connection:** Resource theory constrains entire physical procedures, including untouched registers and discarded outputs, rather than only a conversion on a single isolated state.

**Source pointers:** [Factory model](../science/model.md), “Free states and operations.” C&G §§III.A and III.C.1 provide tensor-product and complete-preservation structure.

<a name="m04"></a>

### M04: Stabilizer control and magic inputs

**ID and phase:** M04; background/preliminaries.

**Central question:** Why is a noisy nonstabilizer state a resource when Clifford control is freely available?

**Understanding target:** Identify stabilizer states, their convex hull, Clifford unitaries, Pauli measurement, classical feed-forward, and discarding as the physical setting. Distinguish a resource state from a nonfree gate, and distinguish the physical stabilizer-operation class from a larger mathematical free-operation class.

**Dependencies and story role:** M03. Specializes the general framework to the computational resource studied by the project.

**Conceptual connection:** The converse can use broad structural assumptions while achievability must exhibit operations permitted in the physical stabilizer model.

**Source pointers:** [Factory model](../science/model.md), “Free states and operations”; [CCZ construction](../science/cyclic_construction.md), “Statement.” C&G §IV.A.5 supplies the magic-state setting.

<a name="m05"></a>

### M05: Pure-target accuracy and fidelity

**ID and phase:** M05; background/preliminaries.

**Central question:** What does the error of a factory output measure?

**Understanding target:** Relate pure-target infidelity to the target projector's failure probability. Distinguish squared fidelity, root fidelity, trace distance, and purified distance, including the direction of the conversions used in this project. Recognize that numerical precision coefficients depend on the convention.

**Dependencies and story role:** M01–M02. Fixes the accuracy language before any resource inequality is compared.

**Conceptual connection:** Purity turns an abstract fidelity requirement into a binary probability statement, enabling the converse's target test.

**Source pointers:** [Factory model](../science/model.md), “Fidelity and resource conventions”; [CCZ construction](../science/cyclic_construction.md), “7. Error conventions and scope.” C&G §II uses root fidelity; the project's fidelity is its square.

<a name="m06"></a>

### M06: Free fidelity as retained resource

**ID and phase:** M06; background/preliminaries.

**Central question:** How does closeness to the free-state set quantify stored magic?

**Understanding target:** Define maximum free fidelity and its negative base-two logarithm. Explain why a free channel can increase maximum free fidelity while its logarithmic resource cannot increase. Distinguish this monotonicity from additivity under tensor products.

**Dependencies and story role:** M03–M05. Introduces the resource quantity bounded by the central theorem.

**Conceptual connection:** Fidelity data processing turns a geometric comparison with free states into an operational restriction on a catalyst.

**Source pointers:** [Factory model](../science/model.md), “Fidelity and resource conventions”; [reuse converse](../science/reuse_converse.md), “3. Use a channel whose only resource input is the catalyst.” C&G §§VI.A.2, VI.B, and VI.D supply monotonicity and geometric context.

<a name="m07"></a>

### M07: Entropic measures, operator domination, and memory size

**ID and phase:** M07; background/preliminaries.

**Central question:** Which different resource quantities can express the cost of the same catalyst?

**Understanding target:** Distinguish logarithmic free fidelity, relative entropy to the free set, minimized max-relative entropy, and qubit count. Identify the ordering $`M_{\mathcal F}\ge E_{\mathcal F}\ge G_{\mathcal F}`$ and the special role of the free maximally mixed state in bounding magic measures by register size.

**Dependencies and story role:** M02–M06. Establishes the cost vocabulary needed to interpret different lower bounds without conflating them.

**Conceptual connection:** Entropic distinguishability, operator domination, and physical memory size describe related but unequal constraints on stored resource.

**Source pointers:** [Resource costs](../science/resource_costs.md), “Which resource measures inherit the bound?” and “A stronger direct bound for max-relative entropy and qubits.” C&G §§VI.C and VI.E.2 supply entropy and robustness context; the dimension implication is specified locally.

<a name="m08"></a>

### M08: A noisy state's free component

**ID and phase:** M08; background/preliminaries.

**Central question:** What does the inequality $`\rho\ge p\gamma`$ say about the supplied noisy state?

**Understanding target:** Interpret a positive normalized free component, distinguish a valid weight from the largest possible weight, and explain why full rank supplies one when the maximally mixed state is free. Understand that a free weight can vanish for pure resource inputs.

**Dependencies and story role:** M02–M04. Introduces the source property that will be amplified across repeated uses.

**Conceptual connection:** The free-state geometry of one noisy input becomes a positive comparison contribution inside a long deterministic protocol.

**Source pointers:** [Factory model](../science/model.md), “Source, target and one round”; [magic targets](../science/magic_targets.md), “A useful source free weight”; [related work](../references/RELATED_WORK.md#fangliu2022). C&G §III.D.1 supplies convex-set background; the purification comparison is a separate research ingredient.

<a name="m09"></a>

### M09: Tensor-power target benchmarks

**ID and phase:** M09; background/preliminaries.

**Central question:** How well can free states imitate several ideal target outputs together?

**Understanding target:** Define the actual tensor-power overlap sequence $`f_\ell`$, distinguish it from an assumed product of single-copy overlaps, and identify the established exponential sequences for T and CCZ. Distinguish finite enumeration of small cases from the theorem establishing every tensor power.

**Dependencies and story role:** M04–M06. Supplies the target benchmark that competes with the source free-component weight in the converse.

**Conceptual connection:** A computational target's geometry becomes an exponential scale against which repeated-output accuracy can be assessed.

**Source pointers:** [Magic targets](../science/magic_targets.md), “T and CCZ conventions”; [verification account](../verification/README.md); [Bravyi dependency](../references/RELATED_WORK.md#bravyi2019). C&G §§IV.A.5 and VI.D provide background; the exact overlap and multiplicativity results come from the cited research.

<a name="m10"></a>

### M10: Exact marginal catalysis

**ID and phase:** M10; background/preliminaries.

**Central question:** In what sense can a catalyst be returned unchanged while it becomes correlated with the output?

**Understanding target:** Distinguish equality of the catalyst marginal from product return of the joint state. Identify the independent fresh-input requirement, the inclusion of all reusable nonfree memory, and the difference between unconditional marginals and states conditioned on an earlier outcome.

**Dependencies and story role:** M01–M05. Establishes the exact return convention that makes the project's factory model both permissive and reusable.

**Conceptual connection:** Catalysis concerns persistence of a resource under a specified transformation; correlations determine which persistence statement is actually available.

**Source pointers:** [Factory model](../science/model.md), “Source, target and one round”; [interpretation](../science/interpretation.md), “Correlations and the meaning of reuse.” C&G §V.C gives product-return catalysis as background. The marginal-return model is defined locally and its reuse principle is attributed to Fang and Liu.

<a name="m11"></a>

### M11: The precision limit and its three costs

**ID and phase:** M11; background/preliminaries.

**Central question:** What is held fixed, and what may grow, as the required output error tends to zero?

**Understanding target:** Keep the noisy source, target, and per-round input count fixed while allowing the channel and finite-dimensional catalyst to depend on accuracy. Distinguish ongoing source consumption, retained catalyst resource, and source-only initialization from transient processing workspace.

**Dependencies and story role:** M07–M10. Converts the one-round task into the precise family of tasks addressed by an asymptotic cost law.

**Conceptual connection:** A precision limit for a reusable device has different quantifiers from the usual limit of converting larger and larger input batches.

**Source pointers:** [Factory model](../science/model.md), “Source, target and one round”; [interpretation](../science/interpretation.md), “Three costs” and “Scope of the optimality statement.” C&G §§V.A–V.C provide conversion context; the fixed-input precision limit is specified by this project.

<a name="m12"></a>

### M12: Synthesis of the factory question

**ID and phase:** M12; background/preliminaries.

**Central question:** Can an exactly reusable factory make its outputs arbitrarily accurate while keeping both ongoing input consumption and retained resource bounded?

**Understanding target:** Assemble the states, free operations, positive source weight, pure-target benchmark, return condition, and cost definitions into the complete mathematical task. Explain why a bound on source consumption alone cannot settle the retained-resource question, and why a retained-resource lower bound needs an achievability comparison to establish optimal order.

**Dependencies and story role:** M01–M11. Ends the background phase by integrating its local concepts into the project's global problem.

**Conceptual connection:** Resource conversion, catalysis, and precision become one operational accounting question with distinct necessary and sufficient claims.

**Source pointers:** [Factory model](../science/model.md), “Scientific results and reading route”; [interpretation](../science/interpretation.md), opening and “Three costs.” C&G §§III.A, V.C, and VI.A supply the organizing framework; the complete question and its quantifiers are local.

## Phase II: Narrative/innovation

<a name="m13"></a>

### M13: Reuse despite output correlations

**ID and phase:** M13; narrative/innovation.

**Central question:** Why does an exact catalyst marginal suffice to preserve each later output's accuracy?

**Understanding target:** Follow the marginal induction: an independent fresh block and the unchanged catalyst marginal reproduce the same reduced channel input, while a trace-preserving operation leaves earlier output marginals unchanged. Distinguish this unconditional conclusion from independence or identical conditional performance.

**Dependencies and story role:** M02–M03, M10, M12. Starts the narrative with the local reuse mechanism needed to create a long output sequence.

**Conceptual connection:** Local channel inputs can remain stationary even when the full history develops correlations.

**Source pointers:** [Reuse converse](../science/reuse_converse.md), “1. Repetition preserves the marginal promise”; [Fang–Liu attribution](../references/RELATED_WORK.md#fangliu2026). C&G §V.C supplies catalytic context, not this correlated-reuse result.

<a name="m14"></a>

### M14: A joint target test without independent outputs

**ID and phase:** M14; narrative/innovation.

**Central question:** What collective accuracy statement follows from the individual output guarantees?

**Understanding target:** Explain the commuting-projector union bound giving joint product-target infidelity at most $`\ell\varepsilon`$. Recognize it as a sufficient upper estimate, without inferring product structure or a necessary per-output error allocation for every correlated stream.

**Dependencies and story role:** M05, M09, M13. Converts local marginal accuracy into the global test used by the proof.

**Conceptual connection:** A product target defines a collective event even when the actual output state is correlated.

**Source pointers:** [Reuse converse](../science/reuse_converse.md), “1. Repetition preserves the marginal promise”; [interpretation](../science/interpretation.md), “Correlations and the meaning of reuse.” C&G §II supplies measurement background; the operator estimate is derived locally.

<a name="m15"></a>

### M15: Replace the fresh inputs by their free component

**ID and phase:** M15; narrative/innovation.

**Central question:** What survives when the entire repeated protocol is fed free source inputs instead?

**Understanding target:** Derive the comparison $`\Omega_\ell\ge p^{k\ell}\Xi_\ell`$ and the resulting comparison-state failure bound. Explain normalization, the exponential weight, and why the catalyst need not be returned in this second experiment.

**Dependencies and story role:** M02–M03, M08, M13–M14. Builds the main operator comparison across the complete repeated channel.

**Conceptual connection:** Tensor products multiply a single-input free weight, while complete positivity transports it through an arbitrarily complicated deterministic factory.

**Source pointers:** [Reuse converse](../science/reuse_converse.md), “2. Compare with free source inputs”; [purification dependency](../references/RELATED_WORK.md#fangliu2022). C&G §§II and III.A supply channel-composition background; the free-component method has the separately cited provenance.

<a name="m16"></a>

### M16: Isolate the catalyst as the resource input

**ID and phase:** M16; narrative/innovation.

**Central question:** Why does the comparison experiment constrain the initial catalyst rather than the total noisy input batch?

**Understanding target:** Identify the free channel obtained by fixing all fresh inputs to free states, and establish $`F_{\mathcal F}(\tau)\le F_{\mathcal F}(\Xi_\ell)`$ with the correct direction. Explain which closure assumptions make the construction free.

**Dependencies and story role:** M03, M06, M15. Turns the comparison experiment into a statement about retained resource alone.

**Conceptual connection:** Removing every other resource input lets data processing assign the remaining operational capability to the catalyst.

**Source pointers:** [Reuse converse](../science/reuse_converse.md), “3. Use a channel whose only resource input is the catalyst.” C&G §§III.A, VI.A.2, and VI.B provide compositional monotonicity background.

<a name="m17"></a>

### M17: The finite-error fidelity converse

**ID and phase:** M17; narrative/innovation.

**Central question:** How does a target test turn the comparison state's accuracy into a catalyst-resource bound?

**Understanding target:** Combine the two-outcome fidelity inequality with the free target overlap to obtain the finite-error theorem for every integer repetition count. Distinguish the analytical measurement used for a bound from a free operation that the factory must implement. Identify why neither catalyst additivity nor an input-target resource gap enters.

**Dependencies and story role:** M05–M06, M09, M14–M16. Completes the converse mechanism as one global necessary inequality.

**Conceptual connection:** Ordinary distinguishability under a binary measurement bounds the resource content of a reusable device.

**Source pointers:** [Reuse converse](../science/reuse_converse.md), “Finite-error theorem” and “3. Use a channel whose only resource input is the catalyst.” C&G §§II and VI.B provide fidelity-processing context; the theorem is derived in the project.

<a name="m18"></a>

### M18: A bounded resource budget sets an accuracy floor

**ID and phase:** M18; narrative/innovation.

**Central question:** What does the finite-error theorem forbid when stored fidelity resource is bounded?

**Understanding target:** Express the theorem as an error floor optimized over integer repetitions. Explain why $`f_\ell\to0`$ suffices to make that floor positive for every finite resource budget, even without a uniform catalyst-dimension bound. Keep necessity distinct from a construction achieving the floor.

**Dependencies and story role:** M06, M09, M17. Gives the converse an operational meaning before taking an asymptotic limit.

**Conceptual connection:** A resource measure can constrain a device's accuracy more directly than its Hilbert-space dimension does.

**Source pointers:** [Resource costs](../science/resource_costs.md), “A finite stored-resource budget gives an error floor.” C&G §VI.A.2 supplies monotone-based restrictions; the explicit floor is local.

<a name="m19"></a>

### M19: Balance repetition against source noise

**ID and phase:** M19; narrative/innovation.

**Central question:** Why does exponential target-overlap decay force logarithmic growth of stored resource?

**Understanding target:** Explain the competition between target overlap $`2^{-a\ell}`$ and comparison error $`\ell\varepsilon p^{-k\ell}`$. Identify the repetition scale, the logarithmic correction, and the coefficient $`a/(a+kb)`$, with $`b=\log_2(1/p)`$. Preserve the fixed-source and fixed-input quantifiers.

**Dependencies and story role:** M08–M09, M11, M17–M18. Converts the finite bound into the project's precision law.

**Conceptual connection:** Two exponential scales in a repeated experiment produce a resource cost proportional to the logarithm of inverse error.

**Source pointers:** [Resource costs](../science/resource_costs.md), “Logarithmic fidelity-resource cost.” C&G §§V.B and VI.C supply asymptotic and entropic context; this optimization and coefficient are local.

<a name="m20"></a>

### M20: Separate inherited bounds from the stronger memory bound

**ID and phase:** M20; narrative/innovation.

**Central question:** Which catalyst costs inherit the fidelity bound, and which admit a stronger direct comparison?

**Understanding target:** Apply $`M\ge E\ge G`$ and the magic dimension bounds without reversing an implication. Explain how direct max-relative-entropy domination gives the stronger coefficient $`a/(kb)`$ for finite $`M`$ and qubits when $`kb>0`$, while the proved relative-entropy coefficient remains $`a/(a+kb)`$. Recognize that no coefficient is claimed optimal.

**Dependencies and story role:** M07, M15–M17, M19. Translates the abstract converse into distinct statements about stored magic and retained memory.

**Conceptual connection:** An order-based resource measure can control the target test more sharply than a fidelity comparison, but that improvement belongs only to the quantities the order argument bounds.

**Source pointers:** [Resource costs](../science/resource_costs.md), “Which resource measures inherit the bound?” and “A stronger direct bound for max-relative entropy and qubits.” C&G §§VI.C and VI.E.2 supply the measure framework; the stronger comparison is local.

<a name="m21"></a>

### M21: Locate the distinction from earlier catalytic bounds

**ID and phase:** M21; narrative/innovation.

**Central question:** Which regimes does this converse reach beyond the compared resource-gap theorem?

**Understanding target:** Distinguish the earlier strict input-target Rényi gap from target-catalyst additivity. Explain why pure T and CCZ targets do have strong fidelity multiplicativity against arbitrary mixed catalysts. Use the noisy-T example to identify a fixed batch for which every allowed gap fails, without treating that example as an achievable factory.

**Dependencies and story role:** M06–M10, M17–M20. Integrates the converse with its exact scientific provenance and prevents an incorrect novelty explanation.

**Conceptual connection:** A theorem's operational reach depends on all its hypotheses, and a separation of hypotheses is distinct from a construction in the separated regime.

**Source pointers:** [Magic targets](../science/magic_targets.md), “Strong multiplicativity for a small pure target” and “Absence of every Renyi gap in the earlier converse”; [Rubboli–Tomamichel comparison](../references/RELATED_WORK.md#rubboli2022). C&G §§V.C, VI.A.4, and VI.C provide catalytic and additivity background; the later theorem comparison has separate research sources.

<a name="m22"></a>

### M22: A deterministic CCZ batch with a global guarantee

**ID and phase:** M22; narrative/innovation.

**Central question:** What batch-distillation capability is sufficient to begin a matching construction?

**Understanding target:** Identify the imported constant-rate CCZ protocol, its deterministic treatment of all decoder outcomes, and its global infidelity guarantee. Relate fixed depolarization $`\nu`$ to stochastic error $`7\nu/8`$ while keeping the valid free weight $`p=\nu`$ distinct. Identify the source regime and absence of a perfect magic seed.

**Dependencies and story role:** M02, M04–M05, M08–M09, M11–M12. Starts the constructive branch with a concrete physical batch operation.

**Conceptual connection:** The same fixed noisy source must satisfy both the converse's free-component premise and the construction's small-error premise.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “1. The batch protocol and its error guarantee”; [Wills–Hsieh–Yamasaki dependency](../references/RELATED_WORK.md#wills2025). C&G §§IV.A.5 and V.B provide distillation background; the batch theorem is a later imported result.

<a name="m23"></a>

### M23: Reach every sufficiently small requested error

**ID and phase:** M23; narrative/innovation.

**Central question:** Why does the batch family give logarithmic size at every small accuracy rather than only along a sparse subsequence?

**Understanding target:** Connect linear rate and decoding distance to exponential error suppression, and explain why bounded ratios of successive available code lengths are also needed. Use the explicit code family to select a batch with size $`O(\log(1/\varepsilon))`$ for each sufficiently small error.

**Dependencies and story role:** M11, M19, M22. Makes the construction's asymptotic quantifier match the converse's precision limit.

**Conceptual connection:** A continuous accuracy requirement must be realized using a discrete family of physical protocols.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “1. The batch protocol and its error guarantee” and “2. Code lengths can track every requested accuracy.” C&G §V.B supplies asymptotic-conversion context; the finite code-family control is supplied by the cited construction and local accounting.

<a name="m24"></a>

### M24: Fix the input count and prepare the phase label exactly

**ID and phase:** M24; narrative/innovation.

**Central question:** How can varying batch sizes support one fixed per-round source budget?

**Understanding target:** Explain output rounding to a power of two, the bounded input-to-output ratio, and padding with free registers. Identify why these choices give one sufficient constant $`K=3360`$ and an exactly preparable uniform flag, without asserting that every smaller budget is feasible. Count discarded raw copies as supplied inputs.

**Dependencies and story role:** M03–M04, M11, M22–M23. Adapts the batch primitive to the uniform register and input structure needed by a reusable factory.

**Conceptual connection:** Rate statements become exact operational budgets only after integer sizes, classical randomness, and discarded inputs are accounted for.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “3. A single fixed input count and an exactly preparable flag.” C&G §§III.A and IV.A.5 supply free-ancilla and stabilizer-operation context; the rounding and constants are specified locally.

<a name="m25"></a>

### M25: The cyclic state returns exactly

**ID and phase:** M25; narrative/innovation.

**Central question:** How does the catalyst exchange stored batch outputs for fresh raw inputs without changing its marginal?

**Understanding target:** Interpret each flag-conditioned summand as a combination of raw blocks and a marginal of the actual batch output. Follow ordinary emission and batch refresh, and explain why the full conditional states cycle with unchanged weights, including the flag's correlations with memory.

**Dependencies and story role:** M10, M13, M22–M24. Establishes the central exact-return identity of the constructive branch.

**Conceptual connection:** A stationary mixture of phases converts a many-output batch protocol into a one-output reusable procedure.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “4. The catalyst and the exact-return proof”; [Fang–Liu dependency](../references/RELATED_WORK.md#fangliu2026). C&G §V.C supplies catalytic context; the correlated cyclic construction is attributed to Fang and Liu.

<a name="m26"></a>

### M26: Verify the factory's output and retained cost

**ID and phase:** M26; narrative/innovation.

**Central question:** Does the cyclic procedure realize the promised factory using only the stated free operations and retained registers?

**Understanding target:** Derive the emitted state's average over batch marginals and inherit accuracy from the global batch guarantee. Explain the classical flag update without a coherent non-Clifford counter. Count $`3K(m-1)+\log_2m`$ retained qubits and bound stored magic by that dimension, while distinguishing transient processing workspace.

**Dependencies and story role:** M04–M07, M11, M23–M25. Completes the construction as a physically admissible upper bound in the same operational model as the converse.

**Conceptual connection:** Exact return, output quality, and full resource accounting must hold in one implementation for an achievability claim to be meaningful.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “Output accuracy,” “Every operation is free in the stated model,” and “5. Retained memory and magic resource.” C&G §§III.A, IV.A.5, and VI.C provide operation and measure context; the complete accounting is local.

<a name="m27"></a>

### M27: Prepare the catalyst and identify the startup bound's provenance

**ID and phase:** M27; narrative/innovation.

**Central question:** Can the catalyst itself be prepared from the same noisy source, and why must that preparation consume more inputs at higher accuracy?

**Understanding target:** Construct the exact cyclic state from the actual noisy batch output and additional raw blocks, with no ideal target seed or tomography requirement. Distinguish the fixed worst-case initialization budget from expected stopping cost. Explain why composing preparation with the first use already yields the logarithmic startup lower bound through ordinary purification, without using catalyst return.

**Dependencies and story role:** M03, M08, M11, M22–M26. Completes source accounting and separates the inherited preparation constraint from the new retained-resource conclusion.

**Conceptual connection:** Resource preparation and resource retention are different operational questions even when both have logarithmic scaling.

**Source pointers:** [CCZ construction](../science/cyclic_construction.md), “6. Exact preparation and optimal source-only initialization order”; [resource costs](../science/resource_costs.md), “Preparation cost has a different provenance.” C&G §§V.A, VI.A.2, and VI.A.4 provide preparation and monotonicity background; the startup comparison uses the separately cited purification principle.

<a name="m28"></a>

### M28: Match the optimized retained-resource orders

**ID and phase:** M28; narrative/innovation.

**Central question:** In what precise regime do the converse and construction determine the optimal scaling?

**Understanding target:** Combine the positive source free weight, CCZ tensor-power overlap, and constructed upper bounds to obtain logarithmic optimal order for qubits and each stated magic measure. Interpret separate infima over factories and avoid requiring a common optimizer. Retain the sufficiently weak fixed noise and sufficiently large fixed input-budget conditions.

**Dependencies and story role:** M09, M11, M19–M20, M22–M27. Joins the two narrative branches into the matched scientific result.

**Conceptual connection:** A universal necessary cost and one admissible construction determine an asymptotic order even when their leading constants differ.

**Source pointers:** [Resource costs](../science/resource_costs.md), “Matching orders for sufficiently low-noise CCZ”; [CCZ construction](../science/cyclic_construction.md), “5. Retained memory and magic resource.” C&G §§V.B and VI.A provide operational-optimization context; the matching law follows from this project's combined arguments.

<a name="m29"></a>

### M29: Identify the assumptions that change the conclusion

**ID and phase:** M29; narrative/innovation.

**Central question:** Which nearby factory models require a different argument?

**Understanding target:** Locate how approximate return modifies accumulation, how heralding changes normalization and monotonicity, and how zero or accuracy-dependent free weight changes the comparison. Distinguish exact return at one source from return on an input neighborhood, and constant fresh-input count from ordinary growing-batch distillation. Preserve the difference between marginal and joint-stream accuracy.

**Dependencies and story role:** M02–M03, M08, M10–M11, M13–M20, M28. Tests the logical scope of the combined result through its actual assumptions, without claiming extensions.

**Conceptual connection:** An operational theorem is specified by quantifiers, error conventions, and success conditions as well as its asymptotic formula.

**Source pointers:** [Interpretation](../science/interpretation.md), “Correlations and the meaning of reuse,” “Exact return at a fixed noisy input,” “Controlled return error changes the reuse estimate,” “Heralding and source variation,” and “Scope of the optimality statement.” C&G §§V.A–V.C provide contrasting conversion settings; the boundary analysis is local.

<a name="m30"></a>

### M30: Synthesis of the scientific contribution

**ID and phase:** M30; narrative/innovation.

**Central question:** What does the complete project establish about reusable magic-state factories?

**Understanding target:** Explain the connected result: constant ongoing input consumption can coexist with exact marginal reuse, while positive source free weight and tensor-power target free overlap tending to zero force growing retained magic as output error vanishes. Under exponential overlap decay, the lower bounds are logarithmic for the stated magic measures and retained memory. In the stated CCZ regime the optimal order is logarithmic. Connect that conclusion to the finite-error mechanism, the absent resource-gap requirement, the constructive witness, and the separate provenance of startup cost. Identify the unoptimized quantities and model boundaries without turning them into broader impossibility claims.

**Dependencies and story role:** M12–M29. Ends the narrative phase by integrating mechanism, attainability, attribution, and interpretation into one global account.

**Conceptual connection:** Reusability describes persistence under operation; precision determines how much resource the reusable device must contain.

**Source pointers:** [Factory model](../science/model.md), “Scientific results and reading route” and “Attribution”; [interpretation](../science/interpretation.md), “Three costs” and “Scope of the optimality statement”; [related work](../references/RELATED_WORK.md), “What is imported and what is established here?” C&G §§III.A, V.C, and VI.A supply the unifying resource-theory framework; the scientific synthesis rests on the project's canonical proofs and cited research dependencies.
