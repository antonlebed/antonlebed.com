"""Two amnesia clauses at the prediction door read "unmeasured" -- but
one is forced by the shape of its state map and the other is a
coarsening the corpus already has a law for.

THE QUESTION. The amnesia corpus grades the prediction door PER
CONSUMER: the INDIVIDUAL (one adapted optimum) and the ENSEMBLE (the
whole optimum set, a present no single state holds). Both grades are
recorded with a flatness clause left open -- the individual's fibers
"almost never row-exclusive, flatness on the shrunken fibers
unmeasured", and the ensemble's "spread already under the deficit,
within-block flatness unmeasured". Neither clause says what it would be
measuring. Flatness is a property of a state map against a WEIGHT and
of a named X, and at this door the state map of one consumer is not a
map at all: a row has between 2 and 32 co-optimal behavior classes, so
"the adapted state" is a RELATION and its posterior depends on a
selection rule nobody wrote down.

  Q1  Is the ensemble's deficit partition SPREAD in the corpus's own
      sense -- every fiber meeting at least two X-classes?
  Q2  Is within-fiber flatness a measurement at all, or forced by the
      shape of the state map?
  Q3  Where it is not forced -- at the STREAM, a coarsening of the
      row -- does it hold, and does the unwritten selection rule
      change the answer?

THE HAND-ATTACK (paper, before this engine).

  (1) THERE IS NO RESOURCE COORDINATE IN A ROW, so Lemma B has no grip
      here. The reader corpus's metabolism is the resource environment
      (B, W) -- budget and window caps -- and this door runs at ONE
      such setting, on unresourced policies. A row (map, stream) is
      entirely DATA: the map transforms the stream, it does not fund
      the reader. So H is nine data points with no factor to split,
      and destination universality is Lemma B at a TRIVIAL R: under
      the trace-geometry losses Phi is constant across rows, hence a
      function of the empty resource, hence posterior = prior for
      free.

  (2) WHICH MAKES X = THE ROW, and the stream a COARSENING of it. The
      corpus already owns that distinction: a certificate for X does
      not descend to functions of X, every coarsening needing its own
      flatness clause -- THE COUNT LEAK. So the two readings are not
      two candidate data; they are the datum and one of its
      coarsenings, and the second is where the leak would show.

  (3) FLATNESS OVER THE ROW IS FORCED WHEREVER Phi IS A FUNCTION OF
      IT. The posterior on a fiber is then the prior restricted, so at
      the uniform weight every fiber is flat and nothing is measured.
      The only open quantity at that reading is SPREAD.

  (4) FLATNESS OVER THE COARSENING IS NOT FORCED. Writing F for a
      fiber and F_x for the rows of F carrying stream x, the stream
      posterior at the uniform weight goes as |F_x|, so it is flat
      exactly when every stream the fiber holds arrives under the SAME
      NUMBER of maps -- a count condition on a ragged grid where id
      carries 4 streams, sq 2 and dbl 3. This is the count leak's own
      shape: a uniform posterior counted over unequal coarse classes.

  (5) AND GRADE S IS NOT DECIDABLE AT THIS DOOR AT ALL. S means
      uniform at EVERY weight in the family, and the corpus supplies
      no weight family here: the losses are the family elsewhere, and
      this door fixes its loss to ask its question. Any family one
      invents answers its own question -- vary the data prior and no
      spread fiber is ever S, split off a fake resource and some are.
      So this engine reports T-or-not at the uniform weight and
      refuses S, which is a scope statement and not a failure.

  (6) THE INDIVIDUAL IS A RELATION, NOT A MAP. A row has many
      co-optimal behavior classes, so "the adapted state" needs a
      selection rule the corpus never wrote down. Two readings, both
      named and both run: (i) a FIXED TIE-BREAK, lowest class index,
      which makes Phi a function and (3) apply verbatim; and (ii)
      UNIFORM CHOICE among co-optima, P(s | row) = 1/|argmin(row)|,
      which puts that reciprocal into the posterior. The corpus's
      grade is whichever it meant, and it said neither.

THE TRANSPLANTS, marked. None. Every object below is imported from
explore_prediction_door.py rather than rebuilt, and the grading
vocabulary is the amnesia corpus's own applied to its own recorded
consumers; nothing is carried across a parameter value.

PREDICTIONS (fixed before the run).

  PC1  POSITIVE CONTROL, THE SIBLING'S CENSUS. Rebuilt here, the
       behavior-class count is 38 and the pure argmin sizes are
       dbl/phi 2, dbl/sqrt2 4, dbl/fib 2, sq/phi 7, sq/sqrt2 32; the
       universal intersection is empty; exclusive classes sit at
       sq/sqrt2 (6) and sq/phi (1) and at no other row, so the count
       of rows with none is 9 - 2 = SEVEN. The sibling's prose says
       six, which is its arithmetic and not its measurement, so the
       bar here is derived from its own two exceptions; its OTHER
       six-of-nine, greedy falling out of the argmin, is checked as
       stated. A miss means this rig is not reading the sibling's
       object. Read before anything else.

  PC2  POSITIVE CONTROL, THE ANCHOR. The deficit partition rebuilt
       here has THREE blocks with row counts 5, 3, 1 and argmin set
       sizes 5, 1, 11, matching explore_bandwidth_dial.py's recorded
       anchor.

  PR1  THE ANCHOR HAS A READABLE FIBER. Observable: one block holds
       exactly one row, hence one stream, so spread fails at both
       readings. If every block holds two or more, the recorded clause
       stands as written.

  PR2  THE COARSENING LEAKS WHERE THE DATUM DOES NOT. Observable: the
       anchor block holding {id/phi, id/sqrt2, id/sqrt3, id/theta8,
       sq/phi} is flat over rows at the uniform weight and NOT flat
       over streams, phi arriving under two maps while sqrt2, sqrt3
       and theta8 arrive under one. This is the prediction that
       separates the datum from its coarsening; if it fails, the
       ragged grid is not reaching the fibers that matter.

  PR3  EVERY ROW-SPREAD FIBER OF A FUNCTION CONSUMER IS FLAT OVER
       ROWS. Observable: 100%, no exceptions, at both ensembles and at
       the individual under the fixed tie-break -- the forced result
       of (3), printed as the contrast that makes PR2 readable rather
       than as a discovery.

  PR4  AND STRICTLY FEWER ARE FLAT OVER THE COARSENING. Observable: at
       the uniform weight the stream-flat count is strictly below the
       row-flat count at every consumer with a stream-spread fiber. If
       they agree, the coarsening carries no leak here and the count
       condition is met by accident of the grid.

  PR5  THE SELECTION RULE IS LOAD-BEARING. Observable: under reading
       (ii) strictly fewer of the individual's stream-spread fibers
       are flat than under the same fibers with no selection factor.
       If the two agree, the unwritten rule was harmless and (6) is
       wrong.

RUN. This file needs explore_prediction_door.py beside it: the rows,
the images, the policies, the behavior classes and both losses are
imported from there rather than copied, so the two are one program in
two files.

python explore_door_grades.py   (estimate ~10 s, dominated by the
sibling's own class build at 0.6 s on record; exact rational arithmetic
on a 38 x 9 table, single process, memory far under the analysis
ceiling.)

FINDINGS (from the printed run below).

F1  THE CONTROLS PASS AND ONE OF THEM CORRECTED ITS OWN SOURCE. 38
    behavior classes; pure argmin sizes dbl/phi 2, dbl/sqrt2 4,
    dbl/fib 2, sq/phi 7, sq/sqrt2 32; universal intersection empty;
    greedy out of the argmin on 6 of 9 rows; the anchor rebuilding as
    three blocks of 5, 3 and 1 rows with argmin set sizes 5, 1 and 11.
    The row-exclusive bar was DERIVED from the sibling's own two
    exceptions rather than copied from its prose, which says six of
    nine rows carry none: with exclusive classes at sq/sqrt2 and
    sq/phi and nowhere else the count is seven, and the measurement
    here is seven. The slip is arithmetic in a sentence, and the
    sibling's other six-of-nine -- the one that shipped to a page --
    is correct.

F2  THE ANCHOR IS NOT SPREAD (PR1 confirmed, correcting the recorded
    clause). Its three blocks are {dbl/phi, dbl/sqrt2, dbl/fib},
    {id/phi, id/sqrt2, id/sqrt3, id/theta8, sq/phi} and {sq/sqrt2},
    and the third holds ONE row, hence one stream: READABLE at the
    datum and at its coarsening both. So "spread already under the
    deficit" is false as written, and the quantity the clause named
    as open is the one that fails.

F3  WITHIN-BLOCK FLATNESS AT THE DATUM IS FORCED, NOT MEASURED (PR3
    confirmed, 100% everywhere). Wherever the state map carries no
    selection factor the posterior on a fiber is the prior restricted,
    so at the uniform weight EVERY row-spread fiber is flat: 2 of 2 at
    the anchor, 3 of 3 at the individual under a fixed tie-break, 31
    of 31 at the individual read as a bare relation. Nothing there was
    ever going to be measured, and the recorded clause was owed a
    derivation rather than a run.

F4  BUT THE COARSENING LEAKS, WHICH IS WHERE THE MEASUREMENT LIVED
    (PR2 and PR4 confirmed). The stream is a function of the row, and
    the corpus's own law says a certificate for X does not descend to
    functions of X. It does not: the same fibers give 1 of 2, 2 of 3
    and 15 of 28 -- strictly below the datum's counts at every
    consumer that has a stream-spread fiber. The anchor's five-row
    block is the specimen and its arithmetic is visible in one line of
    counts: phi arrives under two maps and sqrt2, sqrt3 and theta8
    under one, so the stream posterior reads 2/5 against 1/5 three
    times while the row posterior is a flat 1/5 five times. That is
    THE COUNT LEAK firing at a second consumer and a second loss from
    the depth world where it was minted -- a uniform posterior counted
    over unequal coarse classes.

F5  AND THE INDIVIDUAL'S GRADE IS A FUNCTION OF A RULE NOBODY WROTE
    (PR5 confirmed). Under uniform choice among co-optima ZERO of its
    28 stream-spread fibers are flat, against 15 for the same fibers
    with no selection factor and 2 of 3 under a fixed tie-break. Three
    readings of one recorded clause, 0 against 15 against 2, exact
    rationals with no tolerance in the comparison. A row carries
    between 2 and 32 co-optima, so "the adapted state" is a relation,
    and the 1/|argmin| factor of a uniform choice is enough to tilt
    every fiber it touches. The clause was not an unmeasured quantity;
    it was an unwritten rule.

F6  GRADE S IS REFUSED, and the refusal is the scope statement.
    S means uniform at EVERY weight in the family, and this door
    supplies no family: it fixes its loss in order to ask its
    question, and the losses are what index the family elsewhere. Any
    family invented here answers its own question, which is checkable
    both ways -- vary the data prior and no spread fiber is ever S,
    posit a resource coordinate the rows do not have and some are. So
    everything above is read at ONE named weight and reported as T or
    not-T. The next-side ensemble needs none of it: all 9 of its
    fibers are singletons, spread 0 of 9, grade R, flatness vacuous --
    which is the honest reading of R, a readable fiber making flatness
    free and worthless.

READING. Two clauses recorded as unmeasured were one derivation and
one wrong description, and the measurement they were owed sits one
level down. The derivation: where the state map is a function of the
datum, within-fiber flatness at the uniform weight is the prior
restricted, so it is forced and carries nothing -- the only open
quantity at the datum is SPREAD. The wrong description: the anchor was
called spread and one of its three blocks holds a single row. What
actually grades is the COARSENING, the stream inside the row, and it
leaks exactly where the corpus's count leak says it should, on a grid
where one stream arrives under two maps and its neighbours under one.
And beneath both, the individual's state map is not a map: its grade
moves from 0 to 15 of 28 with the selection rule alone. Tier: F1
through F5 are exact and exhaustive at this scope (9 rows, 100
policies, 38 behavior classes, horizon 120), read at the uniform
weight; F6 is a scope statement, not a result.

Run record: run 1 exit 1 at PC1, the bar copied from the sibling's
prose rather than derived from its own numbers. Run 2 exit 0 but
graded the row alone. Run 3 graded the row against the stream under an
invented weight family, splitting streams from maps as data from
resource -- which this corpus does not do: its resource environment is
the budget and window caps, both row coordinates are data, and the
stream is a COARSENING rather than a factor. Both were caught in
review, the second by reading what the reader corpus calls metabolism.
Run 4 exit 0, the invented family removed and grade S refused with its
reason, all controls green, 0.6 s.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import time
from fractions import Fraction

import explore_prediction_door as door

ROWS = door.ROWS
MAPS = sorted({m for m, _ in ROWS})
STREAMS = sorted({s for _, s in ROWS})

# The weight on rows. There is no resource coordinate to factor here
# (hand-attack (1)), so this is the data prior itself and the corpus
# supplies no family varying it -- which is why grade S is refused
# below rather than reported. Uniform is the one named weight.
WEIGHT = {row: Fraction(1) for row in ROWS}


def row_weight(row):
    return WEIGHT[row]


# ------------------------------------------------------- the consumers

def argmin_sets(classes, key):
    """Per row, the set of behavior-class indices minimizing `key`.

    key = "miss" is the next-side pure order; key = "deficit" is the
    anchor, compared with the sibling's lexicographic deficit order."""
    out = {}
    for row in ROWS:
        if key == "miss":
            best = min(c["rows"][row]["miss"] for c in classes)
            out[row] = frozenset(ci for ci, c in enumerate(classes)
                                 if c["rows"][row]["miss"] == best)
        else:
            best = None
            ids = []
            for ci, c in enumerate(classes):
                d = c["rows"][row]["deficit"]
                if best is None or door.cmp_lex(d, best) < 0:
                    best, ids = d, [ci]
                elif door.cmp_lex(d, best) == 0:
                    ids.append(ci)
            out[row] = frozenset(ids)
    return out


