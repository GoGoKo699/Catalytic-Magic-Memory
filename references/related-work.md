# Related work and scope of the contribution

The question studied here is the persistent memory required by a deterministic catalytic magic-state factory. A fixed finite number of fresh copies of a noisy source is supplied on every round. The catalyst has exactly the same marginal state after each round, while correlations with the emitted states are permitted. The lower bound charges the catalyst's relative entropy of magic and hence its number of qubits. It does not assume that the fresh input has less magic than the target according to a one-shot Rényi monotone.

For a source with a positive free component, the argument combines exact reuse with a branch in which all fresh inputs are free. The resulting finite-error bound implies logarithmic persistent memory for the target families considered here. In the below-threshold CCZ setting, a matching order of memory follows by combining two existing constructions: constant-rate batch distillation [WHY2025](#why2025) and batch-to-catalyst conversion [FL2026](#fl2026). These constructions, the free-component method, and the stabilizer-overlap identities are prior ingredients.

The comparisons below identify the additional hypotheses of the closest results. They support a specific contribution within this model, rather than an exhaustive claim of priority across all formulations of catalytic resource theory. Bibliographic entries are in [references.bib](references.bib). All logarithms in the comparison calculations are base two, and fidelity is squared Uhlmann fidelity.

## Overlap and additivity ingredients

<a id="b2019"></a>

### [B2019] Bravyi et al.: stabilizer alignment

Sergey Bravyi, Dan Browne, Padraic Calpin, Earl Campbell, David Gosset, and Mark Howard, **Simulation of quantum circuits by low-rank stabilizer decompositions**, *Quantum* **3**, 181 (2019). [DOI](https://doi.org/10.22331/q-2019-09-02-181) · [arXiv:1808.00128v2](https://arxiv.org/abs/1808.00128v2), 27 August 2019.

Section 6.2, Definition 9 and Theorem 5 introduce stabilizer alignment and prove multiplicativity for aligned pure states. Section 6.3, Lemma 11 establishes the relevant bounds on stabilizer-projector overlaps for ranks corresponding to one, two, or three logical qubits; Corollary 3 shows that all pure states on at most three qubits are aligned. These results supply the tensor-power overlap rates for the one-qubit T state and the three-qubit CCZ state.

The required overlaps are

```math
F_{\rm stab}(T)=\cos^2(\pi/8),\qquad
F_{\rm stab}(\mathrm{CCZ})=9/16.
```

Their multiplicativity within the target tensor powers is an existing ingredient. Generic failures of stabilizer-fidelity multiplicativity do not establish an obstruction for these particular small targets. In particular, the project does not claim a new stabilizer-alignment theorem.

<a id="rtt2024"></a>

### [RTT2024] Rubboli, Takagi, and Tomamichel: mixed-state additivity

Roberto Rubboli, Ryuji Takagi, and Marco Tomamichel, **Mixed-state additivity properties of magic monotones based on quantum relative entropies for single-qubit states and beyond**, *Quantum* **8**, 1492 (2024). [DOI](https://doi.org/10.22331/q-2024-10-04-1492) · [arXiv:2307.08258v4](https://arxiv.org/abs/2307.08258v4), 26 November 2024.

Theorems 2–4 establish additivity for specified families of mixed states, including multiplicativity of stabilizer fidelity for products of single-qubit states. Section 6, Eq. (44), gives a distillation bound. The following paragraph extends it to catalytic assistance when the relevant target–catalyst product satisfies the required additivity equality. It does not provide a size bound for an arbitrary catalyst returned only as a marginal of a correlated output.

Section 7.2, Proposition 6 gives single-qubit stabilizer fidelity, and Section 8 provides symmetric-state examples. Their state called H is Clifford equivalent to the T-gate injection state used here; their state called T has a different Bloch direction. The comparison below fixes the state explicitly to avoid this naming ambiguity.

## Closest catalyst-resource bound

<a id="rt2022"></a>

### [RT2022] Rubboli and Tomamichel: a Rényi-gap theorem

Roberto Rubboli and Marco Tomamichel, **Fundamental Limits on Correlated Catalytic State Transformations**, *Physical Review Letters* **129**, 120506 (2022). [DOI](https://doi.org/10.1103/PhysRevLett.129.120506) · [arXiv:2111.13356v2](https://arxiv.org/abs/2111.13356v2), 22 August 2022.

Theorem 2, with the quantitative form in Supplemental Section V, Theorem 7, proves logarithmically divergent catalyst resource when, for some $`\alpha\in[1/2,1)`$,

```math
\mathfrak D_\alpha(\rho_{\rm in})<\mathfrak D_\alpha(\psi),
```

and $`\mathfrak D_\alpha`$ is additive for the target against every catalyst. The error is purified distance of the joint output from the target–catalyst product. This is a substantial predecessor: a logarithmic catalyst-resource law itself is already known under these hypotheses.

The present comparison turns on the strict input–target resource gap. Pure targets approximately decouple from their environment, so the different error convention alone is not a substantive separation. Nor can one extend the theorem to $`\alpha\to0`$ without additional work: the stated range is $`[1/2,1)`$, and Appendix B discusses a failure of the analogous smoothed Petz-divergence approach.

### An explicit input for which the gap is absent

The following calculation combines the single-qubit fidelity and product additivity of [RTT2024](#rtt2024) with monotonicity in the sandwiched Rényi parameter; it is an applicability check, not a claim that a two-input factory is achievable.

Define

```math
|T\rangle=(|0\rangle+e^{i\pi/4}|1\rangle)/\sqrt2,
\quad
\rho=0.99|T\rangle\!\langle T|+0.01|T^\perp\rangle\!\langle T^\perp|,
\quad f=\cos^2(\pi/8).
```

An explicit free optimizer is

```math
\sigma_* = \frac{|+\rangle\!\langle+|+|+i\rangle\!\langle+i|}{2}
=f|T\rangle\!\langle T|+(1-f)|T^\perp\rangle\!\langle T^\perp|,
```

whose Bloch vector is $`(1/2,1/2,0)`$. To see optimality, twirl any free state by the identity and the Clifford $`U=(X+Y)/\sqrt2`$. This fixes $`\rho`$, preserves the free set, and cannot decrease its fidelity with $`\rho`$. The twirled state has Bloch vector $`(a,a,0)`$ with $`|a|\le1/2`$, so its eigenvalue $`s`$ along $`|T\rangle`$ lies in $`[1-f,f]`$. Its fidelity with $`\rho`$ is $`(\sqrt{0.99s}+\sqrt{0.01(1-s)})^2`$, which increases throughout this interval because $`s\le f<0.99`$. Thus $`s=f`$ is optimal, giving

```math
F_{\rm stab}(\rho)
=\left(\sqrt{0.99f}+\sqrt{0.01(1-f)}\right)^2
\simeq0.9168385592.
```

Using the single-qubit fidelity multiplicativity of [RTT2024](#rtt2024), Theorem 2, and $`\mathfrak D_{1/2}=-\log_2 F_{\rm stab}`$ gives

```math
\mathfrak D_{1/2}(\rho^{\otimes2})
=-2\log_2 F_{\rm stab}(\rho)
\simeq0.2505207491
> -\log_2 f
\simeq0.2284466968.
```

The target value is constant over the entire relevant Rényi range. For $`\alpha\in[1/2,1)`$, put $`\beta=(1-\alpha)/\alpha\in(0,1]`$. For any free $`\sigma`$, scalar Jensen applied to its spectral decomposition gives

```math
\langle T|\sigma^\beta|T\rangle
\le \langle T|\sigma|T\rangle^\beta
\le f^\beta.
```

The pure-state formula for sandwiched Rényi divergence therefore implies

```math
\widetilde D_\alpha(T\|\sigma)
=\frac{\alpha}{\alpha-1}\log_2\langle T|\sigma^\beta|T\rangle
\ge-\log_2 f.
```

The same commuting free state $`\sigma_*`$ attains equality, so $`\mathfrak D_\alpha(T)=-\log_2 f`$. Since $`\mathfrak D_\alpha(\rho^{\otimes2})\ge\mathfrak D_{1/2}(\rho^{\otimes2})`$, the strict gap required by [RT2022](#rt2022) fails throughout its parameter range. Free ancillary qubits can equalize the input and output dimensions. The source is full rank, so the present positive-free-component bound still applies. This establishes a concrete difference in theorem scope without relying on generic nonadditivity claims.

## Purification bounds and the free-component method

<a id="fl2020"></a>

### [FL2020] Fang and Liu: full-rank purification bounds

Kun Fang and Zi-Wen Liu, **No-Go Theorems for Quantum Resource Purification**, *Physical Review Letters* **125**, 060405 (2020). [DOI](https://doi.org/10.1103/PhysRevLett.125.060405) · [arXiv:1909.02540v4](https://arxiv.org/abs/1909.02540v4), 6 August 2020.

Theorem 1 bounds the error of purification from a full-rank input, including a success-probability-dependent version; Corollary 2 excludes exact purification. This establishes the underlying full-rank obstruction before the present work.

Applying that theorem directly to the combined input $`\rho^{\otimes n}\otimes\tau`$ requires the catalyst to satisfy the corresponding input condition. An arbitrary catalyst may be rank deficient. Even among full-rank catalysts of fixed dimension, the smallest eigenvalue can approach zero. Thus the stated minimum-eigenvalue estimate does not directly give a bound in terms of catalyst qubits or relative entropy of magic alone.

<a id="fl2022"></a>

### [FL2022] Fang and Liu: positive free components

Kun Fang and Zi-Wen Liu, **No-Go Theorems for Quantum Resource Purification: New Approach and Channel Theory**, *PRX Quantum* **3**, 010337 (2022). [DOI](https://doi.org/10.1103/PRXQuantum.3.010337) · [arXiv:2010.11822v4](https://arxiv.org/abs/2010.11822v4), 10 March 2022.

Definition 1 uses the largest free component

```math
\Gamma(\rho)=\max\{p:\rho\ge p\sigma,\ \sigma\text{ free}\}.
```

Theorem 4 gives $`\varepsilon\ge\Gamma(\rho)(1-F_{\rm free}(\psi))`$, and Corollary 5 gives logarithmic copy overhead. Proposition 7 characterizes positive free component by support; full rank is sufficient, not necessary.

The branch decomposition in the present proof is this existing method. The additional step is to repeat an exactly reusable factory and charge its arbitrary resourceful catalyst on the all-free-input branch. The catalyst need not be returned on that branch. Directly applying the older bound to the combined source and catalyst can be vacuous because their joint free component can vanish, including for a pure magic catalyst.

<a id="rt2021"></a>

### [RT2021] Regula and Takagi: channel resource bounds

Bartosz Regula and Ryuji Takagi, **Fundamental limitations on distillation of quantum channel resources**, *Nature Communications* **12**, 4411 (2021). [DOI](https://doi.org/10.1038/s41467-021-24699-0) · [arXiv:2010.11942v3](https://arxiv.org/abs/2010.11942v3), 17 July 2021.

This independently developed resource-weight and robustness approach gives purification errors, overhead bounds, and channel-distillation constraints. It is part of the prior foundation for free-component arguments; the present work makes no priority claim for that method or for logarithmic noncatalytic distillation overhead.

<a id="r2022"></a>

### [R2022] Regula: projective robustness

Bartosz Regula, **Probabilistic Transformations of Quantum Resources**, *Physical Review Letters* **128**, 110505 (2022). [DOI](https://doi.org/10.1103/PhysRevLett.128.110505) · [arXiv:2109.04481v3](https://arxiv.org/abs/2109.04481v3), 15 March 2022.

Theorem 4, Eq. (6), gives a general infidelity lower bound in terms of projective robustness of the input, valid even for probabilistic transformations. The discussion preceding Eq. (3) states that projective robustness is finite exactly when a free state has the same support as the input.

A pure magic catalyst can therefore have infinite projective robustness while occupying finitely many qubits and having finite relative entropy of magic. Applying this purification bound to the combined input does not by itself yield the finite-memory lower bound studied here. This is a limitation of that direct application, not a claim that projective-robustness techniques cannot be extended.

## Existing constructions that attain the memory order

<a id="why2025"></a>

### [WHY2025] Wills, Hsieh, and Yamasaki: constant-rate batches

Adam Wills, Min-Hsiu Hsieh, and Hayata Yamasaki, **Constant-overhead magic state distillation**, *Nature Physics* **21**, 1842–1846 (2025). [DOI](https://doi.org/10.1038/s41567-025-03026-0) · [arXiv:2408.07764v2](https://arxiv.org/abs/2408.07764v2), 21 August 2024.

Theorem 1.1 states constant-overhead qubit magic-state distillation. Theorem 6.1 and Eqs. (301)–(305) give a deterministic CCZ batch construction with constant output rate and exponentially decreasing whole-batch error below a fixed threshold. The protocol uses error correction without postselection. Section 4.4 and Appendix B describe the conversion through ten-qubit magic states; an explicit decomposition uses 70 CCZ states per such input block.

This supplies the batch ingredient for the upper bound. The asymptotic memory conclusion uses the published code family and its error estimate; it does not claim a new code, an improved threshold, or competitive practical constants.

<a id="fl2026"></a>

### [FL2026] Fang and Liu: one-shot catalytic distillation

Kun Fang and Zi-Wen Liu, **One-shot distillation with constant overhead using catalysts**, *Nature Communications* **17**, 6010 (2026). [DOI](https://doi.org/10.1038/s41467-026-72686-0) · [arXiv:2410.14547v3](https://arxiv.org/abs/2410.14547v3), 2 September 2026.

Theorem 3 converts a batch protocol into catalytic single-output distillation. Theorem 4 proves exact marginal return and repeated use in the deterministic setting, allowing output correlations; Corollary 6 gives constant fresh-input overhead. Methods 4.1–4.2 describe the catalyst and reuse argument. Its block storage and classical flag give the memory accounting used here when combined with [WHY2025](#why2025).

Section 2.3, following Corollary 6, explicitly raises the question of whether vanishing error can be achieved with finite catalyst magic. The present result addresses the deterministic, fixed-source, positive-free-component setting. The probabilistic one-shot protocols of Theorem 7 and Corollary 8 are not automatically covered when catalyst return is required only upon success.

## Broadcasting and robustness

<a id="son2026"></a>

### [SON2026] Son et al.: robustness to source perturbations

Jeongrak Son, Ray Ganardi, Shintaro Minagawa, Francesco Buscemi, Seok Hyung Lie, and Nelly H. Y. Ng, **Catalytic Channels Are the Only Noise-Robust Catalytic Processes**, *Physical Review Letters* **136**, 050202 (2026). [DOI](https://doi.org/10.1103/pc1j-bd5y) · [arXiv:2412.06900v2](https://arxiv.org/abs/2412.06900v2), 7 January 2026.

Here robustness requires exact catalyst return for every source in a neighborhood of the nominal input. Theorems 1–2 connect catalytic channels, resource broadcasting, and restrictions under specified free-operation and composition assumptions.

The factory studied here assumes exact return at one fixed source. Its lower bound does not establish stability under source perturbations or noise in the catalyst. Conversely, a no-go result requiring neighborhood-wide exact return does not directly settle this weaker fixed-source model. The operation-class qualifications in this paper also matter when specializing its statements to stabilizer operations.

<a id="zfl2024"></a>

### [ZFL2024] Zhang, Feng, and Luo: no-broadcasting of magic

Zijian Zhang, Lingxuan Feng, and Shunlong Luo, **No-broadcasting of magic states**, *Physical Review A* **110**, 012462 (2024). [DOI and publisher abstract](https://doi.org/10.1103/PhysRevA.110.012462), published 25 July 2024.

The publisher abstract establishes no-broadcasting of magic by stabilizer operations and announces a trade-off between magic consumed in the initial system and magic gained in the target system. This is directly relevant background, and it is cited in [SON2026](#son2026).

The full theorem statements and quantitative trade-off have not been checked against an accessible full text. Accordingly, this reference does **not** support a claim here that every quantitative no-broadcasting bound is weaker than the present result. A theorem-by-theorem comparison with that trade-off remains a specific literature limitation. The lower-bound proof itself is independent of this reference.

## Delimitation

The supported distinction is a catalyst-resource and memory bound without a one-shot input–target resource-gap assumption, for deterministic reuse with exact nominal marginal return and arbitrary allowed correlations. Its ingredients and matching CCZ construction are attributed above. The statement does not cover a catalyst returned only on successful postselection, approximate return accumulated over indefinitely many rounds, source drift, or the physical qubit and time overhead of protecting the catalyst against hardware noise.
