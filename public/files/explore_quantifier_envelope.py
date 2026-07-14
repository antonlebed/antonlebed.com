"""
The quantifier envelope: the pair as a two-sided certificate (STITCH probe, P71).

Builds on the quantifier pair (P66, LOGIC.md SI): DIA(a) = a^lambda
("true to SOME degree": channel bit 1 iff residue != 0) and its De Morgan
conjugate BOX(a) = 1 - (1-a)^lambda ("FULLY true": 1 iff residue = 1),
with DIA NOT = NOT BOX exactly, DIA exact on AND, BOX exact on OR, each
leaking ONE-DIRECTIONALLY on the dual connective (p-2 pairs per channel).

THE QUESTION (the ROAD bar): does the PAIR decide something a plain
idempotent mask cannot? A mask e_S selects channels; DIA alone is the
data-computed mask (the P37 measurement). The probe: evaluate any
formula's classical shadow from MEASUREMENTS ONLY -- per leaf, the two
bits (DIA a, BOX a) -- and certify verdicts where possible.

THE ENVELOPE. Push NOT to the leaves (negation normal form; De Morgan
survives identically off the lattice). Define, per formula F:
    roof  U(F): leaf a -> DIA a, leaf NOT a -> NOT BOX a, then evaluate
                the AND/OR tree as Boolean logic on the bits.
    floor L(F): leaf a -> BOX a, leaf NOT a -> NOT DIA a, ditto.
Both are Boolean evaluations of measurement bits -- no graded value is
touched past the two collapses per leaf.

PREDICTIONS (stated before the run):
 P1 (rule, proved): channel-wise, for EVERY NNF formula and all inputs,
    L(F) <= BOX F <= DIA F <= U(F).
    Proof by induction. Literals: exact on both ends -- DIA(NOT a) =
    NOT BOX a IS the conjugacy. AND node: DIA(fg) = DIA f AND DIA g
    (fields, exact) <= U(f) AND U(g) by monotonicity; BOX(fg) >=
    BOX f AND BOX g (the inversion gain is one-directional) >= L AND L.
    OR node: dual -- BOX exact, DIA loses one-directionally. The P66
    leak directions are exactly the two inequality slots; nothing else
    is used. COROLLARY (the decision): U = 0 certifies the shadow
    false, L = 1 certifies it fully true, U = L certifies the verdict
    outright -- sound by P1.
 P2 (rule): the gap is located -- the uncertainty region U AND NOT L
    lies inside the UNION of the inputs' defect supports (finding 6's
    no-creation law in envelope dress): a channel where every input is
    classical has U = L = the classical evaluation. At a single
    literal the region IS the defect support exactly:
    DIA a - BOX a = DIA(delta(a)) -- equivalently DIA a AND DIA(NOT a)
    = DIA(delta(a)): the measured-contradiction identity (the pair's
    gap is the measurement of the defect).
 P3 (the bar, demonstrated): reading the roof alone as the verdict
    (DIA-only -- the measurement-as-mask) errs at a measured nonzero
    rate; PAIR-CERTIFIED verdicts err NEVER (zero over the full
    censuses + ring-level samples). DIA alone certifies only falsity,
    BOX alone only full truth; deciding both ways needs the pair, and
    every negated leaf needs the conjugacy.
 P4 (slack rates, exact): envelope slack enters only at DIA-of-OR
    (destructive interference, (1-x)(1-y) = 1) and BOX-of-AND
    (inversion, xy = 1), each on exactly p-2 of the (p-1)^2
    relevant pairs per channel -- the P66 counts, re-derived here as
    envelope-slack counts.
 P5 (sharpness): for READ-ONCE formulas the envelope is ACHIEVED at
    every p >= 5: max achievable DIA F over inputs consistent with the
    measurements = U, min achievable BOX F = L (exhaustive over the
    formula family by exact set-composition). At p = 3 both ends can
    be unreachable -- the graded region of F_3 is the single point -1,
    self-inverse and with 1-(-1) = -1 self-inverse too, so the OR
    interference (-1 OR -1 = -3 = 0) and the AND inversion
    ((-1)(-1) = 1) are FORCED: the p = 3 rigidity. Repeated leaves
    can break achievability at any p (the dependency problem --
    the interval-arithmetic contact); searched and reported.

RESULTS (the run below prints the record; P5's repeated-leaf clause
half-falsified, re-encoded -- everything else confirmed):
  P1 sandwich: zero violations anywhere -- exhaustive per channel
     (2-leaf trees all p <= 23: 12,448; 3-leaf p <= 13: 257,984;
     4-leaf p <= 7: 1,998,720; 3-leaf trees on TWO vars, repeated
     leaves: 193,024) + 40,000 random formula-input pairs (to 6
     leaves, p <= 23) + 2,000 ring-level RAD samples through crt.py
     pow collapses, channel-wise.
  P2 gap location: uncertainty inside the defect union, exhaustive +
     sampled, zero escapes; the literal identities DIA - BOX =
     DIA(delta) and DIA a AND DIA(NOT a) = DIA(delta) exhaustive all
     channels + ring-level.
  P3 the bar: demo formula (a AND b) OR (c AND d) under the
     classical-leaning mixture (gamma = 0.1): pair-certified verdicts
     0 errors / 127,371 certified channel-verdicts (20,000 RAD
     tuples); DIA-only roof-as-verdict errs 79 times on the same
     stream. Exact per-channel rates by full weighted enumeration
     (p^4 tuples): P[certified] = 1 at channel 2 (no graded region),
     falling 0.950 -> 0.868 from p = 3 to 17 (the graded-leaf
     probability gamma(p-2)/p grows with p); P[certified & wrong] =
     0.000000 exactly, every channel; DIA-only error mass > 0 on
     every odd channel. Sample matches enumeration within 3 sigma
     per channel; all-7-certified rate 0.5098 vs predicted 0.5137
     (channel independence by CRT).
  P4 slack counts: exactly p-2 interference pairs (OR) and p-2
     inversion pairs (AND) per channel, every odd p <= 23.
  P5 sharpness: read-once achievability ZERO violations at p = 5, 7,
     11 (53,646 cells each: all trees to 4 leaves x polarities x
     class profiles, exact set-composition); at p = 3, 3,700 roof +
     3,700 floor unreachable cells -- the rigidity, exactly as
     predicted ((-1) OR (-1) = 0, (-1) AND (-1) = 1, both forced).
     Repeated leaves, HALF-FALSIFIED: in the one-variable family
     (trees to 3 leaves, fiber-exact) violations occur ONLY at p = 3
     (20 roof + 20 floor of 216 cells; single-point graded fiber);
     at p = 5..13 the envelope is still achieved -- the dependency
     problem shows instead as genuinely dependent shadows inside the
     bracket (a AND NOT a is FULLY TRUE wherever delta(x) = -1 is
     solvable, p = 3 or p = 1 mod 3, while its floor is identically
     0). Multi-variable repeated-leaf families beyond this sweep:
     open.

Tier: P1, P2, P4 rule (proved by the induction above; verified
exhaustively per channel as stated). P5 rule for the swept families
(read-once p = 3, 5, 7, 11; one-variable p <= 13), observation
beyond. P3 empirical demonstration with exact enumerated rates.

Runs on RAD (k = 7) with exhaustive per-channel censuses. ~6 s, tiny
memory. ALL CHECKS PASSED (28).
"""

