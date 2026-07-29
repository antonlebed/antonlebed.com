"""
explore_vsa_encoder.py -- the exact VSA (MULTIPLICATIVE) as a ring-native encoder.

THE QUESTION. explore_grammar_growth.py showed the collision-grown substrate
tracks the ENCODING, not the grammar, under the natural PLACE-VALUE encoding
(additive: a surface form is a base-B integer; a paradigm is form = lexeme +
offset). Its through-line: the substrate is a stream-independent counter, so the
data-facing leverage lives in the ENCODER. explore_collision_growth.py and
explore_grammar_growth.py both used ADDITIVE encoders. This script swaps the
encoder's binding operation for the project's OWN native one -- the exact VSA of
explore_meaning_codeword.py: bind = MULTIPLY, unbind = divide by the meadow
inverse. Two
questions: (A) does the multiplicative encoder confer the analogical-completion
capability a non-compositional control cannot -- the capability lift in the
ANALOGY modality (transform extraction, the VSA's signature)? (B) does the
multiplicative encoder open the substrate door that the additive place-value
encoder left SHUT -- is the door's closure ENCODER-FAMILY-INVARIANT?

THE RING. RAD = Z/510510 (the canonical VSA ring of explore_meaning_codeword.py;
k = 7, factors {2, 3, 5, 7, 11, 13, 17}). Exact binding and the meadow laws carry on any product
of fields (the squarefree floor), so RAD suffices -- the d = 4 snap is not needed
for bind/unbind. Lexemes and feature-offsets are UNITS of RAD (coprime to 510510);
form(L, cell) = L * prod_f g_f[v_f] mod 510510, itself a unit -- exact VSA bind.
Pool for collision growth = POOL5 = [2, 3, 5, 7, 11] (explore_grammar_growth.py's
"easiest door"; the small factors of the modulus).

THE TWO HALVES.
  (A) ANALOGY (the VSA's signature; the task shape SIGMORPHON's shared tasks call
      paradigm completion). a : b :: c : d. With a = L1*c1, b = L1*c2, the transform
      T = b * a^-1 = c2 * c1^-1 is LEXEME-INDEPENDENT (L1 cancels). Applied to a
      held-out query c = L2*c1 it gives T*c = L2*c2 = form(L2, c2), EXACT. Test:
      designate cell 0 the citation form; extract each cell's transform from ONE
      anchor lexeme; fill every held-out (lexeme != anchor, cell != 0). CONTROL:
      a non-compositional random bijection of (lexeme, cell) -> unit (no algebraic
      transform), so the extracted T mis-applies.
  (B) SUBSTRATE DOOR (explore_grammar_growth.py one level up). Forms are integers
      in [0, 510510); collision-grow over their difference sets with POOL5. Encode
      the SAME paradigm both additively and multiplicatively and compare.

THE HAND-DERIVATION (frozen pre-engine; adjudicated in the RUN RECORD).
  Convention (re-derived, mint guard): bind = multiply; unbind of b by a is
  b * a^-1 (a^-1 = pow(a, -1, N) exact iff gcd(a, N) = 1, else the meadow pinv,
  which recovers surviving windows). The transform sending a -> b is T = b * a^-1
  (T*a = b), applied to the query. Hand pair (N = 510510): L1 = 19, L2 = 23,
  c1 = 29, c2 = 31 (all units). a = 551, b = 589, query c = 23*29 = 667,
  truth = 23*31 = 713. T*c = 589 * 551^-1 * 667 = (19*31) * 23 * 19^-1 = 31*23
  = 713 -- exact (551^-1 * 29 = 19^-1 since 551 = 19*29). The engine must print 713.

  The door mechanism: a same-lexeme cross-cell difference is
  form(L, c2) - form(L, c1) == L*(c2 - c1) (mod any p | N), so a pool prime p
  RESOLVES it iff p does not divide (c2 - c1) -- L is a unit, contributing no pool
  factor. This is IDENTICAL to the additive encoder's (c2 - c1) resolvability, so
  multiplicative and additive grow the SAME substrate on same-lexeme demand
  (mechanism-proved). The difference from additive: additive same-lexeme demand
  COMPRESSES to the lexeme-independent offset-difference set {c2 - c1}
  (explore_grammar_growth.py finding 2); multiplicative gives {L_i*(c2 - c1)}, one
  per lexeme -- NO compression, though each resolves identically. Under
  multiplicative binding compositionality is INVISIBLE as difference-set
  compression; it shows only in the unbind/analogy capability. Multi-feature and
  cross-lexeme differences under multiplication are differences of PRODUCTS
  (L_i*c - L_j*c'), scrambled -> generic-looking -> redundantly coverable -> not
  unique-need. So the door stays SHUT for multiplicative too.

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN RECORD).
  PR1 (analogy lift). The VSA fills held-out (lexeme, cell) at accuracy 1.000; the
      non-compositional control near 0 (exact integer match is structureless). The
      lift explore_composition_lift.py showed for fixed-function readout, now via
      TRANSFORM EXTRACTION -- a new modality, the VSA's own move.
  PR2 (the unit price -- the nativeness cost). Exact unbind needs the anchor form a
      UNIT. A unit encoder gives analogy 1.000; a random-INTEGER encoder degrades,
      and does so WINDOW-BY-WINDOW (the meadow pinv recovers the windows where a is
      a unit, garbles the rest) -- graded, not catastrophic. The native cure is to
      encode into the unit group (structural, generic -- NOT a per-task codebook),
      restoring 1.000 at capacity phi(N). This distinguishes the two kill clauses:
      the CAPABILITY is native; OPENING THE DOOR is not (PR4).
  PR3 (the door -- KILL headline). The multiplicative encoder does NOT open the
      substrate door. On a shared paradigm the multiplicative and additive encoders
      grow the SAME substrate (same-lexeme resolvability provably identical), the
      multiplicative loses only the difference-set COMPRESSION, and sibling
      cross-transfer is near-intact -- the door's closure is ENCODER-FAMILY-
      INVARIANT (neither the additive place-value nor the native multiplicative VSA
      opens it natively).
  PR4 (the SURVIVE control). A DESIGNED multiplicative encoder with c2 - c1 chosen
      unique-need (== 770 times a unit) DOES open the door: its demanding stream
      grows [3] while a 3-sublattice sibling skips 3 and leaves it unresolved. The
      rig CAN see the door open, so PR3's null is a real null -- and the opening
      re-imports the structure (hand-tuned offsets), exactly the additive S5 result.

THE KILL-SHAPE (printed observable). PR3 fires (multiplicative grows the same /
generic substrate as additive, transfer near-intact) AND PR1 fires (the rig
actually performs compositional binding, so the null is not a dead rig). THE
SURVIVE-SHAPE: some NATIVE (non-designed) multiplicative encoder yields unique-need
differences without hand-tuning the offsets.

POSITIVE CONTROLS (run before any verdict is read). (a) the imported resolves()
== product form == CRT-tuple test. (b) the hand pair: T*667 == 713 exactly.
(c) the engine's unique-need difference 770 still grows [3] on POOL5 (the door CAN
open). (d) unit inverse: a * pow(a, -1, N) % N == 1 on sampled units, and the
meadow pinv satisfies x * pinv(x) == e_support(x) on sampled non-units.

FINDINGS (tiers inline; run record below; all sections assert).

1. THE ANALOGY LIFT IS REAL, VIA TRANSFORM EXTRACTION (observation at scope; S1).
   The exact VSA fills every held-out (lexeme, cell) at 55/55 = 1.000 -- extract
   T_c = form(anchor, c) * form(anchor, citation)^-1 from ONE anchor lexeme, apply
   to every other lexeme's citation form, recover its cell c exactly. The matched
   non-compositional control (a random bijection to units) scores 0/55 = 0.000. This
   reproduces the capability lift explore_composition_lift.py established, in
   a NEW modality -- transform extraction (the VSA's own a:b::c:? move), not fixed-
   function readout -- and it is exact because the lexeme CANCELS from the ring
   transform (T = c2 * c1^-1, lexeme-free), the systematic-generalization guarantee.

2. THE NATIVENESS PRICE IS UNIT MEMBERSHIP, PAID PER WINDOW (observation at scope;
   S2). Exact unbind needs the anchor form a UNIT. A multiplicative encoder with
   NON-UNIT factors (unit fraction 0.028) completes only 3/55 = 0.055 exactly, BUT
   its per-WINDOW accuracy is 277/385 = 0.719: the meadow pseudo-inverse recovers
   every channel on which the anchor is invertible and garbles the rest, so the
   compositional signal degrades GRACEFULLY (window by window), never to garbage.
   The native cure is structural, not per-task: encode into the unit group
   (form(i, c) = L_i * K_c with L_i, K_c units) restores 55/55 = 1.000 at capacity
   phi(N). So the CAPABILITY is native (unit encoding is a generic constraint); only
   the door-opening is not (finding 4).

3. THE DOOR VERDICT IS ENCODER-FAMILY-INVARIANT (rule, mechanism-proved + S3). A
   same-lexeme cross-cell difference is form(L, c2) - form(L, c1) == L*(c2 - c1)
   (mod any p | N), so a pool prime resolves it iff it does not divide the CELL
   difference (c2 - c1) -- the unit lexeme L cancels. On a paradigm with SHARED cell
   values, the additive encoder (form = base + K_c) and the multiplicative encoder
   (form = L*K_c) therefore grow the IDENTICAL substrate [3, 5, 7]; the only
   difference is COMPRESSION -- additive's same-lexeme demand is the lexeme-
   independent K-difference set (|D| = 15), multiplicative's is one copy per lexeme
   (|D| = 180) with identical resolvability. So under multiplicative binding
   compositionality is INVISIBLE as difference-set compression (it lives in the
   unbind capability, finding 1), and the substrate-door verdict does not depend on
   which binding operation the encoder uses. (Both grow a set that SKIPS 2: units are
   coprime to 2, hence odd, so every cell difference is even and 2 resolves nothing
   -- a sublattice imprint of the UNIT constraint itself, not of the grammar,
   reinforcing "the substrate tracks the encoding.")

4. THE MULTIPLICATIVE DOOR STAYS SHUT; ONLY A DESIGNED TRANSFORM OPENS IT
   (observation + rule; S4). Multiplicative-paradigm sibling streams grow
   [3, 5, 7, 11] and cross-transfer NEAR-INTACT (leak 2, 0.134% -- the
   explore_grammar_growth.py wall-survival standard). A DESIGNED multiplicative
   encoder with a unique-need cell GAP (cells K0, K1 = K0 + 770 both units, so the
   same-lexeme diff L_i*(K1 - K0) = L_i*770 = 2*5*7*11 is resolvable only by 3) opens
   the engine's own door: its demanding stream grows [3] while a 3-sublattice sibling
   grows [2, 5, 7] (skips 3) and leaves 770 unresolved (gap 1) -- reachable only by
   hand-tuning the gap to BE unique-need, re-importing the structure, as the additive S5.

THE VERDICT. The encoder cast SPLITS cleanly. The exact VSA as a ring-native
encoder DOES confer the analogical-completion capability a non-compositional
control cannot (finding 1), at a native and structural price -- unit membership,
paid gracefully per window (finding 2). But swapping the encoder's binding
operation from additive to the project's own multiplicative one does NOT change the
substrate-door verdict: same-lexeme resolvability is the cell-difference's whichever
operation binds (finding 3), so the door stays SHUT for the native multiplicative
encoder and opens only for a DESIGNED unique-need transform that re-imports the
structure (finding 4). This DEEPENS explore_grammar_growth.py's KILL of the native
route: the door's closure is not an artifact of the place-value encoding -- it is
ENCODER-FAMILY-INVARIANT across the two natural binding operations. The leverage the
grammar test located in the encoder is real for CAPABILITY (the encoder is where
compositional generalization lives) but does NOT extend to the substrate door (no
native encoder opens it). Honest limit: hand-designed, toy scope, RAD and the
5-prime pool, these paradigm families; the transform mechanism and the encoder-
invariance of same-lexeme resolvability are rules (mechanism-proved), the lift, the
per-window price, and the transfer verdicts are observations at scope.

RUN RECORD (python explore_vsa_encoder.py, ~1 s, trivial memory):
  S0 controls: 3000 resolve==product==CRT; hand pair T*667 = 713; 770 -> [3];
     unit a*a^-1==1 (500), non-unit x*pinv(x)==e_support(x) (500)
  S1 lift:     VSA 55/55 = 1.000; non-compositional control 0/55 = 0.000
  S2 price:    non-unit encoder exact 3/55 = 0.055, per-window 277/385 = 0.719
     (graded); native cure (units) 55/55 = 1.000
  S3 invariant: shared cells -> additive |D| 15 grew [3,5,7]; multiplicative |D| 180
     grew [3,5,7] (identical); multiplicative loses compression, both skip 2
  S4 door:     multiplicative siblings [3,5,7,11] leak 2 (0.134%, near-intact);
     designed mult. cell-gap 770 (K0=41) -> [3], 3-sublattice sibling [2,5,7] gap 1
  TOTAL 4011 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run (git history).
PR1 (analogy lift) and PR2 (the unit price, graded per-window) landed exactly. PR4
(the designed door opens) landed exactly. PR3's HEADLINE (the door is encoder-
family-invariant, closed for multiplicative) landed, but its sub-claim "additive and
multiplicative grow the SAME set" was REFINED by a hand-derivation error the engine
caught: the identity holds only when the two encoders share the SAME cell values
(the first run compared additive small offsets [0..4] against multiplicative random
units and they diverged [2,3] vs [3,5] -- the L-cancels mechanism was right, but the
CELL differences must match for the sets to coincide). Once the paradigm is shared,
the sets are identical ([3,5,7]) as the mechanism predicts. A bonus the run
surfaced: encoding into UNITS forces every cell difference even, so the grown
substrate SKIPS 2 -- a sublattice imprint of the unit constraint, an encoding
effect, not grammar.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import prod, gcd
from itertools import combinations

from explore_collision_growth import (
    grow_least_new, unresolved_diffs, resolves, diffs_of,
)

CHECKS = 0

N = 510510                                  # RAD modulus
FACTORS = [2, 3, 5, 7, 11, 13, 17]          # RAD channels
POOL5 = [2, 3, 5, 7, 11]                    # growth pool -- the easiest door


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# --------------------------------------------------------- ring machinery

def is_unit(x):
    return gcd(x % N, N) == 1


def inv_unit(x):
    return pow(x % N, -1, N)


def pinv(x):
    """Meadow pseudo-inverse on RAD: channelwise inverse, 0 on the zero windows;
    x * pinv(x) == e_support(x) (the element-as-operator law)."""
    y = 0
    for p in FACTORS:
        xp = x % p
        rp = pow(xp, -1, p) if xp else 0            # inverse on support, else 0
        # CRT-merge residue rp at prime p into y
        m = N // p
        y = (y + rp * m * pow(m, -1, p)) % N
    return y


def support_idem(x):
    """e_support(x): 1 on windows where x is nonzero, 0 elsewhere (a codeword)."""
    e = 0
    for p in FACTORS:
        rp = 1 if x % p else 0
        m = N // p
        e = (e + rp * m * pow(m, -1, p)) % N
    return e


def rand_unit(rng):
    while True:
        x = rng.randrange(1, N)
        if is_unit(x):
            return x


# ------------------------------------------------------------- encoders

def vsa_paradigm(rng, n_lex, n_cell):
    """Multiplicative: form(i, c) = L_i * K_c mod N, all units. Returns
    (forms{(i,c):v}, lexemes, cells)."""
    lex = [rand_unit(rng) for _ in range(n_lex)]
    cells = [rand_unit(rng) for _ in range(n_cell)]
    forms = {(i, c): (lex[i] * cells[c]) % N
             for i in range(n_lex) for c in range(n_cell)}
    return forms, lex, cells


def additive_paradigm(rng, n_lex, offsets):
    """Additive: form(i, c) = base_i + offsets[c] (the place-value view)."""
    base = rng.sample(range(100000), n_lex)
    return {(i, c): base[i] + offsets[c]
            for i in range(n_lex) for c in range(len(offsets))}


def noncompositional(rng, n_lex, n_cell):
    """Control: each (lexeme, cell) an independent random unit -- no transform."""
    vals = set()
    while len(vals) < n_lex * n_cell:
        vals.add(rand_unit(rng))
    vals = list(vals)
    out, k = {}, 0
    for i in range(n_lex):
        for c in range(n_cell):
            out[(i, c)] = vals[k]
            k += 1
    return out


# --------------------------------------------------- the analogy protocol

def complete_paradigm(forms, n_lex, n_cell, anchor=0, cite=0, unbind=inv_unit):
    """Fill every held-out (lexeme != anchor, cell != cite) by the transform
    T_c = form(anchor, c) * unbind(form(anchor, cite)) extracted from the anchor,
    applied to each lexeme's citation form. Returns (correct, total)."""
    correct = total = 0
    for c in range(n_cell):
        if c == cite:
            continue
        T = (forms[(anchor, c)] * unbind(forms[(anchor, cite)])) % N
        for i in range(n_lex):
            if i == anchor:
                continue
            pred = (T * forms[(i, cite)]) % N
            correct += (pred == forms[(i, c)])
            total += 1
    return correct, total


