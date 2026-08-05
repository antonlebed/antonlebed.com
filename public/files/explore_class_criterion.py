"""Class existence in the boundary family: the trace criterion, the
finite certificate, and the windows where the class is provably empty.

THE QUESTION
------------
The boundary-family witness (explore_max_string_witness.py,
explore_general_max_string.py) leaves one leg measured per cell: a
both-parity residue class of (q_K + u q_{K-r}, p_K + u p_{K-r}) mod m,
the boundary class (t, c) = (0, 0) excluded. Is class existence
provable in general — and if not, exactly where does it fail?

THE HAND-ATTACK (pre-engine, on paper, checkpointed before this
write)
------------------------------------------------------------------
Vocabulary: v_K = (q_K, p_K); M_K = (v_K, v_{K-1}), det M_K = (-1)^K,
M_0 = I, M_K = M_{K-1} A_K with A_k = [[a_k, 1], [1, 0]];
v_{K-r} = M_K C_{K,r}^{-1} e1 with C_{K,r} = A_{K-r+1} ... A_K a
function of (K mod P, r). So the scanned combination is
w_K = v_K + u v_{K-r} = M_K g_K with g_K = e1 + u C_{K,r}^{-1} e1.

LEMMA A (the finite certificate). The class condition at K is a
function of the state S_K = (K mod P, M_K mod m), which evolves
invertibly on a finite set, hence is purely periodic with some period
T. So ONE even member and ONE odd member below any bound, plus T,
certify infinitely many members of each parity (K and K + 2T share
state and parity): class existence at a scanned cell is a THEOREM the
moment two members and the period are exhibited. The "one leg still
measured" was always finitely certifiable.

LEMMA B (the common-value equation). Value w = (t, c) attained at
even K and odd J <=> M_K g_K = M_J g_J; w != 0 is automatic from
g != 0 since M is invertible. When g_K = g_J = g — forced at P = 1,
and true at any P when r = 1, where g = (1, u) is phase-free — this
says g is a fixed vector of D = M_J^{-1} M_K = A_{J+1} ... A_K, an
ODD-length consecutive product with det D = -1 mod m. For prime m a
nonzero fixed vector exists iff det(D - I) = 0, and
det(D - I) = 1 - tr D + det D = -tr D: iff tr D = 0 mod m.

THE TRACE CRITERION (P = 1, prime m — an iff). At a constant-a window
every odd-length product is A^n with tr A^n = L_n(a), the Lucas
sequence (L_0 = 2, L_1 = a, L_{n+1} = a L_n + L_{n-1}). A both-parity
class exists iff L_n(a) = 0 mod m at some ODD n. Reachability never
obstructs at P = 1: a fixed vector with unit first coordinate is
g = (1, u) at r = 1; first coordinate 0 means g ~ (0, 1), reachable
as e1 - C_{K,2}^{-1} e1 = (0, a) when a is a unit; and a = 0 mod m
makes A itself the swap, tr A = 0 with fixed vector (1, 1).

THE OBSTRUCTION (theorem, golden window a = 1). L_n^2 - 5 F_n^2 =
4(-1)^n, so mod 5 L_n^2 = ±4 and L_n is NEVER 0: at m = 5 no
both-parity class exists at ANY knobs (r, u, t, c). Mod 3 the Lucas
period is 8 with zeros only at n = 2, 6 (even); mod 7 zeros only at
n = 4 mod 8: both obstructed. m = 2 works (L_3 = 4) and m = 11 works
(L_5 = 11). THE GENERAL EXISTENCE CLAIM IS FALSE — the kill-shape
fires at the calibration window itself, and this is why the golden
storeys needed comb telescopes.

THE RAMIFIED LAW (constant-a, odd prime m | a^2 + 4). The same
identity reads L_n^2 - (a^2 + 4) F_n^2 = 4(-1)^n, so mod a ramified
odd prime L_n^2 = ±4 != 0: every odd prime dividing the discriminant
a^2 + 4 is obstructed. At m = 2 with a even, L_1 = a = 0 works — the
even prime escapes.

GENERAL P: the r = 1 criterion (some odd-length consecutive product D
with D (1, u) = (1, u)) is SUFFICIENT at every window. It is NOT
necessary: V1 m = 5 has no r <= 2 class yet carries one at r = 3
(measured) — phase-dependent g_K != g_J escapes the single-vector
frame. TRANSPLANT FLAG: the iff is derived at P = 1 only; at P >= 2
the criterion is one-directional here.

THE DESIGN (checks; predictions frozen before the run)
------------------------------------------------------------------
D0  Positive controls: (i) tr(A^n) mod m equals the Lucas recurrence
    mod m, a in {1..4}, m in {2..7}, n <= 50; (ii) at [0; 1, 1, 3],
    m = 3 the scan re-finds a both-parity class with t = 1 (the
    witness rig's D2 finding). PREDICTION: green.
D1  The certificate sweep: every cell of the two boundary-family
    rigs — V1..V4 x m = 2..7 (24 cells) and [0; 1, 1, a] with m = a,
    a = 2..7 (6 cells). Scan knobs r <= 6, u < m, all (t, c) !=
    (0, 0), members K <= 400; for the first class found print the
    certificate: an even member, an odd member, the state period T,
    and the mechanical re-check that the state at K recurs at K + T.
    PREDICTION: all 30 cells certified — every measured class
    upgrades to a theorem by Lemma A.
D2  The obstruction, brute force at the golden window (tail (1,)):
    m in {3, 5, 7}: scan r <= 30, u < m, all (t, c) != (0, 0),
    K <= 3000 — PREDICTION: NO both-parity class at any of the
    three (derived above; the theorem's teeth). Controls m in
    {2, 11}: PREDICTION: classes found (the scan can find at golden).
D3  The P = 1 iff sweep: a = 1..8, m in {2, 3, 5, 7, 11, 13}. The
    criterion verdict (some odd n in one Lucas period mod m with
    L_n = 0) against the brute verdict (r <= 2, K <= 2 T + 400).
    PREDICTION: the two verdicts agree at all 48 cells, and every
    criterion-yes cell carries a class at r <= 2 (the sufficiency
    construction never needs more).
D4  The ramified map: a = 1..8, odd primes m <= 19: the obstructed
    set by criterion, against the odd prime divisors of a^2 + 4.
    PREDICTION: every odd prime divisor of a^2 + 4 at m <= 19 is
    obstructed. OBSERVABLE (no prediction): the non-ramified
    obstructions — the golden-style sporadics — printed beside them.

THE EXTENSION (design frozen before the second run). The first run's
D0ii FAILED ON THE CHECK'S OWN IMPLEMENTATION: the scan returns the
first both-parity class sorted by value and found (t, c) = (0, 1)
where the check demanded t = 1 — the t = 1 class was never looked
for. Fixed to search the class map for the witness rig's (1, 0)
directly. And D4's sporadic column has a classical closed form,
derived on paper before this write: with U the companion sequence
(U_0 = 0, U_1 = 1, same recurrence) and z(m) its rank of apparition,
the identity U_{2n} = U_n L_n plus gcd(U_n, L_n) | 2 gives, for odd
prime m: L_n = 0 mod m at some odd n  <=>  z(m) = 2 mod 4. (z odd
kills all L-zeros; z = 0 mod 4 makes every L-zero index even; z = 2
mod 4 puts them exactly at odd multiples of z/2.) Ramified odd m
have z = m odd — obstructed, recovering the ramified law. At m = 2
the class always exists at P = 1 (a even: the swap; a odd: L_3 =
a^3 + 3a = 0 mod 2).
D5  The apparition form: a = 1..8, odd primes m <= 50: verdict of
    criterion_P1 against (z(m) mod 4 == 2). PREDICTION: identical at
    every cell.

RESOURCE: everything runs mod m (no big integers anywhere); well
under a second and trivially under 512MB.

RUN RECORD
----------
Two runs (D0-D4, then D0ii fixed + D5 added, designs frozen above
before each). Under a second each, trivial memory.

FINDINGS (post-run)
-------------------
D0: trace(A^n) = L_n at every (a, m, n) scanned; the witness rig's
(t, c) = (1, 0) class at [0;1,1,3] m = 3 re-found at (r, u) = (1, 0),
members K = 22 (even), 5 (odd). (First run's D0ii failure was the
check's own implementation — it read the scan's first class, sorted
by value, instead of looking up the predicted one.)
D1: ALL 30 CELLS CERTIFIED — every cell of both boundary-family rigs
carries a both-parity class with an even member, an odd member, and
state period T (T = 5..100 across cells), recheck green: by Lemma A,
class existence at every measured cell is now a THEOREM. 29 of 30
certify at r = 1; V1 m = 5 needs r = 3 (the known cell).
D2: the golden window is EMPTY at m = 3, 5, 7 under a scan far wider
than any certificate needed (r <= 30, K <= 3000, all u, t, c) — the
derived obstruction's teeth — while the controls m = 2 and m = 11
find classes at r = 1 as predicted.
D3: criterion and brute verdicts agree at all 48 (a, m) cells, and
every criterion-yes cell carries its class at r <= 2: the P = 1 iff
stands as derived.
D4: every odd ramified prime <= 19 is obstructed at its window
(a = 1: 5; a = 3: 13; a = 4, 6: 5; a = 8: 17). The sporadic
obstructions are DENSE — e.g. a = 1 is obstructed at 3, 7, 13, 17 of
the seven odd primes <= 19, workable only at 11 and 19 — which is
what the apparition form (D5) explains: obstruction is the common
case across the scanned map, not the exception.
D5: the closed form is EXACT — criterion_P1 agrees with
(z(m) mod 4 = 2) at all 112 cells (a = 1..8, odd primes m <= 50).

THE READING: class existence in the boundary family is NOT general —
it is governed, at constant-a windows, by the rank of apparition:
a both-parity class exists at odd prime m iff z(m) = 2 mod 4, and
always at m = 2. The engine is provably empty at the golden window
for m = 3, 5, 7 (and at every odd ramified prime at every constant-a
window), which SCOPES the boundary-family method: where z(m) = 2
mod 4 fails, the gate needs different machinery — exactly the comb
telescopes the earlier storeys built. Meanwhile Lemma A turns every
MEASURED class into a proved one with a three-number certificate
(even member, odd member, state period), so the x m discontinuity is
now a theorem at all 24 arbitrary-period cells and all 6 witness
cells. The remaining opens move up a level: the odd-a comb freeze,
and whether z(m) = 2 mod 4 has a density statement worth filing.
"""

