# Finite verification

The written proofs establish the converse and the matching asymptotic law. The checks here independently evaluate explicit mathematical ingredients where an indexing, phase, convention or rounding error could change the conclusion.

## Run

Python 3.10 or newer is required. There are no third-party dependencies. The recorded run used Python 3.12.

```bash
python3 verification/run_all.py
python3 verification/run_all.py --json
```

A successful run reports five PASS lines. The JSON result is compared with [expected.json](expected.json). A mismatch raises an error. Assertions must remain enabled; do not run with Python's optimization option.

## What is checked

| Check | Method | What the result establishes |
|---|---|---|
| CCZ stabilizer overlap | Exact enumeration of maximal commuting three-qubit Pauli subspaces and all eigenvalue signs | All 1,080 pure stabilizer projectors have CCZ overlap at most $`9/16`$, and eight attain it |
| T and T tensor T stabilizer overlaps | The same Pauli enumeration, with expectations evaluated directly from complex state amplitudes | The maxima over all 6 and 60 pure stabilizer projectors are $`f=(2+\sqrt2)/4`$ and $`f^2`$, including entangled two-qubit stabilizers |
| Correlated catalyst cycle | Exact rational partial traces on asymmetric, quantum-correlated batches of three and four blocks | The complete flagged catalyst marginal returns exactly, and the emitted state is the average batch marginal |
| Resource-gap conditions | Spectral and Bloch-coordinate fidelity formulas, plus the depolarized-T free-weight decomposition | Both stated two-input examples exceed the T target value $`0.228446696836`$ bits; the noise conventions agree after converting depolarization to eigenstate error |
| Explicit code parameters | Integer and rational arithmetic for tower indices 3 through 12 | The displayed padding, decoder-radius and bounded-spacing inequalities hold on the inspected members |

### Stabilizer enumeration

A binary symplectic vector labels the canonical Hermitian Pauli $`P(x,z)=i^{x\cdot z}X^xZ^z`$. Every three-dimensional isotropic subspace has eight simultaneous eigenspaces, each defining a rank-one stabilizer projector. The script enumerates 135 such subspaces, retains the Pauli multiplication signs, and computes the expectation of each projector in $`\mathrm{CCZ}|+\rangle^{\otimes3}`$ with exact rational arithmetic.

This reproduces the single-copy overlap independently. It does **not** prove tensor-power multiplicativity; that is an imported analytical result identified in the [references](../references/related-work.md#b2019).

The same enumeration also covers the three one-qubit and fifteen two-qubit maximal commuting Pauli subspaces. Direct amplitude calculations for $`|T\rangle`$ and $`|T\rangle^{\otimes2}`$ give maximum overlaps approximately $`0.853553390593`$ and $`0.728553390593`$. Every joint eigenspace distribution is checked for positivity and normalization: exactly for CCZ and within $`10^{-12}`$ for T and T tensor T. Pauli labels, commutation and multiplication signs use exact arithmetic in all cases. The two-copy result is a finite check, not a proof for arbitrary tensor powers.

### Correlated-cycle contractions

The batch state is a mixture of a GHZ state and an asymmetric computational-basis state. Its off-diagonal GHZ coherence makes it quantum correlated, and its unequal single-register marginals make ordering errors observable. The supplied input block is a full-rank rational qubit state. These small examples test the conversion's marginal identities; they do not simulate the algebraic-geometric distillation code or establish its noise threshold.

The entire classical phase is retained in the comparison. Checking only the averaged quantum buffer would miss a possible correlation with the controller.

### Resource-gap example

The script evaluates the known optimal free-state fidelity in two coordinate systems and checks the numerical strict inequality. The optimizer, sandwiched-Renyi monotonicity and mixed-state additivity that extend this comparison to all permitted orders are justified in the [related-work account](../references/related-work.md#rt2022). A finite numerical calculation alone would not establish that extension.

For T eigenstate error $`0.01`$, the two-input value is $`D_{1/2}=0.250520749128`$ bits. The separate depolarization convention $`\rho_\nu=(1-\nu)|T\rangle\langle T|+\nu I/2`$ has eigenstate error $`\nu/2`$. At $`\nu=0.01`$, the script checks $`G=-\log_2F_{\rm STAB}=0.152175104935`$ bits and $`2G=0.304350209870`$ bits. It also verifies the Bloch-coordinate decomposition with free weight $`p=\nu/(1-1/\sqrt2)=0.034142135624`$. These arithmetic checks do not prove that the stated fidelities or free weights are optimal.

### Code-family arithmetic

The checked genus formula is the explicit tower used in [the construction](../science/construction.md). The code length is bounded by an interval because the selected rational places enter the construction. Width is computed from the chosen fixed budget and number of output blocks; no unspecified code length is silently replaced by an exact value.

For $`C=70`$, the fixed budget is $`r=1680`$, the sufficient source-infidelity threshold is approximately $`2.2268731306\times10^{-5}`$, and the first displayed catalyst contains 206,035,200 quantum qubits. These are conservative witness parameters.

The universal tower-spacing and all-accuracy arguments are analytical. The finite checks do not certify the entire decoder, a fault-tolerant implementation, or an optimized experimental design.

## Interpretation

The checks use exact arithmetic for the CCZ overlap, catalyst contractions and code-family inequalities, and ordinary floating point for T amplitudes, qubit fidelity formulas, logarithms and thresholds. They provide reproducible support for the concrete ingredients, independently of the theorem prose. They are not independent human peer review, an exhaustive literature audit or a numerical proof of the asymptotic result.
