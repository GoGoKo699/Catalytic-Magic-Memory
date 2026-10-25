# Related work and proof dependencies

The central converse concerns deterministic purification from a fixed noisy source, with a fixed fresh-input count and exact return of an arbitrary correlated catalyst. It forces the catalyst's logarithmic free fidelity to diverge with output precision. Its distinction from earlier catalyst-resource bounds is the absence of an input-target resource-gap assumption.

The following comparison uses the stated editions and operational models. It establishes specific differences between theorem hypotheses; it is not an assertion that every possible catalysis result has been excluded. Full bibliographic records are in [references.bib](references.bib).

## What is imported and what is established here?

| Ingredient or conclusion | Provenance |
|---|---|
| Preservation of individual output marginals under repeated exact marginal reuse | Fang and Liu, Theorem 4 |
| Positive free-component bounds for noisy resource purification | Fang and Liu (2022) |
| Stabilizer fidelities of T/CCZ and multiplicativity for the relevant target products | Bravyi et al.; mixed-qubit results of Rubboli, Takagi and Tomamichel |
| Deterministic constant-rate CCZ batch distillation | Wills, Hsieh and Yamasaki |
| Cyclic conversion of a batch protocol into a catalytic protocol | Fang and Liu, Theorem 3 |
| Catalyst-only free-input comparison, finite fidelity-resource error floor, and all-fixed-input-budget retained-resource converse | Derived in [reuse_converse.md](../science/reuse_converse.md) and [resource_costs.md](../science/resource_costs.md) |
| Matching logarithmic CCZ retained-resource order | The converse combined with the imported constructions and the explicit resource accounting in [cyclic_construction.md](../science/cyclic_construction.md) |
| Logarithmic source-only initialization necessity | An ordinary-purification corollary, separate from the retained-catalyst result |

The single educational anchor is Chitambar and Gour's [*Quantum Resource Theories*](https://doi.org/10.1103/RevModPhys.91.025001), Reviews of Modern Physics 91, 025001 (2019). It supplies resource-theory foundations and measure definitions. The [source-to-project bridge](../learning/CHITAMBAR_GOUR_BRIDGE.md) translates its root fidelity and product-return catalytic formulation before developing the project's squared-fidelity, correlated-marginal-return argument. The later results below remain separately attributed research dependencies.

<a name="fangliu2026"></a>
## Fang and Liu: constant-input catalytic distillation

