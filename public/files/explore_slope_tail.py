"""What the one-step covering hypothesis was standing in for: the
reachable tree, and the pre-period it leaves behind.

THE QUESTION. explore_slope_lattice.py replaced the length test by a
per-class SATURATION test: with L the state scale, phi = L w / z the
phase, N = L b^c the emission step, q = L u / v the injection step,
g = gcd(q, N) and n = N / g, a class t in Z/g is SATURATED when all n
of its residues mod N have a representative in the derived interval
I, and the game is feasible at lookahead c iff the forward orbit of
the start class under f(t) = b t + kappa, kappa = -(b-1) phi mod g,
stays saturated. That criterion is PROVED where one injection covers
the whole subgroup <q> -- n <= 2a + 1 -- and beyond it a RULE,
measured exact at 1833 cells. The rule is what this asks about. Its
own record names the suspicion: one step covers part of the subgroup,
several steps generate all of it. This turns that into a derivation
and measures exactly what the derivation does NOT reach.

THE DERIVATION, hand-attacked on paper before this engine existed.
Conventions re-derived from explore_slope_lattice.py's rgame rather
than from memory. Residues mod N throughout; the emission term is a
multiple of N, so the reader's play is invisible there and the
successor of a residue r under injection x is b r + q x - (b-1) phi.

(A) THE COMPLEMENT IS AN INTERVAL. Where the span test withholds the
span s of I is at most N, so reduction mod N is injective on I and
pi(I) is s consecutive residues: its complement B := Z/N \\ pi(I) is
therefore the N - s residues that follow them, an INTERVAL in Z/N.
A class mod g is saturated exactly when it misses B.
Two corollaries that cost nothing: where N - s < g the interval B
holds at most one residue of each class, and where N - s >= g it
holds one of every class, so no class is saturated at all.

(B) THE REACHABLE TREE HAS A CLOSED FORM. From r, the residues
reachable in j steps are

    T_j(r) = b^j r - (b-1) phi r_j + q S_j   (mod N),

r_j the j-digit repunit and S_j = { sum b^(j-i) x_i : x_i in D } the
j-fold digit sum set. Induction: T_1 is the successor set, and
T_(j+1) = b T_j - (b-1) phi + q D with b r_j + 1 = r_(j+1) and
b S_j + D = S_(j+1).

(C) REDUNDANCY MAKES S_j AN INTERVAL. S_1 = [-a, a]; if
S_j = [-a r_j, a r_j] as a set of consecutive INTEGERS then
S_(j+1) = union over k in S_j of [b k - a, b k + a], whose blocks
abut or overlap exactly when b <= 2a + 1 -- which is redundancy --
giving [-a r_(j+1), a r_(j+1)]. So the digit set's shape never enters
again after this step.

(D) THE DEPTH THE SUBGROUP IS COVERED AT. x |-> q x mod N carries
Z/n bijectively onto <q> = g Z/N, so q S_j covers <q> exactly when
2 a r_j + 1 >= n. Write J = min{ j >= 1 : 2 a r_j + 1 >= n }. The
coset hypothesis n <= 2a + 1 is J = 1, and nothing else.

(E) NECESSITY FROM DEPTH J ON, WITH NO HYPOTHESIS. If m is in the
winning set then T_j(m) sits inside pi(I) for every j. For j >= J
that tree is the FULL coset b^j m - (b-1) phi r_j + <q>, which is
exactly the class f^j(m mod g) mod g. So that class misses B: it is
saturated. Hence m in W implies f^j(m mod g) in A for all j >= J.

(F) SUFFICIENCY, ALSO WITH NO HYPOTHESIS. Let
W* = { m in I : f^j(m mod g) in A for all j >= 1 }. For m in W* and
any injection x, the successor residue has class f(m mod g), which is
in A and so misses B, so it has a representative m' in I; the
emission carrying the value to m' is in D by the endpoint bound
exactly as in the proved criterion; and m' is again in W* since its
orbit is m's shifted. So W* is a strategy set and W* is contained in
W.

(G) SO THE GAP IS NAMED. W* is contained in W is contained in
W^J := { m in I : f^j(m mod g) in A for all j >= J }, and the
criterion is exact at a cell exactly when W* = W^J there. They can
differ only if some orbit meets an unsaturated class at a level
1 <= j < J and none from J on.

(H) THE CYCLE COROLLARY, WHICH IS THE POINT. Z/g is finite and f is
affine, so every orbit is eventually periodic. A class ON the cycle
recurs at arbitrarily large j, so an unsaturated recurrent class is
already caught at some j >= J. The criterion is therefore PROVED at
every cell where each unsaturated class the orbit meets below J is
recurrent -- in particular at every cell with gcd(b, g) = 1, where f
is a bijection and every orbit is PURELY periodic with no pre-period
to hide in. What the one-step hypothesis was standing in for is a
pre-period, not a covering.

(I) WHAT IS LEFT. The residual is exactly: gcd(b, g) > 1 AND J >= 2
AND some orbit meeting an unsaturated class strictly inside its own
pre-period at a level below J. No orbit's pre-period is longer than
max over p dividing gcd(b, g) of ceil(v_p(g)/v_p(b)) -- the depth at
which b^j Z/g stops shrinking -- so the residual is a finite,
cheap-to-enumerate condition rather than a scope.

THE DESIGN, frozen before the engine.

P-A The controls come back through this code path: rgame verbatim
    from explore_slope_lattice.py, the four integer delays, and the
    three specimen sparse sets EXACTLY as sets.
P-B THE TREE LAW. On every cell of a small-N slice and at every
    j <= min(J, 4): the residues reachable from a state in j steps,
    computed by iterating the successor map, equal the closed form
    b^j r - (b-1) phi r_j + q [-a r_j, a r_j] mod N as a SET. This is
    (B), (C) and (D) at once, and everything below rests on it.
P-C NECESSITY FROM DEPTH. At every cell of the full scope: every m in
    the measured winning set has f^j(m mod g) in A for J <= j <= J+g.
    This is (E), and it is the half the coset hypothesis was carrying.
P-D SUFFICIENCY. At every cell: W* is contained in the measured
    winning set. This is (F).
P-E THE COVERAGE. Census over the cells with n > 2a + 1 -- the ones
    the old hypothesis excluded: how many are now PROVED by the cycle
    corollary (H), split by which clause grants (J = 1 cannot occur
    here, so: gcd(b, g) = 1, or a pre-period no unsaturated class sits
    below J in). This is the number that says how much of the rule
    the derivation retires.
P-F THE RESIDUAL. Enumerate the cells (I) leaves, and at each ask
    whether W* = W anyway. Empty residual and the criterion is proved
    entire in this scope; non-empty with W* = W and the rule survives
    on a named finite condition rather than on a cell count;
    non-empty with W* != W and the criterion is WRONG and the page
    shipped a rule that needs correcting.

KILLS, frozen as what this rig PRINTS.

K1 A control misses, or a specimen sparse set differs as a set ->
   the conventions were re-derived wrong and nothing below is read.
K2 A cell where the iterated reachable set differs from the closed
   form -> (B), (C) or (D) is wrong and the derivation has no base.
K3 A cell with m in W and f^j(m mod g) not in A for some
   J <= j <= J+g -> (E) is wrong; necessity does not come from depth
   and the coset hypothesis was carrying something real.
K4 A cell with m in W* but not in W -> (F) is wrong and sufficiency
   needed the hypothesis after all.
K5 A residual cell where W* != W -> the saturation criterion is not
   exact beyond the hypothesis, and the rule stated for it in
   explore_slope_lattice.py is false.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. The four integer delays reproduce through this
   code path and all three specimen sparse sets come back exactly as
   sets. K1 never fired.

F2 THE TREE LAW HOLDS. On the small-N slice, at every sampled state
   and every depth up to min(J, 4), the iterated reachable set equals
   the closed form: 13806/13806. So (B), (C) and (D) carry, and the
   digit set's shape leaves the argument at step (C) for good. K2
   never fired.

F3 THE SANDWICH IS TIGHT ON BOTH SIDES. W* is inside the measured
   winning set at 2903/2903 and the winning set is inside W^J at
   2903/2903. Both are proved with no hypothesis, so these are the
   CHECK on (E) and (F) rather than the evidence for them. K3 and K4
   never fired.

F4 THE COSET HYPOTHESIS RETIRES, AND IT WAS STANDING IN FOR A
   PRE-PERIOD. Of the 1833 cells beyond n <= 2a + 1, the cycle
   corollary proves the criterion at 1826: at 1341 because
   gcd(b, g) = 1 makes f a bijection on Z/g, so no orbit has a
   pre-period to hide an unsaturated class in, and at 485 more
   because the pre-period a cell does have carries no unsaturated
   class below J. What the hypothesis was carrying is not the digit
   set's reach at all -- going deeper is free in a safety game, since
   the winning set is closed forward -- but the one thing depth
   cannot reach: a class the orbit visits once and never again.

F5 THE RESIDUAL IS 7 CELLS, ALL AT J = 2, AND THE CRITERION IS
   EXACT AT ALL 7. K5 never fired. The agreement is not uniformly
   strong evidence and is not reported as if it were: 4 of the 7
   carry an EMPTY winning set, where criterion and game agree only in
   both saying infeasible. The three with a live winning set are the
   load-bearing ones -- (6,3) slope 8/1 at c = 2 (g = 4, n = 9,
   |W| = 17) and (10,6) slope 8/3 at c = 1 under phases 1/2 and 1/8
   (g = 4 and 16, n = 15, |W| = 29 each) -- and at each the
   criterion returns the winning set exactly. So the live evidence
   for the surviving rule is THREE cells, and that is the number to
   quote when asking whether it should still be called a rule.

F6 THE RESIDUAL IS ONE LEVEL DEEP IN THIS SCOPE. Every residual cell
   has J = 2: the first injection step falls short of the subgroup
   and the second covers it, so the whole gap sits at a single
   orbit position. Nothing here says J >= 3 residual cells cannot
   exist -- this scope caps c at 3 and slopes at 9/8 -- and a cell
   with a deep pre-period and a large n is where to look.

VERDICT, by piece, since they do not share a tier.
  - THE TREE LAW (B)-(D) is PROVED for every radix, every symmetric
    redundant digit set, every rational slope and every phase.
    Redundancy is its only hypothesis and it is used once, at (C), to
    make the j-fold digit sums an interval.
  - NECESSITY FROM DEPTH (E) and SUFFICIENCY (F) are PROVED at that
    same scope with NO hypothesis on the digit set. Together they
    sandwich the winning set between W* and W^J.
  - THE SATURATION CRITERION IS PROVED wherever every unsaturated
    class the orbit meets below J is recurrent -- in particular
    wherever gcd(b, g_c) = 1, where f is a bijection and every orbit
    is purely periodic. This retires the coset hypothesis as a
    condition on the law: n <= 2a + 1 is exactly J = 1 and nothing
    more.
  - BEYOND THAT the criterion stays a RULE, but now on a NAMED FINITE
    CONDITION -- gcd(b, g_c) > 1, J >= 2, and an unsaturated class
    strictly inside a pre-period below J -- rather than on a cell
    count. 7 such cells in this scope, exact at every one.

WHAT IT COST TO SEE. The hypothesis n <= 2a + 1 read as a statement
about the digit set's REACH, and a reach hypothesis has nowhere to go
but a bigger digit set. It is a statement about DEPTH, and depth is
free here: the reachable tree grows by a factor of b per step while
the subgroup does not grow at all, so the covering the hypothesis
demanded in one step arrives on its own in J. Once that is seen the
only obstruction left is structural rather than quantitative -- a
class visited once -- and it lives exactly where f fails to be
invertible. The rule shrank not by measuring more cells but by asking
what the hypothesis was FOR.

RUN RECORD: pure Python, integers only, standard library; 2903 cells
with the safety game replayed once per cell, plus 13806 tree checks
on the N <= 400 slice. 27.8s wall clock against a ~40s estimate, peak
working set 22.9 MB against the 512 MB analysis ceiling (memwatch.py).
Prints reproduced by:
python prime/code/explore_slope_tail.py
"""

