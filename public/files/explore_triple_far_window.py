r"""THE LEVEL ABOVE THE SEAT -- does the all-principal event still carry
an unpaid share of the forcing at primes far above the discriminant,
or is the naive explicit formula exact there? (child of
explore_triple_image_level.py, whose walks this file re-runs on the
kept class readings with the prime cap raised from 1000 to 10000.)

THE QUESTION. A totally split prime q of a complex cubic field K
carries three places whose classes sum to zero; the all-principal event
is "all three principal", its uniform share 1/h^2. The parent reads the
UNIFORM LEVEL L_u = count / expectation over the window q < 1000 with
every prime power q^k < 1000 counted at 1/k, and the FORCING F, the
excess the powers the algebra sends to the identity put on that level;
it finds L_u - 1 = f F with f near 0.4 at every class number prime to 3,
and explore_ceiling_forcing.py finds the same f zero at degree 2 above
p = 30. Every cubic read so far sits BELOW the discriminant: the
window's primes are 3 to 1000 and the fields run to |d| = 96000. The
question is what the level reads at primes ABOVE the discriminant,
1000 <= q < 10000 over |d| <= 24000, where the forcing thins to a few
hundredths (few prime powers among many primes) and the two readings
of the near window -- the formula's exact compensation, or a fixed
unpaid fraction of the forcing -- separate on the LEVEL itself.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE OBSERVABLE IS THE LEVEL, NOT THE FRACTION. f = (L_u - 1)/F
      has bar (1/sqrt(exp_u))/F; in [1000, 10000) the forcing at h = 2
      is 0.05 (box 0's rehearsal print: F 0.048 on exp_u 1714), so f's
      bar there is 0.50 at h = 2 on box 0 and worse above, and "f
      within 2 sigma of the near band [0.33, 0.45]" is met by any f.
      L_u's own bar is 1/sqrt(exp_u): over boxes 0-3 (|d| <= 24000,
      479 fields at h = 2, 1061 odd primes in the far window against
      167 below 1000) exp_u at h = 2 is near 21000, bar 0.007, and the
      two readings sit at 1.000 and 1 + 0.39 F = 1.019, 2.7 sigma
      apart; the h >= 4 strata prime to 3 pooled separate at about 2.4
      sigma. Box 4 (|d| <= 48000) would take h = 2 to 4 sigma and the
      pool to 3.5; it is priced (31 minutes) and taken only if the read
      over boxes 0-3 lands within a sigma of a boundary.
  (2) THE PRICE IS THE PRIMES', NOT THE FIELDS'. The class map's cost
      per place does not grow with the prime (its cofactor bound is
      Minkowski's, a fact about the field), so the walk to 10000 costs
      11.5x the walk to 1000 at every box (rehearsed: box 0 92 s
      against 8 s; the six boxes' near walls 8, 12, 27, 68, 162, 417 s),
      and the class readings are the parent's checkpoints, never
      re-read. Boxes 0-3: about 22 minutes, checkpointed per box.
  (3) THE CAP HAS ONE BINDING THAT FANS OUT AS MODULE GLOBALS read at
      call time: PRIME_CAP, ODD_PRIMES and BIN_EDGES on the cubic
      principal, class-map, split-triple, cube-term and ramified-term
      rigs, BIN_EDGES on the excess-box and image-level rigs, KMAX and
      TOR_M on the image-level rig (2^13 = 8192 < 10000). The bins
      become (3, 30, 100, 300, 1000, 3000, 10000): the four bins below
      1000 are the parent's own, so the far walk must reproduce the
      near walk CELL FOR CELL in them, which is the control C1 --
      every term is filed by the bin of the prime power q^k itself,
      and a power above 1000 of a prime below it lands in a far bin
      without touching the near ones. The ramified census is the one
      structure that grows with the cap (a ramified prime between 1000
      and 10000 exists for |d| > 1000); it is printed, not compared.
  (4) WHAT THE FAR RAW LEVEL SHOULD READ. L_u - 1 = raw excess + free
      excess + F in units of exp_u. If the naive formula is exact
      (L_u = 1) and the free terms landed at their share, the raw level
      would read 1 - F; the near window's free terms land SHORT of
      their share (the parent's F3), so the raw level sits above 1 - F
      by the free deficit's share. The prediction below allows 0.1.
  (5) THE POOLED STATISTIC over the h >= 4 strata prime to 3 (all in
      the A regime): the counts, the uniform expectations and the
      forcings summed over the strata readable in the far window
      (exp_u >= MIN_READ there), L_u the ratio, F the ratio, bar
      1/sqrt(sum exp_u) -- exact, each field at its own share. The
      3 | h rows are printed on the parent's scalar regime sort and
      qualified as the parent qualifies them; nothing pooled reads
      them.
  (6) THE LINEAGE PASS rides for free. The parent's readings of boxes 2
      and 3 were made under the topband rig's cache bug (its T6, fixed
      after the parent's walks drifted by a field between processes);
      boxes 0 and 1 re-read under the fix are identical to their
      checkpoints. `--reread` re-reads a box fresh under the fix, diffs
      every field's class number, generator places and relation basis
      against the kept reading, then walks the fresh readings at the
      near cap and diffs the cells against the kept readings' near
      walk (the cheaper walk; a class number or a place that moved
      shows in either).
      The diff's size is the finding; a class number that moves would
      move the ceiling's stratum for that field.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_triple_image_level.py: the population, the boxes, the
    class readings, the three walks, the image shares, the levels and
    every bar are IMPORTED and run under rebound caps; nothing in the
    walk is rewritten. The kept readings are the parent's checkpoints.
 T2 THE NEAR BAND [0.33, 0.45] and its centre 0.39 are the parent's F2
    over p < 1000; that the fraction is a function of the window
    against the discriminant is the suspicion being read, not assumed.
 T3 THE NAIVE FORMULA's exactness above the seat is the degree-2
    reading (explore_ceiling_forcing.py F3: within 0.11 of 0 in every
    real bin above 30) transplanted to degree 3; it is one of the two
    frozen readings, not a prior.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE KILL-SHAPE, printed: L_u over [1000, 10000) pooled over the
      boxes walked sits within 2 sigma of 1 + 0.39 F AND more than 2
      sigma above 1, at h = 2 and at the pooled h >= 4 strata prime to
      3, both. That KILLS: the event carries its unpaid fraction at
      every window, above the seat as below it.
  P2  PREDICTED: L_u over [1000, 10000) within 2 sigma of 1 at h = 2
      and at the pooled h >= 4; the raw level (no powers) within 0.1
      of 1 - F at both. The naive formula is exact above the seat, as
      it is at degree 2 above 30, and the near window's fraction is
      the seat's.
  P3  THE THIRD SHAPE, named so it is not read as either: L_u more
      than 2 sigma BELOW 1 at either read. Box 0's rehearsal print
      sits there at h = 4 (0.846 on exp_u 66) and h = 5 (0.853 on 56)
      inside their bars; if the pool confirms it the raw primes are
      short of 1/h^2 above the seat by more than the forcing pays,
      and the deficit is not the seat's.
  P4  THE TWO FAR BINS AGREE: at h = 2, L_u in [1000, 3000) and in
      [3000, 10000) within 2 sigma of each other.
  P5  REPRODUCTION (C1): the far walk's four bins below 1000 equal the
      near walk's cell for cell in every box, and the near-window f at
      h = 2 by box reprints the parent's F5 (0.20, 0.22, 0.27, 0.38 at
      boxes 0-3) within 0.005 through the rebound bins.

THE CONTROLS, run before any prediction is read.

  C0  THE BINDINGS: after the rebinding every module named in (3)
      reads PRIME_CAP 10000, 1228 odd primes, seven bin edges; the
      powers of 2 run to 2^13 and 1024 files in the fifth bin.
  C1  REPRODUCTION as P5.
  C2  THE POSITIVE CONTROL: over the near window [3, 1000) and the
      same boxes the instrument reads L_u more than 2 sigma above 1
      at h = 2 with f in [0.15, 0.45] -- the known non-zero fraction
      detected by the same code path that reads the far window. It
      binds where a fraction 0.2 would show at 2 sigma (0.2 F / bar
      > 2), which one box alone does not give; a rehearsal on box 0
      prints it unbound.
  C3  THE PARENT'S OWN CHECKS per box (its C5) clean on the far walk;
      the map's-order census (its C6) identical to the near walk's.

THE DESIGN. S0 the rebinding and C0. S1 the population (the parent's
checkpoint). S2 per box: the kept readings loaded, the near walk
loaded or made (the parent's checkpoint), the far walk loaded or made
(this file's checkpoint), C1 and C3. S3 the table: every readable
stratum's near read beside its far read (L_u with its bar, F, f, the
raw level, the image level), the pooled h >= 4, h = 2 by box and by
far bin, C2. S4 the verdict, P1-P4. S5 `--reread`: the lineage pass of
(6) on the named boxes. Flags: `--far-cap N` (10000), `--boxes a,b,..`
(0,1,2,3), `--ckpt DIR` (beside the system temp), `--reread a,b,..`
(none), `--fresh`.

FINDINGS. Boxes 0-3, 3849 complex fields to |d| <= 24000, 1285 with
h > 1 (481 at h = 2), the kept readings completed by the forced
relations (the parent's (9); the completion moved four class numbers
here, d = -6791, -10015, -10187, -10355, each halved, LMFDB agreeing
at the three it lists). C0 held: 1228 odd primes, 1061 in the far
window, the powers of 2 to 2^13, 1024 in the fifth bin. C1: every
box's far walk equals its near walk cell for cell in the four bins
below 1000, the far walls 93, 140, 312, 758 s against 8, 12, 26, 67
(11.1x to 12.0x, the class map's price the population's). C3 clean in
every box, the map's-order census identical to the near walk's (one
field, d = -13484, in box 3). P5: the near-window f at h = 2 by box
reprints 0.200, 0.223, 0.269, 0.377 against the parent's 0.20, 0.22,
0.27, 0.38. C2 bound and held: the near window at h = 2 reads 1.099
+- 0.016 (z +6.0), f 0.32, a fraction 0.2 showing at 3.8 sigma.

  F1. THE KILL FIRES: THE LEVEL AT PRIMES COMPARABLE TO THE
      DISCRIMINANT IS 1 + 0.39 F AT BOTH READS (observation; P1 holds,
      P2 and P3 fail). Over 1000 <= q < 10000 and |d| <= 24000 the
      uniform level reads 1.020 +- 0.007 at h = 2 (F 0.050), 2.9 sigma
      above 1 and 0.1 sigma from 1 + 0.39 F = 1.0195, and 1.066 +-
      0.022 pooled over h = 4, 5, 7, 8, 10, 11 (exp_u 2133, F 0.170),
      3.0 sigma above 1 and 0.0 sigma from 1.0665. The uncompensated
      fraction there is f = 0.40 +- 0.14 at h = 2 and 0.38 +- 0.13
      pooled, the near window's 0.32 and 0.20 over the same boxes (0.4
      at every stratum over all six). The window is above the seat's
      least places and of the discriminant's order, not far above it:
      only box 0 (|d| <= 3000) reads q >> |d|, at 0.996 +- 0.024, one
      sigma from either reading, and the next decade of primes over
      boxes 0-1 would carry (a hand count of its prime powers against
      its primes, not a run) a forcing near 0.014 against a bar near
      0.006, undecisive; the q >> |d| regime needs the level to 0.001
      or another object. What is decided: at degree 3 the naive
      explicit formula is 40 % short of the forcing at every window
      read, below and at the discriminant, where at degree 2 it is
      exact above p = 30.
  F2. THE RAW PRIMES' SHORTFALL IS THE SAME SHARE OF THE FORCING IN
      BOTH WINDOWS (observation). The raw level, no powers, reads
      0.978 at h = 2 against 1 - F = 0.950 and 0.936 pooled against
      0.830: the raw primes are short of 1 by 0.022 and 0.064, 0.44
      and 0.38 of the forcing, where below 1000 they are short by 0.14
      and 0.43, 0.45 and 0.40 of a forcing six times larger (0.311
      and 1.070). The share the raw primes fail to pay is the
      invariant; f differs between the windows (0.32 and 0.20 near,
      0.40 and 0.38 far) by the free terms' deficit, large below 1000
      and small above it. By
      stratum the far level reads 1.108 +- 0.028, 1.000 +- 0.039,
      0.909 +- 0.086, 1.167 +- 0.124, 1.266 +- 0.245, 1.174 +- 0.307
      at h = 4, 5, 7, 8, 10, 11 (F 0.14 to 0.53); the 3 | h rows on the
      scalar sort read 0.996, 1.001, 1.676 at h = 3, 6, 9.
  F3. THE TWO FAR BINS AGREE AND THE BOXES AGREE (observation; P4
      holds). At h = 2, [1000, 3000) reads 1.010 +- 0.014 and [3000,
      10000) 1.023 +- 0.008, 0.9 sigma apart; by box 0.996, 1.021,
      1.023, 1.022 (bars 0.024 to 0.009), the far f -0.09, 0.41, 0.48,
      0.43 against the near 0.20, 0.22, 0.27, 0.38.
  F4. THE LINEAGE PASS (observation; S5). The first fresh re-read of
      box 2 under the seeded harvest moved ONE class number, d = -9251,
      from 2 to 6 -- and LMFDB reads 2: the seed had let the rung
      ladder stop early on a representative whose bare harvest is
      rank-deficient at two rungs (the shop's bare_order, the ladder's
      stop rule since). Under the fixed ladder the fresh re-reads of
      boxes 2 and 3 (901 and 1816 fields with a lattice) move no class
      number, the near walks from them equal the kept readings' walks
      cell for cell, and every stratum's level reprints to the digit;
      the bases differ at 66 and 110 fields (the same lattices, other
      rows), the generator columns at 2 fields of box 3 read through
      another representative, the attestation tags at 2. The cache
      bug's rate over these 2717 fields is zero; boxes 4 and 5 (12461
      fields, 100 minutes) were not re-read and stay completed by the
      seed on load.

RUN RECORD. 2026-09-07, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_triple_far_window.py
--boxes 0,1,2,3 --reread 2,3`. Rehearsed on box 0 alone (93 s, 37 MB).
The first full run died at box 2 on the parent's zero-sum count (2
split-prime cubes off zero, the two fields whose lattice lacked a
forced relation), which is how the completion (9) was found; the
second ran 2113 s, peak 84 MB, with the readings completed, and read
d = -9251 at 6 in the lineage pass; the third, under the fixed stop
rule, is the record: 921 s (the far walks loaded, the re-reads 229 and
596 s), peak 85 MB, 42 checks here and 3176 in the parent's walks.
"""
import gc
import json
import math
import os
import sys
import tempfile
import time


