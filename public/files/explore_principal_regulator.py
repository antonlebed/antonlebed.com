"""Does the REGULATOR grade the small-p principal deficit, where the cycle
LENGTH did not?

THE QUESTION.  Over a real quadratic field the share of small split primes
that are principal falls short of the uniform 1/h+, and the LEVEL of that
shortfall is graded by |D| at fixed h+ (explore_principal_scale.py).  No
mechanism has survived.  The one derived candidate was the principal
cycle's LENGTH l: a reduced indefinite form has |a| < sqrt(D), so a small
principal prime must appear as a leading coefficient somewhere in the
principal cycle, and the pool of available small principal primes is
therefore sized by that cycle.  Terciles of l taken WITHIN a band -- which
is what holds |D| fixed enough to be a control rather than a relabelling
of the band -- refuted it: -0.031 +/- 0.014 at h+ = 2, the wrong sign, and
+0.031 +/- 0.025 and +0.051 +/- 0.048 at h+ = 4 and 8, neither reaching
1.3 standard errors.

That refutation killed a COUNT.  The theory names a SIZE.  A count of
cycle entries is not the regulator; the regulator is a sum of LOGARITHMS
over them, and the two come apart exactly where the cycle visits small
leading coefficients -- which is the pool the mechanism was about.  This
rig redoes the identical within-band tercile contrast on the regulator.

THE ACCUMULATION, DERIVED ON PAPER BEFORE ANY ENGINE CODE.  Shanks's
distance increments by

    delta_i = (1/2) log |(b_i + sqrt(D)) / (b_i - sqrt(D))|

at the step rho(f_i), for f_i = (a_i, b_i, c_i) reduced.  A reduced
indefinite form has 0 < b < sqrt(D), so the quotient is negative and the
absolute value is (sqrt(D) + b) / (sqrt(D) - b).  Rationalize:

    (sqrt(D)+b)/(sqrt(D)-b) = (sqrt(D)+b)^2 / (D - b^2) = (sqrt(D)+b)^2 / (-4ac)

using D = b^2 - 4ac, and -4ac > 0 because ac < 0 for an indefinite reduced
form.  Hence

    delta_i = log( (sqrt(D) + b_i) / (2 sqrt(|a_i| |c_i|)) ).

Summed around the CLOSED cycle the a and c ledgers telescope, rho sending
(a, b, c) to (c, b', c') so that c_i = a_{i+1} and the two multisets
coincide:

    R_cyc = sum_i delta_i = sum_i log( (sqrt(D) + b_i) / (2 |a_i|) ).

That last form is the one to code, and it is NOT the naive
log((sqrt(D)+b)/|a|) -- the factor of 2 per step is a whole l*log(2) of
regulator, which at l ~ 235 is ~163, larger than the regulator itself.
Every term is positive: reduced means |sqrt(D) - 2|a|| < b < sqrt(D), so
sqrt(D) + b > 2|a| whether or not 2|a| exceeds sqrt(D).

WHICH REGULATOR THIS IS, AND WHY IT IS THE ONE THAT PAIRS WITH h+.  The
form cycle is a NARROW object, so R_cyc is expected to be the narrow
regulator R+ = log(eps+) with eps+ the fundamental totally positive unit:
R+ = R when N(eps) = +1 and 2R when N(eps) = -1, against h+ = 2h and h+ = h
respectively.  Either way h+ R+ = 2 h R = 2 sqrt(D) L(1, chi) by the class
number formula.  So AT FIXED h+ the regulator is sqrt(D) L(1, chi) up to a
constant, and a within-band tercile of it is a tercile of L(1, chi) up to
the band's own factor-of-two spread in sqrt(D) -- which K4 removes by
re-cutting on R+/sqrt(D).  This is not an aside: L(1, chi) is the same
function the character-basis reading of this deficit already sits on.

WHY THE SIZE COULD GRADE WHAT THE COUNT DID NOT.  Writing the per-step
term as log(sqrt(D) + b_i) - log(2|a_i|), the regulator at FIXED l is
larger exactly when the cycle's leading coefficients are SMALLER on
average.  Small |a| is the pool the refuted mechanism was reaching for and
never measured: l counts the cycle's entries, R+ weights them by how small
they are.  So the mechanism's prediction survives translation into the
right statistic, and it predicts the same SIGN it predicted for l.

PREDICTIONS, FIXED BEFORE THE RUN.

  P1  THE CONTROL.  R_cyc equals log(eps) when N(eps) = +1 and 2 log(eps)
      when N(eps) = -1, to 1e-9 relative, at every control field whose
      Pell minimal solution is found inside the search bound.  Pell is
      solved by brute force over y in integers -- an independent route
      that touches no form machinery.  A second control checks the
      analytic identity h R = -sum_{a<D} chi(a) log sin(pi a / D) at small
      D, which touches neither forms nor Pell.  (That identity as written
      here is short by a factor of two -- see the findings; the slate is
      left as it was called.)  Neither control is
      diagnostic of the question; they decide whether the accumulation is
      the regulator at all, and they are read BEFORE any contrast.

  P2  R+ AND l ARE NOT THE SAME STATISTIC.  Within a band at fixed h+ the
      Spearman correlation of R+ with l is high but short of 1 -- called
      at 0.60 to 0.95.  If it prints above 0.98 the contrast below is the
      refuted one re-run and nothing is learned either way; that is a
      reason to distrust a SURVIVAL, not a kill, and it is called here so
      it cannot be called after.

  P3  THE READING.  The within-band top-minus-bottom tercile contrast on
      R+, pooled over bands exactly as the l contrast was pooled, is
      POSITIVE and reaches 2 standard errors at one or more of
      h+ = 2, 4, 8.

  P4  R+/sqrt(D) AGREES.  The same contrast cut on R+/sqrt(D), which
      removes the residual sqrt(D) spread inside a band, agrees in SIGN
      with P3 at every h+ where both print.

  P5  THE PLACEBO IS NULL.  The same machinery cut on a per-field
      pseudo-random key prints a pooled contrast inside 1 standard error
      at every h+.

THE KILL, NAMED AS WHAT THE RIG PRINTS AND NOT AS WHAT IT WOULD MEAN.
K3's pooled contrast prints below 2.0 standard errors at EACH of
h+ = 2, 4, 8, AND the three pooled signs are not all equal.  If that is
what prints, the regulator grades the deficit no better than the count
did.  If instead a pooled contrast clears 2 standard errors with the
signs agreeing across the three strata, the mechanism survives in sign
and the size is whatever K3 prints.

THE ARMS ARE RUN ON ONE FIELD SET.  The l contrast is recomputed here on
the identical rows rather than quoted from the earlier rig, because the
comparison between the count and the size is the whole point and two
populations would decide it by themselves.  Its agreement with the
published figures is itself a pin on this rig.

THE STATISTIC CONTRASTED is the bottom decade's ratio -- principal split
primes at p <= 100 over split primes at p <= 100, times h+ -- which is
the same cell the l contrast used.

SCOPE.  Real fundamental discriminants only; a definite class is a single
reduced form and has no cycle, so there is no regulator at D < 0.  Five
geometric bands spanning 512x, the same sampling stride and the same NMIN
and MINF gates as the scale rig.  NF = 1200 per band is a CEILING and not
a count: the 2000-4000 band is only 2000 wide and holds 609 fundamental
discriminants, so it is swept WHOLE while the other four are sampled.
Every per-cell population at the smallest band is correspondingly thinner,
which is worth carrying into any reading of that column.

FINDINGS.

THE CONTROLS PASS AND THEY BOTH TAUGHT SOMETHING.  P1 holds exactly:
R_cyc / log(eps) prints 2.00000 at every N(eps) = -1 control field and
1.00000 at every N(eps) = +1 one, over the fundamental discriminants
5 < D < 400 whose Pell solution is inside the bound -- so the
accumulation is the NARROW regulator, as derived.  The analytic arm
first printed exactly 2.00000 everywhere, a CONSTANT and not a scatter,
which is the shape that says convention: the sum over a = 1..D-1 double
counts under a <-> D-a, chi(D-a) = chi(a) and sin(pi(D-a)/D) =
sin(pi a/D) at D > 0.  With the half restored it prints 1.00000 at every
field.  A control read as a pass/fail bit would have thrown away the
diagnosis; the number said where the factor was.

P2 FAILED, AND ITS FAILURE IS THE FINDING.  Spearman(R+, l) within a band
at fixed h+ runs 0.793 to 0.999 over the nineteen printed cells, and the
LOW END is quoted first because it is the only cell that does not support
the reading: h+ = 8 at the smallest band, on 55 fields.  Eighteen of the
nineteen sit at 0.939 or above and eleven at 0.98 or above -- against the
0.60 to 0.95 called before the run, and above the 0.98 named in advance
as the level at which the contrast is the refuted one re-run.  The
correlation TIGHTENS with |D| at every h+: 0.980, 0.987, 0.995, 0.996,
0.999 across the lever at h+ = 2 and 0.793, 0.939, 0.960, 0.979, 0.983 at
h+ = 8, so the one dissenting cell is the smallest-|D| corner and not a
stratum -- and it is also the THINNEST cell in the table, 55 fields, that
band being the one the sampler exhausts rather than samples.  K7 measures why: the MEAN STEP R+/l concentrates, its
coefficient of variation falling 0.184, 0.131, 0.080, 0.058, 0.040 across
the lever at h+ = 2 and 0.451 to 0.102 at h+ = 8, the mean settling by
the top band on 1.194 and 1.198 at h+ = 2 and 4 and on the higher 1.262
and 1.241 at h+ = 6 and 8 -- concentrated everywhere, on a level that is
not yet common across the strata.
The per-step distance is asymptotically a constant, so within a band the
regulator IS the cycle length scaled, and the size and the count are not
two statistics here.  (That 1.19 sits near the Levy constant
pi^2/(12 log 2) = 1.1866 without being it; noted, not claimed.)

SO THE MECHANISM IS REFUTED, AND IT IS REFUTED IN ITS OWN TERMS RATHER
THAN BY A SECOND NULL.  P3 fails: the pooled R+ contrast is
-0.031 +/- 0.014 at h+ = 2 -- 2.2 standard errors and the WRONG SIGN
against a prediction of positive -- then +0.021 +/- 0.025 at h+ = 4 and
-0.005 +/- 0.049 at h+ = 8.

AND THE FROZEN KILL DID NOT COVER THAT OUTCOME, which is recorded rather
than quietly reinterpreted.  P3 called SURVIVAL as positive and at least
2 standard errors; the kill called DEATH as under 2 standard errors at
each of h+ = 2, 4, 8 with the signs disagreeing.  What printed is 2.2
standard errors NEGATIVE at h+ = 2, which satisfies neither -- the two
conditions were written as if the only significant result available were
a favourable one, so a significant contrary one falls in the gap between
them.  The verdict is unaffected and is if anything the stronger reading:
a prediction of positive met by a significant negative is refuted harder
than by a null.  The defect is in the CRITERION, not the result, and its
shape is general -- a kill and its survival clause must PARTITION the
outcomes, and naming a sign in one of them without naming it in the other
is how the gap opens.  P4 holds and buys nothing: cutting on
R+/sqrt(D) gives -0.020, +0.011, -0.011 at those same strata, so the
band's residual sqrt(D) spread was never what was hiding a signal.  The
one cell clearing 2 standard errors positively is h+ = 6 at
+0.262 +/- 0.072, and it is the cell this corpus already reads as noise:
its four bands run +0.345, +0.452, -0.450, +0.514 on 35 to 48 fields
each, a pooled figure averaging a sign flip.

AND THE SHARPEST ARM RUNS AGAINST THE MECHANISM.  K8 contrasts on R+/l,
which by the derivation is exactly the part of the regulator that is not
the count -- large where the cycle's leading coefficients are small,
which is the pool the mechanism was ever about.  It pools to
+0.012 +/- 0.014, -0.027 +/- 0.025, -0.293 +/- 0.077 and -0.091 +/- 0.046
at h+ = 2, 4, 6, 8: null at the best-populated stratum and NEGATIVE where
it moves, against a predicted positive.  h+ = 6 flips sign between K3 and
K8, which is what two complementary cuts of one near-degenerate statistic
do and is a further reason not to read that stratum.

THE PLACEBO IS NULL ONLY WHEN IT IS DRAWN.  The first key tried was
(D * SEED) % 1000003, and it printed +0.164 +/- 0.050 at h+ = 8 -- 3.3
standard errors, which reads as the pooling machinery manufacturing
significance and is nothing of the kind.  A linear map mod a prime over
discriminants sampled at a FIXED STRIDE has terciles that are unions of
arithmetic progressions in |D|, and the ratio varies with |D| inside a
band, so that placebo was cutting on the very quantity it was meant to be
blind to.  Five DRAWN keys pool to -0.014, -0.007, +0.002, -0.023, -0.005
at h+ = 2 and -0.004, +0.023, +0.049, -0.085, -0.006 at h+ = 8, all
inside 1.7 standard errors; at h+ = 6 they run to +/-0.144, so the
observed +0.262 there beats all five draws while sitting well inside what
that stratum's own band-to-band scatter admits.  A placebo has to be
DRAWN, never computed from the quantity being controlled for.

P5's LETTER FAILED AND ITS SUBSTANCE HELD, which is worth separating.
The prediction called every pooled placebo contrast inside ONE standard
error, and 9 of the 20 drawn figures exceed that, the largest at 1.78.
The threshold was the error: 20 pooled figures under a true null put
about 6 beyond 1 s.e. and their maximum near 2.2, so the observed 9 and
1.78 are if anything TIGHTER than nominal -- the standard errors this rig
prints are conservative, not optimistic.  P5 should have been written
against the MAXIMUM over draws, which is the quantity a five-draw placebo
actually estimates.  Recorded rather than reinterpreted, and it is the
same defect round 3 found in the kill clause: a threshold named without
asking how many chances it would get.

WHAT THIS CLOSES.  The standing objection to the cycle-length refutation
was that the theory names a SIZE and only a COUNT had been killed.  Over
real quadratic fields at fixed h+ that distinction does not exist: the
class number formula ties h+ R+ to 2 sqrt(D) L(1, chi), and the mean step
ties R+ to l.  The |D| gradient at fixed h+ still has no mechanism, and
finding one now needs a population where the regulator and h+ move
INDEPENDENTLY -- which quadratic fields do not supply, and which is a
design question before it is a run.

RUN RECORD: 14.6 s wall, single process, well under the 512MB default
(no numpy, no array allocation -- the sweep holds one tuple per field).
5,409 fields swept across five bands -- 609 + 1200 x 4, the first band
exhausted rather than sampled; the l arm reproduces the published
within-band pooled contrasts to three decimals at every stratum
(-0.031 +/- 0.014, +0.031 +/- 0.025, +0.254 +/- 0.074, +0.051 +/- 0.048
at h+ = 2, 4, 6, 8), which pins this rig against explore_principal_scale.
"""

