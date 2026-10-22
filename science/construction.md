# A matching construction for CCZ distillation

A deterministic catalytic CCZ factory can consume a fixed number of fresh noisy states per output while using $`O(\log(1/\epsilon))`$ catalyst qubits. The construction below combines the batch distillation protocol of [WHY2025](../references/related-work.md#why2025) with the catalytic conversion of [FL2026](../references/related-work.md#fl2026). It makes the memory scaling, initialization, and error convention explicit.

The construction assumes ideal stabilizer operations, arbitrary classical control and classical randomness, and independent fresh copies of one fixed noisy source. The catalyst is mixed and may become correlated with emitted outputs. Its complete marginal, including a classical phase register, returns exactly after every call. The [resource accounting](resources.md) distinguishes this statement from a bound on physical fault-tolerant hardware or execution time.

## 1. Source, target, and statement

Let

```math
|\psi\rangle=|CCZ\rangle=CCZ|+\rangle^{\otimes 3},
\qquad
\psi=|\psi\rangle\langle\psi|.
```

Fix a depolarizing mixture parameter $`\lambda>0`$ and supply independent copies of

```math
\rho_\lambda=(1-\lambda)\psi+\lambda\frac{I_8}{8}.
```

The source infidelity is

```math
p=1-\mathrm{Tr}(\psi\rho_\lambda)=\frac{7\lambda}{8}.
```

Thus $`p`$ is the probability of a nontrivial error in the orthogonal CCZ basis; it is not the depolarizing mixture parameter $`\lambda`$. Indeed, with $`Z^{\mathbf b}=Z^{b_1}\otimes Z^{b_2}\otimes Z^{b_3}`$,

```math
\rho_\lambda
=(1-p)\psi+
\frac{\lambda}{8}
\sum_{\mathbf b\in\{0,1\}^3\setminus\{\mathbf 0\}}
Z^{\mathbf b}\psi Z^{\mathbf b}.
```

The eight states $`Z^{\mathbf b}|\psi\rangle`$ form an orthonormal basis. This representation places the independent source directly within the local stochastic input model used in [WHY2025], §2.4 and §4.2.

**Upper-bound statement.** Let $`C`$ be the fixed CCZ conversion cost defined below, and suppose

```math
0<p<p_*,
\qquad
p_*=\frac{1}{236eC}.
```

There is one fixed integer

```math
r_0=24C
```

such that, for every $`0<\epsilon<1`$, a deterministic stabilizer channel $`\Lambda_\epsilon`$ and a catalyst $`\tau_\epsilon`$ satisfy

```math
\Lambda_\epsilon
\left(\rho_\lambda^{\otimes r_0}\otimes\tau_\epsilon\right)
=\omega_{SA},
\qquad
\omega_A=\tau_\epsilon,
\qquad
1-\mathrm{Tr}(\psi\omega_S)\le\epsilon.
```

The catalyst uses $`q=O(1+\log(1/\epsilon))`$ quantum qubits and $`b=O(1+\log\log(1/\epsilon))`$ classical bits as $`\epsilon`$ becomes small. The precise finite bounds below avoid the interpretation of the latter expression near $`\epsilon=1`$. Preparing the catalyst consumes $`O(1+\log(1/\epsilon))`$ additional copies of the same source, once at initialization.

The upper bound holds for this particular constant input budget and for any larger fixed budget by discarding extra inputs. It does not assert feasibility for every smaller input budget.

## 2. The inherited batch protocol

### Conversion cost

[WHY2025], §4.4, represents a $`1024`$-dimensional qudit by ten qubits. Its diagonal non-Clifford gate $`\theta(U_1^{(7)})`$ has a decomposition into $`Z`$, $`CZ`$, and $`CCZ`$ gates. Define $`C`$ to be the integer number of $`CCZ`$ gates in one fixed such decomposition.

Each $`CCZ`$ gate can be supplied by a CCZ magic state and stabilizer operations. Hence $`C`$ source states prepare one noisy ten-qubit magic state. The inverse conversion extracts one CCZ state from each distilled ten-qubit state by Pauli measurements and conditional Clifford corrections, for every measurement outcome. No extra magic seed is needed. The decomposition has $`1\le C\le120`$; Appendix B supplies an explicit choice with $`C=70`$.

Fixing that choice gives the concrete witness

```math
C=70,
\qquad
r_0=1680,
\qquad
p_*=\frac{1}{16520e}\approx2.22687\times10^{-5}.
```

Equivalently, the sufficient condition on the mixture parameter is

```math
0<\lambda<\frac{8}{7\cdot236eC}
\approx2.54500\times10^{-5}.
```

These constants are sufficient bounds for an existence proof. They are not optimized thresholds or practical resource estimates.

### Code parameters

Use $`N`$ for the number of code qudits, $`M`$ for the number of output CCZ states, $`t`$ for the guaranteed decoding radius, and $`K`$ for the number of noisy input CCZ states. This renames the code parameters denoted $`n,k,t`$ in [WHY2025].

For the genus-$`g`$ construction in [WHY2025], §5.3, Eqs. (274)–(286),

```math
\left\lfloor\frac{114g}{4}\right\rfloor-3
\le N
\le
\left\lfloor\frac{118g}{4}\right\rfloor-1,
\qquad
M=\left\lfloor\frac{5g}{4}\right\rfloor,
\qquad
t=\left\lfloor\frac{g}{8}\right\rfloor.
```

The associated deterministic batch channel $`\mathcal B_g`$ consumes

```math
K=CN
```

source states and produces $`M`$ CCZ output registers:

```math
\eta_M=\mathcal B_g(\rho_\lambda^{\otimes K}).
```

The outputs need not be independent. A decoder that does not correct a particular error pattern still returns an output, so the map is trace preserving and there is no heralded failure branch. These properties are part of [WHY2025], Theorem 6.1.

## 3. A global exponential error bound

Each ten-qubit input to the code is prepared from a disjoint group of $`C`$ noisy source states. The probability that a specified preparation group contains a fault is at most $`Cp`$. For any specified set of $`s`$ groups, the probability that all those groups contain faults is at most $`(Cp)^s`$. The input model and free twirling used by [WHY2025] make the resulting errors correctable whenever at most $`t`$ groups are faulty.

Let $`F`$ be the set of faulty groups. A union bound over subsets of size $`t+1`$ gives

```math
\Pr\{|F|\ge t+1\}
\le
\sum_{\substack{S\subseteq\{1,\ldots,N\}\\|S|=t+1}}
\Pr\{S\subseteq F\}
\le
\binom{N}{t+1}(Cp)^{t+1}.
```

On every correctable error pattern, the whole ideal output is $`\psi^{\otimes M}`$. Therefore this bounds the **global batch infidelity**:

```math
\epsilon_g
:=
1-\mathrm{Tr}(\psi^{\otimes M}\eta_M)
\le
\binom{N}{t+1}(Cp)^{t+1}.
\tag{1}
```

This is the bound proved in [WHY2025], Eqs. (301)–(305). It is stronger than a separate error bound on each output and does not require an additional factor of $`M`$ here.

For an explicit conservative exponent, set $`s=t+1`$. The rounding inequalities give

```math
s\ge\frac g8,
\qquad
N\le\frac{59g}{2}-1,
\qquad
\frac Ns\le236.
```

Using $`\binom Ns\le(eN/s)^s`$ in (1),

```math
\epsilon_g
\le(236eCp)^s
\le(236eCp)^{g/8}
=e^{-\beta g},
\qquad
\beta:=\frac18\ln\frac{1}{236eCp}>0.
\tag{2}
```

The condition $`p<p_*`$ is precisely what makes $`\beta`$ positive. This is an exponential upper bound with a fixed positive exponent at every fixed permitted source state.

For each marginal $`\eta_j`$ of $`\eta_M`$,

```math
1-\mathrm{Tr}(\psi\eta_j)
\le
1-\mathrm{Tr}(\psi^{\otimes M}\eta_M)
\le\epsilon_g.
\tag{3}
```

The first inequality follows from

```math
\psi^{\otimes M}
\le
I^{\otimes(j-1)}\otimes\psi\otimes I^{\otimes(M-j)}.
```

This step remains valid for arbitrarily correlated batch outputs.

## 4. One fixed fresh-input budget

The catalytic construction needs $`M`$ blocks of a common size. Set

```math
r=r_0=24C,
\qquad
\zeta=\rho_\lambda^{\otimes r}.
```

For $`g\ge46`$,

```math
24M
\ge30g-24
\ge\frac{59g}{2}-1
\ge N.
```

Consequently $`rM\ge CN=K`$. A channel on $`M`$ input blocks can discard exactly $`rM-K`$ source states and run $`\mathcal B_g`$ on the remaining $`K`$.

Every genus used below is at least $`g_3=32705`$, so the integer and rounding condition is satisfied throughout the family. The number $`r`$ is fixed before choosing $`\epsilon`$; it does not vary with the batch length.

Let $`\pi`$ be any free three-qubit state, for example $`|000\rangle\langle000|`$, and define the padding channel

```math
\mathcal E(X)=X\otimes\pi^{\otimes(r-1)}.
```

One padded output now occupies the same $`3r`$-qubit block as $`\zeta`$. Define

```math
\widehat\eta_M=\mathcal E^{\otimes M}(\eta_M).
```

There is a deterministic stabilizer channel $`\widehat{\mathcal B}_g`$ on $`M`$ blocks such that

```math
\widehat{\mathcal B}_g(\zeta^{\otimes M})
=\widehat\eta_M.
\tag{4}
```

Discarding excess noisy inputs, running the batch, and adjoining free padding are all included in this channel.

## 5. The catalyst and its exact return

The following cyclic construction is [FL2026], Theorem 3 and Methods §4.1, Eqs. (6)–(13), specialized to a deterministic batch and to the fixed block size $`r`$.

For $`0\le s\le M`$, write

```math
\widehat\eta_{1:s}
:=
\mathrm{Tr}_{s+1,\ldots,M}(\widehat\eta_M),
\qquad
\widehat\eta_{1:0}:=1.
```

The catalyst has $`M-1`$ quantum blocks and a classical register $`F`$ with values $`1,\ldots,M`$:

```math
\tau_g
=
\frac1M\sum_{i=1}^{M}
\zeta^{\otimes(i-1)}
\otimes
\widehat\eta_{1:M-i}
\otimes |i\rangle\langle i|_F.
\tag{5}
```

The total number of quantum blocks in every summand is $`M-1`$. The state $`\widehat\eta_{1:M-i}`$ is an actual marginal of the possibly correlated batch output, not a product of marginal states or an ideal target.

### One call

Place one fresh block $`\zeta`$ to the left of the catalyst's quantum blocks. The joint input is

```math
\frac1M\sum_{i=1}^{M}
\zeta^{\otimes i}
\otimes
\widehat\eta_{1:M-i}
\otimes |i\rangle\langle i|_F.
```

Conditioned on the classical flag:

1. If $`i<M`$, leave the quantum blocks unchanged.
2. If $`i=M`$, apply $`\widehat{\mathcal B}_g`$ to the $`M`$ blocks.
3. Replace the flag $`i`$ by $`i+1`$, with $`M`$ replaced by $`1`$.
4. Emit the last quantum block, remove its free padding, and retain the first $`M-1`$ blocks and the flag as the catalyst.

All branches are trace preserving. The flag update is a classical computation on a measured classical register; no coherent non-Clifford arithmetic operation is assumed to be free.

### Joint state after the flag update

Using (4) and relabeling the summation index gives the exact pre-emission state

```math
\Omega_g
=
\frac1M\sum_{j=1}^{M}
\zeta^{\otimes(j-1)}
\otimes
\widehat\eta_{1:M-j+1}
\otimes |j\rangle\langle j|_F.
\tag{6}
```

For $`j=1`$, this is the freshly distilled batch. For $`j>1`$, it is the branch that previously had flag $`j-1`$. There is always at least one batch-output block at the right end.

Tracing out the last quantum block in (6) gives

```math
\mathrm{Tr}_{\mathrm{last}}\Omega_g
=
\frac1M\sum_{j=1}^{M}
\zeta^{\otimes(j-1)}
\otimes
\widehat\eta_{1:M-j}
\otimes |j\rangle\langle j|_F
=\tau_g.
\tag{7}
```

The identity uses only consistency of partial traces. It makes no symmetry or independence assumption about $`\eta_M`$.

After removing padding, the emitted state is

```math
\omega_S
=
\frac1M\sum_{s=1}^{M}\eta_s.
\tag{8}
```

Combining (3) and linearity of overlap with a pure target,

```math
1-\mathrm{Tr}(\psi\omega_S)
=
\frac1M\sum_{s=1}^{M}
\left[1-\mathrm{Tr}(\psi\eta_s)\right]
\le\epsilon_g.
\tag{9}
```

Thus the catalyst returns exactly and one fresh block produces one accurate output with certainty.

The classical phase advances in each realization. Equation (7) asserts return of the complete mixed density operator, including the phase and its correlations with the quantum buffer. It does not assert that each sampled component of (5) returns separately.

### Reuse

The next call supplies a new independent $`\zeta`$ and applies the same channel only to that input and the retained catalyst. Previous outputs can remain correlated with the catalyst. Their presence does not affect its reduced input state $`\tau_g`$, so the same marginal calculation applies on every call. This is the deterministic reuse guarantee of [FL2026], Theorem 4.

In particular, every emitted state has the error bound (9), and the catalyst marginal remains $`\tau_g`$ after any finite number of calls. This assertion concerns output marginals; it does not identify a long output stream with independent copies.

## 6. Choosing a batch for every target accuracy

An asymptotically good code family alone would not ensure $`O(\log(1/\epsilon))`$ memory for every small $`\epsilon`$: its available lengths might have large gaps. The explicit family in [WHY2025], Example 5.3.1, Eqs. (287)–(296), resolves this issue.

For each integer $`i\ge3`$, its genus is

```math
g_i=
\begin{cases}
33\,32^{i-1}-34\,32^{(i-1)/2}+1,
&i\ \text{odd},\\[2mm]
33\,32^{i-1}-561\,32^{i/2-1}+1,
&i\ \text{even}.
\end{cases}
\tag{10}
```

In particular, $`g_3=32705`$. These genera satisfy

```math
\frac{63}{2}\,32^{i-1}
\le g_i
\le33\,32^{i-1}
\qquad(i\ge3).
\tag{11}
```

For odd $`i`$, the coefficient subtracted from $`33\,32^{i-1}`$ is at most $`34/32=17/16<3/2`$. For even $`i`$, it is at most $`561/1024<3/2`$. The positive final $`1`$ only strengthens the lower bound; the total subtracted term exceeds $`1`$, giving the upper bound. Hence

```math
\frac{g_{i+1}}{g_i}
\le
\frac{33\cdot32}{63/2}
=\frac{704}{21}
<34.
\tag{12}
```

For a requested $`0<\epsilon<1`$, set

```math
G_\epsilon
:=
\max\left\{
g_3,\,
\frac{\ln(1/\epsilon)}{\beta}
\right\}
```

and choose the first $`i\ge3`$ with $`g_i\ge G_\epsilon`$. The sequence diverges, so this choice exists. If $`i>3`$, minimality gives $`g_{i-1}<G_\epsilon`$, and (12) yields $`g_i<34G_\epsilon`$. If $`i=3`$, the same upper bound is immediate. Thus

```math
G_\epsilon\le g_i\le34G_\epsilon,
\qquad
\epsilon_{g_i}\le e^{-\beta g_i}\le\epsilon.
\tag{13}
```

The catalyst in (5) has

```math
q=3r(M-1)
\le\frac{15r}{4}g_i
\le\frac{255r}{2}
\max\left\{
g_3,\,
\frac{\ln(1/\epsilon)}{\beta}
\right\},
\tag{14}
```

quantum qubits and

```math
b=\lceil\log_2 M\rceil
\le
\left\lceil
\log_2\left(\frac54\,34G_\epsilon\right)
\right\rceil
\tag{15}
```

classical phase bits. Equations (14) and (15) are finite bounds valid across the full family. At fixed source quality and fixed $`r`$, they imply the claimed logarithmic quantum memory and doubly logarithmic phase memory as $`\epsilon\to0`$.

## 7. Infidelity and trace distance

Throughout this page, error means pure-target infidelity

```math
e_\psi(\rho)=1-\mathrm{Tr}(\psi\rho).
```

[FL2026] states its catalytic theorem with trace distance. Equations (5)–(8) are exact state identities, so applying them directly gives the infidelity result (9) without changing the error parameter.

For a trace-distance requirement, define

```math
D_{\mathrm{tr}}(\rho,\psi)=\frac12\|\rho-\psi\|_1.
```

For a pure target,

```math
e_\psi(\rho)
\le D_{\mathrm{tr}}(\rho,\psi)
\le\sqrt{e_\psi(\rho)}.
```

Therefore the construction at infidelity $`\epsilon`$ guarantees trace distance at most $`\sqrt{\epsilon}`$. To guarantee trace distance at most $`\delta`$, use a batch with infidelity at most $`\delta^2`$. This replaces $`\ln(1/\epsilon)`$ by $`2\ln(1/\delta)`$ and preserves the logarithmic scaling. The two error parameters are not silently identified.

## 8. Relation to the lower bound

The source is full rank and satisfies

```math
\rho_\lambda\ge\lambda\frac{I_8}{8},
\qquad
\rho_\lambda^{\otimes r}
\ge\lambda^r
\left(\frac{I_8}{8}\right)^{\otimes r}.
```

Thus the same fixed source and input budget have free-domination weight $`w=\lambda^r`$. The target obeys

```math
\max_{\sigma\in\mathrm{STAB}}
\mathrm{Tr}(\psi^{\otimes L}\sigma)
=\left(\frac9{16}\right)^L
```

by [B2019](../references/related-work.md#b2019), Eq. (33), Theorem 5, Corollary 3, and the discussion following Eq. (108). This multiplicativity statement concerns CCZ tensor powers; it does not assume multiplicativity with an arbitrary catalyst.

The fixed-input lower bound therefore applies to exactly the class of factories constructed here. Together, the bounds give an optimal $`\Theta(\log(1/\epsilon))`$ catalyst quantum-memory law for this sufficiently clean fixed source and constant budget $`r=1680`$. The batch protocol and cyclic catalyst are inherited constructions; the upper bound establishes achievability in the same resource and error model.
