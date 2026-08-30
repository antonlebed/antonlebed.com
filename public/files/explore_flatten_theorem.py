"""explore_flatten_theorem.py -- THE RANK-2 CLOSED FORM AS A THEOREM,
AND WHAT SETS THE LOW-RANK THRESHOLD.

explore_flatten_select.py closed 695 cells of h(M, J) -- the least
HEIGHT of a nonzero M-atom vector whose first J moments vanish -- and
explore_flatten_band.py took single rank columns far past that chart.
Between them they left one law measured and unproved: at lattice rank
r = M - J equal to 2 the minimum has a CLOSED FORM,

    h(J + 2, J) = height((1 + x)(x - 1)^J),

checked at every depth J = 2..140 and failing at none. Everything this
thread holds is of that shape -- a census, or a law measured in a
range. This rig is not a fifth census. It asks whether the rank-2 law
is a THEOREM, in the charter's sense of the word: a complete proof for
all J that does not rest on computation at specific values.

(FLATTENING, HEIGHT, PURE PRODUCT, RANK and the CHAMPION keep their
earlier senses, restated because this file is read alone. A vector c on
M atoms is the polynomial P(x) = sum_r c_r x^r; its moments m_j =
sum_r C(r, j) c_r are its coefficients in the (x - 1) basis, so the
FLATTENING -- the least j with m_j nonzero -- IS the multiplicity of
the root 1. HEIGHT is the sup norm max_r |c_r|. The vectors of width M
flattened to depth J are exactly (x - 1)^J Z[x] cut at degree < M, a
LATTICE of rank r = M - J, and h is its shortest vector in the sup
norm. A PURE PRODUCT is prod_i (x^{d_i} - 1) over a multiset of
positive parts; ph is the least height of one that fits the cell, and a
cell FAILS when h < ph. Writing [d]_x = 1 + x + ... + x^{d-1}, a pure
product with c >= J parts and degree sum <= M - 1 is (x - 1)^c times a
product of [d]_x, so its COFACTOR after dividing out (x - 1)^J is
q = (x - 1)^t prod_{d in E} [d]_x with t + sum_{d in E} (d - 1) <=
r - 1. The CHAMPION is the cofactor (1 + x)^{r-1}, the unique cofactor
of maximal vanishing order at -1, whose height explore_flatten_band.py
found to be the closed form past each low rank's own threshold.)

THE QUESTION, in three parts.

  (a) IS IT A THEOREM AT RANK 2? The lattice at rank 2 is
      {q(x)(x - 1)^J : deg q <= 1}, so the claim is a statement about
      binomial coefficients and nothing else. Writing c_k = C(J, k),
      zero outside 0 <= k <= J, the coefficient of x^k in
      (a + bx)(x - 1)^J is (-1)^{J-k}(a c_k - b c_{k-1}), so the claim
      is: for every J >= 2 and every integer pair (a, b) other than
      (0, 0),

          max_k |a c_k - b c_{k-1}| >= max_k |c_k - c_{k-1}|,

      with equality only at (a, b) = +-(1, 1).
  (b) WHAT IS THE SECOND MINIMUM? Every rig in this thread runs a full
      basis reduction, and the profile is not thrown away -- lll_incr
      RETURNS mu and the squared Gram-Schmidt norms, and the callers
      hand them straight to the ball enumeration, which prunes with
      them. What has never happened is anyone READING them as a
      successive-minima statistic: lambda_2 and the lambda_2/lambda_1
      ratio appear nowhere in this corner. At rank 2 the same argument that
      settles (a) settles them exactly and for free, with no reduction
      and no enumeration.
  (c) WHY DOES A LOW RANK HAVE A THRESHOLD AT ALL? The champion
      attains h from J = 2, 7 and 13 at ranks 2, 3 and 4
      (explore_flatten_band.py). Below its own threshold a rank is
      clean -- h = ph -- and yet the champion is not the minimiser, so
      some OTHER member of the pure family is winning there. Which one
      is printed nowhere. This is the near end of the front the far
      end's asymptotic argument does not reach, and at low rank the
      whole pure family is a handful of polynomials, so the question is
      answerable exactly rather than measured.

THE HAND-DERIVATION (pre-engine, on paper). Parts (1)-(6) are the
proof of (a) and (b); part (7) fixes what (c) is held to before
any engine ran, and the paper does NOT settle it.

  (1) THE INDEX CONVENTION, re-derived from the engine's own
      construction rather than recalled. (x - 1)^J = sum_k
      (-1)^{J-k} C(J, k) x^k. Multiplying by a + bx, the coefficient of
      x^k is a(-1)^{J-k} C(J, k) + b(-1)^{J-k+1} C(J, k-1) =
      (-1)^{J-k} (a c_k - b c_{k-1}). The index k runs 0..J+1, since
      the product has degree J + 1 = M - 1. Write

          H(a, b) = max_{k in Z} |a c_k - b c_{k-1}|,
          D       = H(1, 1) = max_k |c_k - c_{k-1}|,
          N       = max_k c_k = C(J, floor(J/2)).

  (2) THE ENDPOINTS. k = 0 gives |a| and k = J + 1 gives |b|, so

          H(a, b) >= max(|a|, |b|)                              (L1)

      for every pair. This is what makes a finite search COMPLETE, AND
      ONLY UP TO ITS OWN BOUND: no pair with max(|a|, |b|) > c can have
      H <= c, so a search of the box |a|, |b| <= c settles every
      question whose answer is at most c, and NOTHING above it. The box
      cut at D therefore proves the MINIMUM and is blind to the second
      minimum, which is larger. For that, one more necessary condition
      is needed and (4) supplies it: H <= c also forces
      |a c_m - b c_{m-1}| <= c, which pins b to an interval about
      2c/c_{m-1} wide around a c_m / c_{m-1} -- about 2 wide when c is
      at most N. So every pair with H <= N lies in a STRIP of O(N)
      pairs rather than a box of O(N^2), and enumerating the strip is a
      proof over all of Z^2 at both bounds.

  (3) THE TWO SYMMETRIES. H(-a, -b) = H(a, b) is immediate. The second
      is the one the earlier route missed and it is the whole reason
      the proof is short. Since c_k = c_{J-k}, substituting k -> J+1-k
      -- a bijection of Z under which c_{J+1-k} = c_{k-1} and
      c_{J-k} = c_k, both sides vanishing together outside the row --
      gives a c_{J+1-k} - b c_{J-k} = -(b c_k - a c_{k-1}), hence

          H(a, b) = H(b, a).                                    (L2)

      The binomial row is a PALINDROME, so the lattice is invariant
      under reversal, and reversal swaps the two coefficients of the
      cofactor.

  (4) THE PEAK, AND THE INDEX MATTERS. Take m = floor(J/2), the FIRST
      index attaining the maximum, not the last. Since
      c_k / c_{k-1} = (J - k + 1)/k > 1 exactly when k < (J + 1)/2, and
      floor(J/2) < (J + 1)/2 at every J, the row is STRICTLY increasing
      on 0..m, so

          1 <= c_{m-1} < c_m = N     for every J >= 2.         (L3)

      Taking ceil(J/2) instead would give only c_{m-1} <= c_m, which is
      enough for the minimum and NOT enough for the second minimum's
      attaining set -- at odd J the two central entries are equal, and
      every pair (t+1, t) would then tie at N instead of beating it.
      One index apart is the difference between a value and a
      uniqueness.

  (5) THE TARGET IS BELOW THE PEAK, STRICTLY. For any k, if c_k and
      c_{k-1} are both nonzero they are positive integers, so
      |c_k - c_{k-1}| <= max(c_k, c_{k-1}) - 1 <= N - 1 when they
      differ and is 0 when they do not; and if one of them is zero
      then k is 0 or J + 1 and the value is 1. Since N >= 2 for
      J >= 2,

          D <= N - 1.                                          (L4)

      THIS IS WHERE J >= 2 ENTERS, and it is the only place. At J = 1
      the row is 1, 1: N = 1, D = 1, and the conclusion is false --
      (1, 0) attains the minimum too. The hypothesis is exactly the
      hypothesis the argument needs, which is the first thing to check
      about a short proof.

  (6) THE PROOF. Let (a, b) be a nonzero integer pair.
      - b = 0: H = |a| N >= N > D by (L4), with equality to N exactly
        at |a| = 1. Same for a = 0.
      - ab < 0: |a c_m - b c_{m-1}| = |a| c_m + |b| c_{m-1}
        >= N + 1 > N > D, since c_{m-1} >= 1 by (L3).
      - ab > 0: by (L2) and H(-a, -b) = H(a, b) assume a >= b >= 1.
        If a > b then a c_m - b c_{m-1} > a c_m - b c_m = (a - b) N
        >= N > D -- STRICTLY, because c_{m-1} < c_m by (L3) and
        b >= 1. If a = b then H = a D, which is D at a = 1 and at
        least 2D otherwise.
      So the minimum is D and its minimiser set is exactly +-(1, 1).
      THE SAME CASE LIST GIVES THE SECOND MINIMUM AND ITS ATTAINING SET
      with nothing added, and this is where the strictness earns its
      keep: every pair NOT parallel to (1, 1) falls in one of the first
      three cases, each bounding H by at least N, and the bound is an
      EQUALITY only in the first case at |a| = 1 or |b| = 1. So in the
      sup norm

          lambda_1 = D,   lambda_2 = N = C(J, floor(J/2)),      (L5)

      with lambda_2 attained at +-(1, 0) and +-(0, 1) and nowhere else.
      A rank-2 flattening lattice has NO second short vector: its two
      successive minima are separated by the whole of the differencing
      gain.

  (7) THE THRESHOLD, WHICH THE PAPER DOES NOT SETTLE. At rank r the
      pure family's cofactors are the finitely many
      (x - 1)^t prod [d]_x with t + sum (d - 1) <= r - 1 -- three of
      them at r = 2 (1, x - 1 and 1 + x), and a handful at r = 3 and
      r = 4. At rank 2, (L4) says the champion 1 + x beats the cofactor
      1 at every J >= 2, and x - 1 is worse than 1 outright -- its
      product is (x - 1)^(J+1), of height C(J+1, floor((J+1)/2)), which
      Pascal's rule makes at least N and in fact strictly more -- so the
      champion IS the pure minimiser at every depth and the threshold
      is the smallest depth there is. At ranks 3 and 4 the comparison
      is between a champion of height about N/r and siblings whose
      heights are of the same order, and which wins at small J is not
      decided by the asymptotic argument that decides large J. The
      frozen suspicion is that the measured thresholds 7 and 13 are
      exactly the last depth at which some SIBLING of the champion --
      a cofactor with a lower vanishing order at -1, or an [d]_x with
      d > 2 -- has the smaller height, so that the near end of the
      band is set inside the pure family and needs no lattice argument
      at all.

THE PREDICTIONS, frozen before the engine ran.

  P1  Arm B's complete search returns min = D and minimiser set
      exactly +-(1, 1) at every J it reaches.
  P2  Every lemma L1-L5 holds at every J the lemma arm sweeps.
  P3  The second minimum is N exactly, attained at +-(1, 0) and
      +-(0, 1) and nowhere else, and the ratio N/D approaches
      (sqrt(e)/2) sqrt(J + 1) from the saddle-point estimate -- within
      2% by the deepest J the ratio arm reaches.
  P4  The rank-2 pure family has exactly three cofactors up to sign
      and ph = D, so h = ph at rank 2 for every J >= 2 is a theorem
      and not a range.
  P5  THE OPEN ONE. The champion fails to attain ph at ranks 3 and 4
      for J below the measured thresholds and at no J above them: the
      largest non-attaining depth is 6 at rank 3 and 12 at rank 4,
      against thresholds 7 and 13. Rank 3 I expect to hold -- the two
      heights are within one factor of each other and the crossing is
      where the paper puts it. RANK 4 I DO NOT KNOW: comparing only
      the powers (1 + x)^s makes rank 4 cross near J = 6, so if 12 is
      right the depths 6..12 must be carried by a cofactor with a part
      exceeding 2, and if 12 is wrong the near end is not a pure-family
      effect and the front stays open.

THE KILLS, as observables and not as inferences.

  K1  any of L1-L5 reported false at any swept J.
  K2  arm B's minimum differs from D, or its minimiser set differs
       from {+-(1, 1)}, at any J.
  K3  arm B's second minimum differs from N, or its attaining set
       differs from {+-(1, 0), +-(0, 1)}, at any J.
  K4  the controls do not fire: J = 1 not reported as breaking
       uniqueness, or a deliberately mutated target accepted.
  K5  the rank-2 cofactor set is not {1, x - 1, 1 + x} up to sign, or
       ph differs from D.
  K6  the largest non-attaining depths are not (none, 6, 12) at ranks
       2, 3 and 4.

THE DESIGN.

  ARM A -- THE LEMMAS. Sweep J = 2..200 and check L3 and L4 outright;
  check L1 and L2 on the full box |a|, |b| <= 6 plus a spread of larger
  pairs; check the peak step of (6) on every pair with 1 <= b < a <= 6.
  A lemma arm is worth having precisely because the proof is short: if
  the theorem is right for a reason other than the one written down,
  this is where it shows.

  ARM B -- THE COMPLETE MINIMISATION. For J = 2..14 enumerate the
  STRIP of (2) at bound N -- every integer pair with H <= N, complete
  over Z^2 -- and read both answers off it: the minimum and its full
  minimiser set from the sub-D part, the second minimum and its
  attaining set from the pairs not parallel to (1, 1). Each is a proof
  at that J by itself, independent of the paper argument, and the two
  must agree. Reading the second minimum off a box cut at D would NOT
  be one, which is the trap this arm is built around.

  ARM C -- THE CONTROLS, run before any verdict is read.
  C1 a POSITIVE CONTROL on the checker's teeth: run arm B's machinery
  at J = 1, where the theorem is FALSE, and require that it reports the
  uniqueness break. A checker that passes J = 1 is checking nothing.
  C2 two MUTATIONS at every J of arm B: the claims "min = D - 1" and
  "min = D + 1" must both be rejected. C3 a control on the STRIP
  itself, which replaced a brute force and so differs from it in
  exactly one variable, the pruning: at J = 2..9 the strip's pairs must
  equal a brute-force box of side 2N + 1 exactly. A dropped pair would
  surface as a missing low-height pair and nothing else here could see
  it.

  ARM D -- THE CLOSED FORM AND THE RATIO. Check the identity
  c_k - c_{k-1} = C(J+1, k) (J + 1 - 2k) / (J + 1) at J = 2..200, which
  turns D into a maximum over one explicit expression, and report the
  argmax's offset from the centre against the sqrt(J+1)/2 the
  saddle-point estimate predicts. Then report N/D against
  (sqrt(e)/2) sqrt(J + 1) at a ladder of depths to J = 2000.

  ARM E -- THE BRIDGE. Enumerate the rank-2 pure family from the
  cofactor condition and confirm the three cofactors and ph = D at
  J = 2..40. Arm B proves h = D; this arm is what makes it h = ph.

  ARM F -- THE THRESHOLD. For r = 2, 3, 4 enumerate the whole pure
  family at each J = 2..40, compute every cofactor's height against
  (x - 1)^J, and print for each J whether the champion attains the
  minimum and, where it does not, which cofactor beats it. The
  observable is the largest non-attaining J at each rank. It is a
  statement about the PURE family; it equals a statement about h only
  where h = ph is known, which arm B makes unconditional at rank 2 and
  which at ranks 3 and 4 rests on the BAND scan's range: the census's
  own rectangle stops at M <= 40, and it is explore_flatten_band.py
  that carries those ranks to depth 140.

  ARM G -- WHAT A RANK-3 ATTEMPT WOULD REST ON. The next rank's route
  has premises, and a premise carried in prose is a premise nothing
  prints. Three readings over J = 2..200: that the first-difference
  row is antisymmetric and that the REVERSAL symmetry -- the whole
  engine of the rank-2 proof -- survives that sign change; the depths
  where the transplanted (L4) fails, i.e. where D2 > D1 - 1; and the
  depths where the evaluation bound at -1, height >= 2^J/(J+3),
  fails to clear D2.

RESOURCE. Exact integer arithmetic, no numpy, no BLAS. The heaviest
object is one binomial row at J = 2000. Seconds, far under the 512 MB
ceiling.

THE FINDINGS. Every kill missed; all six predictions hold, including
the one that was open.

  F1  THE RANK-2 CLOSED FORM IS A THEOREM. For every J >= 2 the least
      height of a nonzero vector of width J + 2 flattened to depth J is

          h(J + 2, J) = max_k |C(J, k) - C(J, k-1)|,

      and the minimising vectors are exactly +-(1 + x)(x - 1)^J. The
      proof is (1)-(6) above: it is four lines of case work over the
      sign and order of the cofactor's two coefficients, it uses no
      computation at any specific value, and its only hypothesis is
      J >= 2, entering at exactly one place. It is the first statement
      in this corner proved at the THEOREM tier, which this corpus
      reserves for a complete proof over all values that does not rest
      on computation -- but NOT the first thing here proved for all
      values, and the distinction is worth keeping: at rank 1 the
      lattice has a single generator and the two bounds coincide by
      construction, which is a PROPERTY and is proved for every width.
      What separates them is how much argument is needed, not whether
      a sweep is being leaned on. What the earlier route was
      missing was not a sharper estimate but the PALINDROME symmetry
      (L2): the binomial row reads the same backwards, so the lattice
      is reversal-invariant and reversal swaps a and b, which reduces
      the whole positive quadrant to a >= b and puts the peak
      comparison one line away. Bounding |a| and |b| through the
      endpoints and then fighting for the middle band is the route
      that has a gap; the symmetry removes the band.

  F2  AND IT IS CORROBORATED WITHOUT THE PROOF. Arm B enumerates every
      integer pair with H <= N -- complete over Z^2, not over a box --
      and there are strikingly few: SIX at J = 3, eight at nine of the
      depths and ten at the deepest three, the whole of Z^2 outside
      that handful sitting strictly above the second minimum. The
      count is 4 -- the two signs of (1,0) and (0,1) -- plus twice the
      number of multiples t(1,1) with tD <= N, so it reads the ratio
      N/D off directly, and J = 3 is short because 2D = 4 exceeds
      N = 3 there. At every J = 2..14 the
      minimum is D with minimiser set exactly {+-(1, 1)} -- 13 depths
      agreeing with the paper argument by a route that shares nothing
      with it.

  F3  THE SUCCESSIVE MINIMA ARE BOTH EXACT, AND THE SECOND ONE IS THE
      PEAK. The same case list gives lambda_2 = N = C(J, floor(J/2)),
      attained exactly at +-(1, 0) and +-(0, 1) -- confirmed at every
      depth of arm B, attaining set and all, and confirmed over Z^2
      rather than over a box: a search cut at the MINIMUM cannot
      certify the SECOND minimum, being blind to every pair whose
      coordinates fall between them, so this reading took the strip
      of (2). So a rank-2 flattening
      lattice has no second short vector at all: the two minima are
      separated by the entire differencing gain, and the ratio is

          lambda_2 / lambda_1 ~ (sqrt(e)/2) sqrt(J + 1),

      measured at 2.8000, 5.9009, 26.0948 and 36.8785 at J = 10, 50,
      1000 and 2000 against 2.7341, 5.8871, 26.0816 and 36.8757 --
      2.41% at the shallow end and 0.01% at J = 2000. The residual is
      NOT a decaying series: the argmax of the difference row is an
      integer while the saddle point is not, so the ladder's errors
      oscillate. This is the successive-minima reading no rig in this
      thread has taken, though every one of them already HOLDS the
      data: the reduction returns the Gram-Schmidt norms and the ball
      enumeration prunes with them, so the profile is in hand at every
      charted cell and has only ever been used as a search bound. At
      rank 2 it needed neither reduction nor enumeration -- only the
      proof already written.

  F4  THE BRIDGE, SO THE THEOREM IS ABOUT THE THREAD'S OWN QUANTITY.
      The rank-2 pure family offers exactly three cofactors up to
      sign -- 1, x - 1 and 1 + x -- and ph equals D at all 39 depths
      checked, as (L4) forces: 1 + x gives D <= N - 1 while 1 gives N
      and x - 1 gives more. So at rank 2 h = ph is a THEOREM and not a
      rule in range, and rank 2 leaves the census's failing set for a
      reason rather than for want of a counterexample.

  F5  THE CHAMPION'S THRESHOLD AT LOW RANK IS A PURE-FAMILY EFFECT,
      AND THE WINNER HAS A NAME. The open prediction P5 holds at both
      ranks. Two thresholds are easily read as one and are not: the
      first depth at which a rank FAILS, and the depth from which the
      champion is the minimiser. Ranks 3 and 4 have the second and
      not the first -- they fail at no depth swept -- so what follows
      is about the champion and says nothing about failing.
      The champion (1 + x)^(r-1) fails to attain ph at ranks 3 and 4
      exactly below the thresholds the lattice census measured: the
      largest non-attaining depth is 6 at rank 3 and 12 at rank 4,
      against measured thresholds of 7 and 13
      (explore_flatten_band.py). So the depth at which the closed form
      takes over at low rank is decided INSIDE a family of 7 and 14
      polynomials, by direct comparison, with no lattice argument
      anywhere -- the far end of the band is asymptotic and the near
      end, at these ranks, is arithmetic. WHO WINS INSTEAD IS THE
      CONTENT. At rank 3 it is 1 + x, the champion of the rank BELOW,
      at J = 2, 4 and 6 -- ALONE only at 6, tying with 1 + x + x^2 at
      the other two. At rank 4 it is (1 + x)(1 + x + x^2), alone, one
      cofactor for the whole run J = 3..12 -- which has vanishing
      order 1 at -1, not 3, so below the threshold the winner is a
      LOW-order cofactor and the asymptotic argument that says only
      the order matters is not merely imprecise there, it points the
      wrong way. AND THE NON-ATTAINING SET IS RAGGED, not an interval:
      it is {2, 4, 6} at rank 3, the odd depths between being exact
      TIES, and {3,...,10, 12} at rank 4, where the champion attains
      at J = 11 and loses again at 12. That is the same raggedness the
      census reports in the failing band's low edge, seen here in an
      object small enough to read off. RANK 4 STARTS AT 3 AND NOT AT 2
      because at J = 2 the champion is not in the family at all: a
      pure product needs u = J + t - |E| >= 0 parts equal to 1, so
      (1 + x)^3 needs J >= 3, and J = 2 is empty of it rather than
      non-attaining. The arm prints that separately and excludes it,
      which is the difference between a comparison lost and a
      comparison not available.

  F6  THE CONTROLS ALL BITE. At J = 1 the minimiser set is six pairs
      rather than two, so the uniqueness clause breaks exactly where
      the proof's use of N >= 2 says it must -- the checker is not
      passing everything. The two mutated targets D - 1 and D + 1 are
      rejected at all 13 depths, and the strip agrees with a
      brute-force box of side 2N + 1 at every depth J = 2..9, so the
      pruning that makes the second minimum provable drops nothing.

  F8  THE RANK-3 ROUTE HAS ONE PREMISE THAT SURVIVES AND TWO THAT
      START TOO LATE. If a rank-3 cofactor vanishes at -1 it is
      (1+x)q1, and the question becomes the rank-2 question over the
      FIRST-DIFFERENCE row d instead of the binomial row. That row is
      ANTISYMMETRIC, d_{J+1-k} = -d_k, at all 199 depths swept -- so
      it is not a palindrome and the proof's engine looks lost. It is
      not: the substitution k -> J+2-k sends a d_{J+2-k} - b d_{J+1-k}
      to -(a d_{k-1} - b d_k), so H_d(a, b) = H_d(b, a) survives the
      sign, with no violation over the same 199 depths at every
      coefficient pair to 4. WHAT DOES NOT SURVIVE IS THE HEIGHT
      COMPARISON. The transplanted (L4) asks D2 <= D1 - 1, which FAILS
      at every J from 2 to 8 and holds from 9 to 200 -- and rank 3's
      own threshold is 7, so the two depths where the champion first
      wins are exactly the two the transplanted argument cannot reach.
      The other opening is no better placed: |q(-1)| 2^J <= M * height
      gives height >= 2^J/(J+3) when q(-1) is nonzero, which clears D2
      from J = 11 to 200 but fails at J = 2..8 and again at 10. Both
      are measurements over a swept range and neither is a proof; what
      they say is that a rank-3 proof has a genuinely separate small-J
      argument to make, and that the reversal symmetry is the piece
      that carries over.

  F7  WHAT IS NOT SHOWN. The theorem is rank 2 and rank 2 only. F5's
      route does not generalise upward on its own: it compares a
      finite family and says nothing about the LATTICE minimum, so it
      reproduces the thresholds at ranks 3 and 4 only because h = ph
      was found there over a range -- 139 depths each at ranks 2, 3
      and 4 out to J = 140, which is explore_flatten_band.py's column
      scan and NOT the census, whose own rectangle stops at M <= 40.
      That is a rule in range and not a theorem. Nothing here touches
      the ranks 5..18 that fail, where h < ph is the whole point, nor
      the high wall.
      The proof's own bottleneck for rank 3 is visible: with a
      cofactor of degree 2 the peak comparison bounds the height by
      |q(-1)| N minus a correction that the middle coefficient can
      make arbitrarily large, so the peak alone no longer decides and
      the bulk window the earlier route described is genuinely needed.

RUN RECORD. Seven full runs. Three of the differences between them
were to how a print READS; two were real defects, one in what arm B
could PROVE and one in what the pure family CONTAINS.

Run 1 reported one member of arm D's argmax pair together with a
signed offset, which reads as a claim that the maximum sits on one
side of the centre -- but the difference row is antisymmetric about
(J+1)/2, so the argmax is always a MIRROR PAIR and only its distance
from the centre is a number; and it attributed the ratio ladder's
non-monotone error to the parity of J, which a denser sweep did not
support -- that sweep was a throwaway probe, shipped in no file, so no
figure of it is quoted anywhere here. The oscillation is the integrality of the
argmax, which the pair print now shows directly: 7.500 against the
saddle point's 7.089 at J = 200. Run 3 differs from run 2 only in the
kill LABELS, K-A..K-F renamed K1..K6, because a letter pair in the
kill dictionary collided with a tripwire this corpus runs over every
shipped script and the false positive costs nothing to avoid.

RUN 4 CARRIES THE ONE REAL FIX, and it is a defect in a COMPLETENESS
claim rather than in a number. Arm B searched the box |a|, |b| <= D
and read BOTH the minimum and the second minimum off it. The endpoint
bound certifies a box only up to that box's own side: every pair with
a coordinate above D has H > D, which settles the minimum and says
nothing about the second minimum at N > D, so every pair with a
coordinate strictly between D and N went unexamined and the second
minimum was a sample presented as a proof. The peak inequality
supplies the missing condition -- H <= N also forces
|a c_m - b c_{m-1}| <= N, which pins b to about two values per a --
so the arm now enumerates the STRIP of every pair with H <= N,
complete over Z^2. It found the same answers, and it is faster by an
order of magnitude, the strip holding 8 or 10 pairs where the box held
up to four million: wall fell from about 25 s to 1.9 s. Control C3 was
added with it, because the strip REPLACED a brute force and a pruning
that dropped a pair would be invisible to every other arm; it agrees
with a brute-force box of side 2N + 1 at J = 2..9.

RUN 5 CARRIES THE SECOND REAL FIX, and it is in the pure family's own
definition. The enumeration took every (t, E) inside the degree
budget, and one of them is not a product: a multiset with |E| parts
above 1 needs J + t - |E| parts equal to 1, and at r = 4, J = 2 the
triple (0, (2,2,2)) fails that -- so the CHAMPION (1+x)^3 was being
compared at a depth where no pure product has it. The constraint is
now in cofactor_multisets, which takes J, and arm F prints such depths
as EMPTY of the champion rather than as non-attaining. Only rank 4,
J = 2 moves: the non-attaining set there is {3..10, 12} and not
{2..10, 12}. Every threshold, every ph and every winner is unchanged,
and the tell was visible before the fix -- the winning cofactor was
already reported as running J = 3..12 beside a set said to start at 2.

RUN 6 adds arm G and changes nothing else; every earlier arm's output
is identical to run 5's.

RUN 7 MOVES THE PEAK INDEX from ceil(J/2) to floor(J/2), which is a
change to the PROOF and not to any number: every arm's output is
identical again. The old index gives c_{m-1} <= c_m, enough for the
minimum; the new one gives c_{m-1} < c_m strictly, which is what makes
the second minimum's ATTAINING SET follow from the case list rather
than only its value. At odd J the two central entries are equal, so
under the old index every pair (t+1, t) ties at N and uniqueness is
unproved -- a gap the doc had already asserted closed. Arm A's L3 and
L5 now test the strict forms, and pairs_upto keeps one fallback for
J <= 1, where m = 0 and there is no c_{m-1} to prune with; that is the
depth control C1 runs at, so the control now answers by brute force
the same question the strip answers everywhere else.

Wall 2.9 s; peak working set 12.5 MB under memwatch.py, far under the
512 MB ceiling. The controls run FIRST by construction, so no verdict
in this file was read before they fired.
"""