import os
import random
import sys
import time
from math import isqrt, log, sin, pi

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_principal_share import (                          # noqa: E402
    primes_upto, kronecker, form_at, fundamental_discriminants,
    class_data_real, principal_cycle, principal_real)

PCAP = 100                # the bottom decade IS the cell being contrasted
DBANDS = [(2000, 4000), (8000, 16000), (32000, 64000),
          (128000, 256000), (512000, 1024000)]
NF = 1200                 # fields sampled per band
NMIN = 6                  # split primes a field needs in the decade
MINF = 8                  # fields a cell needs to print
HPLUS = [2, 3, 4, 6, 8]
RDRAWS = 5                # placebo draws
PELL_Y = 2 * 10 ** 6      # brute-force bound on y in x^2 - D y^2 = +-4
SEED = 20845


def band_label(b):
    return "%d-%d" % b


def sample_fields(lo, hi, nf):
    """The scale rig's stride, so the field sets coincide band by band."""
    ds = fundamental_discriminants(lo, hi, +1)
    if len(ds) <= nf:
        return ds
    step = len(ds) / nf
    return [ds[int(i * step)] for i in range(nf)]


# ------------------------------------------------------- the accumulation

def regulator_of_cycle(cyc, D):
    """sum_i log((sqrt(D) + b_i) / (2|a_i|)) over the closed cycle."""
    s = D ** 0.5
    tot = 0.0
    for a, b, _c in cyc:
        tot += log((s + b) / (2 * abs(a)))
    return tot


