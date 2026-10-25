# Reusable catalytic magic-state distillation

A catalytic factory can consume a bounded number of noisy magic states per output while its catalyst is returned unchanged on its marginal. The catalyst may nevertheless need more stored magic as the target error decreases. This project quantifies that cost for a fixed noisy source and a fixed fresh-input budget.

The distinction is between resources consumed during a round and resources retained across rounds. Exact marginal return allows the same catalyst to be reused. It does not make its initial resource content or memory size independent of the required precision.

## Free states and operations

Let $`\mathcal F(A)`$ be a nonempty closed set of free states on a finite-dimensional register $`A`$. Free states are closed under tensor products and partial trace. Free deterministic channels are completely positive and trace preserving, preserve free states, and are closed under composition, extension by the identity, appending free states and discarding registers.

For qubit magic, $`\mathcal F(A)=\mathrm{STAB}(A)`$ is the convex hull of pure stabilizer states. Physical stabilizer operations consist of stabilizer-state preparation, Clifford unitaries, Pauli measurements, classical feed-forward and discarding. The converse also applies to larger free-operation classes satisfying the same closure conditions. The explicit construction uses physical stabilizer operations.

Closure under identity extension is part of the model: an earlier output remains present while a later round acts on a fresh source and the catalyst. Merely preserving free states on an isolated register does not supply this property.

## Source, target and one round

Fix a source state $`\rho`$ on $`S`$ and a normalized free state $`\gamma`$ such that

```math
\rho\ge p\gamma,\qquad 0<p\le1.
```

The number $`p`$ is a valid free weight. It need not be optimal. For a full-rank $`d`$-dimensional source with free maximally mixed state, one can take $`\gamma=I/d`$ and $`p=d\lambda_{\min}(\rho)>0`$.

Fix an integer $`k\ge1`$ and a pure target projector $`\psi`$ on $`B`$. A round consists of a free channel

```math
\mathcal E:S^{\otimes k}C\longrightarrow BC
```

and a catalyst $`\tau`$ satisfying

```math
\omega_{BC}=\mathcal E(\rho^{\otimes k}\otimes\tau),
\qquad
\mathrm{Tr}_B\omega_{BC}=\tau,
\qquad
1-\mathrm{Tr}(\psi\omega_B)\le\varepsilon.
```

The catalyst can be mixed and internally entangled. It can become correlated with the current output and earlier outputs. There is no product-output assumption. Every new round receives independent copies of $`\rho`$, initially independent of the existing catalyst and output history. All reusable nonfree memory is included in $`C`$.

For each accuracy $`\varepsilon`$, the channel and catalyst may change. The source $`\rho`$, target $`\psi`$ and fresh-input count $`k`$ remain fixed in the asymptotic statements. The catalyst has finite dimension at each accuracy; no uniform dimension bound is imposed.

## Fidelity and resource conventions

All logarithms are base two. Fidelity is squared Uhlmann fidelity:

```math
F(x,y)=\|\sqrt{x}\sqrt{y}\|_1^2.
```

Define the maximum free fidelity and its logarithm by

```math
F_{\mathcal F}(x)=\max_{\sigma\in\mathcal F}F(x,\sigma),
\qquad
G_{\mathcal F}(x)=-\log_2 F_{\mathcal F}(x).
```

For qubit magic the subscript may be written $`\mathrm{STAB}`$. The free sets here are compact, so the maxima exist. More general theories can use suprema.

The target tensor-power overlap is

```math
f_\ell=\max_{\sigma\in\mathcal F(B^{\otimes\ell})}
\mathrm{Tr}(\psi^{\otimes\ell}\sigma).
```

Because $`\psi`$ is pure, $`f_\ell=F_{\mathcal F}(\psi^{\otimes\ell})`$. The general finite-error theorem uses the actual sequence $`f_\ell`$. Its logarithmic consequences assume $`f_\ell\le2^{-a\ell}`$ for a fixed $`a>0`$. No multiplicativity involving the catalyst is assumed.

The error $`\varepsilon`$ is target infidelity. If half trace distance from the target is at most $`\epsilon_{\mathrm{tr}}`$, then $`\varepsilon\le\epsilon_{\mathrm{tr}}`$. If purified distance is at most $`\epsilon_{\mathrm P}`$, then $`\varepsilon\le\epsilon_{\mathrm P}^2`$. These conversions must be made before comparing numerical coefficients with sources using other conventions.

## Scientific results and reading route

| Statement | Exact scope | Authoritative account |
|---|---|---|
| Finite-error catalyst converse | Every integer repetition count; positive source free weight; arbitrary output correlations | [Reuse and the converse](reuse_converse.md) |
| Stored-resource and memory cost | Fixed source and fixed $`k`$; exponentially decreasing target free overlap | [Resource costs](resource_costs.md) |
| Standard magic targets and absence of a resource gap | T, CCZ, and pure targets on at most three qubits | [Magic targets](magic_targets.md) |
| Matching CCZ scaling | A sufficiently weak fixed depolarization and a sufficiently large fixed input budget | [Cyclic construction](cyclic_construction.md) |
| Physical meaning and boundaries | Retained resource, startup inputs, correlations and exact reuse | [Interpretation](interpretation.md) |

The main finite-error result is

```math
F_{\mathcal F}(\tau)\le
\min\left\{1,\left(\sqrt{f_\ell}
+\sqrt{\ell\varepsilon p^{-k\ell}}\right)^2\right\}
\qquad(\ell\ge1).
```

If $`f_\ell\le2^{-a\ell}`$ and $`b=\log_2(1/p)`$, its consequence is

```math
G_{\mathcal F}(\tau)\ge
\frac{a}{a+kb}\left[
\log_2(1/\varepsilon)-\log_2\log_2(1/\varepsilon)
\right]-O(1).
```

In magic theory this also lower-bounds the relative entropy of magic and the retained catalyst qubit count. A direct comparison gives a stronger coefficient for max-relative-entropy magic and the catalyst qubit count; the relative-entropy coefficient remains the one obtained from the fidelity bound. See the resource-cost page.

For a fixed sufficiently low-noise CCZ source there is a constant $`K_*`$ such that, for every fixed $`k\ge K_*`$, the optimal retained catalyst qubit count has order $`\log(1/\varepsilon)`$. The same order holds for the minimum stored $`G_{\mathrm{STAB}}`$ and relative entropy of magic. The construction establishes an asymptotic existence result. It does not estimate practical hardware thresholds or optimize the constant input overhead.

## Attribution

Marginal reuse and the cyclic catalyst construction are due to Fang and Liu. Positive free-component comparisons are established resource-purification tools. Target stabilizer-overlap identities and the constant-rate CCZ batch construction are also imported results. The added converse combines exact reuse with the free-input comparison to constrain the catalyst even when the whole noisy input batch is more resourceful than one target. The [related-work account](../references/RELATED_WORK.md) identifies these dependencies and the precise distinction from existing catalytic converses.