def fibers_function(argmin):
    """A consumer whose Phi is a FUNCTION of the row: each row lands in
    exactly one fiber. The ensemble maps row |-> its argmin SET; the
    individual under reading (i) maps row |-> its lowest-index
    co-optimum."""
    out = {}
    for row in ROWS:
        out.setdefault(argmin[row], []).append(row)
    return list(out.values())


def fibers_lowest(argmin):
    out = {}
    for row in ROWS:
        out.setdefault(min(argmin[row]), []).append(row)
    return list(out.values())


def fibers_relation(argmin):
    """The individual as the corpus states it: a class's fiber is the
    set of rows it is optimal for. Rows appear in many fibers."""
    out = {}
    for row in ROWS:
        for ci in argmin[row]:
            out.setdefault(ci, []).append(row)
    return list(out.values())


# --------------------------------------------------------- the grading

def posterior(fiber, coord, argmin=None):
    """Exact posterior of X on a fiber. coord = "row" or "stream".
    argmin not None selects reading (ii): the uniform choice among a
    row's co-optima divides its mass by the number of them."""
    raw = {}
    for row in fiber:
        w = row_weight(row)
        if argmin is not None:
            w = w / len(argmin[row])
        key = row if coord == "row" else row[1]
        raw[key] = raw.get(key, Fraction(0)) + w
    tot = sum(raw.values())
    return {k: v / tot for k, v in raw.items()}


