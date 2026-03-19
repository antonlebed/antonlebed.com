// ring.js — Ring math for antonlebed.com. ☠️ SCAFFOLDING (dies when WASM replaces it).
// Provides AX.* API for 61 pages. 172L. CRT compat shim killed S890.
// S873: extracted from ax.js. S874: ax.js killed. S890: CRT.* shim killed.

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

function kingdom(n) {
    var m = ringMod(n), g = gcd(m, N);
    if (g === 1) return 0; // unit
    if (g === N) return -1; // void
    // smallest prime factor of gcd determines kingdom
    var p = 2;
    while (p * p <= g) { if (g % p === 0) return p; p++; }
    return g;
}

function crt_r(n, idx) {
    var m = ringMod(n);
    return (idx >= 0 && idx < CRT_MODS.length) ? m % CRT_MODS[idx] : 0;
}

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

const CONSTANTS = {
    s:1, D:2, K:3, E:5, b:7, L:11,
    sigma:1, OMEGA:606376, DATA:210, THIN:2310,
    HYDOR:105, KEY:41, ANSWER:42, SOUL:67,
    G:97, ADDRESS:137, DUAL:173, ME:18, LAMBDA:420,
    GATE:13, ESCAPE:17, THORNS:28, TRUE:970200,
    GATE_FORM:12612600, pi:Math.PI
};
const VALUE_NAMES = {
    0:'void', 1:'s', 2:'D', 3:'K', 5:'E', 7:'b', 11:'L',
    18:'ME', 41:'KEY', 42:'ANSWER', 67:'SOUL', 97:'G',
    105:'HYDOR', 137:'ADDRESS', 173:'DUAL', 210:'DATA',
    420:'LAMBDA', 2310:'THIN', 606376:'OMEGA',
    970200:'TRUE', 12612600:'GATE_FORM'
};

const GRID_COLORS = ['#111','#0074D9','#FF4136','#2ECC40','#FFDC00','#AAAAAA','#F012BE','#FF851B','#7FDBFF','#870C25'];
function fmtGrid(g) {
    if (!Array.isArray(g) || g.length === 0) return '';
    var R = g.length, C = Array.isArray(g[0]) ? g[0].length : 0;
    if (C === 0) return '[]';
    var html = '<div class="grid-display" style="grid-template-columns:repeat(' + C + ',20px)">';
    for (var r = 0; r < R; r++) {
        var row = g[r]; if (!Array.isArray(row)) continue;
        for (var c = 0; c < row.length; c++) {
            var v = typeof row[c] === 'number' ? Math.round(row[c]) : 0;
            var color = (v >= 0 && v < 10) ? GRID_COLORS[v] : '#333';
            html += '<div class="grid-cell" style="background:' + color + '">' + (v !== 0 ? v : '') + '</div>';
        }
    }
    return html + '</div>';
}

// WASM acceleration (for crt_wasm.js integration)
var _wasm = null;
const TRUE_N = 970200;

return {
    get N() { return N; },
    get CRT_MODS() { return CRT_MODS.slice(); },
    setRing, factorPrimePowers,
    ringMod, gcd, crt, coupling, eigenvalue, mirror, kingdom, crt_r,
    eulerPhi, multOrder, multInverse, modPow,
    CRT_NAMES, CRT_COLORS, reconstruct, ringAdd, ringMul,
    decompose: crt, modinv: multInverse_mod,
    CONSTANTS, VALUE_NAMES, GRID_COLORS, fmtGrid,
    setWasm: function(mod) { _wasm = mod; },
    get wasmActive() { return _wasm !== null && N === TRUE_N; }
};
})();