import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING, encode, decode

random.seed(71)
R = RAD_RING
N, LAM, PRIMES = R.N, R.lam, R.primes
ODD = [p for p in PRIMES if p > 2]          # graded region empty at p = 2

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    status = "ok" if cond else "FAIL"
    print(f"  [{status}] {msg}")
    assert cond, msg

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

# ── the pair, per channel (field F_p, lambda_p = p-1; Fermat) ──────────
def dia(x, p):  return 0 if x % p == 0 else 1
def box(x, p):  return 1 if x % p == 1 else 0

# ── formulas: ('lit', var, pol) | ('and', f, g) | ('or', f, g) ─────────
def eval_graded(F, xs, m):
    """Evaluate F with the ring polynomials AND=ab, OR=a+b-ab, NOT=1-a."""
    if F[0] == 'lit':
        v = xs[F[1]] % m
        return v if F[2] else (1 - v) % m
    a, b = eval_graded(F[1], xs, m), eval_graded(F[2], xs, m)
    return a * b % m if F[0] == 'and' else (a + b - a * b) % m

def eval_env(F, meas, upper):
    """Roof (upper=True) / floor: Boolean evaluation of measurement bits.
    meas[var] = (dia_bit, box_bit) of the POSITIVE literal."""
    if F[0] == 'lit':
        d, bx = meas[F[1]]
        if F[2]:
            return d if upper else bx
        return (1 - bx) if upper else (1 - d)    # the conjugacy at the leaf
    a, b = eval_env(F[1], meas, upper), eval_env(F[2], meas, upper)
    return a & b if F[0] == 'and' else a | b

