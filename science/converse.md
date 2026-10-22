# Converse bounds for stationary catalytic magic factories

The [model](model.md) permits arbitrary mixed catalysts, exact return of only their marginal, and unrestricted correlations among the catalyst and emitted states. This document proves a finite bound on the initial relative entropy of magic, derives its logarithmic asymptotic consequence, and gives a positive error floor for a fixed finite catalyst.

The channel is deterministic and completely stabilizer preserving. Every new source block is independent of the past. The same channel and designated catalyst marginal are used at every call.

## 1. Notation and statement

Let $\chi_A$ be the fixed fresh source block, $\tau_C$ the complete persistent state, and
$\Lambda_{AC\to BC}$ a channel satisfying

$$
\operatorname{Tr}_B\Lambda(\chi_A\otimes\tau_C)=\tau_C,
\qquad
\operatorname{Tr}\!\left[
\psi_B\,\operatorname{Tr}_C\Lambda(\chi_A\otimes\tau_C)
\right]\ge1-\varepsilon,
\tag{1}
$$

where $\psi_B=|\psi\rangle\langle\psi|$ is pure. Suppose that

$$
\chi_A\succeq w\,\sigma_{0,A},
\qquad
\sigma_{0,A}\in\operatorname{STAB}(A),
\qquad
0<w\le1.
\tag{2}
$$

Write

$$
R=E_R(\tau_C),
\qquad
b_L=\max_{\sigma\in\operatorname{STAB}(B^L)}
\operatorname{Tr}(\psi^{\otimes L}\sigma),
\qquad
\delta_L=L\varepsilon w^{-L}.
\tag{3}
$$

For finite qubit registers, $b_L>0$ because the maximally mixed state is free. For a nonstabilizer pure target, $b_L<1$: otherwise a free state would equal $\psi^{\otimes L}$, whose single-copy marginal would make $\psi$ free. We assume this nontrivial case below.

The binary entropy and binary relative entropy are

$$
h_2(u)=-u\log_2u-(1-u)\log_2(1-u),
$$

$$
d_2(s\Vert t)
=s\log_2\frac{s}{t}
 +(1-s)\log_2\frac{1-s}{1-t},
\tag{4}
$$

with their continuous endpoint conventions.

### Theorem 1: finite catalyst-resource bound

For every positive integer $L$:

1. If $1-\delta_L\ge b_L$, then

   $$
   \boxed{R\ge d_2(1-\delta_L\Vert b_L).}
   \tag{5}
   $$

2. If $\delta_L\le1/2$, then

   $$
   \boxed{
   R\ge
   (1-\delta_L)\log_2\frac1{b_L}
   -h_2(\delta_L).
   }
   \tag{6}
   $$

Suppose, additionally, that a fixed $f\in(0,1)$ satisfies $b_L\le f^L$ for every $L$, and put $c=\log_2(1/f)$. Then (6) implies

$$
\boxed{
R\ge (1-\delta_L)Lc-h_2(\delta_L),
\qquad
\delta_L\le\frac12.
}
\tag{7}
$$

When $1-\delta_L\ge f^L$, (5) also gives the explicitly evaluable bound

$$
R\ge d_2(1-\delta_L\Vert f^L).
\tag{8}
$$

The hypotheses of (5) and (6) differ. In particular, (6) remains valid if $1-\delta_L<b_L$, although its right-hand side may then be uninformative. One may always combine any displayed lower bound with $R\ge0$.

## 2. Sequential reuse preserves every nominal output guarantee

Start from $\chi_{A_1}\otimes\cdots\otimes\chi_{A_L}\otimes\tau_C$. Apply $\Lambda$ in order to $A_1C,\ldots,A_LC$, keeping all previous output registers. Let
$\widehat\Omega^{\mathrm{nom}}_{B_1\cdots B_LC}$
be the resulting joint state and let
$\Omega^{\mathrm{nom}}_L=\operatorname{Tr}_C\widehat\Omega^{\mathrm{nom}}$.

We first show inductively that, immediately after every call, the marginal on $C$ is $\tau_C$. It holds initially by construction. If it holds after call $i-1$, the untouched fresh register $A_i$ is independent of the entire past. Thus its reduced joint state with $C$ is exactly $\chi_A\otimes\tau_C$. Applying (1) gives the same returned marginal $\tau_C$ and an output $B_i$ with infidelity at most $\varepsilon$.

