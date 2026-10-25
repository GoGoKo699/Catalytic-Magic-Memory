# Logarithmic catalyst size is achievable for CCZ distillation

The [factory model](model.md) and [resource lower bounds](resource_costs.md) specify the matching converse.

## Statement

Let


```math
\Psi=|\mathrm{CCZ}\rangle\langle\mathrm{CCZ}|,\qquad
|\mathrm{CCZ}\rangle=\mathrm{CCZ}|+\rangle^{\otimes3},
```


and fix a depolarized source


```math
\rho_\nu=(1-\nu)\Psi+\nu I_8/8,\qquad \nu>0.
\qquad\text{(1)}
```


There is a constant threshold $`\nu_*>0`$ such that, for every fixed $`0<\nu<\nu_*`$, there exists a fixed positive integer $`K`$ with the following property. For every sufficiently small $`\epsilon>0`$, a deterministic stabilizer protocol consumes exactly $`K`$ fresh copies of $`\rho_\nu`$, outputs a three-qubit state with infidelity at most $`\epsilon`$ to $`\Psi`$, and returns a catalyst $`\tau_\epsilon`$ exactly on its marginal. The catalyst has


```math
q_\epsilon=O(\log(1/\epsilon))
\qquad\text{(2)}
```


qubits, including its classical flag. It can itself be prepared exactly using stabilizer operations and $`O(\log(1/\epsilon))`$ copies of the same noisy source.

This is an achievability consequence of the deterministic batch construction of Wills–Hsieh–Yamasaki [1] and the cyclic catalyst construction of Fang–Liu [2]. The derivation below makes the input budget, flag implementation, error convention, and initialization cost explicit. It supplies the upper bound matching the catalyst-resource converse; it is not a new distillation-code construction.

The stabilizer model includes noiseless Clifford gates, computational-basis preparation and measurement, classical feed-forward, and discarding. It does not supply perfect nonstabilizer states.

## 1. The batch protocol and its error guarantee

Write $`n_j`$ for the number of physical $`2^{10}`$-dimensional qudits in the $`j`$-th code, $`r_j`$ for its logical dimension measured in qudits, and $`t_j`$ for its decoding radius. The CCZ conversion consumes $`C`$ noisy CCZ states per physical qudit, for one fixed integer $`C`$. Thus the actual input count is


```math
N_j=Cn_j.
\qquad\text{(3)}
```


The resulting stabilizer channel $`\mathcal D_j`$ maps $`N_j`$ noisy CCZ states to $`r_j`$ output CCZ registers. Denote its actual, generally correlated output by


```math
\eta^{(j)}=\mathcal D_j(\rho_\nu^{\otimes N_j}).
```


The required properties are


```math
r_j=\Theta(n_j),\qquad t_j=\Theta(n_j),
\qquad\text{(4)}
```


and, for sufficiently small fixed physical error probability $`s`$,


```math
1-\mathrm{Tr}\!\left(\Psi^{\otimes r_j}\eta^{(j)}\right)
\le
\binom{n_j}{t_j+1}(Cs)^{t_j+1}.
\qquad\text{(5)}
```


These are the deterministic batch guarantees in [1, Theorem 6.1 and Eqs. (301)–(305)]. The error is **global infidelity to the full pure target product**, as defined in [1, Eq. (114)]. A decoding outcome outside the guaranteed correction radius still produces an output; it is counted as a possible logical error. There is no accepted-event normalization or postselection.

### An explicit source-noise regime

The states $`Z^z|\mathrm{CCZ}\rangle`$, $`z\in\{0,1\}^3`$, form an orthonormal basis. Equation (1) can therefore be written


```math
\rho_\nu
=\left(1-\frac{7\nu}{8}\right)\Psi
+\frac{\nu}{8}\sum_{z\ne0}Z^z\Psi Z^z.
\qquad\text{(6)}
```


Independent copies of this state satisfy the local stochastic input-noise model with


```math
s=\frac{7\nu}{8}.
\qquad\text{(7)}
```


This is a special case of the noise model in [1, Section 2.4]. The source is full rank, and it also obeys the lower-bound hypothesis


```math
\rho_\nu\ge\nu I_8/8.
\qquad\text{(8)}
```


For a fixed $`\delta>0`$ such that $`t_j+1\ge\delta n_j`$, the elementary estimate