def gen_trees(nleaves):
    """All AND/OR tree skeletons with nleaves leaf slots (slots numbered
    left to right); leaf polarity assigned later."""
    if nleaves == 1:
        return [('slot',)]
    out = []
    for i in range(1, nleaves):
        for lt in gen_trees(i):
            for rt in gen_trees(nleaves - i):
                for op in ('and', 'or'):
                    out.append((op, lt, rt))
    return out

def instantiate(tree, vars_, pols, counter=None):
    """Fill slots left-to-right with (var, pol)."""
    if counter is None:
        counter = [0]
    if tree[0] == 'slot':
        i = counter[0]; counter[0] += 1
        return ('lit', vars_[i], pols[i])
    return (tree[0], instantiate(tree[1], vars_, pols, counter),
                     instantiate(tree[2], vars_, pols, counter))

def nslots(tree):
    return 1 if tree[0] == 'slot' else nslots(tree[1]) + nslots(tree[2])

def formulas(nleaves, var_pool=None):
    """All formulas with nleaves leaves; vars distinct (read-once) unless
    var_pool given (then all assignments from the pool)."""
    for tree in gen_trees(nleaves):
        pools = ([tuple(range(nleaves))] if var_pool is None
                 else itertools.product(var_pool, repeat=nleaves))
        for vars_ in pools:
            for pols in itertools.product((1, 0), repeat=nleaves):
                yield instantiate(tree, vars_, pols)

# ───────────────────────────────────────────────────────────────────────
section("I. THE LITERAL LAYER: conjugacy + the gap identity (P2 literal case)")
# ───────────────────────────────────────────────────────────────────────
# DIA(NOT a) = NOT BOX a; DIA a - BOX a = DIA(delta(a));
# DIA a AND DIA(NOT a) = DIA(delta(a)).   Exhaustive per channel, then
# ring-level through the actual pow collapses.

ok_conj = ok_gap = ok_contra = ok_ind = True
for p in PRIMES:
    lam_p = p - 1
    for x in range(p):
        D  = pow(x, lam_p, p)
        Bx = (1 - pow((1 - x) % p, lam_p, p)) % p
        Dn = pow((1 - x) % p, lam_p, p)
        Dd = pow((x * x - x) % p, lam_p, p)
        if D != dia(x, p) or Bx != box(x, p):           ok_ind = False
        if Dn != (1 - Bx) % p:                          ok_conj = False
        if (D - Bx) % p != Dd:                          ok_gap = False
        if (D * Dn) % p != Dd:                          ok_contra = False
check(ok_ind,   "pow-collapse bits = indicator bits (Fermat), all channels exhaustive")
check(ok_conj,  "DIA(NOT a) = NOT BOX a, all channels exhaustive")
check(ok_gap,   "DIA a - BOX a = DIA(delta(a)), all channels exhaustive")
check(ok_contra,"DIA a AND DIA(NOT a) = DIA(delta(a)) (measured contradiction)")

ok_ring = True
for _ in range(2000):
    a = random.randrange(N)
    D  = pow(a, LAM, N)
    Bx = (1 - pow((1 - a) % N, LAM, N)) % N
    if (D - Bx) % N != pow((a * a - a) % N, LAM, N):
        ok_ring = False
check(ok_ring, "ring-level gap identity, 2000 RAD samples through a^lambda")

