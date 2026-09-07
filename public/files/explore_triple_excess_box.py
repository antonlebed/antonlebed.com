r"""THE h = 2 EXCESS BY BOX -- is the all-principal excess at class number
2 a term of the FAMILY (the count of fields by discriminant, falling with
the box) or a fact of the FIELD (flat in the box)? (child of
explore_triple_ramified_term.py, whose F2 left the h = 2 level at 1.099
+- 0.016 with every prime-power term in; sibling of
explore_family_term.py, which found the split share's deficit to be the
cubic count's secondary term and reached no class-level quantity.)

THE QUESTION. Over the complex cubic fields with class number 2, the
totally split primes q < 1000 whose three places are all principal,
with the unramified and ramified prime powers landed by the explicit
formula, sit at 1.099 +- 0.016 of the uniform share 1/4 (z = +6.0) to
|d| <= 24000; 1.065 +- 0.038 over |d| <= 6000 and 1.107 +- 0.018 over
6000 < |d| <= 24000. The split share's own deficit at a small prime is
a family term: the count of cubic fields by discriminant has a second
term of relative size X^(-1/6) whose local densities per splitting type
differ from the main term's. That term lowers the split count of every
class alike and cannot move a level that compares the identity against
the split count itself. But the all-principal event at h = 2 is itself
a local condition on a field: the Galois closure of the Hilbert class
field over Q has group (Z/2)^2 x| S_3 = S_4, the event "p totally split
in K with all three places principal" is "Frob_p = e in S_4" against
"Frob_p in the Klein four-group", and the fixed field of an S_3 is the
S_4 quartic field E with cubic resolvent K and d_E = d_K (Heilbronn:
these quartics are the 2-torsion of Cl(K)). So the level is a share
across the FAMILY of quartic fields E ordered by discriminant, and a
secondary term of THAT count with its own local densities would move
it. The one model-free separation: a family term falls with the
discriminant box; a per-field fact does not. This file reads the h = 2
level per box to |d| <= 96000, four times the parents' population.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE FAMILY SHAPE. A second term of relative order X^(-1/6),
      integrated over a box (X1, X2], carries the factor
          g = (X2^(5/6) - X1^(5/6)) / (X2 - X1)
      against the main term's 1: g = 0.2633, 0.2059, 0.1834, 0.1634,
      0.1456, 0.1297 over the six boxes (0, 3000], (3000, 6000], (6000,
      12000], (12000, 24000], (24000, 48000], (48000, 96000]; 0.2346
      over the parents' box (0, 6000] and 0.1350 over (24000, 96000],
      ratio 1.738 (the midpoint approximation (60000/3000)^(1/6) gives
      1.6). A family term with the cubic count's
      exponent scales the excess level - 1 by g; a per-field fact
      leaves it constant. The exponent 1/6 is the CUBIC count's (T1);
      the fit below leaves the exponent free as well.

  (2) WHAT THE TWO READINGS PREDICT AT THE TOP. Excess E = level - 1.
      Family, fitted to the wide value 0.099 at g = 0.1794 (the
      (0, 24000] box): E = 0.075 over (24000, 96000]. Field: E = 0.099.
      The top box holds about 12,500 complex fields (the enumeration to
      96000 rehearsed for the sibling), 16 % of them at h = 2 by a
      fifty-field sample, so some 2,000 fields against the parents'
      484: the bar on the level falls from 0.016 to about 0.008, and
      the two readings sit 3 sigma apart on it. The prints in hand
      lean the field's way already: the increment (6000, 24000] read
      ABOVE the parents' box, 0.107 against 0.065, where a family term
      predicts 0.065 x 0.1701/0.2346 = 0.047.

  (3) THE STATISTIC. Level = (n3 + c3 + R_e) / ((ns + cN + R_N) . 1/4)
      per box, the parents' algebra unchanged; sigma Poisson on the
      expectation, so sigma(level) = 1 / sqrt(exp). Two one-parameter
      fits over the six boxes by weighted least squares, FLAT E_b = c
      and DECAY E_b = c g_b, chi-square each on 5 degrees of freedom;
      and the exponent alpha free in E_b = c g_b(alpha), g_b(alpha) =
      (X2^(1-alpha) - X1^(1-alpha)) / ((1 - alpha)(X2 - X1)), scanned
      on a grid over [-1, 0.95] with its 1-sigma range at delta
      chi-square 1. alpha = 0
      is the field, alpha = 1/6 the cubic count's term.

  (4) THE BIN STRUCTURE IS A SECOND READ. The wide excess sits in the
      bins [3, 30) (1.250, where the small ramified and unramified
      powers land) and [300, 1000) (1.126; the frozen text called it
      "the raw count, no powers reach it", wrongly: 19^2 to 31^2, 7^3,
      5^4, 3^6 and 2^9 land there, corrected at the child
      explore_triple_image_level.py), the middle bins near 1. A family term at s = 5/6 is a
      small-p statement -- the cubic one's density ratio is (1 + p^(-1/3))^3
      -- so a family excess is largest in [3, 30) and falls with the
      box there; the [300, 1000) excess is at primes comparable to the
      discriminant, where the sibling's F5 found the cubic family's
      share leaving its two terms both ways. The by-bin x by-box table
      is printed so a kill carries its next question: which bin moves.

  (5) THE POSITIVE CONTROL OF THE BOX STATISTIC. The same fit run on a
      quantity KNOWN to be a family term: the split share's deficit
      1/6 - share at the primes 3 to 31, pooled, over the complex
      fields of each box (every field, no class map). DECAY must beat
      FLAT there and the deficit pooled over the boxes must sit within
      2 sigma of the two-term table (explore_family_term.py (3)), or
      the fit reads nothing. What the control's free exponent reads is
      the CALIBRATION of the fit: the term is 30 % of the main term in
      the first box, so its deficit falls faster than g and the
      effective exponent sits above 1/6.

  (6) THE PRICE. Class reading 0.37 s per field on fifty fields sampled
      from (48000, 96000] (mean; max 1.43 s), about 77 minutes over
      the two new boxes' 12,464 complex fields, plus 12 minutes for
      the four boxes to 24000 and 4 for the enumeration: near 100
      minutes. The run is checkpointed PER BOX -- the six boxes' tables
      land in a directory as they complete and a restart loads them --
      so a kill costs a box; rehearsed at cap 6000. One pathology
      found at the pricing: the topband rig's T7 cross-check of its
      bounded Hermite routine against the shop's original stalls past
      ten minutes on a 524-row relation set at d = -90239 (the
      original's entries swell; the bounded routine answers in under a
      second). The controls spend their budgets on the first two
      boxes, where the topband run spent them; the boxes are read in
      ascending order for that reason.

  (7) WHAT IS NOT CONTROLLED. (a) The exponent of a quartic family term
      is unread; the free-alpha fit is the hedge. (b) The excluded
      fields under the topband rig's T4 policy, printed per box and
      killing the run above 1 % of a box. (c) The remainder below the
      discriminant (the parents' (6b)-(6c)): a per-field oscillation
      whose SIZE depends on the discriminant would itself move with
      the box, at a rate not the count's; the free alpha and the bin
      table are the reads that would show it.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_family_term.py: the exponent 5/6 and the factor g are
    the CUBIC count's (Taniguchi-Thorne, Bhargava-Shankar-Tsimerman);
    the quartic count's secondary term is not read here, and its
    published status is read full-text before anything is claimed on
    a SURVIVE. The widened maximal order (sieve to 20000) is imported.
 T2 FROM explore_triple_ramified_term.py and explore_triple_cube_term.py:
    the per-field reader, the unramified walk, the ramified walk, the
    regime sort and the level's algebra are IMPORTED and not
    re-implemented; C1 reprints their F2 before any box is read.
 T3 FROM explore_ceiling_topband.py: the class reading (read_field with
    its T10/T11 retry and attestation), the T4 exclusion policy and
    the T5-T7 performance swaps are IMPORTED; the reading is run on
    the complex fields only (the level is complex-only, and the real
    fields were a fifth of the topband wall).

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE KILL-SHAPE, printed: the h = 2 excess over (24000,
      96000] against the parents' box excess E_p (recomputed here, C1)
      and against E_p / 1.738. Within 2 sigma of E_p (the two bars
      combined) AND more than 2 sigma above E_p / 1.738 KILLS the
      family reading: the excess is the field's. Below 2 sigma of E_p
      and within 2 sigma of the scaled value SURVIVES it. Neither is
      "open".
  P2  THE SIX-BOX FIT: FLAT beats DECAY by more than 4 in chi-square,
      and the free alpha's 1-sigma range contains 0 and excludes 1/6.
  P3  THE TOP-BOX EXCESS reads between 0.08 and 0.12 with a bar under
      0.010, more than 8 sigma above 0.
  P4  THE BINS: in each of the two new boxes the [3, 30) and [300,
      1000) bins read above 1 by more than 2 sigma and the middle two
      within 2 sigma of 1.
  P5  THE OTHER STRATA: h = 3 M stays within 2 sigma of 1 in the pooled
      new boxes; every readable stratum at h >= 4 in the new boxes
      reads above 1 (the wide print's direction, the wide read's
      second residual).

THE CONTROLS, run before any prediction is read.

  C0  THE COUNT: the complex fields per box against the two-term
      formula (explore_family_term.py C0), within +-40 at every box
      edge.
  C1  REPRODUCTION: boxes 1-2 pooled reprint the ramified rig's
      parents'-box levels with the term in, 1.065 at h = 2 and 0.922 at
      h = 3 M; boxes 1-4 pooled reprint its wide levels 1.099 and
      0.943; all within 0.003.
  C2  THE POSITIVE CONTROL of (5): on the split-share deficit DECAY
      beats FLAT by more than 9 in chi-square, and the deficit pooled
      over every box and prime sits within 2 sigma of the two-term
      prediction; the per-box z is printed. The first draft asserted
      every box within 2 sigma and failed at the rehearsal in (0,
      3000] at z = -2.44 (measured deficit 0.0682 against the table's
      0.0558 pooled over the ten primes): the sibling asserted per
      prime pooled over the boxes, never per box, and the first box is
      where the two-term remainder is largest; the assert was moved to
      the sibling's tested statement and the fit.
  C3  THE RAMIFIED RIG'S OWN CHECKS, per box: every lift relation holds
      (its C3), the type agrees with the valuation (C4), no tame P^3
      prime == 2 mod 3 splits in the resolvent (P5), no power triple
      off zero-sum.
  C4  EXCLUSIONS under 1 % of each box's complex fields (T4).

THE DESIGN. The enumeration to |d| <= 96000 with the sibling's widened
order, reduced at once to coefficient triples per field and
checkpointed; the complex fields sorted by |d| and cut into the six
boxes. Per box, per field: the topband class reading; for h > 1 the
split-triple reader, the unramified walk with the prime 2, the
ramified walk, the regime sort; the cells landed per stratum and bin,
the census and the checks accumulated; per field the splitting type
at 3..31 for C2. Each box's tables written to the checkpoint
directory as JSON when complete; a restart loads finished boxes. Then
the reads: C1 over the pooled boxes, C2 and its fit, the h = 2 level
by box with both terms, by bin x box, the same level split by term
(unramified only; the ramified weights' landing against what the
algebra forces at h = 2), the fixed window's value under independent
uniform Frobenius, the three fits, P1-P5; after those printed, S5b,
the level with each term at its own image's share. Flags:
`--cap N` (a rehearsal cap; boxes above it dropped), `--ckpt DIR`
(default: a directory beside the system temp), `--fresh` (ignore
checkpoints). Estimate: 100 minutes, peak 350 MB at the enumeration
(the sibling's measured envelope), the reading under 200 MB.

FINDINGS. One population, 16313 complex fields to |d| <= 96000 in six
boxes (419, 469, 960, 2001, 4126, 8338 fields), 6442 of them with
h > 1 and 2202 at h = 2 (39, 54, 122, 264, 531, 1192 per box); three
fields excluded (d = -41860, -86359, -95615), the three the reading
to 24000 excluded now read, the wider box supplying representatives.
C0 held at every edge (-2.9, +0.2, -6.2, +0.6, +28.8, -23.7). C1
reprinted the ramified rig's four levels to the digit: 1.065 and 0.922
on the parents' box, 1.099 and 0.943 to 24000. C2: the deficit pooled
over boxes and primes sits at z = -0.70 against the two terms, DECAY
beats FLAT by 78 (chi-square 18.5 against 97.0), and the free exponent
reads 0.260 [0.240, 0.275] -- the calibration of (5). C3: 16269 lift
relations hold, 13364 types agree, 2302 tame P^3 primes clean, no map
disagreement. C4: 3 of 16313.

  F1. THE EXCESS DOES NOT MOVE WITH THE BOX, AND NEITHER FROZEN SHAPE
      FIRES (observation; P1 neither, P2 fails, P3 fails on its bounds,
      P4 and P5 hold). The h = 2 level with both terms in, by box:
      1.060 (z +1.04), 1.069 (+1.39), 1.084 (+2.54), 1.117 (+5.27),
      1.058 (+3.75), 1.066 (+6.37). The top box's excess 0.0634 +-
      0.0086 sits 0.05 sigma below the parents' box's 0.0654 +- 0.0378
      and 1.10 sigma above the family-scaled 0.0376 +- 0.0217: the
      parents' bar is too wide for the frozen kill. The six-box fits:
      FLAT chi-square 5.4, DECAY 5.3, the free exponent 0.090 [-0.015,
      0.180], and at the control's calibrated 0.26 chi-square 8.6, 3.2
      above FLAT (1.8 sigma). P3 failed because the excess is smaller
      than the wide value, not larger: the 1.099 to 24000 was carried
      by the box (12000, 24000] at 1.117.

  F2. THE BINS MOVE IN OPPOSITE DIRECTIONS (observation; P4 holds in
      both new boxes). [3, 30): 0.901, 1.098, 1.199, 1.349, 1.407,
      1.478 (z +13.9 in the top box), RISING with the box; [300,
      1000): 1.097, 0.998, 1.093, 1.171, 1.064, 1.030, falling from the
      fourth box; the middle bins 0.82 to 0.99. The new boxes pooled:
      1.456 (+15.9), 0.973, 1.005, 1.040 (+3.6). No single family
      term moves two bins in opposite directions.

  F3. THE EXCESS IS THE FORCED LANDINGS COUNTED AT THE UNIFORM SHARE;
      AT THEIR OWN IMAGE'S SHARE THE LEVEL IS SHORT, AND FLAT IN THE
      BOX (observation; the split by term frozen before the run, the
      image read post-hoc after F1-F2 printed; the forcing a property).
      Split by term: the unramified level alone reads 1.025, 1.034,
      1.045, 1.074, 1.008, 1.009 by box -- 1.058 +- 0.017 to 24000 and
      1.009 +- 0.009 above it -- while the ramified weights, 0.9 to 1.3
      per field and rising with the box, are predicted by the algebra
      (P^3 whole, P^2 Q at 1/2) to add +0.032 to +0.045 of level in
      every box against the uniform quarter, and land on e at 1.00 to
      1.15 of that prediction, above it because a P^2 Q pair's EVEN
      powers are forced onto e as well (2[P] = 0) and the prediction
      takes them at 1/2; S5b takes them at 1/2 too, so its image level
      is an upper bound by that much. Above 24000 the excess is the
      ramified term's alone. Under independent
      uniform Frobenius at every prime power the window q^k < 1000
      would put the unramified level at 1.282 (by bin 1.889, 1.417,
      1.279, 1.168); the explicit formula's compensation by the raw
      primes brings it to 1.01. At h = 2 the forced weights -- split squares, inert
      cubes, totally ramified places, the Q of every P^2 Q pair -- are
      0.062, 0.070, 0.072, 0.071, 0.075, 0.075 of the N weight per box
      and predict an excess of +0.13 to +0.15 on their own. With each
      term at its image's share (forced at 1, the P^2 Q pair at 1/2,
      the rest at 1/4) the level reads 0.936, 0.927, 0.940, 0.971,
      0.920, 0.927; pooled 0.931 (z -9.7), 0.955 to 24000 and 0.925
      above. By bin, pooled: the image level in [3, 30) climbs 0.61,
      0.71, 0.77, 0.85, 0.88, 0.92 with the box, [30, 100) and [100,
      300) sit 0.72 to 0.88, [300, 1000) 0.93 to 1.08. The rise of
      [3, 30) under the uniform read is the ramified count: P^2 Q pairs
      per h = 2 field 1.49, 1.63, 1.78, 1.85, 2.10, 2.17 across the
      boxes. The free place P of a P^2 Q pair is principal in 0.500,
      0.477, 0.461, 0.481, 0.424, 0.480 of pairs against the 1/2 taken.

  F4. THE OTHER STRATA IN THE NEW BOXES (observation; P5 holds). h = 3
      M 1.009 (z +0.59), h = 3 D 0.952 (-2.86); every readable stratum
      at h >= 4 above 1 and RISING with h: 1.312, 1.452, 1.385 (6 M),
      1.763, 1.829, 2.173 (9 M), 2.283, 2.164, 2.366 (12 M) at h = 4,
      5, 6, 7, 8, 9, 10, 11, 12. The UNRAMIFIED level alone -- the
      statistic the cube-term rig read flat across seven strata to
      24000 within bars of 0.07 to 0.31 -- rises the same way on the
      new boxes: 1.194, 1.284, 1.216, 1.598, 1.602, 1.883, 2.122, 2.238,
      2.128 (z +5.6, +5.4, +3.1, +5.7, +4.2, +6.7, +4.8, +4.6, +3.9),
      so the flatness was the bars', not the level's. An inert prime's cube lands on e at
      every h and a totally ramified place is principal at every h
      prime to 3, each counted against 1/h^2, so the forcing's excess
      grows as h^2 -- the shape of the rise. The image-share read at
      those strata needs every term's N weight by source and power,
      which this file's cells do not keep.

RUN RECORD. 2026-09-06, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_triple_excess_box.py`
with `--ckpt` naming a scratch directory. One process, CPython, no
BLAS. 42 checks; 6321 s wall over the six boxes (172, 95, 245, 636,
1563, 3362 s; the enumeration 248 s of it, 16313 fields kept from
474030 polynomials), peak working set 362.0 MB at the enumeration
against memwatch's 512 MB ceiling; the reading 0.35 s a field in the
top box. The read stage was rerun from the checkpoints twice, 0.3 s
each: once after the free-exponent grid crashed at alpha >= 1 (the
first box's edge 0 to a negative power; the rehearsal's two boxes
never reached the fit), once with S5b added after S5's print had been
read. Rehearsed at cap 6000 first (134 s, 34 MB, C1 reprinting the
parents' box, the checkpoint round trip exercised by a second
invocation); priced on fifty fields sampled from (48000, 96000] (18.5
s, mean 0.37 s, max 1.43 s) after a first sample stalled at d = -90239
inside the imported Hermite cross-check.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import json
import math
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_topband as TB          # T3: patches at import
import explore_cubic_field_shop as CFS
import explore_cubic_principal as ECP
import explore_cubic_split_triple as ST
import explore_triple_cube_term as CT
import explore_triple_ramified_term as RT

_ARGV = sys.argv
sys.argv = _ARGV[:1]                          # the sibling parses argv[1]
import explore_family_term as FT               # noqa: E402  (T1)
sys.argv = _ARGV

ECP.maximal_order3 = FT.maximal_order3_wide   # T1: the declared swap


def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


CAP = int(_flag("--cap", 96000))
CKPT = _flag("--ckpt", os.path.join(tempfile.gettempdir(),
                                    "excess_box_%d" % CAP))
FRESH = "--fresh" in sys.argv
ALL_BOXES = ((0, 3000), (3000, 6000), (6000, 12000), (12000, 24000),
             (24000, 48000), (48000, 96000))
BOXES = tuple(b for b in ALL_BOXES if b[1] <= CAP)
READ_PRIMES = FT.READ_PRIMES                  # 3..31, C2
BIN_EDGES = ECP.BIN_EDGES
MIN_READ = CT.MIN_READ
MIN_SPLIT = ST.MIN_SPLIT
HIGH_FRAC = ST.HIGH_FRAC
UNRESOLVED_KILL = TB.UNRESOLVED_KILL
REPRO = {"parents": {(2, 'A'): 1.065, (3, 'M'): 0.922},
         "wide": {(2, 'A'): 1.099, (3, 'M'): 0.943}}    # C1
REPRO_TOL = 0.003
CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)
    sys.stdout.flush()


# ----------------------------------------------------------- (1) the shape
def g_box(lo, hi, alpha=1.0 / 6):
    """The box average of X^(-alpha): (X2^(1-a) - X1^(1-a)) /
    ((1 - a)(X2 - X1))."""
    if abs(alpha) < 1e-12:
        return 1.0
    e = 1.0 - alpha
    if abs(e) < 1e-12:
        return (math.log(hi) - math.log(max(lo, 1))) / (hi - lo)
    return (hi ** e - lo ** e) / (e * (hi - lo))


def fit_flat(es, ss):
    w = [1.0 / s / s for s in ss]
    c = sum(wi * e for wi, e in zip(w, es)) / sum(w)
    chi = sum(wi * (e - c) ** 2 for wi, e in zip(w, es))
    return c, chi


def fit_decay(es, ss, gs):
    w = [1.0 / s / s for s in ss]
    c = (sum(wi * g * e for wi, g, e in zip(w, gs, es))
         / sum(wi * g * g for wi, g in zip(w, gs)))
    chi = sum(wi * (e - c * g) ** 2 for wi, g, e in zip(w, gs, es))
    return c, chi


def fit_alpha(es, ss, boxes):
    """The exponent scanned on [-1, 0.95] (the box average of X^(-alpha)
    diverges at alpha >= 1 on a box starting at 0): (best alpha, lo, hi,
    chi)."""
    grid = [i / 200.0 for i in range(-200, 191)]
    res = []
    for a in grid:
        gs = [g_box(lo, hi, a) for (lo, hi) in boxes]
        c, chi = fit_decay(es, ss, gs)
        res.append((chi, a))
    best = min(res)
    inside = [a for (chi, a) in res if chi <= best[0] + 1.0]
    return best[1], min(inside), max(inside), best[0]


# ------------------------------------------------------- the population
def s1_population():
    section("S1  THE POPULATION -- Hunter's box to |d| <= %d, complex "
            "fields by box, and the count control C0" % CAP)
    path = os.path.join(CKPT, "fields.json")
    t0 = time.time()
    if os.path.exists(path) and not FRESH:
        fields = json.load(open(path))
        print("  %d complex fields loaded from %s" % (len(fields), path))
    else:
        fl, b = ECP.enumerate_fields(CAP)
        fields = [(d, [(a, bb, c) for (a, bb, c, O) in polys])
                  for (ad, d, cx, polys) in fl if cx]
        n_all = len(fl)
        del fl
        gc.collect()
        print("  %d polynomials -> %d fields, %d complex, %.1f s"
              % (b[0], n_all, len(fields), time.time() - t0))
        if not os.path.isdir(CKPT):
            os.makedirs(CKPT)
        json.dump(fields, open(path, "w"))
    fields.sort(key=lambda t: -t[0])
    for (lo, hi) in BOXES:
        n = sum(1 for (d, _p) in fields if lo < -d <= hi)
        cum = sum(1 for (d, _p) in fields if -d <= hi)
        two = (3.0 * FT.A_CONST * hi
               + math.sqrt(3.0) * FT.B_CONST * hi ** (5.0 / 6))
        print("  (%5d, %5d]  %5d complex fields  cumulative %5d  two "
              "terms %8.1f  diff %+6.1f  g = %.4f"
              % (lo, hi, n, cum, two, cum - two, g_box(lo, hi)))
        ok(abs(cum - two) <= 40, "complex count off the two terms by "
           "%.1f at X = %d" % (cum - two, hi))
    return fields


# --------------------------------------------------------- the box read
def key_str(key):
    return "%d:%s" % key


def key_of(s):
    h, reg = s.split(":")
    return (int(h), reg)


def read_box(bi, fields):
    """One box: the class reading on every complex field, the three
    walks on every field with h > 1; the tables returned as plain
    dicts, JSON-ready."""
    lo, hi = BOXES[bi]
    sub = [(d, polys) for (d, polys) in fields if lo < -d <= hi]
    t0 = time.time()
    un, ram, census, nfields = {}, {}, {}, {}
    checks = dict(c3_ok=0, c3_bad=0, c4_agree=0, c4_disagree=0,
                  c4map_disagree=0, c5_tame=0, c5_bad=0, bad_sum=0)
    fam = dict((p, [0, 0]) for p in READ_PRIMES)       # p -> [unr, split]
    excluded = []
    tags = {}
    t_read = t_walk = 0.0
    for i, (d, polys) in enumerate(sub):
        if i and i % 500 == 0:
            print("  ... %d/%d fields, %.1f s (reading %.1f, walks %.1f)"
                  % (i, len(sub), time.time() - t0, t_read, t_walk))
            sys.stdout.flush()
        pl = [(a, b, c) + (FT.maximal_order3_wide(a, b, c)[0],)
              for (a, b, c) in polys]
        a, b, c, O = pl[0]
        pdisc = CFS.poly_disc3(a, b, c)
        for p in READ_PRIMES:
            if d % p == 0:
                continue
            _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, p)
            fam[p][0] += 1
            fam[p][1] += (kd == 'split')
        t1 = time.time()
        rec, _retried, tag = TB.read_field(d, True, pl)
        t_read += time.time() - t1
        tags[tag] = tags.get(tag, 0) + 1
        if rec is None:
            excluded.append(d)
            continue
        h = rec[6]
        if h == 1:
            continue
        t1 = time.time()
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            t_walk += time.time() - t1
            continue
        two = CT.place_over_two(rec)
        cells, nb, _small = CT.walk_field(rec, per_prime, piv, k, two)
        checks['bad_sum'] += nb
        ns = sum(x['ns'] for x in cells.values())
        neq = sum(x['neq'] for x in cells.values())
        reg = 'A'
        if H % 3 == 0:
            exact = CT.diagonal_3part(per_prime, piv, k, H)
            if H == 3:
                reg = ('X' if ns < MIN_SPLIT
                       else 'D' if float(neq) / ns >= HIGH_FRAC else 'M')
            else:
                reg = 'X' if ns < MIN_SPLIT else 'D' if exact else 'M'
        key = key_str((H, reg))
        nfields[key] = nfields.get(key, 0) + 1
        rcells = RT.walk_ramified(rec, piv, k,
                                  census.setdefault(key, RT.new_census()),
                                  checks)
        su = un.setdefault(key, {})
        for bb, cell in cells.items():
            CT.merge(su.setdefault(str(bb), CT.new_cell()), cell)
        sr = ram.setdefault(key, {})
        for bb, cell in rcells.items():
            RT.merge_r(sr.setdefault(str(bb), RT.new_rcell()), cell)
        t_walk += time.time() - t1
    wall = time.time() - t0
    print("  box (%d, %d]: %d complex fields, %d with h > 1, %d excluded "
          "%s; tags %s; %.1f s (reading %.1f, walks %.1f)"
          % (lo, hi, len(sub), sum(nfields.values()), len(excluded),
             excluded, sorted(tags.items()), wall, t_read, t_walk))
    ok(len(excluded) <= UNRESOLVED_KILL * max(len(sub), 1),
       "T4 kill: %d of %d excluded" % (len(excluded), len(sub)))
    return dict(un=un, ram=ram, census=census, nfields=nfields,
                checks=checks, fam=fam, excluded=excluded, wall=wall,
                n=len(sub))


def s2_boxes(fields):
    section("S2  THE BOX READS -- class reading and the three walks, "
            "checkpointed per box in %s" % CKPT)
    out = []
    for bi in range(len(BOXES)):
        path = os.path.join(CKPT, "box%d.json" % bi)
        if os.path.exists(path) and not FRESH:
            data = json.load(open(path))
            data['fam'] = dict((int(p), v) for p, v in data['fam'].items())
            print("  box (%d, %d] loaded: %d fields, %d with h > 1, "
                  "%d excluded, %.1f s when run"
                  % (BOXES[bi][0], BOXES[bi][1], data['n'],
                     sum(data['nfields'].values()), len(data['excluded']),
                     data['wall']))
        else:
            data = read_box(bi, fields)
            json.dump(data, open(path, "w"))
        for ck in ('c3_bad', 'c4_disagree', 'c4map_disagree', 'c5_bad',
                   'bad_sum'):
            ok(data['checks'][ck] == 0, "box %d: %s = %d"
               % (bi, ck, data['checks'][ck]))
        print("  [C3] box %d: lift relations %d hold, types %d agree, "
              "tame P^3 %d, all clean"
              % (bi, data['checks']['c3_ok'], data['checks']['c4_agree'],
                 data['checks']['c5_tame']))
        out.append(data)
    return out


# -------------------------------------------------------------- the reads
def level_of(boxes, key, bins=None):
    """(level, z, exp, n3) with both terms in, pooled over boxes."""
    u = CT.new_cell()
    r = RT.new_rcell()
    ks = key_str(key)
    for data in boxes:
        for bb, cell in data['un'].get(ks, {}).items():
            if bins is None or int(bb) in bins:
                CT.merge(u, cell)
        for bb, cell in data['ram'].get(ks, {}).items():
            if bins is None or int(bb) in bins:
                RT.merge_r(r, cell)
    share = CT.share_of(*key)
    lv, z, exp = CT.level(u['n3'], u['c3'] + r['c3'],
                          u['ns'] + u['cN'] + r['cN'], share)
    return lv, z, exp, u['n3']


def fmt(lv, z):
    return ("%.3f" % lv if lv is not None else "--",
            "%+.2f" % z if z is not None else "--")


def parts_of(boxes, key, bins=None):
    """The pooled unramified cell and ramified cell of one stratum."""
    u = CT.new_cell()
    r = RT.new_rcell()
    ks = key_str(key)
    for data in boxes:
        for bb, cell in data['un'].get(ks, {}).items():
            if bins is None or int(bb) in bins:
                CT.merge(u, cell)
        for bb, cell in data['ram'].get(ks, {}).items():
            if bins is None or int(bb) in bins:
                RT.merge_r(r, cell)
    return u, r


def window_level(h, bins=None):
    """The level's value under the uniform model at a FIXED window as
    the discriminant grows, Frobenius independent at every prime power
    q^k < 1000 (2 included) at its Chebotarev share, so the weight on
    {e} over a quarter of the weight on N is sum_k w_k #{g^k = e} /
    (1/4 sum_k w_k #{g^k in N}), the counts the parent's (4). It is 1
    only when no k >= 2 power lies in the window."""
    num = den = 0.0
    for q in [2] + list(ECP.ODD_PRIMES):
        for (k, n) in CT.powers(q):
            bi = CT.bin_of(n)
            if bi is None or (bins is not None and bi not in bins):
                continue
            num += (1.0 / k) * CT.count_pow(h, k, 'e')
            den += (1.0 / k) * CT.count_pow(h, k, 'N')
    return num / (den / (h * h))


def s3_reproduce(boxes):
    section("S3  C1 -- the ramified rig's F2 reprinted from the pooled boxes")
    for label, upto in (("parents", 6000), ("wide", 24000)):
        if CAP < upto:
            print("  %s: cap %d below %d, skipped" % (label, CAP, upto))
            continue
        sub = [b for b, (lo, hi) in zip(boxes, BOXES) if hi <= upto]
        nf = {}
        for data in sub:
            for k, v in data['nfields'].items():
                nf[k] = nf.get(k, 0) + v
        print("  %s (|d| <= %d): %d fields with h > 1, excluded %s"
              % (label, upto, sum(nf.values()),
                 sum((d['excluded'] for d in sub), [])))
        for key, want in sorted(REPRO[label].items()):
            lv, z, exp, n3 = level_of(sub, key)
            print("    h = %d %s  all-p %4d  level %s z %s  (rig: %.3f)"
                  % (key[0], key[1], n3, fmt(lv, z)[0], fmt(lv, z)[1],
                     want))
            ok(lv is not None and abs(lv - want) <= REPRO_TOL,
               "C1: h = %d %s reads %s against %.3f" % (key[0], key[1],
                                                          lv, want))


def s4_control(boxes):
    section("S4  C2 -- the positive control: the split share's deficit "
            "at 3..31 by box, a known family term")
    es, ss, gs = [], [], []
    tot_m = tot_pm = tot_var = 0.0
    print("  %-16s %6s %8s %8s %8s %6s  %s"
          % ("box", "unr", "share", "deficit", "table", "z",
             "share at p = 3, 5, 7, 13"))
    for data, (lo, hi) in zip(boxes, BOXES):
        n = sum(v[0] for v in data['fam'].values())
        m = sum(v[1] for v in data['fam'].values())
        share = m / float(n)
        # the two-term table pooled over the primes at this box's weights
        pred_m = sum(data['fam'][p][0]
                     * FT.pred_share(p, lo, hi, [FT.SIGNS[0]])
                     for p in READ_PRIMES)
        pred = pred_m / float(n)
        sd = math.sqrt(pred * (1 - pred) / n)
        z = (share - pred) / sd
        tot_m += m
        tot_pm += pred_m
        tot_var += n * pred * (1 - pred)
        print("  (%5d, %5d]  %6d %8.4f %8.4f %8.4f %+6.2f  %s"
              % (lo, hi, n, share, 1.0 / 6 - share, 1.0 / 6 - pred, z,
                 " ".join("%.3f" % (data['fam'][p][1]
                                    / float(data['fam'][p][0]))
                          for p in (3, 5, 7, 13))))
        es.append(1.0 / 6 - share)
        ss.append(sd)
        gs.append(g_box(lo, hi))
    z_all = (tot_m - tot_pm) / math.sqrt(tot_var)
    print("  all boxes and primes pooled: measured %.0f split against "
          "%.1f predicted, z %+.2f" % (tot_m, tot_pm, z_all))
    ok(abs(z_all) <= 2, "C2: the pooled deficit leaves the two-term "
       "table by %.2f sigma" % z_all)
    if len(boxes) >= 3:
        cf, chf = fit_flat(es, ss)
        cd, chd = fit_decay(es, ss, gs)
        a, alo, ahi, cha = fit_alpha(es, ss, BOXES)
        print("  FLAT  c = %.4f  chi2 %.1f | DECAY (1/6) c = %.4f  chi2 %.1f"
              " | free alpha %.3f [%.3f, %.3f] chi2 %.1f"
              % (cf, chf, cd, chd, a, alo, ahi, cha))
        ok(chf - chd > 9, "C2: DECAY beats FLAT by only %.1f" % (chf - chd))
    else:
        print("  fewer than three boxes: the fit is not run")


def s5_excess(boxes):
    section("S5  THE h = 2 EXCESS BY BOX, both terms in -- P1-P4")
    key = (2, 'A')
    es, ss, gs, rows = [], [], [], []
    print("  %-16s %5s %6s %7s %7s %7s  %s"
          % ("box", "flds", "all-p", "exp", "level", "z", "by bin "
             "[3,30) [30,100) [100,300) [300,1000)"))
    for data, (lo, hi) in zip(boxes, BOXES):
        lv, z, exp, n3 = level_of([data], key)
        nf = data['nfields'].get(key_str(key), 0)
        bins = []
        for bb in range(len(BIN_EDGES) - 1):
            l2, z2, e2, _ = level_of([data], key, bins=(bb,))
            bins.append("%s(%s)" % fmt(l2, z2))
        print("  (%5d, %5d]  %5d %6d %7.1f %7s %7s  %s"
              % (lo, hi, nf, n3, exp, fmt(lv, z)[0], fmt(lv, z)[1],
                 " ".join(bins)))
        rows.append((lv, z, exp))
        if lv is not None:
            es.append(lv - 1.0)
            ss.append(1.0 / math.sqrt(exp))
            gs.append(g_box(lo, hi))
    print("  THE SPLIT BY TERM: the same level unramified only, and the "
          "ramified weights' landing against the algebra")
    print("  %-16s %7s %7s | %8s %8s %8s %8s %7s"
          % ("box", "unram", "z", "R_N/fld", "R_e", "forced",
             "surplus", "level"))
    for data, (lo, hi) in zip(boxes, BOXES):
        u, r = parts_of([data], key)
        nf = data['nfields'].get(key_str(key), 0)
        lu, zu, eu = CT.level(u['n3'], u['c3'], u['ns'] + u['cN'], 0.25)
        exp = (u['ns'] + u['cN'] + r['cN']) / 4.0
        # at h = 2 every P^3 place and every Q place is principal, so the
        # P^3 weight lands on {e} whole and the P^2 Q weight with the
        # P place's principal share, 1/2 under the uniform model
        forced = (r['src']['p3s'] + r['src']['p3i'] + r['src']['p3w']
                  + 0.5 * r['src']['p2q'])
        print("  (%5d, %5d]  %7s %7s | %8.2f %8.1f %8.1f %+8.3f %7.3f"
              % (lo, hi, *fmt(lu, zu), r['cN'] / max(nf, 1), r['c3'],
                 forced, (forced - r['cN'] / 4.0) / exp,
                 1.0 + (forced - r['cN'] / 4.0) / exp))
    for label, sel in (("old (0, 24000]", [b for b, (lo, hi)
                                            in zip(boxes, BOXES)
                                            if hi <= 24000]),
                       ("new (24000, 96000]", [b for b, (lo, hi)
                                               in zip(boxes, BOXES)
                                               if lo >= 24000])):
        if not sel:
            continue
        u, r = parts_of(sel, key)
        lu, zu, eu = CT.level(u['n3'], u['c3'], u['ns'] + u['cN'], 0.25)
        exp = (u['ns'] + u['cN'] + r['cN']) / 4.0
        forced = (r['src']['p3s'] + r['src']['p3i'] + r['src']['p3w']
                  + 0.5 * r['src']['p2q'])
        lv, z, _, _ = level_of(sel, key)
        print("    %-20s unramified %s z %s (+- %.4f) | forced ramified "
              "surplus %+.4f -> null %.3f against the level %s"
              % (label, *fmt(lu, zu), 1.0 / math.sqrt(eu),
                 (forced - r['cN'] / 4.0) / exp,
                 1.0 + (forced - r['cN'] / 4.0) / exp, fmt(lv, z)[0]))
        line = "    %-20s unramified by bin" % ""
        for bb in range(len(BIN_EDGES) - 1):
            u, r = parts_of(sel, key, bins=(bb,))
            l2, z2, _ = CT.level(u['n3'], u['c3'], u['ns'] + u['cN'], 0.25)
            line += "  [%d, %d) %s z %s" % (BIN_EDGES[bb],
                                            BIN_EDGES[bb + 1], *fmt(l2, z2))
        print(line)
    print("  THE FIXED WINDOW'S VALUE under independent uniform "
          "Frobenius at every prime power, h = 2, unramified: whole "
          "window %.3f; by bin %s"
          % (window_level(2), ", ".join(
              "[%d, %d) %.3f" % (BIN_EDGES[bb], BIN_EDGES[bb + 1],
                                 window_level(2, bins=(bb,)))
              for bb in range(len(BIN_EDGES) - 1))))
    print("  the [3, 30) unramified level by box:",
          ", ".join("%.3f" % CT.level(*(lambda u: (u['n3'], u['c3'],
                                                    u['ns'] + u['cN']))(
                                          parts_of([d], key, bins=(0,))[0]),
                                       0.25)[0] for d in boxes))
    print("  by bin, the two new boxes pooled and the four old pooled:")
    for label, sel in (("old (0, 24000]", [b for b, (lo, hi)
                                            in zip(boxes, BOXES)
                                            if hi <= 24000]),
                       ("new (24000, 96000]", [b for b, (lo, hi)
                                               in zip(boxes, BOXES)
                                               if lo >= 24000])):
        if not sel:
            continue
        line = "    %-20s" % label
        for bb in range(len(BIN_EDGES) - 1):
            l2, z2, e2, _ = level_of(sel, key, bins=(bb,))
            line += "  [%d, %d) %s z %s" % (BIN_EDGES[bb],
                                            BIN_EDGES[bb + 1], *fmt(l2, z2))
        lv, z, exp, n3 = level_of(sel, key)
        line += "  | all %s z %s" % fmt(lv, z)
        print(line)
    out = dict(rows=rows)
    if len(es) >= 3:
        cf, chf = fit_flat(es, ss)
        cd, chd = fit_decay(es, ss, gs)
        a, alo, ahi, cha = fit_alpha(es, ss, BOXES[:len(es)])
        print("  FLAT  c = %.4f  chi2 %.1f | DECAY (1/6) c = %.4f  chi2 %.1f"
              " | free alpha %.3f [%.3f, %.3f] chi2 %.1f"
              % (cf, chf, cd, chd, a, alo, ahi, cha))
        c26, ch26 = fit_decay(es, ss, [g_box(lo, hi, CONTROL_ALPHA)
                                       for (lo, hi) in BOXES[:len(es)]])
        print("  at the control's calibrated exponent %.2f: chi2 %.1f "
              "(%+.1f against FLAT)" % (CONTROL_ALPHA, ch26, ch26 - chf))
        out.update(flat=(cf, chf), decay=(cd, chd), alpha=(a, alo, ahi))
    return out


CONTROL_ALPHA = 0.26      # what C2's genuine family term read on these boxes


def image_share_cells(data, key, bins=None):
    """The h = 2 stratum's weights sorted by what the algebra forces.
    Returns (ns, n3, cN, c3, forced_u, R_p3, R_p2q, R_e): forced_u the
    unramified weight landing on e by necessity (split squares, inert
    cubes), R_p3 the totally ramified weight (all of it on e), R_p2q the
    P^2 Q weight (Q forced, P free), R_e the ramified weight on e."""
    ks = key_str(key)
    ns = n3 = 0
    cN = c3 = fu = rp3 = rp2q = re = 0.0
    for bb, cell in data['un'].get(ks, {}).items():
        if bins is not None and int(bb) not in bins:
            continue
        ns += cell['ns']
        n3 += cell['n3']
        cN += cell['cN']
        c3 += cell['c3']
        fu += cell['c3_src']['ssq'] + cell['c3_src']['icb']
    for bb, cell in data['ram'].get(ks, {}).items():
        if bins is not None and int(bb) not in bins:
            continue
        rp3 += cell['src']['p3s'] + cell['src']['p3i'] + cell['src']['p3w']
        rp2q += cell['src']['p2q']
        re += cell['c3']
    return ns, n3, cN, c3, fu, rp3, rp2q, re


def image_level(data_list, key, bins=None):
    """The h = 2 level with each term expected at ITS image's share: the
    forced weights at 1, the P^2 Q pairs at 1/2 (one free class in Z/2),
    everything else at 1/4. Returns (level, z, exp, forced fraction of
    the N weight, the excess the forcing alone predicts)."""
    tot = [0.0] * 8
    for data in data_list:
        for i, v in enumerate(image_share_cells(data, key, bins)):
            tot[i] += v
    ns, n3, cN, c3, fu, rp3, rp2q, re = tot
    N = ns + cN + rp3 + rp2q
    if N <= 0:
        return None, None, 0.0, 0.0, 0.0
    exp = (N - fu - rp3 - rp2q) * 0.25 + fu + rp3 + rp2q * 0.5
    count = n3 + c3 + re
    lv = count / exp
    z = (count - exp) / math.sqrt(exp)
    forcing = (exp - N * 0.25) / (N * 0.25)
    return lv, z, exp, (fu + rp3 + rp2q) / N, forcing


def s5b_image(boxes):
    section("S5b THE IMAGE-SHARE READ (post-hoc, after S5 printed) -- the "
            "h = 2 level with each term at its own image's share")
    print("  at h = 2 the algebra forces onto e: a split prime's square "
          "(2u = 0), an inert prime's cube (the three shifts of a")
    print("  sum-zero vector sum to 0, at every h), every totally "
          "ramified place (3[P] = 0 in Z/2) and the Q of a P^2 Q pair")
    print("  ([Q] = -2[P]); free: the raw split primes at 1/4 and the P "
          "of a P^2 Q pair at 1/2. The uniform read counts every")
    print("  weight at 1/4. Columns: the forced fraction of the N weight, "
          "the excess the forcing alone predicts, the image level.")
    key = (2, 'A')
    print("  %-16s %7s %8s %8s %8s %7s   %s"
          % ("box", "exp", "forced", "forcing", "uniform", "image",
             "image level by bin [3,30) [30,100) [100,300) [300,1000)"))
    for data, (lo, hi) in zip(boxes, BOXES):
        lu, zu, eu, _ = level_of([data], key)
        lv, z, exp, ff, forcing = image_level([data], key)
        bins = []
        for bb in range(len(BIN_EDGES) - 1):
            l2, z2, _, _, _ = image_level([data], key, bins=(bb,))
            bins.append("%s(%s)" % fmt(l2, z2))
        print("  (%5d, %5d]  %7.1f %8.3f %+8.3f %8s %7s   %s"
              % (lo, hi, exp, ff, forcing, fmt(lu, zu)[0],
                 "%s z %s" % fmt(lv, z), " ".join(bins)))
    for label, sel in (("old (0, 24000]", [b for b, (lo, hi)
                                            in zip(boxes, BOXES)
                                            if hi <= 24000]),
                       ("new (24000, 96000]", [b for b, (lo, hi)
                                               in zip(boxes, BOXES)
                                               if lo >= 24000]),
                       ("all", list(boxes))):
        if not sel:
            continue
        lv, z, exp, ff, forcing = image_level(sel, key)
        lu, zu, _, _ = level_of(sel, key)
        line = ("    %-20s uniform %s  image %s z %s (exp %.1f, forced "
                "%.3f, forcing %+.3f)"
                % (label, fmt(lu, zu)[0], fmt(lv, z)[0], fmt(lv, z)[1],
                   exp, ff, forcing))
        print(line)
    # the P^2 Q pair's free place: its principal share by box
    print("  the P^2 Q pair's free place P, principal share by box (the "
          "image read takes 1/2): %s"
          % ", ".join("%.3f" % (d['census'][key_str(key)]['p2q']['pp']
                                / float(d['census'][key_str(key)]['p2q']
                                        ['n'])) for d in boxes))


def s6_others(boxes):
    section("S6  THE OTHER STRATA in the new boxes -- P5")
    new = [b for b, (lo, hi) in zip(boxes, BOXES) if lo >= 24000]
    if not new:
        print("  no box above 24000 at cap %d" % CAP)
        return None
    keys = set()
    for data in new:
        keys.update(key_of(k) for k in data['nfields'])
    out = {}
    print("  level with both terms in | unramified only (the level the "
          "cube-term rig read)")
    for key in sorted(keys):
        lv, z, exp, n3 = level_of(new, key)
        u, _r = parts_of(new, key)
        lu, zu, _eu = CT.level(u['n3'], u['c3'], u['ns'] + u['cN'],
                               CT.share_of(*key))
        nf = sum(d['nfields'].get(key_str(key), 0) for d in new)
        tag = "  readable" if exp >= MIN_READ and key[1] != 'D' else ""
        print("  h = %2d %s  %4d fields  all-p %4d  exp %7.1f  level %s "
              "z %s | unramified %s z %s%s"
              % (key[0], key[1], nf, n3, exp, *fmt(lv, z), *fmt(lu, zu),
                 tag))
        out[key] = (lv, z, exp)
    return out


def s7_verdict(boxes, ex, others):
    section("S7  THE SLATE READ")
    key = (2, 'A')
    old = [b for b, (lo, hi) in zip(boxes, BOXES) if hi <= 6000]
    new = [b for b, (lo, hi) in zip(boxes, BOXES) if lo >= 24000]
    if not new:
        print("  no new box at cap %d: P1, P3-P5 not read (rehearsal)" % CAP)
        return
    lp, zp, ep, _ = level_of(old, key)
    lt, zt, et, _ = level_of(new, key)
    Ep, sp = lp - 1, 1.0 / math.sqrt(ep)
    Et, st = lt - 1, 1.0 / math.sqrt(et)
    ratio = g_box(0, 6000) / g_box(24000, 96000)
    Es, ss_ = Ep / ratio, sp / ratio
    z_flat = (Et - Ep) / math.sqrt(st ** 2 + sp ** 2)
    z_dec = (Et - Es) / math.sqrt(st ** 2 + ss_ ** 2)
    print("  parents' box excess %.4f +- %.4f; scaled by 1/%.3f: %.4f "
          "+- %.4f; top (24000, 96000] excess %.4f +- %.4f"
          % (Ep, sp, ratio, Es, ss_, Et, st))
    print("  top against parents' %+.2f sigma; top against scaled %+.2f "
          "sigma" % (z_flat, z_dec))
    if abs(z_flat) <= 2 and z_dec > 2:
        v = "KILL -- the excess is the field's"
    elif z_flat < -2 and abs(z_dec) <= 2:
        v = "SURVIVE -- the excess falls at the family's rate"
    else:
        v = "NEITHER SHAPE as frozen -- read the fits"
    print("  [P1] %s" % v)
    if 'flat' in ex:
        cf, chf = ex['flat']
        cd, chd = ex['decay']
        a, alo, ahi = ex['alpha']
        print("  [P2] FLAT chi2 %.1f, DECAY chi2 %.1f, difference %+.1f "
              "(FLAT wins by > 4: %s); alpha %.3f in [%.3f, %.3f]: "
              "contains 0 %s, excludes 1/6 %s"
              % (chf, chd, chd - chf, "YES" if chd - chf > 4 else "NO",
                 a, alo, ahi, "YES" if alo <= 0 <= ahi else "NO",
                 "YES" if not (alo <= 1.0 / 6 <= ahi) else "NO"))
    print("  [P3] top excess %.4f +- %.4f, %.1f sigma above 0: %s"
          % (Et, st, Et / st,
             "YES" if 0.08 <= Et <= 0.12 and st < 0.010 and Et / st > 8
             else "NO"))
    p4 = []
    for data, (lo, hi) in zip(boxes, BOXES):
        if lo < 24000:
            continue
        zs = [level_of([data], key, bins=(bb,))[1] for bb in range(4)]
        good = (zs[0] is not None and zs[0] > 2 and zs[3] > 2
                and abs(zs[1]) <= 2 and abs(zs[2]) <= 2)
        p4.append(good)
        print("  [P4] (%d, %d] bin z %s: %s"
              % (lo, hi, ", ".join("%+.2f" % z for z in zs),
                 "YES" if good else "NO"))
    if others:
        l3 = others.get((3, 'M'))
        hi_ = [(k, v) for k, v in others.items()
               if k[0] >= 4 and k[1] != 'D' and v[2] >= MIN_READ]
        below = [k for k, v in hi_ if v[0] is not None and v[0] < 1]
        print("  [P5] h = 3 M in the new boxes %s (within 2 sigma: %s); "
              "readable h >= 4 strata %d, below 1: %s"
              % ("%s z %s" % fmt(l3[0], l3[1]) if l3 else "absent",
                 "YES" if l3 and abs(l3[1]) <= 2 else "NO", len(hi_),
                 ", ".join("h = %d %s" % k for k in below) or "none"))


def main():
    t0 = time.time()
    fields = s1_population()
    boxes = s2_boxes(fields)
    del fields
    gc.collect()
    s3_reproduce(boxes)
    s4_control(boxes)
    ex = s5_excess(boxes)
    s5b_image(boxes)
    others = s6_others(boxes)
    s7_verdict(boxes, ex, others)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall this process; box walls %s"
          % (CHECKS, time.time() - t0,
             ["%.0f" % d['wall'] for d in boxes]))


if __name__ == "__main__":
    main()