# ------------------------------------------------------------ the controls

def pell_fundamental(D, ybound):
    """Least (x, y), y >= 1, with x^2 - D y^2 = +-4.  Integers throughout."""
    for y in range(1, ybound + 1):
        t = D * y * y
        for rhs in (t + 4, t - 4):
            if rhs <= 0:
                continue
            x = isqrt(rhs)
            if x * x == rhs:
                return x, y
    return None


def chi_kronecker(D, a):
    """chi_D(a) for ANY a >= 1, built multiplicatively.

    The rig's kronecker() is documented for an ODD PRIME argument and is
    silently WRONG outside that domain -- at a = 2 it returns +1 for every
    odd D, since pow(D%2, 0, 2) is 1.  It is not reusable here and the
    even part is done by the standard rule instead."""
    out = 1
    n = a
    while n % 2 == 0:
        if D % 2 == 0:
            return 0
        out *= 1 if D % 8 in (1, 7) else -1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            c = kronecker(D, p)
            if c == 0:
                return 0
            out *= c
            n //= p
        p += 2
    if n > 1:
        c = kronecker(D, n)
        if c == 0:
            return 0
        out *= c
    return out


def analytic_hR(D):
    """-(1/2) sum_{a=1}^{D-1} chi(a) log sin(pi a / D), which is h * R.

    The HALF is not decoration.  For D > 0, chi(D-a) = chi(-1) chi(a) =
    chi(a) and sin(pi(D-a)/D) = sin(pi a/D), so the full sum counts each
    term twice.  Coded without it the control returns exactly 2.00000 at
    every field -- a constant, which is what says convention rather than
    error, and the reason a control is read as a printed number and not
    as a pass/fail bit."""
    tot = 0.0
    for a in range(1, D):
        c = chi_kronecker(D, a)
        if c:
            tot -= c * log(sin(pi * a / D))
    return tot / 2.0