# ───────────────────────────────────────────────────────────────────────
section("II. THE SANDWICH (P1) + GAP LOCATION (P2): exhaustive per channel")
# ───────────────────────────────────────────────────────────────────────
# L <= BOX F <= DIA F <= U channel-wise, and U AND NOT L = 0 wherever
# every input is classical. Exhaustive: 2-leaf trees all p <= 23,
# 3-leaf p <= 13, 4-leaf p <= 7; repeated-variable trees included
# (soundness never uses independence).

def sandwich_census(nleaves, ps, var_pool):
    nvars = nleaves if var_pool is None else len(var_pool)
    tested = 0
    for p in ps:
        fams = list(formulas(nleaves, var_pool))
        for xs in itertools.product(range(p), repeat=nvars):
            meas = [(dia(x, p), box(x, p)) for x in xs]
            classical = all(x in (0, 1) for x in xs)
            for F in fams:
                res = eval_graded(F, xs, p)
                df, bf = dia(res, p), box(res, p)
                U = eval_env(F, meas, True)
                L = eval_env(F, meas, False)
                if not (L <= bf <= df <= U):
                    return False, tested, (p, F, xs, L, bf, df, U)
                if classical and U != L:
                    return False, tested, ('gap', p, F, xs)
                tested += 1
    return True, tested, None

extra = [19, 23]
ok2, n2, w2 = sandwich_census(2, list(PRIMES) + extra, None)
check(ok2, f"2-leaf read-once, all p <= 23: sandwich + classical gap = 0 ({n2} checks)")
ok3, n3, w3 = sandwich_census(3, [p for p in PRIMES if p <= 13], None)
check(ok3, f"3-leaf read-once, p <= 13: sandwich + classical gap = 0 ({n3} checks)")
ok4, n4, w4 = sandwich_census(4, [p for p in PRIMES if p <= 7], None)
check(ok4, f"4-leaf read-once, p <= 7: sandwich + classical gap = 0 ({n4} checks)")
okr, nr, wr = sandwich_census(3, [p for p in PRIMES if p <= 13], (0, 1))
check(okr, f"3-leaf trees on TWO vars (repeated leaves), p <= 13 ({nr} checks)")

# Gap location (P2 general): uncertainty inside the union of the inputs'
# defect supports -- per channel: U AND NOT L = 1 implies SOME input
# non-classical. Already asserted above (the 'classical' branch); now the
# random census at larger p + deeper trees.
def random_formula(nvars, max_leaves):
    n = random.randint(1, max_leaves)
    tree = random.choice(gen_trees(n))
    vars_ = [random.randrange(nvars) for _ in range(n)]
    pols  = [random.randint(0, 1) for _ in range(n)]
    return instantiate(tree, vars_, pols)

viol = 0
tested = 0
for _ in range(40000):
    p = random.choice([3, 5, 7, 11, 13, 17, 19, 23])
    nv = random.randint(1, 4)
    F = random_formula(nv, 6)
    xs = [random.randrange(p) for _ in range(nv)]
    meas = [(dia(x, p), box(x, p)) for x in xs]
    res = eval_graded(F, xs, p)
    df, bf = dia(res, p), box(res, p)
    U, L = eval_env(F, meas, True), eval_env(F, meas, False)
    if not (L <= bf <= df <= U):
        viol += 1
    if U == 1 and L == 0 and all(x in (0, 1) for x in xs):
        viol += 1
    tested += 1
check(viol == 0, f"random census: {tested} formula-input pairs, sandwich + "
                 f"location (formulas to 6 leaves, p <= 23), 0 violations")

# Ring level through crt.py: random formulas on RAD integers, collapse by
# pow(., LAM, N), compare channel-wise after encode.
ok_ringlvl = True
for _ in range(2000):
    nv = random.randint(1, 4)
    F = random_formula(nv, 5)
    xs = [random.randrange(N) for _ in range(nv)]
    res = eval_graded(F, xs, N)
    dres = encode(pow(res, LAM, N), R)
    bres = encode((1 - pow((1 - res) % N, LAM, N)) % N, R)
    for i, p in enumerate(PRIMES):
        meas = [(dia(x % p, p), box(x % p, p)) for x in xs]
        U, L = eval_env(F, meas, True), eval_env(F, meas, False)
        if not (L <= bres[i] <= dres[i] <= U):
            ok_ringlvl = False
check(ok_ringlvl, "2000 RAD ring-level samples (pow collapses, channel-wise): sandwich holds")

