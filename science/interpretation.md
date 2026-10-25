# What the catalyst cost means

The scientific question is whether a factory can produce increasingly accurate pure magic states while keeping both its fresh-input count and its retained catalyst resource bounded. Under the [stated deterministic model](model.md), a positive free component of the source and decreasing target free overlap prevent this.

The [converse](reuse_converse.md) gives an error floor for every finite stored-magic budget. Exponential target-overlap decay turns that floor into a logarithmic resource requirement. For a sufficiently low-noise CCZ source, the [cyclic construction](cyclic_construction.md) attains the same order with physical stabilizer operations.

## Three costs

| Cost | What is counted | Supported conclusion |
|---|---|---|
| Ongoing input consumption | Fresh noisy source copies supplied in each round | Can remain a fixed constant in the CCZ construction |
| Retained catalyst | Quantum registers and classical flag kept between rounds; their magic resource | Fidelity magic, relative entropy of magic, max-relative entropy and qubit count have optimal logarithmic order in the stated CCZ regime |
| Source-only initialization | Copies of the same noisy source used to prepare the catalyst by a deterministic free procedure | Logarithmic order is sufficient; necessity already follows from ordinary purification |

The first quantity is the constant-overhead advantage established by earlier catalytic constructions. The second is the retained-resource obligation established by the converse. The third gives an operational way to prepare the catalyst but has a separate lower-bound provenance.

The catalyst's resource is not consumed on its marginal in each round. A catalyst prepared for a fixed accuracy can be reused indefinitely with that same marginal accuracy. The divergence concerns a family of catalysts as the requested error tends to zero.

## Correlations and the meaning of reuse

The catalyst can correlate with its output, and different outputs can be correlated. Nevertheless, the reduced input to each fresh round is the same source block tensored with the same catalyst marginal. This is enough for the same unconditional output guarantee on every use.

For $`\ell`$ outputs the proof establishes joint target infidelity at most $`\ell\varepsilon`$. It does not identify the joint output with the product of its marginals. Nor does it turn the sufficient allocation $`\varepsilon\le\delta/\ell`$ into a necessary condition for a joint error target $`\delta`$. Correlations can change that comparison.

Conditioning on observed outcomes from earlier uses can change the conditional catalyst state. The unconditional marginal theorem is not a promise that every conditioned history has identical performance. Any persistent nonfree controller belongs in the returned catalyst.

## Exact return at a fixed noisy input

The return condition is imposed on one prescribed source state. It need not hold on every nearby source, or on the free source used in the proof's comparison experiment. Full rank of the actual source does not promote this one-state condition to a neighborhood condition.

This distinction separates the model from noise-robust catalysis, where exact catalyst preservation must persist throughout a neighborhood of inputs. The [related-work comparison](../references/RELATED_WORK.md#son2026) explains the different quantifiers.

The construction treats Clifford gates, measurements and feed-forward as noiseless free operations. It is a resource-theoretic result about noisy magic inputs, not a complete hardware fault-tolerance analysis.

## Controlled return error changes the reuse estimate

Suppose one instead has only the nominal guarantee
$`\tfrac12\|\omega_C-\tau\|_1\le\eta`$ at the prescribed input $`\rho^{\otimes k}\otimes\tau`$.

Write $`T`$ for the induced channel on the catalyst marginal. Contractivity and a triangle inequality give
$`\tfrac12\|T^j(\tau)-\tau\|_1\le j\eta`$.
The $`j`$th output infidelity can then be as large as
$`\varepsilon+(j-1)\eta`$. Consequently, the estimate used in the converse becomes

```math
\mathrm{Tr}[(I-\Pi_\ell)\Omega_\ell]
\le
\ell\varepsilon+\frac{\ell(\ell-1)}2\eta.
```

This identifies exactly where imperfect return enters the argument. The main theorems and the matching-order CCZ statement use $`\eta=0`$; their displayed finite-error formulas cannot be reused unchanged for a different return convention.

## Heralding and source variation

A successful branch of a heralded protocol is trace nonincreasing. After conditioning, the free-input comparison has a normalization depending on its own success probability. That probability can differ from success on the actual source. In addition, resource fidelity need not be monotone after conditioning, and returning the catalyst on success alone says nothing about its state after failure. The deterministic proof therefore does not automatically cover arbitrary heralded protocols.

A positive free component is also substantive. Pure resource inputs can have zero free weight and can permit exact transformations without any catalyst. If the source noise tends to zero with the requested error, its free weight is no longer a fixed constant. The general finite inequality should then be evaluated with the changing parameters.

Finally, fixing the fresh-input count matters. Ordinary growing batches can perform increasingly accurate distillation. The lower bound does not exclude that route.

## Scope of the optimality statement

The matched result is an asymptotic law for retained resource and memory at a fixed sufficiently weak CCZ depolarization and a sufficiently large fixed fresh-input budget. It includes arbitrary mixed and internally entangled catalysts, arbitrary correlations with outputs, and every deterministic free channel in the stated closure class.

No matching leading coefficient, minimum feasible batch size, optimized gate count, refresh latency, transient workspace or physical-device threshold is claimed. The explicit construction demonstrates existence and full resource accounting. The logarithmic retained-resource requirement is the general conclusion.