# --------------------------------------------------------- S0: controls

def s0_controls():
    print("S0: positive controls")
    rng = random.Random(20250609)
    for _ in range(3000):
        k = rng.randrange(1, 5)
        S = rng.sample(POOL5, k)
        x, y = rng.randrange(3000), rng.randrange(3000)
        pf = (x - y) % prod(S) != 0
        tf = any(x % p != y % p for p in S)
        check(resolves(S, x, y) == pf and resolves(S, x, y) == tf, "engine control")
    print("  imported resolve() == product == CRT-tuple (3000 samples)")

    L1, L2, c1, c2 = 19, 23, 29, 31
    a, b, q = (L1 * c1) % N, (L1 * c2) % N, (L2 * c1) % N
    T = (b * inv_unit(a)) % N
    d = (T * q) % N
    check(d == (L2 * c2) % N == 713, f"hand pair completed to {d}, expected 713")
    print(f"  hand pair a=551 b=589 query=667 -> T*query = {d} (truth 713)")

    S = grow_least_new({770}, POOL5)
    check(S == [3], f"unique-need 770 grew {S}, expected [3]")
    print(f"  engine unique-need 770 -> grew {S}: the door CAN open")

    for _ in range(500):
        u = rand_unit(rng)
        check((u * inv_unit(u)) % N == 1, "unit inverse failed")
    for _ in range(500):
        x = rng.randrange(N)
        check((x * pinv(x)) % N == support_idem(x), "meadow pinv != e_support")
    print("  unit a*a^-1 == 1 (500); non-unit x*pinv(x) == e_support(x) (500)")