# ───────────────────────────────────────────────────────────────────────
section("III. SLACK IS LOCATED AND COUNTED (P4): the p-2 law, envelope dress")
# ───────────────────────────────────────────────────────────────────────
# Single-node formulas. Roof slack on OR(a,b): U=1, DIA=0 -- exactly the
# true-true interference pairs (1-x)(1-y)=1: p-2 per channel. Floor slack
# on AND(a,b): BOX=1, L=0 with both inputs not fully true -- the inversion
# pairs xy=1, x!=1: p-2 per channel.

F_or  = ('or',  ('lit', 0, 1), ('lit', 1, 1))
F_and = ('and', ('lit', 0, 1), ('lit', 1, 1))
ok_or = ok_and = True
for p in ODD:
    n_or = n_and = 0
    for x in range(p):
        for y in range(p):
            meas = [(dia(x, p), box(x, p)), (dia(y, p), box(y, p))]
            if eval_env(F_or, meas, True) == 1 and dia(eval_graded(F_or, (x, y), p), p) == 0:
                n_or += 1
            if box(eval_graded(F_and, (x, y), p), p) == 1 and eval_env(F_and, meas, False) == 0:
                n_and += 1
    if n_or  != p - 2: ok_or  = False
    if n_and != p - 2: ok_and = False
check(ok_or,  "roof slack on OR = the p-2 interference pairs, every odd channel")
check(ok_and, "floor slack on AND = the p-2 inversion pairs, every odd channel")

# ───────────────────────────────────────────────────────────────────────
section("IV. SHARPNESS (P5): read-once achievability, the p = 3 rigidity")
# ───────────────────────────────────────────────────────────────────────
# Read-once => leaves independent => the achievable residue SET of every
# node composes exactly: S(node) = op(S1 x S2). Per class profile
# (0 -> {0}, 1 -> {1}, g -> F_p \ {0,1}), compare max achievable DIA F
# with U and min achievable BOX F with L.

def reach(F, sets, p):
    if F[0] == 'lit':
        S = sets[F[1]]
        return S if F[2] else {(1 - x) % p for x in S}
    A, B = reach(F[1], sets, p), reach(F[2], sets, p)
    if F[0] == 'and':
        return {a * b % p for a in A for b in B}
    return {(a + b - a * b) % p for a in A for b in B}

CLASS_SETS = lambda p: {'0': {0}, '1': {1}, 'g': set(range(2, p))}
CLASS_MEAS = {'0': (0, 0), '1': (1, 1), 'g': (1, 0)}

def achievability(ps, max_leaves):
    """Per p: (#profile-formula cells, roof violations, floor violations,
    one exhibit)."""
    out = {}
    for p in ps:
        cells = vroof = vfloor = 0
        exhibit = None
        for n in range(1, max_leaves + 1):
            for F in formulas(n):
                for prof in itertools.product('01g', repeat=n):
                    sets = [CLASS_SETS(p)[c] for c in prof]
                    meas = [CLASS_MEAS[c] for c in prof]
                    S = reach(F, sets, p)
                    U = eval_env(F, meas, True)
                    L = eval_env(F, meas, False)
                    maxd = max(dia(r, p) for r in S)
                    minb = min(box(r, p) for r in S)
                    cells += 1
                    if maxd != U:
                        vroof += 1
                        if exhibit is None: exhibit = ('roof', F, prof, U, maxd)
                    if minb != L:
                        vfloor += 1
                        if exhibit is None: exhibit = ('floor', F, prof, L, minb)
        out[p] = (cells, vroof, vfloor, exhibit)
    return out

ach = achievability([3, 5, 7, 11], 4)
for p in (5, 7, 11):
    c, vr, vf, _ = ach[p]
    check(vr == 0 and vf == 0,
          f"p = {p}: roof AND floor achieved on every read-once cell ({c} cells)")
c3, vr3, vf3, ex3 = ach[3]
check(vr3 > 0 and vf3 > 0,
      f"p = 3 rigidity: {vr3} roof + {vf3} floor unreachable cells of {c3} "
      f"(graded region = {{-1}}, self-inverse: interference and inversion FORCED)")
