"""
explore_premium.py -- THE DOOR-OPENING PREMIUM (sibling of
explore_headroom.py, explore_slack_machine.py, explore_growth_laws.py,
explore_phoenix_bill.py).

THE QUESTION. A state of the growing tower is a positive integer N, a move
is a multiplication N -> N*m, and the transparency headroom

    V(N) = W(lambda(N)) / N,   W(L) = the largest modulus whose lambda | L,

splits every move into what it SPENDS and what it OPENS:

    V(Nm) = ( V(N) / gcd(m, V(N)) ) * G'(N, m),   G' a positive integer

(the headroom ledger, explore_headroom.py finding 2). The SPENDING side is
finished: gcd(m, V) is truncated subtraction on V's exponents, the slack
machine's lossy law wearing the observer's clothes. THE OPENING SIDE, G',
IS UNEXAMINED -- and it is where every rise in headroom comes from, since
V rises exactly when G' > gcd(m, V). This file asks what G' IS.

The shape of the answer was visible before any code. A move opens a door
when it admits a prime p to the wall, and the doors of a state are a
function of lambda alone -- p is at the wall iff (p-1) | lambda -- so G'
should be readable off lambda and the move, with N appearing nowhere. That
matters beyond bookkeeping: THE PROBE READS V, NOT LAMBDA. If the premium
is a function of lambda, a sighted probe cannot compute its own next
reading, and the congruence failure already measured (85.9% of
lambda-moving moves split a blind class) stops being a statistic and
becomes a mechanism.

THE OBJECTS. For a prime p write v_p for the p-adic valuation. The DOORS
of L are Doors(L) = { p prime : (p-1) | L }, and

    W(L) = (2 if L odd else 2^(v_2(L)+2)) * prod{ p^(v_p(L)+1)
             : p odd, p in Doors(L) },

W's 2-part being 2 for ODD L and 2^(v_2(L)+2) for even because lambda(2^a)
is 1, 2, then 2^(a-2); L = 1 is the state the tower starts from, so the odd
case is not a corner. Two derived objects carry the file. THE WALL GAIN of
a move is G = W(lambda(Nm)) / W(lambda(N)), a positive integer because
lambda(N) | lambda(Nm) and W is monotone in divisibility. THE UNPAID PART
is P = m / gcd(m, V(N)), the factor of the move that transparency does not
cover. And for a move that imports a prime q not already in N, THE COHORT

    C(L, q^e) = Doors(lcm(L, q^(e-1)(q-1))) \\ Doors(L)

is the set of primes the move admits to the wall for the first time.

THE DESIGN, in nine sections (S8 and S9 were added mid-run; see their headers). The
slate is frozen before any engine code;
where a run contradicts it the framing is left standing and flagged rather
than quietly rewritten.

WHOSE VOCABULARY. The suspicion is written in the OBSERVER's terms --
doors, percept, blindness -- while the object it dissects, G', was minted
on the ledger's terms. That is deliberate: the ledger named G' and did not
ask what it was, and the reason to ask is an observer's reason. THE
TRANSPLANT TO MARK: the spending half is truncated subtraction DOWNWARD on
V's exponents, and section 4 predicts the opening half is truncated
subtraction UPWARD on lambda's. That intuition is imported wholesale from
the neighbouring half of the same ledger and is flagged as such, even
though lcm = max makes it look forced.

S1 POSITIVE CONTROL, run before any verdict is read. wall() against its own
   DEFINITION -- the largest modulus found by brute search -- compared only
   where the wall fits under the search cap, since a truncated search
   reports the formula wrong for every large wall. Then the three witnesses
   the ledger froze must come back unchanged: (N, m) = (16, 2) prints
   G' = 1 with V unchanged at 15 and lambda 4 -> 8; (N, m) = (3, 16) prints
   V 8 -> 5; and N = 10, N = 11 share the headroom 24 and one push of 5
   sends them to 264 and 240. A rig that cannot reproduce those is not
   measuring the same G'.

S2 THE PREMIUM IDENTITY. Unfolding both headrooms in G' = V(Nm)*gcd/V(N)
   cancels N outright: V(Nm)/V(N) = W(lambda(Nm)) * N / (Nm * W(lambda(N))),
   so for EVERY N and m,

       G'(N, m) = G / P,   G = wall gain,  P = unpaid part.

   The ledger theorem (G' a positive integer) is then exactly the statement
   P | G: the wall's gain covers whatever the move failed to pay out of V.
   PREDICTION S2: G' = G/P with 0 mismatches over the battery; G and P are
   positive integers and P | G in every case, 0 exceptions.

S3 THE CLOSED FORM ON A FRESH IMPORT. Let q not divide N, m = q^e, and
   L = lambda(N). Then lambda(Nq^e) = lcm(L, M) with M = q^(e-1)(q-1),
   and v_q(V(N)) = (v_q(L)+1) if q's door is OPEN at L -- (q-1) | L -- and
   0 if it is shut, since q does not divide N. Both factors of G/P are
   therefore functions of L and q^e with no other reference to N:

       G' = W(lcm(L, M)) / ( W(L) * q^(e - a) ),
       a = min(e, v_q(L)+1) if (q-1) | L, else 0.

   If that holds, HEADROOM'S ASCENT IS A FUNCTION OF LAMBDA -- and the
   probe reads V. The scope is the load-bearing part and is attacked here
   rather than assumed: for a REPEAT push lambda(Nm) needs the exponents of
   N, not just lambda(N), and the hand-attack found the witness before the
   engine ran -- lambda(3) = lambda(8) = 2, and m = 3 is a repeat for 3 and
   fresh for 8.
   PREDICTION S3a: the closed form matches the definitional G' for every
   fresh import in the battery, 0 exceptions; any two battery states
   sharing a lambda give the same G' under the same fresh q^e, 0
   exceptions.
   PREDICTION S3b: lambda-sufficiency FAILS once repeats are admitted, and
   the frozen witness prints G'(3, 3) = 7 against G'(8, 3) = 1.

S4 NEW DOORS TIMES BUMPS. The gain should factor into the cohort and the
   exponent bumps at doors already open, with the truncated subtraction
   marked above:

       G' = 2^(eps(L') - eps(L))
            * prod{ p^(v_p(L')+1) : p odd in C }
            * prod{ p^(max(0, v_p(M) - v_p(L))) : p odd, door open at L }
            / P,       L' = lcm(L, M).

   PREDICTION S4: the three-factor product equals the definitional G' for
   every fresh import in the battery, 0 exceptions, and
   v_p(L') - v_p(L) = max(0, v_p(M) - v_p(L)) at every prime.

S5 THE SILENT IMPORT. The margin to distrust, killed on paper before the
   engine: "a fresh import with G' = 1 means the door was already open" is
   FALSE. An open door gives G' = 1 for a trivial reason -- L' = L, nothing
   opens, and q | V so the move is transparent -- but a SHUT door can also
   give G' = 1, when the move admits q alone and bumps nothing. L = 2 and
   q = 11: lcm(2, 10) = 10, the rising prime is 5 whose door needs 4 | 10
   and stays shut, so W goes 24 -> 264 = 11*24 and the import pays for
   itself exactly. Such a move changes lambda while leaving V UNCHANGED --
   invisible to the probe, and not transparent.
   PREDICTION S5: G' = 1 on a fresh single prime iff the wall gain is
   exactly q, iff the cohort is {q} with v_q(L) = 0 and no bumps; the pair
   (L, q) = (2, 11) prints G' = 1 with a SHUT door and cohort {11}; every
   open-door fresh single import prints G' = 1 with V(Nq) = V(N)/q, 0
   exceptions; and no battery case has G' = 1 with a shut door and a
   cohort other than {q}.

S6 WHICH PRIMES ARE GATEWAYS. Some q open a large cohort, some open only
   themselves. From the empty state L = 1, Doors(1) = {2}, so the cohort is
   { p prime : (p-1) | (q-1) } minus the 2 -- gatewayhood is a DIVISOR
   statement about q-1 and nothing else. The safe primes are the minimal
   gateways: for q = 2r+1 with r an odd prime the divisors of q-1 above 1
   are 2, r, 2r, giving 3, the even r+1, and q itself, so the cohort is
   exactly {3, q}.
   PREDICTION S6: |C(1, q)| = #{ d | q-1 : d >= 2, d+1 prime } with 0
   exceptions; every safe prime q = 2r+1 with r >= 5 has cohort exactly
   {3, q}. THE RANKING is measured, not predicted, by Spearman correlation
   of |C(1,q)| against the divisor count of q-1, against the largest prime
   factor of q-1, and against q itself -- with the frozen expectation that
   the divisor count beats both.

S7 THE STITCH, AND WHAT THE PROBE CANNOT DO. Two claims, one object.
   (a) The phoenix opens exactly { p : (p-1) | 2^t D } at frozen depths
   (the spectrum law, explore_phoenix_bill.py) -- which is Doors(lambda)
   evaluated
   along a determined trajectory, while the cohort is Doors(lambda)
   DIFFERENCED along an arbitrary move. If they are one relation the
   spectrum law is the premium's integral, and the depth v_p(D)+1 the
   spectrum law quotes is W's own exponent v_p(L)+1, which is the slack
   delta_p. Along L = 2^t from seed 1 the windows are the Fermat primes.
   (b) lambda(N1) = lambda(N2) forces W equal, so V equal forces N equal:
   THE PROBE IS INJECTIVE ON A LAMBDA-FIBRE, and every blind class is a set
   of states with pairwise DISTINCT lambda. Blindness is entirely a
   cross-lambda phenomenon. For an equal-headroom pair, gcd(q, V) agrees,
   so a fresh import splits the pair exactly when the two PREMIUMS differ:
   the door-opening premium IS the information the probe gains.
   PREDICTION S7a: along L = 2^t the cohort of the step 2^t -> 2^(t+1) is
   {2^(t+1)+1} when that is prime and empty otherwise, nonempty exactly at
   t+1 in {1, 2, 4, 8, 16} for t < 17.
   PREDICTION S7b: every non-singleton headroom class below the pool cap has
   pairwise distinct lambda, 0 exceptions; and a printed equal-headroom
   pair is split by a FRESH import. THE SILENCE SETS -- which fresh primes
   preserve a given blind pair -- are measured, not predicted.

S8 THE PREMIUM ON A REPEAT PUSH (added to the design after section 3
   printed, and frozen from a hand derivation before its engine was
   written; section 3's scope line is what provoked it). Section 3 leaves
   repeats outside, and the reason is exactly one number. For any prime l
   with c = v_l(N), the l-part of N*l^e is l^(c+e) and every other part is
   untouched, so lambda(N*l^e) = lcm(lambda(N), lambda(l^(c+e))) -- and c
   is not free, since v_l(V) = v_l(W(L)) - c gives c = v_l(W(L)) - v_l(V).
   So

       G' = W( lcm(L, lambda(l^(c+e))) )
            / ( W(L) * l^(e - min(e, v_l(V))) ),   c = v_l(W(L)) - v_l(V),

   for EVERY prime-power move, fresh or repeat: the premium depends on the
   state only through its lambda and a SINGLE COORDINATE of the probe's
   percept. Section 3 is the c = 0 case. The frozen repeat witness is then
   not a mystery but an arithmetic: V(3) = 8 and V(8) = 3 have v_3 equal to
   0 and 1, so the two states sit at different depths in 3 and the premiums
   must differ.
   PREDICTION S8a: the general closed form matches the definitional G' on
   every prime-power move in the battery, repeats included, 0 exceptions.
   PREDICTION S8b: two states sharing lambda AND v_l(V) give the same
   premium under l^e, 0 exceptions; the battery holds pairs sharing lambda
   but not v_l(V) that disagree, and the frozen witness (3, 8) under m = 3
   is one of them.

S9 WHAT THE SILENT SET IS (added to the design after section 5 printed,
   and frozen from a hand derivation before its engine was written; the
   question it answers was going to be deferred until the
   derivation ran). Section 5 leaves the silent set as a list. Unfold it.
   A fresh q is silent at L iff the wall gain is exactly q, that is

       W(lcm(L, q-1)) = q * W(L),

   and if L divides q-1 the lcm collapses to q-1, so the condition reads
   W(q-1) = q*W(L) -- which, divided by q, is V(q) = W(L). SILENCE AND
   BLINDNESS ARE THE SAME CONDITION: the primes silent at L (those with
   L | q-1) are exactly the members of the probe's blind class V = W(L).
   At L = 2 the restriction is vacuous, since q-1 is even for every odd
   prime, so the ENTIRE silent set at L = 2 is the class V = W(2) = 24 --
   the family findings 6 and 8 already named twice, arrived at a third
   way. The algebra is one line once both definitions are unfolded and a
   reader who says "both sides are W(q-1) = q*W(L)" is right; what the
   unfolding buys is the identification, and its consequence is a
   roadmap-level NEGATIVE stated in this section's finding.
   PREDICTION S9a: for every L in the sweep and every fresh prime q < 30000
   with L | q-1, q is silent at L iff V(q) = W(L), 0 exceptions.
   PREDICTION S9b: the silent set at L = 2 above 5 equals the set of
   primes with V(q) = 24 exactly, 0 discrepancy.

WHAT WOULD KILL WHAT (observables, not inferences). S2 dies on one printed
move with G' != G/P, or with P not dividing G. S3a dies on one printed fresh
import where the closed form disagrees with the definitional G', or on one
printed pair of equal-lambda states disagreeing under the same fresh move.
S3b dies if the frozen pair prints equal premiums -- which would say
lambda-sufficiency is wider than the section claims, not narrower. S4 dies
on one printed fresh import where the three-factor product disagrees. S5
dies if (2, 11) prints anything but G' = 1 with a shut door, or if some
battery case prints G' = 1 with a shut door and a cohort other than {q}. S6
dies on one printed q whose cohort size differs from the divisor count, or
on one printed safe prime with a cohort other than {3, q}. S7a dies on one
printed t with a cohort that is neither the Fermat prime nor empty. S7b dies
on one printed non-singleton class containing two states with equal lambda. S8a
dies on one printed prime-power move where the general form disagrees.
S8b dies on one printed pair sharing lambda and v_l(V) whose premiums
differ. S9a dies on one printed silent q with L | q-1 and V(q) != W(L), or
one printed q with V(q) = W(L) that is not silent. S9b dies on one prime
in either set and not the other.

FINDINGS.

1. THE PREMIUM IDENTITY (theorem, proved for all N and m; verified
   23084/23084 moves, N in 2..399 and m in 2..59). Unfolding both
   headrooms cancels the state outright:

       G'(N, m) = (wall gain) / (unpaid part)
                = [ W(lambda(Nm)) / W(lambda(N)) ] / [ m / gcd(m, V(N)) ].

   So the ledger's two halves are not two mechanisms but one quotient: the
   move buys a wall gain and pays for whatever part of itself transparency
   does not cover, and the theorem that G' is a positive integer is exactly
   the statement that THE UNPAID PART DIVIDES THE GAIN (0 exceptions). The
   spending half was already known to be truncated subtraction; what this
   adds is that the opening half is not a residual but a ratio of two
   objects the state already carries.

2. THE CLOSED FORM ON A FRESH IMPORT (theorem, proved for every N and every
   prime power q^e with q not dividing N; verified 18291/18291). Both
   factors lose their N. Since q does not divide N, lambda(Nq^e) =
   lcm(lambda(N), lambda(q^e)) and v_q(V(N)) = v_q(W(lambda(N))), so with
   L = lambda(N),

       G' = W(lcm(L, lambda(q^e))) / ( W(L) * q^(e - min(e, v_q(W(L)))) ).

   HEADROOM'S ASCENT IS A FUNCTION OF LAMBDA. Nothing about the state
   survives into it but its lambda, and lambda is precisely what a probe
   reading V does not have -- finding 8 is what that costs the probe.
   THE FROZEN FORM WAS WRONG AND THE RIG PRINTS ITS OWN KILL: section 3
   wrote lambda(q^e) as q^(e-1)(q-1) and v_q(W(L)) as v_q(L)+1, which is
   the ODD-prime branch of each, and it fails on 85 of the 18291 fresh
   imports -- at q = 2 and nowhere else, since lambda(2^e) runs 1, 2,
   2^(e-2) and the wall's 2-part is 2^(v_2(L)+2). First failure N = 3,
   q = 2, e = 3: the frozen form says 5, the truth is 1, because
   lambda(8) = 2 rather than 4. The repair is not a patch but a
   UNIFORMISATION -- write the move's own lambda for the lcm and the wall's
   own exponent for the payment and both branches disappear -- and the
   frozen expression is kept in the engine behind a flag so the failure is
   printed rather than corrected out of sight. The lesson is the prediction's
   own: the hand derivation was written in the vocabulary of odd primes
   and carried to 2 without a second thought, which is the marked
   transplant one level down from where the design marked it.

3. NEW DOORS TIMES BUMPS (theorem; verified 18291/18291). The gain factors
   into the cohort and the exponent bumps at doors already open, with
   L' = lcm(L, lambda(q^e)):

       G' = 2^(eps(L') - eps(L))
            * prod{ p^(v_p(L')+1) : p odd, p newly at the wall }
            * prod{ p^(v_p(L') - v_p(L)) : p odd, door already open }
            / q^(e - min(e, v_q(W(L)))),

   and every bump exponent is max(0, v_p(lambda(q^e)) - v_p(L)) at every
   prime, 0 exceptions. So the marked transplant was RIGHT ABOUT THE
   BUMPS and only about them: the bump factor is truncated subtraction
   upward on lambda's exponents where the spending half is downward on
   V's. The COHORT factor has no counterpart on the spending side at all,
   and that asymmetry is the content rather than a blemish -- spending is
   pure truncated subtraction, opening is truncated subtraction PLUS a
   term for the doors that were not there before, and that extra term is
   the whole reason V can rise. Worked row: from
   lambda = 10, importing 7 opens the cohort {7, 31}, carries lambda to 30
   and the wall from 264 to 171864, and pays 7 for a premium of 93.

4. LAMBDA ALONE IS GUARANTEED ONLY ON THE FRESH IMPORTS (rule, proved
   one way and killed the other by a witness frozen before the run; the
   guarantee is WIDER than this file's battery can see -- it holds on every
   move COPRIME to the state, of which a fresh prime power is the one-prime
   case, per explore_composite_move.py). Over the
   battery's 59 lambda classes holding two or more states, 13281
   same-lambda comparisons under the same fresh move give 0 disagreements.
   It fails on the first repeat push: lambda(3) = lambda(8) = 2, and m = 3
   is a repeat at N = 3 and a fresh import at N = 8 -- lambda goes 2 -> 6
   in the first and stands still in the second, and the premiums are 7 and
   1. The reason is exact: for a repeat push lambda(Nm) needs the EXPONENTS
   of N, which lambda(N) does not carry. The scope word is ONLY and never
   EXACTLY: on repeats lambda usually still happens to determine the
   premium -- 226 of the 312 (lambda, l, e) cells holding two or more
   repeat states agree anyway, and the 86 that disagree are simply what
   the theorem cannot cover. That is the whole of the gap, and finding 9
   closes it with one further number.

5. THE SILENT IMPORT (rule, proved + verified; the counterexample was found
   on paper before the engine ran). A fresh single prime with G' = 1 does
   NOT mean its door was open. Behind an OPEN door the premium is 1 for a
   trivial reason -- lambda does not move, nothing opens, and q | V, so the
   move is transparent and V(Nq) = V(N)/q (1103/1103). Behind a SHUT door
   G' = 1 says the wall gain is exactly q, which happens iff the cohort is
   {q} alone with v_q(L) = 0 and no bumps anywhere -- 436 of the battery's
   4994 shut-door single imports pay G' = 1, and every one of the 436 has
   that cohort. Witness: L = 2, q = 11, where lcm(2, 10) = 10 raises
   v_5 from 0 to 1 but 5's own door needs 4 | 10 and stays shut, so the
   wall goes 24 -> 264 = 11*24 and the import pays for itself exactly.
   SUCH A MOVE CHANGES LAMBDA AND LEAVES V UNTOUCHED: it is invisible to
   the probe without being transparent, a third category beside the two the
   ledger had (N = 3 under 11, 23, 47 and 59 all hold V at 8). The family
   is not the safe primes wearing a new name: 342 of the 436 import a safe
   prime and 94 do not. And it is EMPTY AT AN ODD LAMBDA (0 exceptions,
   proved): an odd L carries a wall 2-part of 2, a fresh odd q makes
   lcm(L, q-1) even, and the 2-part jumps to 2^(v_2(q-1)+2) >= 8, so the
   premium is at least 4. Since lambda is even from N = 3 up, the silent
   set is a phenomenon of every state except the two the tower starts
   from.

6. GATEWAYHOOD IS A DIVISOR STATEMENT ABOUT q-1 (theorem at L = 1;
   verified 302/302 primes below 2000; the ranking measured). From the
   empty state Doors(1) = {2}, so the cohort of a fresh q is
   { p prime : (p-1) | (q-1) } minus the 2, and

       |C(1, q)| = #{ d | q-1 : d >= 2, d+1 prime }

   exactly. The FLOOR is the single prime 3, which opens only itself; for
   every other q the minimum is a cohort of two, {3, q}, and 47 primes
   below 2000 attain it. The SAFE PRIMES are one sub-family of those and
   not the whole of them: for q = 2r+1 with r an odd prime >= 5 the
   divisors of q-1 above 1 are 2, r and 2r, giving 3, the even r+1 and q
   itself (35/35 below 2000). Of the 47, 37 are safe primes -- those 35
   plus 5 and 7, which are safe (r = 2 and 3) and are exactly the two the
   argument's r >= 5 excludes -- and 10 are not safe at all, led by 239,
   443 and 647. THE MINIMUM-GATEWAY PRIMES ABOVE 5 WITH 3 NOT DIVIDING
   q-1 ARE THE LARGEST BLIND CLASS, exactly and not merely by
   containment: for q > 5 a cohort of
   {3, q} forces v_2(q-1) = 1, since v_2 >= 2 would seat 5 as a third door,
   so W(q-1) = 2^3 * 3^(v_3(q-1)+1) * q and V(q) = 24 * 3^v_3(q-1). Hence
   { q > 5 : cohort {3, q} and 3 does not divide q-1 } = { q > 5 : V(q) =
   24 }, 45 primes below 2000 with 0 discrepancy -- and 7 sits outside for
   the reason the equality names, 3 | 6 giving V(7) = 72. The blind class
   filed as "contains every safe prime" is better described as the
   minimum-gateway family, of which the safe primes are a part.
   Cohort sizes below 2000 run 1 to 16 with mean 5.09, the largest
   at q = 1801 and q = 1621. The ranking is what the shape predicts and the
   correlations separate cleanly: Spearman against the divisor count of q-1
   is +0.941, against the LARGEST PRIME FACTOR of q-1 it is -0.580, and
   against q itself only +0.132. Both halves of smoothness show, in
   opposite signs, and size barely registers -- a gateway is a prime whose
   predecessor has many small factors, and nothing else.

7. THE SPECTRUM LAW IS THE PREMIUM'S INTEGRAL (rule; verified on the
   Fermat ladder, t <= 17). The phoenix opens { p : (p-1) | 2^t D } at
   frozen depths; the cohort is Doors(lambda) DIFFERENCED along a move.
   They are one functional evaluated and differentiated -- so the rudder's
   window set and the headroom premium are the same object, and the DEPTH
   the spectrum law quotes, v_p(D)+1, is W's own exponent v_p(L)+1, which
   is the slack delta_p -- at an OPEN door, which is what a window is, so
   the branch finding 9 has to separate does not arise here. One relation
   read three ways: a window set, a wall exponent, a machine counter. Along L = 2^t from the seed the cohort of
   the step 2^t -> 2^(t+1) is the Fermat prime 2^(t+1)+1 when that is prime
   and EMPTY otherwise -- nonempty at exactly 5 of the first 17 steps,
   opening 3, 5, 17, 257 and 65537, each at wall exponent 1.

8. THE PROBE IS INJECTIVE ON A LAMBDA-FIBRE, AND THE PREMIUM IS EXACTLY
   WHAT IT LEARNS (theorem + measurement over N <= 6000). V = W(lambda)/N,
   so equal lambda forces equal wall and equal V then forces equal N:
   TWO DISTINCT STATES WITH THE SAME READING MUST HAVE DIFFERENT LAMBDA.
   Blindness is entirely a cross-lambda phenomenon -- all 271 non-singleton
   headroom classes below 6000, covering 2128 states, have pairwise
   distinct lambda, 0 exceptions. And for an equal-headroom pair gcd(q, V)
   agrees, so a fresh import splits the pair exactly when the two PREMIUMS
   differ: the door-opening premium IS the information the probe gains.
   THE PROBE CANNOT COMPUTE ITS OWN NEXT READING, and the argument is the
   witness rather than finding 2 -- a quantity being a function of lambda
   would not by itself stop it from ALSO being a function of V, and only
   an exhibited disagreement does. At the tombstones: N = 2 and N = 24
   both read V = 1 with lambda 1 and 2, and a fresh 5 pays premiums 24 and
   2, sending them to 24 and 2. So V(Nq) is not a function of (V(N), q),
   and the congruence failure has a mechanism under it rather than a rate.
   SILENCE SETS are sparse and structured: over ONE representative pair
   per class -- the two smallest members of each of the 271 -- 688
   silences are doors already open at both states, 309 carry a premium
   above 1 that happens to agree, and 168 are the admitted-alone imports of
   finding 5, of which 136 import a SAFE prime. So the minimum-gateway
   family of finding 6 supplies the commonest silencers of finding 5, and
   the family that IS the largest blind class is the family that keeps
   blind classes blind.

9. THE PREMIUM OF ANY PRIME-POWER MOVE IS LAMBDA PLUS ONE EXPONENT
   (theorem, proved for all N and all prime powers; verified 20298/20298
   moves, 2007 of them repeats). Multiplying by l^e carries the l-part of
   N from l^c to l^(c+e) and touches nothing else, so lambda(N*l^e) =
   lcm(lambda(N), lambda(l^(c+e))); and c is not an independent quantity,
   since v_l(V) = v_l(W(L)) - c. Hence

       G' = W( lcm(L, lambda(l^(c+e))) ) / ( W(L) * l^(e - min(e, v_l(V))) ),
       c = v_l(W(L)) - v_l(V),

   for every prime-power move, fresh or repeat, with finding 2 the c = 0
   case. THE STATE ENTERS THROUGH ITS LAMBDA AND A SINGLE COORDINATE OF
   THE PROBE'S PERCEPT -- not the whole percept, and nothing else about N.
   The prediction has teeth rather than being a re-parametrisation: 14544
   of the 20298 moves land on a (lambda, v_l(V), l, e) key another move
   already held, across 5754 distinct keys, and 0 keys carry two premiums.
   So the ledger closes on both sides for prime-power moves, and the
   coordinate that was missing is v_l(V) -- which is the slack machine's
   register entry at l EXACTLY WHEN l's door is open, and 0 below a
   strictly positive slack when it is shut (the two branches of the
   exponent identity, explore_headroom.py finding 1). The premium is a
   function of V's exponent, not of the slack; the two agree wherever the
   machine actually computes, since a seated l has its door open.
   The frozen repeat witness stops being a witness and
   becomes an arithmetic: V(3) = 8 and V(8) = 3 have v_3 equal to 0 and 1,
   so 3 sits at depth 1 in the prime 3 and 8 at depth 0, and premiums of 7
   and 1 are forced.

10. SILENCE IS BLINDNESS (theorem, proved; verified over eight lambda and
   every prime below 30000, 0 disagreements). Unfolding section 5's
   condition: q is silent at L iff W(lcm(L, q-1)) = q*W(L), and when
   L | q-1 the lcm collapses to q-1, leaving W(q-1) = q*W(L), which
   divided by q is V(q) = W(L). So

       for L | q-1,  q is SILENT at L  <=>  V(q) = W(L),

   and THE PRIMES SILENT AT L ARE THE MEMBERS OF THE PROBE'S BLIND CLASS
   V = W(L). At L = 2 the restriction is vacuous, q-1 being even for every
   odd prime, so the ENTIRE silent set at L = 2 is the class V = 24 -- 400
   primes below 30000, 0 discrepancy. That family has now been reached
   three independent ways: as the minimum gateways (finding 6), as the
   commonest silencers of blind pairs (finding 8), and as the silent set
   at the tower's first even lambda. As algebra it is one line and a
   reader who says "both sides are W(q-1) = q*W(L)" is right; what the
   unfolding buys is that the two questions are ONE question.
   THE CONSEQUENCE IS A NEGATIVE, and it is the useful part. "Is the
   silent set at L infinite" IS "is the blind class V = W(L) infinite".
   At L = 2 that is the class whose one identified route runs through the
   safe primes -- the Sophie Germain question (explore_headroom.py finding
   7; since settled without it -- explore_blind_spot_infinite.py proves
   that class infinite, so the silent set at L = 2 is infinite too). So
   the silent set is not a way AROUND the conjecture ceiling that
   the blind-class question hits; it is the same wall approached from the
   other side, and work spent hunting non-safe silent primes at
   L = 2 would have been work spent hunting non-safe members of
   V = 24 without knowing it. The permanent-blindness question survives
   only where a blind class is already known infinite, which by
   explore_headroom.py finding 5 means the tombstones, V = 1.

SCOPE. Everything is exact integer arithmetic. Ranges differ by section and
each print carries its own: the move battery is N in 2..399 with m in
2..59, the fresh-import battery adds exponents e = 1..3 over primes q < 60,
the gateway sweep runs over primes q < 2000 at L = 1, the Fermat ladder
covers L = 2^t for t <= 17, the blind-class pool is N <= 6000, and section
8 sweeps every prime-power move with N in 2..399, l < 60 and e <= 3,
repeats included, and section 9 sweeps eight lambda against every
prime below 30000.
Primality is deterministic Miller-Rabin over the standard base set, valid
below ~3.3e24; nothing tested here approaches that. What is PROVED for all
N rather than sampled: the premium identity, the closed form and its
factorisation on a fresh prime power, the silent-import characterisation,
the cohort count at L = 1 with the minimum-gateway characterization of the
V = 24 primes, and the
injectivity of the probe on a lambda-fibre. The gateway ranking, the
silence-set composition and the class census are measurements at the stated
caps and nothing is claimed beyond them, the general prime-power form of
section 8 being proved for all N as well.

RUN RECORD. Python 3, no third-party dependencies, 1.0 s wall clock,
negligible memory. Nine sections, all checks pass. The positive control
runs first and the run aborts before any verdict is read if it fails. The
frozen form of section 3 is retained behind a flag and its 85 failures are
printed as a section-3 row; the run is green because the section asserts
that the frozen form fails AT q = 2 AND NOWHERE ELSE, which is the
observable, rather than asserting that it holds.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


# ---------------------------------------------------------------- arithmetic

_FCACHE = {}


def factorint(n):
    hit = _FCACHE.get(n)
    if hit is not None:
        return hit
    f, r, d = {}, n, 2
    while d * d <= r:
        while r % d == 0:
            f[d] = f.get(d, 0) + 1
            r //= d
        d += 1 if d == 2 else 2
    if r > 1:
        f[r] = f.get(r, 0) + 1
    if n < 200000:
        _FCACHE[n] = f
    return f


def v_p(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def divisors(n):
    ds = [1]
    for p, e in factorint(n).items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def lcm(a, b):
    return a // gcd(a, b) * b


def lam(n):
    """Carmichael's lambda."""
    if n == 1:
        return 1
    out = 1
    for p, e in factorint(n).items():
        if p == 2:
            part = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            part = p ** (e - 1) * (p - 1)
        out = lcm(out, part)
    return out


