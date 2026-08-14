"""IS THE PRINCIPAL SHARE'S DEFICIT AN EQUIDISTRIBUTION EFFECT? -- the
share of split primes that are principal, read as a FUNCTION of p and
decomposed against the genus characters, over BOTH signs of D.

THE QUESTION. explore_real_principal.py removed the coverage floor by
running the least principal rank-1 characteristic L_1 over REAL quadratic
fields, where the unit group is infinite and the norm form indefinite.
The floor vanished, and what it exposed was that the floor had never been
the whole explanation of a second number: the first-hit model at density
1/(2h) still undershoots, by 1.15x at h = 1 rising to 3.23x by h = 6.
Its K5 then found the mechanism's signature without going through L_1 at
all -- the PRINCIPAL SHARE of split primes p <= 1000 is short of the
nominal 1/h and shorter as h grows, 0.67 of nominal by h = 8 against
exactly 1 at h = 1. That buys about 1.33x of the 3.23x at h = 6 and no
more, which is what a bottom-of-range effect looks like averaged over a
whole range.

So the sharp question is the one that rig printed and did not answer: the
share as a FUNCTION of p. If it climbs toward 1/h as p grows, the
undershoot is equidistribution and nothing else, and the residual is
priced rather than open. If it is FLAT in p, the deficit is not a
bottom-of-range effect at all and something else is grading the share by
the class number.

THE SUSPICION IN ITS OWN VOCABULARY. The standing one is a CONGRUENCE
suspicion and not a size one: the genus congruences mod D have not
equidistributed at primes small against D. The genus characters are
what that sentence is about, so they are what this rig measures, rather
than a p-trend read off the share alone. Note whose vocabulary the
statistic is written in: 1/h and 1/(2h) are CLASS GROUP quantities, while
"the congruences have not equidistributed" is a statement about a
QUOTIENT of that group -- and the quotient has its own nominal value,
which is the whole of the decomposition below.

THE TRANSPLANT, FLAGGED. Every expectation here about a climb is imported
from the pooled reading at p <= 1000, a single value of the very
parameter this rig varies. The pooled number cannot see a trend, and a
deficit that is flat in p is fully consistent with everything measured so
far. P1 is what that import commits to and K1 is what refuses it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE GROUP TO READ IT IN IS THE NARROW ONE. Genus theory is stated
      on the narrow class group: for a fundamental discriminant D with t
      prime discriminant factors D = D_1 * ... * D_t (each -4, +-8, or
      p* = (-1)^((p-1)/2) p), the genus characters chi_{D_i} cut the
      narrow class group Cl+ onto (Z/2)^(t-1), so the number of genera is
      2^(t-1) and the principal genus has index 2^(t-1) in Cl+. A prime p
      coprime to D is represented by a form in the PRINCIPAL GENUS
      exactly when chi_{D_i}(p) = +1 for every i. The product of those t
      characters is chi_D(p), which is +1 for every split p, so the
      constraint is not t independent bits but t-1 -- which is why the
      nominal is 2^(t-1) and not 2^t.

      The incumbent's WIDE statistic (the ideal class group, the sign
      disjunction over +-p) is the one L_1 and K5 are written in, and it
      is kept here as a separate column for continuity. But the
      decomposition runs on the NARROW group, because that is the group
      the genus characters are defined on. Two nominals, then, and they
      are not the same number: 1/h for the wide share, 1/h+ for the
      narrow one.

  (2) THE DECOMPOSITION IS EXACT AND HAS TWO FACTORS. Narrow principal
      implies principal genus, so for any population of split primes

          share_narrow  =  share_genus  x  share_within,

      where share_genus is the fraction lying in the principal genus and
      share_within the fraction of THOSE that are narrow principal. The
      nominals multiply the same way: 1/h+ = (1/2^(t-1)) x (2^(t-1)/h+).
      So the deficit the pooled reading found has to sit in one factor or
      the other, and which one it sits in is the whole finding. The
      suspicion names the genus factor. Nothing in the pooled number
      chose between them, because the pooled number never split them.

  (3) THE SUSPICION HAS A POPULATION WHERE IT PREDICTS NOTHING, AND THAT
      IS THE SHARP TEST. At t = 1 -- D itself a prime discriminant --
      there is ONE genus, the single character is chi_D, and chi_D(p) =
      +1 holds for every split p by definition. So share_genus is
      IDENTICALLY 1 at those fields, not approximately: the genus factor
      cannot carry any deficit there at all. If the share is short at
      t = 1 too, and short by a margin that grows with h in the same way,
      the congruence explanation is refuted on its own terms rather than
      merely unsupported. This is a partition of the field population and
      not a second statistic, which is what makes it cheap.

  (4) WHY BOTH SIGNS, AND WHAT THE FLOOR DOES TO THE IMAGINARY ONE. The
      same share is defined at D < 0 and the same decomposition holds
      there, the genus theory being indifferent to the sign. What differs
      is the floor: below |D|/4 no split prime is principal at all, so
      the imaginary share is identically ZERO there and any comparison
      across the two signs that includes that region is measuring the
      floor a second time rather than the congruences. The population
      here runs to |D| <= 4000, so |D|/4 <= 1000 -- every bin ABOVE 1000
      is floor-free at every field in the sweep, which is why the bin
      edges are placed where they are. The imaginary side's own bottom
      bin is reported and is not comparable; it is the one place the two
      signs are expected to disagree for a reason already known.

  (5) THE TEST ITSELF. For odd p with chi_D(p) = +1, take b with
      b^2 = D mod 4p and b = D mod 2 (Tonelli mod p, parity fixed mod 2).
      Then (p, b, (b^2-D)/(4p)) has discriminant D and represents p. At
      D > 0 it is narrow principal iff its reduction lies in the
      PRINCIPAL CYCLE, and wide principal iff that holds for either sign
      of p (explore_real_principal.py derivation 3). At D < 0 forms are
      definite with a unique reduced representative per class, narrow and
      wide coincide, and the test is equality with the reduced principal
      form. The imaginary branch is a FORM test here rather than the
      incumbent's loop over y in 4p = u^2 + |D|y^2: the loop is bounded
      by |D|y^2 <= 4p and so grows with p, and this rig runs p ten times
      further than that rig did. Control C4 is what licenses the swap.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE.

  P1. THE SHARE CLIMBS WITH p. At every class number with a deficit at
      p <= 1000, the share's ratio to nominal is closer to 1 in the top
      prime bin than in the bottom one, on the real side.

  P2. THE DEFICIT IS THE GENUS FACTOR'S. share_genus sits below
      1/2^(t-1) at the bottom bin and climbs toward it; share_within is
      flat against 2^(t-1)/h+ across the bins, carrying no trend of
      comparable size.

  P3. AT t = 1 THERE IS NO DEFICIT LEFT TO FIND. Restricted to fields
      whose discriminant is itself a prime discriminant, the narrow share
      sits at its nominal 1/h+ in every bin including the bottom one,
      because the factor that carries the deficit is identically 1 there.

  P4. BOTH SIGNS AGREE ABOVE THE FLOOR. In the bins above p = 1000, the
      imaginary side's share-to-nominal ratios track the real side's at
      equal h, the genus mechanism being indifferent to the sign of D.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the
controls and never before.

  K1 kills P1: the printed per-(h, bin) ratio share x h+ on the real
     side. If at some h >= 4 the top bin's ratio is no nearer 1 than the
     bottom bin's -- printed as both numbers side by side -- P1 dies at
     that h. A ratio that MOVES AWAY from 1 kills it outright.

  K2 kills P2: the printed per-bin share_genus x 2^(t-1) and
     share_within x h+/2^(t-1), pooled over the strata. A within-genus
     trend of the same sign and comparable size to the genus trend kills
     the attribution; a genus factor already at 1 in the bottom bin kills
     it the other way.

  K3 kills P3: the printed t = 1 table, narrow share against 1/h+ by
     bin. A bottom-bin ratio at t = 1 as far from 1 as the all-t one at
     the same h kills P3.

  K4 kills P4: the printed imaginary table beside the real one, bins
     above 1000 only.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. THE INSTRUMENT PIN AT h = 1. Over a field with narrow class number
      1 every split prime is narrow principal, so the share must be
      exactly 1.0000 in EVERY bin and at both signs. Any binning
      apparatus that shows a p-dependence there is broken before it is
      read -- this is the trap the roadmap named, and it is a control and
      not a finding.

  C2. THE INCUMBENT REGRESSION. Restricted to p <= 1000 and to the same
      population and filters explore_real_principal.py's K5 used (real
      fundamental discriminants to 4000, fields with at least 20 split
      primes below the cap, strata of at least 4, the mean taken over
      FIELDS and not pooled over pairs), the WIDE share must reproduce
      that rig's printed 1.0000, 0.4573, 0.2975, 0.2033, 0.1626, 0.1252,
      0.1060, 0.0841 at h = 1..8. A new rig that disagrees with the
      incumbent on the incumbent's own statistic is wrong until shown
      otherwise.

  C3. GENUS CONTAINMENT, AND EXACTNESS WHERE THE QUOTIENT IS EVERYTHING.
      Narrow principal must imply the principal genus at every pair
      tested -- a containment, printed as a violation count. And at
      fields where 2^(t-1) = h+ (one class per genus) the two shares must
      agree EXACTLY at every field and every bin, since the principal
      genus is then the principal class.

  C5. GENUS DIVISIBILITY, WHICH PINS THE CLASS NUMBERS THEMSELVES.
      2^(t-1) is the order of a QUOTIENT of the narrow class group, so
      it must DIVIDE h+ at every field of either sign. Nothing else here
      tests the imaginary class number above h = 1 -- C1 pins only the
      h+ = 1 fields, and a wrong count at any larger h would relabel a
      whole row of every imaginary table without moving a single share.
      This is the cheap independent check that closes that hole, and it
      is a genuine one: it is derived from the genus theory rather than
      from the counting loop it audits.

  C4. THE DEFINITE FORM TEST AGAINST THE INCUMBENT LOOP. On the
      imaginary side the form test must agree with
      explore_real_principal.py's is_principal_imag -- the u^2 + |D|y^2
      search -- at every pair tried below the incumbent's own cap, which
      is what licenses running the form test past that cap.

THE FOLLOW-UP SLATE -- frozen AFTER the first four kills printed and
BEFORE the second engine, and flagged as post-hoc for that reason.

  THE CONFOUND. Reading K1 exposed one that the incumbent's own claim
  rests on and neither rig had isolated. The deficit is reported as
  GRADED BY THE CLASS NUMBER -- here, and as F3/F5 in
  explore_real_principal.py, and on the public page. But h grows with |D|
  (Siegel), and the population is a |D| range, so every stratum with a
  large h is also a stratum with a large mean |D|. "Short by more as h
  grows" and "short by more as |D| grows" are not distinguished by any
  table above. And the |D| reading is the one the equidistribution
  suspicion actually predicts, since what is small is p AGAINST D.

  P5. THE GRADING IS |D|'s, AND h IS ITS PROXY. Cut the same share ratio
      two ways at once -- by h+ and by |D| band. If the grading is |D|'s,
      the ratio falls DOWN a column (fixed h+, rising |D|) and is flat
      ACROSS a row (fixed |D|, rising h+).

  K5 kills P5: the printed two-way table of the share ratio by (h+, |D|
     band), on both signs -- the imaginary side carrying the wider h
     range at equal |D| and so the sharper read. A ratio that falls
     across a row at fixed |D| by as much as it falls down a column
     kills P5, and the class number keeps its grading.

  WHAT K5's ANSWER THEN OWES, frozen before its own engine. If the
  grading is the class number's, WHICH class number is it? Everything
  above is cut by h+, and the incumbent's F4 -- the sign of the
  fundamental unit's norm grading L_1 at fixed WIDE h -- has a candidate
  explanation waiting in that gap: N(eps) = -1 gives h+ = h and
  N(eps) = +1 gives h+ = 2h, so at fixed h the N(eps) = +1 fields carry
  TWICE the narrow class number. If the deficit is a function of h+, F4
  is that doubling seen through a wide-h cut, and the genus-congruence
  explanation offered for it is not needed.

  P6. N(eps) ADDS NOTHING ONCE h+ IS FIXED. Cut the same ratio by h+ and
      by the sign of N(eps): the two columns agree at every h+ carrying
      both.

  K6 kills P6: the printed two-column table. A systematic gap between
     the columns at fixed h+ leaves N(eps) with its own grading and F4
     unexplained by this route. (The identity h+ = h or 2h is how the
     rig DERIVES h from h+ and the sign, so it is definitional here and
     is not evidence; what K6 tests is only whether the share, cut by
     h+, still sees the sign.)

RESOURCE. Pure integer arithmetic, no numpy, no arrays held beyond one
principal cycle per field and one accumulator per stratum. Estimated
under 512MB by a wide margin; wall-clock is the open quantity and is
printed. The follow-up re-reads the sweep already in memory and runs no
new arithmetic.

THE FINDINGS.

  F1. THE SHARE CLIMBS WITH p, AT EVERY CLASS NUMBER (pattern, 1216 real
      fields; P1 SURVIVES, K1 misses). The narrow share against its
      nominal 1/h+, over the frozen bins 1-1000, 1000-3000, 3000-10000:

          h+ = 2    0.938  0.978  0.990
          h+ = 4    0.815  0.927  0.982
          h+ = 6    0.764  0.935  0.961
          h+ = 8    0.662  0.855  0.964
          h+ = 12   0.644  0.835  0.917
          h+ = 16   0.716  0.629  0.843

      Every stratum is nearer 1 in the top bin than in the bottom one,
      which is K1's observable, and by the top bin the deficit is at
      most 5.4% at every h+ through 8 and at most 8.5% through 12. The climb is not monotone at the small
      strata -- h+ = 16 dips in the middle bin on 11 fields, h+ = 5 and
      10 on 8 and 9 -- and the field counts are printed beside every
      entry because that is what says which wiggles are readable. So the
      deficit is a BOTTOM-OF-RANGE effect and not a standing shortfall,
      and the equidistribution reading of it is the right one.

  F2. IT IS NOT THE GENUS CONGRUENCES (observation; P2 KILLED, and
      P3 KILLED). The exact decomposition splits the deficit in two, and
      neither factor owns it. At h+ = 8 the genus factor runs 0.720,
      0.874, 0.975 across the bins and the within-genus factor runs
      0.843, 0.961, 0.989 -- the same sign, the same shape, and
      comparable size, which is K2's kill. Which factor carries more is
      a function of the stratum and not of the mechanism: at h+ = 2 the
      within factor is exactly 1.000 in every bin, one class per genus
      leaving the genus factor the whole share; at h+ = 4 the genus
      factor is 0.821 against a within factor of 0.967.

      P3 is where it is decided rather than merely weakened. At t = 1 --
      D itself a prime discriminant, ONE genus, the genus factor
      identically 1 by derivation (3) -- the narrow share is still
      0.885, 0.843 and 0.716 of nominal at h+ = 3, 5 and 7 in the bottom
      bin -- on 20, 8 and 4 fields, so the h+ = 3 row is the one carrying
      the refutation -- which is as short as the all-t table is at
      comparable h+
      (0.662 at h+ = 8). A deficit of full size sits at exactly the
      fields where the named mechanism can produce none. So the
      congruence explanation offered for it is not underdetermined by
      the data, it is refuted by it, and what remains is the plain
      statement: the class group's own equidistribution over primes has
      not arrived at the bottom of the range, and the genus quotient is
      one visible part of that rather than its cause.

  F3. BOTH SIGNS OF D AGREE ONCE THE FLOOR IS OUT (pattern, 1217
      imaginary fields; P4 SURVIVES). Imaginary against real at equal
      narrow class number, bins 1000-3000 and 3000-10000:

          h = 2   0.974 1.001   vs   0.978 0.990
          h = 4   0.928 0.981   vs   0.927 0.982
          h = 6   0.945 0.954   vs   0.935 0.961
          h = 8   0.895 0.955   vs   0.855 0.964

      The imaginary side reaches h = 60 in this population where the
      real side stops at 16, and the same climb continues there
      (h = 40: 0.290 then 0.796). So the effect is the class group's and
      not the signature's -- which is worth saying precisely because the
      FLOOR was the opposite, a phenomenon of the signature alone.

  F4. THE GRADING IS THE CLASS NUMBER'S AND NOT THE DISCRIMINANT'S
      (observation; P5 KILLED). The confound is real and it is
      answered. Cut both ways at once on the real side, at p <= 1000:
      down a column at fixed h+ = 8 the ratio reads 0.662, 0.628, 0.661,
      0.687 across the |D| bands to 1000, 2000, 3000, 4000 -- flat, with
      no direction; across the row at fixed |D| in 3000-4000 it reads
      1.000, 0.947, 0.884, 0.805, 0.797, 0.687 at h+ = 1, 2, 3, 4, 6, 8.
      The imaginary side agrees in the bin clear of the floor
      (3000-10000): h+ = 16 gives 0.883, 0.907, 0.872, 0.971 across the
      |D| bands and h+ = 32 gives 0.657, 0.897, 0.961, both flat or
      rising, while down the h column at fixed |D| in 2000-3000 the
      ratio falls 0.923 to 0.603 between h = 6 and h = 44.

      THE ONE PLACE THE ANSWER LOOKS DIFFERENT, AND WHY IT IS NOT. The
      imaginary cut at 1000 < p <= 3000 DOES fall with |D| at fixed h
      (h = 20: 0.934, 0.761, 0.690, 0.554). That bin is not clear of the
      floor: the floor sits at |D|/4, which reaches 1000 at the top of
      this population, so the large-|D| end of that row is reading
      primes on the floor's own tail. The bin above starts at three
      times the highest floor in the sweep and is the clean read, which
      is why both are printed rather than the favourable one.

  F5. AND THE UNIT'S NORM ADDS NOTHING ONCE THE NARROW CLASS NUMBER IS
      FIXED (observation; P6 SURVIVES). Split by the sign of N(eps) at
      fixed h+, the share ratio reads 0.922/0.942 at h+ = 2, 0.831/0.813
      at 4, 0.773/0.761 at 6 and 0.663/0.661 at 8 -- differences of at
      most 0.02 with no consistent direction. That resolves the
      incumbent's F4, which read the same grading at fixed WIDE h and
      had no mechanism for it but a genus one: N(eps) = -1 gives
      h+ = h and N(eps) = +1 gives h+ = 2h, so a wide-h stratum mixes
      two narrow class numbers a factor of two apart, and the deficit is
      a function of the narrow one. The sign of the unit's norm grades
      L_1 because it doubles h+, and for no other reason measured here.

  F6. THE POOLED SHARE UNDERSTATED THE EFFECT BY ABOUT A FACTOR OF TWO,
      AND AT THE SCALE L_1 IS READ IT IS THE SAME ORDER AS THE WHOLE
      UNDERSHOOT (observation, POST-HOC REFINEMENT -- the bottom edge at
      100 was added after the first prints and the frozen tables above
      keep their own edges). L_1 has a mean in the tens, so the bin it
      actually lives in is 1-100, and the pooled 1-1000 reading averages
      that against a decade where the deficit is already half gone:

          h+          1-100   100-1000   1-1000 (pooled)
           2          0.868      0.949      0.938
           4          0.630      0.844      0.815
           6          0.414      0.823      0.764
           8          0.332      0.714      0.662
          12          0.403      0.688      0.644
          16          0.501      0.743      0.716

      A share of 0.332 lengthens a first hit by about 3.0x, and 0.403 by
      about 2.5x, against the incumbent's measured undershoots of 2.27x
      at wide h = 4 and 3.23x at wide h = 6 -- whose fields carry
      h+ = 8 and 12 respectively wherever N(eps) = +1, which is about
      two thirds of them: 81 of the 117 fields at wide h = 4 carry
      h+ = 8, and 17 of the 27 at wide h = 6 carry h+ = 12. So the effect at the right scale is
      the same ORDER as the thing it was supposed to explain, where the
      pooled reading bought only 1.33x of 3.23x. THIS IS NOT A DIVISION
      AND IS NOT PRINTED AS ONE: the rig prints the share, and pairing
      each field's own local share against its own L_1 is a first-hit
      model this rig does not build. What the numbers license is the
      order and the direction, which is enough to retire the claim that
      a SECOND mechanism graded by the class number is doing most of the
      work -- the grading is one mechanism read at the wrong scale.

      The imaginary column shows the contrast the floor makes and is why
      it is printed beside: at p <= 100 the share rounds to 0.000 at
      every h from 9 up but one, and across that whole population --
      869 fields -- exactly ONE carries a principal split prime below
      100 (|D| = 296, h = 10, which is the 0.016 the h = 10 row prints).
      The floor is most of that and not all of it: 26 of those fields
      have |D| <= 400 and so a floor inside the bin, and at h >= 9 a
      nominal 1/h over the dozen split primes there leaves about one
      expected hit anyway. Either way nothing about equidistribution is
      READABLE in that column, which is precisely the confusion the
      real side was needed to break.

RUN RECORD: wall 4.9 s, 1216 real and 1217 imaginary fundamental
discriminants, odd primes to 10000, pure integer arithmetic. All five
controls green and read first -- C5 was added by the audit that followed
and is counted among them, on the hole it names: C1 found every one of
976 h+ = 1
field-bins carrying a share of exactly 1 at both signs; C2 reproduced
the incumbent's wide share at h = 1..8 with no stratum off by more than
5e-5; C3 found no narrow-principal place outside the principal genus and
exact agreement at all 4224 one-class-per-genus field-bins; C4 agreed
with the incumbent's u^2 + |D|y^2 loop at 14941 of 14941 pairs, which is
what licenses the definite-form test past that loop's practical range;
and C5 found 2^(t-1) dividing h+ at all 2433 fields of both signs.
Three measurements here are POST-HOC and say so where they are printed:
K5 and K6 were frozen after the first four kills and before their own
engine, and K7's finer bottom bin was added last -- the frozen tables
group their bins back together so that P1 through P4 are read on exactly
the edges they were written against.
"""

