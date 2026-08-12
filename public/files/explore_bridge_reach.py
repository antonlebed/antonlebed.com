"""THE BRIDGE'S REACH — surjectivity of the
fate -> object map + the cascade boundary's two directions.

THE QUESTION. The ladder of growth-fate <-> classical-conjecture bridges
(Sigma_1 < Sigma_1/Pi_1 < Pi_2, explore_conjecture_bridge.py) gained a
DENSITY-kind entry (explore_transparency_bridge.py)
and a Pi_2 endpoint certificate that is sufficient-not-equivalent
(explore_abscissa_reserve.py, Pierpont => sigma_c = +inf) — the fate -> object map onto
Pi_2 is many-to-one. Two parts:
  (a) is the map SURJECTIVE onto each level/kind — and can Pi_2 be
      hit by EQUIVALENCES rather than one-directional certificates?
  (b) does the Pi_2 cascade boundary itself resolve (every char-0
      trajectory locks <=> no infinite Proth carrier ladder,
      explore_module_law.py C)?

THE DESIGN OBJECT. The BOUNDED-ALPHABET mover over Z (the species
explore_function_field_melt.py charted for depth/mortality; Z's pure
2-column is its immortal witness): moves restricted to deepening columns in a
fixed finite prime set S (push q^(t+1), q in S). The world's
accumulator is lambda(state); a window p opens iff (p-1) | the
accumulator (the growth window-opening rule, explore_conjecture_bridge.py /
explore_transparency_bridge.py). The
world's BREADTH capability — which windows are EVER reachable — is
then a derived set, and its unboundedness is a designed Pi_2 fate.

PREDICTIONS R1-R4 (fixed before the run, hand-derived in advance
— an early pass caught a prediction error before any code was run: the dowry.
Findings enter by a SEPARATE post-run edit copying printed output):
  R1 (the alphabet law): lambda(q^T) = q^(T-1)(q-1) drags supp(q-1)
    in at FIXED exponent, so with A_inf = prod_{q in S} q^inf * F,
    F = the outside-S part of lcm{q-1 : q in S}:
      reachable windows = {p : outside-S part of (p-1) divides F}.
    - S SHIFT-CLOSED (supp(q-1) subset S for all q in S; forces
      2 in S): F = 1, windows = the S-smooth shifted primes EXACTLY.
      {2},{2,3},{2,5},{2,3,5},{2,3,5,7} all closed.
    - S = {2}: windows = {2,3,5,17,257,65537} below 1e6 (must
      reproduce spectrum(1), explore_conjecture_bridge.py).
    - 2-FREE alphabets are NOT sterile (a later correction): S = {3}
      has F = 2, windows = {2,3} + {primes 2*3^b+1} = 7, 19, 163,
      487, 1459 (hand: 1459 prime) — v_2 PINNED at 1; the alphabet
      designs both the support and the exponent pins.
    - Non-closed with 2: S = {2,11} has F = 5 — 41 (40 = 2^3*5)
      OPENS, 101 (100 = 2^2*5^2) stays SHUT.
    - Hand row: 7-1 = 6 in {2,3} not {2,5}; 11-1 = 10 in {2,5} not
      {2,3}; 31-1 = 30 needs {2,3,5}.
  R2 (the equivalence family): for shift-closed S, window-count
    unbounded <=> #{p : p-1 S-smooth} = inf — an EQUIVALENT Pi_2
    bridge PER ALPHABET (vs explore_abscissa_reserve.py's sufficiency
    certificate), Fermat at S = {2},
    the {2,3} family at Pierpont's, one open conjecture per S; the
    complement (window stall <=> finiteness) is its Sigma_2 face.
    Counts below 1e6 monotone in S; S = {2} STALLS at 6 (no window
    between 65537 and 1e6); {2,3}, {2,3,5}, {2,3,5,7} gain in every
    decade 1e1..1e6.
  R3 (the reach chart): levels Sigma_1 / Pi_1 / Sigma_2 / Pi_2 are
    ALL hit by equivalences (B1 proved, 78557 proved, R2 open both
    faces); Pi_2 is many-to-one WITH equivalences (R2 family + the
    cascade reduction) alongside the sufficient-only
    explore_abscissa_reserve.py
    certificate; single-world fates top out at Pi_2-surface — the
    corpus's two ways past Pi_2 (density: explore_transparency_bridge.py,
    abscissa: explore_abscissa_reserve.py) are
    KIND changes, not level climbs.
  R4 (the cascade census): carrier q_R = m*p^(v+1)+1 (module law C;
    canonical m: odd for p = 2, even and p-coprime for odd p — parity
    forces it). PREDICTED HAND VALUES: at p = 2, cap M = 8 (m in
    {1,3,5,7}), the first ALL-MISS depth is v = 9 (513 = 27*19,
    1537 = 29*53, 2561 = 13*197, 3585 = 5*717), with hits at
    v = 1..8: least prime per depth 3, 5, 41, 17, 97, 193, 641, 257.
    All-miss depths exist for every cap tried and dominate as v
    grows (heuristic P(hit) ~ c*M/(v ln p) -> 0; chained survival
    prod ~ c^V/V! superexponentially dead). The hardness pin
    (argument): per-stage existence needs a prime == 1 mod p^(v+1)
    inside a window LINEAR in the modulus (width M*q at q =
    p^(v+1)) — the GRH worst-case least-prime bound ~ (phi(q) log
    q)^2 ~ q^2 exceeds it for all large v, Linnik-type q^L more so
    — so even GRH cannot run the ladder; ruling it out needs
    all-miss uniformity over reachable configurations — true in
    every Cramer-type model, owned by no technique (covering
    congruences kill ONE multiplier for ALL depths, the ladder
    dodges by varying m; the wander/dowry can grow the cap —
    unbounded wander OPEN, explore_lock_prime.py). The boundary does
    not RESOLVE;
    it SHARPENS: bounded-cap ladders die at a computable, certified
    all-miss depth (modulo the explore_module_law.py reduction), and
    the open
    content is exactly wander unboundedness.

DESIGN. Primitives mirror explore_conjecture_bridge.py (is_primeZ:
deterministic MR below 3.317e24, strong PRP above — PRP affects HIT
claims only; an MR composite verdict is a PROOF, so all-miss
certificates are unconditional). Alphabet accumulator computed
directly (lcm of lam(q^T), no big factorint); window tests are
(p-1) | acc over an SPF sieve to 1e6. R4 composites certified by a
small factor where one exists (trial division), else by MR witness.
All sections assert; est. ~2-4 min total, << 512 MB, no numpy.

FINDINGS (run record at bottom; all sections
assert; copied from run output only).

1. THE ALPHABET LAW (rule, proved; verified at 9 alphabets to 1e6).
   The bounded-alphabet mover's reachable window set is
     {p prime : the outside-S part of (p-1) divides F},
   F = the outside-S part of lcm{q-1 : q in S} — proof: the
   accumulator lambda(prod q^T) = lcm(q^(T-1)(q-1)) has diverging
   S-exponents and outside-S part stabilized at F; the set is
   schedule-free (any schedule pushing every q in S unboundedly).
   sim == law at all 9 alphabets. Consequences, all asserted:
   - S SHIFT-CLOSED (supp(q-1) subset S for every q in S) <=> F = 1
     <=> windows = the S-smooth shifted primes EXACTLY. S = {2}
     reproduces spectrum(1) = {2, 3, 5, 17, 257, 65537}
     (explore_conjecture_bridge.py).
   - 2-FREE alphabets are NOT sterile — they are DOWRY-PINNED thin
     families: S = {3} has F = 2, windows = {2, 3} + primes 2*3^b+1
     = 7, 19, 163, 487, 1459, 39367 (v_2 pinned at 1); S = {5} has
     F = 4 (v_2 pinned at 2): 2, 3, 5, 11, 101, 251, 62501. The
     alphabet designs BOTH the support and the exponent pins.
   - Non-closed with 2: S = {2,11} has F = 5 — 41 (40 = 2^3*5)
     OPENS while 101 (100 = 2^2*5^2) stays SHUT.

2. THE EQUIVALENCE FAMILY (property — the set identity; counts
   observation). For every shift-closed alphabet the window set IS
   the conjecture's set, so window-count unbounded <=> S-smooth
   shifted primes infinite: an EQUIVALENT Pi_2 bridge PER ALPHABET
   (vs explore_abscissa_reserve.py's sufficient-only Pierpont
   certificate), its
   stall face <=> finiteness (Sigma_2). One open conjecture per
   alphabet, Fermat at the bottom. Counts below 10^j (j = 1..6):
     S={2}        3   4   5   5   6   6   (STALLS at 6 past 65537)
     S={2,3}      4  10  18  25  32  42   (gains every decade)
     S={2,3,5}    4  14  34  59  95 141
     S={2,3,5,7}  4  17  52 101 194 324
     S={2,5}      3   6  11  13  18  20
   Monotone in S along the chain; the S = {2} stall is the Fermat
   face; the {2,3} family is Pierpont's (plus the b = 0 Fermat
   members — the union, one statement per alphabet).

3. THE REACH CHART (chart, observation; asserted on the encoded
   rows). The fate -> object map hits EVERY arithmetic level with
   EQUIVALENCES: Sigma_1 (B1 Dirichlet PROVED; B3 edits
   instance-open), Pi_1 (Sierpinski, PROVED at 78557), Pi_2 (the R2
   family, every S open; + the cascade reduction), Sigma_2 (the R2
   complements) — surjectivity-with-equivalences onto the levels,
   answering part (a); Pi_2 is many-to-one WITH equivalences
   alongside explore_abscissa_reserve.py's sufficient-only certificate.
   Everything past
   Pi_2 in the corpus is a KIND change (density: explore_transparency_bridge.py,
   average: explore_ledger_threshold.py / explore_reserve_zoo.py,
   abscissa: explore_abscissa_reserve.py — the settled row), not a level climb:
   single-world fates top out at Pi_2-surface.

4. THE CASCADE CENSUS (observation + argument; certificates
   unconditional). Carrier m*p^(v+1)+1 = m*p^e+1 (e = v+1 >= 2),
   canonical m (odd at p = 2; even, p-coprime at odd p — parity
   forces it). First all-miss exponents A(p, M) — each a CERTIFIED
   kill of every cap-M single-char ladder passing that depth
   (modulo the explore_module_law.py reduction):
     p=2: A(2,8)=9  A(2,16)=22  A(2,32)=23  A(2,64)=34
          A(2,128)=79  A(2,256)=109
     p=3: A(3,9)=11  A(3,27)=11  A(3,81)=23
     p=5: A(5,25)=9  A(5,125)=29
   The e = 9 certificate: 513 = 3*171, 1537 = 29*53, 2561 = 13*197,
   3585 = 3*1195 (predicted hand values, factor splits differ). Least
   prime per exponent e = 2..8: 5, 41, 17, 97, 193, 641, 257
   (predicted in advance). Hit density decays as the c/e heuristic: hits per
   century e = 2..1001 at M = 8: 27, 7, 3, 3, 3, 1, 1, 0, 1, 0;
   E[hits e=502..1001] ~ sum 4/(e ln 2) = 4.0 vs observed 3.
   THE PIN (argument): per-stage existence needs a prime == 1 mod
   p^(v+1) inside a window LINEAR in the modulus — beyond the GRH
   worst-case ~q^2 at every large v (the bound cannot certify even
   ONE large stage, let alone all — insufficiency, not a death
   proof); ruling it out is owned by no technique (a covering
   congruence kills ONE multiplier at ALL depths; the ladder dodges
   by varying m; the wander/dowry can grow the cap). THE MODEL
   THRESHOLD (argument): in a Cramer-type model P(miss at depth v)
   ~ exp(-c*M_v/(v ln p)), so a ladder survives with positive
   probability iff sum P(miss) < inf iff its cap grows M_v >~
   c'*v*ln v — wander at least LOGARITHMIC in depth; every
   bounded-or-slower wander schedule dies a.s., and the model does
   NOT kill log-wander ladders. PART (b) ANSWER: the boundary does
   NOT resolve; it SHARPENS — every CENSUSED cap dies at a
   certified exponent (each further cap is its own finite,
   semi-decidable computation), so modulo per-cap all-miss
   existence the open content is WANDER GROWTH, now PRICED: can the
   dynamics pay log-depth wander along a trajectory? — the same
   mechanism explore_lock_prime.py's wander census probes over seeds
   (kin, not identical: one is sup over seeds, the other growth
   along one trajectory).
   [SETTLED IN PART, explore_ghost_wander.py: the cap is read off the
   state, and the budget inequality pins its excess at zero for odd p
   and at one unit for p = 2, so the answer here is NO and the walk
   dies unconditionally at p = 2, 3, 5. What survives of this finding
   is the census itself and the per-cap all-miss values; what is
   superseded is "the open content is wander growth" — the open
   content is now the rings whose rank-1 chars avoid 2, 3 and 5.]

HONEST SCOPE. The Pi_2 equivalences are set identities of designed
worlds — the content is the design + the alphabet law, not new
analytic number theory; every S-conjecture stays open. Chart levels
are surface-quantifier classifications of the natural formulations.
The R4 kill claims are per-char, bounded-cap, modulo the module-law
reduction (explore_module_law.py C — cited, not re-derived here).
That reduction has since been PROVED in that section, for the ideal
world; so what stood as a modulo is now a scope, and these claims
read over ideal dynamics. The full ALL-trajectory boundary stays
open. Primality is deterministic
below 3.317e24 and strong-PRP above (hit claims only; all-miss
certificates carry printed factors or MR-composite proofs).

RUN RECORD (this file, ~0.7 s, 53 checks, well under 512 MB, no
numpy; all sections assert). Predictions R1-R4 were fixed in advance
of the run (hand-derived pre-engine). An early check caught a
prediction error before any code was run: the sterility lemma was derived on the
raw accumulator, but the window rule reads lambda(state), whose
dowry (q-1) un-sterilizes 2-free alphabets — the corrected law is
finding 1. PRE-GREEN (one construction bug, no world-miss): R1-R3
green on the first run; R4 crashed pre-assert on a depth/exponent
indexing conflation (the predicted hand values sit at carrier
EXPONENT e = v+1; labels re-indexed, every predicted value unchanged —
caught in a later pass). Every WORLD-prediction held: spectrum(1),
the F values, the 41/101 split, the stall at 6, the decade gains,
the e = 2..8 hit list, A(2,8) = 9, the density decay. The
R4 ARGUMENT layer was corrected post-run (a later review: scope
of the certified kills; the model threshold — a blanket
"model-dead" was false); FINDING 4 is the current statement, the
prediction above stays verbatim as the original record.

Related scripts: explore_conjecture_bridge.py (the ladder,
the spectrum functor), explore_transparency_bridge.py
(the density kind), explore_abscissa_reserve.py (the
sufficient-only Pi_2 certificate),
explore_module_law.py / explore_function_field_melt.py (the cascade
reduction; the bounded-alphabet species),
explore_lock_prime.py (the wander census, max 3, unboundedness
open).
"""