def is_flat(post):
    return len(set(post.values())) == 1


def classes_of(fiber, coord):
    return {row if coord == "row" else row[1] for row in fiber}


def map_counts(fiber):
    """|F_x| per stream: the count condition of hand-attack (4)."""
    out = {}
    for m, x in fiber:
        out[x] = out.get(x, 0) + 1
    return out


# --------------------------------------------------------- the controls

def _check(label, cond, detail):
    print("    [%s] %-52s %s" % ("PASS" if cond else "FAIL", label, detail))
    return cond


def controls(classes, am_next, am_def):
    print("PC1 THE SIBLING'S CENSUS")
    ok = True
    ok &= _check("38 behavior classes", len(classes) == 38,
                 "%d" % len(classes))
    want = {("dbl", "phi"): 2, ("dbl", "sqrt2"): 4, ("dbl", "fib"): 2,
            ("sq", "phi"): 7, ("sq", "sqrt2"): 32}
    got = {r: len(am_next[r]) for r in want}
    ok &= _check("pure argmin sizes at the five recorded rows",
                 got == want,
                 ", ".join("%s %d" % (door.fmt_row(r), got[r])
                           for r in want))
    uni = set.intersection(*(set(am_next[r]) for r in ROWS))
    ok &= _check("universal intersection empty", not uni, "%d" % len(uni))
    fib = {}
    for row in ROWS:
        for ci in am_next[row]:
            fib.setdefault(ci, []).append(row)
    excl = {r: sum(1 for ci in am_next[r] if fib[ci] == [r]) for r in ROWS}
    zero = sum(1 for r in ROWS if excl[r] == 0)
    ok &= _check("row-exclusive: seven rows at 0, sq/sqrt2 6, sq/phi 1",
                 zero == 7 and excl[("sq", "sqrt2")] == 6
                 and excl[("sq", "phi")] == 1,
                 ", ".join("%s %d" % (door.fmt_row(r), excl[r])
                           for r in ROWS))
    greedy_out = sum(1 for r in ROWS
                     if not any(p[2] == 0 and p[3] == 0
                                for ci in am_next[r]
                                for p in classes[ci]["members"]))
    ok &= _check("greedy falls out of the argmin on six of nine rows",
                 greedy_out == 6, "%d" % greedy_out)

    print("PC2 THE ANCHOR")
    blocks = fibers_function(am_def)
    sizes = sorted(len(v) for v in blocks)
    setsz = sorted(len(am_def[v[0]]) for v in blocks)
    ok &= _check("three blocks, rows 5/3/1, argmin sets 1/5/11",
                 sizes == [1, 3, 5] and setsz == [1, 5, 11],
                 "rows %s, sets %s" % (sizes, setsz))
    return ok


