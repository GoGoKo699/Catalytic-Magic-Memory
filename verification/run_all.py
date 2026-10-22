#!/usr/bin/env python3
"""Finite checks supporting the written catalytic-memory proofs.

Standard library only. Exact rational arithmetic is used for Pauli overlaps and
the correlated catalyst cycle. These checks do not prove tensor-power
multiplicativity, the asymptotic converse, or the batch-code theorem.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json
import math
from pathlib import Path

Matrix = list[list[F]]


def zeros(n: int) -> Matrix:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[x * y for x in ar for y in br] for ar in a for br in b]


def power(a: Matrix, n: int) -> Matrix:
    out = [[F(1)]]
    for _ in range(n):
        out = kron(out, a)
    return out


def reduce_qubits(a: Matrix, keep: tuple[int, ...], n: int) -> Matrix:
    """Partial trace, using qubit 0 as the most significant tensor factor."""
    assert len(a) == 1 << n
    assert tuple(sorted(set(keep))) == keep
    traced = tuple(k for k in range(n) if k not in keep)

    def bits(x: int, positions: tuple[int, ...]) -> int:
        out = 0
        for k in positions:
            out = (out << 1) | ((x >> (n - 1 - k)) & 1)
        return out

    out = zeros(1 << len(keep))
    for x, row in enumerate(a):
        for y, value in enumerate(row):
            if bits(x, traced) == bits(y, traced):
                out[bits(x, keep)][bits(y, keep)] += value
    return out


def average(items: list[Matrix]) -> Matrix:
    n = len(items[0])
    return [[sum(a[i][j] for a in items) / len(items)
             for j in range(n)] for i in range(n)]


def trace(a: Matrix) -> F:
    return sum(a[i][i] for i in range(len(a)))


def pauli_overlap_check() -> dict:
    """Enumerate every signed rank-one three-qubit stabilizer projector."""
    n, d = 3, 8

    def xz(v: int) -> tuple[int, int]:
        return v & (d - 1), v >> n

    def commutes(u: int, v: int) -> bool:
        x, z = xz(u)
        a, b = xz(v)
        return ((x & b).bit_count() + (z & a).bit_count()) % 2 == 0

    def multiply(u: int, v: int) -> tuple[int, int]:
        # P(x,z)=i^popcount(x&z) X^x Z^z.
        x, z = xz(u)
        a, b = xz(v)
        h = u ^ v
        c, e = xz(h)
        exponent = ((x & z).bit_count() + (a & b).bit_count()
                    + 2 * (z & a).bit_count() - (c & e).bit_count()) % 4
        assert exponent in (0, 2), "Only commuting factors are multiplied."
        return h, 1 if exponent == 0 else -1

    def expectation(v: int) -> F:
        x, z = xz(v)
        # CCZ|+++> has equal magnitudes and only amplitude 111 is negative.
        signs = [1] * 7 + [-1]
        total = sum(signs[j ^ x] * signs[j] *
                    (-1 if (j & z).bit_count() % 2 else 1)
                    for j in range(d))
        phase = (x & z).bit_count() % 4
        if phase % 2:
            assert total == 0
            return F(0)
        return F(total * (1 if phase == 0 else -1), d)

    spaces: dict[tuple[int, ...], tuple[int, int, int]] = {}
    for basis in combinations(range(1, d * d), n):
        u, v, w = basis
        if not all(commutes(a, b) for a, b in combinations(basis, 2)):
            continue
        span = tuple(sorted({0, u, v, w, u ^ v, u ^ w, v ^ w, u ^ v ^ w}))
        if len(span) == d:
            spaces.setdefault(span, basis)

    histogram: Counter[F] = Counter()
    for basis in spaces.values():
        for eigen_signs in range(d):
            total = F(0)
            for subset in range(d):
                element, sign = 0, 1
                for k, generator in enumerate(basis):
                    if (subset >> k) & 1:
                        element, phase = multiply(element, generator)
                        sign *= phase * (-1 if (eigen_signs >> k) & 1 else 1)
                total += sign * expectation(element)
            overlap = total / d
            assert 0 <= overlap <= 1
            histogram[overlap] += 1
    assert len(spaces) == 135
    assert sum(histogram.values()) == 1080
    assert max(histogram) == F(9, 16)
    return {
        "maximal_commuting_pauli_subspaces": len(spaces),
        "pure_stabilizer_projectors": sum(histogram.values()),
        "maximum_ccz_overlap": str(max(histogram)),
        "overlap_histogram": {str(k): histogram[k] for k in sorted(histogram)},
    }


def catalyst_cycle_check() -> dict:
    """Test the full marginal identities on asymmetric correlated batches."""
    zeta = [[F(3, 5), F(1, 5)], [F(1, 5), F(2, 5)]]
    results = []
    for m in (3, 4):
        d = 1 << m
        eta = zeros(d)
        # Half a GHZ density matrix plus half an asymmetric basis projector.
        for x in (0, d - 1):
            for y in (0, d - 1):
                eta[x][y] = F(1, 4)
        eta[1][1] += F(1, 2)
        assert trace(eta) == 1
        prefix = {s: reduce_qubits(eta, tuple(range(s)), m)
                  for s in range(m + 1)}
        sectors = [kron(power(zeta, i - 1), prefix[m - i])
                   for i in range(1, m + 1)]
        returned = [None] * m
        emitted = []
        for i in range(1, m + 1):
            incoming = kron(zeta, sectors[i - 1])
            assert trace(incoming) == 1
            if i == m:
                assert incoming == power(zeta, m)
                joint = eta
            else:
                joint = incoming
            next_flag = i % m
            returned[next_flag] = reduce_qubits(joint, tuple(range(m - 1)), m)
            emitted.append(reduce_qubits(joint, (m - 1,), m))
        assert returned == sectors
        expected = average([reduce_qubits(eta, (s,), m) for s in range(m)])
        actual = average(emitted)
        assert actual == expected
        # The chosen batch has genuinely quantum correlations (GHZ coherence).
        assert eta[0][-1] == F(1, 4)
        assert reduce_qubits(eta, (0,), m) != reduce_qubits(eta, (m - 1,), m)
        results.append({
            "batch_blocks": m,
            "exact_flagged_catalyst_marginal_return": True,
            "output_is_average_of_batch_marginals": True,
            "emitted_density_matrix": [[str(v) for v in row] for row in actual],
        })
    return {"correlated_quantum_batches": results}


def resource_gap_check() -> dict:
    """Evaluate the analytic qubit optimizer in two independent coordinates."""
    f = (2 + math.sqrt(2)) / 4
    noise = .01
    spectral = (math.sqrt((1 - noise) * f) +
                math.sqrt(noise * (1 - f))) ** 2
    radius = 1 - 2 * noise
    rx = radius / math.sqrt(2)
    # Uhlmann squared fidelity in Bloch coordinates, s=(1/2,1/2,0).
    bloch = (1 + rx + math.sqrt((1 - radius * radius) / 2)) / 2
    assert abs(spectral - bloch) < 1e-14
    source = -2 * math.log2(spectral)
    target = -math.log2(f)
    assert source > target
    return {
        "source_t_eigenstate_error": noise,
        "optimal_free_fidelity": round(spectral, 12),
        "two_input_D_half_bits": round(source, 12),
        "target_D_alpha_bits_for_alpha_at_least_half": round(target, 12),
        "strict_gap_in_wrong_direction_bits": round(source - target, 12),
        "scope": "Values; optimizer and additivity are justified in the written account.",
    }


def genus(i: int) -> int:
    assert i >= 3
    if i % 2:
        return 33 * 32 ** (i - 1) - 34 * 32 ** ((i - 1) // 2) + 1
    return 33 * 32 ** (i - 1) - 561 * 32 ** (i // 2 - 1) + 1


def code_parameter_check() -> dict:
    """Check finite members against the inequalities proved in construction.md."""
    c, r = 70, 1680
    rows = []
    for i in range(3, 13):
        g = genus(i)
        m, t = (5 * g) // 4, g // 8
        n_lo, n_hi = (114 * g) // 4 - 3, (118 * g) // 4 - 1
        assert F(63, 2) * 32 ** (i - 1) <= g <= 33 * 32 ** (i - 1)
        assert genus(i + 1) < 34 * g
        assert c * n_hi <= r * m
        assert F(n_hi, t + 1) <= 236
        assert t + 1 > F(g, 8)
        assert n_lo <= n_hi and m > 0
        if i in (3, 4):
            rows.append({
                "tower_index": i, "genus": g, "outputs_M": m,
                "decoder_radius": t, "qudit_length_interval": [n_lo, n_hi],
                "persistent_quantum_qubits": 3 * r * (m - 1),
                "classical_flag_bits": (m - 1).bit_length(),
            })
    threshold = 1 / (236 * math.e * c)
    return {
        "C": c, "fixed_fresh_ccz_budget_r": r,
        "sufficient_source_infidelity_threshold": round(threshold, 15),
        "checked_tower_indices": [3, 12],
        "first_two_members": rows,
        "scope": "Finite arithmetic checks; all-index and all-accuracy bounds are analytical.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print deterministic results.")
    args = parser.parse_args()
    result = {
        "ccz_stabilizer_overlap": pauli_overlap_check(),
        "correlated_catalyst_cycle": catalyst_cycle_check(),
        "prior_resource_gap_witness": resource_gap_check(),
        "explicit_code_parameters": code_parameter_check(),
    }
    expected_path = Path(__file__).parent / "expected.json"
    if expected_path.exists():
        assert result == json.loads(expected_path.read_text()), \
            "Results differ from the committed scientific snapshot."
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for name in result:
            print(f"PASS {name}")
        print("All finite checks passed. General claims rely on the written proofs and cited theorems.")


if __name__ == "__main__":
    main()
