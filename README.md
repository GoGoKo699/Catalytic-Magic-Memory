# Catalytic Magic Memory

A reusable magic-state factory can consume a constant number of fresh noisy inputs per output. Improving its accuracy still requires a growing stock of magic in persistent quantum memory. This project proves a logarithmic lower bound on that stored resource and derives matching CCZ memory scaling from established distillation constructions.

For a fixed sufficiently low, nonzero noise level and a sufficiently large fixed input budget, the minimum quantum catalyst width satisfies

```math
q_{\min}(\epsilon)=\Theta\!\left(\log\frac{1}{\epsilon}\right).
```

Here $`\epsilon`$ is state infidelity. The factory is deterministic, uses ideal stabilizer operations, and returns its catalyst marginal exactly. Outputs may be correlated with the catalyst and with one another. All persistent quantum memory and correlated control are counted; an arbitrary amount of free classical storage is allowed.

## Principal results

| Result | Scope | Scientific account |
|---|---|---|
| Finite-error lower bound on stored magic | Any fresh block with a positive free-state component; arbitrary mixed catalyst | [Converse](science/converse.md) |
| Logarithmic quantum-memory necessity | Every fixed finite noisy-input budget; computational $`T`$ and CCZ targets | [Model](science/model.md) and [converse](science/converse.md) |
| Nonzero error floor for finite stored magic | Explicit inequality, with no input–target resource ordering assumption | [Converse](science/converse.md) |
| Matching logarithmic CCZ memory | Fixed below-threshold depolarized source and a sufficient constant input budget | [Construction](science/construction.md) |
| Quantum memory cannot be replaced by classical flags | Classical–quantum catalysts with unrestricted finite classical storage | [Model](science/model.md) |
| Startup and ongoing costs | No perfect magic seed; initialization and persistent memory charged separately | [Resources](science/resources.md) |

The lower bound is the contribution developed here. The upper construction combines [Wills–Hsieh–Yamasaki batch distillation](references/related-work.md#why2025) with [Fang–Liu catalytic conversion](references/related-work.md#fl2026). The target-overlap identities are due to [Bravyi and collaborators](references/related-work.md#b2019).

## Why repetition reveals the memory cost

Let the fresh input satisfy $`\chi\ge w\sigma_0`$, where $`\sigma_0`$ is free and $`w>0`$. After $`L`$ nominal reuses, the joint output has infidelity at most $`L\epsilon`$ to the product target, even when its components are correlated.

The same circuit with all fresh inputs replaced by $`\sigma_0`$ has weight $`w^L`$ in a positive decomposition of the nominal experiment. Its joint error is therefore at most $`\delta_L=L\epsilon/w^L`$. In that experiment the initial catalyst is the only source of magic. A binary target test and relative-entropy monotonicity give

```math
E_R(\tau)\ge
(1-\delta_L)L\log_2(1/f)-h_2(\delta_L),
\qquad \delta_L\le\tfrac12,
```

where $`F_{\mathrm{STAB}}(\psi^{\otimes L})=f^L`$. Choosing $`L`$ proportional to $`\log(1/\epsilon)`$ gives the lower bound. The proof uses the tensor powers of the target, without assuming additivity involving an arbitrary catalyst.

The [closest-work comparison](references/related-work.md) explains the distinction from earlier correlated-catalysis bounds: no assumption that the fresh input contains less resource than the target is required.

## Read the science

Start with the [scientific route](science/README.md), then follow the [model](science/model.md), [converse proof](science/converse.md), [attaining construction](science/construction.md), and [resource interpretation](science/resources.md). The [related-work account](references/related-work.md) identifies inherited ingredients, exact theorem pointers, and the limits of the literature comparison. Machine-readable citations are in the [bibliography](references/references.bib).

The [LLM reading guide](llms.txt) maps questions to authoritative files.

## Learn the project

The [30-milestone understanding map](learning/MILESTONES.md) moves from 13 background/preliminaries milestones to 17 narrative/innovation milestones. Each phase connects local ideas into the complete model or result, with prerequisites and direct scientific source pointers.

The single educational anchor is John Watrous's *The Theory of Quantum Information*. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies focused readings, translates fidelity and trace-distance conventions, and develops a two-phase catalyst example before connecting the textbook tools to the converse and construction.

## Reproduce the finite checks

From the repository root, with Python 3.10 or newer:

```bash
python3 verification/run_all.py
```

The standard-library checks enumerate all 1,080 three-qubit stabilizer projectors, verify correlated catalyst marginal identities with exact rational matrices, reproduce the resource-gap example, and check explicit code-family parameters. See [verification and expected outputs](verification/README.md) for what each calculation establishes. The general theorem and all-accuracy scaling are analytical results.

## Physical scope

The sharp scaling concerns persistent logical quantum memory. One explicit sufficient construction uses 1,680 noisy CCZ inputs per output, with a conservative source-infidelity threshold about $`2.23\times10^{-5}`$. Its first displayed code-family member gives a padded catalyst of 206,035,200 logical qubits. These constants establish attainability of the scaling; they are not a practical factory recommendation.

[Resource accounting](science/resources.md) keeps preparation, classical storage, transient workspace, and periodically executed batch circuits explicit. The claim does not optimize physical fault-tolerant qubits, circuit depth or elapsed time. Exact nominal catalyst return and deterministic processing are the operational assumptions; return only on heralded success needs a different analysis.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