import time
from math import comb, sqrt, e as E_CONST


# ---------------------------------------------------------------- util

def binrow(J):
    """The row c_k = C(J, k), k = 0..J."""
    return [comb(J, k) for k in range(J + 1)]


def cof(row, k):
    """c_k with the zero convention outside the row."""
    return row[k] if 0 <= k < len(row) else 0


def pmul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return r


def ppow(p, n):
    r = [1]
    for _ in range(n):
        r = pmul(r, p)
    return r


def height(p):
    return max(abs(v) for v in p)


def H_pair(row, a, b):
    """max_k |a c_k - b c_{k-1}|, k over 0..J+1."""
    J = len(row) - 1
    return max(abs(a * cof(row, k) - b * cof(row, k - 1))
               for k in range(J + 2))


def D_of(row):
    return H_pair(row, 1, 1)


def N_of(row):
    return max(row)


# ------------------------------------------------- the pure family

def cofactor_multisets(r, J):
    """Every cofactor a pure product at rank r, depth J actually has.

    A pure product is prod_i (x^{d_i} - 1) over a multiset of c parts;
    parts equal to 1 contribute a bare (x - 1). Writing E for the parts
    exceeding 1 and u >= 0 for the number of 1-parts, c = |E| + u and
    the cofactor after dividing out (x - 1)^J is
    (x - 1)^t prod_{d in E} [d]_x with t = c - J. The degree budget is
    t + sum_{d in E} (d - 1) <= r - 1.

    THE SECOND CONSTRAINT IS EASY TO DROP AND IT BITES: u = J + t - |E|
    must be at least 0, or no product with that cofactor EXISTS. It can
    only bind when |E| exceeds J, which at these ranks happens at one
    place -- r = 4, J = 2, E = (2, 2, 2), t = 0, whose cofactor
    (1 + x)^3 is the CHAMPION. Without the constraint the champion is
    compared at a depth where it is not in the family at all.
    """
    budget = r - 1
    out = []

    def walk(minpart, spent, parts):
        for t in range(0, budget - spent + 1):
            if J + t - len(parts) >= 0:
                out.append((t, tuple(parts)))
        d = minpart
        while spent + (d - 1) <= budget:
            parts.append(d)
            walk(d, spent + (d - 1), parts)
            parts.pop()
            d += 1

    walk(2, 0, [])
    return out


