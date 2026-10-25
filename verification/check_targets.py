#!/usr/bin/env python3
"""Enumerate all pure stabilizer projectors on up to three qubits.

Binary symplectic subspaces are enumerated with exact integer arithmetic.
Only state overlaps use floating point. This checks the finite constants used
in the scientific account; it does not prove tensor-power multiplicativity.
"""

import cmath
import json
import math


def canonical_basis(vectors):
    """Reduced row-echelon basis over GF(2), with highest-bit pivots."""
    rows = []
    for vector in vectors:
        for row in rows:
            if vector & (1 << (row.bit_length() - 1)):
                vector ^= row
        if vector:
            pivot = 1 << (vector.bit_length() - 1)
            rows = [row ^ vector if row & pivot else row for row in rows]
            rows.append(vector)
            rows.sort(reverse=True)
    return tuple(rows)


def commute(v, w, n):
    mask = (1 << n) - 1
    vx, vz = v & mask, v >> n
    wx, wz = w & mask, w >> n
    return ((vx & wz).bit_count() + (vz & wx).bit_count()) % 2 == 0


def isotropic_bases(n):
    spaces = {()}
    for dimension in range(n):
        next_spaces = set()
        for basis in spaces:
            for vector in range(1, 1 << (2 * n)):
                if all(commute(vector, row, n) for row in basis):
                    enlarged = canonical_basis((*basis, vector))
                    if len(enlarged) == dimension + 1:
                        next_spaces.add(enlarged)
        spaces = next_spaces
    return sorted(spaces)


def apply_pauli(vector, state, n):
    mask = (1 << n) - 1
    x, z = vector & mask, vector >> n
    phase = 1j ** ((x & z).bit_count() % 4)
    output = [0j] * (1 << n)
    for index, amplitude in enumerate(state):
        sign = -1 if (z & index).bit_count() % 2 else 1
        output[index ^ x] = phase * sign * amplitude
    return output


def stabilizer_fidelity(state, n):
    if len(state) != 1 << n:
        raise ValueError("State dimension does not match qubit count")
    if abs(sum(abs(x) ** 2 for x in state) - 1) > 1e-12:
        raise ValueError("State is not normalized")
    bases = isotropic_bases(n)
    expected_bases = math.prod((1 << j) + 1 for j in range(1, n + 1))
    if len(bases) != expected_bases:
        raise AssertionError((n, len(bases), expected_bases))
    best = 0.0
    projectors = 0
    for basis in bases:
        moments = []
        for subset in range(1 << n):
            transformed = list(state)
            for j, pauli in enumerate(basis):
                if subset & (1 << j):
                    transformed = apply_pauli(pauli, transformed, n)
            moment = sum(x.conjugate() * y for x, y in zip(state, transformed))
            if abs(moment.imag) > 1e-12:
                raise AssertionError("Commuting Hermitian product has complex expectation")
            moments.append(moment.real)
        probabilities = []
        for sign_bits in range(1 << n):
            probability = sum(
                (-1 if (sign_bits & subset).bit_count() % 2 else 1) * moment
                for subset, moment in enumerate(moments)
            ) / (1 << n)
            if not -1e-12 <= probability <= 1 + 1e-12:
                raise AssertionError("Invalid joint eigenspace probability")
            probabilities.append(probability)
            best = max(best, probability)
            projectors += 1
        if abs(sum(probabilities) - 1) > 1e-12:
            raise AssertionError("Joint stabilizer eigenspaces are not normalized")
    return {"qubits": n, "isotropic_subspaces": len(bases),
            "pure_stabilizer_projectors": projectors, "maximum_overlap": best}


def main():
    t = [1 / math.sqrt(2), cmath.exp(1j * math.pi / 4) / math.sqrt(2)]
    tt = [t[i // 2] * t[i % 2] for i in range(4)]
    ccz = [(1 if i != 7 else -1) / math.sqrt(8) for i in range(8)]
    f_t = (1 + 1 / math.sqrt(2)) / 2
    cases = [("T", t, 1, f_t), ("T_tensor_T", tt, 2, f_t ** 2),
             ("CCZ", ccz, 3, 9 / 16)]
    output = {}
    for name, state, n, expected in cases:
        result = stabilizer_fidelity(state, n)
        if abs(result["maximum_overlap"] - expected) > 1e-12:
            raise AssertionError((name, result, expected))
        result["analytic_value"] = expected
        result["exponent_bits"] = -math.log2(expected)
        output[name] = result
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
