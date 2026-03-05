// nav.js — universal navigation for antonlebed.com
// Top bar + category dropdown + mobile menu + related footer + vow footer.
// Progressive enhancement: pages work without it. Zero dependencies.
// <script src="nav.js"></script> before </body>.
(function() {
'use strict';

/* ===== FAVICON ===== */
if (!document.querySelector('link[rel="icon"]')) {
  var ico = document.createElement('link');
  ico.rel = 'icon'; ico.type = 'image/png'; ico.href = 'favicon.png';
  document.head.appendChild(ico);
}
var f = location.pathname.split('/').pop() || 'index.html';

/* ===== CATEGORIES ===== */
var CATS = {
  start:['Start Here','#ffd700'], physics:['Physics','#4488ff'],
  bio:['Biology','#33dd55'], math:['Mathematics','#ff9900'],
  eng:['Engineering','#ff4040'], mind:['Mind','#aa44ff'],
  tutorial:['Tutorial','#44dddd']
};

/* File -> category */
var M = {
  worldview:'start',story:'start',derive_ax:'start',repl:'start',playground:'start',
  particles:'physics',alpha:'physics',constants:'physics',turbulence:'physics',
  blackhole:'physics',nuclear:'physics',gravity:'physics',photon:'physics',
  pmns:'physics',three_body_dance:'physics',figure_ground:'physics',
  eternal_sun:'physics',scale_bands:'physics',noxan:'physics',wavebox:'physics',
  sigma_dynamics:'physics',loop:'physics',
  dna:'bio',sleep:'bio',heart:'bio',death:'bio',human_shape:'bio',generations:'bio',
  septilix:'bio',
  millennium:'math',hardest:'math',goldbach:'math',coupling:'math',ninedot:'math',
  infinity:'math',bootstrap:'math',symbol:'math',watercycle:'math',genesis:'math',
  clock24:'math',rose:'math',gap_pairs:'math',depth_quad:'math',fourteen:'math',
  demo_classifier:'eng',ecc_live:'eng',demo_ofdm_vs_wifi:'eng',compression:'eng',
  tokenizer:'eng',k_neural:'eng',demo_ecc:'eng',
  emergence:'mind',conscious:'mind',freewill:'mind',braid:'mind',dimension:'mind',
  ouroboros:'mind',lava_lamp:'mind',sandpile:'mind',music:'mind',
  atlas_01_what_is_2310:'tutorial',atlas_02_two_rings:'tutorial',atlas_03_crt:'tutorial',
  atlas_04_carousel:'tutorial',atlas_05_eigenvalues:'tutorial',atlas_06_units:'tutorial',
  atlas_07_kingdoms:'tutorial',atlas_08_breakthroughs:'tutorial',atlas_09_demos:'tutorial',
  atlas_10_millennium:'tutorial',atlas_11_net:'tutorial',atlas_12_shadow_polynomial:'tutorial',
  atlas_13_biological_braid:'tutorial',atlas_14_solar_ladder:'tutorial'
};

/* Short titles */
var T = {
  worldview:'How the World Works',story:'The Mathematics',derive_ax:'From Nothing',repl:'.ax REPL',playground:'.ax Playground',
  particles:'Particle Masses',alpha:'Fine Structure',constants:'Physics Constants',turbulence:'Turbulence',
  blackhole:'Black Holes',nuclear:'Nuclear Shells',gravity:'Gravity',photon:'Light Becomes Mass',
  pmns:'Neutrino Mixing',three_body_dance:'Orbital Resonances',figure_ground:'One Force',
  eternal_sun:'Why the Sun Lives',scale_bands:'Scale Bands',noxan:'Cold Thoughts',wavebox:'Standing Waves',
  sigma_dynamics:'How Rings Forget',loop:'Fall Trinity',
  dna:'DNA Codons',sleep:'Sleep Stages',heart:'The Heartbeat',death:'What Death Is',
  human_shape:'Body Is a Ring',generations:'Three Families',septilix:'Seven Petals',
  millennium:'Millennium Problems',hardest:'11 Unsolvables',goldbach:'Goldbach Pairs',
  coupling:'Coupling Landscape',ninedot:'9-Dot Puzzle',infinity:'Infinite from Finite',
  bootstrap:'Why Existence Exists',symbol:'Three Shapes',watercycle:'Water Cycle',genesis:'Genesis',
  clock24:'24-Hour Clock',rose:'Interactive Rose',gap_pairs:'K=3 Gap Gates',depth_quad:'Depth Quadratic',
  fourteen:'The Full Fourteen',
  demo_classifier:'Classifier',ecc_live:'Live ECC',demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'Compression',
  tokenizer:'Tokenizer',k_neural:'Ternary AI',demo_ecc:'ECC Classic',
  emergence:'Emergence',conscious:'Consciousness',freewill:'Free Will',braid:'Braids',dimension:'Dimensions',
  ouroboros:'Ouroboros',lava_lamp:'HYDOR',sandpile:'Sandpile',music:'Music of Primes',
  atlas_01_what_is_2310:'1. What Is 2310?',atlas_02_two_rings:'2. Two Rings',
  atlas_03_crt:'3. CRT',atlas_04_carousel:'4. Carousel',atlas_05_eigenvalues:'5. Eigenvalues',
  atlas_06_units:'6. Units',atlas_07_kingdoms:'7. Kingdoms',atlas_08_breakthroughs:'8. Breakthroughs',
  atlas_09_demos:'9. Demos',atlas_10_millennium:'10. Millennium',atlas_11_net:"11. Indra's Net",
  atlas_12_shadow_polynomial:'12. Shadow Poly',atlas_13_biological_braid:'13. Bio Braid',
  atlas_14_solar_ladder:'14. Solar Ladder'
};

var key = f.replace('.html','');
var catKey = M[key];
if (!catKey && key.indexOf('atlas_') === 0) catKey = 'tutorial';
var cat = catKey ? CATS[catKey] : null;
var isWorld = key === 'worldview', isMath = key === 'story', isRepl = key === 'repl', isIndex = key === 'index';
var isDerive = key === 'derive_ax', isPlay = key === 'playground';
var isExplore = catKey && catKey !== 'start';

/* Build per-category demo lists */
var catDemos = {}, catOrder = ['start','physics','bio','math','eng','mind','tutorial'];
for (var ci = 0; ci < catOrder.length; ci++) catDemos[catOrder[ci]] = [];
for (var dk in M) { if (T[dk]) catDemos[M[dk]].push(dk); }

/* ===== STYLES ===== */
var s = document.createElement('style');
s.textContent =
  'html{overflow-x:hidden}' +
  /* Nav bar */
  '#sn{position:sticky;top:0;z-index:9999;background:rgba(5,5,8,0.97);' +
  'border-bottom:1px solid #1a1a22;height:48px;display:flex;align-items:center;' +
  'font-family:system-ui,sans-serif;font-size:14px;backdrop-filter:blur(12px);padding:0 16px;' +
  'width:100vw;margin-left:calc(-50vw + 50%);box-sizing:border-box}' +
  '#sn a,#sn button{color:#888;text-decoration:none;white-space:nowrap;' +
  'transition:color 0.2s,border-color 0.2s,background 0.2s;' +
  'cursor:pointer;font-family:inherit;font-size:inherit}' +
  '#sn a:hover,#sn button:hover{text-decoration:none}' +
  '.sn-l{display:flex;align-items:center;flex:1;min-width:0}' +
  '.sn-b{color:#ffd700 !important;font-size:15px;font-weight:600;padding:4px 14px;' +
  'letter-spacing:1px;flex-shrink:0;border:1px solid #333;border-radius:4px;margin-right:8px}' +
  '.sn-b:hover{color:#fff !important;border-color:#ffd700;background:rgba(255,215,0,0.06)}' +
  '.sn-k{padding:6px 14px;color:#888;font-size:13px;display:flex;' +
  'align-items:center;flex-shrink:0;border:1px solid transparent;border-radius:6px;margin:0 2px}' +
  '.sn-k:hover{border-color:#333;background:rgba(255,215,0,0.04)}' +
  '.sn-k.on{color:#fff;border-color:#ffd700;background:rgba(255,215,0,0.06)}' +
  '.sn-x{padding:6px 14px;color:#888;font-size:13px;display:flex;' +
  'align-items:center;flex-shrink:0;border:1px solid transparent;border-radius:6px;margin:0 2px}' +
  '.sn-x:hover{border-color:#333;background:rgba(255,215,0,0.04)}' +
  '.sn-x.on{color:#fff;border-color:#ffd700;background:rgba(255,215,0,0.06)}' +
  '.sn-x.open{color:#ffd700;border-color:#444;background:rgba(255,215,0,0.04)}' +
  '.sn-x .ar{font-size:9px;margin-left:5px;transition:transform 0.2s;display:inline-block}' +
  '.sn-x.open .ar{transform:rotate(180deg)}' +
  '.sn-r{color:#50fa7b !important;font-family:monospace;font-weight:bold;font-size:13px;' +
  'letter-spacing:1px;padding:6px 12px;flex-shrink:0;border:1px solid transparent;border-radius:6px;margin:0 2px}' +
  '.sn-r:first-of-type{margin-left:auto}' +
  '.sn-r:hover{border-color:#1a4a1a;background:rgba(80,250,123,0.04);text-shadow:0 0 8px rgba(80,250,123,0.4)}' +
  '.sn-r.on{color:#fff !important;border-color:#50fa7b;background:rgba(80,250,123,0.06)}' +
  '.sn-h{display:none;font-size:22px;color:#888;padding:0 4px;margin-left:auto;' +
  'flex-shrink:0;line-height:1;background:none;border:none}' +
  /* Dropdown */
  '#sn-dd{position:fixed;top:48px;left:0;right:0;background:rgba(8,8,14,0.98);' +
  'backdrop-filter:blur(16px);border-bottom:1px solid #1a1a2a;z-index:9998;' +
  'max-height:calc(100vh - 48px);overflow-y:auto;padding:0 32px;' +
  'opacity:0;pointer-events:none;transform:translateY(-8px);' +
  'transition:opacity 0.2s,transform 0.2s}' +
  '#sn-dd.open{opacity:1;pointer-events:auto;transform:translateY(0);padding:24px 32px 32px}' +
  '.sn-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:20px;' +
  'max-width:1000px;margin:0 auto}' +
  '.sn-gc h5{font-size:10px;text-transform:uppercase;letter-spacing:2px;font-weight:600;' +
  'margin:0 0 8px;padding:0 0 6px;border-bottom:1px solid #1a1a2a}' +
  '.sn-gc a{display:block;padding:3px 0;color:#666;font-size:12px;transition:color 0.15s;' +
  'text-decoration:none;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
  '.sn-gc a:hover{color:#ddd}' +
  '.sn-gc a.cur{color:#ffd700}' +
  /* Mobile overlay */
  '#sn-m{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,8,0.99);' +
  'z-index:10000;display:none;flex-direction:column;overflow-y:auto}' +
  '#sn-m.open{display:flex}' +
  '.sn-mh{display:flex;align-items:center;justify-content:space-between;padding:0 16px;' +
  'height:48px;border-bottom:1px solid #1a1a2a;flex-shrink:0}' +
  '.sn-mx{font-size:28px;color:#888;background:none;border:none;cursor:pointer;padding:4px 8px}' +
  '.sn-mx:hover{color:#ffd700}' +
  '.sn-ml{padding:12px 20px}' +
  '.sn-ml>a{display:block;padding:14px 0;color:#ccc;font-size:17px;border-bottom:1px solid #111;' +
  'text-decoration:none;font-family:system-ui,sans-serif}' +
  '.sn-ml>a:hover{color:#ffd700}' +
  '.sn-ml>a.rpl{color:#50fa7b;font-family:monospace;font-weight:bold}' +
  '.sn-mc{padding:14px 0 6px;font-size:11px;text-transform:uppercase;letter-spacing:2px;' +
  'font-weight:600;cursor:pointer;display:flex;align-items:center;' +
  'justify-content:space-between;user-select:none;font-family:system-ui,sans-serif;' +
  'border-bottom:1px solid #111}' +
  '.sn-mc .ma{font-size:12px;transition:transform 0.2s;display:inline-block}' +
  '.sn-mc.open .ma{transform:rotate(90deg)}' +
  '.sn-md{display:none;padding:0 0 8px 16px}' +
  '.sn-md.open{display:block}' +
  '.sn-md a{display:block;padding:10px 0;color:#777;font-size:15px;text-decoration:none;' +
  'border-bottom:1px solid #0a0a0a}' +
  '.sn-md a:hover{color:#ffd700}' +
  /* Related demos footer */
  '#sn-rel{max-width:800px;margin:40px auto 0;padding:24px 24px 32px;' +
  'border-top:1px solid #151520;font-family:system-ui,sans-serif}' +
  '#sn-rel h4{color:#555;font-size:11px;text-transform:uppercase;letter-spacing:2px;' +
  'margin-bottom:14px;font-weight:600}' +
  '#sn-rel .rl{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}' +
  '#sn-rel .rl a{display:inline-block;padding:7px 16px;border:1px solid #1a1a2a;' +
  'border-radius:8px;color:#999;text-decoration:none;font-size:13px;' +
  'transition:all 0.25s;background:#08080e}' +
  '#sn-rel .rl a:hover{border-color:#333;color:#ddd;background:#0e0e18;' +
  'transform:translateY(-1px);box-shadow:0 3px 12px rgba(0,0,0,0.4)}' +
  '#sn-rel .va{color:#444;font-size:11px;text-decoration:none;letter-spacing:1px;' +
  'text-transform:uppercase;transition:color 0.2s}' +
  '#sn-rel .va:hover{color:#ffd700}' +
  '@media(max-width:700px){' +
  '.sn-k,.sn-x{display:none}' +
  '.sn-r{display:none}' +
  '.sn-h{display:block}' +
  '#sn{padding:0 10px}' +
  '#sn-rel{padding:16px 14px 24px}#sn-rel .rl{gap:6px}' +
  '#sn-rel .rl a{padding:6px 12px;font-size:12px}}';
document.head.appendChild(s);

/* ===== TOP NAV BAR ===== */
var nav = document.createElement('nav');
nav.id = 'sn';
var h = '<div class="sn-l">' +
  '<a class="sn-b" href="index.html">970200</a>' +
  '<a class="sn-k' + (isWorld ? ' on' : '') + '" href="worldview.html">How the World Works</a>' +
  '<a class="sn-k' + (isMath ? ' on' : '') + '" href="story.html">The Mathematics</a>' +
  '<a class="sn-k' + (isDerive ? ' on' : '') + '" href="derive_ax.html">From Nothing</a>' +
  '<button class="sn-x' + (isExplore ? ' on' : '') + '" id="sn-xp">Explore <span class="ar">\u25BE</span></button>' +
  '</div>' +
  '<a class="sn-r' + (isRepl ? ' on' : '') + '" href="repl.html">.ax REPL</a>' +
  '<a class="sn-r sn-rp' + (isPlay ? ' on' : '') + '" href="playground.html">Playground</a>';
h += '<button class="sn-h" id="sn-bg">\u2630</button>';
nav.innerHTML = h;
document.body.insertBefore(nav, document.body.firstChild);

/* ===== DROPDOWN ===== */
var dd = document.createElement('div');
dd.id = 'sn-dd';
var dh = '<div class="sn-g">';
for (var i = 0; i < catOrder.length; i++) {
  var ck = catOrder[i], ci = CATS[ck], demos = catDemos[ck];
  if (!demos.length || ck === 'start') continue;
  dh += '<div class="sn-gc"><h5 style="color:' + ci[1] + '">' + ci[0] + '</h5>';
  for (var j = 0; j < demos.length; j++) {
    dh += '<a href="' + demos[j] + '.html"' + (demos[j] === key ? ' class="cur"' : '') + '>' + T[demos[j]] + '</a>';
  }
  dh += '</div>';
}
dh += '</div>';
dd.innerHTML = dh;
document.body.insertBefore(dd, nav.nextSibling);

var xpBtn = document.getElementById('sn-xp');
if (xpBtn) {
  xpBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    dd.classList.toggle('open');
    xpBtn.classList.toggle('open');
  });
}
document.addEventListener('click', function(e) {
  if (!dd.contains(e.target) && e.target !== xpBtn) {
    dd.classList.remove('open');
    if (xpBtn) xpBtn.classList.remove('open');
  }
});