# the canonical exhibits, by hand:
check(eval_graded(F_or, (2, 2), 3) == 0,
      "exhibit: at p = 3, (-1) OR (-1) = 0 -- two any-degree leaves disjoin false")
check(eval_graded(F_and, (2, 2), 3) == 1,
      "exhibit: at p = 3, (-1) AND (-1) = 1 -- two not-fully-true leaves conjoin true")

# Repeated leaves: independence gone, set-composition invalid -- enumerate
# the joint fiber instead. Search trees on ONE variable (a vs NOT a), the
# minimal dependency stage.
def fiber_achievability(ps, max_leaves):
    out = {}
    for p in ps:
        cells = vroof = vfloor = 0
        exhibit = None
        for n in range(2, max_leaves + 1):
            for F in formulas(n, var_pool=(0,)):
                for c in '01g':
                    fiber = CLASS_SETS(p)[c]
                    meas = [CLASS_MEAS[c]]
                    U = eval_env(F, meas, True)
                    L = eval_env(F, meas, False)
                    res = [eval_graded(F, (x,), p) for x in fiber]
                    maxd = max(dia(r, p) for r in res)
                    minb = min(box(r, p) for r in res)
                    cells += 1
                    if maxd != U:
                        vroof += 1
                        if exhibit is None: exhibit = ('roof', F, c, U, maxd)
                    if minb != L:
                        vfloor += 1
                        if exhibit is None: exhibit = ('floor', F, c, L, minb)
        out[p] = (cells, vroof, vfloor, exhibit)
    return out

fib = fiber_achievability([3, 5, 7, 11, 13], 3)
print("  repeated-leaf (one variable, trees to 3 leaves) achievability:")
any_viol = False
for p, (c, vr, vf, ex) in sorted(fib.items()):
    print(f"    p = {p:2d}: {c} cells, roof unreachable {vr}, floor unreachable {vf}"
          + (f"   e.g. {ex[0]} cell {ex[1]} class '{ex[2]}'" if ex else ""))
    if vr or vf:
        any_viol = True
check(any_viol, "repeated-leaf achievability violations exist -- only at p = 3 "
                "(the rigidity in dependent dress; p >= 5 clean in this family)")
# the canonical dependent exhibit: a AND NOT a can be FULLY TRUE when
# delta(x) = -1 is solvable (x^2 - x + 1 = 0: p = 3 or p = 1 mod 3),
# while its floor is identically 0.
F_dep = ('and', ('lit', 0, 1), ('lit', 0, 0))
sol = {p: [x for x in range(p) if (x * x - x + 1) % p == 0] for p in [3, 7, 13]}
ok_dep = all(len(v) > 0 and
             all(box(eval_graded(F_dep, (x,), p), p) == 1 for x in v)
             for p, v in sol.items())
check(ok_dep, "a AND NOT a fully true at delta(x) = -1 (p = 3, 7, 13), floor 0: "
              "the dependency exhibit")

# ───────────────────────────────────────────────────────────────────────
section("V. THE BAR (P3): certified verdicts vs the measurement-as-mask")
# ───────────────────────────────────────────────────────────────────────
# Demo: F = (a AND b) OR (c AND d) -- retrieval fires if either evidence
# pair corroborates. Inputs per channel from the classical-leaning mixture
# (prob 1-gamma: residue uniform on {0,1}; prob gamma: uniform on F_p) --
# the masking regime: mostly Boolean gates, located graded exceptions.
# Exact per-channel rates by full weighted enumeration, then a 20,000-tuple
# RAD stream through the actual ring ops.

F_demo = ('or', ('and', ('lit', 0, 1), ('lit', 1, 1)),
                ('and', ('lit', 2, 1), ('lit', 3, 1)))
GAMMA = 0.1

def channel_rates(p, gamma):
    """Exact: (P[certified], P[roof-as-verdict wrong], P[certified & wrong])."""
    w = [gamma / p] * p
    w[0] += (1 - gamma) / 2
    w[1] += (1 - gamma) / 2
    P_cert = P_roof_err = P_cert_wrong = 0.0
    for xs in itertools.product(range(p), repeat=4):
        wt = w[xs[0]] * w[xs[1]] * w[xs[2]] * w[xs[3]]
        meas = [(dia(x, p), box(x, p)) for x in xs]
        res = eval_graded(F_demo, xs, p)
        df, bf = dia(res, p), box(res, p)
        U, L = eval_env(F_demo, meas, True), eval_env(F_demo, meas, False)
        if U == L:
            P_cert += wt
            if df != U or bf != L:
                P_cert_wrong += wt
        if U != df:
            P_roof_err += wt
    return P_cert, P_roof_err, P_cert_wrong

