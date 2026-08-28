r"""DOES THE FIRST-HIT SURVIVAL DERIVATION PORT TO DEGREE 3, AND IS THE
REGIME SPLIT LOAD-BEARING IN IT? -- the early first hit over cubic
fields as the count's survival function, the index of dispersion read
at every index scale, and the h = 3 stratum integrated as two densities
against one.

THE QUESTION. Over real quadratic fields the early first hit is derived:
explore_first_hit_survival.py reads the first principal split prime as
the survival function of the field's principal count, E[I] = sum_n
P(N(n) = 0), carries the index of dispersion at every index scale
through a two-moment law, and returns the measured first hit within
noise at all seven strata. Over cubic fields both of its inputs
reproduce -- the share short at small p and the count under-dispersed
against its own local density (explore_cubic_class_map.py F2-F3) -- and
the derivation has not been run there. Degree 3 adds one thing degree 2
did not have: a totally split prime carries THREE degree-1 places whose
classes sum to zero, and at class number 3 the realized triples are
either the whole sum-zero group or its diagonal
(explore_cubic_split_triple.py), so the same class number holds TWO
arithmetics with two principal densities. This rig ports the derivation
and asks whether that split is load-bearing in it.

WHOSE VOCABULARY, asked at the freeze. The unit is a PRIME carrying a
degree-1 place, and its bit is "some degree-1 place over p is
principal" -- the quantity the nominal q's of explore_cubic_principal.py
derivation (2) are probabilities of, and the quantity the map's share
and index read. The index I is the position of the first such prime in
the field's own sequence of degree-1-carrying odd unramified primes; a
field's sequence mixes the two kinds (totally split, partially split),
and the bit's density depends on the kind.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM DEGREE 2: the survival identity, the two-moment law, the index
    curve and the paired bootstrap are explore_first_hit_survival.py's,
    imported rather than re-implemented. The identity is law at any
    degree (it holds for any joint law of the bits); the two-moment
    family and its exactness at both ends are the same algebra with a
    different q per prime. What is imported and UNDER TEST is the
    finding: that the index at the first hit's own scales accounts for
    the early hit.
 T2 FROM THE CUBIC RIGS: the enumeration, the class reading, the map's
    verdict per prime and the regime reader are explore_cubic_
    principal.py's, explore_cubic_class_map.py's and explore_cubic_
    split_triple.py's, imported with their controls (the inherited h = 1
    pin, the norm accounting, the fingerprint assumption) and not re-run
    here. The per-field record they produce is checkpointed to
    _ckpt/cubic_first_hit.json so the bootstrap does not pay for it.
 T3 THE SIGN. That the measured first hit arrives EARLY against a
    correctly priced independent model is degree 2's finding
    (explore_paired_division.py); at degree 3 only the nominal-density
    ratio has been read (early by 1.17x to 3.21x, which mixes the share
    deficit in), never the local one. The local independent ratio is
    read here for the first time, and the derivation has something to
    account for only where it sits below 1.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE COUNT OVER TRIPLES, AND ITS COVARIANCE -- DERIVED, NOT
      TRANSPLANTED. At a totally split prime (p) = P1 P2 P3 with classes
      c1 + c2 + c3 = 0 in Cl(K), of order h. Under the uniform model the
      pair (c1, c2) is uniform on Cl^2 and c3 = -(c1 + c2). Per-place
      principal indicators e_i = 1[c_i = 0] have mean 1/h each, and
      PAIRWISE they are independent: P(c1 = 0, c2 = 0) = 1/h^2, and
      P(c1 = 0, c3 = 0) = P(c1 = 0, c2 = 0) = 1/h^2 likewise. So every
      pairwise covariance is ZERO and the constraint lives in the
      three-way term alone: P(all three principal) = 1/h^2 against
      1/h^3 for three free draws. The prime's bit b = 1 - prod (1 - e_i)
      therefore has

          q_split = 1 - (h-1)(h-2)/h^2   (uniform on the sum-zero group)

      against 1 - (h-1)^3/h^3 for three free places -- 1 against 7/8 at
      h = 2, 7/9 against 19/27 at h = 3. At a DEGENERATE field (the
      realized triples on the diagonal) the three coordinates are ONE
      draw: e1 = e2 = e3 and q_split = 1/h. At a partially split prime
      the one degree-1 place is uniform on Cl and q_partial = 1/h in
      both regimes. Across PRIMES the Frobenius model is independent, so
      N(n) = sum_{i<=n} b_i is a sum of independent Bernoullis with
      kind- and regime-dependent q, and its independent variance is
      V_n = sum q_i (1 - q_i) EXACTLY as at degree 2 -- the sum-zero
      constraint changes q and nothing else. The regularity the index
      reads is the departure of the count's variance from that V_n, and
      it is a between-prime fact the model has no term for.

  (2) THE TWO DENSITIES. A field's per-prime q is the (kind, prime-bin)
      cell's measured share over the OTHER fields of its stratum --
      leave-one-out, so the share deficit cannot enter the reference
      (explore_paired_division.py derivation (2), the map's K2 amendment
      II). The stratum is (signature, Galois type, class number,
      REGIME), the regime being read off the equal-class fraction where
      3 divides h (degenerate at fraction >= 0.9) and single elsewhere.
      So at h = 3 the split primes of a degenerate field are priced from
      degenerate fields and those of a generic field from generic ones:
      two densities, integrated separately. The POOLED reading prices
      every h = 3 field from all 83, one density -- and reads the index
      of dispersion across the mixture, where it sits at 1.583 rather
      than 0.220 and 0.252 inside the halves.

  (3) E[I] ON PAPER, NOMINAL AND INDEPENDENT. A quarter of the
      degree-1-carrying primes are totally split (density 1/6 against
      1/2 partial), so P(hit at a prime) = q_split/4 + 3 q_partial/4 and
      E[I] = 1/P(hit): 1/(1/4 + 3/8) = 1.6 at h = 2, where EVERY split
      prime is principal (the sum-zero group at h = 2 has no proper
      stable subgroup, so a non-principal split prime there is
      impossible and is a saturation failure of the map if printed);
      1/(7/36 + 1/4) = 2.25 at generic h = 3 and 3 at degenerate h = 3;
      1/(5/32 + 3/16) = 2.9 at h = 4; 1/(13/100 + 3/20) = 3.6 at h = 5.
      The bottom-bin share deficit (0.64 to 0.12 of nominal) pushes each
      up. So the first hit at degree 3 lives at index scales 2 to 4 --
      SHALLOWER than degree 2's 2.5 to 5 -- and at n = 1 the index is 1
      in expectation whatever the joint law, so the regularity has
      less room to act here than it had at degree 2. That is a
      prediction about the SIZE of what the derivation can find, made
      before the print.

  (4) THE STANDARD ERROR, PRICED FROM EACH STRATUM'S OWN FIELD COUNT.
      The first-hit index is near-geometric with cv ~ sqrt(1 - P(hit)),
      so the ratio's sd is about cv / sqrt(n_fields): 0.06 at complex
      h = 2 (94 fields), 0.11 at generic h = 3 (45), 0.13 at degenerate
      h = 3 (38), 0.20 at h = 4 and h = 5 (18 each), 0.3 at h = 6 and 7
      (6 each, printed and not read). A 1.96-sd band is therefore +-0.12
      at h = 2 and +-0.4 at h = 4: only h = 2 can grade a size, and
      degree 2's own shortfall (0.87 at its h = 2) would sit at about
      2 sd there. "In band" at every other stratum is cheap and is not
      read as a landing; what the thin strata carry is the SIGN of the
      independent ratio.

  (5) WHERE THE POWER IS. A derivation lands where the independent
      ratio is OUT of band and the derived one in it. Where both are
      inside, the stratum cannot tell the two apart and says so. The
      second observable is not a ratio but a SEPARATION: the h = 3
      derivation run on the mixture against the same run inside the
      halves. An index above 1 makes the two-moment law LESS regular
      than independence, so the pooled model's E[I] moves LATER than
      independence while the split model's moves earlier -- opposite
      directions, on the same 83 fields, in one paired bootstrap.

THE SLATE -- PREDICTIONS, FIXED BEFORE THE ENGINE.

  P1. THE SIGN PORTS. At complex h = 2, h = 3 (both halves), h = 4 and
      h = 5, the local independent model's ratio (measured mean index
      over the model's) sits below 1.
  P2. THE DERIVATION LANDS WHERE IT CAN BE GRADED. At complex h = 2 the
      derived ratio in index units sits inside 1.96 bootstrap sd of 1,
      the independent ratio outside it.
  P3. THE SPLIT IS LOAD-BEARING. At complex h = 3 the pooled and the
      two-density derived ratios differ by more than 2 bootstrap sd of
      their paired difference, the pooled one further from 1.
  P4. THE INDEX HAS A SCALE HERE TOO. At h = 2 the index at n = 1 sits
      within 2 null sd of 1 and at n = 3 below 1 by more than 2.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS.

  K1 kills P1: any read stratum's printed independent index-ratio at or
     above 1.
  K2 kills P2: at h = 2 the printed derived z at or beyond 2 in absolute
     value, OR the printed independent z inside 2 (no power: nothing to
     account for).
  K3 kills P3: the printed pooled-minus-split z under 2 in absolute
     value at h = 3.
  K4 kills P4: at h = 2 the printed index-curve z at n = 1 beyond 2 in
     absolute value, or at n = 3 at or above -2.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE IMPORT. The index of dispersion read here against the coarse
      (kind, bin) leave-one-out cells over the WHOLE complex h = 3
      stratum reproduces the map's 1.583 to 0.02, and inside the halves
      the split-triple rig's 0.220 and 0.252 to 0.02.
  C2. THE REGULAR END IS EXACT. The imported engine on period-k
      sequences at random phase returns (k + 1)/(2k) to 1e-9 at the
      exact index (k = 2, 3, 5) -- the engine's own control, re-run
      because the engine is imported.
  C3. THE ALGEBRA AT h = 2. Every totally split prime at complex h = 2
      carries a principal place: the split cells' shares read 1.000.
  C4. THE PIPELINE UNDER ITS OWN NULL. Bits regenerated at each cell's
      full share, 20 replicates through the whole machinery: the index
      curve reads 1 within noise at h = 2 and the derived ratio sits
      within 0.02 of the independent one there.

RESOURCE. The cubic pipeline (enumeration, class reading, map) is
explore_cubic_class_map.py's own at ~4 min wall and ~80 MB the first
time, then the checkpoint; the derivation itself is per-field float
accumulation, no numpy, seconds. Under 512MB; wall-clock printed.

THE FINDINGS.

  F1. THE SIGN PORTS, AND THE DERIVATION LANDS AT THE ONE STRATUM THAT
      CAN GRADE IT (pattern over the five complex strata of 18 fields or
      more; P1 SURVIVES at all five; P2 SURVIVES in its first clause and
      is KILLED in its second, h = 2 carrying no power). Index units --
      the measured mean first-hit index over the model's, E[I] = sum S_n
      exact, the bootstrap sd behind each z:

        stratum          n  meas.I indep.I  ratio    z  | deriv.I  ratio    z
        h = 2           94   2.56   2.76   0.929 -1.81 |   2.68   0.956 -0.98
        h = 3 degen.    38   3.26   3.90   0.837 -2.78 |   3.23   1.009 +0.13
        h = 3 generic   45   2.24   2.35   0.956 -0.95 |   2.26   0.994 -0.11
        h = 4           18   5.44   6.19   0.879 -0.97 |   5.90   0.922 -0.62
        h = 5           18   5.44   5.61   0.971 -0.34 |   4.90   1.111 +1.04

      Against its own leave-one-out density the first hit arrives EARLY
      at every one of the five -- the quadratic side's direction, now
      read at degree 3 on the local reference for the first time -- and
      only ONE stratum carries it past the band: the degenerate half of
      class number 3, at 0.837 and 2.8 sd. There the survival model fed
      the index curve returns 1.009 +/- 0.07 (0.787 -> 0.967 in
      p-units). At h = 2 the independent shortfall is 7% at 1.8 sd --
      the sd priced at 0.06 on paper reads 0.039, a totally split prime
      being a CERTAIN hit at h = 2 (C3) so the first hit is nearer
      deterministic than the geometric guess -- and the derivation
      takes it to 0.956 +/- 0.045, halfway, with the independent ratio
      inside the band the derivation cannot be graded there. h = 5's
      overshoot to 1.111 is read against its own null of 1.13 (C4): at
      18 fields the leave-one-out reference is biased upward by 11 to
      13% and the stratum says nothing. h = 4 clamps 16 field-scales,
      its index at n = 1 reading 2.32 at z +3.1 -- the one scale above
      1 by more than 2 sd among the 40 read.

  F2. THE REGIME SPLIT IS NOT LOAD-BEARING FOR THE STRATUM'S MEAN, AND
      IT IS FOR WHERE THE EARLY HIT SITS (observation; P3 KILLED). The
      83 fields of class number 3 priced as ONE density and integrated
      as one stratum derive 1.005 +/- 0.029; priced as two regimes and
      integrated separately, 1.002 +/- 0.032; the paired difference is
      +0.003 at sd 0.024, z +0.14, and the independent ratios agree too
      (0.884 against 0.886). The reason is printed: the pooled index
      curve reads 0.904, 0.897, 0.556, 0.428, 0.434 at n = 1..5 and
      1.526 at the cap. The mixture's over-dispersion is the gap between
      two groups' MEANS, which grows with the count and has not opened
      at the scales where the first hit is decided (n* = 3.9 and 2.3),
      so at those scales the pooled stratum is under-dispersed like
      every other and the two-moment law reads the same regularity
      either way. What the split decides is WHICH fields are early: the
      degenerate half at 0.837 (z -2.78) and the generic half at 0.956
      (z -0.95), the whole of the stratum's early hit sitting on the 38
      fields whose split primes carry one class three times.

  F3. THE DEGENERATE FIELDS' INDEX CURVE IS THE QUADRATIC ONE
      (observation). At degenerate h = 3 the index reads 0.960, 0.846,
      0.509, 0.496, 0.462 at n = 1..5 against 0.943, 0.717, 0.612,
      0.523, 0.459 at quadratic h = 2 (explore_first_hit_survival.py
      F2): a degenerate field's split prime is ONE draw, as a quadratic
      field's split prime is one place, and the two curves fall from 0.95
      to the same 0.46 over five scales -- the same endpoints, not the
      same digits between them. The generic half reads 0.453,
      0.865, 0.642, 0.754, 0.541, and its first scale carries a density
      term: measured survival 0.711 against the cell's 0.613 (deficit
      1.16 against phi 0.95), the pooled-cell reading the degree-2 rig's
      F3 names and larger here, the first degree-1-carrying prime being
      3 or 5 and one cell holding both. At h = 2 the curve is 0.958,
      0.765, 0.831, 0.860, 0.879, 0.762, 0.720, 0.604 -- coherent, no
      scale beyond 2 sd before n = 8 (K4: n = 3 reads 0.831 at z -1.09,
      so P4's second clause is KILLED and its first holds, n = 1 at
      0.958, z -0.14) -- the degree-2 h = 4 shape. And the tail is the
      degree-2 tail: every field has hit by its eighth prime at h = 2
      and its seventh at both h = 3 halves, where the two-moment law
      keeps 0.8%, 3.4% and 0.2% alive -- the law is exact at both ends
      and too slow between them, at this degree as at the other.

RUN RECORD: `python prime/code/memwatch.py python
prime/code/explore_cubic_first_hit.py`, one process, CPython, no BLAS.
First run 210.3 s wall, peak working set 76.6 MB (the cubic pipeline
194.6 s: 15370 polynomials -> 1103 fields, 867 with h = 1, 236 mapped,
every prime decided; the checkpoint written); the second, from the
checkpoint, 15.9 s at 42.5 MB. Odd primes to 1000, index scales 1..40,
200 bootstrap resamples per stratum, 20 null replicates; 24899 primes
priced at the fine cell, 193 at the coarse, 67 at the kind's stratum
share. Five checks, all green on the second run. ONE CONTROL WAS
CORRECTED AFTER ITS FIRST PRINT AND BEFORE ANY KILL WAS READ, and the
correction was to the CONTROL: C1 first computed the index against this
rig's own (kind, bin) cells and read 1.508, 0.207, 0.297 against the
map's 1.583, 0.220, 0.252 -- a different reference, not a different
count -- and now computes the map's own statistic (one bin ratio over
both kinds, scaled onto each kind's nominal q), reproducing all three
to three decimals, with this rig's reference printed beside it (0.202
and 0.301 at the halves, 0.344 at h = 2). The pooled index curve print
was added in the same edit, so F2's reason is printed rather than
inferred; every other number of the first run is reproduced unchanged
by the second. Null offsets (C4): h = 2 clean at 0.994 and 0.991 with
the curve at 1.00-1.10; the thinner strata carry the leave-one-out
inflation, 1.01 to 1.13 in both ratios at h = 3 to 5, which is what
their ratios are read against.
"""