import sys
import time
from math import isqrt


# ---------------------------------------------------------------- primes

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    return [i for i in range(n + 1) if sieve[i]]


def kronecker(D, p):
    """chi_D(p) for p an ODD prime. +1 split, -1 inert, 0 ramified."""
    if D % p == 0:
        return 0
    return 1 if pow(D % p, (p - 1) // 2, p) == 1 else -1


def sqrt_mod_p(a, p):
    """Tonelli-Shanks. Assumes a is a QR mod p, p an odd prime."""
    a %= p
    if a == 0:
        return 0
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


# ------------------------------------------------- fundamental discriminants

def squarefree(n):
    for d in range(2, isqrt(n) + 1):
        if n % (d * d) == 0:
            return False
    return True


def fundamental_discriminants(lo, hi, sign):
    """Fundamental discriminants D with lo < sign*D <= hi."""
    out = []
    for a in range(lo + 1, hi + 1):
        D = a if sign > 0 else -a
        if D % 4 == 1 and squarefree(abs(D)):
            out.append(D)
        elif D % 4 == 0:
            m = D // 4
            if m % 4 in (2, 3) and squarefree(abs(m)):
                out.append(D)
    return out


def prime_discriminants(D):
    """The prime discriminant factors of a fundamental discriminant.

    Every fundamental discriminant is a product of prime discriminants
    -- p* = (-1)^((p-1)/2) p at odd p, and one of -4, 8, -8 at 2 -- and
    the factorization is unique. The 2-part is not searched for: it is
    whatever is left after the odd ones are divided out, and the assert
    is what checks that the identity held rather than a comment claiming
    it did."""
    out, prod = [], 1
    n = abs(D)
    while n % 2 == 0:
        n //= 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            out.append(q if q % 4 == 1 else -q)
            prod *= out[-1]
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        out.append(n if n % 4 == 1 else -n)
        prod *= out[-1]
    rest = D // prod
    assert D == prod * rest and rest in (1, -4, 8, -8), (D, prod, rest)
    if rest != 1:
        out.append(rest)
    return out


def in_principal_genus(chars, p):
    """chi_{D_i}(p) = +1 at every prime discriminant factor. p odd, p not | D."""
    for d in chars:
        if pow(d % p, (p - 1) // 2, p) != 1:
            return False
    return True


# -------------------------------------------------- indefinite form machinery

def _normalize_b(a, b, D, rt):
    m = 2 * abs(a)
    hi = abs(a) if abs(a) > rt else rt
    return b + ((hi - b) // m) * m


def rho(f, D, rt):
    a, b, c = f
    b2 = _normalize_b(c, -b, D, rt)
    return (c, b2, (b2 * b2 - D) // (4 * c))


def is_reduced(f, D, rt):
    """|sqrt(D) - 2|a|| < b < sqrt(D), decided in integers -- rt is a floor,
    so comparing against it directly admits forms that are not reduced."""
    a, b, c = f
    if b <= 0 or b * b >= D:
        return False
    t = 2 * abs(a)
    lo_ok = (t - b < 0) or (D > (t - b) * (t - b))
    return lo_ok and (t + b) * (t + b) > D


def reduce_form(f, D, rt):
    for _ in range(4 * rt + 64):
        if is_reduced(f, D, rt):
            return f
        f = rho(f, D, rt)
    raise RuntimeError("reduction did not terminate")


def cycle_of(f, D, rt):
    out, g = [f], rho(f, D, rt)
    while g != f:
        out.append(g)
        g = rho(g, D, rt)
        if len(out) > 200000:
            raise RuntimeError("cycle did not close")
    return out


def principal_cycle(D, rt):
    b0 = D % 2
    f = reduce_form((1, b0, (b0 * b0 - D) // 4), D, rt)
    return cycle_of(f, D, rt)


def divisors_signed(n):
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
    return ds + [-d for d in ds]


def all_reduced_forms(D, rt):
    out = []
    for b in range(1, rt + 1):
        if (b - D) % 2:
            continue
        n = (b * b - D) // 4
        for a in divisors_signed(-n):
            if n % a:
                continue
            c = n // a
            if is_reduced((a, b, c), D, rt):
                out.append((a, b, c))
    return out


def class_data_real(D, rt):
    """(wide h, narrow h+, sign of N(eps)) from the cycles.

    N(eps) = -1 exactly when the principal form's OPPOSITE is
    narrow-equivalent to it. Cycle LENGTH parity decides nothing:
    D = 8 (N = -1) and D = 12 (N = +1) both have principal cycle
    length 2 (explore_real_principal.py)."""
    forms = set(all_reduced_forms(D, rt))
    hplus, seen, prin_cycle = 0, set(), None
    b0 = D % 2
    c0 = (b0 * b0 - D) // 4
    prin = reduce_form((1, b0, c0), D, rt)
    for f in forms:
        if f in seen:
            continue
        cyc = cycle_of(f, D, rt)
        seen.update(cyc)
        hplus += 1
        if prin in cyc:
            prin_cycle = set(cyc)
    opp = reduce_form((-1, b0, -c0), D, rt)
    neps = -1 if opp in prin_cycle else +1
    h = hplus if neps == -1 else hplus // 2
    return h, hplus, neps


# ---------------------------------------------------- definite form machinery

def reduce_definite(f, D):
    """The unique reduced representative of a positive definite class."""
    a, b, c = f
    while True:
        if c < a or (c == a and b < 0):
            a, b, c = c, -b, a
            continue
        if b > a or b <= -a:
            m = (a - b) // (2 * a)
            b = b + 2 * a * m
            c = (b * b - D) // (4 * a)
            continue
        return (a, b, c)


def class_number_imag(D):
    """Count reduced positive definite forms: -a < b <= a <= c, and b >= 0
    where a = c. a is bounded by 3a^2 <= |D|."""
    n, absD, a = 0, -D, 1
    while 3 * a * a <= absD:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (a == c and b < 0):
                continue
            n += 1
        a += 1
    return n


# ------------------------------------------------------- principality tests

def form_at(D, p):
    """(p, b, (b^2-D)/(4p)) of discriminant D, representing p. p odd split."""
    x = sqrt_mod_p(D, p)
    b = x if (x - D) % 2 == 0 else x + p
    assert (b * b - D) % (4 * p) == 0
    return b


def principal_real(D, p, b, prin_set, rt):
    """(narrow, wide) principality of a degree-1 place above p, D > 0."""
    num = b * b - D
    if reduce_form((p, b, num // (4 * p)), D, rt) in prin_set:
        return True, True          # narrow principal implies wide principal
    wide = reduce_form((-p, b, num // (-4 * p)), D, rt) in prin_set
    return False, wide


def principal_imag(D, p, b, prin_form):
    return reduce_definite((p, b, (b * b - D) // (4 * p)), D) == prin_form


def principal_imag_loop(D, p):
    """The incumbent's test: 4p = u^2 + |D|y^2 (explore_real_principal.py)."""
    b0 = D % 2
    absD = -D
    y = 1
    while absD * y * y <= 4 * p:
        rem = 4 * p - absD * y * y
        u = isqrt(rem)
        if u * u == rem and (u - b0 * y) % 2 == 0:
            return True
        y += 1
    return False


# ------------------------------------------------------------------- driver

DMAX = 4000                       # the population K5 was read on
BIN_EDGES = [100, 1000, 3000, 10000]
# The incumbent's whole range is bins 0 AND 1 together; bin 0 alone is the
# scale L_1 itself lives at, which is why the edge is there.
INCUMBENT = [0, 1]
MIN_SPLIT = 20                    # the incumbent's per-field filter
# Only about 12 of the odd primes below 100 split at a typical field, so the
# incumbent's filter would empty bin 0 rather than clean it. The per-field
# share there is correspondingly noisy and the table's own field counts are
# what says how far the mean over fields carries it.
MINS = [8, 20, 20, 20]
# The bins the original predictions were written against.
FROZEN = [[0, 1], [2], [3]]
MIN_FIELDS = 4                    # the incumbent's per-stratum filter


def bin_of(p):
    for i, e in enumerate(BIN_EDGES):
        if p <= e:
            return i
    return None


def bin_label(g):
    """The range a GROUP of adjacent bins covers. Groups exist because the
    edge at 100 was added AFTER the first prints: the earlier tables keep
    the edges their own predictions were written against by grouping bins
    0 and 1 back together, and the refinement is reported on its own."""
    lo = 1 if g[0] == 0 else BIN_EDGES[g[0] - 1]
    return "%d-%d" % (lo, BIN_EDGES[g[-1]])


NB = len(BIN_EDGES)


def sweep_real(plist):
    """Per-field counts by bin: split, narrow, wide, genus, narrow&genus."""
    out = []
    for D in fundamental_discriminants(0, DMAX, +1):
        rt = isqrt(D)
        if rt * rt == D:
            continue
        h, hplus, neps = class_data_real(D, rt)
        pc = set(principal_cycle(D, rt))
        chars = prime_discriminants(D)
        c = [[0] * 5 for _ in range(NB)]
        for p in plist:
            if kronecker(D, p) != 1:
                continue
            i = bin_of(p)
            b = form_at(D, p)
            nar, wid = principal_real(D, p, b, pc, rt)
            gen = in_principal_genus(chars, p)
            row = c[i]
            row[0] += 1
            row[1] += nar
            row[2] += wid
            row[3] += gen
            row[4] += nar and gen
        out.append((D, h, hplus, neps, len(chars), c))
    return out


def sweep_imag(plist):
    out = []
    for D in fundamental_discriminants(0, DMAX, -1):
        h = class_number_imag(D)
        b0 = D % 2
        prin = reduce_definite((1, b0, (b0 * b0 - D) // 4), D)
        chars = prime_discriminants(D)
        c = [[0] * 5 for _ in range(NB)]
        for p in plist:
            if kronecker(D, p) != 1:
                continue
            i = bin_of(p)
            b = form_at(D, p)
            nar = principal_imag(D, p, b, prin)
            gen = in_principal_genus(chars, p)
            row = c[i]
            row[0] += 1
            row[1] += nar
            row[2] += nar          # narrow = wide at D < 0
            row[3] += gen
            row[4] += nar and gen
        out.append((D, h, h, +1, len(chars), c))
    return out


def share_table(rows, title, col, nominal, groups, tsel=None):
    """Mean over FIELDS of a per-field share, by class number and bin.

    col indexes the count row; nominal(h, hplus, t) returns what the share
    is measured against. The mean is over fields and not pooled over
    pairs, which is the statistic the incumbent's K5 printed."""
    print("\n%s" % title)
    acc = {}
    for D, h, hplus, neps, t, c in rows:
        if tsel is not None and t != tsel:
            continue
        for gi, g in enumerate(groups):
            r = agg(c, g)
            if r[0] < max(MINS[i] for i in g):
                continue
            nom = nominal(h, hplus, t)
            if nom is None or nom <= 0:
                continue
            acc.setdefault(hplus, {}).setdefault(gi, []).append(
                (r[col] / r[0]) / nom)
    hdr = "     %-5s" % "h+"
    for g in groups:
        hdr += " %15s" % bin_label(g)
    print(hdr + "        (share / nominal; 1.00 = no deficit)")
    for hp in sorted(acc):
        if len(acc[hp].get(0, [])) < MIN_FIELDS:
            continue
        line = "     %-5d" % hp
        for gi in range(len(groups)):
            v = acc[hp].get(gi, [])
            line += " %8.3f(%4d)" % (sum(v) / len(v), len(v)) if len(v) >= MIN_FIELDS \
                else " %15s" % "-"
        print(line)


DBANDS = [1000, 2000, 3000, 4000]


def agg(c, idxs):
    """The five counts summed over a group of bins."""
    return [sum(c[i][j] for i in idxs) for j in range(5)]


def two_way(rows, title, bs):
    """The share ratio in ONE prime bin, cut by class number AND |D| band.

    h grows with |D|, so a one-way cut by h cannot say which of the two
    grades the deficit. This cuts both at once: down a column is |D|
    rising at fixed h, across a row is h rising at fixed |D|."""
    print("\n%s" % title)
    acc = {}
    for D, h, hplus, neps, t, c in rows:
        r = agg(c, bs)
        if r[0] < MIN_SPLIT:
            continue
        for j, e in enumerate(DBANDS):
            if abs(D) <= e:
                break
        acc.setdefault(hplus, {}).setdefault(j, []).append(
            (r[1] / r[0]) * hplus)
    hdr = "     %-5s" % "h+"
    lo = 0
    for e in DBANDS:
        hdr += " %15s" % ("|D| %d-%d" % (lo, e))
        lo = e
    print(hdr)
    for hp in sorted(acc):
        if sum(len(v) for v in acc[hp].values()) < 2 * MIN_FIELDS:
            continue
        line = "     %-5d" % hp
        for j in range(len(DBANDS)):
            v = acc[hp].get(j, [])
            line += " %8.3f(%4d)" % (sum(v) / len(v), len(v)) \
                if len(v) >= MIN_FIELDS else " %15s" % "-"
        print(line)


def main():
    t0 = time.time()
    plist = [q for q in primes_upto(BIN_EDGES[-1]) if q != 2]
    print("ODD PRIMES to %d: %d   (p = 2 is the budget inequality's, and "
          "including it measures a different statistic)"
          % (BIN_EDGES[-1], len(plist)))
    print("population: fundamental discriminants |D| <= %d, both signs" % DMAX)

    print("\n=== SWEEP ===")
    real = sweep_real(plist)
    print("real fields:      %d   (%.1f s)" % (len(real), time.time() - t0))
    t1 = time.time()
    imag = sweep_imag(plist)
    print("imaginary fields: %d   (%.1f s)" % (len(imag), time.time() - t1))

    # ---- C1: the instrument pin -----------------------------------------
    print("\n=== C1  INSTRUMENT PIN AT h+ = 1 (control) ===")
    bad1 = tested1 = 0
    for name, rows in (("real", real), ("imag", imag)):
        for D, h, hplus, neps, t, c in rows:
            if hplus != 1:
                continue
            for i in range(NB):
                if c[i][0] == 0:
                    continue
                tested1 += 1
                if c[i][1] != c[i][0]:
                    bad1 += 1
                    print("  MISMATCH %s D=%d bin %s: %d/%d"
                          % (name, D, bin_label(i), c[i][1], c[i][0]))
    print("h+=1 field-bins tested: %d, non-unit shares: %d" % (tested1, bad1))

    # ---- C2: the incumbent regression -----------------------------------
    print("\n=== C2  INCUMBENT REGRESSION, wide share at p <= 1000 (control) ===")
    print("     (explore_real_principal.py K5: 1.0000 0.4573 0.2975 0.2033 "
          "0.1626 0.1252 0.1060 0.0841 at h = 1..8)")
    acc2 = {}
    for D, h, hplus, neps, t, c in real:
        r = agg(c, INCUMBENT)
        if r[0] < MIN_SPLIT:
            continue
        acc2.setdefault(h, []).append(r[2] / r[0])
    got = []
    for h in sorted(acc2):
        if len(acc2[h]) < MIN_FIELDS:
            continue
        v = acc2[h]
        got.append((h, len(v), sum(v) / len(v)))
    print("     " + "  ".join("h=%d:%.4f(%d)" % (h, m, n) for h, n, m in got[:8]))
    K5 = [1.0000, 0.4573, 0.2975, 0.2033, 0.1626, 0.1252, 0.1060, 0.0841]
    bad2 = sum(1 for (h, n, m), k in zip(got[:8], K5) if abs(m - k) > 5e-5)
    print("     strata disagreeing with the incumbent beyond 5e-5: %d" % bad2)

    # ---- C3: genus containment and exactness ----------------------------
    print("\n=== C3  GENUS CONTAINMENT (control) ===")
    bad3 = exact_tested = bad3b = 0
    for name, rows in (("real", real), ("imag", imag)):
        for D, h, hplus, neps, t, c in rows:
            for i in range(NB):
                if c[i][1] != c[i][4]:      # narrow & genus != narrow
                    bad3 += 1
                if 2 ** (t - 1) == hplus and c[i][0]:
                    exact_tested += 1
                    if c[i][1] != c[i][3]:
                        bad3b += 1
    print("narrow-principal outside the principal genus: %d field-bins" % bad3)
    print("one-class-per-genus field-bins: %d, share mismatches: %d"
          % (exact_tested, bad3b))

    # ---- C4: the form test against the incumbent loop -------------------
    print("\n=== C4  DEFINITE FORM TEST vs THE INCUMBENT LOOP (control) ===")
    pairs4 = agree4 = 0
    for D in fundamental_discriminants(0, 600, -1):
        rt = isqrt(-D)
        b0 = D % 2
        prin = reduce_definite((1, b0, (b0 * b0 - D) // 4), D)
        for p in plist:
            if p > 1000 or kronecker(D, p) != 1:
                continue
            pairs4 += 1
            b = form_at(D, p)
            if principal_imag(D, p, b, prin) == principal_imag_loop(D, p):
                agree4 += 1
    print("pairs compared: %d, agreements: %d" % (pairs4, agree4))

    print("\n=== C5  GENUS DIVISIBILITY 2^(t-1) | h+ (control) ===")
    bad5 = tested5 = 0
    for name, rows in (("real", real), ("imag", imag)):
        for D, h, hplus, neps, t, c in rows:
            tested5 += 1
            if hplus % 2 ** (t - 1):
                bad5 += 1
                print("  MISMATCH %s D=%d: h+=%d, 2^(t-1)=%d"
                      % (name, D, hplus, 2 ** (t - 1)))
    print("fields tested: %d, divisibility failures: %d" % (tested5, bad5))

    if bad1 or bad2 or bad3 or bad3b or bad5 or pairs4 != agree4:
        print("\nCONTROLS FAILED -- results not read.")
        return 1

    # ---- K1: the share as a function of p -------------------------------
    share_table(real, "[K1] REAL: narrow principal share / (1/h+), by bin",
                1, lambda h, hp, t: 1.0 / hp, FROZEN)

    # ---- K2: the decomposition ------------------------------------------
    share_table(real, "[K2a] REAL: principal-genus share / (1/2^(t-1)), by bin",
                3, lambda h, hp, t: 1.0 / 2 ** (t - 1), FROZEN)
    print("\n[K2b] REAL: within-genus share / (2^(t-1)/h+), by bin")
    accw = {}
    for D, h, hplus, neps, t, c in real:
        for gi, g in enumerate(FROZEN):
            r = agg(c, g)
            if r[3] < max(MINS[i] for i in g):
                continue
            nom = 2 ** (t - 1) / hplus
            accw.setdefault(hplus, {}).setdefault(gi, []).append(
                (r[4] / r[3]) / nom)
    hdr = "     %-5s" % "h+"
    for g in FROZEN:
        hdr += " %15s" % bin_label(g)
    print(hdr)
    for hp in sorted(accw):
        if len(accw[hp].get(0, [])) < MIN_FIELDS:
            continue
        line = "     %-5d" % hp
        for gi in range(len(FROZEN)):
            v = accw[hp].get(gi, [])
            line += " %8.3f(%4d)" % (sum(v) / len(v), len(v)) if len(v) >= MIN_FIELDS \
                else " %15s" % "-"
        print(line)

    # ---- K3: the population where the genus factor is identically 1 -----
    share_table(real, "[K3] REAL, t = 1 ONLY (one genus): narrow share / (1/h+)",
                1, lambda h, hp, t: 1.0 / hp, FROZEN, tsel=1)

    # ---- K4: the imaginary side, floor-free bins only --------------------
    share_table(imag, "[K4] IMAGINARY: narrow share / (1/h), bins above the "
                "floor (|D|/4 <= %d at every field here)" % (DMAX // 4),
                1, lambda h, hp, t: 1.0 / hp, [[2], [3]])
    share_table(imag, "[K4-lo] IMAGINARY, the bins below 1000 -- NOT "
                "comparable, the floor lives here",
                1, lambda h, hp, t: 1.0 / hp, [INCUMBENT])

    # ---- K5: is the grading the class number's or the discriminant's? ---
    two_way(real, "[K5] REAL: share ratio at p <= 1000, by class number "
            "AND |D| band", INCUMBENT)
    two_way(imag, "[K5] IMAGINARY: the same at 1000 < p <= 3000 -- the wider "
            "h range at equal |D|, and above the floor", [2])
    # The floor sits at |D|/4, which is 1000 at the top of this population,
    # so the bin above reads primes sitting ON the floor's tail at the large
    # |D| end and its |D| direction is confounded by construction. The bin
    # below starts at three times the highest floor in the sweep and is the
    # clean read of the same cut.
    two_way(imag, "[K5] IMAGINARY: the same again at 3000 < p <= 10000 -- "
            "clear of the floor's tail at every |D| in the population", [3])

    # ---- K6: does the unit's norm survive fixing the NARROW class number?
    print("\n[K6] REAL: share ratio at p <= 1000 by h+ and the sign of "
          "N(eps) -- F4's grading was read at fixed WIDE h")
    acc6 = {}
    for D, h, hplus, neps, t, c in real:
        r = agg(c, INCUMBENT)
        if r[0] < MIN_SPLIT:
            continue
        acc6.setdefault(hplus, {}).setdefault(neps, []).append(
            (r[1] / r[0]) * hplus)
    print("     %-5s %15s %15s" % ("h+", "N(eps) = -1", "N(eps) = +1"))
    for hp in sorted(acc6):
        line = "     %-5d" % hp
        shown = 0
        for s in (-1, +1):
            v = acc6[hp].get(s, [])
            if len(v) >= MIN_FIELDS:
                line += " %8.3f(%4d)" % (sum(v) / len(v), len(v))
                shown += 1
            else:
                line += " %15s" % "-"
        if shown == 2:
            print(line)

    # ---- K7: the refinement, and the only bin L_1 itself lives in -------
    share_table(real, "[K7] REAL, POST-HOC REFINEMENT: the same narrow share "
                "with the bottom decade split off -- L_1 has a mean in the "
                "tens, so 1-100 is the scale the first hit is read at",
                1, lambda h, hp, t: 1.0 / hp, [[0], [1], [2], [3]])
    share_table(imag, "[K7] IMAGINARY: the same -- and here the floor OWNS "
                "the bottom decade, which is what the contrast shows",
                1, lambda h, hp, t: 1.0 / hp, [[0], [1], [2], [3]])

    print("\nwall: %.1f s" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