import sys
from array import array
from math import lcm, log

# ── number-theory primitives (thin re-decl; mirror explore_conjecture_bridge) ──

MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)  # deterministic < 3.317e24


def is_primeZ(n):
    if n < 2:
        return False
    for p in MR_BASES:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in MR_BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def lam_pp(q, a):
    if q == 2:
        return 1 if a == 1 else (2 if a == 2 else 1 << (a - 2))
    return q ** (a - 1) * (q - 1)


X = 10 ** 6          # window census bound
T = 25               # alphabet push depth (2^(T-2) > X: exponent caps don't bind)

# SPF sieve to X (array('i'): ~4 MB)
_spf = array('i', [0]) * 0


def build_spf(x):
    global _spf
    _spf = array('i', [0]) * 0
    _spf = array('i', range(x + 1))
    i = 2
    while i * i <= x:
        if _spf[i] == i:
            for j in range(i * i, x + 1, i):
                if _spf[j] == j:
                    _spf[j] = i
        i += 1


def spf_factor(n):
    f = {}
    while n > 1:
        p = _spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("  ** FAIL:", msg)


# ── the alphabet machinery ──

def accumulator(S, t=T):
    """lambda of the state prod_{q in S} q^t, computed directly."""
    A = 1
    for q in S:
        A = lcm(A, lam_pp(q, t))
    return A


