# BRIDGES — where growth meets open number theory

The object: the places where a growth world of GROWTH.md meets a
question about primes, most of them configurations that exist iff a
prime p exists with p − 1 of a prescribed multiplicative shape. A world
grows its modulus by the least multiplier its demand admits: the
transparency demand admits one that leaves λ fixed, the dynamics demand
one that raises λ, the independence demand one coprime to the modulus;
the transparency demand's walk dies at the wall, the largest modulus
whose λ divides the current λ. The bridges concern the alphabet worlds,
which fill to the wall and then push a prime of a fixed set S, the
phoenix among them; the
values the odd part of λ can take, λ(M) the exponent of the unit group
of Z/M (the Carmichael function); and the tower read by the
transparency demand. This page asks which of these bridges are exact
equivalences, which run one way, and which rest on a proved theorem
rather than an open one. Its verifier is bridges.py, which also checks
instances of GROWTH.md's steering of a state onto a prime by a single
multiplication (GROWTH.md#the-lock-prime-law): 200 states onto 2, and
five states each onto 3, 5, 7, 13 and 17, each run watched for the 30
greedy picks after the multiplication (any move at a prime above the
target costs more than the target, so the run scans the primes up to
it).

The answer, in one line: two bridges are exact equivalences resting on
open questions, the seating law on primes with p − 1 of a prescribed
shape and the atoms (which odd h is the odd part of some λ(M), built
from the odd parts of λ at odd prime powers) on primes h′·2^b + 1, h′
dividing h, whose least failure is, on the published record, the least
prime Sierpiński number; two run one way, the lock into Dirichlet's
theorem and so proved, the cascade closed wherever a known covering
kills infinitely many dead levels and open past that (each argued on its
own page, GROWTH.md and CASCADE.md); and one is a proved density theorem
(TOWER.md#the-density-theorem), an upper bound on the rungs that move λ
whose matching lower bound is open.

| bridge | growth side | number-theory side | direction | status |
|---|---|---|---|---|
| the lock | every prime is some seed's lock (GROWTH.md#the-lock-prime-law) | a prime ≡ 1 (mod B) and ≢ 1 modulo the prime locked onto, B the lcm the lock-prime law builds from the primes up to that prime, prime to it | one way, into Dirichlet | proved |
| the seating law | an alphabet world (BRIDGES.md#the-seating-law) seats infinitely many primes | infinitely many primes p with (p − 1)_S′ dividing F, n_S′ the part of n prime to S and F that part of lcm(λ(seed), q − 1 : q ∈ S); from seed 1 with every q − 1 S-smooth, infinitely many with p − 1 S-smooth | equivalence, per seed and alphabet | open: Fermat at {2}, Pierpont at {2, 3} |
| the atoms | an odd h is the odd part of some λ(M) | for each l^j ‖ h, a divisor h′ of h with v_l(h′) = j and h′·2^b + 1 prime, up to a finite correction | equivalence | the least h that is not: the least prime Sierpiński number, on the published record; open |
| the cascade | every ideal-world trajectory of a number ring locks (CASCADE.md#dead-levels-recur-at-eleven-characteristics) | infinitely many dead levels at one rank-1 characteristic, a prime with an unramified place over it whose norm is that prime | one way, sufficient | proved at a ring with a rank-1 characteristic among the eleven primes with a known covering of their levels' candidates, 2 by a covering of its own and 3, 5, 7, 11, 13, 17, 19, 23, 31 and 37 (odd characteristics below 1000 searched, covering primes below 2,000 modulo which the characteristic's order divides 5,040); open in general |
| the density | the transparency demand admits almost every move of independence's walk | TOWER.md#the-density-theorem | none needed | proved |

A one-way reduction into a theorem settles its growth side, and calling
it an equivalence would add only that two true statements imply each
other; an equivalence settles nothing until its number-theory side is
settled. The lock and the cascade live on GROWTH.md and CASCADE.md; this
page holds the other three.

## The seating law
Tier: theorem; observation (the seat counts below 10⁶).
Verifier: proof; bridges.py::section_w.

An **alphabet world** starts at a seed s and repeats two phases: it
fills, by the transparency demand's greedy walk, which dies at exactly
the wall W(λ(M)) (GROWTH.md#the-three-fates), and then a **push** takes
the least λ-raising move at one prime in a finite set S, its alphabet,
under any schedule that pushes every letter infinitely often. Its seats
are the primes that ever divide its state. Write n_S′ for the part of n
prime to S. Then

    seats(s, S) = {p prime : (p − 1)_S′ divides F},
    F = (lcm(λ(s), q − 1 : q ∈ S))_S′,

whatever the schedule. Fills leave λ fixed, and at the wall an odd prime
r is seated iff (r − 1) | λ, at depth v_r(λ) + 1. So a push of an
unseated letter q opens it and takes the lcm of λ with (q − 1)_S′ once;
a push of a seated letter q deepens it by one and adds one factor q and
nothing prime to S, since (q − 1) | λ already; a push of 2 adds one
factor 2. Once every letter has been pushed, λ's part prime to S is F
forever and its part at every letter diverges, and the seats are the
union of the walls' supports. An odd seat p outside S ends at depth
v_p(F) + 1, and 2 outside S at v₂(F) + 2, v₂(F) being at least 1 since S
then holds an odd letter. Nine alphabets from seed 1, and {2} and {2, 3}
from each of the seeds 7, 11, 65 and 105, are run under a round-robin
and a random schedule on λ alone, each fill read as its wall: at the 489
steps with λ ≤ 10⁶ the wall built from its primes carries that λ, and λ
of it times its least move is the next step. The final λ's part prime to
S is then F by construction, and the seats below 10⁶ after 25 pushes per
letter match the predicate, a match that reads only that 25 pushes per
letter carry every seat below 10⁶.

When every q − 1 with q ∈ S is S-smooth, F is λ(s)_S′, and from seed 1
the seats are exactly the primes p with p − 1 S-smooth: the world seats
infinitely many primes iff there are infinitely many such primes. That
is Fermat's question at S = {2} and Pierpont's at {2, 3}, one question
per alphabet, each a Π₂ statement (for every bound, some seat past it).
Below 10⁶ the seats number 6 at {2}, the count unchanged since 65537,
against 42 at {2, 3}, 141 at {2, 3, 5} and 324 at {2, 3, 5, 7}. An
alphabet without 2 bounds the power of 2 in p − 1: from seed 1, S = {3}
has F = 2, so its seats are 2 and the primes 2·3^b + 1, 3 among them,
each such p − 1 carrying exactly one factor 2; from seed 1, S = {2, 11}
has F = 5, seating 41 and not 101. Another seed moves F: S = {3} from
seed 5 has F = 4 and seats 13.

## The phoenix
Tier: theorem; observation (the walls below 2·10⁷).
Verifier: proof; bridges.py::section_p.

The **phoenix** is the alphabet world S = {2}. At a wall every move
raises λ, so the least move there is 2, which is the dynamics demand's
own greedy pick: the phoenix is the single greedy law "the least move
the transparency demand admits, else the least move", with no choice
left to an operator. From seeds 1, 7 and 11 that law meets 15 walls in
all below 2·10⁷, each equal to W(λ). Its F is odd(λ(s)), the odd part of
λ(s), fixed at birth, so its seats are the spectrum of that odd number,
where

    spectrum(h) = {p prime : odd(p − 1) divides h},

and the spectrum only grows along divisibility, so every phoenix seats
spectrum(1), which is 2 and the Fermat primes. The seed-1 phoenix seats
3, 5, 17, 257 and 65537 as v₂(λ) reaches 1, 2, 4, 8 and 16, and 2^j + 1
is composite for every other j with 1 ≤ j ≤ 40. Its seats being
spectrum(1), it seats infinitely many primes iff there are infinitely
many Fermat primes. From seed 1, the least move that restarts a
transparency walk at its wall seats exactly 2 and the Fermat primes;
from a seed with odd(λ(s)) = h it seats spectrum(h), which at h = 3
(seed 7) adds 7, 13, 97, 193, 769, …

## The atom criterion
Tier: criterion (proved both ways; every odd h ≤ 999 realized by a
built modulus).
Verifier: proof; bridges.py::section_a, bridges.py::section_s,
bridges.py::section_c.

λ(M) is the lcm of λ(q^a) over q^a ‖ M, and the odd part of an lcm is
the lcm of the odd parts, so odd(λ(M)) is the lcm of the atoms
q^(a−1)·odd(q − 1) over the odd q^a ‖ M, the prime 2 contributing
nothing. An odd h is realizable when it is odd(λ(M)) for some M, and it
is realizable iff every prime power l^j ‖ h is served by an atom that
divides h and carries l exactly to the power j. Only if: the lcm reaches
l^j at some atom, and every atom divides h. If: keep each serving
atom's q^a, the largest a per q, which is itself a serving atom since
the atom grows with a; the product of those powers has odd(λ) = h.

An atom equals h iff h·2^b + 1 is prime for some b ≥ 1, or
h = q^(a−1)·odd(q − 1) with a ≥ 2 and q | h, which is a finite check. So
what one prime power can write is that primality predicate with a finite
correction, and realizability is a search over primes h′·2^b + 1 at the
divisors h′ of h, with that correction. Every odd h ≤ 999 is realized;
47 needs b = 583 and 881 needs 1027, each the least b that works, while
383 has none at b ≤ 1000 and is realized at b = 6393, 383·2⁶³⁹³ + 1
certified prime by Proth's theorem. A covering set turns the search's
failure into a proof. 78557 has the covering set
{3, 5, 7, 13, 19, 37, 73} of period 36, so no prime q has
odd(q − 1) = 78557, and neither 17^(a−1) nor 4621^(a−1)·1155 equals it,
so no prime power writes it, yet it is 17·4621 and two primes realize
it: odd(λ(137·18927617)) = 78557, where 137 = 17·2³ + 1 and
18927617 = 4621·2¹² + 1.

## The least unrealizable odd number
Tier: rule (proved; the search to b ≤ 1000 an observation, the nine
open primes the published record's).
Verifier: bridges.py::section_a, bridges.py::section_s.

An odd h is a Sierpiński number when h·2^b + 1 is composite for every b ≥ 1. If
l^j ‖ h is unserved, then l^j itself is no atom, and l^j is an atom iff
l^j·2^b + 1 is prime for some b or l is a Fermat prime. So an
unrealizable h has a prime-power divisor l^j ‖ h, with l not a Fermat
prime, that is Sierpiński, and such an l^j is itself unrealizable, since
the only divisor of l^j carrying l to the power j is l^j. The least odd
number that is never the odd part of λ(M) is therefore the least
Sierpiński prime power of non-Fermat base.

271129 is prime and Sierpiński, with the covering set
{3, 5, 7, 13, 17, 241} of period 24, and 271128 = 2³·3·11·13·79 is no
power of 2, so no M has odd(λ(M)) = 271129: it bounds the least
unrealizable odd number. Below it lie 23,844 odd prime powers l^j of
non-Fermat base; for 278 no l^j·2^b + 1 is prime at b ≤ 1000, the
survivors below 1000 are exactly 383 and 881, and the one proper power
among them, 143641 = 379², resolves at b = 1212, certified by Proth's
theorem. The rest is the prime Sierpiński problem by another name: the
published record of known primes k·2^b + 1 (W. Keller, The Sierpiński
Problem: Definition and Status, prothsearch.com/sierp.html, updated
2026-07-29) settles every other prime survivor and leaves open, among the
prime powers below 271129, exactly the nine primes 22699, 67607, 79309,
79817, 152267, 156511, 222113, 225931 and 237019, all survivors of the
search here. So on that record
the least odd number that is never the odd part of λ(M) IS the least
prime Sierpiński number: one of the nine or 271129, which 271129 is
exactly when the prime Sierpiński problem closes as conjectured.

## Transparent rungs are transparent moves
Tier: property.
Verifier: proof; bridges.py::section_t.

λ(Mp) = lcm(λ(M), p − 1) for a prime p not dividing M, so rung k of the
tower is transparent (TOWER.md#the-transparency-criterion) iff p_k is a
move the transparency demand admits at p_(k−1)#, and the tower is the
greedy independence walk from 1 (GROWTH.md#the-three-fates). The density
theorem therefore says that along independence's walk the transparency
demand admits almost every move: one walk, two demands, agreeing on a
set of density 1. Up to k = 2000 the demand admits 1531 of the 1999
moves.