```math
\binom{n_j}{t_j+1}
\le
\left(\frac{e n_j}{t_j+1}\right)^{t_j+1}
```


implies, whenever $`Cs<\delta/e`$,


```math
\begin{aligned}
1-\mathrm{Tr}\!\left(\Psi^{\otimes r_j}\eta^{(j)}\right)
&\le
\left(\frac{eCs}{\delta}\right)^{t_j+1}\\
&\le e^{-c n_j},\\
c&:=\delta\ln\!\left(\frac{\delta}{eCs}\right)>0.
\end{aligned}
\qquad\text{(9)}
```


The concrete parameters below permit $`\delta=1/236`$. The explicit gate decomposition in [1, Appendix B] uses $`C=70`$. Consequently one sufficient, deliberately conservative regime is


```math
0<\nu<
\frac{8}{7e\cdot236\cdot70}.
\qquad\text{(10)}
```


Only a nonzero threshold is needed for the asymptotic result. Equation (10) is not a claimed optimal or practical threshold.

### No perfect non-Clifford seed is hidden in the batch map

The initial conversion prepares each ten-qubit resource state by consuming $`C`$ of the given noisy CCZ states through gate injection. The remaining gates in that preparation are Clifford. After code-based distillation, computational-basis measurement of seven qubits and outcome-dependent Clifford corrections convert each ten-qubit output to a CCZ state. All measurement outcomes are used. This is the CCZ-to-CCZ route in [1, Section 4.4]; it does not use the separate CCZ-to-T conversion or its high-quality T seed.

## 2. Code lengths can track every requested accuracy

An unbounded sequence of constant-rate codes alone would not establish $`O(\log(1/\epsilon))`$ size for every small $`\epsilon`$: its successive lengths could be arbitrarily far apart. The explicit family in [1, Example 5.3.1] rules out that problem.

Let $`g_j`$ be the genus of the underlying function field. The construction gives


```math
\left\lfloor\frac{57}{2}g_j\right\rfloor-3
\le n_j
\le\left\lfloor\frac{59}{2}g_j\right\rfloor-1,
\quad
r_j=\left\lfloor\frac54g_j\right\rfloor,
\quad
t_j=\left\lfloor\frac18g_j\right\rfloor.
\qquad\text{(11)}
```


Its explicit genus formulas [1, Eq. (287), or Eqs. (289)–(296)] have


```math
g_j=33\cdot32^{j-1}+O(32^{j/2+1}),
\qquad
\frac{g_{j+1}}{g_j}\longrightarrow32.
\qquad\text{(12)}
```


Thus the $`n_j`$ are eventually increasing, and there is a constant $`B<\infty`$ such that


```math
n_{j+1}\le Bn_j
\qquad\text{(13)}
```


for every sufficiently large $`j`$. For example, the asymptotic upper ratio following from (11)–(12) is at most $`32\cdot59/57<34`$, so $`B=34`$ works after a finite initial segment.

The same bounds imply


```math
\frac{n_j}{r_j}\le24
\qquad\text{(14)}
```


whenever $`g_j\ge48`$, and


```math
t_j+1>\frac{g_j}{8}
>\frac{n_j}{236}.
\qquad\text{(15)}
```


Fix the source, hence fix $`c>0`$ in (9). Choose the first sufficiently large code index with


```math
n_j\ge c^{-1}\ln(1/\epsilon).
\qquad\text{(16)}
```


Minimality and (13) give


```math
n_j\le Bc^{-1}\ln(1/\epsilon)
\qquad\text{(17)}
```


for all sufficiently small $`\epsilon`$. Equations (9) and (17) provide global batch infidelity at most $`\epsilon`$ with $`N_j,r_j=O(\log(1/\epsilon))`$.

## 3. A single fixed input count and an exactly preparable flag

Retain only


```math
m_j=2^{\lfloor\log_2r_j\rfloor}
\qquad\text{(18)}
```


of the batch outputs and discard the rest. Denote their joint state by $`\eta_j`$. Since $`r_j/2<m_j\le r_j`$, the rate drops by at most a factor of two. Moreover,


```math
1-\mathrm{Tr}(\Psi^{\otimes m_j}\eta_j)
\le\epsilon.
\qquad\text{(19)}
```


Discarding outputs preserves this bound because a partial target projector is larger, in the positive-semidefinite order, than the full target projector.

From (3), (14), and (18),


