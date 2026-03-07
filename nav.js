// nav.js — universal navigation + i18n for antonlebed.com
// Top bar + category dropdown + mobile menu + related footer + vow footer.
// i18n: EN/FR/RU language selector. localStorage persistence. All nav chrome translated.
// Progressive enhancement: pages work without it. Zero dependencies.
// <script src="nav.js"></script> before </body>.
(function() {
'use strict';

/* ===== CRITICAL CSS (immediate — loaded from <head>, prevents FOUC) ===== */
var pre = document.createElement('style');
pre.textContent = 'body{padding-top:40px!important;animation:sn-in 0.15s ease 0.02s both}' +
'@keyframes sn-in{from{opacity:0}to{opacity:1}}' +
'html{overflow-x:hidden;touch-action:manipulation}' +
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

/* ===== GATE: first-time visitors see the puzzle ===== */
if (f !== 'index.html' && f !== '') {
  try {
    if (localStorage.getItem('rose-gate-passed') !== 'true') {
      location.href = 'index.html?return=' + encodeURIComponent(f);
      return;
    }
  } catch(e) {}
}

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
  sigma_dynamics:'physics',superconductor:'physics',loop:'physics',
  dna:'bio',sleep:'bio',heart:'bio',death:'bio',human_shape:'bio',generations:'bio',
  septilix:'bio',
  millennium:'math',hardest:'math',hardest_mind:'math',goldbach:'math',coupling:'math',lattice:'math',ninedot:'math',
  infinity:'math',bootstrap:'math',symbol:'math',watercycle:'math',genesis:'math',
  clock24:'math',rose:'math',gap_pairs:'math',depth_quad:'math',fourteen:'math',
  sm:'physics',quantum:'physics',thermo:'physics',chemistry:'physics',em:'physics',gr:'physics',cosmo:'physics',classical:'physics',statmech:'physics',condensed:'physics',optics:'physics',acoustics:'physics',
  oracle:'eng',challenge:'eng',
  demo_classifier:'eng',ecc_live:'eng',demo_ofdm_vs_wifi:'eng',compression:'eng',
  tokenizer:'eng',k_neural:'eng',demo_ecc:'eng',
  emergence:'mind',conscious:'mind',freewill:'mind',braid:'mind',dimension:'mind',
  ouroboros:'mind',lava_lamp:'mind',sandpile:'mind',music:'mind',culture:'mind',biology:'mind',
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
  sigma_dynamics:'How Rings Forget',superconductor:'The Shape of Cold',loop:'Fall Trinity',
  dna:'DNA Codons',sleep:'Sleep Stages',heart:'The Heartbeat',death:'What Death Is',
  human_shape:'Your Body Is a Ring',generations:'Three Families',septilix:'Seven Petals',
  millennium:'Millennium Problems',hardest:'Hardest Problems',hardest_mind:'Hardest Questions',goldbach:'Goldbach Pairs',
  coupling:'Coupling Landscape',lattice:'The 420 Lattice',ninedot:'9-Dot Puzzle',infinity:'Infinite from Finite',
  bootstrap:'Why Existence Exists',symbol:'Three Shapes',watercycle:'Water Cycle',genesis:'Genesis',
  clock24:'24-Hour Clock',rose:'Interactive Rose',gap_pairs:'K=3 Gap Gates',depth_quad:'Depth Quadratic',
  fourteen:'The Full Fourteen',
  sm:'25/25 Standard Model',quantum:'Quantum Mechanics',thermo:'Thermodynamics',chemistry:'Chemistry',em:'Electromagnetism',gr:'General Relativity',cosmo:'Cosmology',classical:'Classical Mechanics',statmech:'Statistical Mechanics',condensed:'Condensed Matter',optics:'Optics',acoustics:'Acoustics',
  oracle:'Try Any Number',challenge:'Why This Ring?',
  demo_classifier:'Classifier',ecc_live:'Live Error Correction',demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'CRT Compression',
  tokenizer:'CRT Tokenizer',k_neural:'Ternary AI',demo_ecc:'ECC Classic',
  emergence:'Emergence',conscious:'Consciousness',freewill:'Free Will',braid:'Braids',dimension:'Dimensions',
  ouroboros:'Ouroboros',lava_lamp:'HYDOR',sandpile:'Sandpile',music:'Music of Primes',culture:'Culture & Institutions',biology:'Biology from Ten Terms',
  atlas_01_what_is_2310:'0. The Chain',atlas_02_two_rings:'1. Three Rings',
  atlas_03_crt:'2. Five Petals',atlas_04_carousel:'3. Carousel',atlas_05_eigenvalues:'4. Eigenvalues',
  atlas_06_units:'5. Units',atlas_07_kingdoms:'6. Kingdoms',atlas_08_breakthroughs:'7. Breakthroughs',
  atlas_09_demos:'8. Demos',atlas_10_millennium:'9. Millennium',atlas_11_net:"10. Indra's Net",
  atlas_12_shadow_polynomial:'11. Shadow Polynomial',atlas_13_biological_braid:'12. Bio Braid',
  atlas_14_solar_ladder:'13. Solar Ladder'
};

/* ===== i18n (EN/FR/RU) ===== */
var axLang=(function(){try{var l=localStorage.getItem('ax-lang');if(l==='fr'||l==='ru')return l}catch(e){}return'en'})();
if(axLang!=='en')document.documentElement.lang=axLang;
var _i18n={
  nav:{howWorld:['How the World Works','Comment fonctionne le monde','\u041a\u0430\u043a \u0443\u0441\u0442\u0440\u043e\u0435\u043d \u043c\u0438\u0440'],
    theMath:['The Mathematics','Les math\u00e9matiques','\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430'],
    fromNothing:['From Nothing','\u00c0 partir de rien','\u0418\u0437 \u043d\u0438\u0447\u0435\u0433\u043e'],
    explore:['Explore','Explorer','\u041e\u0431\u0437\u043e\u0440'],
    navLabel:['Navigation','Navigation','\u041d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u044f'],
    main:['Main','Principal','\u0413\u043b\u0430\u0432\u043d\u0430\u044f'],
    atlas:['Interactive Atlas','Atlas interactif','\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0430\u0442\u043b\u0430\u0441'],
    moreIn:['Explore more in','Voir plus dans','\u0415\u0449\u0451 \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435'],
    allCat:['All','Tout','\u0412\u0441\u0435']},
  vow:[
    ['This work is and will always be free. No paywall. No copyright. No exceptions.',
     'Ce travail est et sera toujours gratuit. Pas de mur payant. Pas de copyright. Sans exception.',
     '\u042d\u0442\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 \u0431\u044b\u043b\u0430 \u0438 \u0432\u0441\u0435\u0433\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\u0439. \u041d\u0438\u043a\u0430\u043a\u0438\u0445 \u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u0441\u0442\u0435\u043d. \u041d\u0438\u043a\u0430\u043a\u0438\u0445 \u0430\u0432\u0442\u043e\u0440\u0441\u043a\u0438\u0445 \u043f\u0440\u0430\u0432. \u0411\u0435\u0437 \u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439.'],
    ['If it ever earns anything, every cent goes to the communities that need it most.',
     "S'il rapporte quoi que ce soit, chaque centime ira aux communaut\u00e9s qui en ont le plus besoin.",
     '\u0415\u0441\u043b\u0438 \u043e\u043d\u0430 \u043a\u043e\u0433\u0434\u0430-\u043d\u0438\u0431\u0443\u0434\u044c \u043f\u0440\u0438\u043d\u0435\u0441\u0451\u0442 \u0434\u043e\u0445\u043e\u0434, \u043a\u0430\u0436\u0434\u0430\u044f \u043a\u043e\u043f\u0435\u0439\u043a\u0430 \u043f\u043e\u0439\u0434\u0451\u0442 \u0442\u0435\u043c, \u043a\u043e\u043c\u0443 \u043e\u043d\u0430 \u043d\u0443\u0436\u043d\u0435\u0435 \u0432\u0441\u0435\u0433\u043e.'],
    ['This sacred vow is permanent and irrevocable.',
     'Ce v\u0153u sacr\u00e9 est permanent et irr\u00e9vocable.',
     '\u042d\u0442\u043e\u0442 \u0441\u0432\u044f\u0449\u0435\u043d\u043d\u044b\u0439 \u043e\u0431\u0435\u0442 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u0435\u043d \u0438 \u043d\u0435\u043e\u0431\u0440\u0430\u0442\u0438\u043c.'],
    ['\u2014 Anton Alexandrovich Lebed','\u2014 Anton Alexandrovitch Lebed',
     '\u2014 \u0410\u043d\u0442\u043e\u043d \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447 \u041b\u0435\u0431\u0435\u0434\u044c']]
};
var _li=axLang==='fr'?1:axLang==='ru'?2:0;
function tr(k){var v=_i18n.nav[k];return v?v[_li]:k}

/* Override category names and demo titles for current language */
if(_li>0){
  var _catTr={fr:{start:'Commencer ici',physics:'Physique',bio:'Biologie',math:'Math\u00e9matiques',eng:'Ing\u00e9nierie',mind:'Esprit',tutorial:'Tutoriel'},
    ru:{start:'\u041d\u0430\u0447\u0430\u043b\u043e',physics:'\u0424\u0438\u0437\u0438\u043a\u0430',bio:'\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f',math:'\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430',eng:'\u0418\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f',mind:'\u0420\u0430\u0437\u0443\u043c',tutorial:'\u0423\u0447\u0435\u0431\u043d\u0438\u043a'}};
  var _ct=_catTr[axLang];if(_ct)for(var _c in _ct)if(CATS[_c])CATS[_c][0]=_ct[_c];
  var _titles={fr:{
    worldview:'Comment fonctionne le monde',story:'Les math\u00e9matiques',derive_ax:'\u00c0 partir de rien',
    particles:'Masses des particules',alpha:'Constante de structure fine',
    constants:'Constantes physiques',turbulence:'Turbulence et m\u00e9tabolisme',
    blackhole:'Trous noirs',nuclear:'Couches nucl\u00e9aires',gravity:'Gravit\u00e9',
    photon:'La lumi\u00e8re devient masse',pmns:'M\u00e9lange des neutrinos',
    three_body_dance:'R\u00e9sonances orbitales',figure_ground:'Une seule force',
    eternal_sun:'Pourquoi le Soleil vit',scale_bands:"Bandes d'\u00e9chelle",
    noxan:'Pens\u00e9es froides',wavebox:'Ondes stationnaires',
    sigma_dynamics:'Comment les anneaux oublient',superconductor:'La forme du froid',loop:'Trinit\u00e9 de la chute',
    dna:'Codons ADN',sleep:'Phases du sommeil',heart:'Le battement du c\u0153ur',
    death:"Ce qu'est la mort",human_shape:'Votre corps est un anneau',
    generations:'Trois familles',septilix:'Sept p\u00e9tales',
    millennium:'Probl\u00e8mes du mill\u00e9naire',hardest:'Probl\u00e8mes les plus durs',hardest_mind:'Questions les plus dures',
    goldbach:'Paires de Goldbach',coupling:'Paysage de couplage',lattice:'Le Treillis 420',
    ninedot:'Puzzle des 9 points',infinity:"L'infini du fini",
    bootstrap:"Pourquoi l'existence existe",symbol:'Trois formes',
    watercycle:"Cycle de l'eau",genesis:'Gen\u00e8se',clock24:'Horloge 24h',
    rose:'Rose interactive',gap_pairs:'Portes K=3',
    depth_quad:'Quadratique de profondeur',fourteen:'Les quatorze',
    sm:'25/25 Modele Standard',quantum:'M\u00e9canique quantique',thermo:'Thermodynamique',chemistry:'Chimie',em:'\u00c9lectromagn\u00e9tisme',gr:'Relativit\u00e9 g\u00e9n\u00e9rale',cosmo:'Cosmologie',classical:'M\u00e9canique classique',statmech:'M\u00e9canique statistique',condensed:'Mati\u00e8re condens\u00e9e',optics:'Optique',acoustics:'Acoustique',
    oracle:'Essayez un nombre',
    demo_classifier:'Classifieur',ecc_live:"Correction d'erreurs",
    demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'Compression CRT',
    tokenizer:'Tokeniseur CRT',k_neural:'IA ternaire',demo_ecc:'ECC classique',
    emergence:'\u00c9mergence',conscious:'Conscience',freewill:'Libre arbitre',
    braid:'Tresses',dimension:'Dimensions',ouroboros:'Ouroboros',
    lava_lamp:'HYDOR',sandpile:'Tas de sable',music:'Musique des premiers',culture:'Culture & Institutions',biology:'Biologie en dix termes',
    atlas_01_what_is_2310:'0. La Cha\u00eene',atlas_02_two_rings:'1. Trois anneaux',
    atlas_03_crt:'2. Cinq p\u00e9tales',atlas_04_carousel:'3. Carrousel',
    atlas_05_eigenvalues:'4. Valeurs propres',atlas_06_units:'5. Unit\u00e9s',
    atlas_07_kingdoms:'6. Royaumes',atlas_08_breakthroughs:'7. Perc\u00e9es',
    atlas_09_demos:'8. D\u00e9mos',atlas_10_millennium:'9. Mill\u00e9naire',
    atlas_11_net:"10. Filet d'Indra",atlas_12_shadow_polynomial:"11. Polyn\u00f4me d'ombre",
    atlas_13_biological_braid:'12. Tresse biologique',atlas_14_solar_ladder:'13. \u00c9chelle solaire',
    repl:'.ax REPL',playground:'.ax Bac \u00e0 sable'},
  ru:{
    worldview:'\u041a\u0430\u043a \u0443\u0441\u0442\u0440\u043e\u0435\u043d \u043c\u0438\u0440',story:'\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430',derive_ax:'\u0418\u0437 \u043d\u0438\u0447\u0435\u0433\u043e',
    particles:'\u041c\u0430\u0441\u0441\u044b \u0447\u0430\u0441\u0442\u0438\u0446',alpha:'\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u0430\u044f \u0442\u043e\u043d\u043a\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b',
    constants:'\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u044b',turbulence:'\u0422\u0443\u0440\u0431\u0443\u043b\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c \u0438 \u043c\u0435\u0442\u0430\u0431\u043e\u043b\u0438\u0437\u043c',
    blackhole:'\u0427\u0451\u0440\u043d\u044b\u0435 \u0434\u044b\u0440\u044b',nuclear:'\u042f\u0434\u0435\u0440\u043d\u044b\u0435 \u043e\u0431\u043e\u043b\u043e\u0447\u043a\u0438',gravity:'\u0413\u0440\u0430\u0432\u0438\u0442\u0430\u0446\u0438\u044f',
    photon:'\u0421\u0432\u0435\u0442 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u043c\u0430\u0441\u0441\u043e\u0439',pmns:'\u0421\u043c\u0435\u0448\u0438\u0432\u0430\u043d\u0438\u0435 \u043d\u0435\u0439\u0442\u0440\u0438\u043d\u043e',
    three_body_dance:'\u041e\u0440\u0431\u0438\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0437\u043e\u043d\u0430\u043d\u0441\u044b',figure_ground:'\u041e\u0434\u043d\u0430 \u0441\u0438\u043b\u0430',
    eternal_sun:'\u041f\u043e\u0447\u0435\u043c\u0443 \u0421\u043e\u043b\u043d\u0446\u0435 \u0436\u0438\u0432\u0451\u0442',scale_bands:'\u041c\u0430\u0441\u0448\u0442\u0430\u0431\u043d\u044b\u0435 \u043f\u043e\u043b\u043e\u0441\u044b',
    noxan:'\u0425\u043e\u043b\u043e\u0434\u043d\u044b\u0435 \u043c\u044b\u0441\u043b\u0438',wavebox:'\u0421\u0442\u043e\u044f\u0447\u0438\u0435 \u0432\u043e\u043b\u043d\u044b',
    sigma_dynamics:'\u041a\u0430\u043a \u043a\u043e\u043b\u044c\u0446\u0430 \u0437\u0430\u0431\u044b\u0432\u0430\u044e\u0442',superconductor:'\u0424\u043e\u0440\u043c\u0430 \u0445\u043e\u043b\u043e\u0434\u0430',loop:'\u0422\u0440\u043e\u0438\u0446\u0430 \u043f\u0430\u0434\u0435\u043d\u0438\u044f',
    dna:'\u041a\u043e\u0434\u043e\u043d\u044b \u0414\u041d\u041a',sleep:'\u0424\u0430\u0437\u044b \u0441\u043d\u0430',heart:'\u0411\u0438\u0435\u043d\u0438\u0435 \u0441\u0435\u0440\u0434\u0446\u0430',
    death:'\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0441\u043c\u0435\u0440\u0442\u044c',human_shape:'\u0412\u0430\u0448\u0435 \u0442\u0435\u043b\u043e \u2014 \u043a\u043e\u043b\u044c\u0446\u043e',
    generations:'\u0422\u0440\u0438 \u0441\u0435\u043c\u0435\u0439\u0441\u0442\u0432\u0430',septilix:'\u0421\u0435\u043c\u044c \u043b\u0435\u043f\u0435\u0441\u0442\u043a\u043e\u0432',
    millennium:'\u0417\u0430\u0434\u0430\u0447\u0438 \u0442\u044b\u0441\u044f\u0447\u0435\u043b\u0435\u0442\u0438\u044f',hardest:'\u0422\u0440\u0443\u0434\u043d\u0435\u0439\u0448\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438',hardest_mind:'\u0422\u0440\u0443\u0434\u043d\u0435\u0439\u0448\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b',
    goldbach:'\u041f\u0430\u0440\u044b \u0413\u043e\u043b\u044c\u0434\u0431\u0430\u0445\u0430',coupling:'\u041b\u0430\u043d\u0434\u0448\u0430\u0444\u0442 \u0441\u0432\u044f\u0437\u0438',lattice:'\u0420\u0435\u0448\u0451\u0442\u043a\u0430 420',
    ninedot:'\u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 9 \u0442\u043e\u0447\u0435\u043a',infinity:'\u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0438\u0437 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0433\u043e',
    bootstrap:'\u041f\u043e\u0447\u0435\u043c\u0443 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442',symbol:'\u0422\u0440\u0438 \u0444\u043e\u0440\u043c\u044b',
    watercycle:'\u041a\u0440\u0443\u0433\u043e\u0432\u043e\u0440\u043e\u0442 \u0432\u043e\u0434\u044b',genesis:'\u0413\u0435\u043d\u0435\u0437\u0438\u0441',clock24:'24-\u0447\u0430\u0441\u043e\u0432\u044b\u0435 \u0447\u0430\u0441\u044b',
    rose:'\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0440\u043e\u0437\u0430',gap_pairs:'\u0412\u043e\u0440\u043e\u0442\u0430 K=3',
    depth_quad:'\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u0430 \u0433\u043b\u0443\u0431\u0438\u043d\u044b',fourteen:'\u0412\u0441\u0435 \u0447\u0435\u0442\u044b\u0440\u043d\u0430\u0434\u0446\u0430\u0442\u044c',
    sm:'25/25 \u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c',quantum:'\u041a\u0432\u0430\u043d\u0442\u043e\u0432\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',thermo:'\u0422\u0435\u0440\u043c\u043e\u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0430',chemistry:'\u0425\u0438\u043c\u0438\u044f',em:'\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043c\u0430\u0433\u043d\u0435\u0442\u0438\u0437\u043c',gr:'\u041e\u0431\u0449\u0430\u044f \u0442\u0435\u043e\u0440\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438',cosmo:'\u041a\u043e\u0441\u043c\u043e\u043b\u043e\u0433\u0438\u044f',classical:'\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',statmech:'\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',condensed:'\u041a\u043e\u043d\u0434\u0435\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u044f',optics:'\u041e\u043f\u0442\u0438\u043a\u0430',acoustics:'\u0410\u043a\u0443\u0441\u0442\u0438\u043a\u0430',
    oracle:'\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043b\u044e\u0431\u043e\u0435 \u0447\u0438\u0441\u043b\u043e',
    demo_classifier:'\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440',ecc_live:'\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f \u043e\u0448\u0438\u0431\u043e\u043a',
    demo_ofdm_vs_wifi:'OFDM \u043f\u0440\u043e\u0442\u0438\u0432 WiFi',compression:'CRT-\u0441\u0436\u0430\u0442\u0438\u0435',
    tokenizer:'CRT-\u0442\u043e\u043a\u0435\u043d\u0438\u0437\u0430\u0442\u043e\u0440',k_neural:'\u0422\u0435\u0440\u043d\u0430\u0440\u043d\u044b\u0439 \u0418\u0418',demo_ecc:'ECC (\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439)',
    emergence:'\u042d\u043c\u0435\u0440\u0434\u0436\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c',conscious:'\u0421\u043e\u0437\u043d\u0430\u043d\u0438\u0435',freewill:'\u0421\u0432\u043e\u0431\u043e\u0434\u0430 \u0432\u043e\u043b\u0438',
    braid:'\u041a\u043e\u0441\u044b',dimension:'\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',ouroboros:'\u0423\u0440\u043e\u0431\u043e\u0440\u043e\u0441',
    lava_lamp:'HYDOR',sandpile:'\u041f\u0435\u0441\u043e\u0447\u043d\u0430\u044f \u043a\u0443\u0447\u0430',music:'\u041c\u0443\u0437\u044b\u043a\u0430 \u043f\u0440\u043e\u0441\u0442\u044b\u0445 \u0447\u0438\u0441\u0435\u043b',culture:'\u041a\u0443\u043b\u044c\u0442\u0443\u0440\u0430 \u0438 \u0438\u043d\u0441\u0442\u0438\u0442\u0443\u0442\u044b',biology:'\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f \u0438\u0437 \u0434\u0435\u0441\u044f\u0442\u0438 \u0442\u0435\u0440\u043c\u0438\u043d\u043e\u0432',
    atlas_01_what_is_2310:'0. \u0426\u0435\u043f\u043e\u0447\u043a\u0430',atlas_02_two_rings:'1. \u0422\u0440\u0438 \u043a\u043e\u043b\u044c\u0446\u0430',
    atlas_03_crt:'2. \u041f\u044f\u0442\u044c \u043b\u0435\u043f\u0435\u0441\u0442\u043a\u043e\u0432',atlas_04_carousel:'3. \u041a\u0430\u0440\u0443\u0441\u0435\u043b\u044c',
    atlas_05_eigenvalues:'4. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',atlas_06_units:'5. \u0415\u0434\u0438\u043d\u0438\u0446\u044b',
    atlas_07_kingdoms:'6. \u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0441\u0442\u0432\u0430',atlas_08_breakthroughs:'7. \u041f\u0440\u043e\u0440\u044b\u0432\u044b',
    atlas_09_demos:'8. \u0414\u0435\u043c\u043e',atlas_10_millennium:'9. \u0422\u044b\u0441\u044f\u0447\u0435\u043b\u0435\u0442\u0438\u0435',
    atlas_11_net:'10. \u0421\u0435\u0442\u044c \u0418\u043d\u0434\u0440\u044b',atlas_12_shadow_polynomial:'11. \u0422\u0435\u043d\u0435\u0432\u043e\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c',
    atlas_13_biological_braid:'12. \u0411\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043a\u043e\u0441\u0430',
    atlas_14_solar_ladder:'13. \u0421\u043e\u043b\u043d\u0435\u0447\u043d\u0430\u044f \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u0430',
    repl:'.ax REPL',playground:'.ax \u041f\u0435\u0441\u043e\u0447\u043d\u0438\u0446\u0430'}};
  var _tm=_titles[axLang];if(_tm)for(var _k in _tm)T[_k]=_tm[_k];
}

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
  '.sn-ld{position:relative;flex-shrink:0}' +
  '.sn-lang{padding:3px 8px;color:#888;font-size:11px;font-weight:600;letter-spacing:1px;' +
  'border:1px solid #222;border-radius:6px;margin:0 3px;background:none;' +
  'font-family:system-ui,sans-serif;cursor:pointer;transition:color 0.2s,border-color 0.2s}' +
  '.sn-lang:hover{color:#ffd700;border-color:#444}' +
  '.sn-lp{position:absolute;top:calc(100% + 4px);right:0;background:rgba(8,8,14,0.98);' +
  'border:1px solid #222;border-radius:6px;display:none;min-width:110px;z-index:10000;' +
  'backdrop-filter:blur(12px);padding:4px 0}' +
  '.sn-ld.open .sn-lp{display:block}' +
  '.sn-lp button{display:block;width:100%;padding:7px 14px;color:#888;font-size:12px;' +
  'background:none;border:none;cursor:pointer;text-align:left;font-family:system-ui,sans-serif;' +
  'transition:color 0.15s,background 0.15s;white-space:nowrap}' +
  '.sn-lp button:hover{color:#ffd700;background:rgba(255,215,0,0.04)}' +
  '.sn-lp button.cur{color:#ffd700}' +
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
  '.sn-ld{position:absolute!important;right:10px!important}' +
  '#sn{padding:0 10px;justify-content:center;height:44px}' +
  'body{padding-top:44px!important}' +
  '#sn-rel{padding:16px 14px 24px}#sn-rel .rl{gap:6px}' +
  '#sn-rel .rl a{padding:6px 12px;font-size:12px}}';
document.head.appendChild(s);

/* ===== INLINE SVG FLAGS (cross-platform, zero deps) ===== */
function _fl(l){
  var w=20,h=14,r='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+w+' '+h+'" style="display:inline-block;width:'+w+'px;height:'+h+'px;vertical-align:middle;border-radius:2px;border:1px solid rgba(255,255,255,0.15)">';
  if(l==='fr')return r+'<rect fill="#002395" width="6.67" height="'+h+'"/><rect x="6.67" fill="#fff" width="6.66" height="'+h+'"/><rect x="13.33" fill="#ED2939" width="6.67" height="'+h+'"/></svg>';
  if(l==='ru')return r+'<rect fill="#fff" width="'+w+'" height="4.67"/><rect y="4.67" fill="#0039A6" width="'+w+'" height="4.66"/><rect y="9.33" fill="#D52B1E" width="'+w+'" height="4.67"/></svg>';
  /* EN: simplified Union Jack */
  return r+'<rect fill="#012169" width="'+w+'" height="'+h+'"/><path d="M0 0L'+w+' '+h+'M'+w+' 0L0 '+h+'" stroke="#fff" stroke-width="2.5"/><path d="M0 0L'+w+' '+h+'M'+w+' 0L0 '+h+'" stroke="#C8102E" stroke-width="1"/><path d="M'+w/2+' 0v'+h+'M0 '+h/2+'h'+w+'" stroke="#fff" stroke-width="4"/><path d="M'+w/2+' 0v'+h+'M0 '+h/2+'h'+w+'" stroke="#C8102E" stroke-width="2.5"/></svg>';
}

/* ===== TOP NAV BAR ===== */
var nav = document.createElement('nav');
nav.id = 'sn';
var h = '<div class="sn-l">' +
  '<a class="sn-b" href="index.html">970200</a>' +
  '<a class="sn-k' + (isWorld ? ' on' : '') + '" href="worldview.html">' + tr('howWorld') + '</a>' +
  '<a class="sn-k' + (isMath ? ' on' : '') + '" href="story.html">' + tr('theMath') + '</a>' +
  '<a class="sn-k' + (isDerive ? ' on' : '') + '" href="derive_ax.html">' + tr('fromNothing') + '</a>' +
  '<button class="sn-x' + (isExplore ? ' on' : '') + '" id="sn-xp">' + tr('explore') + ' <span class="ar">\u25BE</span></button>' +
  '</div>' +
  '<a class="sn-r' + (isRepl ? ' on' : '') + '" href="repl.html">.ax REPL</a>' +
  '<a class="sn-r sn-rp' + (isPlay ? ' on' : '') + '" href="playground.html">Playground</a>' +
  '<div class="sn-ld" id="sn-ld"><button class="sn-lang">' +
  _fl(['en','fr','ru'][_li]) +
  ' \u25BE</button><div class="sn-lp">' +
  '<button data-lang="en"' + (_li===0?' class="cur"':'') + '>' + _fl('en') + ' English</button>' +
  '<button data-lang="fr"' + (_li===1?' class="cur"':'') + '>' + _fl('fr') + ' Fran\u00e7ais</button>' +
  '<button data-lang="ru"' + (_li===2?' class="cur"':'') + '>' + _fl('ru') + ' \u0420\u0443\u0441\u0441\u043a\u0438\u0439</button>' +
  '</div></div>';
h += '<button class="sn-h" id="sn-bg">\u2630</button>';
h += '<button class="sn-mn" id="sn-mn">' + tr('navLabel') + '<span class="mnar">\u25BE</span></button>';
nav.innerHTML = h;
document.body.insertBefore(nav, document.body.firstChild);

/* ===== DROPDOWN ===== */
var dd = document.createElement('div');
dd.id = 'sn-dd';
var tutDemos = catDemos['tutorial'] || [];
var dh = '';
if (tutDemos.length) {
  var ti = CATS['tutorial'];
  dh += '<div class="sn-tr"><h5 style="color:' + ti[1] + '">' + tr('atlas') + '</h5><div class="sn-tl">';
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
  '<button class="sn-mn" id="sn-mc">' + tr('navLabel') + '<span class="mnar">\u25B4</span></button>' +
  '</div><div class="sn-ml">' +
  '<div class="sn-ms">' + tr('main') + '</div>' +
  '<a href="index.html" style="color:#ffd700;font-weight:600">970200</a>' +
  '<a href="worldview.html">' + tr('howWorld') + '</a>' +
  '<a href="story.html">' + tr('theMath') + '</a>' +
  '<a href="derive_ax.html">' + tr('fromNothing') + '</a>' +
  '<a class="rpl" href="repl.html">.ax REPL</a>' +
  '<a class="rpl" href="playground.html">.ax Playground</a>' +
  '<div class="sn-ms" style="margin-top:8px">' + tr('atlas') + '</div>';
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

/* ===== LANGUAGE SWITCHER (dropdown) ===== */
function setLang(lang){try{localStorage.setItem('ax-lang',lang)}catch(e){}location.reload();}
var ld=document.getElementById('sn-ld');
if(ld){
  ld.querySelector('.sn-lang').addEventListener('click',function(e){e.stopPropagation();ld.classList.toggle('open')});
  var lps=ld.querySelectorAll('.sn-lp button');
  for(var li=0;li<lps.length;li++)lps[li].addEventListener('click',function(){setLang(this.getAttribute('data-lang'))});
}
document.addEventListener('click',function(e){if(ld&&!ld.contains(e.target))ld.classList.remove('open')});

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
    var rh = '<h4>' + tr('moreIn') + ' ' + cat[0] + '</h4><div class="rl">';
    for (var i = 0; i < picks.length; i++) {
      rh += '<a href="' + picks[i] + '.html" style="border-left:2px solid ' + cat[1] + '44">' + T[picks[i]] + '</a>';
    }
    rh += '</div><a class="va" href="' + catLink + '">' + tr('allCat') + ' ' + cat[0] + ' \u2192</a>';
    rel.innerHTML = rh;
    document.body.appendChild(rel);
  }
}

