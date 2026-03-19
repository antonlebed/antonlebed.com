// ring.js — Ring math subset of ax.js. ☠️ SCAFFOLDING (dies when WASM replaces it).
// Provides AX.* and CRT.* API for pages that need ring arithmetic but not the .ax interpreter.
// ~150L vs ax.js ~1752L. Same API surface for ring math. Drop-in replacement.
// S873: extracted from ax.js. Kills ax.js dependency for 54+ pages.

const AX = (function() {
'use strict';

let N = 970200;
let CRT_MODS = [8, 9, 25, 49, 11];

function factorPrimePowers(n) {
    n = Math.abs(Math.round(n));
    const factors = [];
    for (let p = 2; p * p <= n; p++) {
        if (n % p === 0) { let pk = 1; while (n % p === 0) { pk *= p; n /= p; } factors.push(pk); }
    }
    if (n > 1) factors.push(n);
    return factors;
}

function setRing(newN) {
    newN = Math.abs(Math.round(newN));
    if (newN < 2) newN = 2;
    N = newN;
    CRT_MODS = factorPrimePowers(N);
}

function ringMod(x) { x = Math.round(x); return ((x % N) + N) % N; }

function gcd(a, b) {
    a = Math.abs(Math.round(a)); b = Math.abs(Math.round(b));
    while (b) { [a, b] = [b, a % b]; }
    return a;
}

function modPow(base, exp) {
    base = ((Math.round(base) % N) + N) % N;
    exp = Math.round(exp);
    if (exp < 0) return 0;
    let r = 1;
    while (exp > 0) { if (exp & 1) r = (r * base) % N; exp >>= 1; base = (base * base) % N; }
    return r;
}

function coupling(n) { return N / gcd(ringMod(n), N); }

function crt(n) {
    const r = ringMod(n);
    return CRT_MODS.map(m => r % m);
}

function eigenvalue(n) {
    const c = crt(n), P = Math.PI;
    return c.reduce((sum, ci, i) => sum + (CRT_MODS[i] <= 2 ? 1 : 2) * Math.cos(2 * P * ci / CRT_MODS[i]), 0);
}

function mirror(n) { return ringMod(N - ringMod(n)); }

function multInverse_mod(a, m) {
    a = ((a % m) + m) % m;
    let [old_r, r] = [a, m], [old_s, s] = [1, 0];
    while (r !== 0) { const q = Math.floor(old_r / r); [old_r, r] = [r, old_r - q * r]; [old_s, s] = [s, old_s - q * s]; }
    return ((old_s % m) + m) % m;
}

function reconstruct(channels) {
    const mods = CRT_MODS;
    let sum = 0;
    for (let i = 0; i < mods.length; i++) {
        const Mi = N / mods[i];
        sum += channels[i] * Mi * multInverse_mod(Mi, mods[i]);
    }
    return ((sum % N) + N) % N;
}

function ringAdd(a, b) { return ((a + b) % N + N) % N; }
function ringMul(a, b) { return Number((BigInt(((a % N) + N) % N) * BigInt(((b % N) + N) % N)) % BigInt(N)); }

function eulerPhi(n) {
    n = Math.abs(Math.round(n));
    if (n < 1) return 0;
    let result = n;
    for (let p = 2; p * p <= n; p++) { if (n % p === 0) { while (n % p === 0) n /= p; result -= result / p; } }
    if (n > 1) result -= result / n;
    return Math.round(result);
}

function multOrder(n) {
    const m = ringMod(n);
    if (gcd(m, N) !== 1) return 0;
    let x = m, k = 1;
    while (x !== 1 && k <= 420) { x = (x * m) % N; k++; }
    return x === 1 ? k : 0;
}

function multInverse(n) {
    let m = ringMod(n);
    if (gcd(m, N) !== 1) return -1;
    let [old_r, r] = [m, N], [old_s, s] = [1, 0];
    while (r !== 0) { const q = Math.floor(old_r / r); [old_r, r] = [r, old_r - q * r]; [old_s, s] = [s, old_s - q * s]; }
    return ((old_s % N) + N) % N;
}

const CRT_NAMES = ['Z/8 (D)', 'Z/9 (K)', 'Z/25 (E)', 'Z/49 (b)', 'Z/11 (L)'];
const CRT_COLORS = ['#f44', '#fa0', '#ff0', '#0f0', '#08f'];

return {
    get N() { return N; },
    get CRT_MODS() { return CRT_MODS.slice(); },
    setRing, factorPrimePowers,
    ringMod, gcd, crt, coupling, eigenvalue, mirror,
    eulerPhi, multOrder, multInverse, modPow,
    CRT_NAMES, CRT_COLORS, reconstruct, ringAdd, ringMul,
    decompose: crt, modinv: multInverse_mod
};
})();

// CRT compatibility namespace (S815: for pages that used crt_core.js)
if (typeof window !== 'undefined' && !window.CRT) {
    window.CRT = {
        get N() { return AX.N; },
        get MODS() { return AX.CRT_MODS; },
        NAMES: AX.CRT_NAMES,
        COLORS: AX.CRT_COLORS,
        decompose: function(n) { return AX.crt(n); },
        reconstruct: function(ch) { return AX.reconstruct(ch); },
        gcd: function(a, b) { return AX.gcd(a, b); },
        coupling: function(n) { return AX.coupling(n); },
        modpow: function(base, exp, mod) {
            if (mod !== undefined) {
                let r = 1; base = ((base % mod) + mod) % mod;
                while (exp > 0) { if (exp & 1) r = r * base % mod; base = base * base % mod; exp >>= 1; }
                return r;
            }
            return AX.modPow(base, exp);
        },
        modinv: function(a, m) { return AX.modinv(a, m); },
        ringAdd: function(a, b) { return AX.ringAdd(a, b); },
        ringMul: function(a, b) { return AX.ringMul(a, b); },
    };
}