def dowry_F(S):
    """Outside-S part of lcm{q-1 : q in S}."""
    L = 1
    for q in S:
        L = lcm(L, q - 1)
    for q in S:
        while L % q == 0:
            L //= q
    return L


def shift_closed(S):
    return all(set(factorint(q - 1)) <= set(S) for q in S if q > 2)


def windows_sim(S, primes):
    """Windows opened by the alphabet-S mover: (p-1) | lambda(state)."""
    A = accumulator(S)
    return [p for p in primes if A % (p - 1) == 0]


def windows_law(S, primes):
    """The alphabet law: outside-S part of (p-1) divides F."""
    F = dowry_F(S)
    out = []
    Sset = set(S)
    for p in primes:
        r = p - 1
        for q in Sset:
            while r % q == 0:
                r //= q
        if F % r == 0:
            out.append(p)
    return out


# ═══════════════════════════════════════════════════════════════════════
# R1 — THE ALPHABET LAW: reachable windows = S-part free, dowry-pinned rest
# ═══════════════════════════════════════════════════════════════════════

def section_R1(primes):
    print("R1  THE ALPHABET LAW (bounded-alphabet mover: derived window set)")
    print(f"    census bound X = {X:,}, push depth T = {T}")
    alphabets = [(2,), (2, 3), (2, 5), (2, 3, 5), (2, 3, 5, 7),
                 (3,), (5,), (3, 5), (2, 11)]
    win = {}
    for S in alphabets:
        ws = windows_sim(S, primes)
        wl = windows_law(S, primes)
        win[S] = ws
        ok(ws == wl, f"R1: sim == law for S={S}")
        tag = "closed" if shift_closed(S) else f"F={dowry_F(S)}"
        head = ", ".join(map(str, ws[:8])) + (", ..." if len(ws) > 8 else "")
        print(f"    S={str(S):16s} {tag:8s} |windows| = {len(ws):5d}   {head}")
    # shift-closure <=> F = 1
    for S in alphabets:
        ok(shift_closed(S) == (dowry_F(S) == 1),
           f"R1: shift-closed(S) <=> F(S)=1 at S={S}")
    # closed alphabets: windows == the S-smooth shifted primes exactly
    for S in [(2,), (2, 3), (2, 5), (2, 3, 5), (2, 3, 5, 7)]:
        census = [p for p in primes if set(spf_factor(p - 1)) <= set(S)]
        ok(win[S] == census, f"R1: closed S={S}: windows == S-smooth census")
    # predicted: S={2} reproduces spectrum(1) (explore_conjecture_bridge.py)
    ok(win[(2,)] == [2, 3, 5, 17, 257, 65537],
       "R1: S={2} windows = {2,3,5,17,257,65537} = spectrum(1)")
    # predicted: 2-free alphabets are dowry-pinned, not sterile
    ok(dowry_F((3,)) == 2 and win[(3,)][:7] == [2, 3, 7, 19, 163, 487, 1459],
       "R1: S={3}: F=2, windows start 2,3,7,19,163,487,1459 (v_2 pinned at 1)")
    ok(dowry_F((5,)) == 4, "R1: S={5}: F=4 (v_2 pinned at 2)")
    # predicted: non-closed with 2 — the {2,11} dowry
    ok(dowry_F((2, 11)) == 5, "R1: S={2,11}: F=5")
    ok(41 in win[(2, 11)] and 101 not in win[(2, 11)],
       "R1: S={2,11}: 41 (2^3*5) opens, 101 (2^2*5^2) stays shut")
    # hand row
    ok(7 in win[(2, 3)] and 7 not in win[(2, 5)], "R1: 7 in {2,3} not {2,5}")
    ok(11 in win[(2, 5)] and 11 not in win[(2, 3)], "R1: 11 in {2,5} not {2,3}")
    ok(31 not in win[(2, 3)] and 31 not in win[(2, 5)] and 31 in win[(2, 3, 5)],
       "R1: 31 needs {2,3,5}")
    print()
    return win