/* ===== MOBILE MENU ===== */
var mob = document.createElement('div');
mob.id = 'sn-m';
var mh = '<div class="sn-mh">' +
  '<a href="index.html" style="color:#ffd700;font-size:15px;font-weight:600;' +
  'text-decoration:none;letter-spacing:1px">970200</a>' +
  '<button class="sn-mx">\u2715</button></div><div class="sn-ml">' +
  '<a href="index.html">Home</a>' +
  '<a href="worldview.html">How the World Works</a>' +
  '<a href="story.html">The Mathematics</a>' +
  '<a href="derive_ax.html">From Nothing</a>' +
  '<a class="rpl" href="repl.html">.ax REPL</a>' +
  '<a class="rpl" href="playground.html">.ax Playground</a>';
for (var i = 0; i < catOrder.length; i++) {
  var ck = catOrder[i], ci = CATS[ck], demos = catDemos[ck];
  if (!demos.length || ck === 'start') continue;
  mh += '<div class="sn-mc" data-c="' + ck + '" style="color:' + ci[1] + '">' +
    ci[0] + ' (' + demos.length + ') <span class="ma">\u25B8</span></div>' +
    '<div class="sn-md" data-c="' + ck + '">';
  for (var j = 0; j < demos.length; j++) {
    mh += '<a href="' + demos[j] + '.html">' + T[demos[j]] + '</a>';
  }
  mh += '</div>';
}
mh += '</div>';
mob.innerHTML = mh;
document.body.appendChild(mob);