```math
\frac{N_j}{m_j}<48C.
```


We may therefore take one integer


```math
K=48C
\qquad\text{(20)}
```


for the entire family. For the displayed $`C=70`$ decomposition, $`K=3360`$ is a valid unoptimized choice. The theorem only needs the existence of a constant $`K`$; it does not assert that every smaller input budget is achievable.

Power-of-two rounding ensures that the uniform phase label used below is exactly preparable with $`\log_2m_j`$ independent Hadamard-and-measurement bits. Thus the construction does not rely on a non-dyadic external random source. Any larger fixed budget $`K'\ge K`$ is also possible by discarding $`K'-K`$ fresh inputs each round.

For the remaining argument fix $`j`$ and abbreviate $`N=N_j`$, $`m=m_j`$, and $`\eta=\eta_j`$. Define


```math
\zeta=\rho_\nu^{\otimes K},
\qquad
\pi=|000\rangle\langle000|,
\qquad
\mathcal J(x)=x\otimes\pi^{\otimes(K-1)}.
\qquad\text{(21)}
```


Each padded block has $`3K`$ qubits. A deterministic free map $`\mathcal B`$ takes $`m`$ such raw blocks, discards $`Km-N`$ raw source copies, runs the batch protocol, retains $`m`$ outputs, and pads each output by $`\mathcal J`$. Hence


```math
\mathcal B(\zeta^{\otimes m})=\widehat\eta,
\qquad
\widehat\eta=\mathcal J^{\otimes m}(\eta).
\qquad\text{(22)}
```


All $`Km`$ input source copies are accounted for; discarding is part of the free map.

## 4. The catalyst and the exact-return proof

Write $`\widehat\eta_{1:\ell}`$ for the marginal of $`\widehat\eta`$ on its first $`\ell`$ blocks, with the zero-block marginal understood as the scalar 1. On $`m-1`$ padded blocks and a $`\log_2m`$-qubit classical register $`F`$, define


```math
\boxed{
\tau=
\frac1m\sum_{r=0}^{m-1}
\zeta^{\otimes r}\otimes
\widehat\eta_{1:m-1-r}
\otimes|r\rangle\langle r|_F.}
\qquad\text{(23)}
```


This is the cyclic catalyst of [2, Eq. (8)], with relabeled phases and the padding choice above.

One application receives a fresh block $`\zeta`$, measures the computational-basis flag, and acts as follows.

If $`0\le r<m-1`$, the memory contains $`r`$ raw blocks followed by $`m-1-r`$ batch-output blocks. Emit its last batch-output block. Insert the new raw block after the old raw blocks, and set the flag to $`r+1`$.

If $`r=m-1`$, the memory and fresh input together contain $`\zeta^{\otimes m}`$. Apply $`\mathcal B`$, emit output block $`m`$, retain output blocks $`1,\ldots,m-1`$, and set the flag to 0.

Finally remove the $`K-1`$ free padding triples from the emitted block.

### Exact catalyst marginal

For $`r<m-1`$, tracing out the emitted block leaves


```math
\zeta^{\otimes(r+1)}
\otimes\widehat\eta_{1:m-2-r}
\otimes|r+1\rangle\langle r+1|_F.
\qquad\text{(24)}
```


For $`r=m-1`$, it leaves


```math
\widehat\eta_{1:m-1}\otimes|0\rangle\langle0|_F.
\qquad\text{(25)}
```


Equations (24)–(25) cycle the summands of (23) with their weights unchanged. Therefore, if $`\omega_{BC}`$ is the joint emitted-output and retained-memory state,


```math
\mathrm{Tr}_B\omega_{BC}=\tau
\qquad\text{(26)}
```


exactly. This identity includes the complete flag register and its correlations with the quantum memory.

### Output accuracy

Across the $`m`$ equiprobable phases, each of the $`m`$ batch marginals is emitted exactly once. After removing the padding,


```math
\omega_B=\frac1m\sum_{a=1}^m\eta_a.
\qquad\text{(27)}
```


Equation (19) implies


```math
\mathrm{Tr}(\Psi\eta_a)
\ge\mathrm{Tr}(\Psi^{\otimes m}\eta)\ge1-\epsilon
```


for every $`a`$. By linearity,


```math
1-\mathrm{Tr}(\Psi\omega_B)\le\epsilon.
\qquad\text{(28)}
```