def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


FAR_CAP = int(_flag("--far-cap", 10000))
BOXES_RUN = [int(x) for x in _flag("--boxes", "0,1,2,3").split(",")]
REREAD = [int(x) for x in _flag("--reread", "").split(",") if x]
CKPT = _flag("--ckpt", os.path.join(tempfile.gettempdir(),
                                    "far_window_%d" % FAR_CAP))
FRESH = "--fresh" in sys.argv
_ARGV = sys.argv
sys.argv = [_ARGV[0]]                    # the parent at its own defaults
import explore_triple_image_level as IL         # noqa: E402
sys.argv = _ARGV

EB, TB, CCM, ECP, ST, CT, RT = (IL.EB, IL.TB, IL.CCM, IL.ECP, IL.ST,
                                IL.CT, IL.RT)
BOXES = IL.BOXES
MIN_READ = IL.MIN_READ
NEAR_EDGES = ECP.BIN_EDGES                              # (3, 30, 100, 300, 1000)
FAR_EDGES = NEAR_EDGES + (3000, FAR_CAP)
NEAR_BINS = tuple(range(len(NEAR_EDGES) - 1))
FAR_BINS = tuple(range(len(NEAR_EDGES) - 1, len(FAR_EDGES) - 1))
F5 = (0.20, 0.22, 0.27, 0.38)                           # the parent's F5, boxes 0-3
CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)


