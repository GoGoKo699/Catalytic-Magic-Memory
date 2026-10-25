# Model and resource accounting

This model describes a deterministic magic-state factory that consumes a fixed fresh noisy block, emits one target register, and exactly restores the marginal state of its complete persistent memory. The emitted state may remain correlated with that memory and with all earlier emissions. The [converse](converse.md) bounds the magic stored in the memory and, consequently, the number of persistent quantum qubits.

All registers are finite dimensional for each protocol instance. Their dimensions may grow with the requested accuracy. Classical storage has no prescribed size bound, but is finite in each instance. Logarithms in quantum relative entropies and entropies are base two; $`\ln`$ denotes the natural logarithm.

## 1. Free states and operations

For a register of $`k`$ qubits, let

```math
\mathrm{STAB}_k
=\mathrm{conv}\left\{
  |s\rangle\langle s|:\ |s\rangle
  \text{ is a pure }k\text{-qubit stabilizer state}
\right\}.
```

The number of qubits is omitted when the register is unambiguous. This set is closed under tensor products, partial traces, and classical mixing. In particular, $`I/2^k`$ is free. A genuinely classical register is represented in a computational basis; every probability distribution diagonal in that basis is free.

A quantum channel $`\Lambda_{AC\to BC}`$ is **completely stabilizer preserving** if, for every auxiliary qubit register $`R`$,

```math
(\mathrm{id}_R\otimes\Lambda)
\bigl(\mathrm{STAB}(RAC)\bigr)
\subseteq \mathrm{STAB}(RBC).
```

The converse allows all such completely positive, trace-preserving maps. Complete preservation matters: during repeated use, old output registers can remain entangled with $`C`$ while the next channel acts on $`AC`$. Preservation of free states on $`AC`$ alone would not justify the resource comparison for this larger joint system.

Physical stabilizer operations form a sufficient subclass. They include free stabilizer ancillas, Clifford unitaries, Pauli measurements, classical randomization and feedforward, discarding, and free resets. Classical outcomes may control later stabilizer operations. Measurements and all their branches are included in the unconditional channel: the factory cannot condition its performance claim on a successful postselection event. Arbitrary classical computation on dephased records does not supply a coherent non-Clifford gate.

This distinction separates the two statements used in the repository:

- The converse holds for the larger class of completely stabilizer-preserving channels.
- A physical construction must specify operations from the stabilizer subclass and account for every magic state it supplies.

No fresh nonstabilizer state is available for free. Any such state used during a call must be part of its charged source block or of its persistent catalyst.

## 2. A stationary call

Let $`A`$ be the fresh source register, $`B`$ the emitted target register, and $`C`$ the complete persistent memory. Fix a source state $`\chi_A`$, a catalyst state $`\tau_C`$, and a deterministic channel $`\Lambda_{AC\to BC}`$. Write

```math
\omega_{BC}=\Lambda(\chi_A\otimes\tau_C).
```

For a pure target $`\psi_B=|\psi\rangle\langle\psi|`$ and a specified error tolerance $`\varepsilon\in[0,1]`$, a stationary call satisfies

```math
\mathrm{Tr}_B\omega_{BC}=\tau_C,
\qquad
\mathrm{Tr}(\psi_B\omega_B)\ge 1-\varepsilon.
\qquad\text{(M1)}
```

The first condition is **exact marginal return on the designated input**. It does not require
$`\omega_{BC}=\omega_B\otimes\tau_C`$. Arbitrary output–catalyst correlations are permitted. The catalyst can be mixed, entangled across its internal registers, or rank deficient.

The same channel is used at every call. A channel and catalyst may be designed separately for each $`\varepsilon`$; no fixed catalyst is assumed across an accuracy-dependent family of protocols. Within one instance, however, the source, channel, and designated returned catalyst state are fixed.