print(f"  exact rates, gamma = {GAMMA} (full weighted enumeration, p^4 tuples):")
print(f"    p   P[certified]   P[DIA-only errs]   P[certified & wrong]")
rates = {}
wrong_mass = 0.0
for p in PRIMES:
    pc, pe, pw = channel_rates(p, GAMMA)
    rates[p] = (pc, pe)
    wrong_mass += pw
    print(f"   {p:2d}   {pc:12.6f}   {pe:16.6f}   {pw:19.6f}")
check(wrong_mass == 0.0,
      "certified & wrong has probability 0 at every channel (enumerated exactly)")
check(rates[2][0] == 1.0 and rates[2][1] == 0.0,
      "channel 2 always certified, never errs (no graded region)")
check(all(rates[p][1] > 0 for p in ODD),
      "DIA-only roof-as-verdict error rate > 0 on every odd channel (the mask fails)")

# The ring-level stream.
NSAMP = 20000
cert_total = cert_wrong = roof_err = 0
per_ch_cert = [0] * R.k
all_cert = 0
for _ in range(NSAMP):
    leaves = []
    for _leaf in range(4):
        resid = []
        for p in PRIMES:
            if random.random() < GAMMA:
                resid.append(random.randrange(p))
            else:
                resid.append(random.randint(0, 1))
        leaves.append(decode(tuple(resid), R))
    res = eval_graded(F_demo, leaves, N)
    dres = encode(pow(res, LAM, N), R)
    bres = encode((1 - pow((1 - res) % N, LAM, N)) % N, R)
    tuple_cert = True
    for i, p in enumerate(PRIMES):
        meas = [(dia(x % p, p), box(x % p, p)) for x in leaves]
        U, L = eval_env(F_demo, meas, True), eval_env(F_demo, meas, False)
        if U == L:
            cert_total += 1
            per_ch_cert[i] += 1
            if dres[i] != U or bres[i] != L:
                cert_wrong += 1
        else:
            tuple_cert = False
        if U != dres[i]:
            roof_err += 1
    if tuple_cert:
        all_cert += 1

print(f"\n  RAD stream, {NSAMP} tuples through pow collapses:")
print(f"    certified channel-verdicts: {cert_total}, wrong: {cert_wrong}")
print(f"    DIA-only roof-as-verdict errors on the same stream: {roof_err}")
check(cert_wrong == 0, f"PAIR-certified verdicts: 0 errors in {cert_total}")
check(roof_err > 0, f"DIA-only verdicts: {roof_err} errors on the same stream "
                    f"-- the mask alone cannot decide")

ok_match = True
print(f"    per-channel certification, measured vs exact:")
for i, p in enumerate(PRIMES):
    meas_rate = per_ch_cert[i] / NSAMP
    exact = rates[p][0]
    sigma = (exact * (1 - exact) / NSAMP) ** 0.5
    flag = abs(meas_rate - exact) <= max(3 * sigma, 1e-9)
    print(f"      p = {p:2d}: {meas_rate:.4f} vs {exact:.4f}"
          f"   ({'within' if flag else 'OUTSIDE'} 3 sigma)")
    if not flag:
        ok_match = False
check(ok_match, "measured per-channel certification rates match enumeration (3 sigma)")

pred_all = 1.0
for p in PRIMES:
    pred_all *= rates[p][0]
sig = (pred_all * (1 - pred_all) / NSAMP) ** 0.5
check(abs(all_cert / NSAMP - pred_all) <= 3 * sig,
      f"all-7-channels certified: {all_cert/NSAMP:.4f} vs predicted "
      f"{pred_all:.4f} (channel independence by CRT)")

print()
print("=" * 72)
print(f"ALL CHECKS PASSED ({CHECKS})")
print("=" * 72)