**One-shot distillation with constant overhead using catalysts**, Nature Communications 17, 6010 (2026), [DOI](https://doi.org/10.1038/s41467-026-72686-0). The locators here refer to [arXiv:2410.14547v3](https://arxiv.org/html/2410.14547v3), dated 2 September 2026.

Theorem 3 and its Eq. (8) construct the cyclic catalyst from a batch protocol. Theorem 4 establishes marginal reuse. Corollary 6 gives deterministic constant-input magic distillation. The following discussion asks whether catalysts with bounded magic can attain vanishing error or residual correlations.

The present result addresses the vanishing-error branch for fixed positive-free-component sources and the specified pure targets. The catalysts in their construction are allowed to grow with accuracy, so the converse is compatible with their achievement. A claim about vanishing correlations alone for arbitrary mixed targets is outside the theorem.

<a name="rubboli2022"></a>
## Rubboli and Tomamichel: catalyst-resource divergence with a gap

**Fundamental Limits on Correlated Catalytic State Transformations**, Physical Review Letters 129, 120506 (2022), [DOI](https://doi.org/10.1103/PhysRevLett.129.120506); [arXiv:2111.13356v2](https://arxiv.org/html/2111.13356v2).

Their Theorem 2 already proves logarithmic catalyst-resource divergence. It requires an index $`\alpha\in[1/2,1)`$ for which minimized sandwiched Rényi resource is additive for the target against every catalyst and the entire input has strictly smaller resource than the target. Their result also accommodates approximate catalyst return under its joint-product error convention.

The [noisy-T example](../science/magic_targets.md#absence-of-every-renyi-gap-in-the-earlier-converse) proves that every allowed gap can fail for a fixed input batch while the new converse remains nontrivial. This is the operative distinction. Standard pure T and CCZ targets do have strong fidelity multiplicativity against arbitrary mixed catalysts, so general nonmultiplicativity of magic is not by itself an obstruction for these examples.

Appendix B explains why their smoothed-divergence proof does not extend by replacing the sandwiched quantity with a smoothed Petz divergence below order one. Their reversed-argument remark concerns classical athermality. These observations prevent a direct substitution into that theorem; they do not rule out a different divergence-based proof.

<a name="fangliu2022"></a>
## Fang and Liu: positive free components and purification

**No-Go Theorems for Quantum Resource Purification: New Approach and Channel Theory**, PRX Quantum 3, 010337 (2022), [DOI](https://doi.org/10.1103/PRXQuantum.3.010337); [arXiv:2010.11822v4](https://arxiv.org/html/2010.11822v4).

The free component is a pre-existing tool: if an input dominates a normalized free state with weight $`w`$, a deterministic free output has pure-target infidelity at least $`w(1-f_1)`$. The [startup bound](../science/resource_costs.md#preparation-cost-has-a-different-provenance) follows by composing preparation and one use.

Applied directly to the input including an arbitrary catalyst, the available free weight may vanish because the catalyst can be rank deficient. A startup lower bound also says nothing about which resource must remain stored. The repeated comparison in this repository retains the catalyst as a resource input and bounds its free fidelity, avoiding both limitations.

<a name="bravyi2019"></a>
## Bravyi and collaborators: stabilizer overlaps

**Simulation of quantum circuits by low-rank stabilizer decompositions**, Quantum 3, 181 (2019), [DOI](https://doi.org/10.22331/q-2019-09-02-181); [arXiv:1808.00128v2](https://arxiv.org/html/1808.00128v2).

Section 5.3 supplies the standard target fidelities. Theorem 5 proves multiplicativity for stabilizer-aligned factors, and Corollary 3 includes all pure states on at most three qubits. Lemma 11 bounds the relevant low-rank stabilizer projections for pure states of arbitrary size.

The [target page](../science/magic_targets.md) gives the resulting tensor-power exponents and spells out the small-target strong-multiplicativity consequence, including mixed catalysts. The finite enumeration in this repository checks small-system constants only.

<a name="rubboli2024"></a>
## Rubboli, Takagi and Tomamichel: mixed-state additivity

**Mixed-state additivity properties of magic monotones based on quantum relative entropies for single-qubit states and beyond**, Quantum 8, 1492 (2024), [DOI](https://doi.org/10.22331/q-2024-10-04-1492); [arXiv:2307.08258v4](https://arxiv.org/html/2307.08258v4).

Theorem 2 proves stabilizer-fidelity multiplicativity for arbitrary products of single-qubit states. This is used in the explicit example excluding every gap in the earlier converse. Further results cover specified two- and three-qubit states and other Rényi measures.

Section 6 discusses catalytic extensions under an explicit target-catalyst additivity condition. Its low-order and reversed-divergence bounds improve ordinary distillation overhead; the discussion also reports nonadditivity of reversed magic divergences. These statements do not supply an arbitrary-correlated-catalyst resource-cost theorem at every fixed batch size. Low-order divergences remain relevant alternative tools, rather than methods ruled out by this comparison.

<a name="wills2025"></a>
## Wills, Hsieh and Yamasaki: deterministic CCZ batches

**Constant-overhead magic state distillation**, Nature Physics 21, 1842–1846 (2025), [DOI](https://doi.org/10.1038/s41567-025-03026-0). The detailed construction used here is [arXiv:2408.07764v2](https://arxiv.org/html/2408.07764v2).

Section 2.4 defines the global error convention. Sections 4.3–4.4 give the deterministic decoder and CCZ conversions. Example 5.3.1 specifies suitable code lengths. Theorem 6.1 and Eqs. (301)–(305) give constant-rate distillation with exponentially suppressed error. Appendix B gives the displayed finite CCZ-gate decomposition.

The [achievability page](../science/cyclic_construction.md) combines these ingredients with the cyclic catalyst, counts the full flag and retained registers, and constructs the catalyst from the actual noisy batch output. This supplies a matching asymptotic order, without claiming a new code or a practical optimized overhead.

<a name="son2026"></a>
## Son and collaborators: robustness to an input neighborhood

**Catalytic channels are the only noise-robust catalytic processes**, Physical Review Letters 136, 050202 (2026); [arXiv:2412.06900v2](https://arxiv.org/html/2412.06900v2).

Their robust model requires exact catalyst return for every input in an open neighborhood. This implies return for all input states and links the transformation to resource broadcasting. The current model requires exact return at one specified noisy source. Full rank does not replace the neighborhood quantifier, and the free-source comparison experiment need not preserve the catalyst. The robust-catalysis no-go therefore concerns a stronger return requirement.

## Other finite-size and irreversibility results

- **Lipka-Bartosik and Korzekwa, Finite-size Catalysis in Quantum Resource Theories**, Physical Review A 111, 022440 (2025); [arXiv:2405.08914v2](https://arxiv.org/html/2405.08914v2), revised March 2026. Theorem 3 gives sufficient finite-size catalyst constructions from multicopy rates. Its outlook distinguishes sufficiency from the unresolved necessity of those size criteria.
- **Ao, Philip and Streltsov, PPT Entanglement with Correlated Catalysis: Monotones and Irreversibility**, [arXiv:2608.20063v1](https://arxiv.org/html/2608.20063v1). Its monotones constrain catalytic conversion rates independently of the catalyst. The magic application in Supplemental Section V concerns odd-dimensional Wigner theory. It does not quantify the retained fidelity resource of a qubit catalyst in the present precision limit.
- **Wang and Li, Irreversibility of bound magic states assisted by catalysis**, Physical Review A 114, 012427 (2026), [DOI](https://doi.org/10.1103/yj6l-lhph). The published abstract concerns asymptotic nondistillability of bound magic in odd-prime dimensions. That source regime and question differ from catalyst cost for distillable noisy qubit inputs; no full-proof comparison is asserted here.

The supported conclusion is a converse at the stated fixed-source, fixed-input-budget, exact-return scope, together with a matching CCZ resource order. Neither the comparison nor the construction establishes optimal coefficients, arbitrary success-probability extensions or every possible catalytic transformation.
