// nav.js — shared navigation + related demos for all demo pages
// Progressive enhancement: pages work without it. Zero dependencies.
// Injected via <script src="nav.js"></script> before </body>.
(function() {
'use strict';
/* Favicon — inject on every page that loads nav.js */
if (!document.querySelector('link[rel="icon"]')) {
  var ico = document.createElement('link');
  ico.rel = 'icon'; ico.type = 'image/png'; ico.href = 'favicon.png';
  document.head.appendChild(ico);
}
var f = location.pathname.split('/').pop() || '';
if (!f || f === 'index.html') return;

var CATS = {
  start:['Start Here','#ffd700'], physics:['Physics','#4488ff'],
  bio:['Biology','#33dd55'], math:['Mathematics','#ff9900'],
  eng:['Engineering','#ff4040'], mind:['Mind','#aa44ff'],
  tutorial:['Tutorial','#44dddd']
};

var M = {
  worldview:'start',story:'start',derive_ax:'start',repl:'start',
  particles:'physics',alpha:'physics',constants:'physics',turbulence:'physics',
  blackhole:'physics',nuclear:'physics',gravity:'physics',photon:'physics',
  pmns:'physics',three_body_dance:'physics',figure_ground:'physics',
  eternal_sun:'physics',scale_bands:'physics',noxan:'physics',wavebox:'physics',
  sigma_dynamics:'physics',loop:'physics',
  dna:'bio',sleep:'bio',heart:'bio',death:'bio',human_shape:'bio',generations:'bio',
  millennium:'math',hardest:'math',goldbach:'math',coupling:'math',ninedot:'math',
  infinity:'math',bootstrap:'math',symbol:'math',watercycle:'math',genesis:'math',clock24:'math',
  demo_classifier:'eng',ecc_live:'eng',demo_ofdm_vs_wifi:'eng',compression:'eng',
  tokenizer:'eng',k_neural:'eng',demo_ecc:'eng',
  emergence:'mind',conscious:'mind',freewill:'mind',braid:'mind',dimension:'mind',
  ouroboros:'mind',lava_lamp:'mind',sandpile:'mind',music:'mind',
  rose:'math',gap_pairs:'math',depth_quad:'math',fourteen:'math',
  septilix:'bio'
};

/* Short titles for related-demo links */
var T = {
  worldview:'Five Numbers',story:'The Mathematics',derive_ax:'From Nothing',repl:'.ax REPL',
  particles:'Particle Masses',alpha:'Fine Structure',constants:'Physics Constants',turbulence:'Turbulence',
  blackhole:'Black Holes',nuclear:'Nuclear Shells',gravity:'Gravity',photon:'Light Becomes Mass',
  pmns:'Neutrino Mixing',three_body_dance:'Orbital Resonances',figure_ground:'One Force',
  eternal_sun:'Why the Sun Lives',scale_bands:'Scale Bands',noxan:'Cold Thoughts',wavebox:'Standing Waves',
  sigma_dynamics:'How Rings Forget',loop:'Fall Trinity',
  dna:'DNA Codons',sleep:'Sleep Stages',heart:'The Heartbeat',death:'What Death Is',
  human_shape:'Body Is a Ring',generations:'Three Families',
  millennium:'Millennium Problems',hardest:'11 Unsolvables',goldbach:'Goldbach Pairs',
  coupling:'Coupling Landscape',ninedot:'9-Dot Puzzle',infinity:'Infinite from Finite',
  bootstrap:'Why Existence Exists',symbol:'Three Shapes',watercycle:'Water Cycle',genesis:'Genesis',clock24:'24-Hour Clock',
  demo_classifier:'Classifier',ecc_live:'Live ECC',demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'Compression',
  tokenizer:'Tokenizer',k_neural:'Ternary AI',demo_ecc:'ECC Classic',
  emergence:'Emergence',conscious:'Consciousness',freewill:'Free Will',braid:'Braids',dimension:'Dimensions',
  ouroboros:'Ouroboros',lava_lamp:'HYDOR',sandpile:'Sandpile',music:'Music of Primes',
  rose:'Interactive Rose',gap_pairs:'K=3 Gap Gates',depth_quad:'Depth Quadratic',
  fourteen:'The Full Fourteen',septilix:'Seven Petals'
};

var key = f.replace('.html','');
var catKey = M[key];
if (!catKey && key.indexOf('atlas_') === 0) catKey = 'tutorial';
var cat = catKey ? CATS[catKey] : null;

var title = document.title.split(' \u2014 ')[0].split(' | ')[0].split(' - ')[0];

/* === STYLES === */
var s = document.createElement('style');
s.textContent =
  '#sn{position:sticky;top:0;z-index:9999;background:rgba(5,5,8,0.95);' +
  'border-bottom:1px solid #222;padding:0 16px;height:44px;display:flex;align-items:center;' +
  'font-family:system-ui,sans-serif;font-size:14px;backdrop-filter:blur(8px);gap:12px}' +
  '#sn a{color:#888;text-decoration:none;white-space:nowrap;transition:color 0.2s}' +
  '#sn a:hover{color:#ffd700}' +
  '#sn .cat{font-size:11px;padding:2px 8px;border-radius:10px;font-weight:600;' +
  'letter-spacing:0.5px;text-transform:uppercase;text-decoration:none;transition:opacity 0.2s}' +
  '#sn .cat:hover{opacity:0.8;text-decoration:none}' +
  '#sn .ttl{color:#ccc;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;' +
  'font-size:13px}' +
  '#sn .repl{color:#50fa7b;font-family:monospace;font-weight:bold;font-size:13px;' +
  'letter-spacing:1px}' +
  '#sn .repl:hover{text-shadow:0 0 8px rgba(80,250,123,0.4);color:#50fa7b}' +
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
  '@media(max-width:500px){#sn .ttl{display:none}#sn{gap:8px;padding:0 10px}' +
  '#sn-rel{padding:16px 14px 24px}#sn-rel .rl{gap:6px}' +
  '#sn-rel .rl a{padding:6px 12px;font-size:12px}}';
document.head.appendChild(s);

/* === TOP NAV BAR === */
var n = document.createElement('nav');
n.id = 'sn';
var catLink = catKey ? 'index.html#' + catKey : 'index.html';
var h = '<a href="index.html">\u2190 Hub</a>';
if (cat) {
  h += '<a class="cat" href="' + catLink + '" style="background:' + cat[1] + '18;color:' + cat[1] +
       ';border:1px solid ' + cat[1] + '33">' + cat[0] + '</a>';
}
h += '<span class="ttl">' + title + '</span>';
if (f !== 'repl.html') h += '<a class="repl" href="repl.html">.ax</a>';
n.innerHTML = h;
document.body.insertBefore(n, document.body.firstChild);

/* === RELATED DEMOS FOOTER === */
if (catKey && catKey !== 'tutorial') {
  var siblings = [];
  for (var k in M) {
    if (M[k] === catKey && k !== key && T[k]) siblings.push(k);
  }
  /* Fisher-Yates shuffle, pick up to 4 */
  for (var i = siblings.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = siblings[i]; siblings[i] = siblings[j]; siblings[j] = tmp;
  }
  var picks = siblings.slice(0, 4);
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
})();
