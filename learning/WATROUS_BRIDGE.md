# From Watrous to catalytic magic memory

A magic-state factory supplies special quantum states used to implement gates
outside the stabilizer operations. A reusable factory can consume a fixed
number of noisy states each time it emits an improved state. The question in
this project is what must grow inside that factory when the requested output
error becomes smaller.

The selected educational anchor is **John Watrous, *The Theory of Quantum
Information*, Cambridge University Press, 2018**. The readings below refer to
the author's **standard-layout prepublication manuscript**, with a preface
dated January 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/)
identifies the book's publication as April 2018 and provides the
[contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) and
[errata](https://cs.uwaterloo.ca/~watrous/TQI/TQI.errata.pdf).
Page numbers here are printed manuscript pages, rather than PDF viewer
indices. The source is linked for reading.

The [30-milestone map](MILESTONES.md) fixes the project's understanding
targets. This bridge connects the selected source to those targets through
notation, a complete small example, and the main proof mechanisms.
The [scientific route](../science/README.md) leads directly to exact
statements, proofs, imported results, and resource qualifications.

## Targeted reading from the single anchor

Read the indicated sections as their concepts become useful. The route
uses parts of Chapters 1, 2, 3, and 5; it does not require completing the book.

| Project use | Watrous manuscript pointer | Connection supplied here |
|---|---|---|
| States, tensors, and positive source components, M01, M03, M06 | [Sections 1.1.1–1.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), tensor operators p. 13 and positivity pp. 17–18; [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Definition 2.5 p. 62 and reductions p. 68 | A source block, an output register, and a persistent memory have different roles even when all are density operators. |
| Deterministic maps and retained records, M04, M07, M12–M14 | [Sections 2.2.1–2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Definition 2.13 p. 73, Corollary 2.27 p. 89, and Eq. (2.170) pp. 95–96 | Complete positivity permits local action on a correlated system. Complete stabilizer preservation is an additional resource condition. |
| Target tests and error conventions, M02, M10, M15 | [Section 2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Definition 2.34 p. 101; [Sections 3.1.1, 3.2.1, and 3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Proposition 3.5 p. 130, Proposition 3.13 p. 142, and Theorem 3.33 p. 161 | Pure-target overlap is squared root fidelity. A joint target test does not assume independent actual outputs. |
| Resource monotonicity and the binary converse, M08–M09, M17–M18 | [Sections 5.1.1, 5.2.1, and 5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), Definition 5.18 p. 266 and Theorem 5.35 p. 280 | Minimize relative entropy over free states, then apply data processing to a binary measurement. |
| Quantum versus classical memory, M11, M29 | [Section 2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Eq. (2.170); [Sections 5.2.1–5.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), Definitions 5.17–5.18 and Proposition 5.20, pp. 265–268 | A comparison state with the same classical probabilities charges only the quantum register. |
| The complete model, converse, and construction, M13–M30 | The preceding targeted readings, used together | The project supplies the stabilizer geometry, reuse argument, source comparison, horizon optimization, catalytic cycle, and matched resource account. Primary research dependencies are identified below. |

## Notation and error conventions

| Watrous | This project | Meaning |
|---|---|---|
| $`uu^*`$ | $`\lvert u\rangle\langle u\rvert`$ | Pure-state density operator for a unit vector $`u`$. |
| $`\rho[X]`$ | $`\rho_X=\mathrm{Tr}_{\bar X}\rho`$ | Reduced state of the retained register. |
| $`1`$ for an identity operator | $`I`$ | Identity on the indicated space. |
| $`H(\rho)`$ | $`S(\rho)`$ | Von Neumann entropy in bits. |
| $`F(\rho,\sigma)`$ | $`F_W(\rho,\sigma)`$ in this bridge | Root fidelity; the extra subscript prevents confusion with the project's overlap convention. |
| “Trace distance” $`\lVert\rho-\sigma\rVert_1`$ on p. 34 | $`D_{\mathrm{tr}}(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$ | The project includes the factor one-half. |
| $`\mathcal C(\mathcal X,\mathcal Y)`$ | A set of channels | It is unrelated to the project's register name $`C`$ for the catalyst. |

Here and below, $`\psi=\lvert\psi\rangle\langle\psi\rvert`$ denotes a pure
target projector. Watrous's Definition 3.11 and Proposition 3.13 give

```math
F_W(\rho,\sigma)=\|\sqrt{\rho}\sqrt{\sigma}\|_1,
\qquad
F_W(\rho,\psi)^2=\mathrm{Tr}(\psi\rho).
```

The project's error is therefore

```math
e_\psi(\rho)=1-\mathrm{Tr}(\psi\rho)=1-F_W(\rho,\psi)^2.
```

Theorem 3.33 gives the upper inequality in

```math
e_\psi(\rho)\le D_{\mathrm{tr}}(\rho,\psi)
\le\sqrt{e_\psi(\rho)}.
```

For the lower inequality, measure the two effects $`\{\psi,I-\psi\}`$.
The outcome distributions are $`(1-e_\psi,e_\psi)`$ and $`(1,0)`$,
whose one-norm difference is $`2e_\psi`$. Proposition 3.5 bounds this by
$`\|\rho-\psi\|_1`$. This stronger pure-target lower bound uses the
measurement argument, not just the generic lower fidelity inequality.

Consequently, a trace-distance requirement $`D_{\mathrm{tr}}\le\delta`$
is met by constructing infidelity at most $`\delta^2`$. It changes a
logarithmic expression to $`\ln(1/\delta^2)=2\ln(1/\delta)`$.
It does not identify the two error parameters.

Entropy and relative-entropy logarithms are base two, as in Watrous's
Chapter 5. The symbol $`\ln`$ denotes the natural logarithm. In
$`D(\rho\Vert\sigma)`$, the support of $`\rho`$ must be contained in
that of $`\sigma`$; otherwise the value is infinite. The convention
$`0\log 0=0`$ does not remove this support requirement.

## States, registers, and free resources

A density operator describes the probabilities of all measurements on a
register. A partial trace describes what is observable on a subsystem
without access to the rest. Two global states can have the same marginal
and different correlations. This is why restoring a catalyst's density
operator is a weaker requirement than separating it from its output.

In this project, free states form the convex set $`\mathrm{STAB}`$ of
mixtures of pure stabilizer states. Clifford gates, stabilizer ancillas,
Pauli measurements, classical control, and discarding give physical
stabilizer operations. A deterministic protocol includes every measurement
branch in its channel. Its accuracy is an unconditional output statement.

Watrous supplies channels and complete positivity. The
[model](../science/model.md#1-free-states-and-operations) adds the resource
condition: applying the channel to part of a free joint system must preserve
freeness even when a reference register is retained. The converse permits
this larger class of completely stabilizer-preserving channels; the
construction uses physical stabilizer operations.

A positive free component is the operator inequality
$`\chi\succeq w\sigma_0`$, for a normalized free state $`\sigma_0`$.
For $`0<w<1`$, it means that
$`\chi=w\sigma_0+(1-w)\eta`$ for another density operator $`\eta`$.
The factory is not given a label identifying either component. This is an
analytical decomposition, not a heralded free-input event.

Full-rank noise supplies such a component because
$`\rho\succeq d\lambda_{\min}(\rho)I_d/d`$. For a fixed number of
independent fresh copies, the positive weight remains fixed as the desired
output error decreases. The [source condition](../science/model.md#4-a-positive-free-component-in-the-source)
is the place to check those quantifiers.

A classical controller is represented by a joint state of the form
$`\sum_j a_j\lvert j\rangle\langle j\rvert\otimes\tau_j`$.
Its full joint state has no coherence between labels. A diagonal controller
marginal alone would not establish this. Every persistent record used by the
next call belongs in the returned catalyst, even when its classical storage
is free.

## A complete two-phase return example

The following one-qubit example isolates the catalyst's bookkeeping.
Let the fresh state be $`\zeta=\lvert0\rangle\langle0\rvert`$.
Take a two-output batch channel whose output is

```math
\eta_{12}
=\frac12\lvert00\rangle\langle00\rvert
+\frac14\lvert01\rangle\langle01\rvert
+\frac14\lvert11\rangle\langle11\rvert.
```

This channel can discard its inputs and prepare the displayed mixture
using classical random bits and stabilizer preparations. Its marginals are

```math
\eta_1=\frac34\lvert0\rangle\langle0\rvert
       +\frac14\lvert1\rangle\langle1\rvert,
\qquad
\eta_2=\frac12 I.
```

Store one quantum qubit $`Q`$ and a classical phase $`F`$ taking two
values. Initialize their joint state as

```math
\tau_{QF}
=\frac12\eta_{1,Q}\otimes\lvert1\rangle\langle1\rvert_F
+\frac12\zeta_Q\otimes\lvert2\rangle\langle2\rvert_F.
```

Each call appends a fresh $`\zeta`$ on the left. It then performs the
appropriate row of the following table, retaining the first quantum block
and emitting the last.

| Input phase | Operation on the two quantum blocks | Retained state | Emitted marginal | New phase |
|---|---|---|---|---:|
| 1 | Leave $`\zeta\otimes\eta_1`$ unchanged | $`\zeta`$ | $`\eta_1`$ | 2 |
| 2 | Apply the batch channel to $`\zeta\otimes\zeta`$ | $`\eta_1`$ | $`\eta_2`$ | 1 |

The complete joint state after a call, with output $`B`$, is

```math
\omega_{QBF}
=\frac12\eta_{QB}\otimes\lvert1\rangle\langle1\rvert_F
+\frac12\zeta_Q\otimes\eta_{1,B}\otimes
 \lvert2\rangle\langle2\rvert_F.
```

Tracing out $`B`$ gives exactly $`\tau_{QF}`$. The phase changes in each
sampled branch, but the complete mixed state, including phase correlations,
returns. The emitted marginal is

```math
\omega_B=\frac12(\eta_1+\eta_2)
=\frac58\lvert0\rangle\langle0\rvert
+\frac38\lvert1\rangle\langle1\rvert.
```

Measuring the emitted qubit in the computational basis therefore gives
outcome zero with probability $`5/8`$ on every call. Conditioned on new
phase 1, the joint quantum state is the correlated state $`\eta`$:
the event $`Q=1,B=0`$ has probability zero, while the product of those
marginal probabilities is $`1/8`$. Exact catalyst return has not removed
output–memory correlations.

This example consumes one fresh free qubit per call and stores one quantum
qubit plus one classical bit. All its states are free. It demonstrates
stationarity, asymmetric output marginals, and the averaging rule. The
CCZ construction supplies the substantive magic-distillation batch
ingredient, with every input and initialization resource charged.

## From correlated reuse to the counterfactual

The [reuse argument](../science/converse.md#2-sequential-reuse-preserves-every-nominal-output-guarantee)
starts from a local statement. Before each call, the fresh block is
independent of the past and the catalyst marginal is $`\tau`$. The
reduced input to that call is therefore always $`\chi\otimes\tau`$.
A trace-preserving operation on other registers cannot change an earlier
output marginal. Thus every output has error at most $`\epsilon`$ even
though the outputs can be correlated.

Let $`P_i`$ test the pure target on output $`i`$. The projectors commute
because they act on different registers, and

```math
I-\prod_{i=1}^{L}P_i
\preceq\sum_{i=1}^{L}(I-P_i).
```

Taking the expectation in the actual joint output bounds its product-target
infidelity by $`L\epsilon`$. This is a union bound for commuting tests;
the target is a tensor product, but the actual state need not be.

Now run the same complete circuit with every fresh block replaced by
$`\sigma_0`$. Positivity, tensor products, and the positive action of the
circuit imply

```math
\Omega_{\mathrm{nominal}}
\succeq w^L\Omega_{\mathrm{free}},
\qquad
\delta_L=\frac{L\epsilon}{w^L}.
```

Testing the failure effect bounds the counterfactual output error by
$`\delta_L`$. Its fresh inputs contain no magic, so its output resource
must come from the initial catalyst. The circuit need not return the
catalyst on this comparison input. Return is used to establish repeated
accuracy on the designated nominal source.

The [finite-horizon lemma](../science/converse.md#finite-horizon-lemma)
separates the two roles: any protocol with the stated final marginal
guarantees over a chosen finite horizon obeys the same converse. Exact
stationarity supplies such a guarantee for every horizon. An approximate
return claim alone does not supply that induction.

## From a binary test to quantum memory

Watrous's relative-entropy data-processing theorem says that a channel
cannot increase $`D(\rho\Vert\sigma)`$. Minimizing the second argument
over free states yields monotonicity of the relative entropy of magic
$`E_R`$ under the permitted free maps.

For the counterfactual output, measure the binary test
$`\{\psi^{\otimes L},I-\psi^{\otimes L}\}`$.
This test is an analytical comparison. It need not be implementable as a
free stabilizer measurement: data processing applies to every measurement
channel.

Define $`b_L`$ as the maximum target overlap of a free joint state.
The counterfactual state passes with probability at least
$`1-\delta_L`$, while every free comparison state passes with probability
at most $`b_L`$. Binary relative entropy converts that separation into a
resource cost. For $`\delta_L\le1/2`$ and $`b_L\le f^L`$ with $`0<f<1`$, the
[finite theorem](../science/converse.md#theorem-1-finite-catalyst-resource-bound)
gives

```math
E_R(\tau)\ge
(1-\delta_L)L\log_2(1/f)-h_2(\delta_L).
```

Here $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$ is binary entropy,
with the usual endpoint convention. The exact theorem also gives a
binary-relative-entropy form with its own stated condition. The two
conditions should not be interchanged.

The exponential target-overlap bounds for computational $`T`$ and CCZ
come from [B2019](../references/related-work.md#b2019).
The arbitrary catalyst can be mixed or rank deficient. No additivity
assumption involving that catalyst is used.

For a classical–quantum catalyst with $`q`$ quantum qubits, compare it
with the free state that keeps the same classical probabilities but replaces
each conditional quantum state by $`I/2^q`$. Evaluating the logarithms
block by block gives

```math
E_R(\tau_{JQ})
\le D\!\left(
 \sum_j a_j\lvert j\rangle\langle j\rvert\otimes\tau_j
 \,\middle\Vert\,
 \sum_j a_j\lvert j\rangle\langle j\rvert\otimes I/2^q
\right)
=q-\sum_j a_j S(\tau_j)\le q.
```

The classical probabilities cancel. Increasing their number does not
increase the bound. A coherently stored controller belongs in $`q`$.

Finally set $`x=\ln(1/\epsilon)`$ and $`a=\ln(1/w)>0`$.
Choosing $`L=\lfloor(x-2\ln x)/a\rfloor`$ for sufficiently large
$`x`$ keeps $`\delta_L`$ small while $`L`$ grows linearly in
$`x`$. The finite theorem then forces
$`E_R(\tau)=\Omega(\ln(1/\epsilon))`$ and hence the same lower bound
on quantum width. The [optimization and error floor](../science/converse.md#6-optimize-the-number-of-repetitions)
give the constants and the separate case $`w=1`$.

This argument uses a positive free component, without assuming the input
block has less total resource than the target. The
[closest-work comparison](../references/related-work.md#rt2022) explains
the earlier logarithmic catalyst bounds and the precise distinction.

## From a batch protocol to a stationary factory

The general cycle behind the two-phase example stores a uniform mixture
of $`M`$ phases. A phase consists of unfinished fresh blocks followed by
a prefix marginal of an actual $`M`$-output batch. Most calls move one
fresh block into the buffer and emit one completed block. Once per cycle,
a full batch is processed.

The [exact return identity](../science/construction.md#5-the-catalyst-and-its-exact-return)
uses consistency of partial traces. It does not replace the batch output
by an ideal state, assume identical marginal outputs, or discard a
correlated persistent controller. The emitted state is the average of the
batch marginals. A global batch infidelity bound therefore supplies every
call's marginal error bound.

Two primary results provide the upper-bound ingredients:

- [WHY2025](../references/related-work.md#why2025) supplies a deterministic
  constant-rate CCZ batch protocol with exponentially decreasing global
  error at sufficiently low fixed source noise.
- [FL2026](../references/related-work.md#fl2026) supplies the catalytic
  conversion. The project specializes its exact state identities and
  accounts for quantum width, phase storage, padding, and initialization.

The [code-family argument](../science/construction.md#6-choosing-a-batch-for-every-target-accuracy)
controls the gap between successive available batch sizes. That step is
needed to turn a discrete family into an upper bound for every sufficiently
small requested error. Batch size proportional to $`\ln(1/\epsilon)`$
then gives the same scaling for persistent quantum memory.

For the source $`\rho_\lambda=(1-\lambda)\psi_{\mathrm{CCZ}}+\lambda I_8/8`$,
source infidelity is $`p=7\lambda/8`$. It is distinct from the noise
mixing parameter $`\lambda`$. A sufficient fixed budget is
$`r=1680`$ source copies per output; the construction's conservative
threshold is $`p<1/(236e\cdot70)`$.
The catalyst can be prepared from the same noisy source without a perfect
magic seed. Its preparation cost and the periodically executed batch
circuit remain part of the [resource ledger](../science/resources.md).

## Joining the learning route to the science

M01–M13 connect states, errors, operations, free resources, and complete
memory accounting into one stationary-factory model. M14–M22 build the
converse from local reuse to a finite inequality, asymptotic lower bound,
and comparison with earlier work. M23–M28 assemble the batch ingredient,
exact cyclic return, initialization, and every-accuracy upper bound.
M29–M30 join the resource ledger, evidence, and final theorem.

For a fixed permitted noisy CCZ source and a sufficient fixed input budget,
the two directions yield
$`q_{\min}(\epsilon)=\Theta(\log(1/\epsilon))`$.
The lower bound covers every fixed finite budget; feasibility and the
matching upper bound require the construction's stated source quality and
budget. Logical persistent quantum width is the optimized resource.

The canonical [model](../science/model.md),
[converse](../science/converse.md),
[construction](../science/construction.md), and
[resources](../science/resources.md) own the full arguments.
The [related-work account](../references/related-work.md) separates
the contribution from inherited results and records limits of the
literature comparison. The [finite checks](../verification/README.md)
verify explicit overlaps, state identities, and arithmetic examples.
They complement the analytical proofs.

Watrous is the sole educational anchor. Stabilizer-overlap theorems,
magic-state distillation codes, and catalytic-conversion results remain
research dependencies with their own citations. The bridge does not turn
them into textbook consequences or claim physical-qubit, gate-count, or
runtime optimality.