import sys
from math import gcd

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def repunit(b, j):
    return sum(b ** i for i in range(j))


def digits(a):
    return list(range(-a, a + 1))


# --------------------------------------------------------------- game
# rgame and interval are VERBATIM explore_slope_lattice.py, which took
# them verbatim from explore_slope_proof.py. Copied rather than
# imported so this file is a standalone record; P-A checks the copy.

def rgame(b, a, c, u, v, w=0, z=1):
    """Greatest fixed point of the residual safety game, and whether
    the initial state is in it."""
    L = v * z // gcd(v, z)
    F = a * repunit(b, c)
    win = set(range(-F * L, (F + 1) * L))
    phc = (b - 1) * (L * w // z)
    inj = [L * u * x // v - phc for x in digits(a)]
    shift = L * b ** c
    changed = True
    while changed:
        changed = False
        for r in list(win):
            for s in inj:
                pre = b * r + s
                if not any(pre - e * shift in win for e in digits(a)):
                    win.discard(r)
                    changed = True
                    break
    return (L * w // z) in win, win


def interval(b, a, c, u, v, w=0, z=1):
    """The derived winning interval [Lbot + phi, Htop + phi] and the
    span the proved criterion tests against L b^c."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    E = (a * L * (v * b ** c - u)) // (v * (b - 1))
    if v * b ** c < u:
        E = -1
    wtop = (a * repunit(b, c) + 1) * L - 1
    wbot = -a * repunit(b, c) * L
    htop = min(E, wtop - phi)
    lbot = max(-E, wbot - phi)
    return lbot + phi, htop + phi, htop - lbot + 1, L * b ** c


def cmin_measured(b, a, u, v, w=0, z=1, cap=4):
    for c in range(cap + 1):
        if rgame(b, a, c, u, v, w, z)[0]:
            return c
    return None


def params(b, a, c, u, v, w=0, z=1):
    """The five numbers the derivation runs on."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    N = L * b ** c
    q = L * u // v
    return L, phi, N, q, gcd(q, N)


# ------------------------------------------------- the derivation (D)

def depth_J(b, a, n):
    """(D): the least j whose digit sums cover the whole subgroup."""
    j = 1
    while 2 * a * repunit(b, j) + 1 < n:
        j += 1
    return j


def saturated_classes(b, a, c, u, v, w=0, z=1):
    """(A): the classes mod g whose n residues all have a
    representative in I."""
    _, _, N, _, g = params(b, a, c, u, v, w, z)
    n = N // g
    lo, hi, _, _ = interval(b, a, c, u, v, w, z)
    if lo > hi:
        return set(), g, n, lo, hi
    counts = [0] * g
    for m in range(lo, hi + 1):
        counts[m % g] += 1
    return ({t for t in range(g) if counts[t] >= n}, g, n, lo, hi)


def class_map(b, phi, g):
    """f(t) = b t + kappa on Z/g."""
    kappa = (-(b - 1) * phi) % g
    return lambda t: (b * t + kappa) % g


def orbit(f, t, steps):
    """t_1 .. t_steps, the forward orbit not including t itself."""
    out = []
    cur = t
    for _ in range(steps):
        cur = f(cur)
        out.append(cur)
    return out


def preperiod(f, t, g):
    """Index at which t's forward orbit enters its cycle: t_j is
    recurrent for j >= this and never recurs for j below it."""
    seen = {}
    cur, j = t, 0
    while cur not in seen:
        seen[cur] = j
        cur = f(cur)
        j += 1
    return seen[cur]


def criterion_sets(b, a, c, u, v, w=0, z=1):
    """W* (all j >= 1 saturated) and W^J (all j >= J saturated), as
    subsets of I -- the two ends of the gap (G)."""
    _, phi, N, _, g = params(b, a, c, u, v, w, z)
    A, g, n, lo, hi = saturated_classes(b, a, c, u, v, w, z)
    if lo > hi:
        return set(), set(), A, g, n, 1
    f = class_map(b, phi, g)
    J = depth_J(b, a, n)
    star, deep = set(), set()
    okstar, okdeep = {}, {}
    for t in range(g):
        orb = orbit(f, t, J + g)
        okstar[t] = all(x in A for x in orb)
        okdeep[t] = all(x in A for x in orb[J - 1:])
    for m in range(lo, hi + 1):
        if okstar[m % g]:
            star.add(m)
        if okdeep[m % g]:
            deep.add(m)
    return star, deep, A, g, n, J


def residual_cell(b, a, c, u, v, w=0, z=1):
    """(I): does this cell escape the cycle corollary (H)? True when
    some class meets an unsaturated class strictly inside its own
    pre-period at a level below J."""
    _, phi, N, _, g = params(b, a, c, u, v, w, z)
    A, g, n, lo, hi = saturated_classes(b, a, c, u, v, w, z)
    if lo > hi or gcd(b, g) == 1:
        return False
    f = class_map(b, phi, g)
    J = depth_J(b, a, n)
    if J == 1:
        return False
    for t in {m % g for m in range(lo, hi + 1)}:
        tau = preperiod(f, t, g)
        orb = orbit(f, t, J - 1)
        for j, x in enumerate(orb, start=1):
            if j < tau and x not in A:
                return True
    return False


def reachable_iterated(b, a, c, u, v, r, j, w=0, z=1):
    """The residues reachable from r in j steps, by iterating."""
    _, phi, N, q, _ = params(b, a, c, u, v, w, z)
    offs = [(q * x - (b - 1) * phi) % N for x in digits(a)]
    cur = {r % N}
    for _ in range(j):
        cur = {(b * s + o) % N for s in cur for o in offs}
    return cur


def reachable_closed(b, a, c, u, v, r, j, w=0, z=1):
    """(B) + (C): the same set as a closed form."""
    _, phi, N, q, _ = params(b, a, c, u, v, w, z)
    rj = repunit(b, j)
    base = (b ** j * r - (b - 1) * phi * rj) % N
    return {(base + q * y) % N for y in range(-a * rj, a * rj + 1)}


# ---------------------------------------------------------- the grids
# The scope is explore_slope_lattice.py's, verbatim, so the census
# below is comparable to the 1833 cells this asks about.

WINDOWS = [(2, 1), (3, 2), (4, 2), (10, 6)]

SLOPES = [(u, v) for u in range(1, 9) for v in range(1, 9)
          if gcd(u, v) == 1]

DISJOINT = [(5, 3), (5, 4), (6, 3), (6, 5), (7, 4), (8, 5), (9, 5),
            (9, 8), (7, 6), (3, 3), (2, 2)]

PHASE_SLOPES = [(1, 3), (3, 5), (5, 3), (2, 5), (8, 3)]
PHASES = [(1, 2), (2, 3), (3, 5), (1, 7), (1, 8)]

SPECIMENS = [(2, 1, 1, 3, 1, 7, 0, {3, 10, 17}),
             (2, 1, 8, 3, 0, 1, 2, {-4, -2, 0, 2, 4}),
             (2, 1, 2, 1, 0, 1, 1, {0})]


def scope(cap_c=3):
    """Every cell this rig reads, once: both grids plus the phased
    slice. Yields (b, a, u, v, w, z, c)."""
    for (b, a) in WINDOWS:
        for (u, v) in SLOPES:
            for c in range(cap_c + 1):
                yield (b, a, u, v, 0, 1, c)
    for (b, a) in DISJOINT:
        if 2 * a + 1 <= b:
            continue
        for u in range(1, 10):
            for v in range(1, 10):
                if gcd(u, v) != 1:
                    continue
                for c in range(3):
                    yield (b, a, u, v, 0, 1, c)
    for (b, a) in WINDOWS:
        for (u, v) in PHASE_SLOPES:
            for (w, z) in PHASES:
                for c in range(cap_c + 1):
                    yield (b, a, u, v, w, z, c)


# ----------------------------------------------------------- the runs

def s0_control():
    print("== POSITIVE CONTROL (P-A) ==")
    for (b, a, m, want) in [(2, 1, 3, 3), (2, 1, 4, 2),
                            (10, 6, 2, 1), (10, 6, 10, 1)]:
        got = cmin_measured(b, a, m, 1)
        ok(got == want, f"K1: integer x{m} at ({b},{a}) = {got} != {want}")
    print("  integer delays reproduce: (2,1) x3=3 x4=2; (10,6) x2=1 x10=1")
    bad = []
    for (b, a, u, v, w, z, c, want) in SPECIMENS:
        feas, win = rgame(b, a, c, u, v, w, z)
        if not feas or win != want:
            bad.append((b, a, u, v, w, z, c, sorted(win)))
    print(f"  the three specimen sparse sets reproduce as SETS: "
          f"{len(SPECIMENS) - len(bad)}/{len(SPECIMENS)}")
    ok(not bad, f"K1: specimen set differs at {bad[:3]}")


def s1_tree_law():
    """P-B: the closed form of the reachable tree."""
    print("\n== P-B THE TREE LAW ==")
    checked, bad = 0, []
    for (b, a, u, v, w, z, c) in scope():
        _, _, N, _, g = params(b, a, c, u, v, w, z)
        if N > 400:
            continue
        n = N // g
        J = depth_J(b, a, n)
        lo, hi, _, _ = interval(b, a, c, u, v, w, z)
        if lo > hi:
            continue
        for r in (lo, (lo + hi) // 2, hi):
            for j in range(1, min(J, 4) + 1):
                it = reachable_iterated(b, a, c, u, v, r, j, w, z)
                cf = reachable_closed(b, a, c, u, v, r, j, w, z)
                checked += 1
                if it != cf:
                    bad.append((b, a, u, v, w, z, c, r, j))
    print(f"  iterated tree == closed form: {checked - len(bad)}/{checked}")
    ok(not bad, f"K2: tree law fails at {bad[:3]}")


def s2_sandwich():
    """P-C, P-D, P-E, P-F in one sweep -- the game is replayed once
    per cell, which is what a single sweep buys."""
    print("\n== P-C/P-D THE SANDWICH, P-E THE COVERAGE, P-F THE RESIDUAL ==")
    cells = beyond = proved_bij = proved_orbit = residual = 0
    bad_nec, bad_suf, bad_res, exact_res = [], [], [], 0
    res_cells = []
    for (b, a, u, v, w, z, c) in scope():
        _, phi, N, _, g = params(b, a, c, u, v, w, z)
        n = N // g
        _, win = rgame(b, a, c, u, v, w, z)
        star, deep, A, g, n, J = criterion_sets(b, a, c, u, v, w, z)
        cells += 1
        if not (star <= win):
            bad_suf.append((b, a, u, v, w, z, c))
        if not (win <= deep):
            bad_nec.append((b, a, u, v, w, z, c))
        if n <= 2 * a + 1:
            continue
        beyond += 1
        res = residual_cell(b, a, c, u, v, w, z)
        if res:
            residual += 1
            res_cells.append((b, a, u, v, w, z, c, g, n, J,
                              len(win), star == win))
            if star == win:
                exact_res += 1
            else:
                bad_res.append((b, a, u, v, w, z, c))
        elif gcd(b, g) == 1:
            proved_bij += 1
        else:
            proved_orbit += 1
    print(f"  cells swept: {cells}; beyond the coset hypothesis: {beyond}")
    print(f"  P-D sufficiency  W* subset of W: "
          f"{cells - len(bad_suf)}/{cells}")
    print(f"  P-C necessity    W subset of W^J: "
          f"{cells - len(bad_nec)}/{cells}")
    print(f"  P-E of the {beyond} beyond: proved by f bijective "
          f"(gcd(b,g)=1): {proved_bij}; proved by orbit shape: "
          f"{proved_orbit}")
    print(f"  P-F residual cells: {residual}"
          + (f"; W* == W at {exact_res}/{residual}" if residual else ""))
    for (b, a, u, v, w, z, c, g, n, J, sz, agree) in res_cells:
        print(f"    (b={b},a={a}) slope {u}/{v} phase {w}/{z} c={c}: "
              f"g={g} n={n} J={J} |W|={sz} "
              f"{'exact' if agree else 'MISMATCH'}")
    ok(not bad_suf, f"K4: sufficiency fails at {bad_suf[:3]}")
    ok(not bad_nec, f"K3: necessity from depth fails at {bad_nec[:3]}")
    ok(not bad_res, f"K5: residual cell with W* != W at {bad_res[:3]}")


def main():
    s0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- nothing below is read.")
        return 1
    s1_tree_law()
    s2_sandwich()
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  {f}")
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
