# Exact reuse forces retained resource

The [model](model.md) fixes a source $`\rho\ge p\gamma`$ with normalized free $`\gamma`$ and $`p>0`$, a fresh-input count $`k`$, and a pure target $`\psi`$. One deterministic free channel returns the catalyst $`\tau`$ exactly on its marginal and has target infidelity at most $`\varepsilon`$. All operations below retain the earlier outputs while acting on a fresh source block and the catalyst.

## Finite-error theorem

For every positive integer $`\ell`$,

```math
\boxed{
F_{\mathcal F}(\tau)\le
\min\left\{1,
\left(\sqrt{f_\ell}+\sqrt{\ell\varepsilon p^{-k\ell}}\right)^2
\right\}.
}
```

Here $`F_{\mathcal F}`$ uses squared fidelity and $`f_\ell`$ is the maximum free overlap with $`\psi^{\otimes\ell}`$. The catalyst can be mixed, entangled across its registers, and correlated with all outputs. The theorem imposes neither target-catalyst additivity nor an input-target resource gap.

### 1. Repetition preserves the marginal promise

After one use the catalyst marginal is $`\tau`$. Suppose it is also $`\tau`$ after $`j`$ uses. The next input block is independent of the existing joint state, so the reduced input to the next channel is $`\rho^{\otimes k}\otimes\tau`$. The new output therefore has the same marginal as the first output, and the catalyst marginal is again $`\tau`$. Earlier output marginals are unchanged by a trace-preserving channel on the other registers.

This proves the induction despite the correlations. It is the marginal-reuse principle in [Fang and Liu, Theorem 4](../references/RELATED_WORK.md#fangliu2026).

Let $`\Omega_\ell`$ be the joint state of the $`\ell`$ outputs after discarding the final catalyst, and set $`\Pi_\ell=\psi^{\otimes\ell}`$. Projectors on distinct output registers commute, giving the operator union bound

```math
I-\Pi_\ell\le
\sum_{j=1}^{\ell}(I-\psi_j)\otimes I_{\ne j}.
```

Every marginal has infidelity at most $`\varepsilon`$, hence

```math
\mathrm{Tr}[(I-\Pi_\ell)\Omega_\ell]\le\ell\varepsilon.
```

No output independence was used.

### 2. Compare with free source inputs

Let $`\Lambda_\ell`$ denote the complete repeated channel, including the final catalyst discard. Define a second experiment using free inputs but the same initial catalyst and the same channel:

```math
\Xi_\ell=
\Lambda_\ell(\gamma^{\otimes k\ell}\otimes\tau).
```

It is normalized because $`\Lambda_\ell`$ is trace preserving. Tensor products preserve the source domination inequality, and complete positivity preserves positive-semidefinite order. Thus

```math
\Omega_\ell
=\Lambda_\ell(\rho^{\otimes k\ell}\otimes\tau)
\ge p^{k\ell}\Xi_\ell.
```

Taking the expectation of $`I-\Pi_\ell`$ gives

```math
\mathrm{Tr}[(I-\Pi_\ell)\Xi_\ell]
\le\delta_\ell,
\qquad
\delta_\ell=\ell\varepsilon p^{-k\ell}.
```

The catalyst need not be returned in this second experiment. Exact return was required only for the actual input $`\rho`$. The comparison is an operator inequality, with no postselection or normalization by an observed success probability.

The positive free-component method is an established purification tool; see [Fang and Liu (2022)](../references/RELATED_WORK.md#fangliu2022). Repetition makes it constrain a state generated from the catalyst alone.

### 3. Use a channel whose only resource input is the catalyst

The map

```math
\Phi_\ell:x\longmapsto
\Lambda_\ell(\gamma^{\otimes k\ell}\otimes x)
```

is free. In particular, it maps every free comparison state on $`C`$ to a free output state. Fidelity data processing therefore gives

```math
F_{\mathcal F}(\tau)\le F_{\mathcal F}(\Xi_\ell).
```

To see the direction explicitly, take a free optimizer $`\sigma_C`$ for $`\tau`$. Then
$`F(\tau,\sigma_C)\le F(\Phi_\ell(\tau),\Phi_\ell(\sigma_C))\le F_{\mathcal F}(\Xi_\ell)`$.

For any free output state $`\sigma`$, apply the binary measurement $`\{\Pi_\ell,I-\Pi_\ell\}`$ to $`\Xi_\ell`$ and $`\sigma`$. Write

```math
t=\mathrm{Tr}(\Pi_\ell\Xi_\ell),
\qquad
s=\mathrm{Tr}(\Pi_\ell\sigma).
```

The previous comparison gives $`1-t\le\delta_\ell`$, while the definition of $`f_\ell`$ gives $`s\le f_\ell`$. Ordinary fidelity data processing implies

```math
\begin{aligned}
F(\Xi_\ell,\sigma)
&\le
\left(\sqrt{ts}+\sqrt{(1-t)(1-s)}\right)^2\\
&\le
\left(\sqrt{f_\ell}+\sqrt{\delta_\ell}\right)^2.
\end{aligned}
```

This analytical binary measurement need not be a free measurement. Maximizing over free $`\sigma`$ proves the theorem; clipping the right side at one uses normalization.

## Why the argument applies beyond a resource gap

A comparison between the resource of $`\rho^{\otimes k}`$ and that of one target can become ineffective when the noisy batch already contains more total magic. The theorem instead uses a long output sequence, a positive free component of each fresh input, and the purity of the target. The resulting comparison channel has $`\tau`$ as its only resource input. It never subtracts an additive catalyst resource from both sides of a one-round conversion.

The exponentially small free-input weight $`p^{k\ell}`$ is a cost in this argument. Optimizing the number of repetitions against the target free overlap yields the [precision laws and error floors](resource_costs.md). The [explicit noisy-T example](magic_targets.md#absence-of-every-renyi-gap-in-the-earlier-converse) shows that the hypotheses can hold while every resource gap available in the earlier converse is absent.