Condition (M1) is imposed only when the fresh state is $`\chi_A`$ and the memory marginal is $`\tau_C`$. There is no requirement that the catalyst return on a neighbourhood of source states, on all source states, or on the free comparison input introduced below. This is the marginal-return convention used for deterministic correlated catalytic distillation in [FL2026](../references/related-work.md#fl2026).

### The complete persistent controller

The register $`C`$ includes every quantum system and every correlated classical record needed to operate the next call. A phase label, adaptive branch record, or other controller that is retained between calls belongs to $`C`$ even when its storage is free in the resource accounting. Its joint state with the quantum memory is included in the equality in (M1).

Temporary work registers can be introduced in free states and discarded during a call. A record that is permanently discarded need not be retained in $`C`$. A record used again later cannot be omitted. In particular, an evolving uncounted controller is not a stationary catalyst in this model.

The channel description itself may depend on the target accuracy. No bound on Clifford circuit size, classical computation time, or call duration is part of the converse.

## 3. Independent fresh blocks and sequential reuse

For $`L`$ calls, the initial state is

```math
\chi_{A_1}\otimes\cdots\otimes\chi_{A_L}\otimes\tau_C.
\qquad\text{(M2)}
```

Call $`i`$ applies $`\Lambda`$ to $`A_iC`$ and emits $`B_i`$. Earlier outputs are kept untouched by the factory. The same physical memory is passed from one call to the next; it is not replaced by a newly prepared copy of $`\tau_C`$.

The full source blocks are independent of one another and of the initial memory. A block $`\chi_A`$ may contain internal correlations. The theorem therefore does not require an independent noise model within a block, but it does require the product structure across calls in (M2).

Exact marginal stationarity makes reuse possible even when $`C`$ is correlated with previous outputs. Before each call the reduced state on the new $`A_iC`$ is $`\chi_A\otimes\tau_C`$, so the new output has the same nominal quality guarantee. Later trace-preserving operations on other registers leave an earlier output marginal unchanged. The joint state of all outputs need not be a product.

Keeping old outputs untouched is a proof experiment permitted by the stationary channel. It makes no assumption about whether a user would subsequently consume those outputs in a quantum computation.

## 4. A positive free component in the source

The source condition is the operator inequality

```math
\chi_A\succeq w\,\sigma_{0,A},
\qquad
\sigma_{0,A}\in\mathrm{STAB}(A),
\qquad
0<w\le 1,
\qquad\text{(M3)}
```

where $`\sigma_0`$ is normalized and $`\succeq`$ denotes positive-semidefinite order. For $`w<1`$, this is equivalently a decomposition

```math
\chi=w\sigma_0+(1-w)\eta
```

for some density operator $`\eta`$. The protocol is not told which term of this decomposition was used. The proof does not herald or physically select a free branch.

Every full-rank $`s`$-qubit state $`\rho`$ has a positive free component. With $`d=2^s`$,

```math
\rho\succeq p\,\frac{I_d}{d},
\qquad
p=d\,\lambda_{\min}(\rho)>0.
```

Consequently, for a call consuming $`n`$ copies,

```math
\chi=\rho^{\otimes n},
\qquad
\sigma_0=(I_d/d)^{\otimes n},
\qquad
w=p^n
\qquad\text{(M4)}
```

is always an admissible choice. A better positive domination weight can improve the finite numerical bound, but is not required.

Full rank is sufficient, not necessary: (M3) is the actual hypothesis. A rank-deficient source that contains a positive free component is also covered. A source with no positive free component is outside this converse.

For example, a fixed depolarized pure target,

```math
\rho_\lambda=(1-\lambda)\psi+\lambda I_d/d,
\qquad 0<\lambda<1,
```

obeys $`\rho_\lambda\succeq\lambda I_d/d`$. A call consuming $`n`$ copies has $`w=\lambda^n`$. For a three-qubit CCZ target, the source infidelity is $`7\lambda/8`$.

### An optimized weight for a depolarized T source

For the computational $`T`$ state specified below, let
$`\rho_\lambda=(1-\lambda)\psi_T+\lambda I_2/2`$ with
$`0<\lambda<1-1/\sqrt2`$. Its largest normalized free-component weight is

```math
p_{\rm free}=\frac{\lambda}{1-1/\sqrt2}.
```

Indeed, the free state $`\gamma`$ with Bloch vector $`(1/2,1/2,0)`$ gives
$`\rho_\lambda=p_{\rm free}\gamma+(1-p_{\rm free})\psi_T`$.
Conversely, every decomposition
$`\rho_\lambda=p\sigma+(1-p)\eta`$ with free $`\sigma`$ obeys

```math
1-\frac\lambda2
=\mathrm{Tr}(\psi_T\rho_\lambda)
\le p\cos^2(\pi/8)+(1-p),
```

which forces $`p\le p_{\rm free}`$. For $`n`$ fresh copies,
$`w=p_{\rm free}^{\,n}`$ is therefore an admissible block weight. This does
not claim that the product choice is the largest free weight of the whole
block. Optimizing the weight strengthens finite constants; a merely positive
weight already suffices for the divergence theorem.

### Fixed-weight quantifiers

The finite theorem permits any particular $`n`$ and any admissible $`w`$. Its logarithmic asymptotic corollary fixes a common $`w\in(0,1)`$ while $`\varepsilon\to0`$. A fixed noisy state and a fixed fresh-copy count provide such a weight. If the input count or source changes with accuracy, the finite theorem must be applied with the actual weight for each instance; a uniform asymptotic conclusion needs a separately justified common weight.

## 5. The target overlap assumption

For a pure target on $`b`$ qubits define

```math
b_L
=F_{\mathrm{STAB}}(\psi^{\otimes L})
:=\max_{\sigma\in\mathrm{STAB}_{bL}}
\mathrm{Tr}\!\left(\psi^{\otimes L}\sigma\right).
\qquad\text{(M5)}
```

This is the squared overlap with the closest pure stabilizer state; maximizing over the convex free set gives the same value because the objective is linear. It is distinct from an assumption that the actual output copies are independent.

The basic finite theorem uses $`b_L`$ directly. The logarithmic memory law follows when, for some fixed $`f\in(0,1)`$,

```math
b_L\le f^L
\qquad\text{for every positive integer }L.
\qquad\text{(M6)}
```

Thus only exponential decay of the target's free overlap is needed. No multiplicativity statement involving the arbitrary catalyst is assumed.

For the targets used here, equality in (M6) is a known stabilizer-overlap identity. The stabilizer-alignment results of [B2019](../references/related-work.md#b2019) give the tensor-power identity for these states.

| Target | Explicit convention | Qubits per target | $`f`$ | $`c=\log_2(1/f)`$ |
| --- | --- | ---: | ---: | ---: |
| Computational $`T`$ | $`\displaystyle \lvert T\rangle=(\lvert0\rangle+e^{i\pi/4}\lvert1\rangle)/\sqrt2`$ | 1 | $`\cos^2(\pi/8)`$ | $`0.2284466968\ldots`$ |
| CCZ | $`\displaystyle \lvert\mathrm{CCZ}\rangle=\mathrm{CCZ}\lvert+\rangle^{\otimes3}`$ | 3 | $`9/16`$ | $`0.8300749986\ldots`$ |

Some resource-theory papers use the name $`T`$ for a different, tetrahedral Bloch-sphere state. The explicit ket in this table fixes the convention throughout these documents.

More generally, every pure state on at most three qubits is stabilizer aligned
by [B2019](../references/related-work.md#b2019). Its tensor-power overlap is
therefore $`b_L=F_{\mathrm{STAB}}(\psi)^L`$, with a constant strictly below
one for a nonstabilizer target. For such a small pure target, stabilizer
fidelity also factorizes against an arbitrary mixed catalyst; the
[reference account](../references/related-work.md#strong-small-target-multiplicativity)
explains the stronger statement and its derivation. The converse needs only
the tensor-power identity. Failure of generic multiplicativity is not a
reason to exclude earlier results for $`T`$ or CCZ; the explicit scope
comparison instead uses the
[absence of the required input–target resource gap](../references/related-work.md#an-explicit-input-for-which-the-gap-is-absent).

## 6. Stored magic and quantum memory

The relative entropy of magic, in bits, is

```math
E_R(\tau_C)
=\min_{\sigma_C\in\mathrm{STAB}(C)}
D(\tau_C\Vert\sigma_C),
\qquad
D(\rho\Vert\sigma)
=\mathrm{Tr}\rho(\log_2\rho-\log_2\sigma).
\qquad\text{(M7)}
```

The usual convention gives $`D=+\infty`$ when the support of $`\rho`$ is not contained in that of $`\sigma`$. Nevertheless, $`E_R(\tau_C)`$ is finite for every finite qubit catalyst because the maximally mixed comparison state is free and full rank. The definition and its use in correlated catalytic bounds are standard; see [RT2022](../references/related-work.md#rt2022).

If the complete catalyst is a quantum register of $`q`$ qubits, then

```math
E_R(\tau_C)\le D(\tau_C\Vert I/2^q)
=q-S(\tau_C)\le q.
\qquad\text{(M8)}
```

### Arbitrarily large classical storage

Suppose instead that the complete persistent state is genuinely classical–quantum:

```math
\tau_{JQ}
=\sum_j a_j |j\rangle\langle j|_J\otimes\tau_{j,Q},
\qquad
\dim Q=2^q.
\qquad\text{(M9)}
```

There is no prescribed upper bound on the number of labels $`j`$. The state

```math
\sigma_{JQ}
=\sum_j a_j |j\rangle\langle j|_J\otimes I_Q/2^q
```

is free, and the block-diagonal relative-entropy identity gives

```math
E_R(\tau_{JQ})
\le D(\tau_{JQ}\Vert\sigma_{JQ})
=q-\sum_j a_j S(\tau_{j,Q})
\le q.
\qquad\text{(M10)}
```

Hence an arbitrarily large finite classical controller cannot supply the required relative-entropy magic. Coherently stored labels are quantum memory and must be included in the quantum count. If different classical branches use different numbers of qubits, padding smaller branches with free qubits lets $`q`$ denote the maximum persistent quantum width.

The converse allows an arbitrary initial $`\tau`$, even one prepared with external resources. Its preparation cost is not needed to establish a lower bound on stored magic. Any claimed upper construction has the separate obligation to account for initialization and to identify the source of all its magic.

### Other stored-resource measures

The same comparison experiment also constrains fidelity and max-relative
entropy of magic. Use squared Uhlmann fidelity and define

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1^2,
\qquad
F_{\mathrm{STAB}}(\rho)=\max_{\sigma\in\mathrm{STAB}}F(\rho,\sigma),
\qquad
G(\rho)=-\log_2F_{\mathrm{STAB}}(\rho),
```

```math
M_R(\rho)=\min_{\sigma\in\mathrm{STAB}}D_{\max}(\rho\Vert\sigma),
\qquad
D_{\max}(\rho\Vert\sigma)
=\inf\{m:\rho\preceq2^m\sigma\}.
```

Thus $`M_R`$ is logarithmic generalized robustness, with multiplicative
robustness $`2^{M_R(\rho)}`$. The pointwise divergence inequalities imply

```math
G(\rho)\le E_R(\rho)\le M_R(\rho).
```

For the complete classical–quantum catalyst (M9),
$`\tau_{JQ}\preceq2^q\sigma_{JQ}`$ with the same free comparison state
used in (M10), since $`\tau_{j,Q}\preceq I_Q`$. Hence

```math
G(\tau_{JQ})\le E_R(\tau_{JQ})\le M_R(\tau_{JQ})\le q.
```

This also covers a wholly quantum catalyst. The
[companion resource bounds](converse.md#companion-resource-bounds) quantify
these measures without replacing the stronger direct relative-entropy
theorem.

## 7. Meaning and limits of the model

The resource question is whether bounded fresh noisy input per emission can coexist with bounded reusable quantum memory as the emitted pure-state approximation improves. The converse shows that a positive free component in the source forces increasing stored magic when the target tensor powers have exponentially decreasing stabilizer overlap.

The memory count is a logical persistent quantum-register count. It is not an estimate of fault-tolerant physical qubits, temporary peak workspace, Clifford gate count, classical decoding time, or throughput. Ideal free operations are assumed. The output criterion is state overlap infidelity,
$`1-\mathrm{Tr}(\psi\omega_B)`$; it is not an automatic diamond-norm guarantee for an injected gate. A trace-distance guarantee
$`\tfrac12\|\omega_B-\psi\|_1\le\varepsilon`$
does imply the overlap guarantee in (M1).

The stationary theorem does not assume that the input block contains less total magic than the target. It does require deterministic processing, independent fresh blocks, and exact nominal return of the complete persistent state. Postselected return only on success, adaptive unbounded input consumption, approximate catalyst recovery, source drift, correlated blocks across calls, or unaccounted persistent resources require a different analysis. The [finite-horizon lemma](converse.md#finite-horizon-lemma) takes a guarantee for each output in a specified horizon as its premise. The controlled return-error estimate following that lemma shows how a nominal trace-distance disturbance can accumulate; it does not supply the indefinite accuracy guarantee of exact stationarity.

### The quantity minimized in the matching law

For fixed source $`\rho`$, target $`\psi`$, and integer input budget $`r`$, let $`\mathcal F_q(\varepsilon;\rho,r,\psi)`$ be the set of physical stabilizer factories satisfying (M1), with source $`\rho^{\otimes r}`$ and $`q`$ persistent quantum qubits. Define

```math
q_{\min}(\varepsilon;\rho,r,\psi)
=\inf\left\{q\in\mathbb N_0:
\mathcal F_q(\varepsilon;\rho,r,\psi)\ne\varnothing\right\}.
```

The infimum includes arbitrary initial catalyst states and arbitrary finite free classical storage. The channel and catalyst may depend on $`\varepsilon`$. Set $`q_{\min}=+\infty`$ if the feasible set is empty. Thus a lower bound does not silently assert that every fixed input budget is achievable.

The converse holds for the larger completely stabilizer-preserving class, so it bounds this physical-operation minimum as well. The [CCZ construction](construction.md) proves feasibility with a catalyst prepared from the same noisy source at a sufficient fixed budget. For its fixed permitted source and every fixed $`r\ge1680`$, the two bounds give $`q_{\min}(\varepsilon)=\Theta(\log(1/\varepsilon))`$ as $`\varepsilon\downarrow0`$. The dependence on source and budget is suppressed only in this asymptotic shorthand.

The finite lower bound and its proof are given in [Converse bounds](converse.md). The matching upper bound is established in the [CCZ construction](construction.md), with initialization and the complete resource ledger in [Resources](resources.md).
