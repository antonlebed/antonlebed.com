"""
explore_grammar_growth.py -- is LANGUAGE-shaped structure unique-need?

THE QUESTION. explore_collision_growth.py proved learning-as-collision-driven-
growth IS greedy set-cover over a stream's difference set D (a substrate S of
primes resolves inputs (x, y) iff prod(S) does not divide x - y). Its verdict was
CONTINGENT and it pinned a FLIP CONDITION: generic and merely-sublattice data
grow a stream-INDEPENDENT primorial prefix (the wall survives -- the substrate is
a counter, blind to content), and the wall DISSOLVES (data picks the destination)
only under a UNIQUE-NEED difference -- one divisible by every pool prime but one
(770 = 2*5*7*11, resolvable only by 3), a demand no other stream makes. This
script asks the through-line to language: is LANGUAGE-shaped
structure unique-need (the substrate door opens for language) or generic-prefix
(the wall survives even for language)?

THE BRIDGE, STATED (whose vocabulary). The set-cover object is DIFFERENCES of
integers. Grammar's object is FORMS, CATEGORIES, and systematic TRANSFORMS. The
bridge is an ENCODING of forms as integers, and the whole result hinges on it, so
streams are defined in GRAMMAR's vocabulary first (stems, suffixes, paradigm
cells, transforms), THEN mapped by a STATED natural encoding, THEN reduced to D --
never defined as "differences divisible by q" (which would smuggle in the
sublattice answer). The natural encoding is place-value: a surface form is a
string of symbols read as a base-B integer, stem high-order --
enc(stem . suffix) = enc(stem)*B^len(suffix) + enc(suffix) -- the same positional
reading the tower takes windows of.

THE POOL. The primary pool is the first FIVE primes [2, 3, 5, 7, 11], where the
door is EASIEST: unique-need differences there are prod(pool)/p, i.e. 210..1155,
reachable by modest encodings. A larger pool only makes the door HARDER (unique-
need scale = the (k-1)-primorial: 30030 at k=7, 2e11 at k=12). Giving grammar the
small pool is giving it its fairest shot; a null there is a strong null.

THE UNIQUE-NEED METRIC (coverage multiplicity). For a difference d and pool P,
cov(d) = #{p in P : p does not divide d} = how many pool primes RESOLVE d.
UNIQUE-NEED is exactly cov(d) == 1: d divisible by every pool prime but one, so a
single prime is the sole resolver. Local, minimal-pair-like distinctions are SMALL
differences, hence divisible by few primes, hence HIGH cov (redundantly coverable);
unique-need is the opposite extreme -- a large, maximally composite difference.
min cov over D is a diagnostic (does the data carry a unique-need difference at
all?); the DECISIVE wall observable is the direct cross-stream transfer residual
(the engine's S3 method) -- and the run shows the two can disagree (unique-need
present yet transfer near-intact), so the residual, not min cov, adjudicates.

THE GRAMMAR FAMILIES (each in grammar's vocabulary, then encoded).
  1. CONCATENATIVE inflection: stems (random strings) x suffixes (endings);
     form = stem . suffix. Two supervised tasks -- FEATURE (label = suffix, the
     inflectional category; must-separate = different suffix) and LEMMA (label =
     stem; must-separate = different stem). Bases B = 29 (prime) and 30 (=2*3*5)
     to expose base factorization.
  2. COMPOSITIONAL paradigm (the exact VSA / analogical view):
     lexeme vectors x_i, cells with fixed additive offsets t_c (the systematic
     transform, SAME across lexemes); form = x_i + t_c, label = cell. CONTROL:
     non-compositional -- each (lexeme, cell) an independent random form, same
     count, same range -- destroying the systematic transform.
  3. FUSIONAL morphology: F features x V values, offsets o[f][v]; form =
     base + sum_f o[f][v_f], label = the feature bundle (cell). Natural (small
     offsets) and a SPREAD variant (offsets hand-pushed toward primorial scale)
     -- the fair SURVIVE shot and its price.
Matched GENERIC baselines: random labelings over the same universe with the same
class count (the explore_collision_growth.py S1 regime).

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN RECORD).
  PR1 (feature ~ generic) the inflectional-FEATURE task grows the SAME primorial
      prefix as a matched random labeling and cross-transfers to a sibling grammar
      stream near-intact (residual 0 or the boundary artifact only). Grammar's
      category distinctions are generic. [KILL contribution]
  PR2 (compositional collapse) the compositional paradigm's same-lexeme cross-cell
      demand is the FIXED offset-difference set {|t_c - t_c'|} (lexeme-INDEPENDENT,
      small), so its full difference set is far SMALLER than the matched non-
      compositional control's -- compositionality is visible arithmetically as
      difference-set COMPRESSION. But the grown substrate is STILL a generic prefix
      (compression != unique-need).
  PR3 (the crux, KILL headline) NO natural grammar family (feature, lemma,
      compositional, fusional-natural) produces a unique-need difference: min cov
      over its D is >= 2 everywhere, so cross-transfer is near-intact and the wall
      SURVIVES. Unique-need needs a (k-1)-primorial-scale composite difference; no
      local grammatical distinction makes one.
  PR4 (transplant flag) a composite base B injects B's prime factors as SUBLATTICE
      structure into same-position pairs (same-suffix, different-stem differences
      are multiples of B^len(suffix)), recreating explore_collision_growth.py's U_q
      -- NOT new grammar structure, and for the feature task those pairs share the
      label and drop out of D entirely. grammar-via-composite-base is a subset of
      the sublattice family, no unique-need added.
  PR5 (SURVIVE shot) fusional cross-cell differences are SUMS of feature offsets,
      more composite than a single offset -- yet under NATURAL (small) offsets they
      stay redundantly coverable (min cov >= 2). The door opens (a cov-1 difference
      appears, cross-transfer gap fires) ONLY for the SPREAD variant with offsets
      hand-pushed to primorial scale -- i.e. only under a DESIGNED encoder that
      re-imports the very structure it was meant to reveal.

THE DEEP READING (hypothesis, weighed against the cov metric post-run). Language
distinctions are LOCAL / minimal-pair-shaped = SMALL differences = MAXIMALLY
redundantly coverable (high cov) -- the arithmetic OPPOSITE of unique-need (large,
maximally composite, cov 1). Language would be not merely non-unique-need but
ANTI-unique-need: the worst case for the substrate door, not the best.

THE KILL-SHAPE (printed observable). Every grammar family's grown set equals the
matched-generic primorial prefix AND every cross-transfer residual is <= the
boundary artifact AND min cov over grammar differences is >= 2 => the wall survives
for language; the substrate door does not natively open. THE SURVIVE-SHAPE: some
NATURAL grammar family yields a cov-1 difference AND a genuine cross-transfer gap
=> the data picks the destination for language-shaped structure.

POSITIVE CONTROL (run before any verdict is read). (a) the imported resolves() ==
product form == CRT-tuple test on samples (re-running the engine's own control).
(b) the hand paradigm lexemes {0, 100} x offsets {0, 1, 2}: the same-lexeme
cross-cell demand {1, 2} must grow EXACTLY [2, 3]. (c) the engine's unique-need
difference 770 must STILL grow [3] on pool[:5] -- the door CAN open, so a null
result is a real null, not a dead rig. (d) the concatenation encoding: stem=[1],
suffix=[2], B=10 must give 12 (digits "1","2").

FINDINGS (tiers inline; run record below; all sections assert).

1. THE FEATURE SUBSTRATE TRACKS THE BASE, NOT THE GRAMMAR (rule, mechanism-proved;
   S1, S4). For single-symbol suffixes, an inflectional-FEATURE distinction (label
   = suffix, must-separate = different suffix) never produces a difference ==
   0 mod B: form = enc(stem)*B^L + enc(suffix), so a cross-suffix difference is
   congruent to a nonzero suffix-difference mod B (|Delta suffix| < B). Hence for a
   squarefree B every feature difference is resolved by some prime factor of B, so the
   grown substrate is CONTAINED IN B's prime factors (rule) and is exactly them when
   the stream forces each (observed): B = 30 (= 2*3*5) grows [2, 3, 5]. When B's
   factors lie OUTSIDE the pool (prime B = 29), the feature distinctions are base-free
   relative to the pool and grow the generic prefix [2, 3, 5, 7, 11]. Either way two
   same-base feature streams grow the IDENTICAL set and transfer with ZERO residual --
   the grown set is fixed by the ENCODING's base, not the grammar. (The same-suffix, different-stem pairs ARE a sublattice
   mod {2,3,5} -- 140 of 140 divisible by 30, S4 -- but they share the feature label,
   so all 140 drop out of D: the U_q sublattice of explore_collision_growth.py
   recreated by the base and rendered task-invisible.)

2. COMPOSITIONALITY IS DIFFERENCE-SET COMPRESSION (rule + observation; S2). A
   compositional paradigm (form = lexeme_i + offset_c, one systematic transform per
   cell) has same-lexeme cross-cell demand EXACTLY the offset-difference set
   {|t_c - t_c'|} = [1, 2, 3, 4], lexeme-independent -- so its full difference set
   (|D| = 431) is markedly smaller than a matched non-compositional control's
   (|D| = 644, each cell an independent random form). Compositionality is visible
   arithmetically as compression. But both grow the SAME generic prefix
   [2, 3, 5, 7, 11]: compression is not unique-need.

3. THE CRUX -- UNIQUE-NEED IS PRESENT YET THE WALL SURVIVES (observation at scope;
   S3). Every natural family carries unique-need (cov-1) differences -- feature 5,
   lemma 8-17, compositional 2, fusional 1 -- and lemma B=30 even carries a cov-0
   difference (4620 = 2^2*3*5*7*11, unresolvable by the whole 5-pool). YET every
   sibling-pair cross-transfer is NEAR-INTACT (worst leak 0.625%, most exactly 0).
   For the clean families (feature, compositional, lemma B=29) siblings grow the
   IDENTICAL set and every unique-need difference's sole resolver sits in it -- leak
   0. The two tiny leaks are NOT grammatical: lemma B=30's single leak is the cov-0
   difference 4620 (pool exhaustion -- both siblings grew [2,3,5,7,11] and neither
   can resolve a multiple of 2310), and fusional's two-difference leak (210, 420) is
   a WEAK skip-and-demand -- one sibling grew [2,3,5,7] (skipping 11) while the other
   demands 11 for those composite LEXEME-magnitude differences. Both are boundary-
   scale, driven by ENCODING magnitudes, not grammatical structure. This SHARPENS the
   flip condition of explore_collision_growth.py: a unique-need difference's mere
   presence does NOT dissolve the wall -- dissolution needs unique-need AND a sibling
   that SKIPS its sole resolver, and the GAP SIZE is the count of differences uniquely
   needing that skipped prime. Natural grammar concentrates only a handful there
   (local, redundantly-covered distinctions), so the gap stays boundary-scale and the
   wall SURVIVES; a destination-scale gap needs many distinctions on one skipped prime
   -- a designed encoder (S5). [PR3 as-stated -- "min cov >= 2" -- REFUTED; the KILL
   it predicted HOLDS by the sharper mechanism.]

4. THE DOOR OPENS ONLY UNDER A DESIGNED ENCODER (observation; S5). Fusional natural
   offsets (small) yield 1 unique-need difference; SPREAD offsets hand-pushed to
   primorial scale ([0,210,420],...) yield 17 -- the offset combinations 210, 330,
   462, 770 ARE unique-need by construction. The crisp gap: a designed transform
   t = 770 (= 2*5*7*11) makes its demanding stream grow [3], while a 3-sublattice
   sibling grows [2, 5, 7] (skips 3) and leaves t = 770 unresolved (gap 1) -- the
   engine's own SURVIVE-shape, reachable only by DESIGNING the transform to BE
   unique-need. That is a hand-built encoder re-importing the structure it was meant
   to reveal.

THE VERDICT. Under the natural place-value encoding, LANGUAGE-shaped structure is
NOT unique-need: the collision-grown substrate tracks the ENCODING (the base's
factorization for surface concatenation; the offset scale for paradigms), never the
grammar, and natural grammar streams transfer near-intact -- THE WALL SURVIVES at
DESTINATION scale. It is not perfectly intact: fusional morphology shows a hairline
(0.625%) genuine skip-and-demand from lexeme-magnitude coincidence -- the dissolving
mechanism firing WEAKLY on natural data -- but no natural family reaches destination
scale. The substrate door does not natively open for language; it opens only for a
designed encoder whose transforms are chosen to be unique-need, which re-imports the
very structure the growth was meant to discover. Combined with
explore_collision_growth.py (generic + sublattice data grow a stream-independent
prefix), the two converge: collision-driven growth is a stream-independent counter up
to BOUNDARY scale for natural data; destination-scale stream-dependence needs a data
family engineered to concentrate many distinctions on one skipped prime. Honest limit: hand-designed, toy scope,
the 5-prime pool (where the door is EASIEST -- larger pools only raise the
unique-need scale), and these encodings and grammar families; the feature-base law
and the compositional-collapse identity are rules (mechanism-proved), the
regime verdict is an observation at scope.

RUN RECORD (python explore_grammar_growth.py, ~1 s, trivial memory):
  S0 controls: 3000 resolve==product==CRT-tuple; {1,2}->[2,3]; 770->[3]; enc([1,2])=12
  S1 feature:  B=30 -> [2,3,5] (base factors), B=29 -> [2,3,5,7,11]; siblings cross 0;
     no feature diff = 0 mod B; matched generic -> [2,3,5,7,11]
  S2 comp:     same-lexeme demand [1,2,3,4] = offset-diffs; |D| 431 < control 644;
     both grow [2,3,5,7,11]
  S3 crux:     unique-need (cov-1) in all 5 families, min cov 0-1; worst
     sibling leak 0.625% (fusional 210,420 need 11, a weak skip-and-demand), lemma
     B=30 leak 1 = cov-0 4620 (pool exhaustion), the other three exactly 0
  S4 transplant: 140/140 same-suffix diffs divisible by 30; 0 leak into feature D
  S5 door:     spread offsets 17 unique-need vs natural 1; designed t=770 -> [3],
     3-sublattice sibling -> [2,5,7] skips 3, gap 1
  TOTAL 3023 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run (git history). PR2 (compositional
collapse) and PR4 (base = task-invisible sublattice) landed as predicted. PR5's
HEADLINE (the door opens only under a designed encoder) landed, but its incidental
"min cov >= 2 for natural offsets" clause fell with PR3's (fusional-nat has one cov-1
difference); the door-only-by-design conclusion held via the gap-size mechanism below,
not via absence of unique-need. PR1 was REFINED: the feature task does not
grow the generic prefix but the BASE's prime factors -- indistinguishable from
generic only when the base is prime; the wall-survival half held. PR3 as literally
stated ("min cov >= 2, no unique-need difference") was REFUTED -- natural grammar DOES
carry unique-need (cov-1, even cov-0) differences -- but the KILL it was defending
(the wall survives) held by a SHARPER mechanism the run surfaced: the operative
distinction is SKIP-AND-DEMAND, not mere presence -- dissolution needs a sibling to
skip a prime another demands, and its GAP SIZE is how many differences uniquely need
that prime. Natural grammar produces only boundary-scale skips (fusional's weak 210/
420-need-11 from lexeme magnitudes; lemma's pool-unresolvable cov-0), never the
destination-scale concentration a designed encoder gives. The deep reading was
half-right: language is not "anti-unique-need" (it has cov-1 differences), but its
unique-needs are redundantly covered or magnitude-incidental, so no destination gap.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import prod
from itertools import combinations

from explore_collision_growth import (
    grow_least_new, unresolved_diffs, resolves, POOL, diffs_of,
)

CHECKS = 0
POOL5 = POOL[:5]  # [2, 3, 5, 7, 11] -- the door is easiest here


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------- the metric

def cov(d, pool=POOL5):
    """Coverage multiplicity: how many pool primes RESOLVE d (do not divide it)."""
    return sum(1 for p in pool if d % p != 0)


def min_cov(D, pool=POOL5):
    return min((cov(d, pool) for d in D), default=None)


def unique_need(D, pool=POOL5):
    """The cov-1 differences: divisible by every pool prime but one."""
    return [d for d in D if cov(d, pool) == 1]


# --------------------------------------------------------- encodings

def enc(digits, B):
    """Place-value, leftmost digit HIGH-order: enc([1,2], 10) = 12."""
    v = 0
    for d in digits:
        v = v * B + d
    return v


def random_string(rng, length, B):
    return [rng.randrange(B) for _ in range(length)]


def concat_forms(rng, n_stems, n_suf, B, len_stem=2, len_suf=1):
    """form = stem . suffix, stem high-order. Returns {(stem_i, suf_j): value}."""
    stems = [random_string(rng, len_stem, B) for _ in range(n_stems)]
    sufs = [random_string(rng, len_suf, B) for _ in range(n_suf)]
    # distinct stems / suffixes so labels are well defined
    stems = [list(s) for s in {tuple(s) for s in stems}]
    sufs = [list(s) for s in {tuple(s) for s in sufs}]
    forms = {}
    for i, st in enumerate(stems):
        for j, sf in enumerate(sufs):
            forms[(i, j)] = enc(st, B) * B ** len_suf + enc(sf, B)
    return forms, len(stems), len(sufs)


def labeling_from(forms, key):
    """{value: label} where label = key(stem_idx, suf_idx). Distinct values only."""
    lab = {}
    for (i, j), v in forms.items():
        lab[v] = key(i, j)
    return lab


def paradigm_forms(rng, n_lex, offsets, lex_max=1000):
    """Compositional: form = x_i + t_c. Returns {(lex_i, cell_c): value}."""
    lex = rng.sample(range(lex_max), n_lex)
    return {(i, c): x + offsets[c] for i, x in enumerate(lex) for c in range(len(offsets))}


def noncompositional_forms(rng, n_lex, n_cell, val_max):
    """Control: each (lexeme, cell) an independent random form."""
    vals = rng.sample(range(val_max), n_lex * n_cell)
    out, k = {}, 0
    for i in range(n_lex):
        for c in range(n_cell):
            out[(i, c)] = vals[k]
            k += 1
    return out


def fusional_forms(rng, n_base, feat_vals, offsets, base_max=500):
    """form = base + sum_f o[f][v_f]; cell = the value bundle. feat_vals = [V0,V1,..]."""
    bases = rng.sample(range(base_max), n_base)
    cells = list(_product_ranges(feat_vals))
    out = {}
    for bi, b in enumerate(bases):
        for cell in cells:
            v = b + sum(offsets[f][val] for f, val in enumerate(cell))
            out[(bi, cell)] = v
    return out, cells


def _product_ranges(sizes):
    if not sizes:
        yield ()
        return
    for head in range(sizes[0]):
        for tail in _product_ranges(sizes[1:]):
            yield (head,) + tail


def diffs_of_cells(forms, cell_of):
    """Difference set for the partition value -> cell_of(key). Must-separate =
    different cell. A zero difference is an ENCODING COLLISION (two must-separate
    forms landing on the same integer -- a non-injective encoding, unresolvable by
    ANY substrate); it is not a substrate-resolution demand and is excluded."""
    items = [(v, cell_of(k)) for k, v in forms.items()]
    D = set()
    for (va, ca), (vb, cb) in combinations(items, 2):
        if ca != cb and va != vb:
            D.add(abs(va - vb))
    return D


def same_lexeme_diffs(forms):
    """Cross-cell differences within a single lexeme (the compositional demand)."""
    by_lex = {}
    for (i, c), v in forms.items():
        by_lex.setdefault(i, []).append(v)
    D = set()
    for vs in by_lex.values():
        for a, b in combinations(vs, 2):
            if a != b:
                D.add(abs(a - b))
    return D


# ---------------------------------------------------------- S0 controls

def s0_controls():
    print("S0: positive controls")
    rng = random.Random(20250718)
    for _ in range(3000):
        k = rng.randrange(1, 5)
        S = rng.sample(POOL5, k)
        x, y = rng.randrange(3000), rng.randrange(3000)
        pf = (x - y) % prod(S) != 0
        tf = any(x % p != y % p for p in S)
        check(resolves(S, x, y) == pf and resolves(S, x, y) == tf, "engine control")
    print("  imported resolve() == product == CRT-tuple (3000 samples)")
    S = grow_least_new({1, 2}, POOL5)
    check(S == [2, 3], f"hand paradigm demand grew {S}, expected [2,3]")
    print(f"  hand paradigm same-lexeme demand {{1,2}} -> grew {S}")
    S = grow_least_new({770}, POOL5)
    check(S == [3], f"unique-need 770 grew {S}, expected [3]")
    check(cov(770) == 1, "770 is not cov-1")
    print(f"  unique-need 770 -> grew {S} (cov {cov(770)}): the door CAN open")
    check(enc([1, 2], 10) == 12, "encoding index convention")
    print("  encoding: enc([1,2], B=10) = 12 (stem high-order)")


# ------------------------------------------------ the wall observable

# NEAR-INTACT echoes the engine's wall-survival standard (explore_collision_growth.py
# S3 saw 1-of-209 and 0-of-125 cross-residuals on merely-sublattice transfer): only a
# tiny FRACTION of the sibling's differences leak. Every leak is a multiple of prod(S)
# by definition (unresolved iff prod(S) | d), of two harmless kinds -- a cov-0
# difference (unresolvable by the whole pool -- pool exhaustion) or a WEAK skip-and-
# demand (a few differences uniquely needing a prime the sibling happened not to grow).
# A DESTINATION-scale gap needs MANY differences on one skipped prime -- a designed
# encoder (the t=770 door, S5). The 2% bar is this script's operationalization.
NEAR_INTACT = 0.02  # <= 2% leak = near-intact = the wall survives


def sole_resolvers(D, pool=POOL5):
    """Histogram of the sole resolver of each unique-need (cov-1) difference."""
    hist = {}
    for d in unique_need(D, pool):
        p = next(q for q in pool if d % q != 0)
        hist[p] = hist.get(p, 0) + 1
    return hist


# ------------------------------------------ S1: the feature substrate = the base

def s1_feature():
    print("\nS1: the FEATURE substrate tracks the BASE, not the grammar (PR1/PR4)")
    for B in (30, 29):
        rng = random.Random(11)
        fA, ns, nf = concat_forms(rng, 10, 5, B)
        DA = diffs_of(labeling_from(fA, lambda i, j: j))     # label = suffix
        SA = grow_least_new(DA, POOL5)
        fB, _, _ = concat_forms(rng, 10, 5, B)
        DB = diffs_of(labeling_from(fB, lambda i, j: j))
        SB = grow_least_new(DB, POOL5)
        cross = len(unresolved_diffs(SA, DB))
        no_mult = not any(d % B == 0 for d in DA)   # single-digit suffix mechanism
        kind = "primorial" if B == 30 else "prime"
        print(f"  B={B:2d} ({kind:9s}): A->{SA}, B->{SB}, cross A->B {cross}; "
              f"min cov {min_cov(DA)}; no diff = 0 mod B: {no_mult}")
        if B == 30:
            check(set(SA) <= {2, 3, 5} and set(SB) <= {2, 3, 5},
                  "feature/B=30 grew beyond the base primes")
            check(no_mult, "a feature diff was 0 mod B (multi-digit suffix?)")
            check(cross == 0, "same-base feature streams do not transfer")
        else:
            check(any(p > 5 for p in SA), "prime base did not grow past the base primes")
    rng = random.Random(99)
    gen = grow_least_new(diffs_of({x: rng.randrange(5) for x in range(30000)}), POOL5)
    print(f"  matched generic (5 classes over 0..29999) -> {gen}")
    check(set(gen) > {2, 3, 5}, "generic did not exceed the base primes")
    print("  => the feature substrate = the primes DIVIDING THE BASE (B=30 -> {2,3,5});")
    print("     the ENCODING sets the content, the grammar does not")


# ---------------------------------------- S2: the compositional collapse

def s2_compositional():
    print("\nS2: compositional collapse -- difference-set compression (PR2)")
    rng = random.Random(23)
    offsets = [0, 1, 2, 3, 4]                    # natural small transforms
    comp = paradigm_forms(rng, 12, offsets)
    D_comp = diffs_of_cells(comp, lambda k: k[1])
    D_same = same_lexeme_diffs(comp)
    ctrl = noncompositional_forms(rng, 12, len(offsets), val_max=max(comp.values()) + 1)
    D_ctrl = diffs_of_cells(ctrl, lambda k: k[1])
    S_comp = grow_least_new(D_comp, POOL5)
    S_ctrl = grow_least_new(D_ctrl, POOL5)
    off_diffs = {abs(a - b) for a, b in combinations(offsets, 2)}
    print(f"  compositional: |D| {len(D_comp)}, same-lexeme demand {sorted(D_same)}")
    print(f"    offset-differences {sorted(off_diffs)} -- same-lexeme demand matches")
    print(f"  control (non-compositional): |D| {len(D_ctrl)}")
    print(f"  grown: compositional {S_comp}, control {S_ctrl}; "
          f"min cov comp {min_cov(D_comp)}")
    check(D_same == off_diffs, "same-lexeme demand != offset-differences")
    check(len(D_comp) < len(D_ctrl), "compositional D not smaller than control")
    check(set(S_comp) > {2, 3, 5}, "compositional did not grow a generic prefix")
    print("  => compositionality is VISIBLE as compression, but the grown set is still")
    print("     a generic prefix -- compression != unique-need")


# ------------------------------------------- S3: the crux -- wall survives

def s3_crux():
    print("\nS3: the crux -- unique-need PRESENT, the wall SURVIVES (PR3)")
    rng = random.Random(7)

    def sibling_pair(build):
        DA, DB = build(), build()
        SA, SB = grow_least_new(DA, POOL5), grow_least_new(DB, POOL5)
        resid = max(len(unresolved_diffs(SA, DB)), len(unresolved_diffs(SB, DA)))
        frac = resid / max(len(DA), len(DB), 1)
        return DA, SA, resid, frac

    families = {
        "feature B=30": lambda: diffs_of(labeling_from(
            concat_forms(rng, 10, 5, 30)[0], lambda i, j: j)),
        "lemma B=30": lambda: diffs_of(labeling_from(
            concat_forms(rng, 10, 5, 30)[0], lambda i, j: i)),
        "lemma B=29": lambda: diffs_of(labeling_from(
            concat_forms(rng, 10, 5, 29)[0], lambda i, j: i)),
        "compositional": lambda: diffs_of_cells(
            paradigm_forms(rng, 12, [0, 1, 2, 3, 4]), lambda k: k[1]),
        "fusional-nat": lambda: diffs_of_cells(fusional_forms(
            rng, 6, [3, 3, 3],
            [[rng.randrange(9) for _ in range(3)] for _ in range(3)])[0],
            lambda k: k[1]),
    }
    saw_unique_need, worst_frac = False, 0.0
    for name, build in families.items():
        DA, SA, resid, frac = sibling_pair(build)
        mc, un = min_cov(DA), len(unique_need(DA))
        saw_unique_need = saw_unique_need or mc <= 1
        worst_frac = max(worst_frac, frac)
        print(f"  {name:14s}: grew {str(SA):18s} min cov {mc}  unique-need {un:2d}"
              f"  sole-resolvers {sole_resolvers(DA)}  sibling leak {resid} ({frac:.3%})")
        check(frac <= NEAR_INTACT, f"{name} sibling transfer was not near-intact")
    print(f"  -> unique-need (cov-1) diffs in every family, min cov 0-1, yet every sibling")
    print(f"     cross-transfer is near-intact (worst leak {worst_frac:.3%}): the leaks are")
    print(f"     pool-unresolvable cov-0 diffs (lemma B=30: 4620) or a WEAK skip-and-demand")
    print(f"     from lexeme-magnitude coincidence (fusional: 210,420 need 11, one sibling")
    print(f"     skips it) -- boundary-scale, encoding-driven, not grammatical. The flip")
    print(f"     condition sharpened (unique-need AND a sibling that SKIPS the sole")
    print(f"     resolver), the GAP SIZE = how many diffs uniquely need the skipped prime:")
    print(f"     handful for natural grammar, many only under a DESIGNED encoder (S5).")
    print(f"     The wall SURVIVES for natural grammar.")
    check(saw_unique_need, "no family carried a unique-need difference")


# ------------------------------------------------ S4: base = sublattice

def s4_transplant():
    print("\nS4: composite base = sublattice transplant, task-invisible (PR4)")
    rng = random.Random(5)
    forms, ns, nf = concat_forms(rng, 8, 5, 30, len_stem=2, len_suf=1)
    # same-suffix, different-stem pairs: differences are multiples of B^len_suf
    same_suf = []
    for j in range(nf):
        col = [v for (i, jj), v in forms.items() if jj == j]
        for a, b in combinations(col, 2):
            same_suf.append(abs(a - b))
    div = all(d % 30 == 0 for d in same_suf)
    print(f"  same-suffix diffs all divisible by B=30: {div} "
          f"({len(same_suf)} pairs) -- a sublattice mod {{2,3,5}}")
    check(div, "same-suffix diffs not a B-sublattice")
    # but for the FEATURE task those pairs share the label -> not must-separate
    DF = diffs_of(labeling_from(forms, lambda i, j: j))
    leaks = [d for d in same_suf if d in DF]
    print(f"  of those, in the feature-task D: {len(leaks)} -- they drop out")
    check(not leaks, "same-suffix sublattice leaked into feature D")
    print("  => composite-base structure is the U_q sublattice recreated, task-invisible")


# ------------------------------------------------- S5: the SURVIVE shot

def s5_survive_shot():
    print("\nS5: the door opens ONLY under a DESIGNED encoder (PR5)")
    rng = random.Random(3)
    # (a) natural fusional -- redundantly coverable
    off_nat = [[rng.randrange(9) for _ in range(3)] for _ in range(3)]
    Dn = diffs_of_cells(fusional_forms(rng, 8, [3, 3, 3], off_nat)[0], lambda k: k[1])
    # spread offsets: hand-pushed to primorial scale -> a designed encoder
    off_spread = [[0, 210, 420], [0, 330, 660], [0, 462, 924]]
    Ds = diffs_of_cells(
        fusional_forms(rng, 8, [3, 3, 3], off_spread, base_max=50)[0], lambda k: k[1])
    print(f"  fusional natural offsets: unique-need {len(unique_need(Dn))}, "
          f"min cov {min_cov(Dn)}")
    print(f"  fusional spread offsets:  unique-need {len(unique_need(Ds))}, "
          f"min cov {min_cov(Ds)}  (offset combos ARE unique-need)")
    check(len(unique_need(Dn)) <= 1 and len(unique_need(Ds)) > len(unique_need(Dn)),
          "spread offsets did not manufacture more unique-need than natural")
    # (b) the crisp gap: a designed transform t=770 IS the engine's unique-need
    designed = {(i, 0): 3 * i for i in range(6)}
    designed.update({(i, 1): 3 * i + 770 for i in range(6)})   # transform t = 770
    Dd = same_lexeme_diffs(designed)
    Sd = grow_least_new(Dd, POOL5)
    check(Sd == [3], f"designed t=770 paradigm grew {Sd}, expected [3]")
    # a 3-sublattice sibling never demands 3 and cannot resolve t=770
    sib = {(i, c): 3 * i + 3 * c for i in range(8) for c in range(6)}
    Ssib = grow_least_new(diffs_of_cells(sib, lambda k: k[1]), POOL5)
    gap = len(unresolved_diffs(Ssib, {770}))
    print(f"  designed transform t=770: demanding stream grows {Sd}; a 3-sublattice")
    print(f"    sibling grows {Ssib} (skips 3) and leaves t=770 unresolved: gap {gap}")
    check(3 not in Ssib and gap == 1, "the designed door did not open")
    print("  => SURVIVE-shape reachable ONLY by DESIGNING the transform to BE unique-need")
    print("     -- a hand-built encoder re-importing the structure it was meant to reveal")


if __name__ == "__main__":
    s0_controls()
    s1_feature()
    s2_compositional()
    s3_crux()
    s4_transplant()
    s5_survive_shot()
    print(f"\nALL SECTIONS PASS -- {CHECKS} checks, exit 0")
