# Scientific account

The central question is how the accuracy of a continuously reused magic-state factory constrains its stored quantum resource when its fresh-input budget stays fixed.

## Reading route

1. [Model](model.md): free operations, positive source free weights, state infidelity, exact marginal return, and complete memory accounting.
2. [Converse](converse.md): the finite-horizon inequality, correlated reuse, logarithmic stored-magic and width bounds, companion fidelity and max-relative-entropy bounds, and explicit error floors.
3. [Construction](construction.md): exponential batch suppression, the stationary catalytic cycle, and the matching CCZ width.
4. [Resources](resources.md): fixed-input quantifiers, source thresholds, quantum versus classical memory, source-only preparation bounds, and physical interpretation.

For a structured learning route, use the [30-milestone map](../learning/MILESTONES.md) and the [Watrous bridge](../learning/WATROUS_BRIDGE.md). The bridge supplies targeted foundations and notation translations; the pages above remain the complete scientific account.

## The logical structure

The input condition $`\chi\ge w\sigma_0`$ supplies a positive free component. Repeated nominal accuracy transfers to a counterfactual experiment containing only free fresh inputs. Its output can then owe its magic only to the initial catalyst. A binary target test converts the known exponentially small free overlap into a lower bound on relative entropy of magic.

Exact return is an operational certificate that the same nominal accuracy can be used repeatedly. The proof does not require the counterfactual experiment to preserve the catalyst, and it does not treat the outputs as independent.

The upper bound has a different origin. A known constant-rate batch protocol supplies exponentially small global infidelity. A known catalytic conversion stores a mixture of unfinished fresh blocks and completed output prefixes. It turns the batch yield into a constant fresh-input count per emitted state, while the number of stored blocks remains proportional to the batch length.

## What is inherited

The [reference account](../references/related-work.md) gives precise source versions and theorem pointers. Three ingredients are imported:

- Tensor-power stabilizer overlap for the selected target states.
- Deterministic, constant-rate, exponentially accurate CCZ batch distillation.
- The exact marginal-return conversion from batch distillation to a catalytic factory.

The stored-resource converse, its finite-error form, and the matched interpretation are developed in this account. A numerical check of a few sizes does not replace any of those analytical statements.

## How to assess the claim

Read the [converse](converse.md) with its source weight and error convention fixed. Then compare the same source, target, operations and error convention in the [construction](construction.md). The matching statement holds for a sufficient constant input budget; the lower bound itself holds for every fixed finite budget.

Use the [finite verification](../verification/README.md) to inspect the exact overlap, marginal identities and arithmetic examples. Use the [related-work comparison](../references/related-work.md) to distinguish this model from resource-gap bounds, exact product catalysis, robustness to a neighbourhood of inputs, and probabilistic return.