# ------------------------------------------------ S1: the analogy lift

def s1_analogy_lift(n_lex=12, n_cell=6):
    print("\nS1: the analogy lift -- transform extraction (PR1)")
    rng = random.Random(41)
    vsa, _, _ = vsa_paradigm(rng, n_lex, n_cell)
    ctrl = noncompositional(rng, n_lex, n_cell)
    cv, tv = complete_paradigm(vsa, n_lex, n_cell)
    cc, tc = complete_paradigm(ctrl, n_lex, n_cell)
    print(f"  {n_lex} lexemes x {n_cell} cells; anchor + citation form observed,")
    print(f"  every other (lexeme, cell) held out ({tv} completions)")
    print(f"  VSA (multiplicative)   held-out exact: {cv}/{tv} = {cv/tv:.3f}")
    print(f"  non-compositional ctrl held-out exact: {cc}/{tc} = {cc/tc:.3f}")
    check(cv == tv, "VSA did not complete every held-out cell")
    check(cc == 0, "control completed a held-out cell (should be structureless)")
    print("  => the exact VSA fills novel lexeme x cell combinations; the matched")
    print("     control cannot -- systematic generalization by transform extraction")


# ---------------------------------------------------- S2: the unit price

def s2_unit_price(n_lex=12, n_cell=6):
    print("\nS2: the unit price -- exact unbind needs a UNIT (PR2)")
    rng = random.Random(17)
    # multiplicative encoder with NON-UNIT factors: form = lex_i * K_c, both random
    # residues (mostly non-units) -- the compositional structure is PRESENT but the
    # anchor is usually not invertible, so exact unbind is unavailable.
    lex = [rng.randrange(N) for _ in range(n_lex)]
    cells = [rng.randrange(N) for _ in range(n_cell)]
    forms = {(i, c): (lex[i] * cells[c]) % N
             for i in range(n_lex) for c in range(n_cell)}
    unit_frac = sum(is_unit(v) for v in forms.values()) / len(forms)
    ci, ti = complete_paradigm(forms, n_lex, n_cell, unbind=pinv)
    # per-WINDOW accuracy of the same completions (graded recovery)
    win_ok = win_tot = 0
    for c in range(1, n_cell):
        T = (forms[(0, c)] * pinv(forms[(0, 0)])) % N
        for i in range(1, n_lex):
            pred = (T * forms[(i, 0)]) % N
            truth = forms[(i, c)]
            for p in FACTORS:
                win_ok += (pred % p == truth % p)
                win_tot += 1
    print(f"  non-unit multiplicative encoder: unit fraction of forms {unit_frac:.3f}"
          f"  (products of two random residues ~ (phi/N)^2)")
    print(f"  exact-match analogy: {ci}/{ti} = {ci/ti:.3f}  (unbind = meadow pinv)")
    print(f"  per-WINDOW accuracy: {win_ok}/{win_tot} = {win_ok/win_tot:.3f}"
          f"  -- GRADED recovery (correct on windows where the anchor is a unit)")
    # native cure: encode into the unit group
    vsa, _, _ = vsa_paradigm(random.Random(17), n_lex, n_cell)
    cu, tu = complete_paradigm(vsa, n_lex, n_cell)
    print(f"  native cure (encode into units): {cu}/{tu} = {cu/tu:.3f}")
    check(win_ok / win_tot > ci / ti + 0.2, "per-window not better than exact")
    check(cu == tu, "unit encoder did not restore exact analogy")
    print("  => the price of exact analogy is UNIT membership; a structural (not")
    print("     per-task) cure at capacity phi(N) -- the CAPABILITY is native")


