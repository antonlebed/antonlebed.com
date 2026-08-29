"""explore_flatten_d2.py -- IS PRODUCT EXTREMALITY A HEIGHT-1 ACCIDENT?
BUILD d_2(J).

explore_flatten_offchart.py rebuilt the pure-product law on the inverse
dial -- h(M, J), the least HEIGHT of a nonzero M-atom vector whose first
J moments vanish -- exhaustively at the 63 cells M <= 12 and at 18 more
out to M = 30, and then named the object whose absence stopped the other
136: d_k(J), the least DEGREE of a multiple of (x-1)^J of height at most
k, of which the literature it contacted holds only k = 1. That object is
what this rig builds at k = 2, and the two are inverses of each other:

    h(M, J) <= k   iff   M > d_k(J),

since a vector on M atoms is a polynomial of degree < M and the least
such degree is d_k(J) by definition. So the k = 2 boundary of the whole
chart is ONE SEQUENCE, and every cell of it at every width follows from
one number per depth.

(FLATTENING, HEIGHT, the FREE BOX and the PURE-PRODUCT family keep
explore_flatten_height.py's senses, restated because this rig is read
alone: a vector c on M atoms is the polynomial P(x) = sum_r c_r x^r; its
moments m_j = sum_r C(r,j) c_r are its coefficients in the (x-1) basis,
so the flattening J(c) -- the least j with m_j nonzero -- IS the
multiplicity of the root 1. HEIGHT is the sup-norm max_r |c_r|. A PURE
PRODUCT is prod_i (x^{d_i} - 1) over a multiset D of positive parts; it
has |D| factors and degree sum D.)

THE QUESTION. Two halves, and the second is the one that matters.
  (a) What is d_2(J)?
  (b) Is the pure-product family extremal for it -- as the classical
      determination reports it to be at k = 1 -- or is that a height-1
      accident?

THE INCUMBENT, and where it says we hold nothing. The classical
determination is the HEIGHT-1 statement: Borwein-Mossinghoff
(Experimental Mathematics 9:3, 2000) fix coefficients in {-1, 0, 1} and
minimise the degree; OEIS A059753 carries d_1(n) at n = 1..14 as
1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69, 93, 112, 120, minimal through
14 since 2025, and the paper reports every extremal a pure product for
n <= 10. Nothing here extends that diagonal. FOUR searches over the
height-1 literature were run before this rig was designed -- on the
minimal degree of a bounded-height multiple of (x-1)^n, on the
Borwein-Mossinghoff paper's own generalisations, on an OEIS sequence for
a height-2 analogue, and on the paper's descendants -- and none reached
a height-k statement for k >= 2. That is a BOUNDED CONTACT and not a
proof that none exists; it is what the rig was built on top of.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE HEIGHT-DOMAIN RECURSION, and why it is a different instrument
from the parent's. Writing P = (x-1)R and comparing coefficients gives
R_t = R_{t-1} - P_t with R_{-1} = 0, so the quotient by (x-1) is the
signed running sum of the coefficients. Iterating, define A_0(t) = P_t
and A_j(t) = A_j(t-1) - A_{j-1}(t): A_j is the t-th coefficient of the
j-fold quotient, and (x-1)^J divides P exactly when A_j(N) = 0 for
j = 1..J, where N is the degree. So the search runs over the
COEFFICIENTS of P, each in [-k, k], carrying a J-vector of accumulators
-- branching 2k+1 per position and N+1 positions deep. The offchart
rig's interval-pinned route runs over the QUOTIENT instead, branching
2k+1 over M - J positions: its cost is (2k+1)^rank and falls with the
RANK, this one's is (2k+1)^(N+1) before pruning and falls with the
HEIGHT. They fail at opposite ends, which is exactly the shape of the
72 brackets the offchart rig left standing.

SECOND, THE PROPAGATION BOUND -- the prune that makes the height domain
affordable, and THE OBVIOUS VERSION OF IT IS UNSOUND. A first probe
pruned on the accumulator itself, |A_j(t)| > k*C(m+j, j) with m = N - t
remaining: that treats the lower levels as if they were zero, and they
are not -- a large A_1 keeps driving A_2 whatever the future
coefficients do, so the bound does not cover the motion it is supposed
to and the prune can cut a live branch. It is recorded here because it
is the failure a sound-looking bound invites, and because a search that
prunes live branches returns d_2 values that are too LARGE while looking
exactly like a completed exhaustive search.

The sound version splits the future into propagation plus contribution.
With all future coefficients zero, the accumulators drift by pure
convolution, so A_j(N) would land at
    Z_j = sum_{i=1..j} (-1)^(j-i) C(m+j-i-1, j-i) A_i(t).
A future coefficient P_r enters A_1 from position r onward and reaches
A_j(N) with coefficient (-1)^j C(N-r+j-1, j-1), so the whole future
contribution to A_j(N) is bounded by
    k * sum_{r>t} C(N-r+j-1, j-1) = k * C(m+j-1, j).
Hence A_j(N) = 0 forces |Z_j| <= k*C(m+j-1, j), and violating that at
any j <= J prunes. This is the rig's central instrument.

THIRD, THE BACKWARD SET, and its size is EXACTLY (2k+1)^L. Reading the
recursion backwards: if the state after choosing P_u is (B_1..B_J) and
that choice was p, then the state before it is A_j = B_j + B_{j-1} with
B_0 = p. That map is injective in (B, p) -- p is recoverable as
A_1 - B_1 -- so the set G_L of states from which the last L positions
can complete to all-zero has EXACTLY (2k+1)^L members, with no collapse
to hope for. Storing it turns the last L levels of the forward search
into one membership test. Since the tree's node count is dominated by
its deepest level, this is worth a factor of roughly (surviving
branching)^L, and the binding constraint is memory rather than time: the
states are packed into single integers against per-coordinate bounds
k*C(L+j-1, j), which is what keeps L = 9 at J = 8 inside the envelope
where a tuple set does not.

FOURTH, WLOG THE CONSTANT TERM IS POSITIVE. At the minimal degree
P_0 != 0, since P = x*P' would make P' a multiple of (x-1)^J of the same
height and lower degree; and P and -P are both solutions. So the search
fixes P_0 in 1..k, a free factor of (2k+1)/k at the root.

FIFTH, THE CYCLOTOMIC FLOOR -- a LOWER bound on d_k(J) at every J and
every k, at no compute, and it is the classical proof's own mechanism.
Let P = (x-1)^J q have height <= k and degree <= N, let m = p^e > 1 and
let w be a primitive m-th root of unity. Either Phi_m divides q, or the
resultant Res(Phi_m, q) = prod_{a in (Z/m)*} q(w^a) is a nonzero
rational integer and so at least 1 in absolute value. In the second case
|q(w^a)| = |P(w^a)| / |w^a - 1|^J <= k(N+1) / |w^a - 1|^J, and
prod_a |w^a - 1| = |Phi_m(1)| = p for a prime power, so
    1 <= (k(N+1))^phi(m) / p^J,  i.e.  J*log p <= phi(m)*log(k(N+1)).
Contrapositive: when J*log p > phi(m)*log(k(N+1)), Phi_m DIVIDES P. The
forced Phi_{p^e} are pairwise coprime and coprime to (x-1)^J, so
    N >= J + sum phi(p^e) over every forced prime power,
and the least N surviving that is a floor on d_k(J). The bound
|P(w)| <= k(N+1) is the crude one; a sharper one is available by
reducing P modulo x^m - 1, and is not taken here.

SIXTH, WHAT THE FLOOR BUYS ON THE CHART. h(M, J) >= k+1 exactly when
M <= d_k(J), so every floor on d_k is a floor on h -- at every k, not
only at k = 1 where the offchart rig's arm 5 had to stop. That is the
half the brackets were missing, and it costs nothing.

SEVENTH, THE SMALL-J CLOSED FORMS the route must reproduce. At J = M-1
the lattice has rank 1 and h(M, M-1) = C(M-1, floor((M-1)/2)); at k = 1
the ladder must be A059753; and h >= 1 for every nonzero integer vector.

WHAT WAS ALREADY MEASURED BEFORE THE SLATE WAS FROZEN, stated so that no
prediction below is read as one it is not. Scratch probes established,
before this file existed: the k = 2 ladder at J = 1..7 (1, 2, 4, 7, 11,
16, 22), the least-sum height-<=2 pure product at J = 1..8 (the same
seven values, then 26 at J = 8), the cyclotomic floor's whole table, and
that a first, UNSOUND prune agreed with the sound one at J <= 6. Those
J <= 7 values are REPRODUCTIONS here and not predictions. The
predictions below are what the probes did not reach.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. PRODUCT EXTREMALITY SURVIVES AT HEIGHT 2 WHERE IT FIRST COULD
      FAIL. d_2(8) = 26, the least-sum height-<=2 pure product, and NOT
      29. This is the sharp cell: J <= 7 fits C(J,2)+1 exactly
      (1, 2, 4, 7, 11, 16, 22) and the product family leaves that
      arithmetic pattern at J = 8, so the two candidate answers separate
      here for the first time and the product's is the smaller.
  P2. THE CLOSED FORM IS AN ARTEFACT OF SMALL J. d_2(J) = C(J,2)+1 at
      every J <= 7 and NOT at J = 8.
  P3. THE INCUMBENT LADDER. Run at k = 1 the same route returns
      A059753: 1, 3, 6, 11, 15, 22, 30 at J = 1..7.
  P4. THE FLOOR IS SOUND AND WEAK. The cyclotomic floor never exceeds a
      value an exhibited vector establishes, and is STRICTLY below it at
      every J >= 3 on both diagonals it can be checked on (k = 1 against
      A059753, k = 2 against the ladder).
  P5. THE TWO ROUTES ARE COMPLEMENTARY, WHICH IS THE POINT OF BUILDING
      THE SECOND ONE. The offchart rig's small-ceiling large-rank
      brackets are decided by the ladder, which the quotient route could
      not decide at a 150-million-node cap; and its widest bracket,
      [7, 77] at M = 17, J = 12, is decided by the cyclotomic floor and
      NOT by the ladder.
  P6. EXTREMALS ARE NOT UNIQUE BUT THE PRODUCT IS AMONG THEM. At every J
      where all minimal-degree height-<=2 vectors are enumerated, at
      least one is a pure product up to sign and reversal, and the count
      of extremals exceeds 1 at some J >= 4.

KILLS, as observables rather than inferences.
  K-A. PRODUCT EXTREMALITY REFUTED AT HEIGHT 2: a J where the ladder's
       d_2(J) is STRICTLY BELOW the least-sum height-<=2 pure product.
       The J, both degrees, the witness vector and the product's
       multiset are printed.
  K-B. ROUTE DISAGREEMENT: any (M, J, k) where the height-domain route
       and the offchart rig's interval-pinned quotient route, or full
       brute force, differ on "is there a nonzero height-<=k vector of
       flattening >= J on M atoms". The cell and both answers print.
       ANY K-B FIRING BARS READING K-A's ABSENCE AS EVIDENCE.
  K-C. INCUMBENT DISAGREEMENT: a J <= 7 where the k = 1 ladder differs
       from A059753. The J and both values print.
  K-D. FLOOR UNSOUND: a (k, J) where the cyclotomic floor EXCEEDS a
       degree at which a vector of that height is exhibited. The k, J,
       floor and exhibited degree print.
  K-E. CLOSED-FORM DISAGREEMENT: the height-domain route disagreeing
       with C(M-1, floor((M-1)/2)) at J = M-1.

CONTROLS, run and read BEFORE any verdict, each printing how many cases
it exercised.
  C1 (POSITIVE, PARITY). The height-domain route against FULL brute
     force over [-k,k]^(N+1) on the predicate, at the degrees the brute
     route can pay for. Comparisons that ACCEPT are counted separately
     from ones that reject -- the offchart rig's C1 was read at nearly a
     third more strength than it had for want of exactly that split.
  C2 (INDEPENDENT ALGORITHM). The height-domain route against the
     offchart rig's interval-pinned quotient DFS, which shares no code
     and no cost law with it, over M = 4..13, J = 1..M-1, k = 1..3.
     This is the control that licenses the route at widths C1 cannot
     pay for.
  C3 (INCUMBENT). The k = 1 ladder against A059753 (P3, K-C).
  C4 (TAIL). The height-domain route against the rank-1 closed form
     h(M, M-1) = C(M-1, floor((M-1)/2)) at M <= 7, which is where the
     route can pay: the closed form is 35 at M = 8 and 462 at M = 12,
     and a route whose backward set is (2k+1)^L cannot be run at a
     height of 462. The tail beyond M = 7 is the offchart rig's C3 and
     is not re-established here (K-E).
  C5 (FLOOR SOUNDNESS). The cyclotomic floor against every d_k value
     this rig or the incumbent establishes (P4, K-D).

THE ARMS.
  1. THE HEIGHT-DOMAIN ROUTE. The predicate "is there a nonzero
     polynomial of degree <= N, height <= k, divisible by (x-1)^J", by
     DFS over the coefficients under the propagation bound, meeting a
     packed backward set over the last L positions. Every other arm is
     built on it (C1, C2, C4).
  2. THE LADDER. d_k(J) = the least N the predicate accepts, by scanning
     N upward from J. Run at k = 1 as the incumbent control and at k = 2
     as the object. Where affordable it also ENUMERATES every extremal
     at the minimal degree and reports how many are pure products up to
     sign and reversal (P1, P2, P3, P6, K-A, K-C).
  3. THE PRODUCT FAMILY AT HEIGHT <= k. Least degree over multisets D
     with |D| >= J whose product has height <= k, by the offchart rig's
     product table. The partner of arm 2 in the extremality test, and
     the only arm that reaches past the ladder (P1, K-A).
  4. THE CYCLOTOMIC FLOOR. The hand attack's fifth section, tabulated
     over k = 1..9 and J = 1..15 (P4, C5, K-D).
  5. THE BRACKET SWEEP. h(M, J) at M = 4..30, J = 2..12, with the
     ceiling from arm 3 and the floor from the best of: the ladder
     (h >= k+1 wherever M <= d_k(J)), the cyclotomic table, A059753 as
     a cited k = 1 floor, and the quotient route under a node cap. The
     count that matters is how many cells close and by WHICH instrument
     (P5).

RESOURCE NOTE. Exact integer arithmetic, no numpy, so no BLAS arenas.
The backward set is the memory: packed integer keys against
per-coordinate bounds, (2k+1)^L keys exactly, measured at 178 MB for
k = 2, J = 8, L = 9 -- the largest built here -- against a tuple set's
556 MB for the same, which is why the packing exists. L is therefore
set BY that budget rather than fixed: the largest L with
(2k+1)^L * J within a coordinate budget, capped by the degree. The
budget counts keys TIMES COORDINATES and not keys, because a packed key
is a J-digit integer -- a key-only budget held L = 9 at k = 2 all the
way to J = 12, where the same 1.95 million keys cost half again what
they cost at J = 8, and that is what put a first run over the line. And the cache is capped too -- a set built for one
L answers about a different suffix length and is wrong at another, so L
is part of its key, and an uncapped cache over the control grid's
(J, k, L) triples would hold half a gigabyte of them at once --
so exactly one is kept, which costs nothing where it matters because
the ladder's inner scan over the degree holds L fixed. Wall is
dominated
by the k = 2 ladder's last refutation, and the whole run is estimated at
20 to 30 minutes: over the ten-minute line and named as such, because
the cell that decides P1 is J = 8 and nothing cheaper reaches it -- the
quotient route leaves it bracketed at a 150-million-node cap and the
product family gives only the upper half. Run under memwatch at the
512 MB default.

RUN RECORD (final run: wall 1947.4 s, peak working set 309.7 MB, peak
commit 304.8 MB under memwatch's 512 MB default; the k = 2 ladder is
858.6 s of it and its J = 8 row alone 795.0 s, the controls and arm 5's
sweep dividing the other 1082 s, which the run does not itemise. The
wall is past the 20-to-30-minute estimate above by about a tenth, and
the estimate is left as frozen). SEVEN runs, of which four produced a
verdict, and all four printed the same values. The first two never
reached one: they were KILLED at
the memory ceiling inside C2, at 573.7 and 574.3 MB, and the second
died at the same place as the first because the first fix was aimed at
the wrong half -- the budget was reweighted from keys to
keys-times-coordinates, which is a real correction and was not the
fault. The fault was that the suffix length ignored the DEGREE it was
being built for: the control grid runs at degrees under 13 and was
building sets sized for degree 30 at every cell, and since a freed
arena does not reliably go back to the operating system, the peak was
an accumulation over a hundred builds rather than any single set. The
cap L <= N//2 + 1 fixed it, and it costs the ladder nothing, the
ladder's degrees all being past twice its budgeted L. The third run
completed and its verdict stands unchanged below; the fourth changed
one thing, in arm 5 rather than in a number: the sweep TREATED THE
QUOTIENT ROUTE AS A FLOOR ONLY. That route answers in both directions,
and a witness at height k, arriving after every height below k has been
refuted, IS h -- so a cell it could have decided outright was being
reported as a bracket. The fourth run uses it as a ceiling too and
reproduced the third EXACTLY, 174 and 78 and the same widest bracket,
because in this range the route never returns a witness before its node
cap: the path that was wrong is one no cell here took. It is a latent
mis-report closed, and the numbers below are from a sweep where the
closing changed nothing.

The fifth was ABANDONED BY HAND a minute in, and what it was abandoned
for is F4: the finding that the height-2 extremal is unique had been
read as a CONTRAST with height 1, on the strength of the classical
paper reporting that it computed all the extremals -- an inference from
someone else's phrasing about a count, standing where a measurement
cost under a second. The k = 1 ladder now enumerates too, and it
returns one extremal per depth as well, so the contrast is deleted
rather than sourced. The sixth and final run carries that enumeration
and one correction to the LADDER ITSELF, which is the only fault here
that could have changed a printed value: it resumed the scan at the
previous depth's answer PLUS ONE. d_k is nondecreasing in J, which
licenses resuming AT that answer and not past it -- nondecreasing
permits d_k(J) = d_k(J-1), and a scan starting one degree high cannot
see a repeat, so it would report one too large while still printing a
strictly increasing sequence that looks exactly right. The fix costs
one refutation per depth at a degree already known to be short. Every
value is unchanged, which is now ESTABLISHED rather than assumed: no
d_k repeats anywhere in either ladder.

AND THAT FIX TOOK TWO ATTEMPTS, which is worth more than the fix. The
sixth run was launched believing it carried the correction, and its
record was written saying so; the correction was not in the file. The
edit had been made in a command chain that was killed before it wrote,
and nothing checked -- the file was not re-read and the new text was
not grepped for. The run that followed printed identical values for the
honest reason that there is no repeat to find, so its output could not
have revealed the absence either, and a record that asserts a change is
worth exactly the check that the change landed. The seventh run carries
the fix verified by grep before launch and by an instrumented call
after, which shows each depth re-testing the previous depth's degree.
No prediction, kill or control was touched at any point.

F1. EVERY CONTROL PASSES AND EVERY KILL IS SILENT, and the control that
matters is C2. C1 (parity) compares 77 predicates against FULL brute
force over [-k,k]^(N+1) -- and READ THE SPLIT: 49 of them ACCEPT and 28
REJECT, and it is the 28 refutations that license a LADDER, because
d_k(J) is set by the degrees at which nothing exists and a route that
only ever found things could be wrong at every one of them. But brute
force is (2k+1)^(N+1) and stops at degree 7, while the ladder runs to
degree 30. C2 covers the next stretch: 225 predicates over M = 4..13,
J = 1..M-1, k = 1..3 against the offchart rig's interval-pinned
quotient DFS -- a route sharing no code and no cost law with this one,
(2k+1)^rank against a coefficient search under a propagation bound --
0 skipped on the node cap and 0 mismatches. READ ITS CEILING AND NOT
ITS COUNT: those 225 stop at DEGREE 12, and the k = 2 ladder runs to
26. What covers the deep stretch is C3 rather than C2, and it covers
only half of it: the same route run at k = 1 returns A059753 at
J = 1..7, an externally proved table matched at degrees 22 and 30, well
past anything C2 reaches -- but at k = 1. So the licensed region is
(k <= 3, degree <= 12) by C2 and (k = 1, degree <= 30) by C3, and a
fault specific to k = 2 above degree 12 is checked by NEITHER. That is
the residual, stated because the offchart rig's own audit found exactly
this shape -- a route licensed nowhere near the widths it runs at --
and a control that passes says nothing about what it does not reach.
C4 (rank-1 tail) 6 cases, 0
mismatches. C5 (floor soundness) 22 checks, 0 unsound. K-A, K-B, K-C,
K-D and K-E all silent.

F2. THE OBJECT IS BUILT, AND C3 IS WHAT MAKES IT CREDIBLE (rule,
exhaustive at J <= 8):
    d_2(J) = 1, 2, 4, 7, 11, 16, 22, 26   at J = 1..8,
the least degree of a nonzero multiple of (x-1)^J with every
coefficient in [-2, 2]. Run at k = 1 with nothing else changed, the
same route returns 1, 3, 6, 11, 15, 22, 30 at J = 1..7 -- A059753
exactly, unaided, which is the incumbent's own table recomputed by an
instrument built for the other height (P3 holds 7 for 7, K-C silent).
A ladder that reproduces the classical diagonal is a ladder allowed to
state the one beside it.

F3. PRODUCT EXTREMALITY IS NOT A HEIGHT-1 ACCIDENT (rule, exhaustive at
J <= 8, K-A silent). At every one of the eight depths d_2(J) EQUALS the
least degree over pure products of height at most 2, and the attaining
multisets are (1), (1,1), (1,1,2), (1,1,2,3), (1,1,2,3,4),
(1,1,2,3,4,5), (1,1,2,3,4,5,6), (1,1,2,3,3,4,5,7). The classical
determination reports every extremal a pure product at height 1 and
depth <= 10; that report now has a companion at the other height, and
P1 is what tested it rather than assumed it. THE SHARP CELL IS J = 8
and it is sharp because the two candidate answers separate there: the
first seven values fit C(J,2) + 1 exactly, which would give 29, and the
product family gives 26. The ladder returns 26 (P1, P2 both hold). The
arithmetic pattern is an ARTEFACT of small J and the product law is
not, which is the whole content of running the ladder one depth past
where the pattern was fitted. Note the shape of that eighth multiset:
at J = 2..7 it is 1 and 1 followed by the consecutive integers up to
J - 1 -- which is exactly why those degrees are C(J,2) + 1 -- and the
eighth breaks BOTH halves of that, repeating a part (3, 3) and skipping
one (no 6). The pattern in the degrees and the pattern in the multisets
die at the same depth, which is what says they were one fact.

F4. THE EXTREMAL IS UNIQUE AT BOTH HEIGHTS, AND P6 IS HALF REFUTED.
Enumerating every minimal-degree vector with a positive constant term
-- so each printed solution stands for a sign pair -- there is EXACTLY
ONE at height 2 for every J = 2..7, and it is the pure product. P6's
first half holds; its second half, that the extremal count exceeds 1
somewhere at J >= 4, is FALSE across the whole enumerated range. The
only depth with two is J = 1, where they are (1, -1) and its doubling
(2, -2), so even there the polynomial is unique up to scaling. THE
HEIGHT-1 LADDER WAS THEN ENUMERATED TOO, and this is why: the first
reading of that uniqueness called it a difference from the height-1
problem, on the ground that the classical determination reports
computing ALL the extremals -- which is an inference from someone
else's phrasing about how many there are, and it is wrong. Run at k = 1
the same enumeration returns EXACTLY ONE at every J = 1..6 as well. The
minimum is rigid at both heights, the enumeration is cheap at k = 1 and
no prediction had asked for it, and the contrast that made the rigidity
look like a height-2 phenomenon does not exist.

F5. THE FLOOR IS SOUND, FREE, AND TOO WEAK TO CLOSE A SINGLE CELL. The
cyclotomic argument tabulates a lower bound on d_k(J) at every k = 1..9
and J = 1..15 at no compute. It is SOUND at all 22 checks against an
exhibited value and STRICTLY below at 18 of them, the four equalities
all sitting at J <= 2 -- so P4 holds exactly as frozen, strict at every
J >= 3 (K-D silent). How weak: at k = 1 it gives 14 where A059753 gives
30, and at k = 2 it gives 10 where the ladder gives 22, both at J = 7.
AND THE SWEEP'S OWN ATTRIBUTION IS THE VERDICT ON IT -- the floor
appears NOWHERE in arm 5's list of what closed a cell. It raises floors,
at (17, 12) from 2 to 7, and it is never the instrument that meets a
ceiling. P5's SECOND HALF IS THEREFORE REFUTED, and it was refuted by a
number the slate had in hand: the prediction said the widest offchart
bracket, [7, 77] at M = 17, J = 12, would be decided by this floor, and
d_6(12) >= 19 > 17 does give h >= 7 -- but 7 is that bracket's LOWER end
and 77 its upper, the product there being (1^9, 2, 2, 3) at height 77.
The floor reproduces, for free and without a search, exactly the lower
bound the offchart rig's aborted deepening had already paid for; it does
not meet anything. What it uniquely does is bound d_k above height 1 at
depths no ladder reaches, and on this evidence that capability is not
yet worth a cell. The crude bound |P(w)| <= k(N+1) is what makes it
weak, and sharpening it by reducing P modulo x^m - 1 is the obvious next
move and is not taken here.

F6. WHAT THE SWEEP DECIDES, AND P5 IS HALF RIGHT. Over the 252 cells
M = 4..30, J = 2..12: 174 decided, 78 bracketed. READ THE 174 AND NOT
THE FRACTION -- 93 of them carry a product bound of 1, where h = 1
follows from h >= 1 for any nonzero integer vector and nothing whatever
is measured. The informative 81 split by the instrument that closed
them: 31 by the quotient route, 28 by A059753 as a cited height-1
floor, 22 by the d_2 ladder, and NONE by the cyclotomic floor (F5). So
P5's first half holds and its second does not. The ladder does take the
small-ceiling large-rank end the quotient route could not: the offchart
rig's own probe left M = 19 and M = 20 at J = 7 undecided at a
150-million-node cap after 167 s each, and d_2(7) = 22 puts h >= 3 at
both against a product ceiling of 3, so both are h = 3 by arithmetic,
as is the whole k = 2 boundary at every width and every J <= 8. Those
two are named because they were MEASURED as out of reach; the other 20
of the 22 are cells the ladder closed and no attempt was made here to
ask which of them the offchart rig could have closed another way, so
the 22 are not claimed as its misses.

The 78 that remain include a LOW-RANK, HUGE-CEILING corner the sweep's
range now takes in -- HOW MUCH of the 78 is that corner is NOT measured
here, the sweep printing no rank distribution, and the reading below
rests on the widest cell alone. That cell is [100, 264] at M = 15,
J = 12, of rank 3, where the floor table stops at k = 9 and the
quotient route's deepening passes its node cap at k = 100 -- the sum over k of
(2k+1)^3 being what a deepening pays, so reaching 264 costs on the
order of 10^10 nodes. WHAT THAT CORNER WANTS IS NOT SETTLED HERE AND
THE OBVIOUS READING IS PROBABLY WRONG. It looks like a floor problem
because the floor is what stops, but the cell is a sup-norm minimum
over a lattice of RANK 3, and a deepening in k is a poor instrument for
one: an LLL reduction of the rank-3 lattice followed by a bounded
enumeration would answer it directly and was not tried. So "more
compute does not help" is exactly the claim this rig has not earned,
and the corner is recorded as open with two candidate routes rather
than one.

(SETTLED SINCE, by explore_flatten_lattice.py, which took the second of
those two routes: a reduction plus an exhaustive enumeration of the L2
ball of radius H*sqrt(M) -- H the sup norm of any exhibited lattice
vector, which needs no ceiling from the product family -- decides all
252 cells of F6's sweep, the 78 brackets included, in 127.5 s and
30,158 nodes total against the 10^10 a deepening needs for one of them.
The widest is h(15, 12) = 264, the product's own height. F5 and F6 are
unchanged as records of what THIS rig decided, and two of their
readings are superseded. First, the corner is not low-rank: the rank
distribution of the 78, which this sweep does not print, runs from 3 to
21 with a median of 11 against 12 over all 252 cells, so reading the
corner off the widest bracket read the one cell guaranteed to be
unrepresentative -- brackets are wide at low rank because a deepening's
cost is (2k+1)^rank. Second, and larger: PURE-PRODUCT EXTREMALITY IS
FALSE off the charted range. At 249 of the 252 h is the least height of
a pure product; at h(21, 12), h(23, 10) and h(25, 12) it is strictly
below one, 39 against 44, 9 against 10 and 25 against 28, each on an
exhibited vector cleared by J synthetic divisions. Nothing in F2 or F3
is touched -- d_2(J) at J <= 8 and its equality with the least-degree
height-2 product are exhaustive and stand -- and the failures sit at
widths this ladder never reached.)
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import sys
import time
from math import comb as _comb, log

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import (NodeCap, Products, feasible,
                                      mul_shift)

A059753 = [1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69, 93, 112, 120]

PRODUCT_BUDGET = 44
LADDER_K1 = 7
LADDER_K2 = 8
ENUM_K2_J = 7
ENUM_K1_J = 6
SWEEP_M = 30
SWEEP_J = 12
NODE_CAP = 4000000
COORD_BUDGET = 16000000
CACHE_MAX = 1


def comb(n, r):
    """C(n, r) with the empty-product convention at r = 0, which the
    propagation bound needs at m = 0."""
    return 1 if r == 0 else (0 if n < r else _comb(n, r))


# ------------------------------------- arm 1: the height-domain route

def backward_set(J, L, k):
    """G_L: the states from which the last L positions complete to
    all-zero, packed to integer keys. EXACTLY (2k+1)^L members (hand
    attack, third section) -- the predecessor map has no collisions, so
    that is a size and not an estimate."""
    bnd = [0] + [k * comb(L + j - 1, j) for j in range(1, J + 1)]
    mul = [0] * (J + 1)
    m = 1
    for j in range(1, J + 1):
        mul[j] = m
        m *= 2 * bnd[j] + 1
    cur = {(0,) * J}
    for step in range(L):
        last = step == L - 1
        nxt = set()
        for B in cur:
            for p in range(-k, k + 1):
                prev = p
                A = []
                for j in range(J):
                    A.append(B[j] + prev)
                    prev = B[j]
                if last:
                    key = 0
                    for j in range(1, J + 1):
                        key += (A[j - 1] + bnd[j]) * mul[j]
                    nxt.add(key)
                else:
                    nxt.add(tuple(A))
        cur = nxt
    return cur, bnd, mul


class Route(object):
    """The height-domain predicate, with its backward set cached by
    (J, k, L). A set built for one L is WRONG at another -- the cut sits
    at N - L and a mismatched set answers about a different suffix
    length -- so L is part of the key and never defaulted."""

    def __init__(self, budget=COORD_BUDGET):
        self.budget = budget
        self._cache = {}

    def suffix_len(self, J, k, N):
        """The largest L whose backward set fits the memory budget,
        capped by the degree. Memory, not taste, sets it (hand attack,
        third section): the set has exactly (2k+1)^L members, and the
        budget counts KEYS TIMES COORDINATES rather than keys, because a
        packed key is a J-digit integer -- at J = 12 the same key count
        that measured 178 MB at J = 8 costs half again as much. And L is
        capped at N//2 + 1 whatever the budget allows, because past the
        middle the set is buying suffix the forward search was never
        going to reach: without that cap the CONTROL grid, whose degrees
        are all under 13, built sets sized for degree 30 at every one of
        its cells, and Python returns a freed arena to the operating
        system only sometimes -- so the peak that killed a first run was
        an accumulation across builds and not any single set."""
        cap = min(N, N // 2 + 1)
        L, size = 0, 1
        while L < cap and size * (2 * k + 1) * J <= self.budget:
            size *= 2 * k + 1
            L += 1
        return max(L, 1)

    def _G(self, J, k, L):
        key = (J, k, L)
        if key not in self._cache:
            if len(self._cache) >= CACHE_MAX:
                self._cache.clear()
                gc.collect()
            self._cache[key] = backward_set(J, L, k)
        return self._cache[key]

    @staticmethod
    def _tables(N, J, k):
        W = [[None] * (J + 1) for _ in range(N + 2)]
        BD = [[0] * (J + 1) for _ in range(N + 2)]
        for m in range(N + 2):
            for j in range(1, J + 1):
                W[m][j] = [((-1) ** (j - i)) * comb(m + j - i - 1, j - i)
                           for i in range(1, j + 1)]
                BD[m][j] = k * comb(m + j - 1, j)
        return W, BD

    def run(self, N, J, k, collect=False):
        """(found, nodes, solutions) for degree <= N. With collect,
        every solution is enumerated rather than the first returned; the
        constant term is pinned positive, so each stands for a sign pair
        (hand attack, fourth section)."""
        if N < J:
            return False, 0, []
        L = self.suffix_len(J, k, N)
        G, bnd, mul = self._G(J, k, L)
        W, BD = self._tables(N, J, k)
        cut = N - L
        nodes = [0]
        sols = []
        rng = range(-k, k + 1)

        def rec(t, A, pre):
            m = N - t
            Wm, Bm = W[m], BD[m]
            for p in (range(1, k + 1) if t == 0 else rng):
                nodes[0] += 1
                B = [0] * (J + 1)
                prev = p
                for j in range(1, J + 1):
                    prev = A[j] - prev
                    B[j] = prev
                if t == cut:
                    key, ok = 0, True
                    for j in range(1, J + 1):
                        v = B[j] + bnd[j]
                        if v < 0 or v > 2 * bnd[j]:
                            ok = False
                            break
                        key += v * mul[j]
                    if ok and key in G:
                        if not collect:
                            return True
                        _tail_walk(N, J, k, B, pre + [p], sols)
                    continue
                ok = True
                for j in range(1, J + 1):
                    w, Z = Wm[j], 0
                    for i in range(1, j + 1):
                        Z += w[i - 1] * B[i]
                    if Z > Bm[j] or -Z > Bm[j]:
                        ok = False
                        break
                if not ok:
                    continue
                if rec(t + 1, B, pre + [p] if collect else pre):
                    return True
            return False

        found = rec(0, [0] * (J + 1), [])
        if collect:
            found = bool(sols)
        return found, nodes[0], sols


def _tail_walk(N, J, k, state, pre, out):
    """Expand a backward-set hit into every completion. Only ever called
    on a state the set has certified, so the walk cannot come back
    empty -- and an empty walk means the set and the recursion disagree
    about what the state is, so it raises rather than returning."""
    before = len(out)

    def walk(t, A, acc):
        if t > N:
            if not any(A[1:]):
                out.append(list(acc))
            return
        for p in range(-k, k + 1):
            B = [0] * (J + 1)
            prev = p
            for j in range(1, J + 1):
                prev = A[j] - prev
                B[j] = prev
            acc.append(p)
            walk(t + 1, B, acc)
            acc.pop()

    walk(len(pre), state, list(pre))
    if len(out) == before:
        raise AssertionError(
            "backward set certified a state at N=%d J=%d k=%d that no "
            "completion reaches -- the set and the recursion disagree"
            % (N, J, k))


# --------------------------------------------- arm 2: the d_k ladder

def ladder(route, k, jmax, enum_to=0):
    """d_k(J) for J = 1..jmax, plus every extremal where enumerated.
    d_k is NONDECREASING in J -- a multiple of (x-1)^(J+1) is one of
    (x-1)^J, so the achievable degrees only shrink -- which licenses the
    scan to resume at the previous depth's answer instead of at J. AT
    it, not past it: nondecreasing permits d_k(J) = d_k(J-1), and a scan
    that starts one degree higher cannot see a repeat and would report
    it as one too large, silently and while still printing a strictly
    increasing sequence. The extra cost is one refutation per depth at a
    degree already known to be short by one."""
    out = {}
    prev = 0
    for J in range(1, jmax + 1):
        N = max(prev, J - 1)
        t0 = time.time()
        while not route.run(N, J, k)[0]:
            N += 1
        prev = N
        extremals = None
        if J <= enum_to:
            extremals = route.run(N, J, k, collect=True)[2]
        out[J] = (N, extremals, time.time() - t0)
    return out


# ------------------------------------- arm 3: the product family at k

def product_least_degree(prods, J, k):
    """(least degree, multiset) over |D| >= J with product height <= k."""
    bd, bw = None, None
    for (c, s), H in prods.best.items():
        if c >= J and H <= k and (bd is None or s < bd):
            bd, bw = s, prods.wit[(c, s)]
    return bd, bw


def as_product(vec, prods):
    """The multiset whose pure product is +-vec or +-its reversal, or
    None. Extremality is a statement about the POLYNOMIAL, and
    x^N P(1/x) is the same polynomial read backwards, so both
    orientations count. The table keeps one witness per (count, sum), so
    this tests membership in THAT set of witnesses and not in the whole
    product family -- which is why a miss is reported and never read as
    'no product attains it'."""
    def poly(D):
        p = [1]
        for d in D:
            p = mul_shift(p, d)
        return p
    rev = list(reversed(vec))
    cands = [list(vec), [-c for c in vec], rev, [-c for c in rev]]
    for (_c, s), D in prods.wit.items():
        if s != len(vec) - 1:
            continue
        p = poly(D)
        for cand in cands:
            if p == cand:
                return D
    return None


# ---------------------------------------- arm 4: the cyclotomic floor

def _primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, s in enumerate(sieve) if s]


_PRIMES = _primes(2000)


def forced_degree(N, J, k):
    """Sum of phi(p^e) over the prime powers whose cyclotomic MUST
    divide any height-<=k multiple of (x-1)^J of degree <= N (hand
    attack, fifth section). The prime loop stops where even e = 1 cannot
    be forced, phi(p) = p-1 being increasing in p."""
    tot = 0
    LN = log(k * (N + 1))
    for p in _PRIMES:
        if (p - 1) * LN >= J * log(p):
            if p > 2:
                break
            continue
        e = 1
        while True:
            phi = (p - 1) * p ** (e - 1)
            if phi * LN < J * log(p):
                tot += phi
                e += 1
            else:
                break
    return tot


def cyclotomic_floor(J, k):
    """The least N consistent with the forced divisions -- a lower bound
    on d_k(J) at every J and k, at no compute."""
    N = J
    while J + forced_degree(N, J, k) > N:
        N += 1
    return N


# ------------------------------------------------------- the controls

def brute_predicate(N, J, k):
    """Full enumeration over [-k,k]^(N+1), sharing nothing with arm 1 --
    it divides by (x-1) J times by running sums and checks the remainder,
    rather than pruning anything."""
    from itertools import product as iproduct
    for vec in iproduct(range(-k, k + 1), repeat=N + 1):
        if not any(vec):
            continue
        p = list(vec)
        ok = True
        for _ in range(J):
            s, q = 0, []
            for c in p:
                s -= c
                q.append(s)
            if q[-1] != 0:
                ok = False
                break
            p = q[:-1]
        if ok:
            return True
    return False


def main():
    t_all = time.time()
    route = Route()
    fired = dict(("K-" + c, 0) for c in "ABCDE")

    print("=" * 70)
    print("explore_flatten_d2.py -- d_2(J), and product extremality at height 2")
    print("=" * 70)

    print("\n[arm 3] product table to degree %d" % PRODUCT_BUDGET)
    t0 = time.time()
    prods = Products(PRODUCT_BUDGET)
    print("   %d (count, sum) keys, %.1f s" % (len(prods.best), time.time() - t0))

    print("\n[C1] parity: height-domain route vs FULL brute force")
    accept, reject = 0, 0
    for N in range(1, 8):
        for J in range(1, N + 1):
            for k in (1, 2, 3):
                if (2 * k + 1) ** (N + 1) > 3000000:
                    continue
                a = route.run(N, J, k)[0]
                b = brute_predicate(N, J, k)
                if a != b:
                    fired["K-B"] += 1
                    print("   K-B N=%d J=%d k=%d route=%s brute=%s"
                          % (N, J, k, a, b))
                if b:
                    accept += 1
                else:
                    reject += 1
    print("   %d predicates compared -- %d ACCEPT, %d REJECT -- %d mismatches"
          % (accept + reject, accept, reject, fired["K-B"]))

    print("\n[C2] independent algorithm: height domain vs quotient route")
    cases, capped = 0, 0
    for k in (1, 2, 3):                  # k, J, M -- the inner loop then
        for J in range(1, 13):           # moves only the DEGREE, so the
            for M in range(max(4, J + 1), 14):   # backward set changes at
                                         # most once per suffix length and
                                         # never per cell
                a = route.run(M - 1, J, k)[0]
                try:
                    b = feasible(M, J, k, NODE_CAP)
                except NodeCap:
                    capped += 1
                    continue
                cases += 1
                if a != b:
                    fired["K-B"] += 1
                    print("   K-B M=%d J=%d k=%d height=%s quotient=%s"
                          % (M, J, k, a, b))
    print("   %d predicates compared (%d skipped on the node cap), %d mismatches"
          % (cases, capped, fired["K-B"]))

    print("\n[C4] rank-1 tail against C(M-1, floor((M-1)/2)), M <= 7")
    tail_cases = 0
    for M in range(2, 8):
        J = M - 1
        want = comb(M - 1, (M - 1) // 2)
        k = 1
        while not route.run(M - 1, J, k)[0]:
            k += 1
        tail_cases += 1
        if k != want:
            fired["K-E"] += 1
            print("   K-E M=%d h=%d closed form=%d" % (M, k, want))
    print("   %d cases, %d mismatches" % (tail_cases, fired["K-E"]))

    print("\n[C3, arm 2] the k = 1 ladder against A059753")
    lad1 = ladder(route, 1, LADDER_K1, enum_to=ENUM_K1_J)
    for J in range(1, LADDER_K1 + 1):
        d, ex, secs = lad1[J]
        if d != A059753[J - 1]:
            fired["K-C"] += 1
            print("   K-C J=%d ladder=%d A059753=%d" % (J, d, A059753[J - 1]))
        note = "" if ex is None else "  extremals=%d" % len(ex)
        print("   J=%2d  d_1=%3d  A059753=%3d%s  (%.1f s)"
              % (J, d, A059753[J - 1], note, secs))

    print("\n[arm 2] the k = 2 ladder -- d_2(J)")
    lad2 = ladder(route, 2, LADDER_K2, enum_to=ENUM_K2_J)
    for J in range(1, LADDER_K2 + 1):
        d, ex, secs = lad2[J]
        pd, pw = product_least_degree(prods, J, 2)
        if pd is not None and d < pd:
            fired["K-A"] += 1
            print("   K-A J=%d ladder=%d product=%d %s" % (J, d, pd, pw))
        note = ""
        if ex is not None:
            pure = [v for v in ex if as_product(v, prods) is not None]
            note = "  extremals=%d pure=%d" % (len(ex), len(pure))
        print("   J=%2d  d_2=%3d  product=%s %-20s C(J,2)+1=%3d%s  (%.1f s)"
              % (J, d, pd, str(pw), J * (J - 1) // 2 + 1, note, secs))

    print("\n[arm 4] the cyclotomic floor, k = 1..9, J = 1..15")
    floor = {}
    for k in range(1, 10):
        row = [cyclotomic_floor(J, k) for J in range(1, 16)]
        for J in range(1, 16):
            floor[(k, J)] = row[J - 1]
        print("   k=%d  %s" % (k, row))

    print("\n[C5] floor soundness against every established d_k")
    checks, strict = 0, 0
    for J in range(1, 15):
        pairs = [(1, A059753[J - 1])]
        if J <= LADDER_K2:
            pairs.append((2, lad2[J][0]))
        for k, known in pairs:
            checks += 1
            f = floor[(k, J)]
            if f > known:
                fired["K-D"] += 1
                print("   K-D k=%d J=%d floor=%d exhibited=%d"
                      % (k, J, f, known))
            elif f < known:
                strict += 1
    print("   %d checks, %d strictly below, %d unsound"
          % (checks, strict, fired["K-D"]))

    print("\n[arm 5] the sweep -- h(M, J), M = 4..%d, J = 2..%d"
          % (SWEEP_M, SWEEP_J))
    d2 = dict((J, lad2[J][0]) for J in lad2)
    decided, bracketed, by = 0, 0, {}
    widest = None
    trivial = 0
    for M in range(4, SWEEP_M + 1):
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            ceil_h, _ = prods.bound(M, J)
            if ceil_h is None:
                continue
            # the two ladders are CEILINGS as well as floors: M > d_k(J)
            # exhibits a height-k vector whether or not a product does.
            if J <= len(A059753) and M > A059753[J - 1]:
                ceil_h = min(ceil_h, 1)
            if J in d2 and M > d2[J]:
                ceil_h = min(ceil_h, 2)
            if ceil_h == 1:
                trivial += 1
                decided += 1
                by["h=1 trivially"] = by.get("h=1 trivially", 0) + 1
                continue
            lo, why = 1, None
            for k in range(1, ceil_h):
                w = None
                if k == 1 and J <= len(A059753) and M <= A059753[J - 1]:
                    w = "A059753 (cited)"
                elif k == 2 and J in d2 and M <= d2[J]:
                    w = "the d_2 ladder"
                elif M <= floor.get((k, J), 0):
                    w = "the cyclotomic floor"
                else:
                    # the quotient route answers in BOTH directions and
                    # its True is a ceiling: every height below k has
                    # already been refuted, so a witness at k IS h.
                    try:
                        if feasible(M, J, k, NODE_CAP):
                            ceil_h, why = k, "the quotient route"
                            break
                        w = "the quotient route"
                    except NodeCap:
                        pass
                if w is None:
                    break
                lo, why = k + 1, w
            if lo >= ceil_h:
                decided += 1
                key = why or "h=1 trivially"
                by[key] = by.get(key, 0) + 1
            else:
                bracketed += 1
                if widest is None or ceil_h - lo > widest[0]:
                    widest = (ceil_h - lo, M, J, lo, ceil_h)
    print("   %d decided (%d of them trivially at h = 1), %d bracketed"
          % (decided, trivial, bracketed))
    for key, n in sorted(by.items(), key=lambda kv: -kv[1]):
        print("      %-24s %d" % (key, n))
    if widest:
        print("   widest bracket [%d, %d] at M = %d, J = %d"
              % (widest[3], widest[4], widest[1], widest[2]))

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