def cofactor_poly(t, E):
    q = ppow([-1, 1], t)
    for d in E:
        q = pmul(q, [1] * d)
    return q


def canon(p):
    """A polynomial up to sign, for set comparison."""
    for v in p:
        if v:
            return tuple(p) if v > 0 else tuple(-x for x in p)
    return tuple(p)


# ------------------------------------------------------------ the arms

LEM_JMAX = 200
BOX_JMAX = 14
PURE_JMAX = 40
RATIO_LADDER = [10, 25, 50, 100, 250, 500, 1000, 2000]


def arm_A(fired):
    print("\nARM A -- THE LEMMAS, J = 2..%d" % LEM_JMAX)
    small = [(a, b) for a in range(-6, 7) for b in range(-6, 7)
             if (a, b) != (0, 0)]
    wide = [(37, 1), (1, 37), (-11, 5), (5, -11), (100, 99), (99, 100),
            (0, 23), (23, 0), (-7, -7)]
    bad = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}
    for J in range(2, LEM_JMAX + 1):
        row = binrow(J)
        N, D = N_of(row), D_of(row)
        m = J // 2
        if not (1 <= cof(row, m - 1) < cof(row, m) == N):
            bad["L3"] += 1
        if not D <= N - 1:
            bad["L4"] += 1
        for (a, b) in small + wide:
            h = H_pair(row, a, b)
            if h < max(abs(a), abs(b)):
                bad["L1"] += 1
            if h != H_pair(row, b, a) or h != H_pair(row, -a, -b):
                bad["L2"] += 1
        for a in range(2, 7):
            for b in range(1, a):
                if a * cof(row, m) - b * cof(row, m - 1) <= (a - b) * N:
                    bad["L5"] += 1
    for key in ("L1", "L2", "L3", "L4", "L5"):
        print("   %s violations: %d" % (key, bad[key]))
        if bad[key]:
            fired["K1"] += 1
    print("   (L1 endpoints, L2 the two symmetries, L3 the peak, "
          "L4 D <= N - 1, L5 the peak step of the proof)")
    if not any(bad.values()):
        print("   every lemma holds at every swept depth")


