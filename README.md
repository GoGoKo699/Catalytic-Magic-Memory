# Catalytic Magic Cost

**How much magic must a reusable factory retain when its output error approaches zero?** This project gives catalyst-resource and memory lower bounds for deterministic magic-state distillation with a fixed noisy source and a fixed number of fresh inputs per output. For sufficiently low-noise CCZ sources and a sufficiently large fixed input budget, an explicit construction matches the logarithmic order.

A round returns the catalyst exactly on its marginal. Correlations with the output are allowed. The catalyst can be mixed and internally entangled, and its size and state can depend on the requested accuracy.

| Resource or statement | Result | Conditions |
|---|---|---|
| Stored fidelity resource and relative entropy of magic | $`\Omega(\log(1/\varepsilon))`$ | Positive source free weight; exponentially decreasing target free overlap; fixed fresh-input count |
| Retained catalyst qubits | $`\Omega(\log(1/\varepsilon))`$ | Same assumptions in qubit magic theory |
| Optimal retained CCZ catalyst cost | $`\Theta(\log(1/\varepsilon))`$ for qubits and the stated magic measures | Sufficiently low fixed depolarization and sufficiently large fixed input count |
| Source-only initialization | $`\Theta(\log(1/\varepsilon))`$ in the same CCZ regime | Deterministic preparation from the noisy source; the lower bound follows from established ordinary purification |

Here $`\varepsilon`$ is target infidelity. A constant fresh-input overhead can coexist with a diverging retained resource. The converse makes no assumption that the input batch is less resourceful than one target.

## The finite-error converse

Suppose the fixed source obeys $`\rho\ge p\gamma`$ for a normalized free state $`\gamma`$ and $`p>0`$. Each round consumes $`k`$ independent source copies and returns its catalyst $`\tau`$ exactly. Define squared fidelity, maximum free fidelity and target overlap by

```math
F(x,y)=\|\sqrt{x}\sqrt{y}\|_1^2,
\qquad
F_{\mathcal F}(x)=\max_{\sigma\in\mathcal F}F(x,\sigma),
\qquad
f_\ell=\max_{\sigma\in\mathcal F}\mathrm{Tr}(\psi^{\otimes\ell}\sigma).
```

For every integer $`\ell\ge1`$,

```math
F_{\mathcal F}(\tau)\le
\min\left\{1,\left(\sqrt{f_\ell}
+\sqrt{\ell\varepsilon p^{-k\ell}}\right)^2\right\}.
```

Exact marginal return allows repeated use. The individual accuracy guarantees then bound the joint failure probability. Replacing every fresh input by its free component gives a comparison experiment whose only initial resource is the catalyst. These steps turn output accuracy into a lower bound on retained catalyst magic.

If $`f_\ell\le2^{-a\ell}`$, $`a>0`$, and $`b=\log_2(1/p)`$, then

```math
G_{\mathcal F}(\tau):=-\log_2F_{\mathcal F}(\tau)
\ge\frac{a}{a+kb}
\left[\log_2(1/\varepsilon)-\log_2\log_2(1/\varepsilon)\right]-O(1).
```

For T and CCZ, respectively, $`f_\ell=(\cos^2(\pi/8))^\ell`$ and $`f_\ell=(9/16)^\ell`$. Relative entropy of magic inherits this bound. A direct operator comparison gives a stronger coefficient for max-relative-entropy magic and retained qubits. No leading coefficient is claimed optimal.

## Read the science

Start with the [model and exact claims](science/model.md), then follow the converse, its resource consequences and the matching construction.

| To inspect | Read |
|---|---|
| Operational assumptions, accuracy and resource conventions | [Factory model](science/model.md) |
| Exact reuse, the free-input comparison and the full finite-error proof | [Reuse converse](science/reuse_converse.md) |
| Error floors, logarithmic bounds and preparation cost | [Resource costs](science/resource_costs.md) |
| T/CCZ overlaps, arbitrary-catalyst multiplicativity and an explicit example without a Rényi gap | [Magic targets](science/magic_targets.md) |
| Deterministic CCZ batch distillation, cyclic catalyst and complete retained-register accounting | [Cyclic construction](science/cyclic_construction.md) |
| Physical interpretation, correlations and the limits of the model | [Interpretation](science/interpretation.md) |
| Imported results and precise comparisons with earlier converses | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Finite overlap reconstruction and its limits | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to the authoritative scientific files and records the distinctions that an explanation must preserve.

## Relation to existing results

Earlier work already proves logarithmic catalyst-resource divergence under an input-target resource-gap condition. The converse here reaches fixed-input regimes where that condition fails. An explicit noisy-T example excludes every Rényi index allowed by the compared theorem; it separates hypotheses without asserting the achievability of that particular factory.

Exact marginal reuse and the cyclic construction are due to Fang and Liu. The CCZ upper bound uses the constant-rate batch construction of Wills, Hsieh and Yamasaki. Stabilizer-overlap results and ordinary-purification comparisons are also established inputs. Their roles and source editions are specified in the related-work account.

## Learn the project

The single educational anchor is **Eric Chitambar and Gilad Gour, *Quantum Resource Theories* (2019)**. The [Chitambar–Gour bridge](learning/CHITAMBAR_GOUR_BRIDGE.md) gives a selective section guide, translates fidelity and resource-measure conventions, and develops the steps connecting the review's framework to this project's results. Its worked examples explain correlated-output accuracy and exact return in a two-phase catalyst cycle.

The [30-milestone map](learning/MILESTONES.md) defines a common route through the project. Its **12 background/preliminaries milestones** build the complete factory model from states, operations, accuracy and resource measures. Its **18 narrative/innovation milestones** connect the converse, its precise novelty, the attainable CCZ construction and the resulting resource interpretation. Each milestone records an understanding target, earlier dependencies, a conceptual connection and source pointers.

Use the bridge alongside the map for self-directed study. The scientific pages remain the authoritative route to complete proofs and their primary research dependencies. The [LLM reading guide](llms.txt) connects both routes without assuming a particular reader's background.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/check_targets.py
```

The script uses only Python's standard library. Exact binary linear algebra enumerates all pure stabilizer projectors on one, two and three qubits; numerical overlaps reproduce the T, T tensor T and CCZ constants. The [committed output](verification/expected_targets.json) records the results. General converses, tensor-power statements and asymptotic scaling rely on the written proofs and cited theorems.

## Scope

The model is deterministic and requires exact catalyst marginal return. The asymptotic lower bounds fix the noisy source and the number of fresh inputs per round. The upper construction establishes retained-memory and retained-magic scaling, with explicit source-only initialization. It does not optimize gate count, transient workspace, thresholds or the constant input budget. Heralded protocols, approximate catalyst return and sources with zero free weight require separate arguments.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