# ═══════════════════════════════════════════════════════════════════════
# R2 — THE EQUIVALENCE FAMILY: one open Pi_2 conjecture per alphabet
# ═══════════════════════════════════════════════════════════════════════

def section_R2(primes, win):
    print("R2  THE EQUIVALENCE FAMILY (window-unbounded <=> S-smooth shifted")
    print("    primes infinite -- per alphabet; counts below decades)")
    chain = [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7)]
    decades = [10 ** j for j in range(1, 7)]
    print("    S \\ X            " + "".join(f"{d:>10,}" for d in decades))
    counts = {}
    for S in chain + [(2, 5)]:
        row = [sum(1 for p in win[S] if p <= d) for d in decades]
        counts[S] = row
        print(f"    {str(S):16s} " + "".join(f"{c:10d}" for c in row))
    # monotone in S along the chain (S subset S' => counts <=)
    for a, b in zip(chain, chain[1:]):
        ok(all(x <= y for x, y in zip(counts[a], counts[b])),
           f"R2: counts monotone {a} subset {b}")
    # predicted: S={2} stalls at 6 from 1e5 on (Fermat face)
    ok(counts[(2,)][-2] == 6 and counts[(2,)][-1] == 6,
       "R2: S={2} stalls at 6 (no new window 65537..1e6)")
    # predicted: the closed alphabets past {2} gain in every decade
    for S in chain[1:]:
        gains = [counts[S][j + 1] - counts[S][j] for j in range(len(decades) - 1)]
        ok(all(g > 0 for g in gains),
           f"R2: S={S} gains a window in every decade")
    print("    The fate <=> object identity: the window set IS the conjecture's")
    print("    set, so unbounded-windows <=> S-smooth shifted primes infinite")
    print("    (Pi_2, EQUIVALENT -- vs explore_abscissa_reserve.py's "
          "sufficient-only certificate);")
    print("    the stall face <=> finiteness (Sigma_2). One open conjecture")
    print("    per alphabet: S={2} Fermat, S={2,3} the Pierpont family, ...")
    print()
    return counts