_DCACHE = {}


def doors(L):
    """Doors(L) = { p prime : (p-1) | L } -- the primes at the wall."""
    hit = _DCACHE.get(L)
    if hit is not None:
        return hit
    out = frozenset(d + 1 for d in divisors(L) if is_prime(d + 1))
    _DCACHE[L] = out
    return out


def two_part(L):
    """The exponent of 2 in W(L): 1 for odd L, v_2(L)+2 for even."""
    return 1 if L % 2 else v_p(L, 2) + 2


_WCACHE = {}


def wall(L):
    """The largest modulus whose lambda divides L.

    lambda(2^a) is 1, 2, then 2^(a-2), so the 2-part caps at 2 when L is ODD
    and at 2^(v_2(L)+2) when it is even. For odd p, lambda(p^a) =
    p^(a-1)(p-1) divides L iff (p-1) | L and a <= v_p(L)+1.
    """
    hit = _WCACHE.get(L)
    if hit is not None:
        return hit
    W = 2 ** two_part(L)
    for p in doors(L):
        if p > 2:
            W *= p ** (v_p(L, p) + 1)
    _WCACHE[L] = W
    return W


def headroom(N):
    """V(N) = W(lambda(N))/N -- the transparency headroom.

    N divides its own wall for every N, so the division is exact; the
    assert is a tripwire rather than a check, because a silent floor here
    would corrupt every section downstream and nothing else would notice.
    """
    W = wall(lam(N))
    assert W % N == 0, "N does not divide W(lambda(N)) at N=%d" % N
    return W // N


