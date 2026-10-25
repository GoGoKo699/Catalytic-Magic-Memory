# Precision, stored magic and catalyst memory

Use the [factory model](model.md) and the [finite-error converse](reuse_converse.md). All logarithms are base two. The source, target and integer $`k`$ are fixed unless stated otherwise.

## A finite stored-resource budget gives an error floor

If the catalyst satisfies $`G_{\mathcal F}(\tau)\le g`$, then $`F_{\mathcal F}(\tau)\ge2^{-g}`$. Rearranging the finite-error theorem gives

```math
\boxed{
\varepsilon\ge
\sup_{\ell\ge1}\frac{p^{k\ell}}{\ell}
\left(2^{-g/2}-\sqrt{f_\ell}\right)_+^2.
}
```

The supremum is over integers and $`(x)_+=\max\{x,0\}`$. For $`g=G_{\mathcal F}(\tau)`$ this is the same necessary inequality expressed as an error floor. It is not a sufficient condition for a factory to exist.

If $`f_\ell\to0`$, any finite $`g`$ gives a strictly positive floor: choose a finite $`\ell`$ with $`f_\ell<2^{-g}`$. Thus bounded fidelity resource cannot support vanishing output error, even if the catalyst's dimension is unbounded across the family.

Suppose more specifically that $`f_\ell\le2^{-a\ell}`$ with $`a>0`$, and put $`b=\log_2(1/p)`$. Taking
$`\ell_g=\lceil(g+2)/a\rceil`$ gives

```math
\varepsilon\ge
\frac{2^{-g}p^{k\ell_g}}{4\ell_g}.
```

This follows because $`\sqrt{f_{\ell_g}}\le2^{-g/2}/2`$. It displays a positive accuracy floor for a prescribed stored-magic budget without an asymptotic limit.

## Logarithmic fidelity-resource cost

Set $`L=\log_2(1/\varepsilon)`$ and $`A=a+kb`$. For sufficiently large $`L`$, choose

```math
\ell=\left\lfloor\frac{L-\log_2 L}{A}\right\rfloor\ge1.
```

Then

```math
\frac{\ell\varepsilon p^{-k\ell}}{2^{-a\ell}}
=\ell\,2^{-L+A\ell}
\le\frac{\ell}{L}\le\frac1A.
```

Substituting in the finite-error theorem and using
$`\ell\ge(L-\log_2L)/A-1`$ yields the explicit bound

```math
\boxed{
G_{\mathcal F}(\tau)\ge
\frac{a}{a+kb}(L-\log_2L)
-a-2\log_2\left(1+(a+kb)^{-1/2}\right).
}
```

In particular,

```math
\liminf_{\varepsilon\to0}
\frac{G_{\mathcal F}(\tau_\varepsilon)}
{\log_2(1/\varepsilon)}
\ge\frac{a}{a+k\log_2(1/p)}>0.
```

The explicit expression is intended for the range where the chosen integer $`\ell`$ is positive. The finite-error theorem applies at every error. When source noise or $`k`$ changes with accuracy, use that finite inequality with the actual parameters.

## Which resource measures inherit the bound?

Define

```math
E_{\mathcal F}(x)=\min_{\sigma\in\mathcal F}D(x\Vert\sigma),
\qquad
M_{\mathcal F}(x)=\min_{\sigma\in\mathcal F}D_{\max}(x\Vert\sigma).
```

Here $`D_{\max}(x\Vert\sigma)=\inf\{\lambda:x\le2^\lambda\sigma\}`$. The pointwise order of quantum divergences gives

```math
M_{\mathcal F}(x)\ge E_{\mathcal F}(x)\ge G_{\mathcal F}(x).
```

The same fidelity-resource lower bound applies to every minimized sandwiched Rényi divergence of order at least $`1/2`$. In magic theory, $`E_{\mathrm{STAB}}`$ is relative entropy of magic and $`M_{\mathrm{STAB}}`$ is logarithmic generalized robustness, with multiplicative robustness defined by
$`\Lambda^+(x)=\min\{\lambda:x\le\lambda\sigma,\ \sigma\in\mathrm{STAB}\}`$.

For a $`q`$-qubit catalyst the maximally mixed state is free, so

```math
F_{\mathrm{STAB}}(\tau)\ge
F(\tau,I/2^q)=\frac{(\mathrm{Tr}\sqrt{\tau})^2}{2^q}
\ge2^{-q}.
```

Therefore $`q\ge G_{\mathrm{STAB}}(\tau)`$. This dimension implication uses the magic free set and its free maximally mixed state.

## A stronger direct bound for max-relative entropy and qubits

The comparison state $`\Xi_\ell`$ from the converse also gives a direct operator bound when $`M_{\mathcal F}(\tau)`$ is finite, as it is for every finite-qubit magic catalyst. If $`\tau\le2^m\sigma_C`$ with free $`\sigma_C`$, then

