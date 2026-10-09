# MEMORY — what a grown world can know of its genesis

The object: the thermal growth walks of THERMAL.md seen from inside. A
world's **generator** is its demand and its inverse temperature β, grown
from seed 1 unless stated. An observer is handed one of four views: the
state N, the **dated state** (N and its move count τ), the watched path, or
a probe asking whether a proposed move m is admissible. This page asks
what each view carries about the generator and about the route, the
order the moves came in, and how the answer depends on the fate the
demand grows. Its verifier is memory.py; the witness gap and the
fossil (a dated state keeping all the path's evidence on its
generator, MEMORY.md#the-fossil-paradox) are computed exactly on a
**truncated world**, which draws its moves from 2 to 12 (the moves its
demand admits there), whose seed is 1, and where a state with no
admissible move stays put, a step of weight 1.

The demands are THERMAL.md's independence (m coprime to N,
THERMAL.md#the-zeta-measure) and dynamics (λ(Nm) > λ(N),
THERMAL.md#the-hot-limit-is-ẑ), plus two read only in the cold
blindness below: semisimplicity (Nm squarefree) and GROWTH.md's new
idempotents (m has a prime factor not dividing N). The independence
world is the one independence grows, of fate BREADTH (GROWTH.md), its
limit the zeta measure; its β = ∞ limit is the crystal (the zeta
measure and the crystal: THERMAL.md#the-zeta-measure), and
**cold genesis** is growth by the greedy walk, β = ∞. The DEPTH world,
of fate DEPTH, is the column 3^t,
the chain of the integers mod 3^t (GROWTH.md), that greedy dynamics
grows from seed 1 (GROWTH.md#the-lock-prime-law). A world's
**menu** at a state is the set of moves it may take there, and a
one-window world has the menu {3^a : a ≥ 1} at every state; the
fossil's information is also computed on it with the menu untruncated,
at τ ≤ 4, the law of the depth summed below 600. The answer,
in one line: a state is a lossy code for its own history, and what it
loses is exactly what the normalizers along the route carry (theorem);
so the independence world bounds the evidence for its genesis against
any given temperature, greedy depth gains evidence against thermal
dynamics at a rate asymptotically linear in depth, a watcher keeps
what a dated state drops, at zero temperature from a squarefree seed a
probe reads what no watcher can, and the one-window world, whose dated
state loses nothing, has a maximally unreadable route (theorems).

## The route-weight cancellation
Tier: theorem.
Verifier: proof; memory.py::section_r.

A history from seed s to N is an ordered factorization N/s = m₁⋯m_τ into
moves admissible along the way, and its probability is ∏ m_i^−β / Ψ over
the states it passes, which is (N/s)^−β ∏ 1/Ψ, Ψ being a state's
normalizer, the sum of m^−β over its menu (THERMAL.md). The numerator is
the same for every history, so given the state the posterior over
histories is proportional to ∏ 1/Ψ along the route: every piece of route
information sits in the normalizers, in what the intermediate worlds
could have done, never in what they did. The argument uses only that the
weight is completely multiplicative, so it holds for every demand, and
it makes every posterior below exact.

## The bounded-evidence law
Tier: theorem.
Verifier: proof; memory.py::section_b.

Read a squarefree independence world on the primes p ≤ y. It has
likelihood 1 under the crystal and ∏ (1 − p^−β) under the zeta measure,
so the odds for cold genesis are ∏ (1 − p^−β)^−1, rising with y to ζ(β):
the whole infinite world gives ζ(β):1 for the crystal and no more,
1.6449:1 against β = 2, 94% of the log-odds from p ≤ 10. A world not
squarefree refutes the crystal outright, while no finite reading refutes
a temperature: cold genesis is falsifiable and never confirmable beyond
ζ(β):1 against a given β, a ceiling that grows without limit only as
that β nears 1.

Temperature fares the same. A completed independence world's profile
is its depths G_p, prime by prime, independent geometrics
(THERMAL.md#the-zeta-measure), so its
Fisher information about β is Σ (log p)² r/(1 − r)² with r = p^−β,
which converges for every β > 1: at β = 2 it lies in [0.88447,
0.88459], and no unbiased estimate read off the completed profile has
sd below 1.063, ever. Read as a thermometer, an estimate of β, the
profile reads defects, the excesses G_p − 1 of the depths over 1: a
squarefree profile's score Σ log p·r/(1 − r) is positive at every β, so
its likelihood rises toward 1 as β grows, has no finite maximizer, and
its maximum likelihood reading is the crystal. The share of worlds that
read as crystals is exactly the squarefree share 1/ζ(β), 0.6079 at
β = 2.

The seed is no more readable. Call a prime p **peelable** in N when v_p(N) = 1
and every prime below p divides N. Greedy independence picks the least
prime not dividing the state, so (s, τ) reaches N iff N/s is the
product of a set of peelable primes: at zero temperature a state has
2^j pasts, j its peelable count, 16 at 210. Seed and history separate
only by the convention that the seed is 1.

## The unbounded-memory law
Tier: theorem; observation (depth 1 against the ceiling, at the five β
checked).
Verifier: proof; memory.py::section_d.

In the column, λ(3^a) = 2·3^(a−1), λ(n) being Carmichael's function, the
exponent of the unit group mod n, and the primes p with p − 1 dividing
it are 2, 3 and the primes 2·3^j + 1 with 1 ≤ j < a, so the headroom
ξ(3^a) (HEADROOM.md) is ξ_a = 8 ∏ {2·3^j + 1 prime, 1 ≤ j < a} for
a ≥ 1, the 8 being 2³ (λ(8) = 2 divides λ(3^a), λ(16) = 4 does not),
and
dynamics' normalizer is Ψ_a = ζ(β) − σ_β(ξ_a)
(THERMAL.md#the-hot-limit-is-ẑ), σ_β(n) the sum of d^−β over the
divisors d of n (THERMAL.md), and Ψ_a is non-increasing in a to a limit
Ψ_col. Every move 3^k is admissible from every 3^a, so the histories to
3^t are the subsets of the depths 1 to t − 1 and, by the cancellation, a
thermal dynamics world passes through 3^t with probability

    f(t) = 3^−βt / Ψ₀ · ∏_{1≤a<t} (1 + 1/Ψ_a),

Ψ₀ the normalizer at seed 1, where ξ(1) = 2, not the formula's 8.
The greedy world passes through 3^t surely,
so the log-odds for cold genesis are −log f(t), growing with slope β log
3 − log(1 + 1/Ψ_col) per deepening. The slope is positive at every
β > 1: 3, 5 and 6 never divide ξ, so Ψ_col ≥ 3^−β + 5^−β + 6^−β, and
5^−β ≥ 9^−β/(1 − 3^−β) because (9/5)^β(1 − 3^−β) is 1.2 at β = 1 and
increasing, which gives Ψ_col > Σ_(k≥1) 3^−βk = 1/(3^β − 1), that is
3^β > 1 + 1/Ψ_col, the slope positive. At β = 2 the slope is
0.6936 nats, and depth 1 alone gives 1.2682 against the independence
world's whole ceiling log ζ(2) = 0.4977, and it beats the ceiling at
β = 1.25, 1.5, 2, 3 and 6. Cold genesis, confirmable in the independence
world only up to ζ(β):1 against a given β, is confirmable without bound
in depth.

The same product is the route's law given the state: expanded, it weighs
a set S of the depths below t by ∏_(a ∈ S) 1/Ψ_a, so each depth is
visited independently with probability 1/(1 + Ψ_a), and the route's
entropy given 3^t is Σ_(a<t) h(1/(1 + Ψ_a)), h the binary entropy. Its
rate per deepening tends to h(1/(1 + Ψ_col)), analytic in β and largest,
the limiting coin fair, at β_c = 1.49595, the root of Ψ_col = 1 and the
critical point β_3 of THERMAL.md#the-place-spectrum. A finite depth's
coin there is below one half exactly while ξ_a is short of its limit,
which holds at every depth iff 2·3^j + 1 is prime for infinitely many j,
an open question; the default run shows ξ_a flat from depth 7 to 9. No
phase transition sits there: the likeliest route switches from skipping
the large depths below β_c, where Ψ_col > 1, to visiting them above it,
as the limiting coin crosses one half.

## A deepening world reads its lock prime
Tier: theorem; property (the absolute values).
Verifier: proof; memory.py::section_d.

For C coprime to an odd prime p, λ(C·p^e) = lcm(L₀, p^(e−1)) with
L₀ = lcm(λ(C), p − 1), so λ(C·p^(e+1))/λ(C·p^e) is p exactly for every
e ≥ e₀ = v_p(L₀) + 1 and is not p at e₀ − 1 (at e₀ = 1, λ(Cp)/λ(C)
divides p − 1); at p = 2, C odd, e₀ = max(3,
v₂(λ(C)) + 2), since λ(2^e) = 2^(e−2) from e = 3. An inhabitant of a
world deepening one prime p, its **lock prime**, reads p off the ratio
of λ at any two consecutive late depths. The e₀ is where the ratio
becomes p for good, not where it first equals p: at C = 1, p = 2,
λ(2) = 1 and λ(4) = 2 give the ratio 2 at e = 1 before λ(4) = λ(8)
stalls it.

The limit of the integers mod C·p^e as e grows is the product of the
integers mod C and the p-adic integers, and its deep factor carries the
p-adic absolute value, v_p(x) read off x mod p^e whenever v_p(x) < e.
The crystal's limit is ∏ F_ℓ over all primes ℓ, every factor a finite
field, on which every absolute value is trivial since x^(ℓ−1) = 1 for
x ≠ 0. The crystal keeps every prime, each as a finite-field factor,
and no factor with a nontrivial absolute value; depth keeps one prime,
and its deep factor gets the p-adic absolute value back.

## The witness gap
Tier: theorem (the split); observation (on the truncated world, moves
2 to 12, both demands: the values at τ = 4 moves, the strict ladder over
τ ≤ 4); rule (the cold path's watch, verified k = 1..10^5).
Verifier: proof; memory.py::section_w, memory.py::section_f.

P_N(m) = m^−β/Ψ_N is an exponential family in β with statistic −log m,
so watching is sampling: a watched move carries Fisher information
Var_N(log m), and d/dβ E_N[log m] = −Var_N(log m), so the drift of a
state's size under a change of temperature is the watch's per-move
information. The dated state is a function of the path, so the chain
rule splits the path's information exactly:

    I_path = I_dated + E[I_route],

the last term the information in the route posterior given the dated
state, which the cancellation puts in the normalizers alone. That term
is the **witness gap**: what a watcher keeps and a dated state drops; the
undated state drops at least as much (strictly, for mutual information,
on the truncated world below). On the truncated world, for independence
at β = 2 after τ = 4 moves, the split I_path = I_dated + gap reads
0.649817 = 0.446763 + 0.203054, a gap of 0.203054; for dynamics
0.733136 = 0.682622 + 0.050514. The same split holds for mutual
information under any prior on the generator G (here β, the demand
fixed),
J(G; path) = J(G; dated) + J(G; path | dated), and on the truncated
world with β uniform on {1.5, 2, 3} and τ on 1 to 4 the ladder
state < dated < path is strict for both demands. The Fisher bound
above limits a completed state; on the untruncated walk, whose menu is
always infinite, a watcher gains Var_N(log m) > 0 with every move.
Along the cold path, the states N = p_k#, the menu's sums close as an
Euler product, and at β = 2 each watched move carries Var_N(log m)
between 0.8055 (k = 30) and 0.9474 (k = 1) at every 1 ≤ k ≤ 10^5, so
over those moves a watcher of that path gains at least 0.8055 per move,
and within two moves more than the Fisher bound above allows a whole
completed state. Whether a
watcher's total stays bounded along the independence walk itself is not
settled here.

## The cold blindness
Tier: theorem.
Verifier: proof; memory.py::section_p.

Let q be the least prime not dividing N. Every move independence or new
idempotents admits has a prime factor not dividing N, so it is at least
q, and q is admissible; semisimplicity from a squarefree N admits a
subset of independence's moves containing q. All three greedy picks are
q, the coincidence GROWTH.md#the-three-fates found for the first two, so
from a squarefree seed three demands, whose admissible sets differ at
every N > 1, write one world forever, and no watcher of any length
learns which. Two probes do: for N > 1 with p its least prime, q² is
refused only by semisimplicity and pq admitted only by new idempotents.
Observation and intervention come apart completely at zero temperature
from a squarefree seed.

Heat lets a watcher tell the demands apart at a computable rate. For
nested admissible sets A_narrow ⊂ A_wide at one state, Ψ_narrow and
Ψ_wide the sums of m^−β over each and P_narrow and P_wide the move laws
m^−β/Ψ_narrow and m^−β/Ψ_wide, KL(P_narrow ‖ P_wide) =
log(Ψ_wide/Ψ_narrow) exactly; where q, the least prime not dividing N,
is the least move of both, as at all three demands at a squarefree N,
the divergence is asymptotic to (m*/q)^−β as β grows, m* the least move
in A_wide outside A_narrow, so −log KL grows in β with slope log(m*/q),
the **discrimination rate**. At N = 30 that is log 2 for independence
inside new idempotents (m* = 14) and log 7 for semisimplicity inside
independence (m* = 49).

## The fossil paradox
Tier: theorem (the one-window world); observation (the route entropies
on the truncated world).
Verifier: proof; memory.py::section_f.

In a one-window world every state has the same normalizer, so by the
cancellation the route posterior given the dated state (3^t, τ) is
uniform over the compositions of t into τ parts and free of β. The dated
state is sufficient, the witness gap is zero,
I_dated = I_path = τ(log 3)² r/(1 − r)² with r = 3^−β, and the route's
entropy given the dated state is the largest any law on those
compositions allows. A menu that never changes makes the dated state a
perfect
fossil of the generator and a maximally unreadable past at once:
evidence about the generator and route information are different
resources, and the chain rule says what the state loses of the first is
exactly what the route posterior carries. On the truncated world, where
the one-window menu is {3, 9}, with β uniform on {1.5, 2, 3} and τ
uniform on 1 to 4, the route's entropy given the dated state and β is
0.3183 bits for the one-window world, of a maximum of 0.3183, the
mean entropy of a uniform route posterior over the possible routes,
dynamics 1.1754 of 1.2492, independence 1.5414 of 2.0900.

At the true limits the grading inverts. Hot dynamics reaches Ẑ from
every seed at every β (THERMAL.md#the-hot-limit-is-ẑ) and the one-window
world reaches 3^∞: both limits are β-free and carry no information about
temperature. Of the three, the independence world's limit, the zeta
measure, alone keeps a finite trace, the bounded one above, written in
its defects, geometric in β. A world whose limit is free of β has
nothing left to write on.