# ------------------------------------------------------------- the run

def grade(name, fibers, argmin=None):
    """Print the fiber census of one consumer under the datum and its
    coarsening, at the one named weight."""
    print("  %s: %d fiber(s)%s"
          % (name, len(fibers),
             "  [reading (ii): uniform choice among co-optima]"
             if argmin is not None else ""))
    tally = {}
    for coord in ("row", "stream"):
        spread = [f for f in fibers if len(classes_of(f, coord)) > 1]
        flat = sum(1 for f in spread
                   if is_flat(posterior(f, coord, argmin)))
        tally[coord] = (len(spread), flat)
        print("    X = %-7s spread %2d/%2d | flat at the uniform"
              " weight %2d/%2d%s"
              % (coord, len(spread), len(fibers), flat, len(spread),
                 "   (forced: no selection factor, so the posterior"
                 " is the prior restricted)"
                 if coord == "row" and argmin is None else ""))
    return tally


def main():
    t0 = time.time()
    print("THE PREDICTION DOOR'S GRADES -- the datum, its coarsening, and the"
          " selection nobody wrote down")
    print("rows: %s" % ", ".join(door.fmt_row(r) for r in ROWS))
    print("X candidates: the ROW (9 classes) and the STREAM (%d: %s)"
          % (len(STREAMS), ", ".join(STREAMS)))
    imgs = door.build_images(door.DEEP)
    targets = {row: door.truth_targets(imgs[row]) for row in ROWS}
    classes = door.build_classes(imgs, targets)
    am_next = argmin_sets(classes, "miss")
    am_def = argmin_sets(classes, "deficit")
    print()

    if not controls(classes, am_next, am_def):
        print("CONTROL FAILURE -- stop; no grade may be read.")
        raise SystemExit(1)

    print("\nE1 THE ANCHOR'S BLOCKS, named (the deficit, no future bit)")
    for f in sorted(fibers_function(am_def),
                    key=lambda v: door.fmt_row(v[0])):
        post = posterior(f, "stream")
        print("    {%-38s} streams %d  %s  counts %s  %s"
              % (", ".join(door.fmt_row(r) for r in f),
                 len(classes_of(f, "stream")),
                 "READABLE" if len(f) == 1 else "spread  ",
                 map_counts(f),
                 "flat" if is_flat(post) else
                 "TILTED " + ", ".join("%s=%s" % (k, v)
                                       for k, v in sorted(post.items()))))

    print("\nE2 THE CONSUMERS")
    t_def = grade("ENS_def  (row |-> argmin set, the anchor)",
                  fibers_function(am_def))
    t_next = grade("ENS_next (row |-> argmin set, next-side)",
                   fibers_function(am_next))
    t_i = grade("IND (i)  (row |-> its lowest-index co-optimum)",
                fibers_lowest(am_next))
    t_ii = grade("IND (ii) (class |-> the rows it is optimal for)",
                 fibers_relation(am_next), argmin=am_next)
    t_rel_i = grade("IND (i') (the same relation, no selection factor)",
                    fibers_relation(am_next))

    print("\nVERDICTS")
    anchor = fibers_function(am_def)
    print("  PR1 anchor has a readable fiber: %s"
          % ("yes" if any(len(f) == 1 for f in anchor) else "NO"))
    big = max(anchor, key=len)
    print("  PR2 the 5-row anchor block: flat over rows %s, over streams"
          " %s" % (is_flat(posterior(big, "row")),
                   is_flat(posterior(big, "stream"))))
    forced = all(t["row"][0] == t["row"][1]
                 for t in (t_def, t_next, t_i, t_rel_i))
    print("  PR3 every row-spread fiber flat over rows where Phi carries"
          " no selection factor: %s" % ("yes" if forced else "NO"))
    print("  PR4 stream-flat strictly below row-flat: %s"
          % ", ".join(
              "%s %d<%d %s" % (n, t["stream"][1], t["row"][1],
                               t["stream"][1] < t["row"][1])
              for n, t in (("ENS_def", t_def), ("IND(i)", t_i),
                           ("IND(i')", t_rel_i)) if t["stream"][0]))
    print("  PR5 selection rule load-bearing: reading (ii) %d vs (i')"
          " %d stream-flat: %s"
          % (t_ii["stream"][1], t_rel_i["stream"][1],
             "yes" if t_ii["stream"][1] < t_rel_i["stream"][1] else "NO"))
    print("  Grade S: REFUSED -- no weight family at this door"
          " (hand-attack (5))")
    print("\ndone in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