# ------------------------------------------------------------- the sweep

def sweep_band(lo, hi, plist, nf):
    """Per field: (D, h+, n, m, l, R+)."""
    out = []
    for D in sample_fields(lo, hi, nf):
        rt = isqrt(D)
        if rt * rt == D:
            continue
        _hwide, hplus, _neps = class_data_real(D, rt)
        cyc = principal_cycle(D, rt)
        pc = set(cyc)
        reg = regulator_of_cycle(cyc, D)
        n = m = 0
        for p in plist:
            if kronecker(D, p) != 1:
                continue
            b = form_at(D, p)
            nar, _wid = principal_real(D, p, b, pc, rt)
            n += 1
            if nar:
                m += 1
        out.append((D, hplus, n, m, len(cyc), reg))
    return out


# ---------------------------------------------------------- the contrasts

def contrast(vs):
    """Top-minus-bottom tercile of vs = [(key, value)], sorted on the KEY
    ALONE.  A bare tuple sort tie-breaks on the value being contrasted,
    which would split equal-key fields low-value into the bottom tercile
    and high-value into the top -- a control biased toward the effect it
    tests.  Python's sort is stable, so ties keep the sweep's |D| order."""
    vs = sorted(vs, key=lambda t: t[0])
    k = len(vs) // 3
    lo = [v for _, v in vs[:k]]
    hi = [v for _, v in vs[-k:]]
    ml = sum(lo) / len(lo)
    mh = sum(hi) / len(hi)
    vl = sum((x - ml) ** 2 for x in lo) / max(1, len(lo) - 1)
    vh = sum((x - mh) ** 2 for x in hi) / max(1, len(hi) - 1)
    return ml, mh, (vl / len(lo) + vh / len(hi)) ** 0.5