# ------------------------------------------------------------- the premium

def premium_def(N, m):
    """G' straight from the ledger: V(Nm) * gcd(m, V(N)) / V(N)."""
    V = headroom(N)
    num = headroom(N * m) * gcd(m, V)
    assert num % V == 0, "G' is not an integer at (N,m)=(%d,%d)" % (N, m)
    return num // V


def gain_and_unpaid(N, m):
    """The wall gain G = W(lambda(Nm))/W(lambda(N)) and the unpaid part
    P = m/gcd(m, V(N)). The premium identity says G' = G/P."""
    W0, W1 = wall(lam(N)), wall(lam(N * m))
    assert W1 % W0 == 0, "the wall fell at (N,m)=(%d,%d)" % (N, m)
    return W1 // W0, m // gcd(m, headroom(N))


def move_lam(q, e, frozen=False):
    """lambda(q^e) -- the move's own lambda, which is what the state's lambda
    takes an lcm with.

    The frozen form of section 3 wrote this as q^(e-1)(q-1) throughout. That
    is lambda(q^e) for ODD q and WRONG for q = 2, where lambda runs 1, 2,
    2^(e-2); the flag keeps the design's original expression available so the
    run can print its own kill rather than have it corrected out of sight.
    """
    if frozen or q > 2:
        return q ** (e - 1) * (q - 1)
    return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))