# ═══════════════════════════════════════════════════════════════════════
# R3 — THE REACH CHART: levels x kinds, equivalence-flagged
# ═══════════════════════════════════════════════════════════════════════

CHART = [
    # (fate, classical object, level, kind, status, equiv?)
    ("every prime a lock target (B1)", "EX prime in an AP (Dirichlet)",
     "Sigma_1", "existence", "PROVED", True),
    ("l^e edit feasible (B3)", "EX a: l^e*2^a+1 prime (Proth)",
     "Sigma_1", "existence", "open/instance", True),
    ("l^e edit impossible (B3')", "l^e Sierpinski (covering)",
     "Pi_1", "existence", "PROVED at 78557", True),
    ("alphabet-S windows unbounded (R2)", "S-smooth shifted primes infinite",
     "Pi_2", "existence", "OPEN (every S)", True),
    ("alphabet-S window stall (R2')", "S-smooth shifted primes finite",
     "Sigma_2", "existence", "OPEN (every S)", True),
    ("sigma_c = +inf endpoint (abscissa reserve)", "Pierpont primes infinite",
     "Pi_2", "existence", "OPEN", False),
    ("every char-0 trajectory locks (B2)", "no infinite Proth carrier ladder",
     "Pi_2", "existence", "OPEN", True),
    ("transparency-density -> 1 (transparency bridge)", "smooth shifted-prime density",
     "density", "density", "OPEN", True),
    ("size/rank reserve thresholds (ledger threshold/reserve zoo)", "GD / PD spectrum / Artin",
     "constant", "average", "OPEN", True),
    ("abscissa reserve", "friable divergence (Lichtman)",
     "theorem", "abscissa", "SETTLED", True),
]