def spearman(xs, ys):
    def ranks(zs):
        order = sorted(range(len(zs)), key=lambda i: zs[i])
        r = [0.0] * len(zs)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and zs[order[j + 1]] == zs[order[i]]:
                j += 1
            avg = (i + j) / 2.0
            for t in range(i, j + 1):
                r[order[t]] = avg
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    dy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def pooled_table(all_rows, keyfn, title):
    """The within-band tercile contrast on one key, pooled over bands with
    inverse-variance weights -- the scale rig's K7, key swapped."""
    print("\n=== %s ===" % title)
    print("    %-4s %-14s %6s %8s %8s %9s %8s"
          % ("h+", "|D| band", "n", "low", "high", "contrast", "s.e."))
    for hp in HPLUS:
        num = den = 0.0
        shown = 0
        for b in DBANDS:
            vs = [(keyfn(r), (r[3] / r[2]) * hp)
                  for r in all_rows[b]
                  if r[1] == hp and r[2] >= NMIN]
            if len(vs) < 3 * MINF:
                continue
            ml, mh, se = contrast(vs)
            print("    %-4d %-14s %6d %8.3f %8.3f %9.3f %8.3f"
                  % (hp, band_label(b), len(vs), ml, mh, mh - ml, se))
            shown += 1
            if se > 0:
                num += (mh - ml) / se ** 2
                den += 1.0 / se ** 2
        if shown >= 2:
            print("    %-4d %-14s %6s %8s %8s %9.3f %8.3f   <-- pooled "
                  "over %d bands"
                  % (hp, "POOLED", "", "", "", num / den, den ** -0.5,
                     shown))