# -------------------------------------- S3: additive vs multiplicative door

def same_lexeme_diffs(forms):
    by_lex = {}
    for (i, c), v in forms.items():
        by_lex.setdefault(i, []).append(v)
    D = set()
    for vs in by_lex.values():
        for a, b in combinations(vs, 2):
            if a != b:
                D.add(abs(a - b))
    return D


def s3_encoder_invariant(n_lex=12):
    print("\nS3: additive vs multiplicative -- same substrate, no compression (PR3a)")
    rng = random.Random(5)
    # SAME paradigm for both encoders -- same lexemes, same cell values K_c (units);
    # only the binding op differs (+ vs *). Additive base need not be a unit.
    n_cell = 6
    K = [rand_unit(rng) for _ in range(n_cell)]                 # shared cell values
    base = rng.sample(range(1000000), n_lex)                    # additive lexemes
    lex = [rand_unit(rng) for _ in range(n_lex)]                # multiplicative lexemes
    add = {(i, c): base[i] + K[c]
           for i in range(n_lex) for c in range(n_cell)}
    mul = {(i, c): (lex[i] * K[c]) % N
           for i in range(n_lex) for c in range(n_cell)}
    Da, Dm = same_lexeme_diffs(add), same_lexeme_diffs(mul)
    Sa, Sm = grow_least_new(Da, POOL5), grow_least_new(Dm, POOL5)
    print(f"  shared cells K_c; additive form = base+K, multiplicative form = lex*K")
    print(f"  additive same-lexeme demand:       |D| {len(Da):4d}  grew {Sa}")
    print(f"  multiplicative same-lexeme demand: |D| {len(Dm):4d}  grew {Sm}")
    check(len(Dm) > len(Da), "multiplicative D not larger (compression not lost)")
    check(Sa == Sm, "additive and multiplicative grew different substrates")
    print(f"  => multiplicative loses the compression (|D| {len(Dm)} vs {len(Da)})")
    print(f"     but grows the IDENTICAL substrate {Sm}: same-lexeme resolvability is")
    print("     the cell-difference's (L a unit cancels) -- door verdict encoder-invariant")


