"""
FRAME STEP 3(d): DESIGNED RAMIFICATION -- the predictive test.

The places frame must name one result the sieve frame would not have
asked for (the frame's third gate). This is the (d) test: the
division-ladder chart (explore_division_ladder.py) found floor 2 (quaternions over the tower)
splitting to M_2(F_p) at every odd channel with channel 2 degenerate,
and a later audit read that shape as the Hamilton quaternions'
classical ramification set {2, infinity} seen through residue windows
with infinity deleted -- channel 2 CONFOUNDED, because the naive
(a,b) presentation degenerates in char 2 unconditionally (ij = -ji
collapses to commutativity when -1 = 1). If the ramification reading
is right, ramification sets over Q are DESIGNABLE (Hilbert
reciprocity: any even-size set of places), and the weird channels of
a maximal order's reductions should be exactly the designed finite
places -- with channel 2 SPLIT whenever 2 is not designed. The sieve
frame has no reason to single out any channel before computing; the
places frame predicts the full pattern from Hilbert symbols, one of
which lives at the place the tower deleted.

THE PREDICTIONS (stated before computing).
Four quaternion algebras (a,b | Q), each given by a maximal order
(maximality certified by reduced discriminant = product of designed
finite primes), reduced at every RAD channel p in {2,3,5,7,11,13,17}.
M2 = the reduction is isomorphic to M_2(F_p) (split); LOCAL = the
reduction is a local algebra, radical of dim 2, residue field F_p^2
(ramified). Predicted verdicts:

  algebra     designed ramification   LOCAL at      M2 at
  (5,3)       {3, 5}                  3, 5          2, 7, 11, 13, 17
  (77,-1)     {7, 11}                 7, 11         2, 3, 5, 13, 17
  (-1,-1)     {2, infinity}           2             3, 5, 7, 11, 13, 17
  (-3,-1)     {3, infinity}           3             2, 5, 7, 11, 13, 17

  - 28 channel verdicts, all stated in advance. Channel 2 is the
    kill switch: it must SPLIT for (5,3), (77,-1), (-3,-1) and stay
    LOCAL only for (-1,-1). Failure at channel 2 kills the floor-2
    ramification reading (Step 3(d) of the frame gate).
  - The naive order Z<1,i,j,k> mod 2 is predicted COMMUTATIVE (hence
    never M_2) for ALL four algebras -- the confound from
    explore_division_ladder.py, exhibited.
  - (-3,-1) is the frame's own specimen: reciprocity forces ramification
    sets of even size, but only over ALL places -- the tower-visible
    weird set {3} is ODD-sized because the partner ramification sits at
    the deleted place. The sieve frame cannot state this design rule.

Survey anchors (classical, named so nothing poses as new): Hilbert
symbols (a,b)_v and their explicit formulas (Serre, A Course in
Arithmetic III), Hilbert reciprocity prod_v (a,b)_v = +1, quaternion
algebras ramified at an even set of places with reduced discriminant
= product of the finite ramified primes; maximal orders: d(O) = d(A)
iff O maximal (Voight, Quaternion Algebras); O/pO = M_2(F_p) at
unramified p, and at ramified p a local algebra with radical = the
maximal ideal, residue field F_{p^2} (Deuring/Eichler); Wedderburn
(finite division rings are fields -- so a 4-dim semisimple
noncommutative F_p-algebra is M_2(F_p)); Dickson (rad subset of the
regular trace form's kernel, in any characteristic); Pearl 1968
(Moore-Penrose over F_p exists iff rank(AA^T) = rank(A^T A) =
rank(A)); Chevalley-Warning (forms in >= 3 variables are isotropic
over every F_p). Our content is the tower-side composition: the
designed channel pattern as a PREDICTION, verified at every rung
window.

Findings preview (full statements at the bottom):
  1. DESIGNED RAMIFICATION LANDS (rule + classical): all 28 predicted
     channel verdicts hold -- weird channels are exactly the designed
     finite places, channel 2 splits whenever 2 is undesigned.
  2. THE CONFOUND EXHIBITED (rule): every naive order is commutative
     mod 2; the channel-2 degeneration found in explore_division_ladder.py
     was the presentation -- it is
     real (survives the maximal order) exactly when 2 is designed.
  3. THE DELETED PLACE CARRIES PARITY (rule + classical): (-3,-1)
     realizes a visible weird-set of size ONE -- evenness is conserved
     only across all places, and the tower deleted one.
  4. RAMIFIED SHAPE (rule): at each designed channel the reduction is
     local with rad of dim 2 and residue field F_{p^2} -- the channel
     does not vanish, it FATTENS to the quadratic extension.
  5. OPEN QUESTION SETTLED (rule): 3x3 Moore-Penrose totality fails at
     EVERY RAD channel (isotropic 3-vectors exist at every p) -- the
     decality found in explore_division_ladder.py
     (MP total iff p = 3 mod 4) is 2x2-specific.

Pure Python (fractions), no numpy. ~0.5 s, ~14 MB.
"""