def section_R3():
    print("R3  THE REACH CHART (fate -> object: levels x kinds)")
    print(f"    {'fate':42s} {'level':8s} {'kind':10s} {'status':16s} equiv")
    for fate, obj, lvl, kind, status, eq in CHART:
        print(f"    {fate:42s} {lvl:8s} {kind:10s} {status:16s} "
              f"{'EQUIV' if eq else 'suff-only'}")
        print(f"      -> {obj}")
    levels_eq = {lvl for _, _, lvl, kind, _, eq in CHART
                 if eq and kind == "existence"}
    ok(levels_eq == {"Sigma_1", "Pi_1", "Sigma_2", "Pi_2"},
       "R3: every arithmetic level Sigma_1/Pi_1/Sigma_2/Pi_2 hit by an "
       "EQUIVALENCE (surjectivity with equivalences)")
    pi2 = [row for row in CHART if row[2] == "Pi_2"]
    ok(len(pi2) >= 3 and sum(1 for r in pi2 if r[5]) >= 2,
       "R3: Pi_2 many-to-one, with >= 2 equivalent objects beside the "
       "sufficient-only certificate")
    ok(all(kind != "existence" for _, _, lvl, kind, _, _ in CHART
           if lvl not in ("Sigma_1", "Pi_1", "Sigma_2", "Pi_2")),
       "R3: everything past Pi_2 is a KIND change (density/average/abscissa), "
       "not a level climb")
    print()


