r"""IS THE FIXED-LINE STEP LOAD-BEARING, AND CAN IT BE DERIVED? -- the
second line of E priced when it is INVERTED rather than fixed, and the
step both congruence clauses hang from proved from the one place the
argument had not looked: that conjugation fixes the cubic field
pointwise.

THE FINDING THIS INTERROGATES. explore_ray_class_lines.py derivation
(9) names one step neither it nor explore_cubic_regime_sorter.py
derives: that E, the degree-9 abelian extension of k whose existence
R = D asks for, must take its SECOND line FIXED by conjugation rather
than inverted. Granting it, derivation (6) prices the fixed lines and
reproduces the measured sorter exactly, on all 193 fields and for both
congruence clauses. Refuse it, and the mechanism proves nothing. This
file does two things to that step: it PRICES ITS ALTERNATIVE -- whether
a usable INVERTED second line is available where the regime is uniform,
which is what decides whether the step is load-bearing or vacuous --
and it DERIVES the step itself.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The step is
written in the vocabulary of the RAY CLASS GROUP: lines, fixed and
inverted, characters and their local components. That is the
vocabulary derivation (6) works in, and inside it the step looks like
a fact about which characters exist -- so the natural move is a census
of inverted lines, and that is the move this file was opened to make.
But the object the step is ABOUT is E = H_1 N, a field with a name, and
its Galois group over k carries a second structure the character
vocabulary does not see: the
subgroup Gal(E/N), which is Gal(H_1/K_1) transported. The step is a
fact about THAT subgroup and it is invisible in the ray class group,
where E is only "some degree-9 extension". So the census is run and the
proof is written in the other vocabulary.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM THE SORTER AND THE LINES FILE: the population, the conductor
    decomposition, the regime label, the module engine (Res, module,
    usable_fixed_line) and the form-based class group are imported and
    re-run, never re-implemented. What is new is one derivation and two
    columns.

 T2 THE REGIME LABEL IS A MEASUREMENT AND NOT A CERTIFICATE, inherited
    unchanged: degenerate when the equal-class fraction is at or above
    0.9 over at least 10 totally split primes.

 T3 AN ARGUMENT IS BEING RUN AT THE OPPOSITE SIGN. Derivation (6)
    prices FIXED lines and its whole content is an obstruction: a fixed
    character must be ramified somewhere over f, and where conjugation
    fixes a prime it cannot be. Everything below about INVERTED lines is
    that argument with the sign flipped, and the flip is not free -- the
    obstruction is the part that fails to transport, so derivation (2)
    below re-runs it prime by prime rather than negating a conclusion.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT AN INVERTED SECOND LINE WOULD HAVE TO BE. Keep the notation
      of explore_ray_class_lines.py: k the imaginary quadratic
      resolvent, chi the anti-invariant cubic character of conductor
      (f) cutting out N, and E an abelian extension of k of degree 9
      containing N with character group X = <chi, psi>. E/N unramified
      is the same local condition whichever sign psi has:

          psi|U_Q  lies in  <chi_Q>   for every Q dividing (f),

      and <chi_Q> has order 3 since chi is cubic. So a second line is
      USABLE exactly when its local components clear that condition;
      what changes with the sign is how hard it is to clear.

  (2) AND FOR AN INVERTED psi IT IS FREE. Take psi with psi o sigma =
      psi^-1 and of order 3. At a prime Q dividing (f):
        - sigma SWAPS Q with Qbar. Then the local 3-part at Q is cyclic
          (q =/= 3 split: (Z/q^e)^* ; q = 3 split: (Z/3^a)^* ), so the
          3-torsion of its dual has order 3 and chi_Q, being nontrivial
          of order 3, generates it. psi_Q has order dividing 3 and so
          lies there. No condition, and this is derivation (6)'s own
          reading of the swapped case.
        - sigma FIXES Q. Then psi inverted forces psi_Q anti-invariant,
          so psi_Q lies in the MINUS part of the local 3-part's dual --
          and so does chi_Q, which is anti-invariant and nontrivial. If
          that minus part has rank 1 its 3-torsion is exactly <chi_Q>
          and psi_Q lies in it automatically. Reading the cases
          derivations (3) and (4) there admit: q inert with q = 2 mod 3
          has cyclic local 3-part on which Frobenius inverts, minus rank
          1; 3 inert with 9 | f has F_9 additive with Frobenius, minus
          rank 1; 3 ramified with a = 1 has Q/Q^2, minus rank 1; and
          3 ramified with a = 2 is the one case not settled on paper and
          is MEASURED below. No other prime can divide a conductor.
      So, up to that one case, an inverted line is usable as soon as it
      EXISTS -- the exact opposite of the fixed side, where existence
      was the cheap half and usability did all the sorting. The
      asymmetry has one source: a nontrivial FIXED character of Cl_f(k)
      must be ramified somewhere (derivation (2) there: the plus part is
      purely local), while an inverted one may be unramified everywhere,
      the class group of an imaginary quadratic field being all minus.

  (3) SO THE QUESTION COLLAPSES TO A RANK. A usable inverted line exists
      exactly when Cl_f(k)_3 carries an inverted character of order 3
      independent of chi -- that is, when the minus rank of Cl_f(k)_3 is
      at least 2. Splitting on the conductor and on the ray class
      sequence 1 -> ((O_k/f)^*)_3/im(units) -> Cl_f(k)_3 -> Cl(k)_3 -> 1,
      whose minus parts are exact:
        - f = 1: Cl_f(k) = Cl(k), so the condition is 3-rank Cl(k) >= 2.
        - f > 1 and 3-rank Cl(k) >= 1: an unramified cubic character of
          k serves. It is inverted, Cl(k) being all minus, and it is
          independent of chi, which is ramified at f. Condition MET with
          no further computation.
        - f > 1 and 3-rank Cl(k) = 0: then Cl_f(k)_3 is the local part
          alone and the condition is that ITS minus rank is at least 2.
      The image of the global units is trivial at 3 except at d_0 = -3,
      where a cube root of unity contributes one INVERTED line and the
      local minus rank is read one lower.

  (4) WHICH MAKES THE CENSUS DECIDE ONE THING AND NOT ANOTHER. If usable
      inverted lines are common where the regime is uniform, then "some
      sigma-stable E of degree 9 exists, unramified over N" is not the
      sorter and cannot be: the fixed-line step is carrying the whole
      mechanism, and derivation (1) of the sorter needs E to be H_1 N
      specifically rather than merely some such field. If they are
      absent wherever the regime is uniform, the fixed/inverted
      asymmetry is an artifact of what a conductor can supply and the
      step dissolves. Either way this decides the step's WEIGHT and not
      its truth.

  (5) AND THE STEP IS TRUE, BY AN ARGUMENT IN THE OTHER VOCABULARY.
      Assume R = D. By the sorter's derivation (1), E = H_1 N = H_2 N =
      H_3 N is Galois over Q of degree 18 and E/k is abelian of degree
      9. Let tau in Gal(N/Q) be the transposition fixing K_1 pointwise
      -- transpositions are outside A_3, so tau restricts to the
      nontrivial element of Gal(k/Q), and any lift tau~ in Gal(E/Q)
      induces the conjugation action of sigma on the abelian group
      Gal(E/k). Now:
        - tau~ fixes K_1 pointwise, and H_1 is the Hilbert class field
          of K_1, which is canonical, so tau~(H_1) = H_1.
        - Conjugation by tau~ on Gal(H_1/K_1) is TRIVIAL, and no
          reciprocity is needed to see it: tau~ stabilizes H_1 and fixes
          K_1 pointwise, so tau~|H_1 is an ELEMENT of Gal(H_1/K_1),
          which is abelian.
        - Restriction Gal(E/N) -> Gal(H_1/K_1) is an isomorphism, since
          E = H_1 N and H_1 n N = K_1, and it commutes with conjugation
          by tau~, which stabilizes E, N and H_1. So sigma acts
          TRIVIALLY on the line Gal(E/N): it is a FIXED line of
          Gal(E/k).
        - Gal(E/k) has order 9 and |<sigma>| = 2 is invertible on it, so
          it splits into plus and minus parts. The minus part meets
          Gal(E/N) trivially -- sigma acts trivially on one and by
          inversion on the other, and x = x^-1 forces x = 1 in a
          3-group -- so it injects into the quotient Gal(N/k) and has
          order at most 3; and it is not trivial, since sigma INVERTS
          that quotient (tau gamma tau^-1 = gamma^-1 in S_3) and could
          not if the whole group were plus. So both parts have order 3,
          Gal(E/k) = Gal(E/N) + C is (Z/3)^2 rather than cyclic, and C
          maps isomorphically to Gal(N/k).
      Dualizing, X = X^+ + X^-, where X^- consists of the characters
      trivial on Gal(E/N) -- which is exactly <chi>, chi cutting out N
      -- and X^+ = Hom(Gal(E/N), mu_3) is nontrivial and FIXED. So the
      second line is fixed, and derivation (9) is closed.

  (6) SO THE UNIFORM HALF OF THE LAW IS UNCONDITIONAL. Chaining (5) into
      derivation (6) there: R = D forces a nontrivial fixed psi of
      conductor dividing f with psi|U_Q in <chi_Q> everywhere, which is
      a usable fixed line, which is a split prime of the conductor
      carrying a nontrivial local 3-part. Contrapositive: a field whose
      conductor carries no such prime is UNIFORM, with nothing granted.
      The CONVERSE is untouched and still needs the Hilbert class field
      of K built rather than bounded, so the biconditional stays where
      it is. (Settled later by explore_genus_index.py: the class field
      is the genus field KF, so a usable line forces R = D and the
      biconditional is a criterion at 3-rank 1; everything measured here
      survives.) The corner at 9 | f with 3 ramified in k inherits the same
      upgrade, its prediction having rested on the same step.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. USABILITY IS FREE FOR AN INVERTED LINE (derivation (2)). At every
      field of the population, every prime power q^e exactly dividing f
      with q inert or ramified in k has local 3-part of MINUS rank at
      most 1. (This is what makes the one unsettled case -- 3 ramified
      with a = 2 -- a measurement rather than a hole.)

  P2. USABLE INVERTED LINES ARE COMMON WHERE THE REGIME IS UNIFORM
      (derivation (3)). More than half of the 123 uniform fields carry
      one.

  P3. AND THE INVERTED PREDICATE DOES NOT SORT. It disagrees with the
      regime on at least 10 fields. (Frozen separately from P2 because
      "common at uniform fields" and "not a sorter" are different
      statements: a predicate could be common at uniform fields and
      universal at degenerate ones, which would still be a sorter's
      complement.)

  P4. AND THE DEGENERATE FIELDS CARRY BOTH KINDS. At least one
      degenerate field carries a usable inverted line as well as the
      usable fixed one derivation (6) gives it -- so the two lines are
      not alternatives a field chooses between.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed count of (field, prime power) pairs at a
     sigma-fixed prime with local minus rank above 1. Any value above 0
     kills it, and the inverted column below is then not exact and is
     reported as inexact rather than read.

  K2 kills P2: the printed count of uniform fields carrying a usable
     inverted line, against 123. At or below 61 it is killed.

  K3 kills P3: the printed count of disagreements between the inverted
     predicate and the regime. Below 10 kills it; ZERO would mean the
     inverted line sorts as well as the fixed one, which would make the
     mechanism's sign a coincidence and is the outcome that would hurt.

  K4 kills P4: the printed count of degenerate fields carrying a usable
     inverted line. Zero kills it.

THE CONTROLS, run before any of the above is read.

  C1. THE MODULE ENGINE, re-run in this process. explore_ray_class_lines
      .py's S1 -- the brute-forced unit group against the Euler product,
      conjugation multiplicative and involutive, the 3-Sylow order, the
      plus/minus ranks summing to the total, and the CRT factorization.

  C2. THE POPULATION REPRODUCED: 193 fields, 70 degenerate, 123 uniform.

  C3. CHI'S OWN LINE IS THERE. chi is inverted and ramified at every
      prime of (f), so the minus rank of the 3-part of (O_k/f)^* must be
      at least 1 at every field with f > 1. The printed count of
      violations must be 0 -- a control on the minus rank itself, which
      is the column P2 and P3 are read off.

  C4. THE NAMED WITNESS. d_K = -1228 over d_0 = -307 at f = 2 is the
      discriminant already on record as carrying an inverted second
      line, with the class group supplying one and the inert 2 the
      other:
      3-rank Cl(k) >= 1 and local minus rank exactly 1 at f = 2, and the
      regime uniform. Computed here from the two engines and checked
      against that reading, so a broken column cannot agree by accident.

  C5. AND THE FIXED COLUMN IS RE-READ, NOT RE-DISCOVERED. The usable
      fixed line still disagrees with the regime nowhere, 0 of 193 --
      explore_ray_class_lines.py F4 recomputed here because derivation
      (6) above now reads it as a derived rule in one direction rather
      than a pattern, and a rule whose data moved would be worse than a
      pattern whose data moved.

THE FINDINGS.

  F1. THE ENGINE AND THE POPULATION REPRODUCE, AND THE NAMED WITNESS IS
      A FAMILY (S1-S3). The module engine's five controls read 0 bad
      over 81 discriminant-modulus pairs; the population re-reads as 193
      fields, 70 degenerate and 123 uniform; and no field with f > 1
      loses chi's own inverted line, the minus rank being at least 1 at
      every one of them. THE C4 PIN FIRED, on the pin's arithmetic and
      not on a column: d_K = -1228 was frozen as a field and it is a
      FAMILY OF THREE, all three at d_0 = -307, f = 2, 3-rank Cl(k) = 1,
      minus rank 1, an inverted line and the uniform regime. Every
      column here is a function of (d_0, f), so a family shares them all
      and every reading taken off that discriminant is unaffected; what
      the correction adds is that the three agree on
      the regime too. The family size is the sorter's own derivation
      (5): at f > 1 a ray class group counts the family and 2 and 3
      occur there.

  F2. USABILITY IS FREE FOR AN INVERTED LINE EXCEPT AT ONE
      CONFIGURATION, AND ONE FIELD OCCUPIES IT (K1 = 1; S4). Over the
      sigma-fixed prime powers of the 193 conductors the local minus
      rank is 1 at every one of the 96 inert q = 2 mod 3, the 2 inert
      3^2 and the 29 ramified 3^1 -- and 2 at the single ramified 3^2,
      which is d_K = -11907 at d_0 = -3, f = 63. THE ROW LABELS LEAN ON
      A LAW RATHER THAN ON THE ROWS: S4 names every sigma-fixed prime
      other than 3 as q = 2 mod 3, which is the admissible-prime law of
      explore_ray_class_lines.py F2 and is verified there at 0
      violations over exactly this population -- on a population that
      law was not checked over, those labels would have to be recomputed
      from q. So P1 is KILLED, and
      exactly where derivation (2) said it might be: the one case it
      could not settle on paper is the one that misbehaves. WHAT THAT
      COSTS IS ONE FIELD AND IT IS NAMED: the inverted column is exact
      at 192 fields and unverified at d_K = -11907, where an inverted
      psi must land in a rank-2 minus space rather than a line and
      nothing here checks that it can. That field is DEGENERATE and
      carries a usable fixed line, so every reading taken over the
      UNIFORM fields is untouched by it and so is F4, where it supplies
      its E by the fixed line whatever the inverted one does. The one
      reading it enters is F3's count of degenerate fields carrying an
      inverted line, which is therefore 15 with one of them asserted
      from a rank rather than checked.

  F3. EVERY UNIFORM FIELD CARRIES A USABLE INVERTED LINE (pattern, 123
      of 123; K2, K4, K3; S5). Not a majority -- all of them, and every
      one of the 123 sits in a configuration F2's exception does not
      reach, so the column is exact exactly where this reading is taken.
      Fifteen of
      the 70 degenerate fields carry one as well, so the predicate
      disagrees with the regime at 178 of 193 and the joint table has
      three cells: 123 uniform with an inverted line and no usable fixed
      one, 15 degenerate with both, 55 degenerate with the fixed one
      alone. The inverted line's source splits four ways over the 138
      fields that have one: 39 unramified at f = 1 with 3-rank Cl(k) at
      least 2, 64 unramified at f > 1 with 3-rank at least 1, 3 with
      both routes open, and 32 from the conductor alone at 3-rank 0. So
      it is not one mechanism appearing everywhere but two independent
      supplies, either of which suffices.

  F4. WHICH MAKES THE EXISTENCE OF E UNIVERSAL, AND THE FIXED-LINE STEP
      THE WHOLE MECHANISM (pattern, 193 of 193; S5). Every field of the
      population carries a sigma-stable abelian E of degree 9 over k,
      unramified over N: 138 via an inverted second line and the
      remaining 55 via the fixed one derivation (6) prices. So "such an
      E exists" is not a weak sorter, it is a CONSTANT on this
      population and sorts nothing at all. Derivation (9)'s step is
      therefore not a technical tidy-up -- it carries the entire
      distance between the mechanism and the measured law. AND THE
      MODALITY IS WORTH STATING EXACTLY, since a necessary condition is
      easy to read backwards: with the fixedness dropped the mechanism
      EXCLUDES no field from R = D, so it can never predict the uniform
      regime at all -- which is not the same as predicting the
      degenerate one, and is a weaker and worse position. This is the
      answer to what the census was run for, and it is the sharper of
      the two answers it could have given.

  F5. AND THE STEP IS DERIVED, IN THE VOCABULARY THE CENSUS DOES NOT USE
      (rule, proved at derivation (5); no measurement enters). E = H_1 N
      carries a structure no ray class computation sees: the line
      Gal(E/N), which restriction identifies with Gal(H_1/K_1). The
      transposition fixing K_1 pointwise restricts to the nontrivial
      element of Gal(k/Q) and so induces sigma -- and it acts TRIVIALLY
      on Gal(H_1/K_1), being an ELEMENT of that abelian group.
      Hence Gal(E/N) is a FIXED line of Gal(E/k); the quotient
      Gal(N/k) is inverted; and 2 being invertible on a group of order 9
      splits the module, with an order count then forcing both parts to
      have order 3 -- so Gal(E/k) is (Z/3)^2 and there are two lines to
      talk about at all. Dualizing, the character group is <chi> plus a
      nontrivial FIXED line. So the second line is fixed, necessarily.

  F6. SO THE UNIFORM HALF OF THE LAW IS UNCONDITIONAL AND THE CORNER
      INHERITS IT (rule, proved; the fixed column re-read at 0 of 193,
      C5). Chaining F5 into derivation (6) there: R = D forces a usable
      fixed line, which forces a split prime of the conductor with
      nontrivial local 3-part. Contrapositive, and nothing granted: a
      complex cubic field of relation class number 3 whose conductor
      carries no such prime is UNIFORM. The 193 fields agree with it and
      no longer carry it. The CONVERSE is untouched, still needs the
      Hilbert class field of K built rather than bounded, and is why the
      biconditional stays at pattern (settled later by
      explore_genus_index.py, which proves it through the genus field
      KF; this record's own findings stand). The corner at 9 | f with 3
      ramified in k had its prediction resting on the same step and is
      upgraded with it -- the population's one such field, d_K = -11907
      at f = 63, is decided the other way by the 7 in its conductor and
      reads degenerate, exactly as explore_ray_class_lines.py F7 says.

  F7. AND THE PRINTS CARRY ONE THING THE SLATE DID NOT ASK FOR, WHICH
      IS DERIVABLE AND STRONGER THAN WHAT STOOD (rule, proved; observed
      39 of 39; S5). The joint table has no cell at all for "no inverted
      line and no fixed one", and a field with f = 1 can have no fixed
      line -- there is no prime of the conductor to carry one. So every
      f = 1 field of the population is in the inverted column, which the
      source tally counts at 39, and by derivation (3) each of those has
      3-rank Cl(k) at least 2. ALL of them, against a base rate where
      3-rank 1 is the fundamental discriminant's overwhelming case --
      explore_cubic_regime_sorter.py F1 reads 603 of 607 at family size
      1, which is 3-rank 1, over the fundamental discriminants carrying
      ANY complex cubic field below 6000. That is a different population
      over a shorter range, and naming it that way is the comparison:
      what is being contrasted is a base rate, not a matched control.
      AND IT IS FORCED. At f = 1, N/k is
      unramified, and H_i N/N is unramified for each conjugate, so H~/k
      is an unramified Galois extension and G = Gal(H~/k) has its
      ABELIANIZATION a quotient of Cl(k) -- G itself is not abelian at
      R = M, and the step that survives that is Burnside's: a 3-group
      and its abelianization need the same number of generators.
      |G| = 3|R|, and R is D or M since Cl(K) = Z/3 (R = 0 would put a
      degree-9 field inside N): at R = M, G has order 27 and contains
      M = (Z/3)^2, so it is not cyclic and needs two; at R = D, G is
      Gal(E/k), which derivation (5) shows is (Z/3)^2. Either way
      G^ab needs two generators and is a quotient of Cl(k), so

          f = 1 and Cl(K) = Z/3  ==>  3-rank Cl(k) >= 2.

      That strictly strengthens explore_cubic_regime_sorter.py
      derivation (4), which concluded only 9 | h(k) and only under
      R = D -- and R = D at f = 1 is now excluded outright by F6, there
      being no conductor prime to supply the fixed line. So those 39 --
      a fifth of the population, not a half of it -- are not a sample of
      resolvents at all, and a covariate read across the whole
      population is reading them through a constraint the other four
      fifths do not carry.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_ray_class_inverted.py`. One process, CPython, no
BLAS. 12 checks, 359.7 s wall, peak working set 93.0 MB against
memwatch's 512 MB ceiling. 359.6 s of it is the population, re-read in
one pass to |d_K| <= 13000 exactly as its predecessor reads it; the
module engine's controls and all 193 ray class computations together
run in under 0.2 s. An earlier run of the same length was spent on the
C4 pin firing (F1), which is the price of a control frozen against a
discriminant rather than against a field.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_regime_sorter as ECRS
import explore_ray_class_lines as ERCL

CHECKS = 0

CAP = ERCL.CAP
N_FIELDS, N_DEG, N_UNI = ERCL.N_FIELDS, ERCL.N_DEG, ERCL.N_UNI


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


def fixed_prime_minus_ranks(d0, f):
    """[(q, e, minus_rank)] over the prime powers exactly dividing f
    whose prime is INERT or RAMIFIED in k -- the primes conjugation
    fixes, which are the only ones derivation (2) has to argue at."""
    out = []
    for (q, e) in ERCL.prime_powers(f):
        if ERCL.splitting(d0, q) == "split":
            continue
        out.append((q, e, ERCL.module(d0, q ** e)[4]))
    return out


def inverted_line(d0, f, r3, rm):
    """Derivation (3): a usable inverted second line exists exactly
    when the minus rank of Cl_f(k)_3 is at least 2. r3 is the 3-rank of
    Cl(k); rm the minus rank of the 3-part of (O_k/f)^*, read one lower
    at d_0 = -3 where the cube roots of unity contribute an inverted
    line that the ray class quotient removes."""
    loc = rm - 1 if d0 == -3 else rm
    if f == 1:
        return r3 >= 2
    return r3 >= 1 or loc >= 2


# --------------------------------------------------------- the sections
def s1_engine():
    section("S1  C1 THE MODULE ENGINE -- re-run in this process")
    ERCL.s1_engine()


def s2_population():
    section("S2  C2 THE POPULATION, RE-READ IN ONE PASS TO |d_K| <= %d"
            % CAP)
    t0 = time.time()
    rows, n_band, n_un = ECRS.band_rows(0, CAP)
    nd = sum(1 for t in rows if t[6] == "D")
    nm = sum(1 for t in rows if t[6] == "M")
    print("  %d complex fields enumerated, %d at relation class number 3 "
          "with a readable fraction, %d unresolved and skipped, %.1f s"
          % (n_band, len(rows), n_un, time.time() - t0))
    print("  [C2] %d degenerate, %d uniform (expected %d and %d over %d)"
          % (nd, nm, N_DEG, N_UNI, N_FIELDS))
    ok(len(rows) == N_FIELDS, "%d fields, expected %d"
       % (len(rows), N_FIELDS))
    ok(nd == N_DEG, "%d degenerate, expected %d" % (nd, N_DEG))
    ok(nm == N_UNI, "%d uniform, expected %d" % (nm, N_UNI))
    return rows


def s3_columns(rows):
    section("S3  C3 C4 THE TWO COLUMNS -- the resolvent's 3-rank and the "
            "conductor's minus rank, with chi's own line as the control")
    out = []
    t0 = time.time()
    for (d, d0, f, ns, ne, frac, label) in rows:
        r3 = ECRS.class_group(d0)[3]
        n, s3, r, rp, rm = ERCL.module(d0, f)
        out.append((d, d0, f, r3, rp, rm,
                    ERCL.usable_fixed_line(d0, f),
                    inverted_line(d0, f, r3, rm), label))
    print("  %d fields, %.1f s" % (len(out), time.time() - t0))

    flat = [t for t in out if t[2] > 1 and t[5] == 0]
    print("  [C3] fields with f > 1 and minus rank 0 (chi's own line "
          "missing): %d" % len(flat))
    for t in flat[:8]:
        print("       d_K = %-8d d_0 = %-8d f = %-4d" % (t[0], t[1], t[2]))
    ok(not flat, "%d fields lose chi's own inverted line" % len(flat))

    wit = [t for t in out if t[0] == -1228]
    print("  [C4] the named witness, d_K = -1228, WHICH IS A FAMILY AND "
          "NOT A FIELD: the pin as frozen expected one field and the "
          "discriminant carries three, every column below being a "
          "function of (d_0, f) and so shared by all of them. That is the "
          "sorter's own derivation (5) -- at f > 1 a ray class group "
          "counts the family and sizes 2 and 3 occur -- so the correction "
          "is to the pin's arithmetic and not to a column, and what it "
          "adds is that the regime is homogeneous across the three.")
    for t in wit:
        print("       d_0 = %-8d f = %-4d 3-rank Cl(k) = %d  plus rank %d  "
              "minus rank %d  inverted line: %s  regime %s"
              % (t[1], t[2], t[3], t[4], t[5], "yes" if t[7] else "no",
                 t[8]))
    ok(len(wit) == 3, "%d fields at d_K = -1228, expected 3" % len(wit))
    ok(len(set(t[8] for t in wit)) == 1,
       "the family at d_K = -1228 is regime-mixed")
    w = wit[0]
    ok(w[1] == -307 and w[2] == 2, "witness resolvent/conductor is %d, %d"
       % (w[1], w[2]))
    ok(w[3] >= 1, "witness 3-rank Cl(k) is %d, expected at least 1" % w[3])
    ok(w[5] == 1, "witness minus rank is %d, expected 1" % w[5])
    ok(w[8] == "M", "witness regime is %s, expected M" % w[8])
    ok(w[7], "witness carries no inverted line")

    n3 = sum(1 for t in out if t[1] == -3)
    print("  fields at d_0 = -3, where the unit image is read out of the "
          "minus rank: %d" % n3)
    return out


def s4_free(out):
    section("S4  K1 IS USABILITY FREE FOR AN INVERTED LINE -- the local "
            "minus ranks at the primes conjugation FIXES")
    tally, bad = {}, []
    for t in out:
        for (q, e, mr) in fixed_prime_minus_ranks(t[1], t[2]):
            s = ERCL.splitting(t[1], q)
            key = ("q = 3" if q == 3 else "q = 2 mod 3", s, e, mr)
            tally[key] = tally.get(key, 0) + 1
            if mr > 1:
                bad.append((t[0], t[1], t[2], q, e, mr))
    print("  %-14s %-8s %-4s %-12s %s"
          % ("prime class", "in k", "exp", "minus rank", "occurrences"))
    for key in sorted(tally):
        print("  %-14s %-8s %-4d %-12d %d"
              % (key[0], key[1], key[2], key[3], tally[key]))
    print("  [K1] sigma-fixed prime powers with local minus rank above 1: "
          "%d" % len(bad))
    for t in bad[:8]:
        print("       d_K = %-8d d_0 = %-8d f = %-4d q = %d^%d minus rank "
              "%d" % t)
    return bad


def s5_crosstab(out):
    section("S5  K2 K3 K4 THE INVERTED LINE AGAINST THE REGIME")
    inv_u = [t for t in out if t[8] == "M" and t[7]]
    inv_d = [t for t in out if t[8] == "D" and t[7]]
    dis = [t for t in out if (t[8] == "D") != t[7]]
    print("  [K2] uniform fields carrying a usable inverted line: %d of %d"
          % (len(inv_u), N_UNI))
    print("  [K4] degenerate fields carrying one: %d of %d"
          % (len(inv_d), N_DEG))
    print("  [K3] disagreements between the inverted predicate and the "
          "regime: %d of %d" % (len(dis), len(out)))

    print("  the joint table, inverted against fixed against regime:")
    joint = {}
    for t in out:
        joint[(t[7], t[6], t[8])] = joint.get((t[7], t[6], t[8]), 0) + 1
    print("  %-12s %-12s %-8s %s"
          % ("inverted", "fixed usable", "regime", "fields"))
    for key in sorted(joint):
        print("  %-12s %-12s %-8s %d"
              % ("yes" if key[0] else "no", "yes" if key[1] else "no",
                 key[2], joint[key]))

    print("  and where the inverted line COMES FROM, over the fields that "
          "carry one:")
    src = {}
    for t in out:
        if not t[7]:
            continue
        loc = t[5] - 1 if t[1] == -3 else t[5]
        if t[2] == 1:
            key = "unramified, f = 1 and 3-rank Cl(k) >= 2"
        elif t[3] >= 1:
            key = ("unramified, 3-rank Cl(k) >= 1"
                   + (" (and the conductor supplies one too)"
                      if loc >= 2 else ""))
        else:
            key = "the conductor alone, minus rank >= 2 with 3-rank 0"
        src[key] = src.get(key, 0) + 1
    for key in sorted(src):
        print("  %-58s %d" % (key, src[key]))

    fixed_bad = [t for t in out if (t[8] == "D") != t[6]]
    print("  [C5] disagreements between the usable FIXED line and the "
          "regime: %d of %d" % (len(fixed_bad), len(out)))
    ok(not fixed_bad, "%d fields disagree with the fixed-line rule"
       % len(fixed_bad))
    return inv_u, inv_d, dis


def s6_corner(out):
    section("S6  THE CORNER RE-READ -- 9 | f with 3 RAMIFIED in k, whose "
            "prediction inherited the step derivation (5) closes")
    corner = [t for t in out if t[2] % 9 == 0 and t[1] % 3 == 0]
    print("  fields with 9 | f and 3 ramified in k: %d" % len(corner))
    for t in corner:
        print("       d_K = %-8d d_0 = %-8d f = %-4d plus rank %d  "
              "minus rank %d  fixed usable %-4s inverted %-4s regime %s"
              % (t[0], t[1], t[2], t[4], t[5], "yes" if t[6] else "no",
                 "yes" if t[7] else "no", t[8]))
    print("  the prediction there is UNIFORM and it is now derived rather "
          "than granted: no census reaches the clean corner, and what it "
          "rested on was derivation (9), which derivation (5) above "
          "closes.")
    return corner


def main():
    t0 = time.time()
    s1_engine()
    rows = s2_population()
    out = s3_columns(rows)
    s4_free(out)
    s5_crosstab(out)
    s6_corner(out)
    section("SUMMARY")
    print("  %d checks passed here, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