from fractions import Fraction
from itertools import product as iproduct

RAD_PRIMES = (2, 3, 5, 7, 11, 13, 17)

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

# ----------------------------------------------------------------------
# Quaternion arithmetic over Q in the basis (1, i, j, k):
# i^2 = a, j^2 = b, k = ij = -ji, k^2 = -ab, ik = aj, ki = -aj,
# jk = -bi, kj = bi.
# ----------------------------------------------------------------------

def qmul(x, y, a, b):
    t1, x1, y1, z1 = x
    t2, x2, y2, z2 = y
    return (t1*t2 + a*x1*x2 + b*y1*y2 - a*b*z1*z2,
            t1*x2 + x1*t2 - b*y1*z2 + b*z1*y2,
            t1*y2 + y1*t2 + a*x1*z2 - a*z1*x2,
            t1*z2 + z1*t2 + x1*y2 - y1*x2)

def qconj(x):
    t, u, v, w = x
    return (t, -u, -v, -w)

def trd(x):
    return 2 * x[0]

# ----------------------------------------------------------------------
# Exact linear algebra over Q (Fractions)
# ----------------------------------------------------------------------

def solve_frac(cols, v):
    """Solve sum_c cols[c]*sol[c] = v exactly. cols, v: 4-vectors."""
    n = 4
    A = [[Fraction(cols[c][r]) for c in range(n)] + [Fraction(v[r])]
         for r in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [e / pv for e in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [er - f * ec for er, ec in zip(A[r], A[col])]
    return [A[r][n] for r in range(n)]

def det_frac(M):
    n = len(M)
    A = [[Fraction(e) for e in row] for row in M]
    det = Fraction(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        for r in range(col + 1, n):
            if A[r][col] != 0:
                f = A[r][col] * inv
                A[r] = [er - f * ec for er, ec in zip(A[r], A[col])]
    return det

# ----------------------------------------------------------------------
# Linear algebra mod p
# ----------------------------------------------------------------------

def rref_modp(rows, p):
    M = [[e % p for e in row] for row in rows]
    pivots, r = [], 0
    ncols = len(M[0]) if M else 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(M)) if M[i][c]), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(e * inv) % p for e in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(ei - f * er) % p for ei, er in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
        if r == len(M):
            break
    return M, pivots

def rank_modp(rows, p):
    return len(rref_modp(rows, p)[1]) if rows else 0

def kernel_modp(rows, p, n):
    """Kernel basis of the n-column matrix `rows` mod p."""
    R, piv = rref_modp(rows, p)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for r, pc in enumerate(piv):
            v[pc] = (-R[r][fc]) % p
        basis.append(v)
    return basis

def in_span(basis, v, p):
    if not basis:
        return all(e % p == 0 for e in v)
    return rank_modp(basis + [list(v)], p) == rank_modp(basis, p)

# ----------------------------------------------------------------------
# Hilbert symbols (classical formulas; Serre III)
# ----------------------------------------------------------------------

def legendre(u, p):
    u %= p
    if u == 0:
        return 0
    return 1 if pow(u, (p - 1) // 2, p) == 1 else -1

def vp(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a, n

def hilbert_odd(a, b, p):
    al, u = vp(a, p)
    be, v = vp(b, p)
    s = 1
    if (al * be * ((p - 1) // 2)) % 2:
        s = -s
    if be % 2:
        s *= legendre(u, p)
    if al % 2:
        s *= legendre(v, p)
    return s

def hilbert_2(a, b):
    al, u = vp(a, 2)
    be, v = vp(b, 2)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = eps(u) * eps(v) + al * om(v) + be * om(u)
    return -1 if e % 2 else 1

def hilbert_inf(a, b):
    return -1 if (a < 0 and b < 0) else 1

def ramification_set(a, b):
    """Finite ramified places + 'inf' flag; checks reciprocity."""
    places = sorted(set(abs(p) for p in _prime_factors(abs(a * b)) if p != 2))
    fin, prodall = [], hilbert_inf(a, b) * hilbert_2(a, b)
    if hilbert_2(a, b) == -1:
        fin.append(2)
    for p in places:
        s = hilbert_odd(a, b, p)
        prodall *= s
        if s == -1:
            fin.append(p)
    assert prodall == 1, "Hilbert reciprocity violated -- formula bug"
    return sorted(fin), hilbert_inf(a, b) == -1

def _prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

# ----------------------------------------------------------------------
# Orders: structure constants, reduced discriminant
# ----------------------------------------------------------------------

def structure_constants(basis, a, b):
    """C[x][y] = integer coords of e_x*e_y in the order basis.
    AssertionError if the lattice is not closed under multiplication."""
    cols = [list(e) for e in basis]
    C = [[None] * 4 for _ in range(4)]
    for x in range(4):
        for y in range(4):
            sol = solve_frac(cols, qmul(basis[x], basis[y], a, b))
            assert all(s.denominator == 1 for s in sol), \
                f"order not multiplicatively closed at e{x}*e{y}"
            C[x][y] = [int(s) for s in sol]
    return C

def reduced_disc(basis, a, b):
    G = [[trd(qmul(basis[r], qconj(basis[c]), a, b)) for c in range(4)]
         for r in range(4)]
    det = det_frac(G)
    d2 = abs(int(det))
    d = round(d2 ** 0.5)
    while d * d < d2:
        d += 1
    assert d * d == d2, "discriminant not a perfect square"
    return d

# ----------------------------------------------------------------------
# The reduced algebra O/pO and its verdict
# ----------------------------------------------------------------------

class FpAlg:
    """4-dim F_p-algebra from integer structure constants."""
    def __init__(self, C, p):
        self.p = p
        self.C = [[[c % p for c in C[x][y]] for y in range(4)]
                  for x in range(4)]
        self.basis = [tuple(1 if c == x else 0 for c in range(4))
                      for x in range(4)]

    def mul(self, x, y):
        p, C = self.p, self.C
        z = [0, 0, 0, 0]
        for xa in range(4):
            if not x[xa]:
                continue
            for yb in range(4):
                if not y[yb]:
                    continue
                f = x[xa] * y[yb]
                Cxy = C[xa][yb]
                for c in range(4):
                    z[c] += f * Cxy[c]
        return tuple(v % p for v in z)

    def nilpotent(self, x):
        # dim 4: the regular representation is a 4x4 matrix, so
        # nilpotency index <= 4 -- x^4 = 0 decides.
        x2 = self.mul(x, x)
        x4 = self.mul(x2, x2)
        return x4 == (0, 0, 0, 0)

    def noncommutative(self):
        return any(self.mul(ea, eb) != self.mul(eb, ea)
                   for ea in self.basis for eb in self.basis)

    def gram(self):
        """Gram matrix of the regular trace form T(x,y) = tr L_{xy}."""
        p, C = self.p, self.C
        tr_e = [sum(C[c][bb][bb] for bb in range(4)) % p for c in range(4)]
        return [[sum(C[x][y][c] * tr_e[c] for c in range(4)) % p
                 for y in range(4)] for x in range(4)]

    def radical(self):
        """Jacobson radical as a basis (list of 4-vectors).

        rad is always inside the regular trace form's kernel K (x in
        rad makes every xy nilpotent in the regular rep, so tr = 0 --
        Dickson, any characteristic).  For p <= 3 the converse can
        fail (char <= dim), so brute-force the exact radical there:
        rad = {x : xa nilpotent for all a} (the largest right ideal
        of nilpotents).  For p >= 5: if K = 0, rad = 0; if K != 0,
        verify K is a two-sided nil ideal, which forces rad = K."""
        p = self.p
        if p <= 3:
            elems = list(iproduct(range(p), repeat=4))
            rad = [list(x) for x in elems
                   if all(self.nilpotent(self.mul(x, aa)) for aa in elems)]
            R, piv = rref_modp(rad, p) if rad else ([], [])
            basis = [R[r] for r in range(len(piv))]
            assert len(rad) == p ** len(basis), "radical not a subspace?"
            return basis
        K = kernel_modp(self.gram(), p, 4)
        if not K:
            return []
        # verify two-sided ideal
        for kv in K:
            for e in self.basis:
                assert in_span(K, self.mul(e, tuple(kv)), p), "K not left ideal"
                assert in_span(K, self.mul(tuple(kv), e), p), "K not right ideal"
        # verify nil (enumerate the span -- dim K <= 2 expected, p^2 small)
        for coeffs in iproduct(range(p), repeat=len(K)):
            v = tuple(sum(c * kv[idx] for c, kv in zip(coeffs, K)) % p
                      for idx in range(4))
            assert self.nilpotent(v), "kernel element not nilpotent"
        return K

def quotient_field_check(alg, rad_basis):
    """A/rad for dim(rad) = 2: certify the residue ring is F_{p^2}.
    The three 2-dim unital F_p-algebras are F_{p^2}, F_p x F_p,
    F_p[eps] (classical); idempotent count 2 + no nonzero square-zero
    elements pins F_{p^2}."""
    p = alg.p
    assert len(rad_basis) == 2
    # complete rad_basis to a basis of F_p^4
    full = [list(v) for v in rad_basis]
    for e in alg.basis:
        if rank_modp(full + [list(e)], p) > rank_modp(full, p):
            full.append(list(e))
        if len(full) == 4:
            break
    cols = [[full[c][r] for c in range(4)] for r in range(4)]
    inv = _mat_inv_modp(cols, p)
    def coords(x):
        return tuple(sum(inv[r][c] * x[c] for c in range(4)) % p
                     for r in range(4))
    def proj(x):          # quotient coords = components along full[2], full[3]
        return coords(x)[2:]
    def rep(q):           # a coset representative
        return tuple((q[0] * full[2][c] + q[1] * full[3][c]) % p
                     for c in range(4))
    idem = sqzero = 0
    comm = True
    for q in iproduct(range(p), repeat=2):
        x = rep(q)
        if proj(alg.mul(x, x)) == q:
            idem += 1
        if q != (0, 0) and proj(alg.mul(x, x)) == (0, 0):
            sqzero += 1
    for q1 in iproduct(range(p), repeat=2):
        for q2 in iproduct(range(p), repeat=2):
            if proj(alg.mul(rep(q1), rep(q2))) != proj(alg.mul(rep(q2), rep(q1))):
                comm = False
    assert comm, "2-dim quotient must be commutative"
    return idem == 2 and sqzero == 0

def _mat_inv_modp(M, p):
    n = len(M)
    aug = [M[r][:] + [1 if c == r else 0 for c in range(n)] for r in range(n)]
    R, piv = rref_modp(aug, p)
    assert piv == list(range(n)), "matrix not invertible mod p"
    return [row[n:] for row in R]

def channel_verdict(C, p):
    """Return ('M2',) or ('LOCAL', rad_dim, quotient_is_Fp2)."""
    alg = FpAlg(C, p)
    rad = alg.radical()
    if not rad:
        # semisimple; 4-dim noncommutative over F_p forces M_2(F_p)
        # (Wedderburn: no finite division rings beyond fields)
        assert alg.noncommutative(), "semisimple but commutative -- not M2"
        return ("M2",)
    fp2 = quotient_field_check(alg, rad) if len(rad) == 2 else False
    return ("LOCAL", len(rad), fp2)

# ----------------------------------------------------------------------
# The specimens
# ----------------------------------------------------------------------

HALF = Fraction(1, 2)

def order_a1mod4(a, b):
    """Basis (1, (1+i)/2, j, (j+k)/2) -- an order whenever a = 1 mod 4."""
    return [(1, 0, 0, 0), (HALF, HALF, 0, 0), (0, 0, 1, 0),
            (0, 0, HALF, HALF)]

def order_hurwitz():
    """Basis (1, i, j, (1+i+j+k)/2) -- the Hurwitz order for (-1,-1)."""
    return [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0),
            (HALF, HALF, HALF, HALF)]

NAIVE = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

SPECIMENS = [
    ("(5,3)",   5,  3, order_a1mod4(5, 3),    {3, 5},  False),
    ("(77,-1)", 77, -1, order_a1mod4(77, -1), {7, 11}, False),
    ("(-1,-1)", -1, -1, order_hurwitz(),      {2},     True),
    ("(-3,-1)", -3, -1, order_a1mod4(-3, -1), {3},     True),
]

# THE PREDICTION TABLE -- written before computing.
PREDICTED = {}
for name, _, _, _, ram_fin, _ in SPECIMENS:
    for p in RAD_PRIMES:
        PREDICTED[(name, p)] = "LOCAL" if p in ram_fin else "M2"

# ----------------------------------------------------------------------
section("0. THE PREDICTIONS (before any computation)")
# ----------------------------------------------------------------------
print(f"{'algebra':10s} {'designed ram.':16s} " +
      " ".join(f"{p:>5d}" for p in RAD_PRIMES))
for name, _, _, _, ram_fin, ram_inf in SPECIMENS:
    ram = sorted(ram_fin) + (["inf"] if ram_inf else [])
    row = " ".join(f"{PREDICTED[(name, p)]:>5s}" for p in RAD_PRIMES)
    print(f"{name:10s} {str(ram):16s} {row}")
print("\nKill switch: channel 2 must read M2 for (5,3), (77,-1), (-3,-1).")
print("Also predicted: all four NAIVE orders are commutative mod 2.")

# ----------------------------------------------------------------------
section("I. THE DESIGN LAYER: HILBERT SYMBOLS (classical)")
# ----------------------------------------------------------------------
for name, a, b, _, ram_fin, ram_inf in SPECIMENS:
    fin, inf = ramification_set(a, b)
    print(f"{name:10s} ramified at finite {fin} + " +
          ("inf" if inf else "(inf split)") +
          f"   [reciprocity product = +1 OK]")
    assert set(fin) == ram_fin and inf == ram_inf, "design failed"
    assert (len(fin) + (1 if inf else 0)) % 2 == 0, "odd total ramification?"
print("\nAll four sets are as designed; every TOTAL set is even (reciprocity)")
print("-- but the visible (finite) set of (-3,-1) is {3}, ODD-sized: the")
print("partner ramification sits at the deleted place.")

# ----------------------------------------------------------------------
section("II. MAXIMAL ORDERS: closure + reduced discriminant")
# ----------------------------------------------------------------------
SC = {}
for name, a, b, basis, ram_fin, _ in SPECIMENS:
    C = structure_constants(basis, a, b)        # asserts closure
    SC[name] = C
    d = reduced_disc(basis, a, b)
    d_target = 1
    for q in sorted(ram_fin):
        d_target *= q
    d_naive = reduced_disc(NAIVE, a, b)
    print(f"{name:10s} d(O) = {d:3d} = prod(designed finite primes) "
          f"= {d_target}   [naive order: d = {d_naive}]")
    assert d == d_target, "order not maximal -- discriminant too big"
print("\nd(O) = d(A) certifies maximality (classical); the naive order is")
print("non-maximal at 2 in every case (factor 4 or 2 left over).")

# ----------------------------------------------------------------------
section("III. THE TEST: REDUCTION AT EVERY RAD CHANNEL")
# ----------------------------------------------------------------------
computed = {}
mismatches = []
print(f"{'algebra':10s} " + " ".join(f"{p:>5d}" for p in RAD_PRIMES))
for name, a, b, basis, ram_fin, _ in SPECIMENS:
    row = []
    for p in RAD_PRIMES:
        v = channel_verdict(SC[name], p)
        computed[(name, p)] = v[0]
        row.append(v[0])
        if v[0] != PREDICTED[(name, p)]:
            mismatches.append((name, p, PREDICTED[(name, p)], v[0]))
    print(f"{name:10s} " + " ".join(f"{r:>5s}" for r in row))
n_cells = len(PREDICTED)
print(f"\n{n_cells - len(mismatches)}/{n_cells} predicted verdicts hold; "
      f"mismatches: {mismatches if mismatches else 'NONE'}")
assert not mismatches, f"PREDICTION FAILED: {mismatches}"

# ----------------------------------------------------------------------
section("IV. THE CONFOUND: NAIVE ORDERS MOD 2")
# ----------------------------------------------------------------------
for name, a, b, basis, _, _ in SPECIMENS:
    Cn = structure_constants(NAIVE, a, b)
    alg2 = FpAlg(Cn, 2)
    comm = not alg2.noncommutative()
    print(f"{name:10s} naive Z<1,i,j,k> mod 2: "
          f"{'COMMUTATIVE (never M_2)' if comm else 'noncommutative'}")
    assert comm, "naive order mod 2 should be commutative (ij = -ji = ji)"
print("\nThe channel-2 degeneration from explore_division_ladder.py was the PRESENTATION: it afflicts")
print("split and ramified algebras alike. The maximal order removes it --")
print("and what remains (Hurwitz still LOCAL at 2) is real ramification.")

# ----------------------------------------------------------------------
section("V. THE RAMIFIED SHAPE: rad dim 2, residue field F_{p^2}")
# ----------------------------------------------------------------------
for name, a, b, basis, ram_fin, _ in SPECIMENS:
    for p in sorted(ram_fin):
        v = channel_verdict(SC[name], p)
        assert v == ("LOCAL", 2, True), f"unexpected ramified shape: {v}"
        print(f"{name:10s} at channel {p:2d}: local, dim(rad) = 2, "
              f"O/pO mod rad = F_{p}^2 (field certified)")
print("\nA designed channel does not vanish -- it FATTENS: the residue")
print("field doubles to F_{p^2} (Deuring/Eichler shape, verified).")

# ----------------------------------------------------------------------
section("VI. OPEN QUESTION: 3x3 MOORE-PENROSE AT EVERY CHANNEL")
# ----------------------------------------------------------------------
# explore_division_ladder.py (2x2): MP total iff p = 3 mod 4; failure set = rank-1 matrices
# with isotropic row/column space. Open question: is the
# decality 2x2-specific? At n = 3 the dot form x^2+y^2+z^2 is isotropic
# over EVERY F_p (Chevalley-Warning), so a rank-1 witness A = u w^T with
# w isotropic has rank(AA^T) = 0 != 1 = rank(A) -- the Pearl criterion
# fails and MP(A) does not exist, at every channel.

def _mm3(X, Y, p):
    return [[sum(X[r][t] * Y[t][c] for t in range(3)) % p
             for c in range(3)] for r in range(3)]

def _t3(X):
    return [[X[c][r] for c in range(3)] for r in range(3)]

witness = {}
for p in RAD_PRIMES:
    w = next((x, y, z) for x in range(p) for y in range(p)
             for z in range(p)
             if (x or y or z) and (x*x + y*y + z*z) % p == 0)
    u = (1, 0, 0)
    A = [[(u[r] * w[c]) % p for c in range(3)] for r in range(3)]
    witness[p] = A
    At = _t3(A)
    rA, rAAt, rAtA = rank_modp(A, p), rank_modp(_mm3(A, At, p), p), \
                     rank_modp(_mm3(At, A, p), p)
    print(f"p = {p:2d}: isotropic w = {w}, rank(A) = {rA}, "
          f"rank(AA^T) = {rAAt}, rank(A^T A) = {rAtA} -> MP fails")
    assert rA == 1 and rAAt == 0, "witness construction broken"

# Criterion-independent corroboration at p = 2, 3: exhaust ALL p^9
# candidate G against the four Penrose equations (AGA = A, GAG = G,
# (AG)^T = AG, (GA)^T = GA) -- no solution exists.
for p in (2, 3):
    A = witness[p]
    found = 0
    for entries in iproduct(range(p), repeat=9):
        G = [list(entries[0:3]), list(entries[3:6]), list(entries[6:9])]
        AG, GA = _mm3(A, G, p), _mm3(G, A, p)
        if (_mm3(AG, A, p) == A and _mm3(GA, G, p) == G
                and _t3(AG) == AG and _t3(GA) == GA):
            found += 1
    print(f"p = {p}: {found} of {p**9} candidate G satisfy all four "
          f"Penrose equations (exhaustive)")
    assert found == 0, "MP inverse exists -- criterion misapplied"
print("\nMP totality at 3x3 fails at EVERY channel (and any n >= 3 by")
print("zero-padding): the decality found in explore_division_ladder.py is 2x2-specific. Open question settled.")

# ----------------------------------------------------------------------
section("FINDINGS")
# ----------------------------------------------------------------------
print("""
1. DESIGNED RAMIFICATION LANDS (rule + classical): 28/28 predicted
   channel verdicts hold. Weird channels are exactly the designed
   finite places -- {3,5} for (5,3), {7,11} for (77,-1), {2} for
   (-1,-1), {3} for (-3,-1) -- and channel 2 SPLITS in the three
   designs that leave it out. The kill switch did not fire.

2. THE CONFOUND EXHIBITED (rule): all four naive orders Z<1,i,j,k>
   are commutative mod 2 (ij = -ji = ji in char 2) -- the channel-2
   degeneration found in explore_division_ladder.py was the presentation. Replacing the naive order by a
   maximal one removes the artifact, and what survives (Hurwitz local
   at 2) is real ramification.

3. THE DELETED PLACE CARRIES PARITY (rule + classical): reciprocity
   makes TOTAL ramification sets even, but the tower sees only finite
   places -- (-3,-1) realizes a visible weird-set of size ONE, the
   partner sitting at the deleted place. The design rule for weird
   channel sets cannot be stated inside the sieve frame.

4. THE RAMIFIED SHAPE (rule): at each designed channel, O/pO is local
   with dim(rad) = 2 and residue field F_{p^2} -- the channel fattens
   to the quadratic extension instead of splitting.

5. OPEN QUESTION SETTLED (rule): 3x3 Moore-Penrose totality fails at every
   RAD channel (Chevalley-Warning isotropy breaks the Pearl
   criterion; criterion-independent at p = 2, 3 -- zero of the p^9
   candidate inverses satisfy the four Penrose equations); the
   decality found in explore_division_ladder.py (MP total iff p = 3 mod 4) is 2x2-specific.

FRAME VERDICT: Step 3 gate PASSED -- a designable weird-channel
pattern, predicted in advance from Hilbert symbols (one of which
lives at the deleted place), verified 28/28 at the rung windows.
""")
