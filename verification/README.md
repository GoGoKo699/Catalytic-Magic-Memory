# Finite verification

From the repository root, run:

```bash
python3 verification/check_targets.py
```

The script uses only Python's standard library. It enumerates all maximal isotropic subspaces of the binary Pauli space for one, two and three qubits, then evaluates every joint eigenspace projector. Binary linear algebra and commutation checks use exact integers. State overlaps use double-precision complex arithmetic with an absolute tolerance of $`10^{-12}`$.

| Target | Pure stabilizer projectors enumerated | Maximum overlap |
|---|---:|---:|
| T | 6 | $`(1+1/\sqrt2)/2`$ |
| T tensor T | 60 | $`((1+1/\sqrt2)/2)^2`$ |
| CCZ | 1080 | $`9/16`$ |

The resulting exponents are approximately $`0.228446696836388`$ for T and $`0.830074998557688`$ for CCZ. The committed [output](expected_targets.json) records the numerical values.

This is an independent finite reconstruction of the constants used in the target examples. The script checks the number of isotropic subspaces, normalization and positivity of every stabilizer eigenspace probability, and agreement with the stated analytic values.

The general catalyst converse, all-accuracy asymptotics, tensor-power multiplicativity and CCZ achievability follow from the written proofs and cited results. Enumeration on at most three qubits does not establish those statements. No experimental data or large numerical simulation enters the claims.
