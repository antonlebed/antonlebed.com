r"""WHAT SORTS A COMPLEX CUBIC FIELD OF CLASS NUMBER 3 INTO ITS
SPLIT-TRIPLE REGIME? -- read at the QUADRATIC RESOLVENT, where the
regime is a statement about a degree-9 abelian extension of an imaginary
quadratic field and the covariate that suggested the question is a
count that only applies at one conductor.

THE FINDING THIS ANSWERS. explore_cubic_split_triple.py F1 sorts the 83
complex cubic fields of relation class number 3 into two regimes with
nothing between them: 38 whose every totally split prime carries ONE
ideal class three times (the realized triple group R = D), and 45 that
read the uniform model's spread (R = M). Its F4 reports a strong,
inexact covariate -- 31 of the 38 are the only field of their
discriminant with class number above 1, 44 of the 45 share theirs --
and names the arithmetic behind it, the resolvent correspondence under
which the cubic fields of one FUNDAMENTAL discriminant d_0 correspond to
the index-3 subgroups of the 3-class group of Q(sqrt(d_0)), so that
their number is (3^r - 1)/2 for r its 3-rank. It leaves the sorter open
and names the test: enumerate each family over the WHOLE population
rather than over its h > 1 part.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. F4's column
is written in the vocabulary of a POPULATION -- how many fields of this
enumeration share a discriminant. The object the resolvent theory talks
about is a FIELD, k = Q(sqrt(d_0)), and its class group. The translation
is not a convenience, and it is where the naive reading of the covariate
breaks: a cubic field's discriminant is d_K = f^2 * d_0 with d_0
fundamental, the count (3^r - 1)/2 is the count of cubic fields of
discriminant exactly d_0 -- that is, of CONDUCTOR f = 1 -- and at f > 1
the family is counted by a ray class group of k modulo f instead, whose
possible sizes are differences of two such counts and include 3. So the
family size at d_K is a proxy for r only at f = 1, and this file
measures r DIRECTLY, off the class group of k, rather than inferring it
from a count.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM THE SPLIT TRIPLE: the population, the class reading, the
    per-field regime label and its threshold are
    explore_cubic_split_triple.py's, imported and re-run rather than
    re-implemented -- including its own controls, which run here before
    anything below is read. What is new is one column per field, read
    off a different object (a binary quadratic form class group), and
    the cross-tabulations against it.

 T2 THE REGIME LABEL IS A MEASUREMENT AND NOT A CERTIFICATE. A field is
    called degenerate when its equal-class fraction is at or above 0.9
    over at least 10 totally split primes; the fractions measured there
    are 1.000 or at most 0.375 with nothing between, so the label
    carries no fitted cut, but it remains a reading of finitely many
    primes and every claim below inherits that.

 T3 THE FORM ENGINE IS NEW HERE and is therefore controlled from
    scratch: composition against the identity, against inverses, for
    associativity, and the order of the composed group against an
    independent count of reduced forms. A file whose whole new column
    comes out of one unproved routine is exactly the file that would
    carry a broken instrument silently.

 T4 THE ENUMERATION'S COMPLETENESS IS LOAD-BEARING HERE IN A WAY IT WAS
    NOT BEFORE. A family count is wrong if the enumeration misses a
    field of that discriminant, or if two non-isomorphic fields of one
    discriminant are merged by the splitting fingerprint that separates
    them. Both failures shrink a family, and the resolvent count is a
    THEOREM, so C2 below tests the enumeration against it over every
    fundamental discriminant the complex population carries.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE REGIME IS AN EXTENSION DEGREE. Keep the notation of
      explore_cubic_split_triple.py derivation (2): K a complex cubic
      field with Cl(K) = Z/3, N its Galois closure, H its Hilbert class
      field, H~ the Galois closure of H, and R = Gal(H~/N) the group of
      realized triples, one of 0, D, M. Each conjugate H_i satisfies
      H_i n N = K_i, since that intersection is an extension of K_i of
      degree dividing gcd(3, 2) = 1, so each H_i N / N has degree 3 and
      H~ = H_1 H_2 H_3 N. Hence

          R = D   <=>   [H~ : N] = 3   <=>   H_1 N = H_2 N = H_3 N,

      and calling that common field E, R = D holds exactly when E is
      stable under Gal(N/Q) -- that is, exactly when E/Q is GALOIS, of
      degree 18.

  (2) AND THEN E/k IS ABELIAN OF DEGREE 9. Let k = Q(sqrt(d_K)) be the
      quadratic resolvent, so k is contained in N with [N : k] = 3.
      Under R = D, [E : k] = [E : N][N : k] = 9, and E/Q Galois makes
      E/k Galois; every group of order 9 is abelian. So E is an abelian
      extension of k and class field theory prices it.

  (3) ITS RAMIFICATION IS N/k's. H/K is unramified at every place,
      finite and infinite, so E = HN is unramified over N and every
      ramified place of E/k is one of N/k. Write d_K = f^2 * d_0 with
      d_0 the fundamental discriminant of k. N/k is unramified exactly
      when f = 1.

  (4) THE UNRAMIFIED CASE THEREFORE GIVES A NECESSARY CONDITION WITH NO
      PARAMETERS IN IT. If f = 1 then E/k is abelian and unramified of
      degree 9, so E is contained in the Hilbert class field of k and
      Gal(E/k) is a quotient of Cl(k) of order 9. Hence

          R = D  and  d_K fundamental   ==>   9 divides h(k).

      SETTLED SINCE, AND STRICTLY STRONGER: explore_ray_class_inverted
      .py F6 excludes R = D at a fundamental discriminant outright, and
      its F7 replaces the conclusion here with 3-RANK Cl(k) >= 2 holding
      at every such field, R = D or not.

      Equivalently, in contrapositive: a complex cubic field whose
      discriminant is fundamental and whose resolvent has 3-class group
      exactly Z/3 CANNOT be degenerate. This is the derivation's whole
      content and it runs OPPOSITE to the naive reading of the
      covariate, which reads "alone at its discriminant" as r = 1 and
      r = 1 as the degenerate regime: at f = 1, r = 1 with h_3(k) = 3 is
      exactly the case the derivation forbids.

  (5) SO THE COVARIATE'S OWN DENT IS PREDICTED TO BE A CONDUCTOR
      ARTIFACT. explore_cubic_split_triple.py F4 records d_K = -2891 as
      three fields sharing a discriminant and all degenerate, against
      family sizes (3^r - 1)/2 that can only be 1, 4, 13. But
      -2891 = 7^2 * (-59) is not a fundamental discriminant: f = 7,
      d_0 = -59, and the correspondence that predicts 1, 4, 13 applies
      at f = 1 only. At conductor f the cubic fields with resolvent k
      and conductor dividing f correspond to index-3 subgroups of a ray
      class group of k modulo f, and the ones of conductor EXACTLY f are
      a difference of two such counts -- 4 - 1 = 3 among them. A family
      of three at a non-fundamental discriminant contradicts nothing.

  (6) WHICH MAKES THE FAMILY COUNT A POSITIVE CONTROL RATHER THAN THE
      MEASUREMENT. At every fundamental d_K < 0 carrying at least one
      field of the enumeration, the number of cubic fields of that exact
      discriminant must be (3^r - 1)/2. The two sides are computed here
      by disjoint machinery -- the left off the polynomial enumeration,
      the right off binary quadratic forms of discriminant d_0 -- so
      agreement controls the enumeration's completeness, the fingerprint
      separation of same-discriminant fields, and the form engine at
      once, and it is read BEFORE any regime column is.

  (7) WHAT IS NOT DERIVED. Nothing above makes 9 | h(k) SUFFICIENT for
      R = D at f = 1: E is one unramified cyclic cubic extension of N
      and the derivation does not force it to be the one lying in the
      Hilbert class field of k. Nor does it price f > 1, where the same
      argument bounds the ray class group of k modulo f instead and the
      rig here does not compute one. Both are measured and neither is
      claimed.

  (8) THE SCOPE IS COMPLEX FIELDS, and that is the population, not a
      convenience: d_K < 0 makes k imaginary quadratic, where the class
      group is the group of reduced positive definite forms and the
      narrow and wide groups agree. A totally real cubic field would
      need the indefinite form machinery and the narrow class group, and
      nothing here is claimed about one.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE DERIVED CONDITION HOLDS. No complex cubic field of the
      population with a FUNDAMENTAL discriminant, relation class number
      3 and the degenerate label has h(Q(sqrt(d_K))) with 3-part exactly
      3. (Derivation (4). A single such field kills the derivation, not
      the observation.)

  P2. THE NAIVE HYPOTHESIS FAILS, AND IN THE DIRECTION (4) NAMES. The
      cross-tabulation of regime against r is NOT the diagonal
      "degenerate exactly at r = 1": specifically at least one
      non-degenerate field has r = 1. (Frozen because it is the question
      as previously stated, and because a rig that only tests its own
      new hypothesis cannot report that the old one survived.)

  P3. THE REGIME IS A PROPERTY OF THE FAMILY. Every family -- the fields
      of one discriminant, restricted to those with class number 3 and a
      readable fraction -- is regime-homogeneous.

  P4. THE RESOLVENT COUNT IS EXACT AT FUNDAMENTAL DISCRIMINANTS. For
      every fundamental d_K < 0 carrying a field of the enumeration, the
      number of enumerated fields of that discriminant is (3^r - 1)/2.
      (A control, and the only prediction here whose failure indicts the
      instrument rather than the hypothesis.)

  P5. THE CONDUCTOR IS THE COVARIATE'S REAL CONTENT. The degenerate
      fields are enriched in f > 1 relative to the non-degenerate ones:
      the fraction with f > 1 among the 38 exceeds that among the 45.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed count of degenerate fields with fundamental
     d_K whose resolvent 3-class number is 3. Any value above 0 kills
     it, and with it derivation (2)-(4).

  K2 kills P2: the printed count of non-degenerate fields at r = 1. Zero
     kills P2 -- the naive hypothesis would then have survived the half
     of it this rig can see, and (4) and the measurement would be in
     conflict, which is a result and not a failure.

  K3 kills P3: the printed number of MIXED families, families carrying
     both labels. Any value above 0 kills it.

  K4 kills P4 and is read FIRST: the printed number of fundamental
     discriminants where the enumerated family size differs from
     (3^r - 1)/2. Any value above 0 stops the reading -- the instrument
     is then wrong and no column below means anything.

  K5 kills P5: the printed pair of f > 1 fractions. The degenerate one
     at or below the other kills it.

THE CONTROLS, run before any of the above is read.

  C1. THE FORM ENGINE, from scratch (T3). Over a sample of negative
      discriminants: the reduced forms counted here match
      explore_principal_share.py's independent count; the principal form
      is a two-sided identity; every form composed with its opposite
      gives the principal form; composition is associative on sampled
      triples; the composition table is closed on reduced forms; and the
      order of the 3-torsion subgroup is a power of 3 dividing the class
      number. Plus three pins whose values are classical and not
      computed here: h(-4) = 1, h(-163) = 1, h(-23) = 3.

  C2. THE RESOLVENT COUNT, which is P4 read as a control (derivation
      (6)).

  C3. THE INHERITED CONTROLS, RE-RUN AND NOT CITED.
      explore_cubic_split_triple.py's own sections S1 and S2 run here --
      the h = 1 pin, the map's verdict recomputed, the class-sum and
      equal-class identities at every split prime -- because this file
      reads a new statistic off the same population.

  C4. THE REGIME COLUMN REPRODUCED. The counts of degenerate and
      non-degenerate fields recomputed here must be 38 and 45, the
      numbers explore_cubic_split_triple.py F1 reports, or the label is
      not the same label.

THE FINDINGS.

  F1. THE RESOLVENT COUNT IS EXACT, AND THE COVARIATE THAT RAISED THE
      QUESTION WAS READING THE CONDUCTOR (rule, verified over the whole
      complex population to |d_K| <= 6000; S3). Of the 607 fundamental
      complex discriminants carrying a field of the enumeration, EVERY
      one carries exactly (3^r - 1)/2 of them -- 603 at family size 1
      with r = 1, four at family size 4 with r = 2, and no discriminant
      where the two disagree. WHAT THAT CONTROLS IS NARROWER THAN
      DERIVATION (6) CLAIMED AT THE FREEZE, and the amendment is made
      here rather than folded into the frozen text. A family the
      fingerprint SPLIT in two would over-count at any r, so that
      direction is controlled everywhere; a family with a field MISSED
      can only show where the prediction exceeds 1, which is the four
      discriminants at r = 2; and a discriminant every one of whose
      fields was missed never enters the check at all. So the
      fingerprint separation and the form engine are controlled over the
      whole range, and completeness only at r = 2.
      With that control in hand the previously recorded dent dissolves
      exactly as derivation (5) predicted: -2891 = 7^2 * (-59) is not a
      fundamental discriminant, its three fields are a family at
      conductor 7, and the count 1, 4, 13 was never a constraint on them.

  F2. NO COMPLEX CUBIC FIELD OF FUNDAMENTAL DISCRIMINANT IS DEGENERATE
      (observation, 83 fields at |d_K| <= 6000 and 193 over the three
      bands; S4, S7, S8). All 38 degenerate fields of the first
      population have conductor f > 1, against 31 of the 45 uniform
      ones, and the 14 fields at f = 1 are uniform without exception.
      The derived condition (4) does not explain this: those 14 all have
      3-class number 9 or 27 at their resolvent, so 9 | h(k) holds at
      every one of them and the derivation permits a degeneracy that
      does not occur. AND P1 THEREFORE SURVIVED VACUOUSLY: K1's
      subpopulation is the degenerate fields of fundamental
      discriminant, which is EMPTY, so the printed 0 is not a test of
      anything and derivation (2)-(4) stands unrefuted and unsupported
      by any measurement here.

  F3. THE HYPOTHESIS THIS RIG WAS BUILT TO TEST IS FALSE, AND FALSE
      BACKWARDS (observation; S5). "Degenerate exactly at r = 1" fails in
      both directions at once: 24 of the 45 uniform fields have r = 1,
      and 35 of the 38 degenerate ones have r = 0 -- their resolvent's
      class number is not divisible by 3 at all, so they carry no
      unramified cyclic cubic extension and could not have been read as
      a 3-rank phenomenon. The column that suggested r was a proxy for
      the CONDUCTOR: a non-fundamental discriminant's family is counted
      by a ray class group and is usually a single field, which is what
      "the only field of its discriminant" was measuring.

  F4. THE REGIME IS A PROPERTY OF THE DISCRIMINANT AND NOT OF THE FIELD,
      AND THE CONDUCTOR IS PART OF THAT DATUM (observation; S5). Of the
      19 discriminants carrying more than one readable field of class
      number 3, ZERO are mixed. Pooling by RESOLVENT instead -- the same
      k at different conductors -- gives 25 with more than one and one
      mixed, so d_K carries the regime where d_0 does not.

  F5. THE SORTER IS THE CONDUCTOR, READ MOD 3 (pattern, exact on 193
      complex cubic fields of relation class number 3 with |d_K| <=
      13000; S6, S7, S8). A field is degenerate exactly when

          some rational prime q = 1 mod 3 divides f,
          or 9 divides f AND 3 splits in k,

      and uniform otherwise. Over the first population the two conductor
      sets are disjoint and neither is small -- the degenerate ones run
      7, 9, 13, 14, 18, 19, 21, 26, 35, 37, 39, 42 against 1, 2, 5, 6,
      10, 30 for the uniform -- but THE CONDUCTOR AS AN INTEGER DOES NOT
      SORT once the bands are in: f = 18 carries the degenerate regime
      at d_0 = -11 and the uniform one at d_0 = -19, which is the whole
      reason the second clause reads k as well as f. THE STATUS OF THE TWO CLAUSES IS NOT THE
      SAME and the sections say which is which. The first clause was
      read off the first population (83 fields, fitted) and then held:
      55 further fields at 6000 < |d_K| <= 10000 and 55 more at
      10000 < |d_K| <= 13000, 70 degenerate and 123 uniform across the
      three bands, with no disagreement anywhere except the two that
      produced the second clause. THE SECOND CLAUSE RESTS ON THOSE TWO
      FIELDS. S7's predicate had 9 | f sufficient on its own and was
      killed by d_K = -6156, two fields at f = 18 over d_0 = -19 that
      read 0.200 and 0.250; the in-sample f = 18 case, d_K = -3564 over
      d_0 = -11, is degenerate, and what separates them is that 3 splits
      in Q(sqrt(-11)) and is inert in Q(sqrt(-19)). S8's band contains
      no field that separates the two predicates, so it confirms the
      first clause out of sample and says nothing about the second.
      AND ONE CORNER IS UNTOUCHED: 9 | f with 3 RAMIFIED in k, where one
      field of S8's band sits and is decided by the first clause anyway.

  F6. WHAT THE MECHANISM IS, AND WHY IT IS THE SAME STATEMENT AS
      DERIVATION (2) (a reading, not a proof, AND ONE STEP OF IT IS NOT
      EVEN AN ARGUMENT -- see below). R = D asks for an abelian E of
      degree 9 over k inside the ray class field modulo f, on which
      conjugation acts. N accounts for one line, which conjugation
      inverts, so E needs a second one. THE STEP THAT IS NOT DERIVED is
      that the second must be FIXED by conjugation rather than inverted:
      nothing in the group theory forbids an E with both lines inverted,
      and the uniform fields at conductor 2 and 5 carry a second
      inverted line and are not degenerate, so the measurement says such
      an E does not occur and no argument here says why. Granting that
      step, the rest is plain arithmetic and it reproduces F5's
      predicate exactly. A prime q = 1 mod 3 carries a fixed line
      however it sits in k -- split, the two primes above it are
      swapped and the (Z/3)^2 they carry splits into a fixed line and an
      inverted one; inert, the 3-part of the residue field's units
      divides q - 1 and conjugation, which is the Frobenius x -> x^q,
      fixes it. A prime q = 2 mod 3 can ramify cubically only when
      inert, and there the 3-part sits in q + 1 where the same Frobenius
      inverts. At 3 the one-units are the source, they need 9 | f to
      be reached, and they give a fixed line only when there are two
      primes to swap. That is exactly the predicate F5 measures, and it
      is why the sorter is a fact about k and f rather than about the
      cubic field sitting over them -- which is F4.
      SETTLED SINCE: explore_ray_class_lines.py builds the group this
      paragraph is about and finds the q = 3 sentence WRONG. An inert 3
      with 9 | f does leave a fixed line -- the one-units modulo 9 are
      F_9 with conjugation acting as Frobenius, which fixes the prime
      field -- and the sentence above is the q =/= 3 reasoning
      transplanted onto a different group with a different action. What
      excludes that case is that the fixed line there is ramified in a
      direction an anti-invariant character cannot absorb without
      ramifying E over N. The PREDICATE reproduced here is unaffected
      and F5 stands; only the reason for its second clause is replaced.
      AND SETTLED SINCE, TWICE MORE, on the fixed-versus-inverted step
      named above: explore_ray_class_inverted.py PROVES it, so nothing
      here is owed; and its census refutes the sentence above that "the
      measurement says such an E does not occur", which read one witness
      as an absence. Such an E occurs at EVERY field of this population,
      which is why the step had to be proved rather than granted.

  F7. THE DICHOTOMY ITSELF REPLICATES OUT OF SAMPLE (observation; S7,
      S8). The window [0.45, 0.95] holds no field in either held-out
      band -- 110 fields, every degenerate one reading exactly 1.000 --
      so the two-population reading of this stratum is not an artifact
      of the discriminant range it was found in.

  F8. THE OTHER STRATUM WHERE THE EQUAL TRIPLE EXISTS DECIDES NOTHING
      (observation; S6). Of the six complex fields at h = 6, one has a
      plus conductor (d_K = -5476, f = 37) and reads an equal-class
      fraction of 0.167 on 24 split primes against the uniform model's
      1/12 -- the highest of the six, the others running 0.000 to 0.065,
      and four events against two expected. That is a direction and not
      a reading, and the rule above is claimed at h = 3 only.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_regime_sorter.py`. One process, CPython, no
BLAS. 12 checks here plus the six that the inherited file's S1 and S2
run -- its other sections are not called from here -- 450.6 s wall, peak
working set 104.1 MB against memwatch's 512 MB ceiling. The inherited
population and its controls 236 s; the form engine over 80 fundamental
discriminants 0.0 s; the resolvent count over 607 discriminants 0.1 s;
the first held-out band 632 complex fields read in 105 s, the second 487
in 109 s, two and one field respectively left unresolved by the class
reading and skipped. THE ASSERTIONS HERE COVER THE CONTROLS ONLY: a
predicate that fails is a finding, so S7's kill prints its two fields
and returns rather than stopping the run.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_split_triple as ECST
import explore_cubic_principal as ECP
import explore_principal_share as EPS

CHECKS = 0

MIN_SPLIT = ECST.MIN_SPLIT
HIGH_FRAC = ECST.HIGH_FRAC

N_DEGENERATE = 38       # C4: the two group sizes this file must reproduce
N_UNIFORM = 45

CLASS_PINS = {-4: 1, -163: 1, -23: 3}    # C1, classical and not computed

HELD_LO, HELD_HI = 6000, 10000    # S7's held-out band, |d_K| strictly above
                                  # the population the predicate came from
SECOND_HI = 13000                 # S8's band, above S7's


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


# --------------------------------------------- binary quadratic forms
def ext_gcd(a, b):
    """(g, x, y) with a*x + b*y = g >= 0, iterative. THE SIGN IS THE
    POINT: the Euclidean loop on negative inputs returns a negative g,
    and the caller below completes (x, y) to a unimodular matrix from
    those cofactors, where a sign error is a determinant of -1."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return (a, x0, y0) if a >= 0 else (-a, -x0, -y0)