def section(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def fmt(x, d=3):
    return "--" if x is None else "%.*f" % (d, x)


def fz(z):
    return "--" if z is None else "%+.1f" % z


# ------------------------------------------------------ the binding (3)
def bind(cap):
    """One cap, fanned out to every module global read at call time."""
    primes = [p for p in ECP.CR._sieve(cap) if p != 2]
    edges = NEAR_EDGES if cap == NEAR_EDGES[-1] else FAR_EDGES
    for M in (ECP, CCM, ST, CT, RT):
        M.PRIME_CAP = cap
        M.ODD_PRIMES = primes
        M.BIN_EDGES = edges
    EB.BIN_EDGES = edges
    IL.BIN_EDGES = edges
    kmax = 1
    while 2 ** (kmax + 1) < cap:
        kmax += 1
    IL.KMAX = kmax
    IL.TOR_M = tuple(range(1, kmax + 1))
    return primes, edges, kmax


def s0_bindings():
    section("S0  THE BINDINGS -- the cap fanned out, C0")
    primes, edges, kmax = bind(FAR_CAP)
    for M in (ECP, CCM, ST, CT, RT):
        ok(M.PRIME_CAP == FAR_CAP and M.ODD_PRIMES is primes
           and M.BIN_EDGES is edges, "C0: %s not rebound" % M.__name__)
    ok(EB.BIN_EDGES is edges and IL.BIN_EDGES is edges, "C0: bins")
    ok(IL.KMAX == kmax and IL.TOR_M == tuple(range(1, kmax + 1)), "C0: KMAX")
    pw = CT.powers(2)
    print("  cap %d: %d odd primes, %d in [1000, %d); bins %s; powers of 2 "
          "to 2^%d, 1024 in bin %d; KMAX %d"
          % (FAR_CAP, len(primes), sum(1 for p in primes if p >= 1000),
             FAR_CAP, edges, pw[-1][0], CT.bin_of(1024), IL.KMAX))
    if FAR_CAP == 10000:
        ok(len(primes) == 1228 and pw[-1][0] == 13 and CT.bin_of(1024) == 4,
           "C0: the prime count, the power depth or the bin of 1024")
    bind(NEAR_EDGES[-1])
    ok(CT.PRIME_CAP == 1000 and len(CT.ODD_PRIMES) == 167
       and IL.KMAX == 9, "C0: the near rebinding")
    print("  near rebinding restored: cap 1000, 167 odd primes, KMAX 9")


# ----------------------------------------------------------- the walks
def cells_below(data, bins):
    """The per-stratum, per-bin tables restricted to the named bins."""
    out = {}
    for f in ('un', 'ram', 'img'):
        out[f] = dict((k, dict((bb, c) for bb, c in v.items()
                               if int(bb) in bins))
                      for k, v in data[f].items())
    out['nfields'] = data['nfields']
    out['disagree'] = data.get('disagree', [])
    return json.loads(json.dumps(out))


def walk_at(cap, bi, readings):
    bind(cap)
    data = IL.walk_box(bi, readings)
    bind(NEAR_EDGES[-1])
    return json.loads(json.dumps(data))


def s2_boxes(fields):
    section("S2  THE WALKS -- the kept readings, near and far, C1 and C3")
    near, far = [], []
    for bi in BOXES_RUN:
        rpath = os.path.join(IL.CKPT, "readings%d.json" % bi)
        ok(os.path.exists(rpath), "no kept readings for box %d at %s"
           % (bi, rpath))
        R = IL.load_readings(bi)
        npath = os.path.join(IL.CKPT, "walk%d.json" % bi)
        if os.path.exists(npath) and not FRESH:
            dn = json.load(open(npath))
            print("  box %d near walk loaded (%.0f s when run)"
                  % (bi, dn['wall']))
        else:
            dn = walk_at(NEAR_EDGES[-1], bi, R['readings'])
            json.dump(dn, open(npath, "w"))
        fpath = os.path.join(CKPT, "far%d.json" % bi)
        if os.path.exists(fpath) and not FRESH:
            df = json.load(open(fpath))
            print("  box %d far walk loaded (%.0f s when run)"
                  % (bi, df['wall']))
        else:
            df = walk_at(FAR_CAP, bi, R['readings'])
            if not os.path.isdir(CKPT):
                os.makedirs(CKPT)
            json.dump(df, open(fpath, "w"))
        for ck in ('c3_bad', 'c4_disagree', 'c4map_disagree', 'c5_bad',
                   'bad_sum'):
            ok(df['checks'][ck] == 0, "box %d far: %s = %d"
               % (bi, ck, df['checks'][ck]))                      # C3
        same = cells_below(dn, NEAR_BINS) == cells_below(df, NEAR_BINS)
        print("  [C1] box %d: the far walk's bins below 1000 equal the near "
              "walk cell for cell: %s; near/far walls %.0f / %.0f s "
              "(%.1fx)" % (bi, same, dn['wall'], df['wall'],
                           df['wall'] / max(dn['wall'], 1e-9)))
        ok(same, "C1: box %d differs below 1000" % bi)
        print("  [C3] box %d far: lift relations %d hold, types %d agree; "
              "map's order differs from the reading's at %d fields, same "
              "list as near: %s"
              % (bi, df['checks']['c3_ok'], df['checks']['c4_agree'],
                 len(df.get('disagree', [])),
                 df.get('disagree', []) == dn.get('disagree', [])))
        cn = sum(sum(c['n'] for c in cs.values())
                 for cs in dn['census'].values())
        cf = sum(sum(c['n'] for c in cs.values())
                 for cs in df['census'].values())
        print("        ramified census near %d, far %d places (grows with "
              "the cap, not compared)" % (cn, cf))
        near.append(dn)
        far.append(df)
    return near, far


# ----------------------------------------------------------- the reads
def read(boxes, key, bins):
    """The parent's levels under the far bins: L_u with its bar, F, f,
    the raw level, the image level, over the named bins."""
    bind(FAR_CAP)
    L = IL.levels(boxes, key, bins=bins)
    bind(NEAR_EDGES[-1])
    if L is None:
        return None
    L['bar'] = 1.0 / math.sqrt(L['exp_u'])
    return L


def pooled(boxes, keys, bins):
    """(5): the strata's counts, expectations and forcings summed."""
    count = exp_u = forcing = n3 = exp_raw = 0.0
    for key in keys:
        L = read(boxes, key, bins)
        if L is None:
            continue
        count += L['count']
        exp_u += L['exp_u']
        forcing += L['g']['forcing']
        n3 += L['n3']
        exp_raw += L['ns'] * CT.share_of(*key)
    if exp_u <= 0:
        return None
    lu = count / exp_u
    F = forcing / exp_u
    bar = 1.0 / math.sqrt(exp_u)
    return dict(lu=lu, bar=bar, F=F, f=(lu - 1) / F if F > 0 else None,
                sf=bar / F if F > 0 else None, lr=n3 / exp_raw,
                exp_u=exp_u, count=count, zu=(lu - 1) / bar)


def row(L):
    if L is None:
        return "%-44s" % "--"
    return ("%.3f+-%.3f(%s) F %.3f f %s raw %.2f img %.2f"
            % (L['lu'], L['bar'], fz(L['zu']), L['F'], fmt(L['f'], 2),
               L['lr'] if L['lr'] is not None else 0.0, L['li']))


def s3_table(far):
    section("S3  THE TABLE -- every readable stratum, near [3, 1000) beside "
            "far [1000, %d), over boxes %s" % (FAR_CAP, BOXES_RUN))
    keys = set()
    for data in far:
        keys.update(IL.key_of(k) for k in data['nfields'])
    readable, out = [], {}
    print("  stratum      near: L_u+-bar(z) F f raw img              | "
          "far: the same")
    for key in sorted(keys):
        Lf = read(far, key, FAR_BINS)
        if Lf is None or Lf['exp_u'] < MIN_READ or key[1] == 'D':
            continue
        Ln = read(far, key, NEAR_BINS)
        tag = "  " if key[0] % 3 else " *"
        print("  h=%-3d %s%s  %s | %s" % (key[0], key[1], tag, row(Ln),
                                          row(Lf)))
        out[key] = (Ln, Lf)
        if key[0] >= 4 and key[0] % 3 and key[1] == 'A':
            readable.append(key)
    print("  (* = 3 | h, the parent's scalar regime sort, qualified; not "
          "pooled)")
    print("  pooled h >= 4 prime to 3, A, readable far: %s"
          % ", ".join("h=%d" % k[0] for k in readable))
    Pn = pooled(far, readable, NEAR_BINS)
    Pf = pooled(far, readable, FAR_BINS)
    for name, P in (("near", Pn), ("far ", Pf)):
        print("    %s: L_u %.3f +- %.3f (z %s), F %.3f, f %s +- %s, raw %.3f,"
              " exp_u %.0f"
              % (name, P['lu'], P['bar'], fz(P['zu']), P['F'], fmt(P['f'], 2),
                 fmt(P['sf'], 2), P['lr'], P['exp_u']))
    print("  h = 2 by box, far window: L_u+-bar(z) F f raw img")
    for i, bi in enumerate(BOXES_RUN):
        Lf = read([far[i]], (2, 'A'), FAR_BINS)
        Ln = read([far[i]], (2, 'A'), NEAR_BINS)
        print("    box %d (%5d, %5d]: %s | near f %s (F5 %.2f)"
              % (bi, BOXES[bi][0], BOXES[bi][1], row(Lf), fmt(Ln['f'], 3),
                 F5[bi] if bi < len(F5) else float('nan')))
        if bi < len(F5):
            ok(abs(Ln['f'] - F5[bi]) < 0.005,
               "P5: box %d near f %.3f against F5 %.2f" % (bi, Ln['f'], F5[bi]))
    print("  [P5] the near-window f at h = 2 by box reprints the parent's F5 "
          "within 0.005 through the rebound bins")
    print("  h = 2 by far bin:")
    bins2 = {}
    for bb in FAR_BINS:
        L = read(far, (2, 'A'), (bb,))
        bins2[bb] = L
        print("    [%5d, %5d): %s" % (FAR_EDGES[bb], FAR_EDGES[bb + 1], row(L)))
    L2n = read(far, (2, 'A'), NEAR_BINS)
    power = 0.2 * L2n['F'] / L2n['bar']        # sigmas a fraction 0.2 shows at
    held = L2n['zu'] > 2 and 0.15 <= L2n['f'] <= 0.45
    print("  [C2] positive control, near window h = 2: L_u %.3f +- %.3f (z %s),"
          " f %.3f: above 1 by > 2 sigma and f in [0.15, 0.45]: %s (a "
          "fraction 0.2 shows at %.1f sigma here; the control binds above 2)"
          % (L2n['lu'], L2n['bar'], fz(L2n['zu']), L2n['f'], held, power))
    ok(power < 2 or held, "C2 fails with the power to detect 0.2 F")
    return out, Pf, bins2


def s4_verdict(out, Pf, bins2):
    section("S4  THE VERDICT -- P1-P4 on the far window [1000, %d)" % FAR_CAP)
    L2 = out[(2, 'A')][1]
    reads = (("h = 2", L2), ("pooled h >= 4", Pf))
    for name, L in reads:
        zk = (L['lu'] - (1 + 0.39 * L['F'])) / L['bar']
        z1 = L['zu']
        print("  %-14s L_u %.4f +- %.4f: from 1 %s sigma, from 1 + 0.39 F = "
              "%.4f %s sigma; raw %.3f against 1 - F = %.3f"
              % (name, L['lu'], L['bar'], fz(z1), 1 + 0.39 * L['F'], fz(zk),
                 L['lr'], 1 - L['F']))
    kill = all(abs((L['lu'] - (1 + 0.39 * L['F'])) / L['bar']) <= 2
               and L['zu'] > 2 for _n, L in reads)
    pred = all(abs(L['zu']) <= 2 and abs(L['lr'] - (1 - L['F'])) <= 0.1
               for _n, L in reads)
    third = any(L['zu'] < -2 for _n, L in reads)
    print("  P1 the kill-shape (within 2 sigma of 1 + 0.39 F and > 2 sigma "
          "above 1, both reads): %s" % kill)
    print("  P2 predicted (within 2 sigma of 1, raw within 0.1 of 1 - F, "
          "both reads): %s" % pred)
    print("  P3 the third shape (more than 2 sigma below 1 at either "
          "read): %s" % third)
    a, b = bins2[FAR_BINS[0]], bins2[FAR_BINS[1]]
    gap = (b['lu'] - a['lu']) / math.sqrt(a['bar'] ** 2 + b['bar'] ** 2)
    print("  P4 the two far bins at h = 2: %.3f and %.3f, apart by %s sigma:"
          " %s" % (a['lu'], b['lu'], fz(gap), abs(gap) <= 2))
    print("  -> %s" % ("KILL: the event carries its fraction at every "
                       "window" if kill else
                       "the prediction holds: the naive formula is exact "
                       "above the seat" if pred else
                       "THE THIRD SHAPE: the level sits below 1 above the "
                       "seat" if third else
                       "none of the three shapes as frozen; read the table"))


# --------------------------------------------------- the lineage pass (6)
def s5_reread(fields, near):
    if not REREAD:
        return
    section("S5  THE LINEAGE PASS -- boxes %s re-read under the cache fix"
            % REREAD)
    for bi in REREAD:
        rpath = os.path.join(IL.CKPT, "readings%d.json" % bi)
        kept = IL.load_readings(bi)
        path = os.path.join(CKPT, "reread%d.json" % bi)
        if os.path.exists(path) and not FRESH:
            R2 = json.load(open(path))
            print("  box %d re-read loaded (%.0f s when read)" % (bi, R2['wall']))
        else:
            R2 = IL.read_box_readings(bi, fields)
            if not os.path.isdir(CKPT):
                os.makedirs(CKPT)
            json.dump(R2, open(path, "w"))
        K = dict((s[0], s) for s in kept['readings'])
        N = dict((s[0], s) for s in R2['readings'])
        dh, dgp, drel, dtag = [], [], [], 0
        for d, s in K.items():
            t = N.get(d)
            if t is None:
                dh.append((d, s[5], None))
                continue
            if s[5] != t[5]:
                dh.append((d, s[5], t[5]))
            if [list(g[:3]) for g in s[7]] != [list(g[:3]) for g in t[7]]:
                dgp.append(d)               # (q, e, f) per column
            if s[8] != t[8]:
                drel.append(d)
            if s[9] != t[9]:
                dtag += 1
        print("  box %d: %d kept, %d fresh; excluded kept %s fresh %s"
              % (bi, len(K), len(N), kept['excluded'], R2['excluded']))
        print("    class numbers differing: %d %s" % (len(dh), dh[:10]))
        print("    generator places differing: %d %s; relation bases "
              "differing: %d %s; attestation tags differing: %d"
              % (len(dgp), dgp[:6], len(drel), drel[:6], dtag))
        i = BOXES_RUN.index(bi) if bi in BOXES_RUN else None
        if i is None:
            continue
        dn2 = walk_at(NEAR_EDGES[-1], bi, R2['readings'])
        dn = near[i]
        same_all = (cells_below(dn2, NEAR_BINS) == cells_below(dn, NEAR_BINS))
        diffs = []
        for f in ('un', 'ram', 'img'):
            for k in set(dn2[f]) | set(dn[f]):
                for bb in set(dn2[f].get(k, {})) | set(dn[f].get(k, {})):
                    if dn2[f].get(k, {}).get(bb) != dn[f].get(k, {}).get(bb):
                        diffs.append((f, k, bb))
        print("    the near walk from the fresh readings equals the kept "
              "readings' near walk cell for cell: %s; differing cells %d %s"
              % (same_all, len(diffs), diffs[:8]))
        for key in sorted(set(IL.key_of(k) for k in dn['nfields'])):
            a = read([dn], key, NEAR_BINS)
            b = read([dn2], key, NEAR_BINS)
            if a is None or b is None or a['exp_u'] < MIN_READ:
                continue
            print("    h=%-3d %s kept L_u %.4f (n %d) fresh %.4f (n %d)"
                  % (key[0], key[1], a['lu'], dn['nfields'][IL.key_str(key)],
                     b['lu'], dn2['nfields'].get(IL.key_str(key), 0)))


def main():
    t0 = time.time()
    s0_bindings()
    fields = EB.s1_population()
    near, far = s2_boxes(fields)
    out, Pf, bins2 = s3_table(far)
    s4_verdict(out, Pf, bins2)
    s5_reread(fields, near)
    del fields
    gc.collect()
    section("SUMMARY")
    print("  %d checks passed here, %d in the parent's walks, %.1f s wall "
          "this process; far walls %s"
          % (CHECKS, IL.CHECKS, time.time() - t0,
             ["%.0f" % d['wall'] for d in far]))


if __name__ == "__main__":
    main()
