"""explore_composite_move.py -- THE COMPOSITE MOVE, AND WHETHER THE
HEADROOM LEDGER CLOSES ON THE WHOLE GROWTH MONOID (sibling of
explore_premium.py, explore_headroom.py, explore_slack_machine.py).

THE QUESTION. A state of the growing tower is a positive integer N, a move
is a multiplication N -> N*m, and the transparency headroom

    V(N) = W(lambda(N)) / N,   W(L) = the largest modulus whose lambda | L,

splits every move into what it SPENDS and what it OPENS:

    V(Nm) = ( V(N) / gcd(m, V(N)) ) * G'(N, m),   G' a positive integer

(the headroom ledger, explore_headroom.py). Both halves are closed for a
PRIME-POWER move: the spending half is truncated subtraction on V's
exponents, and the opening half reads the state through its lambda and the
SINGLE exponent v_l(V) (explore_premium.py). A general move is a product of
prime powers, and the ledger is not yet closed there. Two questions, one
cheap and one not:

  (a) Is there a closed form for a COMPOSITE move at all? The prime-power
      law works by never referring to an intermediate state. Splitting
      m = ab and composing the two prime-power laws does refer to one, so
      the suspicion worth attacking is that a composite move is genuinely
      path-dependent and has no state-local form.
  (b) If it closes, HOW MUCH of the percept does it need? The prime-power
      law needs one coordinate. A composite move plausibly needs one per
      prime -- and whether that slice is TIGHT, or collapses further, is
      what says whether the probe is closer to or further from computing
      its own next reading.

THE OBJECTS. For a prime p write v_p for the p-adic valuation. The DOORS of
L are Doors(L) = { p prime : (p-1) | L }, and

    W(L) = (2 if L odd else 2^(v_2(L)+2)) * prod{ p^(v_p(L)+1)
             : p odd, p in Doors(L) },

W's 2-part being 2 for ODD L and 2^(v_2(L)+2) for even because lambda(2^a)
is 1, 2, then 2^(a-2). THE WALL GAIN of a move is G = W(lambda(Nm))/W(lambda
(N)); THE UNPAID PART is P = m/gcd(m, V(N)); and G' = G/P (the premium
identity, explore_premium.py). For a move m the PERCEPT SLICE is the tuple
( v_l(V(N)) : l | m ) -- one coordinate of the probe's reading per prime of
the move, and omega(m) of them in all.

THE DESIGN, in seven sections (S6 and S7 were added mid-run; see their
headers). The slate is frozen before any engine code;
where a run contradicts it the framing is left standing and flagged rather
than quietly rewritten.

WHOSE VOCABULARY. The question is written in the LEDGER's terms -- spending,
opening, closure -- while the sharp form of (b) is the OBSERVER's: how many
coordinates of a reading does an ascent need. Both are deliberate and the
second is the reason to ask. THE TRANSPLANT TO MARK: every intuition here
about what a move does to lambda is imported from the one-prime case, where
the move's own lambda is a single lcm factor. A composite move contributes
omega(m) of them at once, and "the primes do not interact" is exactly the
kind of clause that holds for lcm and fails for the wall, whose exponent at
a prime p is read off the LCM rather than off any one factor. Marked, not
assumed: section 4's defect is where interaction would show.

S1 POSITIVE CONTROL, run before any verdict is read. wall() against its own
   DEFINITION -- the largest modulus found by brute search -- compared only
   where the wall fits under the search cap, since a truncated search
   reports the formula wrong for every large wall. Then the three witnesses
   the ledger froze must come back unchanged: (N, m) = (16, 2) prints
   G' = 1 with V unchanged at 15 and lambda 4 -> 8; (N, m) = (3, 16) prints
   V 8 -> 5; and N = 10, N = 11 share the headroom 24 while one push of 5
   sends them to 264 and 240. Last, on every move of the battery with
   omega(m) = 1 the new form must equal the DEFINITIONAL G' -- the check
   that can actually fail -- and must also collapse onto the established
   prime-power expression, which is a check on the new code path and NOT
   on the mathematics, the two being the same formula written for one
   prime.

S2 THE COMPOSITE CLOSED FORM. Hand-derived before the engine, in three
   steps. (i) lambda of n is the lcm of lambda(p^v_p(n)) over p | n, and
   N*m has v_p = v_p(N) off m and c_l + e_l on it, where c_l = v_l(N) and
   e_l = v_l(m); adjoining lambda(N) to the lcm over the untouched primes
   changes nothing, since the factors it adds are the lambda(l^c_l) and
   each divides lambda(l^(c_l+e_l)). So

       lambda(N m) = lcm( L, lcm{ lambda(l^(c_l + e_l)) : l | m } ),
       L = lambda(N).

   (ii) c_l is not free: V = W(L)/N with N | W(L) exactly, so
   c_l = v_l(W(L)) - v_l(V). (iii) The unpaid part factors over the primes
   of m as prod l^(e_l - min(e_l, v_l(V))). Hence for EVERY state and EVERY
   move,

       G'(N, m) = W( lcm(L, lcm{ lambda(l^(c_l+e_l)) : l | m }) )
                  / ( W(L) * prod{ l^(e_l - min(e_l, v_l(V))) : l | m } ),
       c_l = v_l(W(L)) - v_l(V).

   If that holds THE LEDGER CLOSES ON THE WHOLE GROWTH MONOID, and the
   suspicion behind question (a) is wrong for a reason worth stating: the
   direct derivation never splits the move, so no intermediate state is
   referenced. An intermediate state is an artifact of the CHAIN
   decomposition (section 4), not of the composite move.
   PREDICTION S2a: the composite form matches the definitional G' on every
   move in the battery, composites included, 0 exceptions.
   PREDICTION S2b: when m is COPRIME to N every c_l is 0, so G' is a
   function of (L, m) alone there -- any two battery states sharing a
   lambda and both coprime to m give the same premium under m, 0
   exceptions. This is the composite generalisation of the fresh-import
   law and the only regime where lambda alone suffices.

S3 HOW MUCH PERCEPT AN ASCENT NEEDS. Section 2 makes the premium a
   function of the KEY ( L, m, (v_l(V) : l | m) ). Two things to measure
   that a re-parametrisation would not survive. COLLISIONS: how many moves
   land on a key another move already held, broken out by omega(m) -- a key
   that is merely N in disguise would collide with nothing. TIGHTNESS: is
   every coordinate of the slice load-bearing? Drop one coordinate at a
   time from the key of a composite move and count the reduced keys that
   carry two premiums; and drop the whole slice, leaving (L, m).
   PREDICTION S3a: 0 full keys carry two premiums (this is S2a restated as
   a partition, and it is the observable), with the collision counts
   measured, not predicted.
   PREDICTION S3b: the slice is TIGHT -- for composite moves the (L, m) key
   alone carries two premiums, and so does the key with any single
   coordinate dropped. If instead every dropped-coordinate key is
   single-valued the slice is redundant and the honest law is smaller than
   section 2's.

S4 THE CHAIN RULE AND ITS DEFECT. Take any split m = ab with a, b > 1. The
   wall gain telescopes exactly, W(lambda(Nab))/W(lambda(N)) being a
   product of two such ratios. The unpaid part does not, and everything
   else cancels:

       G'(N, ab) = G'(N, a) * G'(Na, b) * gcd(ab, V(N))
                     / ( gcd(a, V(N)) * gcd(b, V(Na)) ).

   THE ORIENTATION IS THE EASY THING TO GET UPSIDE DOWN, so the rig checks
   both and prints which holds. And the correction has a SIGN, proved prime
   by prime before the run: with alpha = v_l(a), beta = v_l(b),
   v = v_l(V(N)) and v' = v_l(V(Na)) = v - min(alpha, v) + v_l(G'(N,a))
   >= v - min(alpha, v), the claim min(alpha+beta, v) <= min(alpha, v) +
   min(beta, v') splits into two cases -- alpha >= v gives RHS >= v >= LHS,
   and alpha < v gives RHS >= alpha + min(beta, v-alpha) = min(alpha+beta,
   v). So the correction is the reciprocal of a positive integer: A SPLIT
   MOVE NEVER UNDERCOUNTS THE PREMIUM. Equality needs, at every l | b,
   either v_l(G'(N,a)) = 0 or beta <= v - alpha -- the first step opens no
   l-door BELOW the exponent the second step is about to pay.
   Since V(Nab) is one state either way, an inflated opening half comes
   with an equally inflated spending half: the GROSS flows of the ledger
   are path-dependent and only their quotient is not.
   PREDICTION S4a: the wall gain telescopes exactly on every split in the
   battery, 0 exceptions -- the control on the decomposition claim, and the
   thing that isolates the defect in the unpaid part alone.
   PREDICTION S4b: the identity above holds exactly with the whole move's
   gcd in the NUMERATOR, 0 exceptions, and the inverted orientation fails
   on at least one printed split.
   PREDICTION S4c: the correction is 1/(a positive integer) on every split,
   0 exceptions -- never above 1 -- and it equals 1 exactly when the
   criterion above says so, 0 disagreements. HOW OFTEN it bites is measured.

S5 SLOW MOTION AS A RESOLUTION KNOB. Two states with equal headroom are one
   state to the probe (a blind pair), and a fresh import splits them
   exactly when the premiums differ (explore_premium.py). A split move
   hands the probe a reading it could not have computed, V(Na), so watching
   one move in two steps is strictly more percept than watching it whole.
   The question is whether that ever MATTERS: is there a blind pair and a
   move that leaves the pair blind, whose intermediate reading splits it?
   PREDICTION S5: such a triple exists in the pool and one is printed. The
   RATE -- of the (pair, move) cases that stay blind across the whole move,
   how many are split by some intermediate reading -- is measured, not
   predicted. A rate of zero would say the ledger's path-dependence is
   invisible to the probe, which is the outcome that would make section 4 a
   bookkeeping curiosity rather than an observer statement.

S6 THE PRIMES OF A MOVE INTERACT (added to the design after section 4
   printed, and frozen from a hand derivation before its engine was
   written; the marked transplant above is what provoked it -- section 2
   closes the ledger without ever asking whether the omega(m) coordinates
   act independently, and they need not). The COHORT of a move is
   C = Doors(lambda(Nm)) \\ Doors(L), the primes it admits to the wall for
   the first time. Doors is monotone in divisibility, so for a split
   m = ab the joint cohort always CONTAINS C(a) and C(b). It can contain
   more, because the joint lcm can be divisible by a d with d+1 prime when
   neither single lcm is: at L = 1 with a = 5 and b = 7, lcm(1,4) = 4 opens
   {3, 5}, lcm(1,6) = 6 opens {3, 7}, and lcm(4,6) = 12 opens {3, 5, 7,
   13}. THE MOVE 35 OPENS A DOOR NEITHER 5 NOR 7 OPENS. So the premium is
   not a product over the primes of the move, and it fails in BOTH
   directions: the interaction cohort makes the joint premium larger than
   the product, while a bump both factors pay for separately is paid once
   jointly and makes it smaller.
   PREDICTION S6a: the witness prints -- 13 in the joint cohort at L = 1,
   m = 35, in neither single cohort -- and C(ab) contains C(a) union C(b)
   on every coprime split in the battery, 0 exceptions. The comparison is
   symmetric in a and b, so each UNORDERED coprime pair is counted once
   here, where section 4's ordered splits are two distinct paths.
   PREDICTION S6b: G'(N, ab) = G'(N, a) * G'(N, b) FAILS on coprime splits,
   in both directions, with the smallest witness of each printed. The rates
   are measured. If instead it never fails the omega(m) coordinates
   decouple and section 2's law factors, which would be a bigger law than
   the one derived.

S7 IS ANY PAIR BLIND FOREVER? (added to the design after section 5
   printed, and frozen from a hand derivation before its engine was
   written; section 5 measures how often a reading INSIDE a move resolves a
   blind pair and never asks whether some pair resists every multiplier.)
   The derivation is three lines. For a blind pair N1 != N2 with
   V(N1) = V(N2) = V, the definition gives W(lambda_i) = V*N_i, so the two
   WALLS DIFFER. Put L = lcm(lambda_1, lambda_2) and take a prime q = 1 mod
   L not dividing either state -- Dirichlet supplies infinitely many, and
   Dirichlet is a theorem, so nothing here rests on a conjecture. Then
   lambda_i | L | q-1, so lambda(N_i q) = lcm(lambda_i, q-1) = q-1 for BOTH
   states: the walls AGREE at W(q-1), and

       V(N_i q) = W(q-1) / (N_i q)

   cannot agree, because N_1 != N_2. So THE MULTIPLIER q RESOLVES THE PAIR,
   and NO PAIR OF DISTINCT STATES IS BLIND UNDER EVERY MULTIPLIER -- the
   resolving set is never empty, and a resolver can be written down rather
   than searched for. This is the injectivity of the probe on a
   lambda-fibre used constructively: instead of observing that a blind pair
   must have distinct lambda, MAKE the two lambda coincide and read off the
   contradiction.
   PREDICTION S7a: for every blind pair in the pool the least such q
   resolves it, with lambda(N_1 q) = lambda(N_2 q) = q-1 at every one, 0
   exceptions.
   PREDICTION S7b: the resolving set is not merely nonempty but easy to
   hit, so the SMALLEST resolving multiplier is far below that q for most
   pairs -- measured, not predicted, since the construction is built for
   certainty rather than for size.

WHAT WOULD KILL WHAT (observables, not inferences). S1 aborts the run if
the wall disagrees with brute force, a frozen witness prints differently,
or the composite form disagrees with the prime-power form anywhere they
overlap. S2a dies on one printed move where the composite form disagrees
with the definitional G'. S2b dies on one printed pair of equal-lambda
states, both coprime to m, disagreeing under m. S3a dies on one printed key
carrying two premiums. S3b dies if every dropped-coordinate key is
single-valued. S4a dies on one printed split whose wall gains do not
telescope. S4b dies on one printed split where the identity fails, or if
the inverted orientation never fails. S4c dies on one printed split with a
correction above 1 or not a unit fraction, or on one printed disagreement
between correction = 1 and the criterion. S5's nonemptiness dies if no
(pair, move, split) in the pool is blind across the move and split in the
middle. S6a dies on one printed coprime split whose joint cohort misses a
prime one factor opens, or if the frozen witness prints without its 13.
S6b dies if parallel multiplicativity holds on every coprime split, or if
only one of the two directions of failure occurs. S7a dies on one printed
pair whose constructed q leaves the two readings equal, or whose two lambda
do not both land on q-1.

FINDINGS.

1. THE LEDGER CLOSES ON THE WHOLE GROWTH MONOID (theorem, proved for all N
   and all m; verified 23084/23084 moves, 13134 of them with omega(m) > 1).
   For every state and every move, with L = lambda(N) and e_l = v_l(m),

       G'(N, m) = W( lcm(L, lcm{ lambda(l^(c_l+e_l)) : l | m }) )
                  / ( W(L) * prod{ l^(e_l - min(e_l, v_l(V))) : l | m } ),
       c_l = v_l(W(L)) - v_l(V).

   THE STATE ENTERS THROUGH ITS LAMBDA AND ONE COORDINATE OF THE PROBE'S
   PERCEPT PER PRIME OF THE MOVE, and through nothing else. The suspicion
   that a composite move is irreducibly path-dependent -- that it HAS an
   intermediate state where a prime-power move has none -- is wrong, and
   the reason is worth more than the formula: the derivation never splits
   the move, so there is no intermediate state to refer to. An
   intermediate state is an artifact of the chain decomposition (finding
   4), not of the composite move, and the composite law is the prime-power
   law with the single lcm factor replaced by omega(m) of them. Worked
   row: N = 2 under m = 35 carries lambda 1 -> 12, opens the doors
   {3, 5, 7, 13}, takes the wall 2 -> 65520, pays 35 unpaid and returns a
   premium of 936. Findings 1 and 2 are the cheap half of this file -- one
   line of algebra past the prime-power law. Findings 3 to 7 are what the
   closure turned out to cost and to buy.

2. LAMBDA ALONE DECIDES EXACTLY ON THE MOVES COPRIME TO THE STATE
   (theorem; 1218/1218 cells, 2903 comparisons). When gcd(N, m) = 1 every
   c_l is 0 and the percept slice drops out, so G' is a function of (L, m)
   there -- the composite generalisation of the fresh-import law, and the
   only regime where lambda is GUARANTEED to suffice. The qualifier is the
   whole of it: elsewhere lambda usually still decides anyway (finding 3),
   so the scope word is ONLY and never EXACTLY, exactly as the prime-power
   law had it. Every battery cell holding two or more equal-lambda states
   coprime to the same composite m agrees.

3. THE PERCEPT SLICE IS TIGHT, AND ITS COMPRESSION DECAYS WITH omega(m)
   (theorem + measurement over the battery). The key (L, m, (v_l(V) : l|m))
   partitions the moves: 10775 distinct keys over 23084 moves, 12309 moves
   landing on a key another move already held, and 0 keys carrying two
   premiums. NO COORDINATE IS SPARE -- checked per prime rather than in
   aggregate, since the claim is about every one of them: all 10 primes
   that carry a coordinate in this battery are load-bearing somewhere.
   Dropping the whole slice leaves 1369 of 5800 (L, m) keys two-valued --
   which also says 76% of them are single-valued, so on composites as on
   repeats lambda alone USUALLY still happens to decide, and "usually" is
   not a law. Dropping ONE coordinate
   leaves 1939 of 10854 reduced keys two-valued, the damage concentrated at
   the small primes (915 of 2634 at v_3, 570 of 3083 at v_2, 31 of 672 at
   v_11). THE COST IS THE COMPRESSION: 3.05x at omega(m) = 1, 1.81x at 2,
   1.16x at 3. The law closes for every move, but as the move gathers
   primes its key approaches the state itself, and the probe's advantage
   over knowing N outright shrinks toward nothing.

4. ONLY THE WALL GAIN IS A STATE FUNCTION OF THE ENDPOINTS (theorem;
   52536/52536 splits). The wall gain is a ratio of two ENDPOINT values, so
   it telescopes by construction and the rig only confirms the
   divisibilities that make each factor an integer -- the content is that
   the unpaid part does NOT, and everything the premium inherits from it:

       G'(N, ab) = G'(N, a) * G'(Na, b) * gcd(ab, V(N))
                     / ( gcd(a, V(N)) * gcd(b, V(Na)) ).

   So the premium's path-dependence IS the unpaid part's, exactly and with
   nothing else in it. And since V(Nab) is ONE STATE either way, an
   inflated opening half arrives with an equally inflated spending half:
   THE GROSS FLOWS OF THE LEDGER ARE PATH-DEPENDENT AND ONLY THEIR QUOTIENT
   IS NOT. What a move "spends" and what it "opens" are therefore not
   properties of the move -- they are properties of the move together with
   the granularity it is watched at, which is finding 7's mechanism.

5. A SPLIT MOVE NEVER UNDERCOUNTS THE PREMIUM (theorem, proved prime by
   prime; 52536/52536 splits, the correction a unit fraction every time and
   exactly 1 on 50946 of them, 97.0%). With alpha = v_l(a), beta = v_l(b),
   v = v_l(V(N)) and v' = v_l(V(Na)) >= v - min(alpha, v), the claim
   min(alpha+beta, v) <= min(alpha, v) + min(beta, v') splits into
   alpha >= v, where the right side is already v, and alpha < v, where it
   is at least min(alpha+beta, v). So THE PREMIUM IS SUBMULTIPLICATIVE
   along every factorisation of the move, and it bites on 1590 splits.
   Equality holds exactly when, at every l | b, either v_l(G'(N,a)) = 0 or
   beta <= v - alpha -- the first step opens no l-door BELOW the exponent
   the second step is about to pay at -- 0 disagreements, which is sharper
   than "the first step opens no b-primes": an opening ABOVE the cap does
   not bite. THE ORIENTATION IS A REAL STATEMENT, not a convention: the
   inverted form, with the whole move's gcd in the denominator, fails on
   1590 splits -- necessarily the same 1590, since the two orientations
   agree exactly where the correction is 1, so this is the biting count
   read twice and not independent evidence.
   Smallest biting split: N = 2 with a = b = 2, where premiums
   6 and 1 chain to 6 while the move 4 pays 3, V running 1 -> 6 -> 3.

6. THE PRIMES OF A MOVE DO NOT DECOUPLE (theorem + measurement; 14726
   coprime splits, counted once per UNORDERED pair since the comparison is
   symmetric where section 4's paths are not). The cohort of a move, the
   primes it admits to the wall for the first time, is monotone in
   divisibility, so a joint cohort always contains its factors' (0
   exceptions) -- and it can contain MORE. At lambda = 1 the move 5 opens
   {3, 5} and the move 7 opens {3, 7}, but
   35 opens {3, 5, 7, 13}: lcm(4, 6) = 12 admits 13, WHICH NEITHER FACTOR
   ADMITS. AND THAT LOCATES THE INTERACTION EXACTLY. The move's lambda is
   an lcm, which is COORDINATEWISE MAX on the exponent vectors, so lambda
   itself decouples over the primes of the move; what does not is
   Doors(L) = {p : (p-1) | L}, a condition on the WHOLE of L rather than on
   any one exponent. A door opens for the join and for neither part exactly
   when p-1 needs factors from both -- 13-1 = 12 = 4*3, the 4 from
   lambda(5) and the 3 from lambda(7). So the interaction is not in the
   exponents but in the divisor condition that reads them together.
   BOTH DIRECTIONS OF FAILURE THEN FOLLOW FROM THE ONE FACT that the gain
   is a function of the LCM: whatever both factors reach ALONE, the join
   reaches once and the product claims twice (below), and whatever neither
   reaches alone but the join does, the join claims once and the product
   never (above). Measured, 12722 coprime splits hold, 1360 land ABOVE the
   product and 644 BELOW. The BELOW witness is its mechanism bare: at
   N = 2 with a = 2, b = 3 the move pays 2 against a product of 24, a
   ratio of 1/12, because both factors carry lambda 1 -> 2 alone and reach
   the SAME wall, so the product claims that one gain twice and no door
   interacts. The ABOVE witness carries BOTH: at N = 2 with a = 5, b = 7
   the joint premium 936 against a product of 864 is a ratio of 13/12, the
   interaction door 13 upward against a shared factor 12 downward, the door
   winning -- so "exceeds the product by the door it opens" is the
   direction and not the arithmetic, and the two mechanisms are generally
   both live in one split rather than sorting themselves into cases. The
   frozen design named the downward mechanism too narrowly, as a shared
   BUMP; a whole shared gain is the general case.
   So A MOVE'S PREMIUM IS NOT ASSEMBLED FROM ITS FACTORS' PREMIUMS -- the
   precise claim, weaker than "the ledger closes on no finer object" and
   the one all the witnesses support. It is finding 3's tightness seen from
   the other side, and the reason the slice cannot be traded for omega(m)
   one-prime laws.

7. SLOW MOTION BREAKS BLINDNESS FOR THE PROBE THAT CANNOT CHOOSE THE MOVE
   (measurement, N <= 1499, one representative pair per headroom class). Of
   986 (pair, move) cases where a composite move leaves a blind pair blind,
   56 -- 5.7% -- are split by some INTERMEDIATE reading; the pool is 96
   pairs against 41 splittable moves. Witness: N = 9 and N = 513 both read
   V = 56 and both still read V = 56 after the move 57, but the split at
   a = 3 reads 1064 against 56. ONE MOVE, TWO RESOLUTIONS, AND THE FINER
   ONE SEES MORE. The SCOPE is the whole content here and is easy to
   overstate: a probe that chooses its own moves ALREADY holds that
   information, because reading after a is the same act as playing the move
   a and stopping. What the measurement separates is choosing WHEN TO READ
   from choosing WHAT TO PLAY -- two faculties the word "observer" bundles
   -- and it says the first is worth something by itself: for a tower
   growing by a move the probe does not pick, a watcher who samples inside
   the move resolves states an endpoint-only watcher cannot. So finding 4's
   path-dependence is not bookkeeping, but it buys resolution only for the
   sampler, and 5.7% is the honest size of it -- a rare win, not a cure for
   blindness. AND THE GRANULARITY LADDER COLLAPSES AT ONE STEP (theorem,
   one line): every partial product of every ordered factorisation of m is
   a divisor of m, and conversely each divisor d is the intermediate of the
   single split (d, m/d), so the readings available at ANY depth are exactly
   { V(Nd) : d | m } -- a pair split by some chain is split by some ONE
   split. The sweep above ranges over every proper divisor, so 5.7% is the
   rate for ALL sampling granularities and not for two-step watching alone,
   and there is no depth hierarchy to measure. What survives is not depth
   but WHICH divisors resolve a given pair, and whether any pair resists all
   of them.

8. NO PAIR OF STATES IS BLIND UNDER EVERY MULTIPLIER (theorem, all blind
   pairs, resting on Dirichlet and on nothing weaker; verified 96/96 over
   the pool). For a blind pair the definition of the headroom gives
   W(lambda_i) = V*N_i, so the two WALLS DIFFER -- and a prime q = 1 mod
   lcm(lambda_1, lambda_2) drives BOTH states to lambda = q-1, which makes
   the walls AGREE at W(q-1) and the readings W(q-1)/(N_i q) differ. So the
   resolving set is NEVER EMPTY, and its member is constructed rather than
   searched for. PERMANENT BLINDNESS DOES NOT EXIST: every pair of distinct
   states the probe cannot tell apart can be told apart by choosing the
   right multiplier first. The construction is the injectivity of the probe
   on a lambda-fibre used CONSTRUCTIVELY -- rather than observing that a
   blind pair must carry distinct lambda, force the two lambda to coincide
   and read off the contradiction -- which is why it needs no conjecture:
   the one non-elementary ingredient is Dirichlet's theorem.
   It buys certainty and not economy: the constructed q runs to 111827 over
   the pool, while all 96 pairs are in fact resolved by some multiplier
   below 60 (smallest resolver 5 at the median, 11 at worst). So the
   interesting question was never WHETHER a pair can be resolved but which
   multipliers do it and how cheaply -- and finding 7's 5.7% is the honest
   measure of the WATCHER's much weaker position, since a watcher takes the
   move it is given and cannot go looking for this q.

SCOPE. Everything is exact integer arithmetic. The move battery is N in
2..399 with m in 2..59, which is the battery the prime-power law was
verified on, so the composite claim is measured where the one-prime claim
already stands. Splits run over every divisor a of m with 1 < a < m, which
counts the two orders of a factorisation separately because they are two
PATHS; section 6 compares a symmetric quantity and so keeps the coprime
splits with a < b only, one per unordered pair. The ten primes that carry a
percept coordinate in a composite move of this battery are the primes up to
29, a composite m <= 59 needing a cofactor of at least 2. The
blind-pair pool is N <= 1499, one representative pair per headroom class
(the two smallest members), against the composite moves of the battery.
Primality is deterministic Miller-Rabin over the standard base set, valid
below ~3.3e24; nothing tested here approaches that. What is PROVED for all N
and m rather than sampled: the composite closed form, the coprime case's
independence of the percept, the exact telescoping of the wall gain, the
chain rule and the sign of its correction with the equality criterion, and
the containment of a factor's cohort in the joint one, and the existence of
a resolver for every blind pair (Dirichlet). The key compression,
the tightness of the slice, the rates at which the correction and parallel
multiplicativity fail, and the slow-motion rate are measurements at the
stated caps and nothing is claimed beyond them.

RUN RECORD. Python 3, no third-party dependencies, 0.8 s wall clock, under
40 MB peak across runs. Seven sections, all checks pass. The positive control
runs first and the run aborts before any verdict is read if it fails; it
includes the new
closed form reproducing the established prime-power form on all 9950
one-prime moves of the battery, so the composite claim is anchored to the
law it generalises.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd

from explore_premium import (MOVE_M, MOVE_N, divisors, doors, factorint,
                             general_premium, headroom, is_prime, lam, lcm,
                             move_lam, premium_def, v_p, wall)

FAIL = []

POOL_CAP = 1500
BRUTE_CAP = 30000


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


# ------------------------------------------------------- the composite form

def percept_slice(N, m):
    """( v_l(V(N)) : l | m ) -- one coordinate of the reading per prime of
    the move, and the only thing about the state the closed form may see
    besides lambda."""
    V = headroom(N)
    return {l: v_p(V, l) for l in factorint(m)}


def composite_premium(L, pslice, m):
    """The premium of ANY move m on a state of lambda L whose percept slice
    at the primes of m is pslice.

    The state is reachable only through L and pslice -- N is not a
    parameter. Each prime of m carries the state's l-part from l^c to
    l^(c+e) with c = v_l(W(L)) - v_l(V), and the wall is evaluated once at
    the lcm of L with all omega(m) of the moved lambdas.
    """
    WL = wall(L)
    Lp, unpaid = L, 1
    for l, e in factorint(m).items():
        Vl = pslice[l]
        c = v_p(WL, l) - Vl
        assert c >= 0, "the slice is not a reading of any state at l=%d" % l
        Lp = lcm(Lp, move_lam(l, c + e))
        unpaid *= l ** (e - min(e, Vl))
    gain = wall(Lp)
    assert gain % WL == 0, "the wall fell at (L,m)=(%d,%d)" % (L, m)
    gain //= WL
    assert gain % unpaid == 0, "the unpaid part does not divide the gain" \
        " at (L,m)=(%d,%d)" % (L, m)
    return gain // unpaid


def move_key(N, m):
    """( L, m, (l, e_l, v_l(V)) sorted ) -- all the closed form reads."""
    ps = percept_slice(N, m)
    return (lam(N), m,
            tuple(sorted((l, e, ps[l]) for l, e in factorint(m).items())))


def splits(m):
    """Every factorisation m = a*b with both parts above 1."""
    return [(a, m // a) for a in divisors(m) if 1 < a < m]


def omega(m):
    return len(factorint(m))


# ---------------------------------------------------------------- S1 control

def s1_control():
    print("S1 POSITIVE CONTROL")
    lam_tab = [lam(n) for n in range(0, BRUTE_CAP + 1)]
    fit = [L for L in sorted({lam(N) for N in MOVE_N})
           if wall(L) <= BRUTE_CAP]
    bad = 0
    for L in fit:
        brute = max(n for n in range(1, BRUTE_CAP + 1) if L % lam_tab[n] == 0)
        if brute != wall(L):
            bad += 1
            if bad == 1:
                print("  wall mismatch at L=%d: formula %d brute %d"
                      % (L, wall(L), brute))
    check(bad == 0, "wall() disagrees with brute force on %d of %d lambda"
          % (bad, len(fit)))
    print("  wall() = the largest modulus with lambda | L on %d/%d lambda"
          " fitting under %d" % (len(fit) - bad, len(fit), BRUTE_CAP))

    ok = (premium_def(16, 2) == 1 and headroom(16) == 15
          and headroom(32) == 15 and lam(16) == 4 and lam(32) == 8)
    check(ok, "the (16, 2) witness does not come back")
    print("  N=16 m=2: G' = %d, V %d -> %d, lambda %d -> %d"
          % (premium_def(16, 2), headroom(16), headroom(32), lam(16),
             lam(32)))
    check(headroom(3) == 8 and headroom(48) == 5,
          "the (3, 16) witness does not come back")
    print("  N=3  m=16: V %d -> %d" % (headroom(3), headroom(48)))
    check(headroom(10) == headroom(11) == 24 and headroom(50) == 264
          and headroom(55) == 240, "the (10, 11) pair does not come back")
    print("  N=10, N=11: V %d = %d, one push of 5 sends them to %d and %d"
          % (headroom(10), headroom(11), headroom(50), headroom(55)))

    n = bad = red = 0
    for N in MOVE_N:
        L, V = lam(N), headroom(N)
        for m in MOVE_M:
            if omega(m) != 1:
                continue
            (l, e), = factorint(m).items()
            n += 1
            f = composite_premium(L, {l: v_p(V, l)}, m)
            if f != premium_def(N, m):
                bad += 1
            if f != general_premium(L, v_p(V, l), l, e):
                red += 1
    check(bad == 0, "the composite form disagrees with the definitional G'"
          " on %d of %d one-prime moves" % (bad, n))
    print("  composite form = definitional G' on %d/%d moves with"
          " omega(m) = 1" % (n - bad, n))
    check(red == 0, "the composite form fails to collapse onto the"
          " prime-power expression %d times" % red)
    print("  and collapses onto the established prime-power expression on"
          " all of them -- a check")
    print("    on this file's code path, not on the mathematics: for one"
          " prime they are one formula")
    print()


# ------------------------------------------------- S2 the composite form

def s2_composite_form():
    print("S2 THE COMPOSITE CLOSED FORM")
    n = bad = comp = 0
    for N in MOVE_N:
        L = lam(N)
        for m in MOVE_M:
            g = premium_def(N, m)
            f = composite_premium(L, percept_slice(N, m), m)
            n += 1
            if omega(m) > 1:
                comp += 1
            if f != g:
                bad += 1
                if bad == 1:
                    print("  mismatch at N=%d m=%d: closed form %d actual %d"
                          % (N, m, f, g))
    check(bad == 0, "the composite form fails on %d of %d moves" % (bad, n))
    print("  closed form = definitional G' on %d/%d moves, %d of them with"
          " omega(m) > 1" % (n - bad, n, comp))

    # A worked row, small enough to read: the two primes of the move raise
    # lambda to their own lcm, and the wall is evaluated there once.
    N, m = 2, 35
    print("  worked row: N=%d, m=%d -- lambda %d -> %d opens the doors %s,"
          % (N, m, lam(N), lam(N * m),
             sorted(doors(lam(N * m)) - doors(lam(N)))))
    print("    the wall goes %d -> %d, the move pays %d unpaid, and the"
          " premium is %d"
          % (wall(lam(N)), wall(lam(N * m)),
             m // gcd(m, headroom(N)), premium_def(N, m)))

    # S2b: on a move COPRIME to the state every c_l vanishes, so lambda
    # alone should decide. Measured over lambda classes, the same way the
    # fresh-import law was.
    by_lam = {}
    for N in MOVE_N:
        by_lam.setdefault(lam(N), []).append(N)
    cells = agree = comparisons = 0
    for L, ns in by_lam.items():
        if len(ns) < 2:
            continue
        for m in MOVE_M:
            if omega(m) < 2:
                continue
            grp = [N for N in ns if gcd(N, m) == 1]
            if len(grp) < 2:
                continue
            cells += 1
            comparisons += len(grp) - 1
            if len({premium_def(N, m) for N in grp}) == 1:
                agree += 1
    check(agree == cells, "lambda fails to decide on %d of %d coprime"
          " composite cells" % (cells - agree, cells))
    print("  on a move COPRIME to the state c_l = 0 at every prime, and"
          " lambda alone decides:")
    print("    %d/%d (lambda, m) cells with two or more coprime states"
          " agree, %d comparisons" % (agree, cells, comparisons))
    print()


# --------------------------------------------- S3 how much percept is needed

def s3_key_and_tightness():
    print("S3 HOW MUCH PERCEPT AN ASCENT NEEDS")
    full, no_slice, dropped = {}, {}, {}
    by_omega = {}
    for N in MOVE_N:
        L, V = lam(N), headroom(N)
        for m in MOVE_M:
            g = premium_def(N, m)
            fac = factorint(m)
            key = move_key(N, m)
            hit = full.setdefault(key, [set(), 0])
            hit[0].add(g)
            hit[1] += 1
            w = len(fac)
            tally = by_omega.setdefault(w, [set(), 0])
            tally[0].add(key)
            tally[1] += 1
            no_slice.setdefault((L, m), set()).add(g)
            if w > 1:
                for l in fac:
                    rk = (L, m, tuple(sorted((l2, v_p(V, l2))
                                             for l2 in fac if l2 != l)))
                    dropped.setdefault((l, rk), set()).add(g)

    coll = [k for k, hit in full.items() if len(hit[0]) > 1]
    multi = sum(hit[1] - 1 for hit in full.values() if hit[1] > 1)
    check(not coll, "%d full keys carry two premiums" % len(coll))
    print("  %d distinct keys over %d moves; %d moves land on a key another"
          " move already" % (len(full), sum(h[1] for h in full.values()),
                             multi))
    print("    held, and %d keys carry two premiums" % len(coll))
    for w in sorted(by_omega):
        keys, moves = by_omega[w]
        print("    omega(m) = %d: %5d moves, %5d distinct keys,"
              " compression %.2fx" % (w, moves, len(keys),
                                      moves / len(keys)))

    two_valued = sum(1 for s in no_slice.values() if len(s) > 1)
    print("  DROPPING THE WHOLE SLICE: %d of %d (lambda, m) keys carry two"
          " premiums" % (two_valued, len(no_slice)))
    check(two_valued > 0, "lambda and m alone already determine the premium")
    per_prime = {}
    for (l, _), s in dropped.items():
        tally = per_prime.setdefault(l, [0, 0])
        tally[0] += len(s) > 1
        tally[1] += 1
    hurt = sum(t[0] for t in per_prime.values())
    tot = sum(t[1] for t in per_prime.values())
    print("  DROPPING ONE COORDINATE (composite moves only): %d of %d"
          " reduced keys carry" % (hurt, tot))
    print("    two premiums")
    check(hurt > 0, "every dropped-coordinate key is single-valued -- the"
          " slice is redundant")
    # "No coordinate is spare" is a claim about EVERY prime, so the primes
    # whose coordinate never matters are counted rather than assumed away.
    spare = sorted(l for l, t in per_prime.items() if t[0] == 0)
    print("    the coordinate is load-bearing somewhere at %d of the %d"
          " primes carrying one;" % (len(per_prime) - len(spare),
                                     len(per_prime)))
    print("    the spare ones, whose coordinate never matters, are %s"
          % (spare if spare else "none"))
    for l in sorted(per_prime)[:6]:
        bad, tot_l = per_prime[l]
        print("    dropping v_%-2d(V): %4d of %4d reduced keys split"
              % (l, bad, tot_l))
    print()


# ------------------------------------------------ S4 the chain rule's defect

def s4_chain_defect():
    print("S4 THE CHAIN RULE AND ITS DEFECT")
    n = telescope_bad = ident_bad = inverted_bad = 0
    sign_bad = crit_bad = tight = 0
    witness = None
    for N in MOVE_N:
        V = headroom(N)
        W0 = wall(lam(N))
        for m in MOVE_M:
            for a, b in splits(m):
                n += 1
                Na = N * a
                Va = headroom(Na)
                if wall(lam(N * m)) // W0 != \
                        (wall(lam(Na)) // W0) * (wall(lam(N * m))
                                                 // wall(lam(Na))):
                    telescope_bad += 1
                gab, ga, gb = premium_def(N, m), premium_def(N, a), \
                    premium_def(Na, b)
                num, den = gcd(m, V), gcd(a, V) * gcd(b, Va)
                if gab * den != ga * gb * num:
                    ident_bad += 1
                    if ident_bad == 1:
                        print("  identity fails at N=%d a=%d b=%d: %d*%d"
                              " vs %d*%d*%d" % (N, a, b, gab, den, ga, gb,
                                                num))
                if gab * num != ga * gb * den:
                    inverted_bad += 1
                if den % num:
                    sign_bad += 1
                elif den == num:
                    tight += 1
                elif witness is None:
                    witness = (N, a, b, ga, gb, gab, den // num)
                crit = all(v_p(ga, l) == 0
                           or v_p(b, l) <= v_p(V, l) - v_p(a, l)
                           for l in factorint(b))
                if crit != (den == num):
                    crit_bad += 1
                    if crit_bad == 1:
                        print("  criterion disagrees at N=%d a=%d b=%d:"
                              " criterion %s, correction %s"
                              % (N, a, b, crit, "1" if den == num
                                 else "1/%d" % (den // num)))
    check(telescope_bad == 0, "the wall gain fails to telescope on %d of %d"
          " splits" % (telescope_bad, n))
    print("  the WALL GAIN is a ratio of ENDPOINT values, so it telescopes"
          " by construction and")
    print("    this confirms only the divisibilities (%d/%d): the defect"
          " sits in the unpaid part" % (n - telescope_bad, n))
    check(ident_bad == 0, "the chain identity fails on %d of %d splits"
          % (ident_bad, n))
    print("  the chain identity holds on %d/%d splits with the WHOLE move's"
          " gcd in the" % (n - ident_bad, n))
    print("    numerator; the inverted orientation fails on %d of them"
          % inverted_bad)
    check(inverted_bad > 0, "the inverted orientation never fails, so the"
          " two are the same statement")
    check(sign_bad == 0, "the correction is not a unit fraction on %d of %d"
          " splits" % (sign_bad, n))
    print("  the correction is 1/(a positive integer) on %d/%d splits --"
          " A SPLIT MOVE NEVER" % (n - sign_bad, n))
    print("    UNDERCOUNTS -- and it is exactly 1 on %d of them (%.1f%%),"
          " so it bites on %d" % (tight, 100.0 * tight / n, n - tight))
    check(crit_bad == 0, "the equality criterion disagrees on %d of %d"
          " splits" % (crit_bad, n))
    print("  the equality criterion agrees on %d/%d splits: the defect"
          " appears exactly when the" % (n - crit_bad, n))
    print("    first step opens an l-door below the exponent the second"
          " step pays at")
    if witness:
        N, a, b, ga, gb, gab, d = witness
        print("  smallest biting split: N=%d, a=%d, b=%d -- premiums %d and"
              " %d chain to %d," % (N, a, b, ga, gb, ga * gb))
        print("    the whole move pays %d, a factor of %d less; V %d -> %d"
              " -> %d" % (gab, d, headroom(N), headroom(N * a),
                          headroom(N * a * b)))
    print()


# --------------------------------------------------------- S5 slow motion

def s5_slow_motion():
    print("S5 SLOW MOTION AS A RESOLUTION KNOB")
    by_V = {}
    for N in range(2, POOL_CAP):
        by_V.setdefault(headroom(N), []).append(N)
    pairs = [(ns[0], ns[1]) for ns in by_V.values() if len(ns) > 1]
    comps = [m for m in MOVE_M if splits(m)]
    blind_after = split_midway = 0
    witness = None
    for N1, N2 in pairs:
        for m in comps:
            if headroom(N1 * m) != headroom(N2 * m):
                continue
            blind_after += 1
            for a, _ in splits(m):
                if headroom(N1 * a) != headroom(N2 * a):
                    split_midway += 1
                    if witness is None:
                        witness = (N1, N2, m, a)
                    break
    print("  %d blind pairs (one representative per headroom class) below"
          " %d, against %d" % (len(pairs), POOL_CAP, len(comps)))
    print("    splittable moves: %d (pair, move) cases stay blind across"
          " the whole move," % blind_after)
    print("    and %d of those (%.1f%%) are split by some INTERMEDIATE"
          " reading" % (split_midway,
                        100.0 * split_midway / max(1, blind_after)))
    print("    the split points swept are EVERY proper divisor of the move,"
          " which is every reading")
    print("    any chain of any depth could offer -- so this rate is not"
          " the two-step rate")
    check(split_midway > 0, "no blind pair is split by an intermediate"
          " reading -- the path-dependence is invisible to the probe")
    if witness:
        N1, N2, m, a = witness
        print("  witness: N=%d and N=%d both read V = %d; under m = %d they"
              " land on V = %d" % (N1, N2, headroom(N1), m,
                                   headroom(N1 * m)))
        print("    together, but the split at a = %d reads %d against %d --"
              " one move, two" % (a, headroom(N1 * a), headroom(N2 * a)))
        print("    resolutions, and the finer one sees more")
    print()


# ------------------------------------------------ S6 the primes interact

def cohort(N, m):
    """The primes the move admits to the wall for the first time."""
    return doors(lam(N * m)) - doors(lam(N))


def s6_interaction():
    print("S6 THE PRIMES OF A MOVE INTERACT")
    joint = cohort(1, 35)
    ca, cb = cohort(1, 5), cohort(1, 7)
    print("  at lambda = 1: the move 5 opens %s, the move 7 opens %s,"
          % (sorted(ca), sorted(cb)))
    print("    and the move 35 opens %s -- lcm(4, 6) = 12 admits 13, which"
          " neither factor" % sorted(joint))
    print("    admits, because 13-1 = 12 = 4*3 needs the 4 from one factor"
          " and the 3 from the other:")
    print("    lambda is an lcm and so decouples over the move's primes,"
          " while Doors reads a")
    print("    divisibility of the WHOLE lambda -- the interaction lives"
          " there and nowhere else")
    check(13 in joint and 13 not in ca and 13 not in cb,
          "the frozen interaction witness does not print")

    n = miss = eq = over = under = 0
    first_over = first_under = None
    for N in MOVE_N:
        for m in MOVE_M:
            for a, b in splits(m):
                if gcd(a, b) != 1 or a > b:
                    continue          # a > b is the same UNORDERED pair
                n += 1
                if not cohort(N, m) >= (cohort(N, a) | cohort(N, b)):
                    miss += 1
                gab = premium_def(N, m)
                prod = premium_def(N, a) * premium_def(N, b)
                if gab == prod:
                    eq += 1
                elif gab > prod:
                    over += 1
                    if first_over is None:
                        first_over = (N, a, b, gab, prod)
                else:
                    under += 1
                    if first_under is None:
                        first_under = (N, a, b, gab, prod)
    check(miss == 0, "the joint cohort misses a factor's cohort on %d of %d"
          " coprime splits" % (miss, n))
    print("  the joint cohort contains both factors' cohorts on %d/%d"
          " unordered coprime splits" % (n - miss, n))
    print("  PARALLEL multiplicativity, G'(N,ab) = G'(N,a)*G'(N,b), over"
          " those %d splits:" % n)
    print("    %d hold, %d have the joint premium ABOVE the product, %d"
          " BELOW it" % (eq, over, under))
    check(over > 0 and under > 0, "parallel multiplicativity fails in only"
          " one direction")
    if first_over:
        N, a, b, gab, prod = first_over
        print("    smallest ABOVE: N=%d, a=%d, b=%d -- jointly %d against a"
              " product of %d," % (N, a, b, gab, prod))
        print("      driven by the doors the joint lcm opens and neither"
              " factor does: %s"
              % sorted(cohort(N, a * b) - cohort(N, a) - cohort(N, b)))
        print("      (the ratio, not the door itself: both mechanisms are"
              " live in one split)")
    if first_under:
        N, a, b, gab, prod = first_under
        print("    smallest BELOW: N=%d, a=%d, b=%d -- jointly %d against a"
              " product of %d," % (N, a, b, gab, prod))
        print("      the shortfall being a gain both factors reach ALONE,"
              " claimed twice by the")
        print("      product and once by the move")
    print("  so the PREMIUM does not decouple over the move's primes even"
          " though lambda does:")
    print("    a move's premium is not assembled from the premiums of its"
          " factors")
    print()


# --------------------------------------------- S7 is any pair blind forever

def blind_pairs(cap):
    """One representative pair per headroom class below the cap: the two
    smallest members, which is the convention the blind-class census uses."""
    pool = {}
    for N in range(2, cap):
        pool.setdefault(headroom(N), []).append(N)
    return [(v[0], v[1]) for v in pool.values() if len(v) > 1]


def forced_resolver(N1, N2):
    """The least prime q = 1 mod lcm(lambda(N1), lambda(N2)) coprime to both.

    Multiplying by it drives BOTH states to lambda = q-1, so their walls
    coincide and their readings cannot.
    """
    L = lcm(lam(N1), lam(N2))
    q = L + 1
    while not (is_prime(q) and N1 % q and N2 % q):
        q += L
    return q


def s7_no_permanent_blindness():
    print("S7 IS ANY PAIR BLIND FOREVER?")
    pairs = blind_pairs(POOL_CAP)
    bad = biggest = 0
    least = []
    for N1, N2 in pairs:
        q = forced_resolver(N1, N2)
        biggest = max(biggest, q)
        if not (lam(N1 * q) == lam(N2 * q) == q - 1
                and headroom(N1 * q) != headroom(N2 * q)):
            bad += 1
            if bad == 1:
                print("  the constructed resolver fails at N=%d, N=%d, q=%d"
                      % (N1, N2, q))
        d = next((d for d in range(2, 60)
                  if headroom(N1 * d) != headroom(N2 * d)), None)
        if d:
            least.append(d)
    check(bad == 0, "the constructed resolver fails on %d of %d pairs"
          % (bad, len(pairs)))
    print("  every one of the %d blind pairs below %d is resolved by the"
          " prime q = 1 mod" % (len(pairs), POOL_CAP))
    print("    lcm(lambda_1, lambda_2), which drives BOTH states to"
          " lambda = q-1 so their walls")
    print("    coincide and their readings cannot: NO PAIR IS BLIND UNDER"
          " EVERY MULTIPLIER")
    print("  the construction buys certainty, not economy -- the largest q"
          " it needs here is %d," % biggest)
    print("    while %d of the %d pairs are already resolved by some"
          " multiplier under 60" % (len(least), len(pairs)))
    if least:
        print("    (smallest resolver: %d at the median, %d at worst)"
              % (sorted(least)[len(least) // 2], max(least)))
    print()


# ------------------------------------------------------------------ the run

def main():
    s1_control()
    if FAIL:
        print("POSITIVE CONTROL FAILED -- no verdict is read.")
        return 1
    s2_composite_form()
    s3_key_and_tightness()
    s4_chain_defect()
    s5_slow_motion()
    s6_interaction()
    s7_no_permanent_blindness()
    if FAIL:
        print("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("all sections pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
