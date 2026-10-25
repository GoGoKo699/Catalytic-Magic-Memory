# Magic targets and the absence of a resource gap

The [general converse](reuse_converse.md) needs the maximum free overlap of target tensor powers. This page identifies that quantity for standard magic targets and gives a concrete regime beyond the resource-gap assumption of the earlier catalytic converse.

## T and CCZ conventions

Define

```math
|T\rangle=\frac{|0\rangle+e^{i\pi/4}|1\rangle}{\sqrt2},
\qquad
|\mathrm{CCZ}\rangle=\mathrm{CCZ}|+\rangle^{\otimes3}.
```

The T state is specified explicitly because T/H nomenclature differs between sources. Its Clifford-equivalent real form has amplitudes $`\cos(\pi/8)`$ and $`\sin(\pi/8)`$.

The stabilizer overlaps are

| Target projector $`\psi`$ | $`F_{\mathrm{STAB}}(\psi)`$ | $`f_\ell`$ | $`a=-\log_2 F_{\mathrm{STAB}}(\psi)`$ |
|---|---:|---:|---:|
| T | $`\cos^2(\pi/8)`$ | $`\cos^{2\ell}(\pi/8)`$ | $`0.2284466968\ldots`$ |
| CCZ | $`9/16`$ | $`(9/16)^\ell`$ | $`0.8300749986\ldots`$ |

