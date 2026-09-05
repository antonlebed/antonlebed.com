r"""THE LEAST-FACTOR SEAT -- is the cubic seat graded by the discriminant's
smallest prime factor, as the quadratic bias is? (a one-print read on
explore_quartic_seat.py's population, whose records, filter and per-field
rows it imports verbatim.)

THE QUESTION. Over the complex cubic fields of 2-rank 1 with |d| <= 24000
the least partial place of a field is a NON-SQUARE in the class group
about 84 times in 100 against the Chebotarev 1/2, at h = 2, 4 and 6
alike, graded by the place's rank and flat in its prime
(explore_quartic_seat.py). At degree 2 the sibling bias -- the least
split prime's excess over the reduction null -- is derived: the genus
character's residue classes are populated unevenly by the discriminant's
smallest prime factors at finite |D|, and the bias falls toward its null
once |D|'s least prime factor exceeds 7 (explore_floor_grade_shape.py).
The hypothesis this file reads is that the two are ONE object: that the
cubic seat, too, is the discriminant's smallest prime factors seen at the
least place, and so falls when they are removed.

THE SLATE (frozen before the engine ran).

  The statistic. For each field of the population, the indicator that
  its rank-1 partial place is a non-square, read from the rows
  explore_quartic_seat.py already builds; the share is that indicator's
  mean over a cell, the bar the null's sqrt(1/4N), never an empirical
  one, so a unanimous cell cannot print a zero bar.

  The split. The population at h = 2 -- the largest stratum and the one
  where non-square means non-principal -- is cut by the least prime
  factor of |d| at 7: fields whose |d| has a prime factor at most 7
  against fields whose least factor exceeds 7. The same cut is printed
  at h = 4 and pooled, and the h = 2 share is printed by the least
  factor itself (2, 3, 5, 7, above 7) for the shape.

  The prediction, transplanted from degree 2 (a TRANSPLANT: the quadratic
  bias is a genus-character fact, and a cubic field's genus theory runs
  on its conductor's lines, not on the factors of d alone): the share at
  least factor > 7 falls below the share at least factor <= 7.

  THE KILL, an observable. The difference of the two h = 2 shares
  divided by the root of the sum of their squared null bars; under 2.0
  in absolute value, the seat is unmoved by the split and the hypothesis
  dies, the cubic seat then a different object from the quadratic bias.
  At or above 2.0 in the predicted direction it survives to a
  derivation, and in the opposite direction it is a new print.

  THE POSITIVE CONTROL, run before the split is read: the pooled rank-1
  non-square share reprinted from the rows within 0.03 of the 0.84 the
  population's own file prints; a reprint off that line says the rows
  are not the sibling's and nothing below it is read.

THE RUN. The population is the sibling's whole class reading, the whole
of the wall; QSEAT_CACHE names its mapped-record pickle where one exists,
and LFS_CACHE names a pickle this file writes of the per-field rows (plain
dicts, the class-group object left behind) so a second read costs seconds.

THE FINDINGS (the post-run record; every number is a print of the run).

  The control passed: the pooled rank-1 non-square share reprinted at
  0.838 +- 0.019 over the 686 fields.

  F1  THE SEAT IS GRADED BY THE LEAST FACTOR (observation, one run). At
      h = 2 the share is 0.900 +- 0.030 over the 280 fields whose |d|
      has a prime factor at most 7 and 0.760 +- 0.035 over the 204 whose
      least factor exceeds 7, a difference of -0.140 at z = -3.05; pooled
      over every stratum 0.892 +- 0.024 against 0.751 +- 0.031, z =
      -3.58; at h = 4 alone -0.095 at z = -0.90 on 101 fields. The
      prediction held and the hypothesis SURVIVES its kill. The two
      cells match in size and in the least place (mean log|d| 9.30
      against 9.19, the share below |d| = 6000 0.19 against 0.21, the
      rank-1 prime 5.8 against 5.6 on average, read off the cached
      rows), so the grade is not the seat's fall with |d| in disguise.

  F2  THE SHAPE IS 2 | d. By the least factor itself at h = 2: 0.969 +-
      0.039 at 2 (161 fields), 0.786 at 3, 0.889 at 5, 0.773 at 7,
      0.760 above 7. The grade is almost wholly the fields where 2
      ramifies, where the least partial place is a non-square 156 times
      in 161; the odd least factors sit together near the above-7
      share.

  F3  THE RESIDUAL STANDS. Above 7 the share is 0.760 +- 0.035, seven
      null bars over the Chebotarev 1/2: what the smallest factors
      explain is a third of the excess, and two thirds of it is not
      theirs at this cut.

RUN RECORD. 2026-09-05, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_least_factor_seat.py`.
One process, CPython, no BLAS. 1075.6 s wall, all of it the sibling's
class reading; peak working set 155.9 MB against the 512 MB ceiling.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import pickle
import sys
import time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_quartic_seat as QS                  # noqa: E402

CUT = 7
CONTROL = (0.84, 0.03)


def least_factor(n):
    n = abs(n)
    p = 2
    while p * p <= n:
        if n % p == 0:
            return p
        p += 1
    return n


def share(rows):
    vals = [r['ns'][0] + 0.5 for r in rows if r['ns']]
    n = len(vals)
    if n == 0:
        return None, None, 0
    return sum(vals) / n, (0.25 / n) ** 0.5, n


def fmt(mu, se, n):
    if mu is None:
        return "--(0)"
    return "%.3f+-%.3f(%d)" % (mu, se, n)


def main():
    t0 = time.time()
    cache = os.environ.get("LFS_CACHE")
    if cache and os.path.exists(cache):
        with open(cache, "rb") as fh:
            rows = pickle.load(fh)
        print("per-field rows read from %s (%d)" % (cache, len(rows)))
    else:
        rows = QS.field_rows(QS.records())
        if cache:
            with open(cache, "wb") as fh:
                pickle.dump(rows, fh)
            print("per-field rows checkpointed to %s" % cache)
    print("%d fields, %.1f s" % (len(rows), time.time() - t0))

    print("\nPOSITIVE CONTROL: the pooled rank-1 non-square share")
    mu, se, n = share(rows)
    print("  pooled %s against %.2f +- %.2f" % (fmt(mu, se, n), *CONTROL))
    if abs(mu - CONTROL[0]) >= CONTROL[1]:
        print("  CONTROL FAILS: the rows are not the sibling's; nothing read")
        return
    print("  CONTROL PASSES")

    for r in rows:
        r['lpf'] = least_factor(r['d'])

    print("\nTHE SPLIT at least prime factor of |d| <= %d against > %d"
          % (CUT, CUT))
    verdict = None
    for label, sub in (("h = 2", [r for r in rows if r['h'] == 2]),
                       ("h = 4", [r for r in rows if r['h'] == 4]),
                       ("pooled", rows)):
        lo = share([r for r in sub if r['lpf'] <= CUT])
        hi = share([r for r in sub if r['lpf'] > CUT])
        if lo[0] is None or hi[0] is None:
            print("  %-7s <= %d %s   > %d %s   (a cell empty)"
                  % (label, CUT, fmt(*lo), CUT, fmt(*hi)))
            continue
        z = (hi[0] - lo[0]) / (lo[1] ** 2 + hi[1] ** 2) ** 0.5
        print("  %-7s <= %d %s   > %d %s   difference %+.3f, z %+.2f"
              % (label, CUT, fmt(*lo), CUT, fmt(*hi), hi[0] - lo[0], z))
        if label == "h = 2":
            verdict = z

    print("\nTHE SHAPE: the h = 2 share by the least prime factor of |d|")
    by = defaultdict(list)
    for r in rows:
        if r['h'] == 2:
            by[min(r['lpf'], CUT + 1)].append(r)
    for q in sorted(by):
        print("  least factor %s  %s"
              % ("> %d" % CUT if q > CUT else "= %d" % q, fmt(*share(by[q]))))

    print("\nTHE KILL: |z| at h = 2 under 2.0 kills; read %+.2f -> %s"
          % (verdict, "KILLED" if abs(verdict) < 2.0
             else ("SURVIVES (falls above %d)" % CUT if verdict < 0
                   else "a new print: RISES above %d" % CUT)))
    print("%.1f s wall" % (time.time() - t0))


if __name__ == "__main__":
    main()