```math
\Xi_\ell\le2^m\Phi_\ell(\sigma_C),
\qquad
\mathrm{Tr}(\Pi_\ell\Xi_\ell)\le2^m f_\ell.
```

Combining this with the failure-probability comparison and optimizing $`m`$ gives

```math
\boxed{
\ell\varepsilon\ge
p^{k\ell}\left(1-2^{M_{\mathcal F}(\tau)}f_\ell\right).
}
```

A negative right side is uninformative. Equivalently, whenever
$`\delta_\ell=\ell\varepsilon p^{-k\ell}<1`$,

```math
M_{\mathcal F}(\tau)\ge
-\log_2 f_\ell+\log_2(1-\delta_\ell).
```

For magic catalysts, $`\tau\le I=2^q(I/2^q)`$ implies
$`M_{\mathrm{STAB}}(\tau)\le q`$. Hence a budget $`q\le m`$, or a budget $`M_{\mathcal F}(\tau)\le m`$, obeys

```math
\varepsilon\ge
\sup_{\ell\ge1}\frac{p^{k\ell}}{\ell}
(1-2^m f_\ell)_+.
```

Under $`f_\ell\le2^{-a\ell}`$, setting
$`\ell_m=\lceil(m+1)/a\rceil`$ gives
$`\varepsilon\ge p^{k\ell_m}/(2\ell_m)`$.

For an explicit precision coefficient let $`B=kb>0`$ and choose

```math
\ell=
\left\lfloor
\frac{L-\log_2L+\log_2(B/2)}{B}
\right\rfloor.
```

For sufficiently large $`L`$, this is positive, $`\ell\le L/B`$ and
$`\delta_\ell\le1/2`$. Consequently,

```math
\boxed{
M_{\mathcal F}(\tau),\ q
\ge\frac aB(L-\log_2L)
+\frac aB\log_2(B/2)-a-1.
}
```

The $`q`$ bound is specific to a qubit catalyst. This stronger coefficient applies to max-relative entropy and qubits; the proved relative-entropy coefficient remains the one obtained from $`G_{\mathcal F}`$. Neither coefficient is claimed optimal. For $`p=1`$, use the finite bounds rather than an expression dividing by $`b`$.

## Matching orders for sufficiently low-noise CCZ

The [explicit construction](cyclic_construction.md) fixes

```math
\rho_\nu=(1-\nu)\Psi_{\mathrm{CCZ}}+\nu I_8/8
```

with a sufficiently small, fixed $`\nu>0`$. It gives an integer $`K_*`$, independent of accuracy, such that every fixed $`k\ge K_*`$ admits exact-return catalytic distillation with

```math
q=O(\log(1/\varepsilon)).
```

It also has $`G_{\mathrm{STAB}}(\tau)\le q`$,
$`E_{\mathrm{STAB}}(\tau)\le q`$ and
$`M_{\mathrm{STAB}}(\tau)\le q`$. The source has free weight at least $`\nu`$ and the target satisfies $`f_\ell=(9/16)^\ell`$. The converses therefore match the upper-bound order.

More precisely, taking infima over all admissible factories at the prescribed error, separately for each cost, gives

```math
q_{\mathrm{opt}},\quad
G_{\mathrm{opt}},\quad
E_{\mathrm{opt}},\quad
M_{\mathrm{opt}}
=\Theta(\log(1/\varepsilon))
```

for these fixed sources and fixed $`k\ge K_*`$. The infima need not have the same optimizer. The assertion concerns the asymptotic order, not matching leading constants. An upper bound at every smaller fixed $`k`$ is not established.

## Preparation cost has a different provenance

Suppose a deterministic free preparation uses $`N_{\mathrm{init}}`$ copies of the same source to produce $`\tau`$. Product free comparison states give fidelity supermultiplicativity, hence subadditivity of $`G_{\mathcal F}`$. Therefore

```math
G_{\mathcal F}(\tau)
\le G_{\mathcal F}(\rho^{\otimes N_{\mathrm{init}}})
\le N_{\mathrm{init}}G_{\mathcal F}(\rho).
```

For a nonfree fixed source this implies a logarithmic initialization lower bound. A simpler bound already follows from ordinary purification: compose initialization and the first $`k`$-input use, then discard the catalyst. The [established free-component argument](../references/RELATED_WORK.md#fangliu2022) gives

```math
\varepsilon\ge
p^{N_{\mathrm{init}}+k}(1-f_1).
```

For $`0<p<1`$,

```math
N_{\mathrm{init}}\ge
\frac{\log_2(1/\varepsilon)+\log_2(1-f_1)}
{\log_2(1/p)}-k.
```

This startup lower bound does not require exact catalyst return. It is inherited from ordinary purification. The additional catalytic conclusion is that the prepared factory must retain diverging magic in the returned catalyst. The CCZ construction supplies matching logarithmic source-only initialization using a fixed worst-case budget.