# ═══════════════════════════════════════════════════════════════════════
# R4 — THE CASCADE CENSUS: all-miss depths kill bounded-cap ladders
# ═══════════════════════════════════════════════════════════════════════

SMALL_PRIMES = None  # trial-division primes, set in main


def canonical_multipliers(p, M):
    """Carrier m*p^(v+1)+1: m odd for p=2; m even, p-coprime for odd p."""
    if p == 2:
        return [m for m in range(1, M, 2)]
    return [m for m in range(2, M, 2) if m % p != 0]


def certify_composite(n):
    """Return a small factor if trial division finds one, else None
    (caller falls back to the MR-composite verdict, itself a proof)."""
    for q in SMALL_PRIMES:
        if q * q > n:
            return None
        if n % q == 0:
            return q
    return None


def exponent_hit(p, e, ms):
    """Least multiplier with m*p^e+1 prime at exponent e, else None."""
    base = p ** e
    for m in ms:
        n = m * base + 1
        f = certify_composite(n)
        if f is not None:
            continue
        if is_primeZ(n):
            return m
    return None


def first_all_miss(p, M, ecap):
    """First all-miss exponent e >= 2 (carrier m*p^(v+1)+1, depth v = e-1)."""
    ms = canonical_multipliers(p, M)
    for e in range(2, ecap + 1):
        if exponent_hit(p, e, ms) is None:
            return e
    return None