No product structure of $`\eta`$, $`\omega_{BC}`$, or the outputs of successive uses is assumed.

### Every operation is free in the stated model

The flag is classical in (23), so measuring it does not disturb the prescribed state. Updating the label means measuring, performing classical arithmetic, and preparing the new computational-basis label. A coherent modular-increment unitary is unnecessary. Conditional block swaps are implemented by classical feed-forward and Clifford SWAP gates. The refresh map $`\mathcal B`$ is a stabilizer channel. Removal of padding and other discarded systems is free. The construction uses no controlled non-Clifford gate acting on a coherent flag.

Because (26) is exact, the same marginal guarantee holds on every reuse with an independent fresh source block, including when the memory remains correlated with earlier emitted outputs. This gives indefinite marginal reusability in precisely the sense of [2, Theorem 4]. It does not assert independent outputs or a fixed global error bound for an arbitrarily long output stream.

## 5. Retained memory and magic resource

The retained catalyst uses exactly


```math
q=3K(m-1)+\log_2m
\qquad\text{(29)}
```


qubits. Combining $`K=O(1)`$, $`m\le r_j=O(n_j)`$, and (17) proves


```math
q=O(\log(1/\epsilon)).
\qquad\text{(30)}
```


The flag requires only $`O(\log\log(1/\epsilon))`$ of these qubits. It is included in the accounting.

Let


```math
G(x)=-\log_2\max_{\sigma\in\mathrm{STAB}}F(x,\sigma),
\qquad
E_R(x)=\min_{\sigma\in\mathrm{STAB}}D(x\Vert\sigma),
```


where $`F`$ is squared Uhlmann fidelity. Since $`I/2^q`$ is free,


```math
G(\tau)\le q,\qquad
E_R(\tau)\le D(\tau\Vert I/2^q)=q-S(\tau)\le q.
\qquad\text{(31)}
```


The same dimensional bound holds for the minimized max-relative entropy. Thus the construction has $`O(\log(1/\epsilon))`$ resource as well as retained qubit cost. Together with the converse for $`\rho_\nu\ge\nu I_8/8`$ and $`F_{\mathrm{STAB}}(\Psi^{\otimes\ell})=(9/16)^\ell`$, the optimal orders are logarithmic for these fixed sources and achievable fixed input budgets.

Equation (29) counts the catalyst retained between uses. It makes no claim about optimized gate count, refresh latency, classical decoding workspace, or the smallest possible transient workspace during batch processing.

## 6. Exact preparation and optimal source-only initialization order

The catalyst does not require an ideal copy of the target product $`\Psi^{\otimes m}`$. Its definition uses the actual noisy state $`\eta`$ produced by the batch channel.

An exact initialization procedure is:

1. Prepare the uniform phase $`r\in\{0,\ldots,m-1\}`$ using $`\log_2m`$ fair measurement bits.
2. Run the batch channel on $`N`$ independent copies of $`\rho_\nu`$ and form its padded output $`\widehat\eta`$.
3. Independently supply $`K(m-1)`$ further source copies, grouped into $`m-1`$ raw blocks.
4. Conditional on $`r`$, retain $`r`$ raw blocks and the first $`m-1-r`$ padded batch-output blocks. Discard all remaining systems and retain the phase flag.

The resulting state is exactly (23), using a fixed worst-case source budget


```math
N_{\mathrm{init}}\le N+K(m-1)=O(\log(1/\epsilon)).
\qquad\text{(32)}
```


The state $`\widehat\eta`$ is generated operationally; the initialization does not require a classical description or tomography of its exponentially large density matrix.

The logarithmic initialization order is also necessary if the catalyst must be prepared only from the same noisy source and free ancillary states. This necessity is inherited from the ordinary resource-purification bound [4], rather than a separate catalytic impossibility result. Compose an initialization using $`J`$ raw copies with the first $`K`$-input use of the resulting catalyst and discard the catalyst. The resulting overall channel $`\mathcal P`$ is free. Equation (8) gives


```math
\mathcal P(\rho_\nu^{\otimes(J+K)})
\ge
\nu^{J+K}\mathcal P((I_8/8)^{\otimes(J+K)}).
\qquad\text{(33)}
```


The state on the right, before multiplication by its weight, is normalized and free. Its CCZ overlap is at most $`9/16`$. Taking the expectation of $`I-\Psi`$ therefore gives


