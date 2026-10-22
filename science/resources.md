# Resources of a reusable catalytic factory

The [CCZ construction](construction.md) consumes a constant number of fresh noisy magic states per emitted output and stores a quantum catalyst whose size grows logarithmically with inverse target infidelity. Its initialization, persistent memory, batch processing, and physical implementation are different resource costs. This page states what is included in the construction and what follows from it.

## 1. Resource ledger

Let $g$ be the selected code genus, $N$ the code's qudit length, $K=CN$ the original batch input count, $M=\lfloor5g/4\rfloor$ its output count, and $r=24C$ the fixed fresh-input budget. Here $N,K,M=\Theta(g)$ and $g=O(1+\log(1/\epsilon))$ at a fixed permitted source state.

| Resource | Bound for the construction | Meaning |
|---|---:|---|
| Fresh noisy CCZ states per call | Exactly $r=24C$ | Includes any input states later discarded by the padded batch |
| Catalyst quantum memory | $q=3r(M-1)$ qubits | The padded catalyst register between calls |
| Classical phase register | $b=\lceil\log_2M\rceil$ bits | Tracks the position in the batch cycle |
| Noisy source states for initialization | At most $K+r(M-1)$ | A separate one-time cost |
| Peak quantum workspace | $O(K+N+rM)=O(g)$ qubits | Catalyst, incoming source registers, and an implementation of the batch |
| Batch-circuit executions | One per $M$ calls along a phase cycle | Each execution processes a growing batch |
| Classical decoding and code data | Polynomial in $N$ for the inherited decoder | Additional to the small phase register |
| Physical encoded qubits and wall-clock time | Not specified | Require a hardware, noise, and fault-tolerance model |

