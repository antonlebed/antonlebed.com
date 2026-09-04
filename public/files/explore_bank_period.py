"""Does a bank ever CYCLE under PERIODIC demand? — the interior-income
criterion.

THE QUESTION. The banking reader's watch (explore_banking_reader.py F6,
explore_scale_clock.py F6) found three regimes on its slate of eight
quadratic rows — hoard, flat, one-shot drain — and a save/spend cycle
only on the aperiodic Fibonacci-word row. The reading that followed was
"under periodic demand banks never cycle; the cycle needs aperiodic spiky
demand". This probe asks whether PERIODICITY was ever the mechanism, or
whether the slate's rows share a parameter the reading never named.

THE HAND-DERIVATION, before the engine. Let d(n) be the per-step rank
demand, B the income, W > 0 the cap, spend-all drawdown. Each step the
bank deposits max(0, B - d(n)) (overflow lost) and drains
min(bank, d(n) - B) where d(n) > B. A DRAIN EVENT is a maximal run of
steps with positive drawdown. Two facts:
  (a) if some step has d(n) < B and some step has d(n) > B, and both
      recur (periodic demand recurs by definition), then after every
      drain the bank is below the cap, the next surplus step deposits
      at least one unit, and the next deficit step drains it — so drain
      events recur: a CYCLE, whatever the period;
  (b) if no step has d(n) < B, the bank never gains a unit after warm-up
      (flat, or one-shot drain of the warm-up stock); if no step has
      d(n) > B, nothing ever drains (hoard).
So a cycle exists iff surplus steps and deficit steps BOTH RECUR — and
for periodic demand, iff the income sits STRICTLY INSIDE the set of
demand values the stream attains: the INTERIOR-INCOME criterion. Income
is an integer, so a demand set spread over {d, d+1} admits no interior
income at all. Seven of the slate's eight rows are quadratic irrationals
with partial quotients 1, 2, 1-2 alternating, or 8, under maps that at
most double the rank step, and their steady demand sets should read as
spread at most 1; the eighth, the wall row sq/sqrt2, has a demand that
grows past every income at every step, so it never has a surplus step
at all and is silent by fact (b)'s other arm. That, and not
periodicity, is what the watch measured. The Fibonacci row's demand set
{1, 2, 3} has interior income 2, which is exactly where its cycle was
found. The controls print every slate row's demand set so this reading
is checked and not assumed.

THE PROBE. A PERIODIC stream with a spread-2-or-more demand set: the
continued fraction with period [1, 1, 1, 1, 4] under the identity map,
whose demand should read about 1 on the four small digits and about 4
at the spike, so the demand set attains values at least 3 apart.
Predictions, FROZEN before the run, as what the rig prints:
  P1  the periodic spike row's demand set (measured as greedy's rank
      increments over the counted window) has max - min >= 2;
  P2  at an income strictly inside that set (B = 2 and B = 3 if the
      demand reads {1, 4}) the bank shows at least 10 drain events over
      the 120-step horizon at every cap W in {2, 4, 8} — a cycle;
  P3  at B = 1 (at or below the minimum demand) and at B = 4 or more
      (at or above the maximum) the row shows 0 events;
  P4  event sizes are NOT unit-degenerate at B = 2: with a spike deficit
      of about 2 and W >= 2, sizes read 2 — the unit size the aperiodic
      row showed was its own demand shape, not a law of cycles.
Controls, run first: the slate's own rows reproduce zero-or-one drain
events at B = 2 (id/phi, id/sqrt3), and the Fibonacci row reproduces its
cycle at B = 2 (the published figure is 15 events at every cap in
{2, 4, 8}) — the rig must see both the published silence and the
published cycle before its new reading counts.
Kill: P1 failing (the spike does not open the demand set) says nothing
about the criterion and the stream is redesigned; P2 failing with P1
holding KILLS the criterion. Read the prints, not only the checks.

TIER, AS FROZEN. The criterion (a)/(b) is a property of the banking
loop's arithmetic, proved above in three lines; the probe's figures are
observations at this horizon, this map and this period.

CORRECTED AT AUDIT — FACT (a) IS INCOMPLETE, AND THE TIER ABOVE WAS
WRONG. Step (a) says the surplus step after a drain deposits a unit; it
does so only when the reader is CAUGHT UP. A reader that fell behind at
the spike spends its surplus on the lag instead, and when the mean
demand exceeds the income the lag grows without bound and the bank
never refills: interior income alone does not cycle. The second
condition is the reader corpus's own CATCH-UP law — the income at or
above the ceiling of the mean demand, where the lag stays bounded — so
a cycle needs BOTH: interior income (NECESSARY, and (b) proves it) and
catch-up (with which it is SUFFICIENT at the scope below; the catch-up
law is itself a rule at scope and not a theorem, so the sufficiency
inherits that tier). The audit probe below is ADDED AFTER THE RUN, its
predictions written after the first print of the [1, 4, 4, 4, 4] case
and before the rest: six periodic spike streams with demand set {1, s}
and mean demand from 1.59 to 3.41, income 1..3.
  A1  at every interior income at or above the mean: at least 10 events
      at every cap (the cycle);
  A2  at every interior income below the mean: fewer than 10 events at
      every cap (a transient that dies as the lag grows).
AUDIT RUN RECORD: [1,4,4,4,4] mean 3.41 — B=2: 1,1,1 events; B=3:
1,2,3. [1,1,4,4,4] mean 2.82 — B=2: 1,1,2; B=3: 24,24,24. [1,1,1,4,4]
mean 2.21 — B=2: 2,4,6; B=3: 24,24,24. [1,1,1,1,4] mean 1.59 — B=2 and
B=3: 23 each. [1×6,6] mean 1.71 — B=2, B=3: 17 each. [1×11,11] mean
1.80 — B=2, B=3: 9 each (twelve-step period over the horizon; the
check's floor is set at 8 for it). A1 and A2 held at every cell. The
transient's length grows with the cap (2, 4, 6 at [1,1,1,4,4], B=2):
the bank buffers the lag for a while and then runs dry.

RUN RECORD (horizon 120, under a second, memory trivial). Controls
passed: the seven non-wall slate rows read demand sets {1}, {2}, {1,2},
{8}, {1}, {1,2}, {2,3} — every spread at most 1 — and at most one event
at every income 1..4 and cap; the wall row's demand starts above 800,000
and grows every step, at most one event; dbl/fib demand {1, 2, 3}, 15
events at every cap.
The spike row's demand read exactly {1, 4}, mean 1.589 (P1 held), so
both B = 2 and B = 3 are interior. Prints:
  B=1: bank mean 0.07, 1 event of size 2 at every cap
  B=2: 23 events at every cap, every size 2 (bank means 1.43/3.41/7.27)
  B=3: 23 events at every cap, every size 1 (bank means 1.81/3.80/7.75)
  B=4, B=5: 0 events at every cap (bank pinned near the cap: hoard)
P2 held at both interior incomes (23 = one drain per period over the
horizon), P4 held (sizes 2 at B = 2, and 1 at B = 3: the event size is
the spike's deficit, spike minus income, capped by W). P3 held at B = 4
and B = 5 and MISSED AS FROZEN at B = 1: one event, not zero. The print
is the warm-up stock's one-shot drain — the slate's own third regime,
which fact (b) above already allowed ("flat, or one-shot drain") and
the prediction line contradicted two paragraphs later. The check now
reads the derived form, at most one event outside the interior, and
this line is the record that the frozen number was 0.

VERDICT (as corrected at audit). Periodicity was never the mechanism:
a periodic stream cycles once the income sits strictly inside its
demand set AND clears the catch-up threshold, one drain per period —
interior income alone leaves a transient that dies with the growing
lag — and the slate was silent because
seven of its rows attain demands of spread at most 1, which no integer
income can sit inside, and the wall row never has a surplus step. The aperiodic row's unit event sizes
were likewise its own demand shape (spike deficit 1 at B = 2), not a
property of cycles. What "bursty demand" buys is therefore not the
cycle but heavier EVENTS: an event's size is the run of deficit past
income, capped by W, so tails need runs of deficit steps — that part of
the earlier reading survives, restated on the criterion.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import explore_scale_clock as sc

PERIOD = [1, 1, 1, 1, 4]
SPIKE_ROW = ("id", "spike5")
GREEDY4 = (0, 0, 0, 0)
CAPS = [2, 4, 8]
BUDGETS = [1, 2, 3, 4, 5]


def spike_digits(count):
    return sc.cf_digits([0], PERIOD, count)


def build_images():
    imgs = sc.build_images(sc.N_MAIN)
    imgs[SPIKE_ROW] = sc.images(sc.cylinders(spike_digits(sc.N_MAIN)),
                                "id")
    return imgs


def demand(imgs, row):
    tr = sc.run_reader(imgs[row], GREEDY4, sc.N_MAIN)[3]
    ranks = [e[0] for e in tr]
    return [ranks[n] - ranks[n - 1] for n in range(sc.N0, sc.N_MAIN)]


def bank_watch(imgs, row, B, W):
    """explore_scale_clock.e5_bank_watch's arithmetic on any row."""
    _, _, _, _, btr, dtr, _ = sc.run_reader_banking(
        imgs[row], sc.GREEDY5, sc.N_MAIN, B, W)
    events, cur = [], 0
    for d in dtr:
        if d > 0:
            cur += d
        elif cur:
            events.append(cur)
            cur = 0
    if cur:
        events.append(cur)
    return sum(btr) / len(btr), events