This argument uses only the reduced state on $A_iC$. It remains valid when $C$ is correlated with $B_1,\ldots,B_{i-1}$. Subsequent trace-preserving operations act outside $B_i$, so they leave its marginal unchanged. At the end,

$$
\operatorname{Tr}\!\left(\psi_{B_i}
\,\Omega^{\mathrm{nom}}_{L,B_i}\right)\ge1-\varepsilon
\quad\text{for every }i.
\tag{9}
$$

The same reuse property is explicit in [FL2026](../references/related-work.md#fl2026); the argument above gives the precise version needed here.

Let $P_L=\psi^{\otimes L}$. The single-register target projectors commute. Their elementary operator union bound is

$$
I-P_L
\preceq
\sum_{i=1}^L
I_{B_1\cdots B_{i-1}}\otimes(I_{B_i}-\psi_{B_i})
\otimes I_{B_{i+1}\cdots B_L}.
\tag{10}
$$

Taking the expectation in the nominal output and using (9) yields

$$
\operatorname{Tr}\!\left[(I-P_L)\Omega^{\mathrm{nom}}_L\right]
\le L\varepsilon.
\tag{11}
$$

No statistical independence of the outputs has been assumed.

## 3. Replace fresh inputs by free states in a comparison experiment

Let $\mathcal K_L$ denote the complete sequential channel from
$A_1\cdots A_LC$ to $B_1\cdots B_L$, including the final trace over $C$.
Keep this channel fixed and define

$$
\Omega^{\mathrm{free}}_L
=\mathcal K_L(\sigma_0^{\otimes L}\otimes\tau_C).
\tag{12}
$$

The superscript indicates that every fresh input in this comparison experiment is free. It does not assert that the output is free: the initial $\tau_C$ can contain magic.

Tensoring (2) gives

$$
\chi^{\otimes L}\otimes\tau_C
\succeq
w^L\sigma_0^{\otimes L}\otimes\tau_C.
\tag{13}
$$

For $w<1$, this can also be seen by expanding
$\chi=w\sigma_0+(1-w)\eta$: the all-free tensor term has weight $w^L$, and every other term is positive. For $w=1$, (2) and normalization force $\chi=\sigma_0$, so (13) is an equality.

Since $\mathcal K_L$ is positive and linear,

$$
\Omega^{\mathrm{nom}}_L\succeq w^L\Omega^{\mathrm{free}}_L.
\tag{14}
$$

Testing (14) with the positive failure projector $I-P_L$ and applying (11) gives

$$
1-\operatorname{Tr}(P_L\Omega^{\mathrm{free}}_L)
\le L\varepsilon w^{-L}
=\delta_L.
\tag{15}
$$

The comparison uses the same initial catalyst and the same physical sequence of channels. It does not assume that the catalyst marginal returns to $\tau_C$ in this comparison run. Such a return is unnecessary. Exact return on the nominal input was used only to obtain (9).

The source decomposition is an operator argument. No free component is heralded, selected, or made available as an extra protocol capability.

## 4. Only the initial catalyst supplies magic in the comparison run

The map

$$
\mathcal G_L(X_C)
=\mathcal K_L(\sigma_0^{\otimes L}\otimes X_C)
\tag{16}
$$

is completely stabilizer preserving. Indeed, appending free states is free; each application of $\Lambda$ preserves stabilizer states even with the old outputs retained as a reference; and discarding the final memory is free. These observations also explain why complete stabilizer preservation was specified in the model.

For any channel $\mathcal G$ mapping free states to free states, quantum relative-entropy data processing gives

$$
\begin{aligned}
E_R(\mathcal G(\rho))
&\le D(\mathcal G(\rho)\Vert\mathcal G(\sigma))\\
&\le D(\rho\Vert\sigma)
\qquad\text{for every free }\sigma.
\end{aligned}
$$

Taking the minimum over $\sigma$ proves monotonicity. Applying it to (16),

$$
R=E_R(\tau_C)
\ge E_R(\Omega^{\mathrm{free}}_L).
\tag{17}
$$

There is no invocation of
$E_R(\tau\otimes\psi)=E_R(\tau)+E_R(\psi)$,
nor of any other additivity property involving the arbitrary catalyst.

## 5. A binary measurement proves the finite bounds

Set

$$
s=\operatorname{Tr}(P_L\Omega^{\mathrm{free}}_L).
$$

Equation (15) gives $s\ge1-\delta_L$. For any free comparison state
$\sigma\in\operatorname{STAB}(B^L)$, let
$t=\operatorname{Tr}(P_L\sigma)$. By definition, $t\le b_L$.

Apply the measurement $\{P_L,I-P_L\}$ to both states. Relative-entropy data processing implies

$$
D(\Omega^{\mathrm{free}}_L\Vert\sigma)
\ge d_2(s\Vert t).
\tag{18}
$$

This measurement is a mathematical test used in the proof. It is not required to be a free operation implemented by the factory.

### Binary-relative-entropy form

Assume $1-\delta_L\ge b_L$. Then
$s\ge1-\delta_L\ge b_L\ge t$.
For $s\ge t$, the function $d_2(s\Vert t)$ increases with $s$ and decreases with $t$. In the interior, this follows from

$$
\frac{\partial}{\partial s}d_2(s\Vert t)
=\log_2\frac{s(1-t)}{t(1-s)}\ge0,
$$

$$
\frac{\partial}{\partial t}d_2(s\Vert t)
=\frac{t-s}{(\ln2)t(1-t)}\le0.
$$

The endpoint cases follow by continuity, with an infinite divergence handled in the usual way. Thus

$$
d_2(s\Vert t)
\ge d_2(1-\delta_L\Vert b_L).
$$

Combine this with (18), minimize over free $\sigma$, and use (17) to obtain (5). If $b_L\le f^L\le1-\delta_L$, the same monotonicity in the second argument gives (8).

### Entropy form

For any $s,t\in[0,1]$ with the usual endpoint conventions,

$$
\begin{aligned}
d_2(s\Vert t)
&=s\log_2\frac1t
 +(1-s)\log_2\frac1{1-t}
 -h_2(s)\\
&\ge s\log_2\frac1t-h_2(s).
\end{aligned}
\tag{19}
$$

Assume $\delta_L\le1/2$. Because $1-s\le\delta_L$, the symmetry and monotonicity of binary entropy on $[0,1/2]$ imply

$$
h_2(s)=h_2(1-s)\le h_2(\delta_L).
$$

Also $s\ge1-\delta_L$ and $t\le b_L$. Hence (19) gives

$$
d_2(s\Vert t)
\ge(1-\delta_L)\log_2\frac1{b_L}
-h_2(\delta_L).
$$

Using (18) and (17) proves (6). Finally,
$b_L\le f^L$ implies $\log_2(1/b_L)\ge Lc$, proving (7).

This completes the finite theorem, including the exponential-overlap specialization. The only target-specific input for computational $T$ and CCZ is the known tensor-power overlap identity from [B2019](../references/related-work.md#b2019).

### Finite-horizon lemma

Fix a positive integer $L$. Suppose a deterministic completely stabilizer-preserving protocol $\Phi_L$ starts with
$\chi^{\otimes L}\otimes\tau_0$, where the fresh blocks are independent and satisfy (2), and produces $L$ target registers. Suppose every final nominal output marginal has infidelity at most $\varepsilon$. The protocol may have an evolving controller and need not return any catalyst state.

Then the finite bounds (5)–(8) hold with $R=E_R(\tau_0)$ and
$\delta_L=L\varepsilon w^{-L}$, under their respective conditions. All initially supplied nonfree auxiliary states must be included in $\tau_0$.

**Proof.** The assumed marginal guarantees give (11) by the projector union bound. Positivity of $\Phi_L$ applied to the tensor domination (13) gives (14)–(15). With all fresh blocks replaced by $\sigma_0$, the resulting map from $\tau_0$ to the outputs is free, so (17) follows. The binary test in Section 5 then proves the same bounds. No return condition occurs in these steps. $\square$

Exact stationarity in the headline theorem supplies the marginal guarantees for every $L$ using the same initial catalyst. The finite-horizon lemma instead takes those guarantees as a premise for one specified horizon. It does not establish that a small one-call catalyst disturbance preserves later accuracy, and it implies no unlimited-reuse claim for an approximately returned catalyst.

## 6. Optimize the number of repetitions

Every admissible positive integer $L$ gives a valid inequality for the same initial catalyst. Therefore one may maximize the applicable right-hand sides of (5)–(8) over integers $L$, taking zero as the default lower bound when no nontrivial value is available.

For the asymptotic law, fix $w\in(0,1)$ and $f\in(0,1)$ and define

$$
a=\ln(1/w)>0,
\qquad
c=\log_2(1/f)>0,
\qquad
x=\ln(1/\varepsilon).
\tag{20}
$$

For sufficiently small positive $\varepsilon$, choose

$$
L_\varepsilon=
\left\lfloor\frac{x-2\ln x}{a}\right\rfloor.
\tag{21}
$$

For example, the following derivation applies whenever
$x\ge1$, $x-2\ln x\ge a$, and $ax\ge2$. These conditions ensure
$L_\varepsilon\ge1$ and the error estimates below lie in their stated range.
The floor in (21) gives

$$
e^{aL_\varepsilon}\le e^x/x^2,
\qquad
L_\varepsilon\le x/a,
$$

and therefore

$$
\delta_{L_\varepsilon}
=L_\varepsilon e^{-x+aL_\varepsilon}
\le\frac{L_\varepsilon}{x^2}
\le\frac1{ax}\le\frac12.
\tag{22}
$$

Moreover,

$$
L_\varepsilon\delta_{L_\varepsilon}\le\frac1{a^2},
\qquad
L_\varepsilon\ge\frac{x-2\ln x}{a}-1.
$$

Substituting these estimates in (7) gives an explicit bound:

$$
\boxed{
R\ge
\frac ca(x-2\ln x)
-c-\frac c{a^2}
-h_2\!\left(\frac1{ax}\right).
}
\tag{23}
$$

In particular, for any family of stationary factories with the same positive domination weight $w$ and the same target-overlap constant $f$,

$$
E_R(\tau_\varepsilon)
\ge
\frac ca\ln\frac1\varepsilon
-O\!\left(\ln\ln\frac1\varepsilon\right),
\tag{24}
$$

$$
\boxed{
\liminf_{\varepsilon\downarrow0}
\frac{E_R(\tau_\varepsilon)}{\ln(1/\varepsilon)}
\ge
\frac{\log_2(1/f)}{\ln(1/w)}.
}
\tag{25}
$$

The constants in the remainder depend on the fixed $a,c$. The channel, catalyst, and catalyst dimension may vary with $\varepsilon$.

The choice (21) attains the leading coefficient available from the specialized entropy bound (7). Indeed, for positive $\varepsilon$, its admissibility condition implies
$aL+\ln L\le x-\ln2$, and hence $L\le x/a$; the right-hand side of (7) is at most $cL$. This observation concerns optimization of the proved bound. It does not assert that the coefficient $c/a$ is the optimal physical memory constant.

### Fixed fresh-copy count

If $\chi=\rho^{\otimes n}$ and $\rho\succeq p\sigma_{\mathrm{free}}$ with fixed $n$ and $p\in(0,1)$, one may take $w=p^n$. Equations (24)–(25) become

$$
E_R(\tau_\varepsilon)
\ge
\frac{\log_2(1/f)}{n\ln(1/p)}
\ln\frac1\varepsilon
-O\!\left(\ln\ln\frac1\varepsilon\right).
\tag{26}
$$

Thus the stored magic diverges logarithmically at every fixed finite fresh-input budget. This is not a uniform expansion for arbitrary $n=n(\varepsilon)$ or changing source noise. Those cases retain the finite theorem with their actual $w$.

The finite theorem also permits $w=1$. In that case the source is free, $a=0$, and (20)–(26) must not be used. Equations (5)–(8) remain valid with $\delta_L=L\varepsilon$.

## 7. An explicit error floor

Assume the exponential target-overlap condition, let $R=E_R(\tau)<\infty$, and define

$$
L_R=\left\lfloor\frac{2(R+1)}c\right\rfloor+1.
\tag{27}
$$

### Corollary 2: fixed-resource error floor

Every stationary factory in the model satisfies

$$
\boxed{
\varepsilon>\frac{w^{L_R}}{2L_R}.
}
\tag{28}
$$

**Proof.** If instead $\varepsilon\le w^{L_R}/(2L_R)$, then
$\delta_{L_R}\le1/2$. Equation (7) and $h_2(\delta_{L_R})\le1$ give

$$
R\ge\frac{L_Rc}{2}-1.
$$

By construction $L_R>2(R+1)/c$, so the right-hand side is strictly greater than $R$, a contradiction. Equality in the assumed error bound would also lead to the contradiction, which explains the strict inequality in (28). $\square$

This is a closed-form sufficient error floor, not a claim of finite-error optimality. Direct optimization of the binary bound can be stronger.

At $\varepsilon=0$, one can also read the impossibility directly from (7): $\delta_L=0$ for every $L$, so $R\ge Lc$ for all positive integers. No finite-resource catalyst can satisfy this. The argument includes pure and rank-deficient catalysts; their relative entropy of magic is still finite in any finite qubit register.

## 8. Consequences for quantum memory

For a $q$-qubit catalyst, comparison with the maximally mixed free state gives
$R\le q$. For a complete classical–quantum catalyst with $q$ quantum qubits and an arbitrarily large finite classical register, the stronger accounting identity proved in the [model](model.md#arbitrarily-large-classical-storage) also gives $R\le q$.

Consequently every finite lower bound above is also a lower bound on $q$. In particular, with fixed $w\in(0,1)$ and $f\in(0,1)$,

$$
\liminf_{\varepsilon\downarrow0}
\frac{q_\varepsilon}{\ln(1/\varepsilon)}
\ge
\frac{\log_2(1/f)}{\ln(1/w)}.
\tag{29}
$$

For a directly stated qubit error floor, set

$$
L_q=\left\lfloor\frac{2(q+1)}c\right\rfloor+1.
$$

The same contradiction proof, using $R\le q$, yields

$$
\boxed{
\varepsilon>\frac{w^{L_q}}{2L_q}.
}
\tag{30}
$$

An unlimited supply of free classical labels cannot evade this conclusion. The count concerns the complete persistent quantum state, with all coherently stored control information included.

## 9. Interpretation and boundaries

Every nominal call leaves the catalyst's marginal unchanged, so the device can emit a long sequence with individually accurate marginals. A length-$L$ sequence also has joint target overlap at least $1-L\varepsilon$. The positive free component of each source block then forces a closely related sequence in which all fresh blocks are free to have joint failure probability at most $L\varepsilon/w^L$.

In this comparison sequence, only the initial catalyst can supply magic. The target tensor product is exponentially unlikely under every free state. Relative-entropy data processing turns that distinguishability into a lower bound on the catalyst's original magic. Choosing $L$ of order $\ln(1/\varepsilon)$ makes the required stored resource grow at the same order.

Several features of the proof are essential:

- Exact return is required only for the nominal source. The free-input comparison may consume or alter the catalyst completely.
- The catalyst need not be pure, and no output–catalyst or inter-output product structure is used.
- The resource comparison does not require the source block to contain less magic than one target. There is no source–target Rényi resource-gap hypothesis of the kind used in [RT2022](../references/related-work.md#rt2022).
- The target-overlap bound concerns tensor powers of the target, not a tensor product with an arbitrary catalyst.
- The factory is deterministic. A catalyst returned only upon a heralded success cannot be inserted into this unconditional repetition proof.
- The block domination weight must remain positive. A fixed-weight asymptotic law does not automatically cover increasingly pure sources or increasing fresh-input budgets.
- Approximate return, source blocks correlated across calls, external feedback that is not included in the persistent state, and extra magic supplies are not covered by the stated theorem.

The consequence is a resource law for exact reusable storage under ideal free operations. It establishes no physical noise threshold, gate-count optimum, latency guarantee, or fault-tolerant hardware estimate. Matching an upper bound in logarithmic order requires a separate construction with the same source, allowed operations, return convention, and charged resources.
