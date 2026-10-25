# From quantum resource theory to catalytic magic cost

A magic-state factory turns noisy resource states into accurate inputs for quantum computation. A catalyst offers a way to reduce the number of fresh states consumed during each use: the factory retains an auxiliary state and returns it unchanged on its marginal. This raises a separate question about precision. How much magic and memory must the retained state contain when the desired output error becomes smaller?

The distinction is between a resource that survives one use and a resource whose required size stays bounded across increasingly demanding uses. The project studies the second question while allowing correlations between the catalyst and its outputs. Its [factory model](../science/model.md) states the assumptions; the [milestone map](MILESTONES.md) organizes the concepts and the subsequent argument.

## The selected anchor and reading route

The educational anchor is Eric Chitambar and Gilad Gour, [*Quantum Resource Theories*](https://doi.org/10.1103/RevModPhys.91.025001), Reviews of Modern Physics **91**, 025001 (2019). Page references here use the [arXiv v3 PDF](https://arxiv.org/pdf/1806.06107v3), revised 20 April 2019. They are its printed pages, not the journal's pagination. The [HTML rendering](https://arxiv.org/html/1806.06107v3) numbers subsections that the PDF labels with letters: III.A becomes III.1, for example.

Sections 1–2 establish the model and conventions, Sections 3–6 develop the converse, and Sections 7–9 connect the construction to its optimal order and scope. The selective anchor route is:

| Background | Anchor locations | Corresponding milestones |
|---|---|---|
| States, channels and accuracy | II, pp. 4–6; fidelity on p. 5 | [M01](MILESTONES.md#m01), [M02](MILESTONES.md#m02), [M05](MILESTONES.md#m05) |
| Free operations and stabilizer control | III.A, pp. 7–9; III.C.1, pp. 10–11; IV.A.5, pp. 27–28 | [M03](MILESTONES.md#m03), [M04](MILESTONES.md#m04) |
| Resource measures and comparison geometry | III.D.1, pp. 13–14; VI.B–VI.D, pp. 41–44; VI.E.2, pp. 46–47 | [M06](MILESTONES.md#m06), [M07](MILESTONES.md#m07), [M08](MILESTONES.md#m08), [M09](MILESTONES.md#m09) |
| Catalysis and the complete accounting question | V.C, p. 37; VI.A, pp. 39–41 | [M10](MILESTONES.md#m10), [M11](MILESTONES.md#m11), [M12](MILESTONES.md#m12) |

The review supplies the framework and measure definitions. The source free-component method, target-overlap identities and later catalytic constructions have their own [research dependencies](../references/RELATED_WORK.md). They are not results attributed to the 2019 review.

## 1. Translate the conventions

The review's fidelity is the root convention. The project uses its square:

```math
F_{\mathrm{CG}}(\rho,\sigma)
=\|\sqrt{\rho}\sqrt{\sigma}\|_1,
\qquad
F(\rho,\sigma)=F_{\mathrm{CG}}(\rho,\sigma)^2.
```

All project logarithms are base two. For a pure target projector $`\psi=|\psi\rangle\langle\psi|`$, squared fidelity equals the target-test success probability. Thus the output error is

```math
\varepsilon=1-F(\psi,\omega_B)
=1-\mathrm{Tr}(\psi\omega_B).
```

A root-fidelity guarantee $`F_{\mathrm{CG}}\ge1-\eta`$ implies $`\varepsilon\le2\eta-\eta^2`$. It does not imply the same numerical infidelity bound $`\varepsilon\le\eta`$. Half trace distance at most $`\epsilon_{\mathrm{tr}}`$ from a pure target implies $`\varepsilon\le\epsilon_{\mathrm{tr}}`$. Purified distance, defined here as $`P=\sqrt{1-F}`$, at most $`\epsilon_{\mathrm P}`$ implies $`\varepsilon\le\epsilon_{\mathrm P}^2`$.

For a free-state set $`\mathcal F`$, define

```math
F_{\mathcal F}(x)=\max_{\sigma\in\mathcal F}F(x,\sigma),
\qquad
G_{\mathcal F}(x)=-\log_2F_{\mathcal F}(x).
```

The measure dictionary, using the review's equation numbers, is:

| Project quantity | Review notation and relation |
|---|---|
| Maximum free fidelity $`F_{\mathcal F}`$ | $`1-R_G`$, Eqs. (88)–(90) |
| Logarithmic free fidelity $`G_{\mathcal F}`$ | $`\widetilde R_{1/2}`$, Eqs. (80), (89) |
| Relative entropy $`E_{\mathcal F}(x)=\min_{\sigma\in\mathcal F}D(x\Vert\sigma)`$ | $`R_{\mathrm{rel}}`$, Eq. (83) |
| Max-relative entropy $`M_{\mathcal F}(x)=\min_{\sigma\in\mathcal F}D_{\max}(x\Vert\sigma)`$ | $`R_{\max}`$, Eq. (81) |
| Multiplicative generalized robustness $`\Lambda^+(x)=\min\{\lambda:x\le\lambda\sigma,\ \sigma\in\mathcal F\}`$ | $`1+R_{\mathrm{rob}}`$, Eqs. (101)–(102) |

In particular, $`M_{\mathcal F}=\log_2\Lambda^+`$. The review's geometric quantity $`R_G`$ and the project's $`G_{\mathcal F}`$ are related but unequal. Their distinction matters when discussing a resource that diverges.

A free channel can increase closeness to the free set, so $`F_{\mathcal F}(\Phi(x))\ge F_{\mathcal F}(x)`$. Its logarithmic resource therefore satisfies the opposite inequality. This follows from fidelity data processing and the fact that the image of a free comparison state remains free. It does not assert additivity. The [resource-cost account](../science/resource_costs.md) also uses

```math
M_{\mathcal F}(x)\ge E_{\mathcal F}(x)\ge G_{\mathcal F}(x).
```

For a $`q`$-qubit magic catalyst, the free comparator $`I/2^q`$ gives $`M_{\mathrm{STAB}}(x)\le q`$. This connects resource measures to memory size without identifying them with one another.

## 2. The factory and its three costs

In the stabilizer setting, free states form the convex hull of pure stabilizer states. Free control includes Clifford unitaries, stabilizer preparation, Pauli measurement, classical feed-forward and discarding. Nonstabilizer inputs supply magic for operations beyond this control. The converse assumes deterministic free channels closed under composition, identity extension, free-state appending and discarding. These conditions allow an operation to act inside a larger system containing earlier outputs.

Fix a noisy source $`\rho`$ with a normalized free comparison state $`\gamma`$ and positive weight:

```math
\rho\ge p\gamma,\qquad 0<p\le1.
```

The weight need not be optimal. If $`\rho`$ has full rank in dimension $`d`$ and $`I/d`$ is free, then $`\gamma=I/d`$ and $`p=d\lambda_{\min}(\rho)`$ suffice. This source property enters through the [free-component purification method](../references/RELATED_WORK.md#fangliu2022).

A round supplies $`k`$ independent source copies to a channel acting with the catalyst:

```math
\mathcal E:S^{\otimes k}C\longrightarrow BC,
\qquad
\omega_{BC}=\mathcal E(\rho^{\otimes k}\otimes\tau),
```

```math
\mathrm{Tr}_B\omega_{BC}=\tau,
\qquad
1-\mathrm{Tr}(\psi\omega_B)\le\varepsilon.
```

The catalyst $`\tau`$ may be mixed and internally entangled. Exact marginal return does not impose $`\omega_{BC}=\omega_B\otimes\tau`$. The review's product-return definition in V.C is therefore introductory context for a different return condition. The project's [reuse principle](../science/reuse_converse.md), attributed to [Fang and Liu](../references/RELATED_WORK.md#fangliu2026), permits correlations while preserving the unconditional output guarantee. Conditioning on earlier outcomes is a separate operation and need not preserve that guarantee.

Every round receives fresh inputs independent of the existing history. All reusable nonfree memory belongs to $`C`$. As $`\varepsilon`$ decreases, the channel and finite-dimensional catalyst may change; the source, pure target and integer $`k`$ remain fixed.

| Cost | Quantity counted | Role in the precision limit |
|---|---|---|
| Ongoing input consumption | $`k`$ noisy source copies per round | Held fixed |
| Retained catalyst | $`G_{\mathrm{STAB}}(\tau)`$, $`E_{\mathrm{STAB}}(\tau)`$, $`M_{\mathrm{STAB}}(\tau)`$ and $`q`$ retained qubits | May grow with required accuracy; includes persistent classical flags |
| Source-only initialization | $`N_{\mathrm{init}}`$ copies of the same source used in deterministic free preparation | Counts the initial preparation separately from subsequent uses |

This [three-cost accounting](../science/interpretation.md#three-costs) separates retained memory from temporary workspace and gate count. A catalyst chosen for one accuracy can retain its marginal across repeated uses; the precision question concerns the resource required across a family of increasingly accurate factories. The later converse and [CCZ construction](../science/cyclic_construction.md) address the necessary and achievable costs of that family.

## 3. Reuse with correlated outputs

This section develops [M13–M14](MILESTONES.md#m13). Suppose the catalyst has marginal $`\tau`$ after a round. A fresh independent input block then gives the next local channel exactly the same reduced input, $`\rho^{\otimes k}\otimes\tau`$. The next output has the same accuracy and the catalyst marginal is again $`\tau`$. A trace-preserving operation on those registers leaves all earlier output marginals unchanged. Induction therefore supplies the same unconditional accuracy on every use. The [full argument and Fang–Liu attribution](../science/reuse_converse.md#1-repetition-preserves-the-marginal-promise) retain the correlations throughout.

A small example shows why marginal accuracy does not determine joint accuracy. Let $`\varphi`$ be a pure projector orthogonal to the target $`\psi`$. Compare the two legitimate joint states

```math
\begin{aligned}
\beta_{\mathrm{corr}}
&=(1-\varepsilon)\psi\otimes\psi
+\varepsilon\varphi\otimes\varphi,\\
\beta_{\mathrm{ind}}
&=[(1-\varepsilon)\psi+\varepsilon\varphi]^{\otimes2}.
\end{aligned}
```

Both have the same one-output marginal and marginal infidelity $`\varepsilon`$. Their joint infidelities with $`\psi\otimes\psi`$ are, respectively, $`\varepsilon`$ and $`2\varepsilon-\varepsilon^2`$. These states illustrate probability accounting; this example does not construct a catalytic factory.

The converse needs an upper estimate that holds for either correlation pattern. Set $`\Pi_\ell=\psi^{\otimes\ell}`$. Target projectors on different output registers commute, so

```math
I-\Pi_\ell
\le\sum_{j=1}^{\ell}(I-\psi_j)\otimes I_{\ne j}.
```

Taking the expectation in the actual joint output $`\Omega_\ell`$ gives

```math
\mathrm{Tr}[(I-\Pi_\ell)\Omega_\ell]\le\ell\varepsilon.
```

The estimate bounds the probability that at least one target test fails. It is sufficient for the proof, and does not imply that every correlated stream needs per-output error $`\delta/\ell`$ to have joint error $`\delta`$. Conditioning on outcomes from earlier rounds is another operation: it can change the conditional catalyst state. The guarantee here concerns unconditional marginals.

## 4. Build the catalyst-only comparison

The steps in [M15–M17](MILESTONES.md#m15) use the review's channel and monotonicity framework to establish the project's finite theorem. Read this section alongside the authoritative [reuse converse](../science/reuse_converse.md).

### Transport the free component through the entire protocol

Let $`\Lambda_\ell`$ be the channel that runs all $`\ell`$ rounds and discards the final catalyst. Its actual input contains $`k\ell`$ fresh source copies. Define a comparison output by replacing those copies with their normalized free component:

```math
\begin{aligned}
\Omega_\ell&=\Lambda_\ell(\rho^{\otimes k\ell}\otimes\tau),\\
\Xi_\ell&=\Lambda_\ell(\gamma^{\otimes k\ell}\otimes\tau).
\end{aligned}
```

Both outputs are normalized. The assumption $`\rho\ge p\gamma`$ implies $`\rho^{\otimes k\ell}\ge p^{k\ell}\gamma^{\otimes k\ell}`$. Complete positivity preserves the inequality, yielding

```math
\Omega_\ell\ge p^{k\ell}\Xi_\ell,
\qquad
\mathrm{Tr}[(I-\Pi_\ell)\Xi_\ell]
\le\delta_\ell:=\ell\varepsilon p^{-k\ell}.
```

The exponent counts every fresh source copy. There is no flag revealing which component was supplied and no postselection on a free-input event. This is an operator comparison. The catalyst need not return in the comparison experiment: its exact return was used only to establish the actual experiment's repeated marginal guarantees. The positive-free-component method has the separately stated [purification provenance](../references/RELATED_WORK.md#fangliu2022).

### Apply resource monotonicity with the correct direction

Fixing all other inputs to free states gives a free channel on the catalyst alone,

```math
\Phi_\ell(x)=\Lambda_\ell(\gamma^{\otimes k\ell}\otimes x),
\qquad
\Phi_\ell(\tau)=\Xi_\ell.
```

The closure under free-state preparation, identity extension, composition and discard is used here. For a free comparison state $`\sigma_C`$, the output $`\Phi_\ell(\sigma_C)`$ is free. Fidelity data processing, followed by optimization over free states, gives

```math
F_{\mathcal F}(\tau)\le F_{\mathcal F}(\Xi_\ell).
```

Maximum free fidelity can increase during free processing because the state can move closer to the free set. Its negative logarithm decreases. Keeping this direction explicit prevents reversing the catalyst bound.

### Turn the target test into a fidelity inequality

For an arbitrary free output state $`\sigma`$, write

```math
t=\mathrm{Tr}(\Pi_\ell\Xi_\ell),
\qquad
s=\mathrm{Tr}(\Pi_\ell\sigma).
```

The comparison gives $`1-t\le\delta_\ell`$, and the definition of the target benchmark gives $`s\le f_\ell`$. Measuring $`\{\Pi_\ell,I-\Pi_\ell\}`$ turns the two states into binary distributions. Fidelity data processing then yields

```math
\begin{aligned}
F(\Xi_\ell,\sigma)
&\le\left(\sqrt{ts}+\sqrt{(1-t)(1-s)}\right)^2\\
&\le\left(\sqrt{f_\ell}+\sqrt{\delta_\ell}\right)^2.
\end{aligned}
```

This test is a mathematical means of bounding ordinary fidelity. The factory is not required to implement it as a free measurement. Maximizing over $`\sigma`$ and combining the inequalities proves

```math
\boxed{
F_{\mathcal F}(\tau)\le
\min\left\{1,
\left(\sqrt{f_\ell}+\sqrt{\ell\varepsilon p^{-k\ell}}\right)^2
\right\}
\quad(\ell\ge1).
}
```

The only resource input to $`\Phi_\ell`$ is $`\tau`$. This is why the argument can constrain the catalyst even when the full noisy input batch contains more resource than one target. No additive catalyst term has to cancel from a one-round conversion inequality.

## 5. Read the accuracy cost

[M18–M20](MILESTONES.md#m18) translate the finite theorem into costs. The [resource-cost page](../science/resource_costs.md) contains the exact constants and their ranges of validity.

If the retained fidelity resource is bounded by $`G_{\mathcal F}(\tau)\le g`$, then $`F_{\mathcal F}(\tau)\ge2^{-g}`$. Rearranging the theorem gives

```math
\varepsilon\ge
\sup_{\ell\ge1}\frac{p^{k\ell}}{\ell}
\left(2^{-g/2}-\sqrt{f_\ell}\right)_+^2,
\qquad (x)_+=\max\{x,0\}.
```

If $`f_\ell\to0`$, choose a finite $`\ell`$ for which $`f_\ell<2^{-g}`$. The right side is then positive. Thus a bounded retained resource gives an accuracy floor even without a uniform bound on catalyst dimension.

For T and CCZ, the established tensor-power overlaps have the form $`f_\ell=2^{-a\ell}`$ with $`a>0`$. Let

```math
L=\log_2(1/\varepsilon),
\qquad b=\log_2(1/p),
\qquad A=a+kb.
```

Increasing $`\ell`$ makes the target harder to imitate freely, through $`2^{-a\ell}`$. It also enlarges the comparison-error allowance, through $`\ell\varepsilon 2^{kb\ell}`$. Their ratio is

```math
\frac{\ell\varepsilon p^{-k\ell}}{2^{-a\ell}}
=\ell\,2^{-L+A\ell}.
```

For sufficiently large $`L`$, the integer choice $`\ell=\lfloor(L-\log_2L)/A\rfloor\ge1`$ keeps this ratio at most $`1/A`$. Consequently,

```math
G_{\mathcal F}(\tau)
\ge\frac{a}{a+kb}(L-\log_2L)-O(1).
```

The logarithmic correction pays for the factor $`\ell`$ in the accumulated error. The leading coefficient stays positive for every fixed $`p>0`$ and fixed $`k`$. Changing either with the requested accuracy requires returning to the finite inequality.

### Translate the bound into distinct physical costs

For a $`q`$-qubit magic catalyst, the free state $`I/2^q`$ supplies

```math
q\ge M_{\mathrm{STAB}}(\tau)
\ge E_{\mathrm{STAB}}(\tau)
\ge G_{\mathrm{STAB}}(\tau).
```

In particular, $`\tau\le I=2^q(I/2^q)`$ proves the first inequality. The remaining order follows from the quantum-divergence definitions. Every quantity in this display inherits the fidelity-resource lower bound.

A direct argument gives a stronger coefficient for $`M`$ and $`q`$. If $`\tau\le2^m\sigma_C`$ with free $`\sigma_C`$, then

```math
\Xi_\ell\le2^m\Phi_\ell(\sigma_C),
\qquad
\mathrm{Tr}(\Pi_\ell\Xi_\ell)\le2^m f_\ell.
```

Optimizing $`m`$ gives $`M_{\mathcal F}(\tau)\ge-\log_2f_\ell+\log_2(1-\delta_\ell)`$ when $`\delta_\ell<1`$ and $`M_{\mathcal F}(\tau)`$ is finite. Finite-qubit magic catalysts satisfy this finiteness condition. Choosing $`\ell`$ just below $`L/(kb)`$ gives coefficient $`a/(kb)`$ for $`M`$ and retained qubits when $`kb>0`$. The proved relative-entropy coefficient remains $`a/(a+kb)`$: a lower bound on $`M`$ alone cannot be transferred to the smaller quantity $`E`$. Neither coefficient is claimed optimal; when $`p=1`$, use the finite formulas.

## 6. Understand the absence of a resource gap

[M21](MILESTONES.md#m21) concerns the theorem's reach. The [related-work comparison](../references/RELATED_WORK.md#rubboli2022) credits the earlier logarithmic catalyst-resource bound and states its hypotheses precisely. That theorem requires a strict input-target gap for some allowed sandwiched Rényi index. The [magic-target account](../science/magic_targets.md#absence-of-every-renyi-gap-in-the-earlier-converse) supplies a concrete separation.

For the source $`\rho_\nu=(1-\nu)\psi_T+\nu I_2/2`$ with $`\nu=0.01`$, the relevant quantities are

| Quantity | Value |
|---|---:|
| Single-source fidelity resource $`G_{\mathrm{STAB}}(\rho_\nu)`$ | $`0.1521751049\ldots`$ |
| Two-source fidelity resource $`G_{\mathrm{STAB}}(\rho_\nu^{\otimes2})`$ | $`0.3043502099\ldots`$ |
| Target resource $`a=-\log_2\cos^2(\pi/8)`$ | $`0.2284466968\ldots`$ |

Mixed-qubit fidelity multiplicativity gives the second line. For every $`\alpha\in[1/2,1)`$ allowed by the compared theorem, the minimized sandwiched Rényi resource of the T target equals $`a`$, while that of the two-source batch is at least its fidelity resource. Thus none of these indices gives a strict input-resource deficit.

The source still has positive optimal free weight $`p_*=\nu/(1-1/\sqrt2)`$. Substituting it into the new converse at $`k=2`$ gives a positive leading fidelity-resource coefficient, approximately $`0.0229064`$.

This calculation separates theorem hypotheses. It does not establish arbitrarily accurate distillation from that particular two-input source. Also, pure T and CCZ targets are strongly fidelity-multiplicative even against an arbitrary mixed catalyst, as proved in the [dedicated account](../science/magic_targets.md#strong-multiplicativity-for-a-small-pure-target). The converse's reach comes from isolating the catalyst in a repeated comparison experiment. The matching construction below concerns a sufficiently large fixed CCZ input budget.

## 7. See the cyclic construction in two phases

The converse becomes more informative when a construction reaches the same order. First consider an abstract batch operation on equal-sized padded blocks. Let $`\zeta`$ be one raw block and suppose a deterministic free channel satisfies

```math
\Gamma(\zeta\otimes\zeta)=\eta_{12},
\qquad
\eta_1=\mathrm{Tr}_2\eta_{12},
\qquad
\eta_2=\mathrm{Tr}_1\eta_{12}.
```

The two output blocks occupy the same spaces as the raw blocks, using free padding where necessary. The state $`\eta_{12}`$ is the actual noisy batch output and may be correlated. This is an assumed batch primitive for illustrating the cycle. A raw block can contain many physical source copies, so the example does not establish distillation from two noisy magic states or the feasibility of a particular two-input factory.

Store one block and a classical flag in the state

```math
\tau=
\frac12\eta_1\otimes|0\rangle\langle0|
+\frac12\zeta\otimes|1\rangle\langle1|.
```

Each use receives one independent fresh block $`\zeta`$. The flag specifies which operation to perform:

| Flag before use | Stored block | Action | Retained block and flag |
|---|---|---|---|
| 0 | $`\eta_1`$ | Emit the stored block and retain the fresh raw block | $`\zeta`$, flag 1 |
| 1 | $`\zeta`$ | Apply $`\Gamma`$ to the stored and fresh raw blocks; emit output register 2 | Output register 1 with marginal $`\eta_1`$, flag 0 |

In the second row, keeping register 1 and emitting register 2 preserves whatever correlations the batch produced between them. No replacement of the joint batch state by $`\eta_1\otimes\eta_2`$ is made.

Let $`B`$ denote the emitted block and $`C`$ the complete retained system, including the flag. Tracing out the emitted block gives

```math
\omega_C=
\frac12\zeta\otimes|1\rangle\langle1|
+\frac12\eta_1\otimes|0\rangle\langle0|
=\tau.
```

Thus the full catalyst marginal returns exactly. The output marginal is

```math
\omega_B=\frac12(\eta_1+\eta_2).
```

For a pure padded-block target $`\psi_{\mathrm{pad}}`$, a global batch guarantee $`\mathrm{Tr}[(\psi_{\mathrm{pad}}\otimes\psi_{\mathrm{pad}})\eta_{12}]\ge1-\varepsilon`$ implies $`\mathrm{Tr}(\psi_{\mathrm{pad}}\eta_a)\ge1-\varepsilon`$ for both marginals. Their average has the same accuracy guarantee. Free padding can then be discarded. Exact return and independent fresh inputs preserve this unconditional guarantee on reuse, even when earlier outputs remain correlated with the memory.

For general $`m`$, the catalyst stores $`m-1`$ blocks and a uniform phase label. Phase $`r`$ contains $`r`$ raw blocks and a prefix marginal of the actual batch output on $`m-1-r`$ blocks. An ordinary step emits the last stored output and inserts the fresh raw block. Once all stored blocks are raw, the new block completes an $`m`$-block batch; the protocol refreshes the memory and resets the phase. These operations cycle the conditional catalyst states with unchanged weights. Each batch marginal is emitted in one phase.

This is the later [Fang–Liu construction](../references/RELATED_WORK.md#fangliu2026), beyond the anchor's introductory catalytic framework. The [canonical construction, Sections 3–4](../science/cyclic_construction.md), gives the general state and return proof. Taking $`m`$ to be a power of two makes the uniform flag exactly preparable from fair measurement bits. Measuring the classical flag and preparing its updated label requires no coherent non-Clifford counter.

## 8. Connect the CCZ family to the optimal order

The actual construction fixes the source

```math
\rho_\nu=(1-\nu)\Psi_{\mathrm{CCZ}}+\nu I_8/8,
\qquad 0<\nu<\nu_*.
```

Here $`\nu_*`$ is a sufficient positive threshold and $`\nu`$ remains fixed as accuracy improves. The source has a valid free weight $`p=\nu`$. Its stochastic error probability in the batch analysis is instead $`s=7\nu/8`$: the maximally mixed contribution is uniform over the eight orthogonal states $`Z^z|\mathrm{CCZ}\rangle`$, one of which is the desired state. These two parameters serve different arguments.

The imported [Wills–Hsieh–Yamasaki protocol](../references/RELATED_WORK.md#wills2025) supplies deterministic batches with exponentially small global infidelity. Its CCZ conversion consumes $`N=Cn`$ source copies for $`n`$ physical qudits, with one explicit decomposition giving $`C=70`$. The code family has output count $`r=\Theta(n)`$ and error at most $`e^{-cn}`$ for sufficiently small fixed source noise and some fixed $`c>0`$. All decoder outcomes produce outputs; no success-conditioned normalization is used.

The explicit code lengths have bounded successive ratios. Therefore, choosing the first available length above the required logarithmic scale gives $`n=O(\log(1/\varepsilon))`$ at every sufficiently small requested error. A sparse unbounded sequence alone would not justify that conclusion.

Retain $`m=2^{\lfloor\log_2r\rfloor}`$ outputs. The established bound $`n/r\le24`$ then gives $`N/m<48C`$. One sufficient fixed per-round budget is consequently $`K=48C=3360`$. Discarding surplus supplied inputs and adding free padding realizes the uniform block spaces used by the cycle. Every supplied copy is counted. Any larger fixed budget also works by discarding the excess; smaller budgets are not settled by this construction.

With raw block $`\zeta=\rho_\nu^{\otimes K}`$, the full retained qubit count is

```math
q=3K(m-1)+\log_2m
=O(\log(1/\varepsilon)).
```

The classical flag is included. The free maximally mixed comparator bounds each stored measure $`G`$, $`E`$, and $`M`$ by $`q`$. Conversely, $`p=\nu>0`$ and $`f_\ell=(9/16)^\ell`$ give logarithmic lower bounds. Taking separate infima over admissible factories therefore yields $`\Theta(\log(1/\varepsilon))`$ for each stated retained cost in this fixed-source, sufficiently-large-fixed-budget regime. The leading constants need not match. [Construction Sections 1–5](../science/cyclic_construction.md) and [resource costs](../science/resource_costs.md#matching-orders-for-sufficiently-low-noise-ccz) provide the detailed bounds.

Initialization uses the actual noisy batch output and additional raw blocks, with a fixed budget at most $`N+K(m-1)=O(\log(1/\varepsilon))`$. It requires no perfect magic seed. The matching startup lower order has a separate provenance: composing a preparation using $`J`$ source copies with the first $`k`$-input use gives the ordinary-purification bound $`\varepsilon\ge\nu^{J+k}(7/16)`$. Exact catalyst return is unnecessary for that startup argument. The new retained-resource conclusion concerns what must remain stored after preparation. See [construction Section 6](../science/cyclic_construction.md#6-exact-preparation-and-optimal-source-only-initialization-order).

## 9. Read the scope of the result

The statements concern deterministic processing and exact catalyst marginal return at one prescribed noisy source. Return on a whole neighborhood of sources is a stronger requirement. Approximate return changes the accumulated-error estimate; heralding changes normalization and resource monotonicity after conditioning. Zero free weight, accuracy-dependent source noise, or a growing fresh-input budget also require their own analysis.

A fixed-accuracy catalyst can be reused indefinitely with its unconditional output guarantee. This does not assert independent outputs, identical performance on every conditioned history, or a fixed total error for an arbitrarily long stream. The union bound supplies a sufficient joint-error estimate, not a necessary allocation law.

The counted memory is retained between uses. Transient decoding workspace, gate count, latency, and device noise are separate costs. Clifford control is ideal in the model, and the sufficient threshold and input budget are unoptimized. These qualifications are collected in the [interpretation](../science/interpretation.md).

The milestone route follows the same structure: [M22–M24](MILESTONES.md#m22) connect batch guarantees to a fixed budget; [M25–M27](MILESTONES.md#m25) establish the cycle and account for its resources; [M28–M30](MILESTONES.md#m28) combine attainability, scope, and significance. The resulting distinction is between constant resource consumption during use and the growing resource that a more accurate reusable factory must retain.