import json
import os
import sys
import time
from math import sqrt
from random import Random

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_first_hit_survival as FHS
import explore_cubic_principal as ECP
import explore_cubic_class_map as CCM
import explore_cubic_split_triple as EST

CKPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ckpt",
                    "cubic_first_hit.json")
CAP = ECP.PRIME_CAP                      # 1000
FINE_EDGES = [3, 6, 10, 18, 32, 56, 100, 178, 316, 562, CAP + 1]
COARSE_EDGES = list(ECP.BIN_EDGES)       # (3, 30, 100, 300, 1000)
COARSE_EDGES[-1] = CAP + 1
MIN_CELL = 8                             # other-field primes a fine cell needs
MIN_STRATUM = ECP.MIN_STRATUM            # 5
HIGH_FRAC = EST.HIGH_FRAC                # 0.9, the degenerate threshold
NSCALE = 40
NSHOW = 8
BOOT = 200
REPS = 20
SEED = 2029
CHECKS = [0, 0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
        print("  !! FAIL: " + msg)


def section(t):
    print("\n=== %s ===" % t)


# ------------------------------------------------------------ the records

def build_records():
    """The cubic pipeline, run once: every field with H > 1, its verdict
    per degree-1-carrying odd unramified prime, and its equal-class
    count over its totally split primes."""
    t0 = time.time()
    fields, buckets = ECP.enumerate_fields(ECP.DISC_CAP)
    print("  %d polynomials -> %d fields, %.1f s"
          % (buckets[0], len(fields), time.time() - t0))
    t0 = time.time()
    out = []
    n_h1 = 0
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        rows = ECP.t2_rows(O, a, b, c)
        h, kind, gp, rel = CCM.class_and_relations(O, d, cx, rows)
        if h is None:
            raise RuntimeError("unresolved class reading at d = %d" % d)
        if h == 1:
            n_h1 += 1
            continue
        H, piv, k, per_prime = EST.read_field(O, a, b, c, d, cx, gp, rel)
        ns, ne, bs, bi, nn, verdicts = EST.field_stats(per_prime, piv, k)
        out.append({"d": d, "cx": bool(cx), "cyc": CCM.is_cyclic(d),
                    "H": H, "n_split": ns, "n_equal": ne,
                    "verdicts": [(p, kd, prin) for (p, kd, prin)
                                 in verdicts]})
    print("  class reading + map: %d fields, %d with h = 1, %d mapped, "
          "%.1f s" % (len(fields), n_h1, len(out), time.time() - t0))
    return out


def load_records():
    if os.path.exists(CKPT):
        with open(CKPT) as fh:
            recs = json.load(fh)
        print("  checkpoint %s: %d mapped fields" % (CKPT, len(recs)))
        return recs
    recs = build_records()
    os.makedirs(os.path.dirname(CKPT), exist_ok=True)
    with open(CKPT, "w") as fh:
        json.dump(recs, fh)
    print("  checkpoint written: %s" % CKPT)
    return recs


def regime_of(r):
    if r["H"] % 3 != 0:
        return "-"
    if r["n_split"] == 0:
        return "?"
    return "D" if r["n_equal"] / float(r["n_split"]) >= HIGH_FRAC else "M"


def sig(r):
    return "complex" if r["cx"] else ("real-cyc" if r["cyc"] else "real")


def make_fields(recs, split_regime=True):
    """The engine's field dicts: 'splits' is the field's sequence of
    (p, hit) over its degree-1-carrying odd unramified primes, 'kinds'
    beside it; 'key' is the stratum."""
    out = []
    for r in recs:
        sp, kinds, L1 = [], [], None
        for (p, kd, prin) in r["verdicts"]:
            if prin is None or p > CAP:
                continue
            sp.append((p, bool(prin)))
            kinds.append(kd)
            if prin and L1 is None:
                L1 = p
        reg = regime_of(r) if split_regime else "-"
        out.append({"D": r["d"], "h": r["H"], "splits": sp, "kinds": kinds,
                    "L1": L1, "key": (sig(r), r["H"], reg)})
    return out


# ------------------------------------------------- the leave-one-out cells

def bin_of(p, edges):
    for i in range(len(edges) - 1):
        if edges[i] <= p < edges[i + 1]:
            return i
    return None


def cell_shares(group):
    """Per field, per prime: q = the (kind, fine bin) cell's share over
    the OTHER fields of the group, falling back to the (kind, coarse
    bin) cell and then to the kind's group-wide share when the fine
    cell holds fewer than MIN_CELL other-field primes. Writes f['qs']
    and returns the count of primes priced at each level."""
    levels = [0, 0, 0]
    tot = {}
    own = []
    for f in group:
        mine = {}
        for (p, hit), kd in zip(f["splits"], f["kinds"]):
            for key in ((kd, "f", bin_of(p, FINE_EDGES)),
                        (kd, "c", bin_of(p, COARSE_EDGES)),
                        (kd, "g", 0)):
                n, h = mine.get(key, (0, 0))
                mine[key] = (n + 1, h + hit)
        own.append(mine)
        for key, (n, h) in mine.items():
            tn, th = tot.get(key, (0, 0))
            tot[key] = (tn + n, th + h)
    for f, mine in zip(group, own):
        qs = []
        for (p, hit), kd in zip(f["splits"], f["kinds"]):
            q = None
            for lv, key in enumerate(((kd, "f", bin_of(p, FINE_EDGES)),
                                      (kd, "c", bin_of(p, COARSE_EDGES)),
                                      (kd, "g", 0))):
                tn, th = tot.get(key, (0, 0))
                n, h = mine.get(key, (0, 0))
                if tn - n >= MIN_CELL or lv == 2:
                    q = (th - h) / float(tn - n) if tn - n > 0 else 0.5
                    levels[lv] += 1
                    break
            qs.append(q)
        f["qs"] = qs
    return levels


def strata_of(fields):
    st = {}
    for f in fields:
        st.setdefault(f["key"], []).append(f)
    return st


def price(fields):
    """Leave-one-out cells inside every stratum; returns the levels."""
    levels = [0, 0, 0]
    for key, group in strata_of(fields).items():
        lv = cell_shares(group)
        for i in range(3):
            levels[i] += lv[i]
    return levels


def map_index(group, h):
    """The map's own statistic, C1's import: the index against each
    coarse bin's measured share taken leave-one-out and scaled onto
    each KIND's nominal q -- one ratio per bin over both kinds, which is
    the map's reference (its K2 amendment II) and not this rig's
    per-kind cell. Written so the two references print side by side."""
    nb = len(COARSE_EDGES) - 1
    totq = [0.0] * nb
    totc = [0.0] * nb
    per = []
    for f in group:
        myq = [0.0] * nb
        myc = [0.0] * nb
        for (p, hit), kd in zip(f["splits"], f["kinds"]):
            i = bin_of(p, COARSE_EDGES)
            myq[i] += ECP.q_nominal(kd, h)
            myc[i] += hit
        per.append((myq, myc))
        for i in range(nb):
            totq[i] += myq[i]
            totc[i] += myc[i]
    ss = vv = 0.0
    for f, (myq, myc) in zip(group, per):
        ratio = [((totc[i] - myc[i]) / (totq[i] - myq[i])
                  if totq[i] - myq[i] > 0 else None) for i in range(nb)]
        cnt = mu = var = 0.0
        usable = True
        for (p, hit), kd in zip(f["splits"], f["kinds"]):
            i = bin_of(p, COARSE_EDGES)
            if ratio[i] is None:
                usable = False
                break
            q = min(1.0, ECP.q_nominal(kd, h) * ratio[i])
            cnt += hit
            mu += q
            var += q * (1.0 - q)
        if usable and var > 0:
            ss += (cnt - mu) ** 2
            vv += var
    return ss / vv if vv > 0 else float("nan")


def cell_index(group):
    """This rig's own reference at the cap: the index against the
    field's leave-one-out (kind, fine bin) cell q's -- the q's the
    survival model integrates -- summed to the last prime."""
    ss = vv = 0.0
    for f in group:
        cnt = mu = var = 0.0
        for (p, hit), q in zip(f["splits"], f["qs"]):
            cnt += hit
            mu += q
            var += q * (1.0 - q)
        if var > 0:
            ss += (cnt - mu) ** 2
            vv += var
    return ss / vv if vv > 0 else float("nan")


# ------------------------------------------------------------ evaluation

def evaluate(group):
    """The imported evaluation plus the index-unit ratios."""
    r = FHS.evaluate_group(group, CAP, NSCALE)
    r["iratio_1"] = r["meas_idx"] / r["nstar"]
    r["iratio_d"] = r["meas_idx"] / r["nstar_d"]
    return r


def sd(xs):
    xs = [x for x in xs if x == x]
    if len(xs) < 2:
        return float("nan")
    m = sum(xs) / len(xs)
    return sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def boot_group(group, rng, nboot):
    """Paired bootstrap over fields, the density fixed: sd of the
    index-unit and p-unit ratios, derived and independent, and of the
    per-scale deficit-minus-phi."""
    acc = {"iratio_1": [], "iratio_d": [], "ratio_1": [], "ratio_d": []}
    diffs = [[] for _ in range(NSHOW + 1)]
    for _ in range(nboot):
        samp = [group[rng.randrange(len(group))] for _ in group]
        r = evaluate(samp)
        for k in acc:
            acc[k].append(r[k])
        for s in r["scales"][:NSHOW]:
            diffs[s["n"]].append(s["deficit"] - s["phi"])
    out = {k: sd(v) for k, v in acc.items()}
    out["sd_scale"] = [sd(d) for d in diffs]
    return out


def combined(groups):
    """Field-weighted combination of several strata's evaluations into
    one (measured index, independent index, derived index)."""
    n = m = i1 = idd = 0.0
    for g in groups:
        if not g:
            continue
        r = evaluate(g)
        n += r["n"]
        m += r["n"] * r["meas_idx"]
        i1 += r["n"] * r["nstar"]
        idd += r["n"] * r["nstar_d"]
    return m / i1, m / idd


def boot_pooled_vs_split(recs_h3, rng, nboot):
    """One paired bootstrap over the complex h = 3 fields: each resample
    is priced and evaluated POOLED (one stratum, one density) and SPLIT
    (by regime, two densities); returns the ratios and the sd of their
    difference."""
    base = [r for r in recs_h3]
    pooled_ratios, split_ratios, diffs = [], [], []

    def both(sample):
        fp = make_fields(sample, split_regime=False)
        price(fp)
        p1, pd_ = combined([fp])
        fs = make_fields(sample, split_regime=True)
        price(fs)
        st = strata_of(fs)
        s1, sd_ = combined(list(st.values()))
        return (p1, pd_), (s1, sd_)

    (p1, pd0), (s1, sd0) = both(base)
    for _ in range(nboot):
        samp = [base[rng.randrange(len(base))] for _ in base]
        (_, a), (_, b) = both(samp)
        pooled_ratios.append(a)
        split_ratios.append(b)
        diffs.append(a - b)
    return {"pooled_1": p1, "pooled_d": pd0, "split_1": s1, "split_d": sd0,
            "sd_pooled": sd(pooled_ratios), "sd_split": sd(split_ratios),
            "sd_diff": sd(diffs)}


def regen(fields, rng):
    """C4: bits redrawn at each (stratum, kind, fine bin) cell's FULL
    share."""
    gen = {}
    for key, group in strata_of(fields).items():
        tot = {}
        for f in group:
            for (p, hit), kd in zip(f["splits"], f["kinds"]):
                ck = (kd, bin_of(p, FINE_EDGES))
                n, h = tot.get(ck, (0, 0))
                tot[ck] = (n + 1, h + hit)
        gen[key] = {ck: th / float(tn) for ck, (tn, th) in tot.items()}
    synth = []
    for f in fields:
        sp, L1 = [], None
        for (p, _), kd in zip(f["splits"], f["kinds"]):
            hit = rng.random() < gen[f["key"]][(kd, bin_of(p, FINE_EDGES))]
            sp.append((p, hit))
            if hit and L1 is None:
                L1 = p
        synth.append({"D": f["D"], "h": f["h"], "splits": sp,
                      "kinds": f["kinds"], "L1": L1, "key": f["key"]})
    return synth


# ------------------------------------------------------------------ main

def main():
    t0 = time.time()
    rng = Random(SEED)
    section("S1  THE RECORDS -- the cubic pipeline or its checkpoint")
    recs = load_records()
    n_cx = sum(1 for r in recs if r["cx"])
    print("  %d mapped fields with H > 1, %d complex; every prime decided: "
          "%s" % (len(recs), n_cx,
                  all(t[2] is not None for r in recs for t in r["verdicts"])))
    fields = make_fields(recs, split_regime=True)
    levels = price(fields)
    print("  primes priced at the fine cell %d, the coarse cell %d, the "
          "kind's stratum share %d" % tuple(levels))
    strata = strata_of(fields)
    keys = sorted(strata, key=lambda k: (k[0] != "complex", k[0], k[1], k[2]))
    print("  strata (signature, H, regime: '-' single, D degenerate, M "
          "generic) and field counts:")
    for k in keys:
        print("    %-9s H=%-2d %s  n=%3d%s"
              % (k[0], k[1], k[2], len(strata[k]),
                 "" if len(strata[k]) >= MIN_STRATUM else "  (not read)"))
    read = [k for k in keys if len(strata[k]) >= MIN_STRATUM
            and k[0] == "complex"]

    section("CONTROLS, read first")
    # C1 -- the import.
    h3 = [f for f in fields if f["key"][0] == "complex" and f["h"] == 3]
    h3D = [f for f in h3 if f["key"][2] == "D"]
    h3M = [f for f in h3 if f["key"][2] == "M"]
    ix_all, ix_D, ix_M = map_index(h3, 3), map_index(h3D, 3), map_index(h3M, 3)
    print("  [C1] complex h = 3 index on the map's reference (bin ratio "
          "onto nominal q): whole %.3f (map 1.583), D %.3f (0.220), M "
          "%.3f (0.252)" % (ix_all, ix_D, ix_M))
    print("       on this rig's (kind, fine bin) cells, the q's the model "
          "integrates, at the cap: D %.3f, M %.3f, h = 2 %.3f"
          % (cell_index(h3D), cell_index(h3M),
             cell_index([f for f in fields if f["key"] ==
                         ("complex", 2, "-")])))
    ok(abs(ix_all - 1.583) < 0.02, "whole-stratum index %.3f" % ix_all)
    ok(abs(ix_D - 0.220) < 0.02 and abs(ix_M - 0.252) < 0.02,
       "regime indices %.3f %.3f" % (ix_D, ix_M))
    # C2 -- the regular end, the engine's own control re-run.
    worst = 0.0
    for k in (2, 3, 5):
        pop = FHS.regular_population(k, 400, rng)
        nsc = 3 * k
        c2x = [1.0] * (nsc + 1)
        for n in range(1, nsc + 1):
            r_ = (n % k) / k
            c2x[n] = (r_ * (1.0 - r_)) / (n * (1.0 / k) * (1.0 - 1.0 / k))
        _, _, _, nstar_d = FHS.survival_model(pop, 10 ** 9, c2x, nsc)
        ones = [1.0] * (nsc + 1)
        _, _, _, nstar_1 = FHS.survival_model(pop, 10 ** 9, ones, nsc)
        worst = max(worst, abs(nstar_d / nstar_1 - (k + 1) / (2.0 * k)))
    print("  [C2] regular end: max |derived - (k+1)/(2k)| = %.2e at the "
          "exact index (must be < 1e-9)" % worst)
    ok(worst < 1e-9, "regular end off by %.2e" % worst)
    # C3 -- the algebra at h = 2.
    h2 = [f for f in fields if f["key"][0] == "complex" and f["h"] == 2]
    ns = nh = 0
    for f in h2:
        for (p, hit), kd in zip(f["splits"], f["kinds"]):
            if kd == "split":
                ns += 1
                nh += hit
    print("  [C3] complex h = 2: %d totally split primes, %d carrying a "
          "principal place (must be all)" % (ns, nh))
    ok(ns == nh, "%d split primes at h = 2 with no principal place"
       % (ns - nh))

    section("THE INDEX CURVE per read stratum: c^2_n at n = 1..%d (exact "
            "null sd under independent bits)" % NSHOW)
    results = {}
    for k in read:
        r = evaluate(strata[k])
        results[k] = r
        sc = r["scales"]
        row = "  ".join("%.3f" % r["c2"][n] for n in range(1, NSHOW + 1))
        zs = "  ".join("%+5.1f" % ((r["c2"][n] - 1.0) / sc[n - 1]["nullsd"])
                       if n <= len(sc) and sc[n - 1]["nullsd"] > 0
                       else "  nan" for n in range(1, NSHOW + 1))
        print("  %-7s H=%d %s (%3d)  c2: %s" % (k[0], k[1], k[2],
                                                 len(strata[k]), row))
        print("  %-22s   z: %s" % ("", zs))

    def zc(k, n):
        s = results[k]["scales"][n - 1]
        return (s["c2"] - 1.0) / s["nullsd"]
    k2 = ("complex", 2, "-")
    print("  [K4] h = 2: index at n = 1 %.3f (z %+.2f), at n = 3 %.3f "
          "(z %+.2f)" % (results[k2]["c2"][1], zc(k2, 1),
                         results[k2]["c2"][3], zc(k2, 3)))

    section("THE DERIVED FIRST HIT, INDEX UNITS (bootstrap %d over fields, "
            "density fixed)" % BOOT)
    print("  stratum              n   meas.I  indep.I  ratio    z_ind | "
          "derived.I  ratio    z_der  | clamps  n*  | p-units: meas indep "
          "derived ratios")
    boots = {}
    for k in read:
        r = results[k]
        b = boot_group(strata[k], rng, BOOT)
        boots[k] = b
        z1 = (r["iratio_1"] - 1.0) / b["iratio_1"]
        zd = (r["iratio_d"] - 1.0) / b["iratio_d"]
        print("  %-7s H=%d %s  %4d   %5.2f   %5.2f   %5.3f  %+5.2f |   "
              "%5.2f    %5.3f  %+5.2f  |  %3d   %4.1f | %6.1f %6.1f %6.1f "
              "%.3f %.3f"
              % (k[0], k[1], k[2], r["n"], r["meas_idx"], r["nstar"],
                 r["iratio_1"], z1, r["nstar_d"], r["iratio_d"], zd,
                 r["clamps"], r["nstar"], r["meas"], r["pred_1"],
                 r["pred_d"], r["ratio_1"], r["ratio_d"]))
    print("  ratio = measured / model, in the field's own index of "
          "degree-1-carrying primes (E[I] = sum S_n exactly); z = (ratio "
          "- 1) / bootstrap sd.")
    print("  [K1] independent ratio at or above 1 at any read stratum; "
          "[K2] at h = 2, |z_der| >= 2 or |z_ind| < 2.")

    section("SCALE BY SCALE at h = 2 and the two h = 3 halves: the "
            "measured survival deficit against phi_n")
    for k in read:
        if k[1] not in (2, 3):
            continue
        r = results[k]
        b = boots[k]
        print("  %s H=%d %s   n  fields   mu_n    c2_n   S_meas  S_model "
              "S_indep  deficit   phi     diff    sd     z"
              % (k[0], k[1], k[2]))
        for s in r["scales"][:NSHOW]:
            sd_ = b["sd_scale"][s["n"]]
            d = s["deficit"] - s["phi"]
            print("    %2d   %4d   %6.3f  %6.3f   %6.4f  %6.4f  %6.4f   "
                  "%6.4f  %6.4f  %+6.4f  %5.4f  %+5.2f"
                  % (s["n"], s["cnt"], s["mu"], s["c2"], s["smeas"],
                     s["smod"], s["sind"], s["deficit"], s["phi"], d, sd_,
                     d / sd_ if sd_ > 0 else float("nan")))

    section("POOLED AGAINST SPLIT at complex h = 3: one density or two "
            "(paired bootstrap %d)" % BOOT)
    recs_h3 = [r for r in recs if r["cx"] and r["H"] == 3]
    fp = make_fields(recs_h3, split_regime=False)
    price(fp)
    rp = evaluate(fp)
    print("  pooled index curve n = 1..%d: %s; at the cap %.3f"
          % (NSHOW, "  ".join("%.3f" % rp["c2"][n]
                               for n in range(1, NSHOW + 1)),
             cell_index(fp)))
    pv = boot_pooled_vs_split(recs_h3, rng, BOOT)
    diff = pv["pooled_d"] - pv["split_d"]
    z = diff / pv["sd_diff"] if pv["sd_diff"] > 0 else float("nan")
    print("  pooled (83 fields, one stratum):  independent ratio %.3f  "
          "derived ratio %.3f +- %.3f"
          % (pv["pooled_1"], pv["pooled_d"], pv["sd_pooled"]))
    print("  split  (D and M, two densities):  independent ratio %.3f  "
          "derived ratio %.3f +- %.3f"
          % (pv["split_1"], pv["split_d"], pv["sd_split"]))
    print("  pooled - split derived ratio: %+.3f, paired sd %.3f, z %+.2f"
          "   [K3] fires at |z| < 2" % (diff, pv["sd_diff"], z))

    section("[C4] THE PIPELINE UNDER ITS OWN NULL: bits regenerated at "
            "each cell's full share, %d replicates" % REPS)
    acc = {k: [] for k in read}
    curves = {k: [0.0] * (NSHOW + 1) for k in read}
    for _ in range(REPS):
        synth = regen(fields, rng)
        price(synth)
        st = strata_of(synth)
        for k in read:
            r = evaluate(st[k])
            acc[k].append((r["iratio_1"], r["iratio_d"]))
            for n in range(1, NSHOW + 1):
                curves[k][n] += r["c2"][n] / REPS
    print("  stratum              indep.ratio  derived.ratio  |diff|   "
          "c2 curve n=1..%d" % NSHOW)
    for k in read:
        a = acc[k]
        m1 = sum(x[0] for x in a) / len(a)
        md = sum(x[1] for x in a) / len(a)
        print("  %-7s H=%d %s      %.3f        %.3f        %.3f   %s"
              % (k[0], k[1], k[2], m1, md, abs(m1 - md),
                 " ".join("%.2f" % curves[k][n] for n in range(1, NSHOW + 1))))
    a = acc[k2]
    d2 = abs(sum(x[0] for x in a) / len(a) - sum(x[1] for x in a) / len(a))
    ok(d2 < 0.02, "null derived-independent gap %.3f at h = 2" % d2)

    section("SUMMARY")
    print("  %d checks, %d failed, wall %.1f s"
          % (CHECKS[0], CHECKS[1], time.time() - t0))


if __name__ == "__main__":
    main()