# ------------------------------------ S4: the door crux + designed control

def diffs_of_cells(forms):
    items = list(forms.items())
    D = set()
    for (ka, va), (kb, vb) in combinations(items, 2):
        if ka[1] != kb[1] and va != vb:            # different cell, distinct value
            D.add(abs(va - vb))
    return D


def s4_door_crux(n_lex=10, n_cell=6):
    print("\nS4: the door crux -- multiplicative stays SHUT; designed opens (PR3b/PR4)")
    rng = random.Random(9)

    def sibling(build):
        DA, DB = build(), build()
        SA, SB = grow_least_new(DA, POOL5), grow_least_new(DB, POOL5)
        resid = max(len(unresolved_diffs(SA, DB)), len(unresolved_diffs(SB, DA)))
        frac = resid / max(len(DA), len(DB), 1)
        return SA, resid, frac

    def build_vsa():
        return diffs_of_cells(vsa_paradigm(rng, n_lex, n_cell)[0])

    SA, resid, frac = sibling(build_vsa)
    print(f"  multiplicative paradigm siblings: grew {SA}, cross-transfer leak"
          f" {resid} ({frac:.3%})")
    check(frac <= 0.02, "multiplicative sibling transfer not near-intact")

    # PR4: a DESIGNED MULTIPLICATIVE encoder whose cell GAP is unique-need. Cells
    # K0, K1 = K0 + 770 both units => same-lexeme diff = L_i*(K1 - K0) = L_i*770,
    # resolvable only by 3 (770 = 2*5*7*11, L_i a unit). Hand-tuning the gap to BE
    # unique-need re-imports the structure -- exactly the additive-encoder S5 move.
    K0 = next(k for k in range(3, N) if is_unit(k) and is_unit(k + 770))
    Kd = [K0, K0 + 770]
    Ld = [rand_unit(rng) for _ in range(6)]
    des = {(i, c): (Ld[i] * Kd[c]) % N for i in range(6) for c in range(2)}
    Sd = grow_least_new(same_lexeme_diffs(des), POOL5)
    check(Sd == [3], f"designed cell-gap 770 grew {Sd}, expected [3]")
    sib = {(i, c): 3 * i + 3 * c for i in range(8) for c in range(6)}
    Ssib = grow_least_new(diffs_of_cells(sib), POOL5)
    gap = len(unresolved_diffs(Ssib, {770}))
    print(f"  designed multiplicative gap 770 (K0={K0}): demanding stream grows {Sd};")
    print(f"    a 3-sublattice sibling grows {Ssib} (skips 3), leaves 770 unresolved: gap {gap}")
    check(3 not in Ssib and gap == 1, "designed door did not open")
    print("  => the native multiplicative door is SHUT (near-intact transfer); it opens")
    print("     only for a DESIGNED unique-need cell gap -- re-import, as additive")


if __name__ == "__main__":
    s0_controls()
    s1_analogy_lift()
    s2_unit_price()
    s3_encoder_invariant()
    s4_door_crux()
    print(f"\nALL SECTIONS PASS -- {CHECKS} checks, exit 0")
