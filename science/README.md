# Scientific account

How must a reusable magic-state factory's stored resource grow when its output becomes more accurate while its fresh noisy-input budget stays fixed? The account below answers this question through a common model, a converse, an attaining CCZ construction and a resource ledger.

## Reading route

| Page | Role in the argument |
|---|---|
| [Model](model.md) | Free operations, exact marginal return, independent fresh blocks, positive source weight, target overlaps and complete memory accounting. |
| [Converse](converse.md) | Reuse and a free-input comparison yield finite stored-resource bounds, logarithmic necessity and nonzero error floors. |
| [Construction](construction.md) | Constant-rate batch distillation and a stationary catalytic cycle attain logarithmic CCZ memory at a sufficient constant input budget. |
| [Resources](resources.md) | Initialization, quantum/classical storage, workspace, throughput, joint-output accuracy and the matched resource law. |

For foundations and worked examples, follow the [30-milestone map](../learning/MILESTONES.md) and [Watrous bridge](../learning/WATROUS_BRIDGE.md). The pages above own the complete statements and proofs.

## Find a result

- **Principal finite converse:** [Theorem 1](converse.md#theorem-1-finite-catalyst-resource-bound), followed by its reuse, positivity and binary-test proof.
- **Other stored-resource measures:** [definitions](model.md#other-stored-resource-measures), [finite bounds](converse.md#companion-resource-bounds) and [logarithmic consequences](converse.md#fidelity-and-max-relative-entropy-costs).
- **Quantum width and free classical storage:** [complete-controller model](model.md#the-complete-persistent-controller), [dimension bound](model.md#arbitrarily-large-classical-storage) and [memory consequences](converse.md#8-consequences-for-quantum-memory).
- **Attainment and initialization:** [construction statement](construction.md#1-source-target-and-statement), [exact return identity](construction.md#5-the-catalyst-and-its-exact-return) and [source-only preparation bound](resources.md#source-only-initialization-lower-bound).
- **Synthesis:** [matched resource law](resources.md#7-boundary-of-the-matched-resource-law) at the same fixed source, target, operations and error convention.

## One comparison experiment, several resource bounds

The source condition supplies a positive free component. Exact nominal return lets the factory be reused while keeping the same marginal output guarantee. Positivity transfers the joint target accuracy to the same circuit with every fresh block replaced by a free state. The initial catalyst is then the only source of magic. A binary target test turns exponentially small free overlap into stored-resource bounds; the direct relative-entropy inequality gives the strongest leading coefficient derived here.

The upper bound combines two imported ingredients: a deterministic constant-rate batch protocol with exponentially small global error, and a catalytic conversion that stores unfinished inputs together with completed output prefixes. Their explicit combination supplies exact marginal return, a fixed input count per emission and logarithmic memory. Initialization uses the same noisy source. Its lower bound is an ordinary-purification consequence, distinct from the requirement that resource remain stored between uses.

## Attribution and evidence

The [related-work account](../references/related-work.md) identifies imported stabilizer-overlap identities, batch-distillation and catalytic-conversion results, together with precise theorem pointers and comparisons to earlier purification and catalyst bounds. The reuse-based stored-resource converse and its matched interpretation are developed in this account.

The [finite checks](../verification/README.md) reproduce explicit overlaps, correlated-state identities and parameter arithmetic. The general theorem, tensor-power identities and every-accuracy scaling rest on the written proofs and cited analytical results. The lower bound applies to every fixed finite noisy-input budget; the matching CCZ upper bound requires the stated source quality and a sufficient constant budget.