def wall_exp(L, q, frozen=False):
    """v_q(W(L)) -- the wall's own exponent at q, and for a prime q NOT in N
    also v_q(V(N)), since V = W(L)/N.

    The frozen form read this as v_q(L)+1 behind an open door, which is the
    odd-prime branch; at q = 2 the wall carries 2^(v_2(L)+2), or 2 when L is
    odd, and that branch is the one section 3 forgot.
    """
    if q == 2 and not frozen:
        return two_part(L)
    return v_p(L, q) + 1 if L % (q - 1) == 0 else 0


def fresh_premium(L, q, e, frozen=False):
    """The closed form for a FRESH import of q^e into a state of lambda L.

    Uses L, q and e only -- no reference to the state itself. Caller must
    guarantee q does not divide N.
    """
    Lp = lcm(L, move_lam(q, e, frozen))
    a = min(e, wall_exp(L, q, frozen))
    G = wall(Lp) // wall(L)
    return G // q ** (e - a)


def general_premium(L, V_l, l, e):
    """The premium of a prime-power move l^e on ANY state, fresh or repeat.

    Reads the state through its lambda L and the single exponent
    V_l = v_l(V(N)). The seated depth is not free: v_l(V) = v_l(W(L)) - c,
    so c = v_l(W(L)) - V_l, and the move carries the l-part from l^c to
    l^(c+e) while touching nothing else.
    """
    c = v_p(wall(L), l) - V_l
    Lp = lcm(L, move_lam(l, c + e))
    return (wall(Lp) // wall(L)) // l ** (e - min(e, V_l))


def fresh_cohort(L, q, e):
    """The primes the fresh import admits to the wall for the first time."""
    return doors(lcm(L, move_lam(q, e))) - doors(L)


def fresh_factored(L, q, e, frozen=False):
    """The same premium built from new doors, bumps and the unpaid part."""
    M = move_lam(q, e, frozen)
    Lp = lcm(L, M)
    val = 2 ** (two_part(Lp) - two_part(L))
    open_now = doors(L)
    for p in doors(Lp):
        if p == 2:
            continue
        if p in open_now:
            val *= p ** (v_p(Lp, p) - v_p(L, p))
        else:
            val *= p ** (v_p(Lp, p) + 1)
    a = min(e, wall_exp(L, q, frozen))
    return val // q ** (e - a)


# ---------------------------------------------------------------- batteries

MOVE_N = range(2, 400)
MOVE_M = range(2, 60)
FRESH_Q = [q for q in range(2, 60) if is_prime(q)]
FRESH_E = (1, 2, 3)


def is_safe_prime(q):
    """q = 2r+1 with r prime. 5 and 7 qualify (r = 2 and 3) and are the two
    the cohort argument of section 6 has to exclude, so the plain predicate
    and that argument's r >= 5 scope are kept apart deliberately."""
    return q > 2 and q % 2 == 1 and is_prime((q - 1) // 2)


def fresh_battery():
    """(N, q, e) triples with q not dividing N and N*q^e in range."""
    for N in MOVE_N:
        for q in FRESH_Q:
            if N % q == 0:
                continue
            for e in FRESH_E:
                yield N, q, e


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")

    CAP = 30000
    lam_tab = [lam(n) for n in range(0, CAP + 1)]
    Ls = sorted({lam(n) for n in range(1, 240)})
    fit = [L for L in Ls if wall(L) <= CAP]
    bad = 0
    for L in fit:
        brute = max(n for n in range(1, CAP + 1) if L % lam_tab[n] == 0)
        if brute != wall(L):
            bad += 1
            if bad == 1:
                print("  wall mismatch at L=%d: formula %d brute %d"
                      % (L, wall(L), brute))
    check(bad == 0, "wall() disagrees with brute force on %d of %d L"
          % (bad, len(fit)))
    print("  wall() = brute-force maximum on %d/%d lambda values fitting"
          " under %d" % (len(fit) - bad, len(fit), CAP))

    g = premium_def(16, 2)
    print("  (16,2): G'=%d  V 15 -> %d  lambda %d -> %d"
          % (g, headroom(32), lam(16), lam(32)))
    check(g == 1 and headroom(16) == 15 and headroom(32) == 15,
          "the (16,2) witness moved")

    print("  (3,16): V %d -> %d  lambda %d -> %d"
          % (headroom(3), headroom(48), lam(3), lam(48)))
    check(headroom(3) == 8 and headroom(48) == 5, "the (3,16) witness moved")

    print("  (10,11) under m=5: V %d,%d -> %d,%d"
          % (headroom(10), headroom(11), headroom(50), headroom(55)))
    check(headroom(10) == 24 and headroom(11) == 24
          and headroom(50) != headroom(55), "the (10,11) witness moved")

    n = 0
    for N in MOVE_N:
        for m in MOVE_M:
            premium_def(N, m)
            n += 1
    print("  G' a positive integer over %d moves, N in 2..399, m in 2..59" % n)
    print()


# ------------------------------------------------------- S2 premium identity

def s2_identity():
    print("S2 THE PREMIUM IDENTITY   G' = (wall gain) / (unpaid part)")
    bad = notdiv = n = 0
    worked = None
    for N in MOVE_N:
        for m in MOVE_M:
            G, P = gain_and_unpaid(N, m)
            g = premium_def(N, m)
            n += 1
            if G % P:
                notdiv += 1
            if G // P != g or G % P:
                bad += 1
                if bad == 1:
                    print("  mismatch at (N,m)=(%d,%d): G=%d P=%d G'=%d"
                          % (N, m, G, P, g))
            if worked is None and g > 1 and P > 1:
                worked = (N, m, G, P, g)
    check(bad == 0, "the premium identity fails on %d of %d moves" % (bad, n))
    check(notdiv == 0, "the unpaid part fails to divide the gain %d times"
          % notdiv)
    print("  G' = G/P on %d/%d moves; P | G on all of them" % (n - bad, n))
    N, m, G, P, g = worked
    print("  worked row  N=%d m=%d: wall %d -> %d, gain %d, unpaid %d,"
          " G'=%d" % (N, m, wall(lam(N)), wall(lam(N * m)), G, P, g))
    print()


# ------------------------------------------------------- S3 the closed form

def s3_closed_form():
    print("S3 THE CLOSED FORM ON A FRESH IMPORT")
    froz_bad, bad, n, froz_q = 0, 0, 0, set()
    first = None
    for N, q, e in fresh_battery():
        g = premium_def(N, q ** e)
        n += 1
        if fresh_premium(lam(N), q, e, frozen=True) != g:
            froz_bad += 1
            froz_q.add(q)
            if first is None:
                first = (N, q, e, fresh_premium(lam(N), q, e, frozen=True), g)
        if fresh_premium(lam(N), q, e) != g:
            bad += 1
            if bad == 1:
                print("  mismatch at N=%d q=%d e=%d: closed %d definitional %d"
                      % (N, q, e, fresh_premium(lam(N), q, e), g))
    check(froz_bad > 0 and froz_q == {2}, "the frozen form's failure set moved")
    print("  the form AS FROZEN fails on %d/%d fresh imports, at q in %s and"
          " nowhere else" % (froz_bad, n, sorted(froz_q)))
    if first:
        N, q, e, f, g = first
        print("    first: N=%d q=%d e=%d gives %d against %d, because the"
              " design wrote" % (N, q, e, f, g))
        print("    lambda(q^e) = q^(e-1)(q-1), which is the ODD branch:"
              " lambda(2^%d) = %d, not %d" % (e, move_lam(2, e), 2 ** (e - 1)))
    print("  repaired uniformly -- lambda(q^e) for the lcm and v_q(W(L)) for"
          " the payment:")
    check(bad == 0, "the closed form fails on %d of %d fresh imports"
          % (bad, n))
    print("    closed form = definitional G' on %d/%d fresh imports"
          " (N<400, q<60, e<=3)" % (n - bad, n))

    by_lam = {}
    for N in MOVE_N:
        by_lam.setdefault(lam(N), []).append(N)
    shared = {L: ns for L, ns in by_lam.items() if len(ns) > 1}
    disagree = pairs = 0
    for L, ns in shared.items():
        for q in FRESH_Q:
            grp = [N for N in ns if N % q]
            if len(grp) < 2:
                continue
            for e in FRESH_E:
                vals = {premium_def(N, q ** e) for N in grp}
                pairs += len(grp) - 1
                if len(vals) > 1:
                    disagree += 1
                    if disagree == 1:
                        print("  lambda=%d q=%d e=%d gives %s"
                              % (L, q, e, sorted(vals)))
    check(disagree == 0, "equal-lambda states disagree on %d fresh moves"
          % disagree)
    print("  %d lambda classes with 2+ states; %d same-lambda comparisons,"
          " %d disagreements" % (len(shared), pairs, disagree))

    g3, g8 = premium_def(3, 3), premium_def(8, 3)
    print("  the repeat witness: lambda(3)=lambda(8)=%d, m=3 gives"
          " G'(3,3)=%d and G'(8,3)=%d" % (lam(3), g3, g8))
    print("    (m=3 is a REPEAT push at N=3 and a fresh import at N=8;"
          " lambda 2 -> %d and 2 -> %d)" % (lam(9), lam(24)))
    check(g3 != g8, "lambda-sufficiency did not fail on the frozen witness")
    print()


# ------------------------------------------------- S4 new doors times bumps

def s4_factored():
    print("S4 NEW DOORS TIMES BUMPS")
    bad = trunc_bad = n = froz_bad = 0
    for N, q, e in fresh_battery():
        L = lam(N)
        f = fresh_factored(L, q, e)
        g = premium_def(N, q ** e)
        n += 1
        if fresh_factored(L, q, e, frozen=True) != g:
            froz_bad += 1
        if f != g:
            bad += 1
            if bad == 1:
                print("  mismatch at N=%d q=%d e=%d: factored %d actual %d"
                      % (N, q, e, f, g))
        M = move_lam(q, e)
        Lp = lcm(L, M)
        for p in set(factorint(Lp)) | set(factorint(M)):
            if v_p(Lp, p) - v_p(L, p) != max(0, v_p(M, p) - v_p(L, p)):
                trunc_bad += 1
    check(bad == 0, "the factored form fails on %d of %d fresh imports"
          % (bad, n))
    check(trunc_bad == 0, "the truncated-subtraction reading fails %d times"
          % trunc_bad)
    print("  factored = definitional on %d/%d fresh imports (the form as"
          " frozen: %d/%d, the same q=2 hole)" % (n - bad, n, n - froz_bad, n))
    print("  v_p(L') - v_p(L) = max(0, v_p(M) - v_p(L)) at every prime,"
          " 0 exceptions")

    L, q, e = lam(11), 7, 1
    M = move_lam(q, e)
    Lp = lcm(L, M)
    print("  worked row  lambda=%d, import q=%d: lambda -> %d, cohort %s,"
          % (L, q, Lp, sorted(fresh_cohort(L, q, e))))
    print("    wall %d -> %d, unpaid %d, G'=%d"
          % (wall(L), wall(Lp), q, fresh_premium(L, q, e)))
    print()


# ------------------------------------------------------ S5 the silent import

def s5_silent():
    print("S5 THE SILENT IMPORT")
    L, q = 2, 11
    coh = fresh_cohort(L, q, 1)
    print("  (L,q)=(2,11): door shut (%d-1 does not divide %d), cohort %s,"
          % (q, L, sorted(coh)))
    print("    wall %d -> %d = %d * %d, G'=%d"
          % (wall(L), wall(lcm(L, q - 1)), q, wall(L),
             fresh_premium(L, q, 1)))
    check(fresh_premium(L, q, 1) == 1 and L % (q - 1) != 0
          and coh == frozenset([q]), "the silent-import witness moved")

    open_bad = shut_bad = n_open = n_shut = n_silent = n_silent_safe = 0
    odd_lam_silent = 0
    silent_states = []
    for N in MOVE_N:
        L = lam(N)
        for q in FRESH_Q:
            if N % q == 0:
                continue
            g = premium_def(N, q)
            if L % (q - 1) == 0:
                n_open += 1
                if g != 1 or headroom(N * q) * q != headroom(N):
                    open_bad += 1
            else:
                n_shut += 1
                if g == 1:
                    n_silent += 1
                    if L % 2:
                        odd_lam_silent += 1
                    if is_safe_prime(q):
                        n_silent_safe += 1
                    if fresh_cohort(L, q, 1) != frozenset([q]) \
                            or v_p(L, q) != 0:
                        shut_bad += 1
                    elif len(silent_states) < 6:
                        silent_states.append((N, q, L, headroom(N)))
    check(open_bad == 0, "%d open-door fresh imports miss G'=1 or V/q"
          % open_bad)
    check(shut_bad == 0, "%d shut-door G'=1 imports have a cohort past {q}"
          % shut_bad)
    print("  open door: G'=1 and V(Nq) = V(N)/q on %d/%d fresh single"
          " imports" % (n_open - open_bad, n_open))
    print("  shut door: %d of %d fresh single imports pay G'=1, and every"
          " one" % (n_silent, n_shut))
    print("    has cohort {q} with v_q(lambda)=0 -- 0 with a larger cohort")
    print("  silent imports (lambda moves, V untouched, door shut):")
    for N, q, L, V in silent_states:
        print("    N=%d q=%d: lambda %d -> %d, V %d -> %d"
              % (N, q, L, lam(N * q), V, headroom(N * q)))
    print("    %d of the %d import a SAFE prime, so %d do not -- the family"
          " is wider" % (n_silent_safe, n_silent, n_silent - n_silent_safe))
    check(odd_lam_silent == 0, "%d silent imports at an ODD lambda"
          % odd_lam_silent)
    print("  and NONE of them sits at an odd lambda, as the 2-part forces:"
          " an odd lambda")
    print("    carries a wall 2-part of 2, a fresh odd q makes lcm(lambda,"
          " q-1) even, and the")
    print("    2-part jumps to 2^(v_2(q-1)+2) >= 8, so the premium is at"
          " least 4 (0 exceptions)")
    print()


# ---------------------------------------------------------------- S6 gateways

def _spearman(xs, ys):
    def ranks(vs):
        order = sorted(range(len(vs)), key=lambda i: vs[i])
        r = [0.0] * len(vs)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vs[order[j + 1]] == vs[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx) ** 0.5
    dy = sum((b - my) ** 2 for b in ry) ** 0.5
    return num / (dx * dy)


def s6_gateways():
    print("S6 WHICH PRIMES ARE GATEWAYS (from the empty state, lambda = 1)")
    qs = [q for q in range(3, 2000) if is_prime(q)]
    sizes, dcount, lpf, safe_bad, count_bad = [], [], [], 0, 0
    for q in qs:
        coh = fresh_cohort(1, q, 1)
        pred = sum(1 for d in divisors(q - 1) if d >= 2 and is_prime(d + 1))
        if len(coh) != pred:
            count_bad += 1
        sizes.append(len(coh))
        dcount.append(len(divisors(q - 1)))
        lpf.append(max(factorint(q - 1)))
        r = (q - 1) // 2
        if q % 2 and is_prime(r) and r >= 5 and coh != frozenset([3, q]):
            safe_bad += 1
    check(count_bad == 0, "the cohort size differs from the divisor count"
          " %d times" % count_bad)
    check(safe_bad == 0, "%d safe primes have a cohort past {3, q}" % safe_bad)
    print("  |C(1,q)| = #{ d | q-1 : d >= 2, d+1 prime } on %d/%d primes"
          " below 2000" % (len(qs) - count_bad, len(qs)))
    n_safe = sum(1 for q in qs if is_safe_prime(q) and (q - 1) // 2 >= 5)
    print("  every safe prime q = 2r+1 with r >= 5 opens exactly {3, q}"
          " (%d of them)" % n_safe)
    print("  cohort size: min %d, max %d, mean %.2f"
          % (min(sizes), max(sizes), sum(sizes) / len(sizes)))
    floor = [q for q, s in zip(qs, sizes) if s == 1]
    two = [q for q, s in zip(qs, sizes) if s == 2]
    two_unsafe = [q for q in two if not is_safe_prime(q)]
    print("  the FLOOR is %s, opening only itself; {3, q} is the minimum for"
          " every other q," % floor)
    print("    attained by %d primes below 2000, %d of them SAFE primes --"
          " %d with r >= 5, plus 5 and 7," % (len(two),
                                              len(two) - len(two_unsafe),
                                              n_safe))
    print("    which are safe primes the cohort argument has to exclude;"
          " the other %d are not safe at all: %s"
          % (len(two_unsafe), two_unsafe[:6]))
    check(floor == [3], "the cohort floor is not the single prime 3")

    # The minimum-cohort primes are the largest blind class, not the safe
    # primes: for q > 5 a cohort of {3, q} forces v_2(q-1) = 1 (else 5 is a
    # third door), so W(q-1) = 2^3 * 3^(v_3+1) * q and V(q) = 24 * 3^v_3.
    floor_primes = {q for q in two if q > 5 and v_p(q - 1, 3) == 0}
    blind24 = {q for q in qs if q > 5 and headroom(q) == 24}
    check(floor_primes == blind24,
          "the minimum-cohort primes and the V = 24 primes differ by %d"
          % len(floor_primes ^ blind24))
    print("  {q > 5 : cohort {3,q} and 3 does not divide q-1} = {q > 5 :"
          " V(q) = 24}," )
    print("    %d primes below 2000, exactly -- the largest blind class IS"
          " the minimum-gateway" % len(blind24))
    print("    family, and the safe primes are one sub-family of it (7 is"
          " excluded by 3 | 6: V(7) = %d)" % headroom(7))
    top = sorted(zip(sizes, qs), reverse=True)[:8]
    print("  top gateways:")
    for s, q in top:
        print("    q=%-5d opens %2d  (q-1 = %s, %d divisors)"
              % (q, s, "*".join("%d^%d" % (p, e) if e > 1 else str(p)
                                for p, e in sorted(factorint(q - 1).items())),
                 len(divisors(q - 1))))
    print("  Spearman |C| vs divisor count of q-1 : %+.3f"
          % _spearman(sizes, dcount))
    print("  Spearman |C| vs largest prime of q-1 : %+.3f"
          % _spearman(sizes, lpf))
    print("  Spearman |C| vs q itself             : %+.3f"
          % _spearman(sizes, qs))
    print()


# ------------------------------------------------ S7 the stitch and the probe

def s7_stitch_and_probe():
    print("S7 THE STITCH, AND WHAT THE PROBE CANNOT DO")
    print("  (a) the Fermat ladder L = 2^t -- the spectrum law as cohorts")
    bad = 0
    for t in range(0, 17):
        L, Lp = 2 ** t, 2 ** (t + 1)
        coh = doors(Lp) - doors(L)
        want = frozenset([Lp + 1]) if is_prime(Lp + 1) else frozenset()
        if coh != want:
            bad += 1
        if coh:
            p = max(coh)
            print("    2^%-2d -> 2^%-2d opens %-6d at wall exponent %d"
                  % (t, t + 1, p, v_p(Lp, p) + 1))
    check(bad == 0, "the Fermat ladder cohort is wrong at %d steps" % bad)
    print("    cohorts nonempty at exactly %d of 17 steps; empty at all"
          " others" % sum(1 for t in range(17)
                          if doors(2 ** (t + 1)) - doors(2 ** t)))

    print("  (b) the probe on a lambda-fibre")
    CAP = 6000
    Vs = {}
    for N in range(2, CAP + 1):
        Vs.setdefault(headroom(N), []).append(N)
    classes = {V: ns for V, ns in Vs.items() if len(ns) > 1}
    dup = 0
    for V, ns in classes.items():
        ls = [lam(N) for N in ns]
        if len(set(ls)) != len(ls):
            dup += 1
    check(dup == 0, "%d blind classes contain two states with equal lambda"
          % dup)
    print("    %d non-singleton headroom classes below %d, covering %d"
          " states" % (len(classes), CAP, sum(len(n) for n in classes.values())))
    print("    every one has pairwise distinct lambda: %d exceptions" % dup)

    print("  (c) a blind pair split by a FRESH import")
    found = None
    for V in sorted(classes):
        ns = classes[V]
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                a, b = ns[i], ns[j]
                for q in FRESH_Q:
                    if a % q == 0 or b % q == 0:
                        continue
                    if premium_def(a, q) != premium_def(b, q):
                        found = (a, b, V, q)
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    a, b, V, q = found
    print("    N=%d and N=%d both read V=%d (lambda %d and %d);"
          % (a, b, V, lam(a), lam(b)))
    print("    a fresh import of %d gives premiums %d and %d, so V -> %d"
          " and %d" % (q, premium_def(a, q), premium_def(b, q),
                       headroom(a * q), headroom(b * q)))
    check(headroom(a * q) != headroom(b * q), "the fresh split witness failed")

    print("  (d) silence sets -- fresh primes that keep a blind pair merged")
    shown, kinds, alone_safe = 0, [0, 0, 0], [0]
    for V in sorted(classes):
        ns = classes[V]
        if len(ns) < 2:
            continue
        a, b = ns[0], ns[1]
        silent, total = [], 0
        for q in [p for p in range(2, 100) if is_prime(p)]:
            if a % q == 0 or b % q == 0:
                continue
            total += 1
            ga, gb = premium_def(a, q), premium_def(b, q)
            if ga != gb:
                continue
            silent.append(q)
            both_open = lam(a) % (q - 1) == 0 and lam(b) % (q - 1) == 0
            kind = 0 if both_open else (1 if ga == 1 else 2)
            kinds[kind] += 1
            if kind == 1 and is_safe_prime(q):
                alone_safe[0] += 1
        if shown < 4:
            print("    (%d, %d) V=%d: %d of %d fresh primes below 100"
                  " silent %s" % (a, b, V, len(silent), total, silent[:8]))
            shown += 1
    print("    over ONE representative pair per class (%d of them, the two"
          " smallest members): %d silences" % (len(classes), kinds[0]))
    print("    are doors already open at both, %d are the admitted-alone"
          " imports of section 5," % kinds[1])
    print("    and %d carry a premium above 1 that happens to agree"
          % kinds[2])
    safe = [q for q in range(3, 100) if is_prime(q) and is_safe_prime(q)]
    print("    of the %d admitted-alone silences, %d import a SAFE prime"
          " (%s below 100)" % (kinds[1], alone_safe[0], safe))
    print()


# --------------------------------------------------- S8 the repeat push

def s8_general():
    print("S8 THE PREMIUM ON A REPEAT PUSH")
    bad = n = repeats = 0
    seen = {}
    for N in MOVE_N:
        L, V = lam(N), headroom(N)
        for l in FRESH_Q:
            for e in FRESH_E:
                g = premium_def(N, l ** e)
                f = general_premium(L, v_p(V, l), l, e)
                n += 1
                if N % l == 0:
                    repeats += 1
                if f != g:
                    bad += 1
                    if bad == 1:
                        print("  mismatch at N=%d l=%d e=%d: general %d"
                              " actual %d" % (N, l, e, f, g))
                key = (L, v_p(V, l), l, e)
                hit = seen.setdefault(key, [set(), 0])
                hit[0].add(g)
                hit[1] += 1
    check(bad == 0, "the general form fails on %d of %d prime-power moves"
          % (bad, n))
    print("  general form = definitional G' on %d/%d prime-power moves,"
          " of which %d are repeats" % (n - bad, n, repeats))

    coll = [k for k, hit in seen.items() if len(hit[0]) > 1]
    multi = sum(hit[1] - 1 for hit in seen.values() if hit[1] > 1)
    check(not coll, "%d (lambda, v_l(V), l, e) keys carry two premiums"
          % len(coll))
    print("  %d distinct (lambda, v_l(V), l, e) keys, %d of the moves"
          " landing on a key another move already held; %d keys carry two"
          " premiums" % (len(seen), multi, len(coll)))

    # How much of lambda-sufficiency survives on repeats, measured rather
    # than asserted: GUARANTEED is not the same as OBSERVED, and section 3's
    # theorem only guarantees the fresh case.
    by_lam = {}
    for N in MOVE_N:
        by_lam.setdefault(lam(N), []).append(N)
    cells = holds = 0
    for L, ns in by_lam.items():
        if len(ns) < 2:
            continue
        for l in FRESH_Q:
            grp = [N for N in ns if N % l == 0]
            if len(grp) < 2:
                continue
            for e in FRESH_E:
                cells += 1
                if len({premium_def(N, l ** e) for N in grp}) == 1:
                    holds += 1
    print("  on REPEAT pushes lambda alone is not GUARANTEED but usually"
          " still suffices:")
    print("    %d of %d (lambda, l, e) cells holding two or more repeat"
          " states agree anyway," % (holds, cells))
    print("    so the scope word is ONLY, never EXACTLY -- the %d that"
          " disagree are what the" % (cells - holds))
    print("    theorem cannot cover, and one of them is the frozen witness")
    check(0 < holds < cells, "the repeat cells are all-or-nothing")

    L, a, b = lam(3), 3, 8
    print("  the frozen witness explained: lambda(%d)=lambda(%d)=%d, but"
          % (a, b, L))
    print("    v_3(V(%d))=%d and v_3(V(%d))=%d, so the seated depths are"
          " %d and %d" % (a, v_p(headroom(a), 3), b, v_p(headroom(b), 3),
                          v_p(a, 3), v_p(b, 3)))
    print("    and the premiums must differ: %d against %d"
          % (premium_def(a, 3), premium_def(b, 3)))
    check(v_p(headroom(a), 3) != v_p(headroom(b), 3),
          "the frozen witness agrees on v_l(V) after all")
    print()


# ------------------------------------------------- S9 silence is blindness

SILENCE_LAMBDAS = (2, 4, 6, 10, 12, 16, 18, 22)
SILENCE_CAP = 30000


def s9_silence_is_blindness():
    print("S9 WHAT THE SILENT SET IS")
    primes = [q for q in range(3, SILENCE_CAP) if is_prime(q)]
    bad = 0
    for L in SILENCE_LAMBDAS:
        W = wall(L)
        silent, divisible, matched = 0, 0, 0
        for q in primes:
            if L % (q - 1) == 0:
                continue                       # door open: not a silent case
            sil = fresh_premium(L, q, 1) == 1
            silent += sil
            if (q - 1) % L:
                continue
            divisible += 1
            if sil != (headroom(q) == W):
                bad += 1
            else:
                matched += sil
        print("  lambda=%-3d W=%-6d silent below %d: %-4d, of which %-4d"
              " have lambda | q-1;" % (L, W, SILENCE_CAP, silent, divisible))
        print("      every one of those %d is a member of the blind class"
              " V = %d" % (matched, W))
    check(bad == 0, "silence and V = W(lambda) disagree %d times" % bad)

    sil2 = {q for q in primes
            if q > 5 and 2 % (q - 1) != 0 and fresh_premium(2, q, 1) == 1}
    v24 = {q for q in primes if q > 5 and headroom(q) == 24}
    check(sil2 == v24, "the silent set at lambda=2 differs from V=24 by %d"
          % len(sil2 ^ v24))
    print("  at lambda = 2 the restriction is vacuous, so the WHOLE silent"
          " set is the class")
    print("    V = 24: %d primes below %d, 0 discrepancy -- the same family"
          % (len(v24), SILENCE_CAP))
    print("    as the minimum gateways and the commonest silencers, a third"
          " face of one set")
    print("  CONSEQUENCE: 'is the silent set at lambda infinite' IS 'is the"
          " blind class")
    print("    V = W(lambda) infinite', so at lambda = 2 it is the Sophie"
          " Germain ceiling")
    print("    already filed -- not a way around that wall but the same"
          " wall, named twice")
    print()


# ------------------------------------------------------------------ the run

def main():
    s1_control()
    if FAIL:
        print("POSITIVE CONTROL FAILED -- no verdict is read.")
        return 1
    s2_identity()
    s3_closed_form()
    s4_factored()
    s5_silent()
    s6_gateways()
    s7_stitch_and_probe()
    s8_general()
    s9_silence_is_blindness()
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("all sections pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