def section_R4():
    print("R4  THE CASCADE CENSUS (carrier m*p^(v+1)+1 = m*p^e+1, cap m < M)")
    # predicted: p=2, M=8 -- hits at e=2..8 then all-miss at e=9 (depth v=8)
    ms8 = canonical_multipliers(2, 8)
    ok(ms8 == [1, 3, 5, 7], "R4: canonical multipliers p=2 M=8 = {1,3,5,7}")
    hits = [exponent_hit(2, e, ms8) for e in range(2, 9)]
    least = [m * 2 ** e + 1 for e, m in zip(range(2, 9), hits)]
    print(f"    p=2 M=8: least prime per exponent e=2..8: {least}")
    ok(least == [5, 41, 17, 97, 193, 641, 257],
       "R4: predicted hit list e=2..8 reproduced")
    A28 = first_all_miss(2, 8, 50)
    ok(A28 == 9, "R4: first all-miss exponent A(2,8) = 9 (predicted hand value)")
    print("    all-miss certificate at e=9 (every candidate composite):")
    for m in ms8:
        n = m * 2 ** 9 + 1
        f = certify_composite(n)
        print(f"      {m}*2^9+1 = {n} = {f} * {n // f}")
        ok(f is not None and n % f == 0, f"R4: certified factor of {n}")
    # the cap ladder: A(p, M) growth
    print("    first all-miss exponent A(p, M) (certified kill of every")
    print("    bounded-cap ladder, modulo the explore_module_law.py reduction):")
    ECAP = 700
    amiss = {}
    for p, caps in [(2, [8, 16, 32, 64, 128, 256]), (3, [9, 27, 81]),
                    (5, [25, 125])]:
        row = []
        for M in caps:
            a = first_all_miss(p, M, ECAP)
            amiss[(p, M)] = a
            row.append(f"A({p},{M})={a if a else f'>{ECAP}'}")
        print(f"      p={p}: " + "  ".join(row))
        ok(all(amiss[(p, M)] is not None for M in caps[:2]),
           f"R4: all-miss exponents exist at p={p} for the first two caps")
    # hit-density decay: p=2, M=8, e <= 1001 by centuries
    dens = []
    for c in range(10):
        h = sum(1 for e in range(100 * c + 2, 100 * c + 102)
                if exponent_hit(2, e, ms8) is not None)
        dens.append(h)
    print(f"    p=2 M=8 hits per century e=2..1001: {dens}")
    ok(dens[0] > dens[-1], "R4: hit density decays (first vs last century)")
    ok(sum(dens[5:]) < sum(dens[:5]),
       "R4: hit density decays (second half < first half)")
    exp_tail = sum(4 / (e * log(2)) for e in range(502, 1002))
    print(f"    heuristic E[hits e=502..1001] ~ 4/(e ln 2) sum = {exp_tail:.1f} "
          f"(observed {sum(dens[5:])})")
    print("    THE PIN: per-stage existence needs a prime == 1 mod p^(v+1)")
    print("    in a window LINEAR in the modulus -- GRH's ~q^2 worst case")
    print("    cannot certify even one large stage. MODEL THRESHOLD: a")
    print("    Cramer-model ladder survives iff its cap grows >~ v ln v")
    print("    (wander >= logarithmic in depth); slower dies a.s. Every")
    print("    CENSUSED cap dies at its certified exponent; the open")
    print("    content is wander growth, priced at log-depth rate.")
    print()


def main():
    global SMALL_PRIMES
    build_spf(X)
    SMALL_PRIMES = [p for p in range(2, 3000) if _spf[p] == p]
    primes = [p for p in range(2, X + 1) if _spf[p] == p]
    win = section_R1(primes)
    section_R2(primes, win)
    section_R3()
    section_R4()
    print(f"{PASS} checks pass, {FAIL} fail")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