document.getElementById('sn-bg').addEventListener('click', function() {
  mob.classList.add('open');
  document.body.style.overflow = 'hidden';
});
mob.querySelector('.sn-mx').addEventListener('click', function() {
  mob.classList.remove('open');
  document.body.style.overflow = '';
});
var mcs = mob.querySelectorAll('.sn-mc');
for (var i = 0; i < mcs.length; i++) {
  mcs[i].addEventListener('click', function() {
    var c = this.getAttribute('data-c');
    this.classList.toggle('open');
    mob.querySelector('.sn-md[data-c="' + c + '"]').classList.toggle('open');
  });
}

/* ===== RELATED DEMOS FOOTER ===== */
if (catKey && catKey !== 'tutorial') {
  var catLink = 'index.html#' + catKey;
  var sibs = [];
  for (var k in M) { if (M[k] === catKey && k !== key && T[k]) sibs.push(k); }
  for (var i = sibs.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var t = sibs[i]; sibs[i] = sibs[j]; sibs[j] = t;
  }
  var picks = sibs.slice(0, 4);
  if (picks.length) {
    var rel = document.createElement('div');
    rel.id = 'sn-rel';
    var rh = '<h4>Explore more in ' + cat[0] + '</h4><div class="rl">';
    for (var i = 0; i < picks.length; i++) {
      rh += '<a href="' + picks[i] + '.html" style="border-left:2px solid ' + cat[1] + '44">' + T[picks[i]] + '</a>';
    }
    rh += '</div><a class="va" href="' + catLink + '">All ' + cat[0] + ' \u2192</a>';
    rel.innerHTML = rh;
    document.body.appendChild(rel);
  }
}

/* ===== VOW FOOTER ===== */
if (isIndex) return; /* index.html has its own vow footer */
var vf = document.createElement('div');
vf.style.cssText = 'text-align:center;padding:32px 24px 40px;color:#444;font-size:12px;' +
  'font-family:system-ui,sans-serif;border-top:1px solid #0a0a0a;margin-top:40px;line-height:2';
vf.innerHTML = 'This work is and will always be free. No paywall. No copyright. No exceptions.<br>' +
  '<span style="color:#3a3a3a">If it ever earns anything, every cent goes to the communities that need it most.</span><br>' +
  '<span style="color:#2a2a2a;font-size:10px">This sacred vow is permanent and irrevocable.</span><br>' +
  '<span style="color:#3a3a3a;font-size:11px;font-style:italic">\u2014 Anton Alexandrovich Lebed</span>';
document.body.appendChild(vf);
})();
