// nav.js — universal navigation for antonlebed.com
// Top bar + category dropdown + mobile menu + related footer + vow footer.
// Progressive enhancement: pages work without it. Zero dependencies.
// <script src="nav.js"></script> before </body>.
(function() {
'use strict';

/* ===== CRITICAL CSS (immediate — loaded from <head>, prevents FOUC) ===== */
var pre = document.createElement('style');
pre.textContent = 'body{padding-top:40px!important}html{overflow-x:hidden}' +
'.back{top:52px!important}' +
'#contrast{z-index:10001!important}#contrast .close{top:52px!important}' +
'#detail{top:52px!important}#legend{top:52px!important}' +
'*{scrollbar-width:thin;scrollbar-color:#333 transparent}' +
'::-webkit-scrollbar{width:8px;height:8px}' +
'::-webkit-scrollbar-track{background:transparent}' +
'::-webkit-scrollbar-thumb{background:#2a2a2a;border-radius:4px}' +
'::-webkit-scrollbar-thumb:hover{background:#444}' +
/* Global accessibility: text readability on varied backgrounds */
':root{--ax-text:#d0d0d0;--ax-dim:#999;--ax-muted:#777;--ax-subtle:#666}' +
'.caption{color:var(--ax-dim)!important}' +
'.dim{color:var(--ax-dim)!important}' +
'.widget-title{color:var(--ax-dim)!important}' +
/* Tooltip auto-fade class for mobile */
'.ax-tooltip-fade{transition:opacity 0.5s!important}';
document.head.appendChild(pre);

/* ===== FAVICON ===== */
if (!document.querySelector('link[rel="icon"]')) {
  var ico = document.createElement('link');
  ico.rel = 'icon'; ico.type = 'image/png'; ico.href = 'favicon.png';
  document.head.appendChild(ico);
}
/* ===== DOM SETUP (deferred until body exists) ===== */
function init() {
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
  particles:'Particle Masses',alpha:'Fine Structure Constant',constants:'All Physics Constants',turbulence:'Turbulence & Metabolism',
  blackhole:'Black Holes',nuclear:'Nuclear Shells',gravity:'Gravity',photon:'Light Becomes Mass',
  pmns:'Neutrino Mixing',three_body_dance:'Orbital Resonances',figure_ground:'One Force',
  eternal_sun:'Why the Sun Lives',scale_bands:'Scale Bands',noxan:'Cold Thoughts',wavebox:'Standing Waves',
  sigma_dynamics:'How Rings Forget',loop:'Fall Trinity',
  dna:'DNA Codons',sleep:'Sleep Stages',heart:'The Heartbeat',death:'What Death Is',
  human_shape:'Your Body Is a Ring',generations:'Three Families',septilix:'Seven Petals',
  millennium:'Millennium Problems',hardest:'11 Famous Unsolvables',goldbach:'Goldbach Pairs',
  coupling:'Coupling Landscape',ninedot:'9-Dot Puzzle',infinity:'Infinite from Finite',
  bootstrap:'Why Existence Exists',symbol:'Three Shapes',watercycle:'Water Cycle',genesis:'Genesis',
  clock24:'24-Hour Clock',rose:'Interactive Rose',gap_pairs:'K=3 Gap Gates',depth_quad:'Depth Quadratic',
  fourteen:'The Full Fourteen',
  demo_classifier:'Classifier',ecc_live:'Live Error Correction',demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'CRT Compression',
  tokenizer:'CRT Tokenizer',k_neural:'Ternary AI',demo_ecc:'ECC Classic',
  emergence:'Emergence',conscious:'Consciousness',freewill:'Free Will',braid:'Braids',dimension:'Dimensions',
  ouroboros:'Ouroboros',lava_lamp:'HYDOR',sandpile:'Sandpile',music:'Music of Primes',
  atlas_01_what_is_2310:'0. Five Primes',atlas_02_two_rings:'1. Three Rings',
  atlas_03_crt:'2. Five Petals',atlas_04_carousel:'3. Carousel',atlas_05_eigenvalues:'4. Eigenvalues',
  atlas_06_units:'5. Units',atlas_07_kingdoms:'6. Kingdoms',atlas_08_breakthroughs:'7. Breakthroughs',
  atlas_09_demos:'8. Demos',atlas_10_millennium:'9. Millennium',atlas_11_net:"10. Indra's Net",
  atlas_12_shadow_polynomial:'11. Shadow Polynomial',atlas_13_biological_braid:'12. Bio Braid',
  atlas_14_solar_ladder:'13. Solar Ladder'
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
  'body{padding-top:40px!important}' +
  /* Nav bar — fixed: no layout reflow, no FOUC */
  '#sn{position:fixed;top:0;left:0;right:0;z-index:9999;background:rgba(5,5,8,0.97);' +
  'border-bottom:1px solid #1a1a22;height:40px;display:flex;align-items:center;' +
  'font-family:system-ui,sans-serif;font-size:14px;backdrop-filter:blur(12px);padding:0 16px}' +
  '#sn a,#sn button{color:#888;text-decoration:none;white-space:nowrap;' +
  'transition:color 0.2s,border-color 0.2s,background 0.2s;' +
  'cursor:pointer;font-family:inherit;font-size:inherit}' +
  '#sn a:hover,#sn button:hover{text-decoration:none}' +
  '.sn-l{display:flex;align-items:center;flex:1;min-width:0}' +
  '.sn-b{color:#ffd700 !important;font-size:15px;font-weight:600;padding:3px 12px;' +
  'letter-spacing:1px;flex-shrink:0;border:1px solid #222;border-radius:6px;margin:0 3px;background:none}' +
  '.sn-b:hover{color:#fff !important;border-color:#444;background:rgba(255,215,0,0.04)}' +
  '.sn-k{padding:3px 12px;color:#888;font-size:13px;display:flex;' +
  'align-items:center;flex-shrink:0;border:1px solid #222;border-radius:6px;margin:0 3px;background:none}' +
  '.sn-k:hover{color:#ccc;border-color:#444;background:rgba(255,215,0,0.04)}' +
  '.sn-k.on{color:#fff;border-color:#ffd700;background:rgba(255,215,0,0.06)}' +
  '.sn-x{padding:3px 12px;color:#888;font-size:13px;display:flex;' +
  'align-items:center;flex-shrink:0;border:1px solid #222;border-radius:6px;margin:0 3px;background:none}' +
  '.sn-x:hover{color:#ccc;border-color:#444;background:rgba(255,215,0,0.04)}' +
  '.sn-x.on{color:#aaa;border-color:#333}' +
  '.sn-x.open{color:#ffd700;border-color:#444;background:rgba(255,215,0,0.04)}' +
  '.sn-x .ar{font-size:9px;margin-left:5px;transition:transform 0.2s;display:inline-block}' +
  '.sn-x.open .ar{transform:rotate(180deg)}' +
  '.sn-r{color:#50fa7b !important;font-family:monospace;font-weight:bold;font-size:13px;' +
  'letter-spacing:1px;padding:3px 12px;flex-shrink:0;border:1px solid #222;border-radius:6px;margin:0 3px;background:none}' +
  '.sn-r:first-of-type{margin-left:auto}' +
  '.sn-r:hover{border-color:#1a4a1a;background:rgba(80,250,123,0.04);text-shadow:0 0 8px rgba(80,250,123,0.4)}' +
  '.sn-r.on{color:#fff !important;border-color:#50fa7b;background:rgba(80,250,123,0.06)}' +
  '.sn-h{display:none;font-size:22px;color:#888;padding:0 4px;margin-left:auto;' +
  'flex-shrink:0;line-height:1;background:none;border:none}' +
  '.sn-mn{display:none;align-items:center;color:#ccc;font-size:14px;background:none;' +
  'border:1px solid #333;border-radius:6px;padding:5px 16px;cursor:pointer;' +
  'font-family:system-ui,sans-serif;flex-direction:row;line-height:1;gap:8px}' +
  '.sn-mn:hover{color:#eee;border-color:#555;background:rgba(255,255,255,0.03)}' +
  '.sn-mn:active{color:#eee}' +
  '.sn-mn .mnar{font-size:16px;color:#888;line-height:1;display:inline-block;' +
  'transform:scale(2.5,1.2)}' +
  '.sn-ms{text-align:center;padding:18px 0 8px;color:#888;font-size:10px;' +
  'text-transform:uppercase;letter-spacing:3px;font-weight:600;font-family:system-ui,sans-serif}' +
  /* Dropdown */
  '#sn-dd{position:fixed;top:40px;left:0;right:0;background:rgba(8,8,14,0.98);' +
  'backdrop-filter:blur(16px);border-bottom:1px solid #1a1a2a;z-index:9998;' +
  'max-height:calc(100vh - 48px);overflow-y:auto;padding:0 32px;' +
  'opacity:0;pointer-events:none;transform:translateY(-8px);' +
  'transition:opacity 0.2s,transform 0.2s}' +
  '#sn-dd.open{opacity:1;pointer-events:auto;transform:translateY(0);padding:24px 32px 32px}' +
  '.sn-tr{max-width:1000px;margin:0 auto 16px;padding:0 0 14px;border-bottom:1px solid #1a1a2a}' +
  '.sn-tr h5{font-size:10px;text-transform:uppercase;letter-spacing:2px;font-weight:600;' +
  'margin:0 0 8px}' +
  '.sn-tr .sn-tl{display:flex;flex-wrap:wrap;gap:4px 10px}' +
  '.sn-tr a{padding:3px 0;color:#999;font-size:12px;transition:color 0.15s;' +
  'text-decoration:none;white-space:nowrap}' +
  '.sn-tr a:hover{color:#eee}' +
  '.sn-tr a.cur{color:#ffd700}' +
  '.sn-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:20px;' +
  'max-width:1000px;margin:0 auto}' +
  '.sn-gc h5{font-size:10px;text-transform:uppercase;letter-spacing:2px;font-weight:600;' +
  'margin:0 0 8px;padding:0 0 6px;border-bottom:1px solid #1a1a2a}' +
  '.sn-gc a{display:block;padding:3px 0;color:#999;font-size:12px;transition:color 0.15s;' +
  'text-decoration:none;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
  '.sn-gc a:hover{color:#eee}' +
  '.sn-gc a.cur{color:#ffd700}' +
  /* Mobile overlay */
  '#sn-m{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,8,0.99);' +
  'z-index:10000;display:none;flex-direction:column;overflow-y:auto}' +
  '#sn-m.open{display:flex}' +
  '.sn-mh{display:flex;align-items:center;justify-content:center;padding:0 16px;' +
  'height:44px;border-bottom:1px solid #1a1a2a;flex-shrink:0}' +
  '.sn-mh .sn-mn{display:flex}' +
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
  '.sn-md a{display:block;padding:10px 0;color:#aaa;font-size:15px;text-decoration:none;' +
  'border-bottom:1px solid #0a0a0a}' +
  '.sn-md a:hover{color:#ffd700}' +
  /* Related demos footer */
  '#sn-rel{max-width:800px;margin:40px auto 0;padding:24px 24px 32px;' +
  'border-top:1px solid #151520;font-family:system-ui,sans-serif}' +
  '#sn-rel h4{color:#888;font-size:11px;text-transform:uppercase;letter-spacing:2px;' +
  'margin-bottom:14px;font-weight:600}' +
  '#sn-rel .rl{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}' +
  '#sn-rel .rl a{display:inline-block;padding:7px 16px;border:1px solid #1a1a2a;' +
  'border-radius:8px;color:#bbb;text-decoration:none;font-size:13px;' +
  'transition:all 0.25s;background:#08080e}' +
  '#sn-rel .rl a:hover{border-color:#333;color:#ddd;background:#0e0e18;' +
  'transform:translateY(-1px);box-shadow:0 3px 12px rgba(0,0,0,0.4)}' +
  '#sn-rel .va{color:#888;font-size:11px;text-decoration:none;letter-spacing:1px;' +
  'text-transform:uppercase;transition:color 0.2s}' +
  '#sn-rel .va:hover{color:#ffd700}' +
  '@media(max-width:700px){' +
  '.sn-l{display:none!important}' +
  '.sn-r{display:none}' +
  '.sn-h{display:none}' +
  '.sn-mn{display:flex}' +
  '#sn{padding:0 10px;justify-content:center;height:44px}' +
  'body{padding-top:44px!important}' +
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
h += '<button class="sn-mn" id="sn-mn">Navigation<span class="mnar">\u25BE</span></button>';
nav.innerHTML = h;
document.body.insertBefore(nav, document.body.firstChild);

/* ===== DROPDOWN ===== */
var dd = document.createElement('div');
dd.id = 'sn-dd';
var tutDemos = catDemos['tutorial'] || [];
var dh = '';
if (tutDemos.length) {
  var ti = CATS['tutorial'];
  dh += '<div class="sn-tr"><h5 style="color:' + ti[1] + '">Interactive Atlas</h5><div class="sn-tl">';
  for (var j = 0; j < tutDemos.length; j++) {
    dh += '<a href="' + tutDemos[j] + '.html"' + (tutDemos[j] === key ? ' class="cur"' : '') + '>' + T[tutDemos[j]] + '</a>';
  }
  dh += '</div></div>';
}
dh += '<div class="sn-g">';
for (var i = 0; i < catOrder.length; i++) {
  var ck = catOrder[i], ci = CATS[ck], demos = catDemos[ck];
  if (!demos.length || ck === 'start' || ck === 'tutorial') continue;
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
  '<button class="sn-mn" id="sn-mc">Navigation<span class="mnar">\u25B4</span></button>' +
  '</div><div class="sn-ml">' +
  '<div class="sn-ms">Main</div>' +
  '<a href="index.html" style="color:#ffd700;font-weight:600">970200</a>' +
  '<a href="worldview.html">How the World Works</a>' +
  '<a href="story.html">The Mathematics</a>' +
  '<a href="derive_ax.html">From Nothing</a>' +
  '<a class="rpl" href="repl.html">.ax REPL</a>' +
  '<a class="rpl" href="playground.html">.ax Playground</a>' +
  '<div class="sn-ms" style="margin-top:8px">Interactive Atlas</div>';
var mAtlasOrder = ['tutorial','physics','bio','math','eng','mind'];
for (var i = 0; i < mAtlasOrder.length; i++) {
  var ck = mAtlasOrder[i], ci = CATS[ck], demos = catDemos[ck];
  if (!demos.length) continue;
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
document.getElementById('sn-mn').addEventListener('click', function() {
  mob.classList.add('open');
  document.body.style.overflow = 'hidden';
});
document.getElementById('sn-mc').addEventListener('click', function() {
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
/* ===== HIDE REDUNDANT FLOATING NAV (atlas pages) ===== */
/* Atlas pages have a fixed bottom-right .nav panel with prev/next chapter links.
   Redundant: top nav bar + Explore dropdown + related footer + inline prev/next links. */
var floatNavs = document.querySelectorAll('.nav');
for (var fi = 0; fi < floatNavs.length; fi++) {
  var fn = floatNavs[fi];
  if (fn.querySelector('a') && getComputedStyle(fn).position === 'fixed') {
    fn.style.display = 'none';
  }
}

/* ===== GLOBAL TOOLTIP AUTO-DISMISS (mobile fix) ===== */
/* On touch devices, tooltips shown on touchstart never get a mouseout to dismiss them.
   This observer watches for any tooltip-like element becoming visible and auto-hides after 3s. */
if ('ontouchstart' in window) {
  var _axTipTimer = null;
  document.addEventListener('touchstart', function() {
    clearTimeout(_axTipTimer);
    _axTipTimer = setTimeout(function() {
      var tips = document.querySelectorAll('[id*="tooltip"],[id*="tip"],[id="grid-tooltip"]');
      for (var i = 0; i < tips.length; i++) {
        if (tips[i].style.display !== 'none' && tips[i].style.display !== '') {
          tips[i].style.opacity = '0';
          tips[i].style.transition = 'opacity 0.5s';
          (function(el) {
            setTimeout(function() { el.style.display = 'none'; el.style.opacity = '1'; }, 500);
          })(tips[i]);
        }
      }
    }, 3000);
  }, { passive: true });
}

if (isIndex) return; /* index.html has its own vow footer */
var vf = document.createElement('div');
vf.style.cssText = 'text-align:center;padding:32px 24px 40px;color:#777;font-size:12px;' +
  'font-family:system-ui,sans-serif;border-top:1px solid #1a1a2a;margin-top:40px;line-height:2';
vf.innerHTML = 'This work is and will always be free. No paywall. No copyright. No exceptions.<br>' +
  '<span style="color:#666">If it ever earns anything, every cent goes to the communities that need it most.</span><br>' +
  '<span style="color:#555;font-size:10px">This sacred vow is permanent and irrevocable.</span><br>' +
  '<span style="color:#666;font-size:11px;font-style:italic">\u2014 Anton Alexandrovich Lebed</span>';
document.body.appendChild(vf);
}
if (document.body) init();
else document.addEventListener('DOMContentLoaded', init);
})();