These identities are established in [Bravyi et al.](../references/RELATED_WORK.md#bravyi2019), including their tensor-product results for stabilizer-aligned states. Every pure state on at most three qubits is stabilizer aligned. The same exponential-overlap condition therefore holds for any fixed nonstabilizer pure target on at most three qubits, with its own single-copy overlap.

For pure targets, optimizing over the stabilizer convex hull is equivalent to maximizing over pure stabilizer states because the overlap is linear in the comparison state. The [finite enumeration](../verification/README.md) independently reproduces the T and CCZ constants and the two-copy T value. Tensor-power multiplicativity is supplied by the analytical result, not inferred from this enumeration.

## Strong multiplicativity for a small pure target

General magic fidelity is not multiplicative. This does not mean that a standard pure target fails to be multiplicative against an arbitrary catalyst. In fact, for a pure target $`\psi`$ on at most three qubits and any mixed catalyst $`\tau`$,

```math
F_{\mathrm{STAB}}(\psi\otimes\tau)
=F_{\mathrm{STAB}}(\psi)F_{\mathrm{STAB}}(\tau).
```

This fact clarifies the comparison with earlier catalytic bounds.

### Pure catalyst

For a pure state $`|\chi\rangle`$, let

```math
F_r(\chi)=2^{-r/2}
\max_P\langle\chi|P|\chi\rangle,
```

where the maximum is over rank-$`2^r`$ stabilizer projectors on the relevant register. Then $`F_0(\chi)`$ is its stabilizer fidelity. Bravyi et al., Lemma 11, prove
$`F_r(\chi)\le F_0(\chi)`$ for $`r=1,2,3`$, for a pure state on any number of qubits.

A bipartite pure stabilizer state across the target and catalyst registers has a local-Clifford Schmidt form with $`r`$ maximally entangled qubit pairs. Since the target has at most three qubits, $`r\le3`$. Its Schmidt vectors span rank-$`2^r`$ stabilizer projectors $`P_A`$ and $`P_C`$. Cauchy–Schwarz gives

```math
\begin{aligned}
|\langle S|\psi\otimes\chi\rangle|^2
&\le2^{-r}
\langle\psi|P_A|\psi\rangle
\langle\chi|P_C|\chi\rangle\\
&\le F_r(\psi)F_r(\chi)\\
&\le F_0(\psi)F_0(\chi).
\end{aligned}
```

For $`r=0`$ the same statement is the product bound. A product of closest stabilizer states attains the lower bound, proving equality for every pure catalyst.

### Mixed catalyst

For fidelity to a convex hull of pure free states, Uhlmann's theorem gives the ensemble identity

```math
F_{\mathrm{STAB}}(x)
=\max_{x=\sum_i p_i|\chi_i\rangle\langle\chi_i|}
\sum_i p_i F_{\mathrm{STAB}}(\chi_i).
```

For completeness, purify a free mixture
$`\sum_i q_i|s_i\rangle\langle s_i|`$ with an orthogonal label. Optimizing its overlap with a purification of $`x`$ amounts to optimizing a pure-state ensemble of $`x`$. For a fixed ensemble, choose each stabilizer vector to maximize
$`|\langle s_i|\chi_i\rangle|^2`$. Optimizing $`q_i`$ by Cauchy–Schwarz gives the sum in the display. Repeated stabilizer vectors and zero weights allow a common label space, so this optimization covers all decompositions.

Every vector in an ensemble decomposition of $`\psi\otimes\tau`$ lies in
$`\mathrm{span}\{|\psi\rangle\}\otimes\mathrm{supp}\tau`$. It therefore has the pure target as a factor. Applying the pure-catalyst product identity inside the ensemble optimization proves the mixed-catalyst equality.

The converse in this repository does not require this equality. Its absence is nevertheless not a valid explanation of why an earlier result fails for T or CCZ.

## A useful source free weight

For a noisy T source

```math
\rho_\nu=(1-\nu)\psi_T+\nu I_2/2,
\qquad
0<\nu<1-\frac1{\sqrt2},
```

the largest free weight is

```math
p_*=\frac{\nu}{1-1/\sqrt2}.
```

Let $`\gamma`$ have Bloch vector $`(1/2,1/2,0)`$, on the stabilizer octahedron. Direct substitution gives
$`\rho_\nu=p_*\gamma+(1-p_*)\psi_T`$, establishing this weight.

Conversely, for any free-component decomposition
$`\rho_\nu=p\gamma'+(1-p)\xi`$, the pure-target overlap satisfies

```math
1-\frac{\nu}{2}
=\mathrm{Tr}(\psi_T\rho_\nu)
\le p\cos^2(\pi/8)+(1-p).
```

This implies $`p\le p_*`$. Thus the weight is optimal. For an arbitrary depolarized target, the simpler weight $`p=\nu`$ from the maximally mixed component is always available; optimization is unnecessary for logarithmic divergence.

## Absence of every Renyi gap in the earlier converse

Let

```math
\mathfrak D_\alpha(x)=
\min_{\sigma\in\mathrm{STAB}}\widetilde D_\alpha(x\Vert\sigma)
```

be minimized sandwiched Rényi divergence. The theorem of
[Rubboli and Tomamichel](../references/RELATED_WORK.md#rubboli2022) requires a parameter $`\alpha\in[1/2,1)`$ with
$`\mathfrak D_\alpha(\rho^{\otimes k})<\mathfrak D_\alpha(\psi)`$, together with target additivity.

For the T target put $`f=\cos^2(\pi/8)`$ and $`a=-\log_2f`$. The free state $`\gamma`$ above has $`|T\rangle`$ as an eigenvector with eigenvalue $`f`$. Evaluating the sandwiched divergence against $`\gamma`$ gives
$`\mathfrak D_\alpha(\psi_T)\le a`$. Monotonicity in $`\alpha`$ and
$`\mathfrak D_{1/2}(\psi_T)=a`$ give the reverse inequality. Hence

```math
\mathfrak D_\alpha(\psi_T)=a
\qquad\text{for every }\alpha\in[1/2,1).
```

[Rubboli, Takagi and Tomamichel](../references/RELATED_WORK.md#rubboli2024) prove multiplicativity of mixed-state stabilizer fidelity for products of single-qubit states. Consequently,

```math
\mathfrak D_\alpha(\rho_\nu^{\otimes k})
\ge G_{\mathrm{STAB}}(\rho_\nu^{\otimes k})
=kG_{\mathrm{STAB}}(\rho_\nu).
```

If $`kG_{\mathrm{STAB}}(\rho_\nu)\ge a`$, no parameter allowed in the earlier theorem supplies its strict gap. The present converse retains a positive coefficient for every such fixed $`k`$, since $`p_*>0`$.

### Explicit example

Write $`r=1-\nu`$. Symmetrizing a free comparison state around the T axis leaves $`\rho_\nu`$ invariant and cannot decrease fidelity. On that axis its Bloch radius is at most $`1/\sqrt2`$. The qubit fidelity formula is

```math
F(\rho_\nu,\sigma_t)
=\frac12\left(1+rt+\sqrt{1-r^2}\sqrt{1-t^2}\right).
```

For $`r>1/\sqrt2`$, this increases on $`0\le t\le1/\sqrt2`$. Therefore,

```math
F_{\mathrm{STAB}}(\rho_\nu)
=\frac12\left(
1+\frac r{\sqrt2}
+\sqrt{\frac{1-r^2}{2}}
\right).
```

At $`\nu=0.01`$,

| Quantity | Value |
|---|---:|
| $`G_{\mathrm{STAB}}(\rho_\nu)`$ | $`0.1521751049\ldots`$ |
| $`G_{\mathrm{STAB}}(\rho_\nu^{\otimes2})`$ | $`0.3043502099\ldots`$ |
| $`\mathfrak D_\alpha(\psi_T)`$ for all allowed $`\alpha`$ | $`0.2284466968\ldots`$ |
| Optimal free weight $`p_*`$ | $`0.0341421356\ldots`$ |
| New leading fidelity-resource coefficient at $`k=2`$ | $`0.0229063968\ldots`$ |

This is a separation of theorem hypotheses. It does not establish that two noisy T inputs per round can attain arbitrary accuracy. The absence of the earlier gap persists for all larger fixed $`k`$. The matching achievability result in this repository uses a sufficiently large fixed batch and a low-noise CCZ source.