The code, conversion circuits, and polynomial-time decoding are inherited from [WHY2025](../references/related-work.md#why2025), particularly §4, §5.3, and Theorem 6.1. The cyclic catalyst is inherited from [FL2026](../references/related-work.md#fl2026), Methods §4.1. The counts in the table follow from their explicit combination.

## 2. Exact initialization from the same noisy source

The catalyst is

$$
\tau_g=\frac1M\sum_{i=1}^{M}
\zeta^{\otimes(i-1)}
\otimes\widehat\eta_{1:M-i}
\otimes|i\rangle\langle i|_F,
\qquad
\zeta=\rho_\lambda^{\otimes r}.
$$

Here $\eta_M$ is the actual output of the deterministic batch channel on $K$ independent copies of $\rho_\lambda$, and the hats denote free padding. Preparation is therefore operational:

1. Sample a uniform classical value $i\in\{1,\ldots,M\}$.
2. Run the batch once on $K$ independent noisy source states. Retain its first $M-i$ outputs, discard the others, and append the specified free padding.
3. Prepare $r(i-1)$ further independent copies of the same source state.
4. Assemble those registers in the order appearing above and retain $i$ as the classical flag.

No exact CCZ state, exact $T$ state, or other pure magic seed appears in this procedure. The state being stored is the noisy batch output produced by the available source. Preparation remains exact as a density-operator identity even though that output only approximates ideal CCZ states.

The maximum source consumption is $K+r(M-1)$. Sampling the phase and running the quantum protocol have no heralded failure event. Uniform classical randomness is part of the free-control model; if implemented using fair random bits, rejection sampling can generate the phase with finite expected classical work and without rejecting any quantum distillation attempt. No worst-case bound on that classical sampling time is required by the channel model.

A single batch execution suffices in each realized preparation branch; there is no requirement to prepare all $M$ mixture components or run $M$ batches. When $i=M$, no batch-output register is retained, so that branch can even omit the batch. The stated maximum remains a convenient uniform upper bound.

Initialization uses independent source states for the batch and for the raw-source part of the buffer. Subsequent calls receive new independent source blocks. This independence is needed for the channel identities and is distinct from the allowed correlations among the batch outputs.

## 3. Quantum memory and free classical memory

The explicit padded catalyst contains $M-1$ blocks of $r$ three-qubit registers. Its quantum-register size is exactly

$$
q=3r(M-1).
$$

Some registers hold known free padding in some phase components. One can generate or remove such padding as needed, but this does not turn the whole buffer into classical data: other components contain a linear number of noisy source registers or distilled-output registers. The formula above is a simple fixed-register implementation and a valid upper bound, without relying on compression.

The phase register has only $M$ classical values. If it is physically represented by computational-basis qubits, those qubits contribute $b=\lceil\log_2M\rceil$ additional storage locations. If classical bits are accounted separately, the quantum catalyst cost remains $q$ and the phase cost is $b$.

This distinction also applies to the lower bound. Suppose an arbitrary catalyst consists of $q$ quantum qubits and an unrestricted classical register:

$$
\tau_{FQ}
=\sum_c p_c |c\rangle\langle c|_F\otimes\tau_c.
$$

The comparison state

$$
\sigma_{FQ}
=\sum_c p_c |c\rangle\langle c|_F\otimes\frac{I_Q}{2^q}
$$

is free. With entropy and relative entropy measured in bits,

$$
E_R(\tau_{FQ})
\le D(\tau_{FQ}\|\sigma_{FQ})
=q-\sum_c p_c S(\tau_c)
\le q.
$$

Consequently, a lower bound on the catalyst's relative-entropy magic also lower-bounds its quantum memory, even when classical storage is free and its dimension is not bounded in advance. A large classical label alone cannot provide the required magic.

The phase register is not the entire classical cost of the implementation. The batch decoder, a description of the code, and controller work registers may require much more classical storage. The construction makes no claim that all classical memory is $O(\log M)$.

## 4. Coherent workspace, gate count, and throughput

The catalyst is present between calls. During the wraparound call, the factory also executes the full batch circuit. A direct implementation stores the $M$ source-sized blocks, represents each code qudit by ten qubits, and performs stabilizer operations using reusable measurement ancillas. The required quantum width is $O(K+N+rM)=O(g)$. The one-time initialization has the same order of width.

This is an abstract circuit-width statement. It permits sequential reuse of ancillas and imposes no geometric locality or constant-depth requirement. The width count includes stored quantum inputs as well as the code registers; it is not just the number of freshly supplied states.

To make the time distinction explicit, write $G_{\mathcal B}(g)$ for the Clifford-gate count of one chosen batch implementation and $G_{\rm move}(g)$ for any per-call routing or permutation cost. Along each complete cycle,

$$
\text{average gate count per output}
\le
\frac{G_{\mathcal B}(g)}{M}+G_{\rm move}(g)
$$

up to the fixed per-call interface operations. A wraparound call itself incurs the full $G_{\mathcal B}(g)$ cost. If block movement is implemented by swaps, that movement also has to be charged. If the architecture allows a logical relabeling or a movable output port, some routing may instead be handled by classical bookkeeping.

The inherited polynomial decoder does not imply constant decoding latency. Nor does constant fresh-magic consumption imply constant quantum gate count or a constant-duration output schedule. Any numerical throughput estimate would need an explicit batch circuit, decoder implementation, routing model, and scheduling policy.

The stationary mixture over phases is useful for the exact catalyst identity. In each realized cycle, the phase advances deterministically and the batch operation occurs once every $M$ calls. At any fixed call in the stationary description, its probability is $1/M$. This probability refers to which trace-preserving branch runs, not to a success probability for producing an output.

## 5. A concrete scale check

Choose the explicit $C=70$ decomposition from [WHY2025], Appendix B, so $r=1680$. The first tower member in Example 5.3.1 has

$$
g_3=32705,\qquad
M=40881,\qquad
t=4088,
$$

and

$$
932089\le N\le964796.
$$

Its original batch uses $70N$ noisy CCZ states. The padded catalyst contains

$$
q=3\cdot1680\cdot(40881-1)
=206035200
$$

quantum qubits, with a $16$-bit phase register. The actual $N$ depends on choices within the inherited algebraic-geometry construction; the displayed catalyst count depends only on $M$ and $r$.

This example shows the scale of this particular achievability witness. The logarithmic law concerns its asymptotic dependence on accuracy. These constants do not demonstrate a practical small-device factory or an advantage over optimized finite-size distillation.

## 6. Correlations and repeated use

Exact return means that the density operator on the retained catalyst register, including its phase, is unchanged after each call. The catalyst can be correlated with previous outputs. The new output marginal still obeys the same infidelity bound because its fresh source block is independent and the local input catalyst marginal is unchanged.

For $L$ retained outputs with individual infidelities at most $\epsilon$, the elementary commuting-projector union bound gives

$$
1-\operatorname{Tr}(\psi^{\otimes L}\omega_{S_1\cdots S_L})
\le L\epsilon.
$$

This is a useful worst-case joint-state bound, not an independence statement. An application that needs global target infidelity $\varepsilon_{\rm tot}$ for $L$ outputs can conservatively choose $\epsilon\le\varepsilon_{\rm tot}/L$. The required catalyst memory then scales as

$$
O\!\left(1+\log\frac{L}{\varepsilon_{\rm tot}}\right)
$$

at the fixed source quality. To require trace distance at most $\delta$ from the pure product target, it suffices to choose $\epsilon\le\delta^2/L$, using the pure-target inequality stated in the construction. Stronger application-specific composability or throughput claims require their own analysis.

## 7. Boundary of the matched resource law

For a fixed sufficiently clean full-rank source, the construction supplies a factory at the fixed budget $r=1680$. The lower bound applies to that same source, target, budget, and exact marginal-return requirement. Its logarithmic necessity and the construction's logarithmic achievability therefore concern the same quantum-memory resource.

The model treats stabilizer gates, free ancillas, measurements, resets, and classical processing as ideal. It charges noisy magic inputs and catalyst quantum memory separately. Protecting the stored catalyst and executing the growing batch on noisy hardware would require an outer fault-tolerant implementation, whose encoded space and time have not been specified here. Imperfect catalyst return, source drift, finite-lifetime memory, and postselected factories are different models.

The CCZ target is deliberate. The CCZ-to-$T$ conversion discussed in [WHY2025], Remark 6.0.1, uses an additional $T$ catalyst and discusses preparing it separately. That conversion is not needed for any resource count above. The matched law stated here therefore has no uncharged exact $T$ seed.