def modinv(a, m):
    g, x, _ = ext_gcd(a % m, m)
    assert g == 1, "no inverse of %d mod %d" % (a, m)
    return x % m


def principal_form(D):
    """The identity class of discriminant D < 0."""
    return (1, 0, -D // 4) if D % 4 == 0 else (1, 1, (1 - D) // 4)


def reduced_forms(D):
    """Every reduced PRIMITIVE positive definite form of discriminant
    D < 0: -a < b <= a <= c, and b >= 0 where a = c. The class group is
    the primitive forms; at a fundamental discriminant there are no
    others, since an imprimitive form of content g has D/g^2 for a
    discriminant, so the filter is a no-op exactly where this file uses
    the count as a control."""
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (a == c and b < 0):
                continue
            if gcd(gcd(a, b), c) != 1:
                continue
            out.append((a, b, c))
        a += 1
    return out


def represent_coprime(f, m):
    """A form equivalent to f whose leading coefficient is coprime to m.
    The class represents f(x, y) for every coprime pair, and completing
    (x, y) to a unimodular matrix transports the form."""
    a, b, c = f
    if gcd(a, m) == 1:
        return f
    r = 1
    while r < 64:
        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                if gcd(x, y) != 1:
                    continue
                a2 = a * x * x + b * x * y + c * y * y
                if a2 <= 0 or gcd(a2, m) != 1:
                    continue
                _, u, v = ext_gcd(x, y)          # x*u + y*v = 1
                w, z = u, -v                     # x*w - y*z = 1
                b2 = 2 * (a * x * z + c * y * w) + b * (x * w + y * z)
                c2 = a * z * z + b * z * w + c * w * w
                return (a2, b2, c2)
        r += 1
    raise AssertionError("no coprime representative for %s mod %d" % (f, m))


def compose(f1, f2, D):
    """Dirichlet composition through a coprime representative."""
    a1, b1, c1 = represent_coprime(f1, f2[0])
    a2, b2 = f2[0], f2[1]
    del c1
    t = (((b2 - b1) // 2) * modinv(a1, a2)) % a2 if a2 > 1 else 0
    B = b1 + 2 * a1 * t
    A = a1 * a2
    C = (B * B - D) // (4 * A)
    return EPS.reduce_definite((A, B, C), D)


def opposite(f):
    return (f[0], -f[1], f[2])


def class_group(D):
    """(forms, h, three_torsion, r, h3) for D < 0. r is the 3-rank."""
    forms = reduced_forms(D)
    h = len(forms)
    e = EPS.reduce_definite(principal_form(D), D)
    n3 = 0
    for f in forms:
        f2 = compose(f, f, D)
        if compose(f2, f, D) == e:
            n3 += 1
    r = 0
    while 3 ** (r + 1) <= n3:
        r += 1
    h3 = 1
    m = h
    while m % 3 == 0:
        h3 *= 3
        m //= 3
    return forms, h, n3, r, h3


# --------------------------------------------- discriminant arithmetic
def squarefree_part(n):
    """(m, f) with n = m * f^2 and m squarefree, sign kept."""
    s = -1 if n < 0 else 1
    n = abs(n)
    f = 1
    d = 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
            f *= d
        d += 1
    return s * n, f


def fundamental_part(dK):
    """(d_0, f) with dK = f^2 * d_0 and d_0 the discriminant of the
    quadratic resolvent Q(sqrt(dK))."""
    m, f = squarefree_part(dK)
    if m % 4 == 1:
        return m, f
    assert f % 2 == 0, "d_K = %d has no fundamental part" % dK
    return 4 * m, f // 2


# --------------------------------------------------------- the sections
def s1_form_engine():
    section("S1  C1 THE FORM ENGINE -- controlled from scratch")
    sample = [D for D in range(-6000, 0)
              if D % 4 in (0, 1) and fundamental_part(D)[1] == 1][::23]
    bad_count = bad_id = bad_inv = bad_assoc = bad_closed = bad_tor = 0
    t0 = time.time()
    for D in sample:
        forms, h, n3, r, h3 = class_group(D)
        if h != EPS.class_number_imag(D):
            bad_count += 1
        e = EPS.reduce_definite(principal_form(D), D)
        if e not in forms:
            bad_id += 1
        fs = forms[:6]
        for f in fs:
            if compose(e, f, D) != f or compose(f, e, D) != f:
                bad_id += 1
            if compose(f, EPS.reduce_definite(opposite(f), D), D) != e:
                bad_inv += 1
            for g in fs:
                if compose(f, g, D) not in forms:
                    bad_closed += 1
                for k in fs[:3]:
                    lhs = compose(compose(f, g, D), k, D)
                    rhs = compose(f, compose(g, k, D), D)
                    if lhs != rhs:
                        bad_assoc += 1
        if n3 != 3 ** r or h % n3:
            bad_tor += 1
    print("  %d discriminants sampled, %.1f s" % (len(sample),
                                                  time.time() - t0))
    print("  order against the independent reduced-form count: %d bad"
          % bad_count)
    print("  identity %d bad, inverses %d bad, associativity %d bad, "
          "closure %d bad" % (bad_id, bad_inv, bad_assoc, bad_closed))
    print("  3-torsion a power of 3 dividing h: %d bad" % bad_tor)
    ok(bad_count == 0, "%d group orders wrong" % bad_count)
    ok(bad_id == 0, "%d identity failures" % bad_id)
    ok(bad_inv == 0, "%d inverse failures" % bad_inv)
    ok(bad_assoc == 0, "%d associativity failures" % bad_assoc)
    ok(bad_closed == 0, "%d closure failures" % bad_closed)
    ok(bad_tor == 0, "%d bad 3-torsion orders" % bad_tor)
    for D, hv in sorted(CLASS_PINS.items()):
        _, h, n3, r, h3 = class_group(D)
        print("  pin D = %-6d h = %d (classical %d)  3-torsion %d  r = %d"
              % (D, h, hv, n3, r))
        ok(h == hv, "h(%d) = %d, classical value %d" % (D, h, hv))


def s2_population():
    section("S2  C3 THE INHERITED POPULATION AND ITS CONTROLS, RE-RUN")
    recs = ECST.s1_population()
    mapped = ECST.s2_controls(recs)
    return recs, mapped


def s3_resolvent_count(recs):
    section("S3  C2 THE RESOLVENT COUNT at fundamental discriminants -- "
            "the positive control")
    fam = {}
    for r in recs:
        d = r[0]
        if d < 0:
            fam[d] = fam.get(d, 0) + 1
    rows = []
    bad = 0
    t0 = time.time()
    for d in sorted(fam, key=abs):
        d0, f = fundamental_part(d)
        if f != 1:
            continue
        _, h, n3, r3, h3 = class_group(d0)
        pred = (n3 - 1) // 2
        rows.append((d, fam[d], pred, r3, h, h3))
        if fam[d] != pred:
            bad += 1
    print("  %d fundamental complex discriminants carry a field, %.1f s"
          % (len(rows), time.time() - t0))
    hist = {}
    for (d, n, pred, r3, h, h3) in rows:
        hist[(n, pred)] = hist.get((n, pred), 0) + 1
    print("  %-14s %-14s %s" % ("family size", "(3^r - 1)/2", "count"))
    for (n, pred) in sorted(hist):
        print("  %-14d %-14d %d" % (n, pred, hist[(n, pred)]))
    print("  [K4] fundamental discriminants where the two disagree: %d"
          % bad)
    ok(bad == 0, "%d resolvent-count mismatches" % bad)
    for (d, n, pred, r3, h, h3) in rows[:6]:
        print("    d_K = %-7d fields %d  r = %d  h(k) = %-4d h_3 = %d"
              % (d, n, r3, h, h3))
    return fam


def s4_table(recs, mapped, fam):
    section("S4  THE SORTER COLUMNS -- conductor, resolvent, 3-rank, "
            "family, regime")
    fam_hi = {}
    for r in recs:
        if r[0] < 0 and r[6] is not None and r[6] > 1:
            fam_hi[r[0]] = fam_hi.get(r[0], 0) + 1
    rows = []
    for (d, cx, H, ns, ne, verdicts) in mapped:
        if not cx or H != 3:
            continue
        frac = (float(ne) / ns) if ns else None
        if ns < MIN_SPLIT or frac is None:
            label = "unread"
        else:
            label = "D" if frac >= HIGH_FRAC else "M"
        d0, f = fundamental_part(d)
        _, h, n3, r3, h3 = class_group(d0)
        rows.append((d, d0, f, r3, h, h3, fam[d], fam_hi.get(d, 0),
                     ns, ne, frac, label))
    rows.sort(key=lambda t: (t[11], abs(t[0])))
    nd = sum(1 for t in rows if t[11] == "D")
    nm = sum(1 for t in rows if t[11] == "M")
    nu = sum(1 for t in rows if t[11] == "unread")
    print("  [C4] %d degenerate, %d uniform, %d unread (the split-triple "
          "file reports %d and %d)" % (nd, nm, nu, N_DEGENERATE, N_UNIFORM))
    ok(nd == N_DEGENERATE, "%d degenerate fields, expected %d"
       % (nd, N_DEGENERATE))
    ok(nm == N_UNIFORM, "%d uniform fields, expected %d" % (nm, N_UNIFORM))
    print("  'family' counts every field of this enumeration at that d_K, "
          "class number 1 included; 'fam>1' is the previously printed "
          "column, which counts only those with class number above 1")
    print("  %-8s %-8s %-4s %-3s %-7s %-5s %-7s %-6s %-6s %-8s %s"
          % ("d_K", "d_0", "f", "r", "h(k)", "h_3", "family", "fam>1",
             "split", "fraction", "regime"))
    for t in rows:
        (d, d0, f, r3, h, h3, nf, nfh, ns, ne, frac, label) = t
        print("  %-8d %-8d %-4d %-3d %-7d %-5d %-7d %-6d %-6d %-8s %s"
              % (d, d0, f, r3, h, h3, nf, nfh, ns,
                 "%.3f" % frac if frac is not None else "--", label))
    return rows


def s5_crosstabs(rows):
    section("S5  THE CROSS-TABULATIONS -- the derived condition, the "
            "naive hypothesis, the family, the conductor")
    read = [t for t in rows if t[11] in ("D", "M")]

    print("  [K1] P1, derivation (4): degenerate fields with FUNDAMENTAL "
          "d_K and resolvent 3-class number 3 -- the case the derivation "
          "forbids")
    viol = [t for t in read if t[11] == "D" and t[2] == 1 and t[5] == 3]
    fund_d = [t for t in read if t[11] == "D" and t[2] == 1]
    print("       %d of the %d degenerate fields have f = 1; %d of those "
          "have h_3(k) = 3" % (len(fund_d), sum(1 for t in read
                                                if t[11] == "D"), len(viol)))
    for t in viol:
        print("       d_K = %-8d d_0 = %-8d h(k) = %d" % (t[0], t[1], t[4]))

    print("  [K2] P2, the naive hypothesis 'degenerate iff r = 1':")
    print("       %-10s %-10s %s" % ("", "r = 1", "r >= 2"))
    for label in ("D", "M"):
        a = sum(1 for t in read if t[11] == label and t[3] == 1)
        b = sum(1 for t in read if t[11] == label and t[3] >= 2)
        print("       %-10s %-10d %d" % (label, a, b))
    print("       non-degenerate fields at r = 1: %d"
          % sum(1 for t in read if t[11] == "M" and t[3] == 1))

    print("  [K3] P3, the regime as a family property:")
    by_d = {}
    for t in read:
        by_d.setdefault(t[0], []).append(t[11])
    multi = [(d, v) for (d, v) in by_d.items() if len(v) > 1]
    mixed = [(d, v) for (d, v) in multi if len(set(v)) > 1]
    print("       %d discriminants carry more than one readable field of "
          "class number 3; %d of them are MIXED" % (len(multi), len(mixed)))
    for (d, v) in sorted(mixed, key=lambda x: abs(x[0])):
        print("       d_K = %-8d labels %s" % (d, "".join(sorted(v))))
    by_d0 = {}
    for t in read:
        by_d0.setdefault(t[1], []).append(t[11])
    m0 = [(d, v) for (d, v) in by_d0.items() if len(v) > 1]
    mix0 = [(d, v) for (d, v) in m0 if len(set(v)) > 1]
    print("       and by RESOLVENT rather than discriminant: %d resolvents "
          "carry more than one, %d mixed" % (len(m0), len(mix0)))

    print("  [K5] P5, the conductor:")
    for label in ("D", "M"):
        g = [t for t in read if t[11] == label]
        nf = sum(1 for t in g if t[2] > 1)
        print("       %-10s %d of %d have f > 1  (%.3f)"
              % (label, nf, len(g), float(nf) / len(g) if g else 0.0))

    print("  the h_3(k) profile of each regime, which no prediction "
          "named:")
    for label in ("D", "M"):
        prof = {}
        for t in read:
            if t[11] == label:
                prof[(t[2] == 1, t[5])] = prof.get((t[2] == 1, t[5]), 0) + 1
        for key in sorted(prof):
            print("       %-10s f %s  h_3(k) = %-6d %d"
                  % (label, "= 1" if key[0] else "> 1", key[1], prof[key]))
    return read


def plus_conductor(f):
    """Whether the conductor contributes a PLUS part to the 3-part of
    the ray class group of k modulo f -- read off f alone. A rational
    prime q = 1 mod 3 dividing f contributes one either way it sits in
    k: split, the two primes are swapped and the (Z/3)^2 they carry
    splits into a plus and a minus line; inert, the 3-part of the
    residue field's unit group has order dividing q - 1 and Frobenius,
    which is conjugation, raises to the q = 1 power and acts trivially
    on it. A prime q = 2 mod 3 can only contribute at all when it is
    inert, and there the 3-part sits in q + 1 where Frobenius acts by
    inversion -- minus only. At 3 the one-units are the source and a
    single power of 3 in f does not reach them. SETTLED SINCE: what this
    predicate computes is not the presence of a plus part but whether
    one is USABLE, and the two differ at an inert 3 -- see F6's pointer
    and explore_ray_class_lines.py."""
    n, ns = f, []
    d = 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            ns.append((d, e))
        d += 1
    if n > 1:
        ns.append((n, 1))
    for (q, e) in ns:
        if q == 3:
            if e >= 2:
                return True
        elif q % 3 == 1:
            return True
    return False


def s6_conductor_rule(rows, mapped):
    section("S6  THE CONDUCTOR RULE -- POST-HOC, read off S4's own table "
            "and checked mechanically here")
    print("  NOTHING BELOW WAS FROZEN. The separator was found in the "
          "printed table above, so it is fitted on these 83 fields and "
          "the count of disagreements is not a test of it. What makes it "
          "more than a fit is the mechanism -- derivation (2) needs an "
          "abelian E of degree 9 over k, and the predicate is whether "
          "the conductor hands the 3-part of the ray class group a PLUS "
          "component at all.")
    read = [t for t in rows if t[11] in ("D", "M")]
    print("  %-10s %-14s %-14s" % ("", "plus conductor", "minus only"))
    bad = 0
    for label in ("D", "M"):
        a = sum(1 for t in read if t[11] == label and plus_conductor(t[2]))
        b = sum(1 for t in read if t[11] == label
                and not plus_conductor(t[2]))
        print("  %-10s %-14d %-14d" % (label, a, b))
        bad += b if label == "D" else a
    print("  disagreements with 'degenerate iff the conductor has a plus "
          "part': %d of %d" % (bad, len(read)))
    fs = sorted(set(t[2] for t in read if t[11] == "D"))
    ms = sorted(set(t[2] for t in read if t[11] == "M"))
    print("  conductors carrying the degenerate regime: %s"
          % " ".join(str(x) for x in fs))
    print("  conductors carrying the uniform regime:    %s"
          % " ".join(str(x) for x in ms))

    print("  OUT OF SAMPLE IN THE CLASS NUMBER, and read as a reading and "
          "not a test: the complex fields at h = 6, the one other stratum "
          "where the equal triple exists at all. The uniform model's "
          "equal-class fraction there is 1/12.")
    for (d, cx, H, ns, ne, verdicts) in sorted(mapped, key=lambda t: abs(t[0])):
        if not cx or H != 6:
            continue
        d0, f = fundamental_part(d)
        print("    d_K = %-8d f = %-4d plus %-6s split %-4d equal %-4d "
              "fraction %s" % (d, f, "yes" if plus_conductor(f) else "no",
                               ns, ne,
                               "%.3f" % (float(ne) / ns) if ns else "--"))
    return bad


def s7_held_out():
    section("S7  THE HELD-OUT BAND -- the conductor rule frozen after S6 "
            "and run on discriminants it has never seen")
    print("  THE PREDICATE IS FROZEN BEFORE THIS SECTION RUNS and is the "
          "one S6 states: a complex cubic field of relation class number "
          "3 is degenerate exactly when 9 divides its conductor or some "
          "rational prime congruent to 1 mod 3 does. The band is "
          "%d < |d_K| <= %d, disjoint from the population that produced "
          "the predicate. K6: any disagreement kills it."
          % (HELD_LO, HELD_HI))
    t0 = time.time()
    fields, _ = ECP.enumerate_fields(HELD_HI)
    band = [f for f in fields if HELD_LO < f[0] <= HELD_HI and f[2]]
    print("  %d complex fields in the band, %.1f s"
          % (len(band), time.time() - t0))
    t0 = time.time()
    rows = []
    n_un = 0
    for (ad, d, cx, polys) in band:
        a, b, c, O = polys[0]
        rows_t2 = ECP.t2_rows(O, a, b, c)
        h, kind, gp, rel = ECST.CCM.class_and_relations(O, d, cx, rows_t2)
        if h is None:
            n_un += 1
            continue
        if h != 3:
            continue
        H_map, piv, k, per_prime = ECST.read_field(O, a, b, c, d, cx, gp, rel)
        if H_map != 3:
            continue
        ns, ne, bs, bi, nn, verdicts = ECST.field_stats(per_prime, piv, k)
        del bs, bi, nn, verdicts
        if ns < MIN_SPLIT:
            continue
        frac = float(ne) / ns
        d0, f = fundamental_part(d)
        rows.append((d, d0, f, ns, ne, frac,
                     "D" if frac >= HIGH_FRAC else "M", plus_conductor(f)))
    print("  %d fields at class number 3 with a readable fraction, %d "
          "unresolved and skipped, %.1f s"
          % (len(rows), n_un, time.time() - t0))
    rows.sort(key=lambda t: (t[6], abs(t[0])))
    print("  %-8s %-8s %-5s %-6s %-6s %-9s %-7s %s"
          % ("d_K", "d_0", "f", "split", "equal", "fraction", "regime",
             "plus"))
    for t in rows:
        print("  %-8d %-8d %-5d %-6d %-6d %-9.3f %-7s %s"
              % (t[0], t[1], t[2], t[3], t[4], t[5], t[6],
                 "yes" if t[7] else "no"))
    bad = [t for t in rows if (t[6] == "D") != t[7]]
    inside = [t for t in rows if 0.45 <= t[5] <= 0.95]
    print("  [K6] disagreements with the frozen predicate: %d of %d"
          % (len(bad), len(rows)))
    for t in bad:
        print("       d_K = %-8d d_0 = %-8d f = %-4d fraction %.3f  "
              "regime %s  predicate says %s"
              % (t[0], t[1], t[2], t[5], t[6], "D" if t[7] else "M"))
    print("  and the bimodality out of sample: %d fields with a fraction "
          "inside [0.45, 0.95]" % len(inside))
    return rows


def plus_conductor_2(f, d0):
    """The predicate S7 leaves behind, refined at 3 and nowhere else: a
    rational prime 1 mod 3 dividing f contributes a plus part however it
    sits in k, but the one-units at 3 contribute one only when 3 SPLITS
    there -- two primes swapped by conjugation, where an inert 3 leaves
    a single one and no plus line. 3 splits in k exactly when d_0 = 1
    mod 3. THE RAMIFIED CASE, 3 | d_0 with 9 | f, is NOT decided here
    and s8 prints how many fields sit in it. SETTLED SINCE: an inert 3
    DOES leave a plus line and the exclusion is that it cannot be used;
    the ramified case is decided the same way, and predicted UNIFORM --
    see F6's pointer and explore_ray_class_lines.py."""
    n, ns = f, []
    d = 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            ns.append((d, e))
        d += 1
    if n > 1:
        ns.append((n, 1))
    for (q, e) in ns:
        if q != 3 and q % 3 == 1:
            return True
    for (q, e) in ns:
        if q == 3 and e >= 2 and d0 % 3 == 1:
            return True
    return False


def band_rows(lo, hi):
    """Every complex field of relation class number 3 with a readable
    equal-class fraction in lo < |d_K| <= hi."""
    fields, _ = ECP.enumerate_fields(hi)
    band = [f for f in fields if lo < f[0] <= hi and f[2]]
    rows, n_un = [], 0
    for (ad, d, cx, polys) in band:
        a, b, c, O = polys[0]
        h, kind, gp, rel = ECST.CCM.class_and_relations(
            O, d, cx, ECP.t2_rows(O, a, b, c))
        if h is None:
            n_un += 1
            continue
        if h != 3:
            continue
        H_map, piv, k, per_prime = ECST.read_field(O, a, b, c, d, cx, gp, rel)
        if H_map != 3:
            continue
        ns, ne = ECST.field_stats(per_prime, piv, k)[:2]
        if ns < MIN_SPLIT:
            continue
        frac = float(ne) / ns
        d0, f = fundamental_part(d)
        rows.append((d, d0, f, ns, ne, frac,
                     "D" if frac >= HIGH_FRAC else "M"))
    return rows, len(band), n_un


def s8_second_band():
    section("S8  THE SECOND HELD-OUT BAND -- the REFINED predicate, "
            "frozen after S7's two disagreements and run on a band "
            "neither it nor they have seen")
    print("  the refined predicate: degenerate exactly when a rational "
          "prime 1 mod 3 divides the conductor, or 9 divides it AND 3 "
          "splits in k. The refinement is fitted on S7's two "
          "disagreements, both at f = 18, so this band is the only "
          "out-of-sample reading of it there will be. K7: any "
          "disagreement kills it.")
    t0 = time.time()
    rows, n_band, n_un = band_rows(HELD_HI, SECOND_HI)
    print("  %d complex fields in %d < |d_K| <= %d, %d at class number 3 "
          "with a readable fraction, %d unresolved and skipped, %.1f s"
          % (n_band, HELD_HI, SECOND_HI, len(rows), n_un,
             time.time() - t0))
    rows.sort(key=lambda t: (t[6], abs(t[0])))
    print("  %-8s %-8s %-5s %-6s %-6s %-9s %-7s %s"
          % ("d_K", "d_0", "f", "split", "equal", "fraction", "regime",
             "refined"))
    for t in rows:
        p = plus_conductor_2(t[2], t[1])
        print("  %-8d %-8d %-5d %-6d %-6d %-9.3f %-7s %s"
              % (t[0], t[1], t[2], t[3], t[4], t[5], t[6],
                 "D" if p else "M"))
    bad = [t for t in rows if (t[6] == "D") != plus_conductor_2(t[2], t[1])]
    old = [t for t in rows
           if (t[6] == "D") != plus_conductor(t[2])]
    undec = [t for t in rows if t[2] % 9 == 0 and t[1] % 3 == 0]
    inside = [t for t in rows if 0.45 <= t[5] <= 0.95]
    print("  [K7] disagreements with the REFINED predicate: %d of %d"
          % (len(bad), len(rows)))
    for t in bad:
        print("       d_K = %-8d d_0 = %-8d f = %-4d fraction %.3f  "
              "regime %s" % (t[0], t[1], t[2], t[5], t[6]))
    print("  the same band against S7's UNREFINED predicate: %d "
          "disagreements -- the refinement's whole value" % len(old))
    print("  fields in the undecided corner (9 | f and 3 ramified in k): "
          "%d" % len(undec))
    print("  bimodality: %d fields with a fraction inside [0.45, 0.95]"
          % len(inside))
    return rows


def main():
    t0 = time.time()
    s1_form_engine()
    recs, mapped = s2_population()
    fam = s3_resolvent_count(recs)
    rows = s4_table(recs, mapped, fam)
    s5_crosstabs(rows)
    s6_conductor_rule(rows, mapped)
    s7_held_out()
    s8_second_band()
    section("SUMMARY")
    print("  %d checks passed here, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