```math
\epsilon\ge\nu^{J+K}\frac7{16},
\qquad
J\ge
\frac{\log_2(1/\epsilon)+\log_2(7/16)}
{\log_2(1/\nu)}
-K.
\qquad\text{(34)}
```


The catalyst resource bound supplies another useful accounting relation. Product choices of free comparison states imply fidelity supermultiplicativity, hence subadditivity of $`G`$. Monotonicity under the initialization channel gives


```math
G(\tau_\epsilon)
\le G(\rho_\nu^{\otimes J})
\le JG(\rho_\nu).
\qquad\text{(35)}
```


Here $`G(\rho_\nu)>0`$ is a fixed constant: the source's CCZ overlap $`1-7\nu/8`$ exceeds $`9/16`$ in the stated noise regime. Equations (32) and (34) establish matching source-only initialization order under a fixed or worst-case input budget. No lower bound on expected input cost of an unrestricted random stopping procedure is asserted.

## 7. Error conventions and scope

The proof uses output infidelity $`1-\mathrm{Tr}(\Psi\omega_B)`$. If a trace-distance target $`\tfrac12\|\omega_B-\Psi\|_1\le\varepsilon`$ is required, choose batch infidelity at most $`\varepsilon^2`$; the retained size and initialization cost remain $`O(\log(1/\varepsilon))`$.

The source parameter $`\nu`$ is fixed as the target accuracy improves. All fresh source copies are independent of the catalyst and prior history. Perfect return is required only on this prescribed source input. No robustness to arbitrary source miscalibration or noisy Clifford control is claimed.

The cost counted is the retained catalyst and its preparation from the noisy source. Constant ongoing input overhead therefore coexists with a logarithmically growing initial resource investment. This statement remains compatible with correlated outputs and does not convert a sufficient marginal-error union bound into a necessary accuracy condition for long output streams.

## Primary references and edition-specific pointers

[1] Adam Wills, Min-Hsiu Hsieh, and Hayata Yamasaki, *Constant-overhead magic state distillation*, Nature Physics **21**, 1842–1846 (2025), DOI [10.1038/s41567-025-03026-0](https://doi.org/10.1038/s41567-025-03026-0). The detailed theorem, section, and equation numbers cited here refer to [arXiv:2408.07764v2](https://arxiv.org/html/2408.07764v2), dated 21 August 2024: Section 2.4 and Eq. (114) for the global-error definition; Sections 4.3–4.4 for deterministic decoding and CCZ conversions; Example 5.3.1 and Eqs. (287)–(296) for code lengths; Theorem 6.1 and Eqs. (301)–(305) for the batch error bound; Appendix B for $`C=70`$. The journal version was published online on 16 September 2025.

[2] Kun Fang and Zi-Wen Liu, *One-shot distillation with constant overhead using catalysts*, Nature Communications **17**, 6010 (2026), DOI [10.1038/s41467-026-72686-0](https://doi.org/10.1038/s41467-026-72686-0). The cyclic-state and proof locators refer to [arXiv:2410.14547v3](https://arxiv.org/html/2410.14547v3), dated 2 September 2026: Theorems 3–4, Corollary 6, and Section 4.1, Eqs. (6)–(13). The construction here uses their deterministic case, with power-of-two output rounding to make classical flag preparation exact using fair measurement bits.

[3] Sergey Bravyi, Dan Browne, Padraic Calpin, Earl Campbell, David Gosset, and Mark Howard, *Simulation of quantum circuits by low-rank stabilizer decompositions*, Quantum **3**, 181 (2019), DOI [10.22331/q-2019-09-02-181](https://doi.org/10.22331/q-2019-09-02-181); [arXiv:1808.00128v2](https://arxiv.org/pdf/1808.00128v2). Section 5.3 gives $`F_{\mathrm{STAB}}(\mathrm{CCZ})=9/16`$; Theorem 5 and Corollary 3 establish the tensor-power identity used by the matching converse.

[4] Kun Fang and Zi-Wen Liu, *No-Go Theorems for Quantum Resource Purification: New Approach and Channel Theory*, PRX Quantum **3**, 010337 (2022), DOI [10.1103/PRXQuantum.3.010337](https://doi.org/10.1103/PRXQuantum.3.010337); [arXiv:2010.11822](https://arxiv.org/abs/2010.11822). Its free-component purification principle gives the source-only initialization lower bound when preparation and one use are composed.