/* ===== VOW FOOTER ===== */
/* ===== HIDE REDUNDANT FLOATING NAV (atlas pages) ===== */
/* Atlas pages have a fixed bottom-right .nav panel with prev/next chapter links.
   Redundant: top nav bar + Explore dropdown + related footer + inline prev/next links.
   Deferred to avoid forced layout reflow (getComputedStyle) during init. */
requestAnimationFrame(function() {
  var floatNavs = document.querySelectorAll('.nav');
  for (var fi = 0; fi < floatNavs.length; fi++) {
    var fn = floatNavs[fi];
    if (fn.querySelector('a') && getComputedStyle(fn).position === 'fixed') {
      fn.style.display = 'none';
    }
  }
});

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

/* Expose language for page-level translation scripts */
window.axLang = axLang;
window.axLi = _li;

if (isIndex || isWorld) return; /* index + worldview have their own vow footers */
var vf = document.createElement('div');
vf.style.cssText = 'text-align:center;padding:32px 24px 40px;color:#777;font-size:12px;' +
  'font-family:system-ui,sans-serif;border-top:1px solid #1a1a2a;margin-top:40px;line-height:2';
var _vow = _i18n.vow;
var _srcLabel=['Source code','Code source','\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u043e\u0434'];
var _pdLabel=['Public domain (Unlicense)','Domaine public (Unlicense)','\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0434\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 (Unlicense)'];
vf.innerHTML = _vow[0][_li] + '<br>' +
  '<span style="color:#666">' + _vow[1][_li] + '</span><br>' +
  '<span style="color:#555;font-size:10px">' + _vow[2][_li] + '</span><br>' +
  '<span style="color:#666;font-size:11px;font-style:italic">' + _vow[3][_li] + '</span>' +
  '<div style="margin-top:16px;padding-top:12px;border-top:1px solid #111">' +
  '<a href="https://github.com/antonlebed/antonlebed.com" style="color:#555;font-size:11px;text-decoration:none;letter-spacing:0.5px" ' +
  'onmouseover="this.style.color=\'#888\'" onmouseout="this.style.color=\'#555\'">' +
  _srcLabel[_li] + ' \u00b7 ' + _pdLabel[_li] + '</a></div>';
document.body.appendChild(vf);
}
if (document.body) init();
else document.addEventListener('DOMContentLoaded', init);
})();