import sys

E1 = (1, 0)


def a_at(tail, k):
    """Partial quotient a_k, k >= 1."""
    return tail[(k - 1) % len(tail)]


def mat_mul(X, Y, m):
    return (
        (X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % m,
        (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % m,
    ), (
        (X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % m,
        (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % m,
    )


def A_mat(a, m):
    return ((a % m, 1), (1, 0))


def v_seq(tail, m, count):
    """(q_K, p_K) mod m for K = 0..count-1; q_0 = 1, q_1 = a_1."""
    q = [1, tail[0] % m]
    p = [0, 1]
    for k in range(2, count):
        a_k = a_at(tail, k)
        q.append((a_k * q[-1] + q[-2]) % m)
        p.append((a_k * p[-1] + p[-2]) % m)
    return list(zip(q, p))


def state_period(tail, m):
    """Period T of S_K = (K mod P, M_K mod m), from K = 1."""
    P = len(tail)
    M = (
        (tail[0] % m, 1),
        (1, 0),
    )  # M_1 = (v_1, v_0) columns: [[q1, q0], [p1, p0]]
    start = (1 % P, M)
    K = 1
    while True:
        K += 1
        M = mat_mul(M, A_mat(a_at(tail, K), m), m)
        if (K % P, M) == start:
            return K - 1


def class_members(tail, m, r, u, kmax):
    """Map (t, c) -> (even members, odd members), K in [r+1, kmax]."""
    v = v_seq(tail, m, kmax + 1)
    out = {}
    for K in range(r + 1, kmax + 1):
        w = ((v[K][0] + u * v[K - r][0]) % m, (v[K][1] + u * v[K - r][1]) % m)
        if w == (0, 0):
            continue
        e, o = out.setdefault(w, ([], []))
        (e if K % 2 == 0 else o).append(K)
    return out


def find_class(tail, m, rmax, kmax):
    """Smallest (r, u) with a both-parity class; returns
    (r, u, t, c, even_members, odd_members) or None."""
    for r in range(1, rmax + 1):
        for u in range(m):
            for w, (ev, od) in sorted(class_members(tail, m, r, u, kmax).items()):
                if ev and od:
                    return (r, u, w[0], w[1], ev, od)
    return None


def lucas_mod(a, m, count):
    L = [2 % m, a % m]
    for _ in range(2, count):
        L.append((a * L[-1] + L[-2]) % m)
    return L


def lucas_pair_period(a, m):
    """Period of (L_n, L_{n+1}) mod m."""
    x, y = 2 % m, a % m
    seen = (x, y)
    n = 0
    while True:
        x, y = y, (a * y + x) % m
        n += 1
        if (x, y) == seen:
            return n


def criterion_P1(a, m):
    """Odd n with L_n(a) = 0 mod m inside one period, or None."""
    T = lucas_pair_period(a, m)
    L = lucas_mod(a, m, T + 1)
    for n in range(1, T + 1, 2):
        if L[n] == 0:
            return n
    return None


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (" -- " + detail if detail else ""))
    return ok


def main():
    allok = True

    print("== D0: positive controls ==")
    ok = True
    for a in range(1, 5):
        for m in range(2, 8):
            L = lucas_mod(a, m, 51)
            An = A_mat(a, m)
            M = An
            for n in range(1, 51):
                if (M[0][0] + M[1][1]) % m != L[n]:
                    ok = False
                M = mat_mul(M, An, m)
    allok &= check("D0i trace(A^n) == Lucas mod m (a<=4, m<=7, n<=50)", ok)
    got = None
    for r in range(1, 3):
        for u in range(3):
            members = class_members((1, 1, 3), 3, r, u, 400).get((1, 0))
            if members and members[0] and members[1]:
                got = (r, u, members[0][0], members[1][0])
                break
        if got:
            break
    allok &= check(
        "D0ii [0;1,1,3] m=3 both-parity class (t,c)=(1,0) re-found",
        got is not None,
        f"knobs+members {got}",
    )

    print()
    print("== D1: the certificate sweep (24 general + 6 witness cells) ==")
    cells = []
    for name, tail in [
        ("V1 (1,1,1,2)", (1, 1, 1, 2)),
        ("V2 (2,1,3,1)", (2, 1, 3, 1)),
        ("V3 (1,2,1,1,3)", (1, 2, 1, 1, 3)),
        ("V4 (3,1,2,2,1)", (3, 1, 2, 2, 1)),
    ]:
        for m in range(2, 8):
            cells.append((name, tail, m))
    for a in range(2, 8):
        cells.append((f"[0;1,1,{a}] m={a}", (1, 1, a), a))
    certified = 0
    for name, tail, m in cells:
        got = find_class(tail, m, 6, 400)
        if got is None:
            print(f"  {name} m={m}: NO CLASS at r<=6, K<=400")
            continue
        r, u, t, c, ev, od = got
        T = state_period(tail, m)
        # mechanical recheck: v at K and K+T agree (spot: first even member)
        v = v_seq(tail, m, ev[0] + T + 1)
        recheck = v[ev[0]] == v[ev[0] + T]
        certified += 1 if recheck else 0
        print(
            f"  {name} m={m}: class (r={r},u={u},t={t},c={c}) "
            f"even K={ev[0]} odd K={od[0]} T={T} recheck={'ok' if recheck else 'FAIL'}"
        )
    allok &= check("D1 all 30 cells certified", certified == len(cells), f"{certified}/{len(cells)}")

    print()
    print("== D2: the golden obstruction (tail (1,)) ==")
    for m, expect_empty in [(3, True), (5, True), (7, True), (2, False), (11, False)]:
        got = find_class((1,), m, 30, 3000)
        ok = (got is None) == expect_empty
        allok &= check(
            f"D2 golden m={m} {'EMPTY' if expect_empty else 'found'}",
            ok,
            f"scan r<=30, K<=3000 -> {got[:4] if got else 'none'}",
        )

    print()
    print("== D3: the P=1 iff sweep ==")
    mism = []
    for a in range(1, 9):
        for m in [2, 3, 5, 7, 11, 13]:
            n0 = criterion_P1(a, m)
            T = state_period((a,), m)
            got = find_class((a,), m, 2, 2 * T + 400)
            if (n0 is not None) != (got is not None):
                mism.append((a, m, n0, got[:4] if got else None))
    allok &= check("D3 criterion == brute at all 48 cells", not mism, f"mismatches: {mism}")

    print()
    print("== D4: the ramified map (a = 1..8, odd primes m <= 19) ==")
    ok = True
    for a in range(1, 9):
        disc = a * a + 4
        obstructed = [m for m in [3, 5, 7, 11, 13, 17, 19] if criterion_P1(a, m) is None]
        ram = [m for m in [3, 5, 7, 11, 13, 17, 19] if disc % m == 0]
        if any(m not in obstructed for m in ram):
            ok = False
        extra = [m for m in obstructed if m not in ram]
        print(f"  a={a} disc={disc}: obstructed {obstructed}, ramified {ram}, sporadic {extra}")
    allok &= check("D4 every odd ramified prime <= 19 obstructed", ok)

    print()
    print("== D5: the apparition form ==")

    def rank_apparition(a, m):
        x, y = 0, 1
        n = 0
        while True:
            x, y = y, (a * y + x) % m
            n += 1
            if x == 0:
                return n

    odd_primes_50 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    mism = []
    for a in range(1, 9):
        for m in odd_primes_50:
            if (criterion_P1(a, m) is not None) != (rank_apparition(a, m) % 4 == 2):
                mism.append((a, m))
    allok &= check(
        "D5 criterion == (z(m) mod 4 == 2), a<=8, odd primes m<=50",
        not mism,
        f"mismatches: {mism}",
    )

    print()
    print("ALL GREEN" if allok else "SOME CHECKS FAILED")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