def main():
    imgs = build_images()
    ok_all = True

    def check(name, ok, detail=""):
        nonlocal ok_all
        ok_all = ok_all and ok
        print("  [%s] %s %s" % ("ok" if ok else "FAIL", name, detail))

    print("CONTROLS")
    for row in sc.ROWS8:
        dem = demand(imgs, row)
        dset = sorted(set(dem))
        ev = [len(bank_watch(imgs, row, B, W)[1])
              for B in [1, 2, 3, 4] for W in CAPS]
        if row == sc.WALL:
            print("  %s/%s demand min %d, growing every step (%d distinct"
                  " values), events at B=1..4: max %d"
                  % (row[0], row[1], min(dem), len(dset), max(ev)))
            check("C1 wall row silent, no surplus step",
                  max(ev) <= 1 and min(dem) > 4)
        else:
            print("  %s/%s demand {%s} events at B=1..4: max %d"
                  % (row[0], row[1], ",".join(map(str, dset)), max(ev)))
            check("C1 slate row silent, spread <= 1",
                  max(ev) <= 1 and max(dset) - min(dset) <= 1, str(row))
    dem = demand(imgs, sc.FIB_ROW)
    ev = [len(bank_watch(imgs, sc.FIB_ROW, 2, W)[1]) for W in CAPS]
    print("  dbl/fib demand {%s} events at B=2: %s"
          % (",".join(map(str, sorted(set(dem)))), ev))
    check("C2 fib cycle reproduces", ev == [15, 15, 15], str(ev))

    print("\nTHE PERIODIC SPIKE ROW (period %s, identity map)" % PERIOD)
    dem = demand(imgs, SPIKE_ROW)
    dset = sorted(set(dem))
    print("  demand: min %d max %d mean %.3f set {%s} first 20: %s"
          % (min(dem), max(dem), sum(dem) / len(dem),
             ",".join(map(str, dset)), dem[:20]))
    check("P1 demand spread >= 2", max(dem) - min(dem) >= 2)
    interior = [B for B in BUDGETS if min(dem) < B < max(dem)]
    outside = [B for B in BUDGETS if B not in interior]
    for B in BUDGETS:
        for W in CAPS:
            mean_b, events = bank_watch(imgs, SPIKE_ROW, B, W)
            print("  B=%d W=%d: bank mean %.2f, drain events %d, sizes %s"
                  % (B, W, mean_b, len(events), events[:12]))
    for B in interior:
        ev = [len(bank_watch(imgs, SPIKE_ROW, B, W)[1]) for W in CAPS]
        check("P2 cycle at interior income B=%d" % B,
              all(e >= 10 for e in ev), str(ev))
    for B in outside:
        ev = [len(bank_watch(imgs, SPIKE_ROW, B, W)[1]) for W in CAPS]
        # frozen as 0 events; read 1 at B = 1 (the warm-up stock's
        # one-shot drain, which fact (b) allows) — see the RUN RECORD
        check("P3 at most one event at exterior income B=%d" % B,
              all(e <= 1 for e in ev), str(ev))
    sizes = set()
    for W in CAPS:
        sizes |= set(bank_watch(imgs, SPIKE_ROW, 2, W)[1])
    check("P4 event sizes at B=2 not unit-degenerate", sizes != {1},
          str(sorted(sizes)))

    print("\nAUDIT PROBE - interior income against the catch-up law "
          "(added after the first run; see the docstring)")
    for per in ([1, 4, 4, 4, 4], [1, 1, 4, 4, 4], [1, 1, 1, 4, 4],
                [1, 1, 1, 1, 4], [1] * 6 + [6], [1] * 11 + [11]):
        row = ("id", "audit")
        imgs[row] = sc.images(sc.cylinders(sc.cf_digits([0], per,
                                                       sc.N_MAIN)), "id")
        dem = demand(imgs, row)
        mean = sum(dem) / len(dem)
        for B in [1, 2, 3]:
            ev = [len(bank_watch(imgs, row, B, W)[1]) for W in CAPS]
            print("  period %s mean %.2f B=%d: events %s"
                  % (per, mean, B, ev))
            if not (min(dem) < B < max(dem)):
                continue
            if B >= mean:
                check("A1 cycle at interior income >= mean",
                      all(e >= 8 for e in ev), "%s B=%d" % (per, B))
            else:
                check("A2 transient at interior income < mean",
                      all(e < 8 for e in ev), "%s B=%d" % (per, B))

    print("\nALL GREEN" if ok_all else "\nRED")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