def main():
    t0 = time.time()
    # p = 2 is dropped, as the scale rig drops it: kronecker() is an
    # ODD-PRIME routine and returns +1 at p = 2 for every odd D, which
    # then reaches form_at with no square root to find.
    plist = [q for q in primes_upto(PCAP) if q != 2]

    # ---- K1: the controls, read before any contrast --------------------
    print("=== K1  IS THE ACCUMULATION THE REGULATOR? ===")
    print("  (Pell solved by brute force over y; the analytic column is")
    print("   -sum chi(a) log sin(pi a/D) = h R, touching neither route)")
    print("    %-7s %4s %4s %5s %11s %11s %8s %11s %8s"
          % ("D", "h", "h+", "N(e)", "R_cyc", "log eps", "ratio",
             "h*R_wide", "anal/hR"))
    bad = 0
    for D in fundamental_discriminants(5, 400, +1):
        rt = isqrt(D)
        if rt * rt == D:
            continue
        hw, hp, neps = class_data_real(D, rt)
        reg = regulator_of_cycle(principal_cycle(D, rt), D)
        pf = pell_fundamental(D, PELL_Y)
        if pf is None:
            continue
        x, y = pf
        leps = log((x + y * D ** 0.5) / 2.0)
        expect = 2.0 if neps == -1 else 1.0
        rat = reg / leps
        rwide = reg / expect
        anal = analytic_hR(D)
        arat = anal / (hw * rwide)
        if abs(rat - expect) > 1e-9 * expect or abs(arat - 1.0) > 1e-6:
            bad += 1
        print("    %-7d %4d %4d %5d %11.6f %11.6f %8.5f %11.6f %8.5f"
              % (D, hw, hp, neps, reg, leps, rat, hw * rwide, arat))
    print("  control fields failing either identity: %d" % bad)

    # ---- the sweep ------------------------------------------------------
    all_rows = {}
    for b in DBANDS:
        all_rows[b] = sweep_band(b[0], b[1], plist, NF)
        usable = sum(1 for r in all_rows[b] if r[2] >= NMIN)
        print("\n  band %-14s %5d fields swept, %5d with >= %d split primes"
              " at p <= %d" % (band_label(b), len(all_rows[b]), usable,
                               NMIN, PCAP))

    # ---- K2: are R+ and l the same statistic? ---------------------------
    print("\n=== K2  SPEARMAN(R+, l) WITHIN A BAND AT FIXED h+ ===")
    print("    %-4s %-14s %6s %9s" % ("h+", "|D| band", "n", "rho"))
    for hp in HPLUS:
        for b in DBANDS:
            rs = [r for r in all_rows[b] if r[1] == hp and r[2] >= NMIN]
            if len(rs) < 3 * MINF:
                continue
            print("    %-4d %-14s %6d %9.3f"
                  % (hp, band_label(b), len(rs),
                     spearman([r[5] for r in rs], [float(r[4]) for r in rs])))

    # ---- K3/K4/K5/K6: the contrasts, all on one field set ---------------
    pooled_table(all_rows, lambda r: r[5],
                 "K3  TOP-MINUS-BOTTOM R+ TERCILE, WITHIN EACH BAND")
    pooled_table(all_rows, lambda r: r[5] / r[0] ** 0.5,
                 "K4  THE SAME ON R+/sqrt(D)")
    pooled_table(all_rows, lambda r: float(r[4]),
                 "K5  THE REFUTED ARM, l, ON THESE IDENTICAL ROWS")
    # K7 is the question in its sharpest form and it is placed BEFORE the
    # placebo only in the printout. R+/l is the mean per-step distance --
    # the part of the regulator that is not the count, which by the
    # derivation is large exactly where the cycle's leading coefficients
    # are small. That is the pool the mechanism was ever about.
    print("\n=== K7  THE MEAN STEP R+/l, WHICH IS THE PART OF R+ THAT IS "
          "NOT l ===")
    print("    %-4s %-14s %6s %8s %8s %8s"
          % ("h+", "|D| band", "n", "mean", "sd", "sd/mean"))
    for hp in HPLUS:
        for b in DBANDS:
            st = [r[5] / r[4] for r in all_rows[b]
                  if r[1] == hp and r[2] >= NMIN]
            if len(st) < 3 * MINF:
                continue
            m = sum(st) / len(st)
            sd = (sum((x - m) ** 2 for x in st) / (len(st) - 1)) ** 0.5
            print("    %-4d %-14s %6d %8.4f %8.4f %8.4f"
                  % (hp, band_label(b), len(st), m, sd, sd / m))
    pooled_table(all_rows, lambda r: r[5] / r[4],
                 "K8  THE CONTRAST ON THE MEAN STEP R+/l")

    # K6: the placebo, and the FIRST key tried is kept as the record.
    # (D * SEED) % 1000003 is a linear map mod a prime over a set of D
    # sampled at a fixed stride, so its terciles are unions of arithmetic
    # progressions IN |D| -- and the ratio varies with |D| inside a band.
    # It printed +0.164 +/- 0.050 at h+ = 8, which looks like the
    # machinery manufacturing significance and is the placebo's own
    # structure. A placebo has to be drawn, not computed from the
    # quantity it is controlling for.
    rng = random.Random(SEED)
    keys = {}
    for b in DBANDS:
        for r in all_rows[b]:
            keys[r[0]] = [rng.random() for _ in range(RDRAWS)]
    for j in range(RDRAWS):
        pooled_table(all_rows, lambda r, j=j: keys[r[0]][j],
                     "K6.%d  THE PLACEBO -- A DRAWN KEY, INDEPENDENT OF |D|"
                     % (j + 1))

    print("\nwall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