def pairs_upto(row, bound):
    """EVERY integer pair with H(a, b) <= bound. Complete over Z^2.

    A box capped at the MINIMUM is complete only for questions whose
    answer is at most that cap, so it cannot certify the SECOND
    minimum, which is larger. Three necessary conditions cut Z^2 to a
    strip instead. H <= bound forces |a| <= bound (the k = 0
    coefficient) and |b| <= bound (the k = J+1 one), and also
    |a c_m - b c_{m-1}| <= bound at the peak index -- and that last
    pins b to an interval of width 2*bound/c_{m-1} around
    a c_m / c_{m-1}, which is about 2 wide, since c_{m-1} is within a
    factor 1 + 2/J of c_m = N and bound is at most N here. So the
    enumeration is O(bound) pairs rather than O(bound^2) and stays a
    PROOF, not a sample.
    """
    J = len(row) - 1
    m = J // 2
    cm, cm1 = cof(row, m), cof(row, m - 1)
    out = []
    if cm1 < 1:
        # Only at J <= 1, where m = 0 and there is no c_{m-1} to prune
        # with -- and J = 1 is exactly where control C1 runs. Fall back
        # to the full box, which is trivial at that size, so the
        # control tests the SAME question the strip answers elsewhere.
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                if (a, b) != (0, 0) and H_pair(row, a, b) <= bound:
                    out.append((H_pair(row, a, b), a, b))
        return out
    for a in range(-bound, bound + 1):
        lo = -(-(a * cm - bound) // cm1)          # ceil division
        hi = (a * cm + bound) // cm1
        for b in range(max(lo, -bound), min(hi, bound) + 1):
            if a == 0 and b == 0:
                continue
            h = H_pair(row, a, b)
            if h <= bound:
                out.append((h, a, b))
    return out


def minimise(row, D, N):
    """The minimum and the second minimum, each proved COMPLETE.

    The minimum comes from every pair with H <= D; the second from
    every pair with H <= N, which is a strictly wider question and
    needs the wider scan. Returns (minimum, minimiser set, second
    minimum over pairs not parallel to (1,1), its attaining set,
    number of pairs the wider scan had to examine).
    """
    wide = pairs_upto(row, N)
    small = [t for t in wide if t[0] <= D]
    best = min(h for h, _, _ in small)
    bestset = sorted((a, b) for h, a, b in small if h == best)
    off = [(h, a, b) for h, a, b in wide if a != b]   # not parallel
    sec = min(h for h, _, _ in off)
    secset = sorted((a, b) for h, a, b in off if h == sec)
    return best, bestset, sec, secset, len(wide)


def arm_B(fired):
    print("\nARM B -- THE COMPLETE MINIMISATION, J = 2..%d" % BOX_JMAX)
    print("   both readings are searched to their OWN bound and each "
          "search is exhaustive over ALL of Z^2, not over a box")
    print("     J     D      N  pairs   min  minimiser set        "
          "lambda_2  attained at")
    for J in range(2, BOX_JMAX + 1):
        row = binrow(J)
        D, N = D_of(row), N_of(row)
        best, bestset, sec, secset, seen = minimise(row, D, N)
        ok1 = (best == D and bestset == [(-1, -1), (1, 1)])
        ok2 = (sec == N
               and secset == [(-1, 0), (0, -1), (0, 1), (1, 0)])
        print("   %4d %6d %6d %6d %6d  %-20s %8d  %s%s"
              % (J, D, N, seen, best, bestset, sec,
                 secset if len(secset) <= 4 else "(%d pairs)"
                 % len(secset),
                 "" if (ok1 and ok2) else "   <-- MISMATCH"))
        if not ok1:
            fired["K2"] += 1
        if not ok2:
            fired["K3"] += 1


def arm_C(fired):
    print("\nARM C -- THE CONTROLS")
    row1 = binrow(1)
    D1, N1 = D_of(row1), N_of(row1)
    best, bestset, _, _, _ = minimise(row1, D1, N1)
    broke = (best == D1 and bestset != [(-1, -1), (1, 1)])
    print("   C1 J = 1: D = %d, min = %d, minimiser set %s"
          % (D1, best, bestset))
    if broke:
        print("      the uniqueness clause BREAKS at J = 1, as the "
              "proof's use of N >= 2 requires -- the checker has teeth")
    else:
        print("      C1 DID NOT FIRE")
        fired["K4"] += 1
    mut = 0
    for J in range(2, BOX_JMAX + 1):
        row = binrow(J)
        D, N = D_of(row), N_of(row)
        best, _, _, _, _ = minimise(row, D, N)
        if best == D - 1 or best == D + 1:
            mut += 1
    print("   C2 mutated targets D - 1 and D + 1 accepted at %d of the "
          "%d depths" % (mut, BOX_JMAX - 1))
    if mut:
        fired["K4"] += 1
    # C3: the strip enumeration replaced a brute force, so it needs a
    # control that differs from it in exactly one variable -- the
    # pruning. A dropped pair would show as a MISSING low-height pair
    # and nothing else in the rig could see it.
    diff = 0
    for J in range(2, 10):
        row = binrow(J)
        N = N_of(row)
        strip = sorted(pairs_upto(row, N))
        brute = sorted((H_pair(row, a, b), a, b)
                       for a in range(-N, N + 1)
                       for b in range(-N, N + 1)
                       if (a, b) != (0, 0)
                       and H_pair(row, a, b) <= N)
        if strip != brute:
            diff += 1
    print("   C3 the strip enumeration against a brute-force box of "
          "side 2N+1, J = 2..9: %d depths differ" % diff)
    if diff:
        fired["K4"] += 1


def arm_D(fired):
    print("\nARM D -- THE CLOSED FORM AND THE SECOND MINIMUM'S RATIO")
    bad = 0
    for J in range(2, LEM_JMAX + 1):
        row = binrow(J)
        for k in range(J + 2):
            lhs = cof(row, k) - cof(row, k - 1)
            rhs_num = comb(J + 1, k) * (J + 1 - 2 * k)
            if lhs * (J + 1) != rhs_num:
                bad += 1
    print("   identity c_k - c_{k-1} = C(J+1,k)(J+1-2k)/(J+1): "
          "%d violations over J = 2..%d" % (bad, LEM_JMAX))
    if bad:
        fired["K1"] += 1
    # |d| is symmetric about (J+1)/2, since d_{J+1-k} = -d_k, so the
    # argmax always comes as a MIRROR PAIR and only its DISTANCE from
    # the centre is a number. Printing one member and a signed offset
    # would invite reading the sign as content.
    print("      J   argmax pair   distance from centre   sqrt(J+1)/2")
    for J in (10, 50, 100, 200):
        row = binrow(J)
        vals = [abs(cof(row, k) - cof(row, k - 1))
                for k in range(J + 2)]
        top = max(vals)
        ks = [k for k, v in enumerate(vals) if v == top]
        print("   %6d   %-11s %19.3f %13.3f"
              % (J, ks, abs((J + 1) / 2.0 - ks[0]),
                 sqrt(J + 1) / 2.0))
    print("      J        lambda_2/lambda_1   (sqrt(e)/2)sqrt(J+1)"
          "   rel err")
    rels = []
    for J in RATIO_LADDER:
        row = binrow(J)
        ratio = N_of(row) / D_of(row)
        pred = sqrt(E_CONST) / 2.0 * sqrt(J + 1)
        rel = abs(ratio - pred) / pred
        rels.append((J, rel))
        print("   %6d %19.4f %22.4f %9.2f%%"
              % (J, ratio, pred, 100.0 * rel))
    print("   deepest rung %.2f%%, and the error is NOT monotone in J: "
          "the argmax above is an integer while the saddle point is "
          "not, so what is left is a rounding oscillation and not a "
          "decaying series" % (100 * rels[-1][1]))


def pure_min(r, J):
    """Least pure-product height at rank r, depth J, and its argmin.

    Returns (ph, list of canonical cofactors attaining it, champion
    height, whether the champion attains ph).
    """
    base = ppow([-1, 1], J)
    champ = canon(ppow([1, 1], r - 1))
    best, bestset = None, []
    champ_h = None
    for (t, E) in cofactor_multisets(r, J):
        q = cofactor_poly(t, E)
        h = height(pmul(q, base))
        c = canon(q)
        if c == champ:
            champ_h = h
        if best is None or h < best:
            best, bestset = h, [c]
        elif h == best and c not in bestset:
            bestset.append(c)
    return best, bestset, champ_h, champ in bestset


def arm_E(fired):
    print("\nARM E -- THE BRIDGE AT RANK 2, J = 2..%d" % PURE_JMAX)
    seen = set()
    bad = 0
    for J in range(2, PURE_JMAX + 1):
        row = binrow(J)
        ph, _, _, _ = pure_min(2, J)
        if ph != D_of(row):
            bad += 1
    for J in range(2, PURE_JMAX + 1):
        for (t, E) in cofactor_multisets(2, J):
            seen.add(canon(cofactor_poly(t, E)))
    want = {canon([1]), canon([-1, 1]), canon([1, 1])}
    print("   rank-2 cofactors up to sign: %s"
          % sorted(seen, key=lambda p: (len(p), p)))
    print("   ph differs from D at %d of the %d depths"
          % (bad, PURE_JMAX - 1))
    if seen != want or bad:
        fired["K5"] += 1
    else:
        print("   so ph = D = h at rank 2, and h = ph there is a "
              "theorem rather than a range")


def arm_F(fired):
    print("\nARM F -- THE THRESHOLD: WHO BEATS THE CHAMPION, AND WHERE")
    lastbad = {}
    for r in (2, 3, 4):
        fam = cofactor_multisets(r, PURE_JMAX)
        print("   rank %d: %d cofactor multisets once the depth is "
              "deep enough to carry them all, champion (1+x)^%d"
              % (r, len(fam), r - 1))
        absent = [J for J in range(2, PURE_JMAX + 1)
                  if canon(ppow([1, 1], r - 1))
                  not in [canon(cofactor_poly(t, E))
                          for (t, E) in cofactor_multisets(r, J)]]
        if absent:
            print("      the champion is not in the family at all at "
                  "J = %s -- a pure product needs |E| <= J + t parts, "
                  "so (1+x)^%d needs J >= %d; those depths are NOT "
                  "non-attaining, they are empty of it"
                  % (absent, r - 1, r - 1))
        misses = []
        for J in range(2, PURE_JMAX + 1):
            if J in absent:
                continue
            ph, bestset, champ_h, attains = pure_min(r, J)
            if not attains:
                misses.append((J, ph, champ_h, bestset))
        for (J, ph, champ_h, bestset) in misses:
            print("      J = %2d  ph = %-8d champion = %-8d beaten by %s"
                  % (J, ph, champ_h,
                     [list(p) for p in bestset]))
        lastbad[r] = max((J for (J, _, _, _) in misses), default=None)
        print("      largest non-attaining depth: %s  (threshold %s)"
              % (lastbad[r],
                 2 if lastbad[r] is None else lastbad[r] + 1))
    got = (lastbad[2], lastbad[3], lastbad[4])
    want = (None, 6, 12)
    print("   largest non-attaining depths (r = 2, 3, 4): %s against "
          "the measured thresholds' prediction %s" % (str(got),
                                                      str(want)))
    if got != want:
        fired["K6"] += 1


def arm_G(fired):
    """The premises the rank-3 route would rest on, measured here.

    They belong in a rig and not in a roadmap: an aim that carries
    figures nothing prints is exactly the species this corpus keeps
    catching. Three readings, none of them a proof.
    """
    print("\nARM G -- WHAT A RANK-3 ATTEMPT WOULD REST ON")
    # (i) the reversal symmetry survives the antisymmetric row.
    anti = sym = 0
    for J in range(2, LEM_JMAX + 1):
        row = binrow(J)
        d = [cof(row, k) - cof(row, k - 1) for k in range(J + 2)]

        def hd(al, be):
            return max(abs(al * (d[k] if 0 <= k < len(d) else 0)
                           - be * (d[k - 1] if 1 <= k <= len(d) else 0))
                       for k in range(len(d) + 1))

        if any(d[J + 1 - k] != -d[k] for k in range(J + 2)):
            anti += 1
        for al in range(-4, 5):
            for be in range(-4, 5):
                if (al, be) != (0, 0) and hd(al, be) != hd(be, al):
                    sym += 1
    print("   the first-difference row is antisymmetric "
          "(d_{J+1-k} = -d_k): %d violations over J = 2..%d"
          % (anti, LEM_JMAX))
    print("   and the reversal symmetry SURVIVES it -- "
          "H_d(a, b) = H_d(b, a): %d violations" % (anti + sym))
    if anti or sym:
        fired["K1"] += 1
    # (ii) the transplanted L4, and (iii) the evaluation bound at -1.
    hs = {}
    for J in range(2, LEM_JMAX + 1):
        hs[J] = [height(pmul(ppow([1, 1], t), ppow([-1, 1], J)))
                 for t in range(3)]
    l4 = [J for J in range(2, LEM_JMAX + 1) if hs[J][2] > hs[J][1] - 1]
    ev = [J for J in range(2, LEM_JMAX + 1)
          if 2 ** J <= hs[J][2] * (J + 3)]
    print("   the transplanted D <= N - 1 (here D2 <= D1 - 1) FAILS at "
          "J = %s and holds at every J from %d to %d"
          % (l4, max(l4) + 1, LEM_JMAX))
    print("   the evaluation bound 2^J/(J+3) exceeds D2 at every J from "
          "%d to %d and fails at J = %s"
          % (max(ev) + 1, LEM_JMAX, ev))
    print("   so neither premise holds at the depths where rank 3's "
          "own threshold sits, and both are measurements, not proofs")


def main():
    t0 = time.time()
    fired = {"K1": 0, "K2": 0, "K3": 0, "K4": 0, "K5": 0,
             "K6": 0}
    arm_C(fired)          # controls first, before any verdict is read
    arm_A(fired)
    arm_B(fired)
    arm_D(fired)
    arm_E(fired)
    arm_F(fired)
    arm_G(fired)
    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
