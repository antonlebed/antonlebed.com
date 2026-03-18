// nav.js — universal navigation + i18n for antonlebed.com
// Top bar + category dropdown + mobile menu + related footer + vow footer.
// i18n: EN/FR/RU/DE/NL language selector. localStorage persistence. All nav chrome translated.
// Progressive enhancement: pages work without it. Zero dependencies.
// <link rel="stylesheet" href="nav-critical.css"> + <script src="nav.js" defer></script>
// nav-critical.css has body{padding-top:40px} + html{overflow-x:hidden} (prevents CLS).
// nav.js deferred: non-render-blocking, executes after DOM parsing.
(function() {
'use strict';

/* ===== SUPPLEMENTAL CSS (layout-stable rules injected after DOM parse) ===== */
var pre = document.createElement('style');
pre.textContent = 'body{animation:sn-in 0.15s ease 0.02s both}' +
'@keyframes sn-in{from{opacity:0}to{opacity:1}}' +
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
/* ===== SEO + AI DISCOVERABILITY (S855) ===== */
/* Inject canonical, robots, and fallback meta description for pages that lack them */
(function(){
  var pg = location.pathname.split('/').pop().replace('.html','') || 'index';
  var url = 'https://antonlebed.com/' + pg + '.html';
  /* Canonical URL */
  if (!document.querySelector('link[rel="canonical"]')) {
    var can = document.createElement('link');
    can.rel = 'canonical'; can.href = url;
    document.head.appendChild(can);
  }
  /* Robots: index, follow */
  if (!document.querySelector('meta[name="robots"]')) {
    var rob = document.createElement('meta');
    rob.name = 'robots'; rob.content = 'index, follow';
    document.head.appendChild(rob);
  }
  /* Fallback meta description from nav title map (for pages without hand-written descriptions) */
  if (!document.querySelector('meta[name="description"]')) {
    var D = {
      arc_demo:'ARC-AGI puzzle solver demo. Watch .ax solve spatial reasoning tasks with CRT decomposition.',
      arcsine_cumulant:'Arcsine law cumulants derived from the 108-ring lattice. Interactive visualization.',
      ax_games:'Five games built with the .ax language. Rose, eigenvalue walk, pong, kingdom, axiom survivor.',
      bernoulli:'Bernoulli numbers from ring structure. The lambda=420 connection to zeta values.',
      cdma_demo:'Spread spectrum communication via CRT residues. Interactive demo.',
      chemistry:'Periodic table structure from five primes. Why elements group the way they do.',
      consensus_demo:'Byzantine consensus protocol using CRT decomposition. Interactive simulation.',
      crt_hash_demo:'Hash function built from Chinese Remainder Theorem. Collision-free by construction.',
      crt_index_demo:'Database indexing via CRT decomposition. O(1) lookup on structured data.',
      crt_keyexchange_demo:'Diffie-Hellman style key exchange using CRT channels. Interactive demo.',
      crt_rng:'Random number generator from CRT residue mixing. Provable uniformity.',
      crt_train_demo:'Neural network training using CRT decomposition. Backprop on ring structure.',
      cunningham:'The two Cunningham chains through the five primes. Why they stop at 13.',
      cyclotomic_fibonacci:'Fibonacci meets cyclotomic polynomials at the five primes. Bridge theorem.',
      d_power_gaussian:'D-power Gaussian primes. How 2^n traces structure in Z[i] mod 970200.',
      decality:'The ten terms of the axiom. Why exactly ten, and what each one does.',
      egg:'From egg to organism. Embryonic development mirrors ring structure.',
      eigenvalue_swim:'Swim through the eigenvalue landscape. Interactive 3D visualization.',
      equator:'The equatorial symmetry of Z/970200Z. Where mirror meets identity.',
      fano_e8:'Bridge from the Fano plane to E8 through the five primes.',
      figurate_bridge:'Triangular, square, pentagonal numbers meet CRT decomposition.',
      fountain_codes:'Fountain codes from CRT — rateless erasure correction. Interactive demo.',
      golden_ratio:'The golden ratio emerges from the ring. phi and Fibonacci in Z/970200Z.',
      gpu_demo:'GPU-accelerated CRT computation via WebGPU. Parallel ring arithmetic.',
      gravastar:'The gravastar hypothesis. Black hole interiors as ring projections.',
      image_filter_demo:'Image filtering using CRT channel separation. Interactive demo.',
      k_squared_stop:'Why does the chain stop at K²=9? The closure theorem.',
      lambda_chain:'Lambda=420 and the chain of LCMs. Why 420 is universal.',
      lie_algebra:'Lie algebra census from the ring. Exceptional groups and five primes.',
      mesh_demo:'Mesh networking protocol using CRT routing. Three ESP32 boards.',
      mirror:'The mirror automorphism n → N-n. Why 970199 is not zero.',
      mirror_cost:'The cost of reflection. What the mirror destroys and preserves.',
      monster_moonshine:'Monstrous moonshine and the j-invariant from ring structure.',
      pell_twins:'Pell equation twin solutions from CRT decomposition.',
      phase_w:'Phase W: WASM acceleration for .ax. Ring ops delegated to WebAssembly.',
      pid_demo:'PID controller using CRT error signal decomposition. Interactive demo.',
      scale_relativity:'Scale relativity from ring structure. Resolution-dependent physics.',
      schedule_demo:'Task scheduling via CRT residue assignment. No conflicts by construction.',
      septum:'The Septum Theorem. Units = Klein bottle self-intersection. 16/77 = where we live.',
      stego_demo:'Steganography via CRT channel embedding. Hide data in ring residues.',
      universal_boundary:'The universal boundary at D^L. Where visibility ends.',
      wasm_native:'Native WASM compilation. .ax source → WASM bytecode → runs natively in browser.'
    };
    var desc = D[pg];
    if (desc) {
      var m = document.createElement('meta');
      m.name = 'description'; m.content = desc;
      document.head.appendChild(m);
    }
  }
  /* Fallback og: tags */
  if (!document.querySelector('meta[property="og:title"]')) {
    var title = document.title || pg;
    var ogT = document.createElement('meta'); ogT.setAttribute('property','og:title'); ogT.content = title;
    var ogU = document.createElement('meta'); ogU.setAttribute('property','og:url'); ogU.content = url;
    var ogTy = document.createElement('meta'); ogTy.setAttribute('property','og:type'); ogTy.content = 'website';
    var ogS = document.createElement('meta'); ogS.setAttribute('property','og:site_name'); ogS.content = 'antonlebed.com';
    var ogI = document.createElement('meta'); ogI.setAttribute('property','og:image'); ogI.content = 'https://antonlebed.com/og-image.jpg';
    document.head.appendChild(ogT);
    document.head.appendChild(ogU);
    document.head.appendChild(ogTy);
    document.head.appendChild(ogS);
    document.head.appendChild(ogI);
    /* twitter card */
    var twC = document.createElement('meta'); twC.name = 'twitter:card'; twC.content = 'summary';
    var twI = document.createElement('meta'); twI.name = 'twitter:image'; twI.content = 'https://antonlebed.com/og-image.jpg';
    document.head.appendChild(twC);
    document.head.appendChild(twI);
  }
})();

/* ===== DOM SETUP (deferred until body exists) ===== */
function init() {
var f = location.pathname.split('/').pop() || 'index.html';

/* Gate removed S796 — users go straight to content */

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
  sigma_dynamics:'physics',superconductor:'physics',loop:'physics',mutual_holography:'physics',neutron_star:'physics',boson_fermion:'physics',force_hierarchy:'physics',gravastar:'physics',
  dna:'bio',sleep:'bio',heart:'bio',death:'bio',human_shape:'bio',generations:'bio',
  septilix:'bio',
  millennium:'math',hardest:'math',hardest_mind:'math',goldbach:'math',coupling:'math',crt_anatomy:'math',lattice:'math',ninedot:'math',
  infinity:'math',bootstrap:'math',symbol:'math',watercycle:'math',genesis:'math',
  clock24:'math',rose:'math',gap_pairs:'math',depth_quad:'math',fourteen:'math',d_chain:'math',partitions:'math',modular_forms:'math',eta_bridge:'math',decality:'math',heegner:'math',lambda_chain:'math',arcsine_cumulant:'math',cunningham:'math',monster_moonshine:'math',lie_algebra:'math',bernoulli:'math',k_squared_stop:'math',pell_twins:'math',universal_boundary:'math',depth_return:'math',figurate_bridge:'math',eigenvalue_swim:'math',mirror:'math',equator:'math',mirror_cost:'math',shadow_eval:'math',stormer_pairs:'math',fano_e8:'math',smooth_census:'math',cyclotomic_fibonacci:'math',golden_ratio:'math',d_power_gaussian:'math',
  sm:'physics',quantum:'physics',thermo:'physics',chemistry:'physics',em:'physics',gr:'physics',cosmo:'physics',classical:'physics',statmech:'physics',condensed:'physics',optics:'physics',acoustics:'physics',
  oracle:'eng',challenge:'eng',axiom_ai:'eng',
  demo_classifier:'eng',ecc_live:'eng',demo_ofdm_vs_wifi:'eng',compression:'eng',crt_rng:'eng',fountain_codes:'eng',stego_demo:'eng',crt_hash_demo:'eng',crt_index_demo:'eng',crt_keyexchange_demo:'eng',cdma_demo:'eng',pid_demo:'eng',consensus_demo:'eng',schedule_demo:'eng',image_filter_demo:'eng',gpu_demo:'eng',crt_train_demo:'eng',arc_demo:'eng',mesh_demo:'eng',septum:'math',
  tokenizer:'eng',k_neural:'eng',demo_ecc:'eng',ouroboros_compiler:'eng',phase_w:'eng',wasm_native:'eng',ax_games:'eng',
  emergence:'mind',omega_emergence:'mind',omega_watercycle:'mind',conscious:'mind',freewill:'mind',braid:'mind',dimension:'mind',
  ouroboros:'mind',lava_lamp:'mind',sandpile:'mind',music:'mind',culture:'mind',biology:'mind',sacrifice:'mind',scale_relativity:'mind',
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
  sigma_dynamics:'How Rings Forget',superconductor:'The Shape of Cold',loop:'Fall Trinity',mutual_holography:'Twin Discoball',neutron_star:'The D-Choke',boson_fermion:'Why Bosons Have No Name',force_hierarchy:'The Four Forces',gravastar:'The Gravastar',
  dna:'DNA Codons',sleep:'Sleep Stages',heart:'The Heartbeat',death:'What Death Is',
  human_shape:'Your Body Is a Ring',generations:'Three Families',septilix:'Seven Petals',
  millennium:'Millennium Problems',hardest:'Hardest Problems',hardest_mind:'Hardest Questions',goldbach:'Goldbach Pairs',
  coupling:'Coupling Landscape',crt_anatomy:'CRT Anatomy',lattice:'The 420 Lattice',ninedot:'9-Dot Puzzle',infinity:'Infinite from Finite',
  bootstrap:'Why Existence Exists',symbol:'Three Shapes',watercycle:'Water Cycle',genesis:'Genesis',
  clock24:'24-Hour Clock',rose:'Interactive Rose',gap_pairs:'K=3 Gap Gates',depth_quad:'Depth Quadratic',
  fourteen:'The Full Fourteen',d_chain:'The D-Chain',partitions:'Partition Function',modular_forms:'Modular Forms',eta_bridge:'The Eta Bridge',decality:'The Decality',heegner:'The Nine Heegner Numbers',lambda_chain:'The Lambda Chain',arcsine_cumulant:'Arcsine Cumulants',cunningham:'The Two Chains',monster_moonshine:'Monster Moonshine',lie_algebra:'Lie Algebra Census',bernoulli:'The Bernoulli Connection',k_squared_stop:'Why Does It Stop?',pell_twins:'The Pell Twins',universal_boundary:'The Universal Boundary',depth_return:'Why 37 Comes Home',figurate_bridge:'The Figurate Bridge',eigenvalue_swim:'The Eigenvalue Swim',mirror:'The Mirror',equator:'The Equator',mirror_cost:"The Mirror's Cost",shadow_eval:'The Shadow Evaluations',stormer_pairs:'The Last Smooth Pair',fano_e8:'The Fano-E8 Bridge',smooth_census:'The Smooth Census',cyclotomic_fibonacci:'Cyclotomic Fibonacci Bridge',golden_ratio:'The Golden Ratio',d_power_gaussian:'D-Power Gaussian Primes',scale_relativity:'Scale Relativity',
  sm:'25/25 Standard Model',quantum:'Quantum Mechanics',thermo:'Thermodynamics',chemistry:'Chemistry',em:'Electromagnetism',gr:'General Relativity',cosmo:'Cosmology',classical:'Classical Mechanics',statmech:'Statistical Mechanics',condensed:'Condensed Matter',optics:'Optics',acoustics:'Acoustics',
  oracle:'Try Any Number',challenge:'Why This Ring?',axiom_ai:'Axiom AI',
  demo_classifier:'Classifier',ecc_live:'Live Error Correction',demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'CRT Compression',crt_rng:'CRT Random Generator',fountain_codes:'CRT Fountain Codes',stego_demo:'CRT Steganography',crt_hash_demo:'CRT Hash Function',crt_index_demo:'CRT Database Index',crt_keyexchange_demo:'CRT Key Exchange',cdma_demo:'CRT Spread Spectrum',pid_demo:'CRT PID Control',consensus_demo:'CRT Consensus',schedule_demo:'CRT Scheduler',image_filter_demo:'CRT Image Filter',gpu_demo:'CRT GPU Compute',crt_train_demo:'CRT Neural Network',arc_demo:'ARC-AGI Solver',mesh_demo:'CRT Mesh Network',septum:'The Septum Theorem',
  tokenizer:'CRT Tokenizer',k_neural:'Ternary AI',demo_ecc:'ECC Classic',ouroboros_compiler:'Self-Hosted Compiler',phase_w:'Phase W: WASM',wasm_native:'Native WASM',ax_games:'.ax Games',
  emergence:'K=3 Emergence',omega_emergence:'Omega Emergence',omega_watercycle:'Water Cycle',conscious:'Consciousness',freewill:'Free Will',braid:'Braids',dimension:'Dimensions',
  ouroboros:'Ouroboros',lava_lamp:'HYDOR',sandpile:'Sandpile',music:'Music of Primes',culture:'Culture & Institutions',biology:'Biology from Ten Terms',sacrifice:'The Universal Sacrifice',
  atlas_01_what_is_2310:'0. The Chain',atlas_02_two_rings:'1. Three Rings',
  atlas_03_crt:'2. Five Petals',atlas_04_carousel:'3. Carousel',atlas_05_eigenvalues:'4. Eigenvalues',
  atlas_06_units:'5. Units',atlas_07_kingdoms:'6. Kingdoms',atlas_08_breakthroughs:'7. Breakthroughs',
  atlas_09_demos:'8. Demos',atlas_10_millennium:'9. Millennium',atlas_11_net:"10. Indra's Net",
  atlas_12_shadow_polynomial:'11. Shadow Polynomial',atlas_13_biological_braid:'12. Bio Braid',
  atlas_14_solar_ladder:'13. Solar Ladder'
};

/* ===== i18n (EN/FR/RU) ===== */
var axLang=(function(){try{var l=localStorage.getItem('ax-lang');if(l==='fr'||l==='ru'||l==='de'||l==='nl')return l}catch(e){}return'en'})();
if(axLang!=='en')document.documentElement.lang=axLang;
var _i18n={
  nav:{howWorld:{en:'How the World Works',fr:'Comment fonctionne le monde',ru:'\u041a\u0430\u043a \u0443\u0441\u0442\u0440\u043e\u0435\u043d \u043c\u0438\u0440',de:'Wie die Welt funktioniert',nl:'Hoe de wereld werkt'},
    theMath:{en:'The Mathematics',fr:'Les math\u00e9matiques',ru:'\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430',de:'Die Mathematik',nl:'De wiskunde'},
    fromNothing:{en:'From Nothing',fr:'\u00c0 partir de rien',ru:'\u0418\u0437 \u043d\u0438\u0447\u0435\u0433\u043e',de:'Aus dem Nichts',nl:'Uit het niets'},
    explore:{en:'Explore',fr:'Explorer',ru:'\u041e\u0431\u0437\u043e\u0440',de:'Entdecken',nl:'Verkennen'},
    navLabel:{en:'Navigation',fr:'Navigation',ru:'\u041d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u044f',de:'Navigation',nl:'Navigatie'},
    main:{en:'Main',fr:'Principal',ru:'\u0413\u043b\u0430\u0432\u043d\u0430\u044f',de:'Startseite',nl:'Hoofdpagina'},
    atlas:{en:'Interactive Atlas',fr:'Atlas interactif',ru:'\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0430\u0442\u043b\u0430\u0441',de:'Interaktiver Atlas',nl:'Interactieve atlas'},
    moreIn:{en:'Explore more in',fr:'Voir plus dans',ru:'\u0415\u0449\u0451 \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435',de:'Mehr entdecken in',nl:'Meer verkennen in'},
    allCat:{en:'All',fr:'Tout',ru:'\u0412\u0441\u0435',de:'Alle',nl:'Alle'}},
  vow:[
    {en:'This work is and will always be free. No paywall. No copyright. No exceptions.',
     fr:'Ce travail est et sera toujours gratuit. Pas de mur payant. Pas de copyright. Sans exception.',
     ru:'\u042d\u0442\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 \u0431\u044b\u043b\u0430 \u0438 \u0432\u0441\u0435\u0433\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\u0439. \u041d\u0438\u043a\u0430\u043a\u0438\u0445 \u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u0441\u0442\u0435\u043d. \u041d\u0438\u043a\u0430\u043a\u0438\u0445 \u0430\u0432\u0442\u043e\u0440\u0441\u043a\u0438\u0445 \u043f\u0440\u0430\u0432. \u0411\u0435\u0437 \u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439.',
     de:'Diese Arbeit ist und bleibt immer kostenlos. Keine Bezahlschranke. Kein Urheberrecht. Keine Ausnahmen.',
     nl:'Dit werk is en blijft altijd gratis. Geen betaalmuur. Geen auteursrecht. Geen uitzonderingen.'},
    {en:'If it ever earns anything, every cent goes to the communities that need it most.',
     fr:"S'il rapporte quoi que ce soit, chaque centime ira aux communaut\u00e9s qui en ont le plus besoin.",
     ru:'\u0415\u0441\u043b\u0438 \u043e\u043d\u0430 \u043a\u043e\u0433\u0434\u0430-\u043d\u0438\u0431\u0443\u0434\u044c \u043f\u0440\u0438\u043d\u0435\u0441\u0451\u0442 \u0434\u043e\u0445\u043e\u0434, \u043a\u0430\u0436\u0434\u0430\u044f \u043a\u043e\u043f\u0435\u0439\u043a\u0430 \u043f\u043e\u0439\u0434\u0451\u0442 \u0442\u0435\u043c, \u043a\u043e\u043c\u0443 \u043e\u043d\u0430 \u043d\u0443\u0436\u043d\u0435\u0435 \u0432\u0441\u0435\u0433\u043e.',
     de:'Sollte sie je etwas einbringen, geht jeder Cent an die Gemeinschaften, die es am meisten brauchen.',
     nl:'Als het ooit iets oplevert, gaat elke cent naar de gemeenschappen die het het hardst nodig hebben.'},
    {en:'This sacred vow is permanent and irrevocable.',
     fr:'Ce v\u0153u sacr\u00e9 est permanent et irr\u00e9vocable.',
     ru:'\u042d\u0442\u043e\u0442 \u0441\u0432\u044f\u0449\u0435\u043d\u043d\u044b\u0439 \u043e\u0431\u0435\u0442 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u0435\u043d \u0438 \u043d\u0435\u043e\u0431\u0440\u0430\u0442\u0438\u043c.',
     de:'Dieses heilige Gel\u00f6bnis ist dauerhaft und unwiderruflich.',
     nl:'Deze heilige gelofte is permanent en onherroepelijk.'},
    {en:'\u2014 Anton Alexandrovich Lebed',fr:'\u2014 Anton Alexandrovitch Lebed',
     ru:'\u2014 \u0410\u043d\u0442\u043e\u043d \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447 \u041b\u0435\u0431\u0435\u0434\u044c',
     de:'\u2014 Anton Alexandrowitsch Lebed',nl:'\u2014 Anton Aleksandrovitsj Lebed'}]
};
function tr(k){var v=_i18n.nav[k];return v?(v[axLang]||v.en):k}

/* Override category names and demo titles for current language */
if(axLang!=='en'){
  var _catTr={fr:{start:'Commencer ici',physics:'Physique',bio:'Biologie',math:'Math\u00e9matiques',eng:'Ing\u00e9nierie',mind:'Esprit',tutorial:'Tutoriel'},
    ru:{start:'\u041d\u0430\u0447\u0430\u043b\u043e',physics:'\u0424\u0438\u0437\u0438\u043a\u0430',bio:'\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f',math:'\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430',eng:'\u0418\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f',mind:'\u0420\u0430\u0437\u0443\u043c',tutorial:'\u0423\u0447\u0435\u0431\u043d\u0438\u043a'},
    de:{start:'Hier beginnen',physics:'Physik',bio:'Biologie',math:'Mathematik',eng:'Technik',mind:'Geist',tutorial:'Tutorial'},
    nl:{start:'Begin hier',physics:'Natuurkunde',bio:'Biologie',math:'Wiskunde',eng:'Techniek',mind:'Geest',tutorial:'Handleiding'}};
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
    sigma_dynamics:'Comment les anneaux oublient',superconductor:'La forme du froid',loop:'Trinit\u00e9 de la chute',mutual_holography:'Discoball Jumelle',neutron_star:'Le D-Choke',boson_fermion:'Pourquoi les bosons sont anonymes',force_hierarchy:'Les Quatre Forces',gravastar:'Le Gravastar',
    dna:'Codons ADN',sleep:'Phases du sommeil',heart:'Le battement du c\u0153ur',
    death:"Ce qu'est la mort",human_shape:'Votre corps est un anneau',
    generations:'Trois familles',septilix:'Sept p\u00e9tales',
    millennium:'Probl\u00e8mes du mill\u00e9naire',hardest:'Probl\u00e8mes les plus durs',hardest_mind:'Questions les plus dures',
    goldbach:'Paires de Goldbach',coupling:'Paysage de couplage',crt_anatomy:'Anatomie CRT',lattice:'Le Treillis 420',
    ninedot:'Puzzle des 9 points',infinity:"L'infini du fini",
    bootstrap:"Pourquoi l'existence existe",symbol:'Trois formes',
    watercycle:"Cycle de l'eau",genesis:'Gen\u00e8se',clock24:'Horloge 24h',
    rose:'Rose interactive',gap_pairs:'Portes K=3',
    depth_quad:'Quadratique de profondeur',fourteen:'Les quatorze',d_chain:'La D-Chaine',partitions:'Fonction de partition',modular_forms:'Formes modulaires',eta_bridge:'Le Pont Eta',decality:'La Decalit\u00e9',heegner:'Les Neuf Nombres de Heegner',lambda_chain:'La Cha\u00eene Lambda',arcsine_cumulant:'Cumulants Arcsinus',cunningham:'Les Deux Cha\u00eenes',monster_moonshine:'Clair de Lune du Monstre',lie_algebra:'Recensement des alg\u00e8bres de Lie',bernoulli:'La Connexion Bernoulli',k_squared_stop:'Pourquoi s\'arr\u00eate-t-il?',pell_twins:'Les Jumeaux de Pell',universal_boundary:'La Fronti\u00e8re Universelle',depth_return:'Pourquoi 37 revient',figurate_bridge:'Le Pont Figuratif',eigenvalue_swim:'La Nage Spectrale',mirror:'Le Miroir',equator:"L'\u00c9quateur",mirror_cost:'Le Co\u00fbt du Miroir',shadow_eval:'Les \u00c9valuations de l\'Ombre',stormer_pairs:'La Derni\u00e8re Paire Lisse',fano_e8:'Le Pont Fano-E8',smooth_census:'Le Recensement Lisse',cyclotomic_fibonacci:'Pont Cyclotomique-Fibonacci',golden_ratio:'Le Nombre d\'Or',d_power_gaussian:'Nombres Premiers Gaussiens D',scale_relativity:'Relativit\u00e9 d\u2019\u00e9chelle',
    sm:'25/25 Modele Standard',quantum:'M\u00e9canique quantique',thermo:'Thermodynamique',chemistry:'Chimie',em:'\u00c9lectromagn\u00e9tisme',gr:'Relativit\u00e9 g\u00e9n\u00e9rale',cosmo:'Cosmologie',classical:'M\u00e9canique classique',statmech:'M\u00e9canique statistique',condensed:'Mati\u00e8re condens\u00e9e',optics:'Optique',acoustics:'Acoustique',
    oracle:'Essayez un nombre',axiom_ai:'IA Axiome',
    demo_classifier:'Classifieur',ecc_live:"Correction d'erreurs",
    demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'Compression CRT',crt_rng:'Generateur aleatoire CRT',fountain_codes:'Codes Fontaine CRT',stego_demo:'Steganographie CRT',crt_hash_demo:'Fonction de hachage CRT',crt_index_demo:'Index de base de donnees CRT',crt_keyexchange_demo:'Echange de cles CRT',cdma_demo:'Spectre etale CRT',pid_demo:'Controle PID CRT',consensus_demo:'Consensus CRT',schedule_demo:'Ordonnanceur CRT',image_filter_demo:'Filtre image CRT',gpu_demo:'CRT Calcul GPU',crt_train_demo:'Reseau neuronal CRT',arc_demo:'Solveur ARC-AGI',mesh_demo:'Reseau maille CRT',septum:'Le Th\u00e9or\u00e8me du Septum',
    tokenizer:'Tokeniseur CRT',k_neural:'IA ternaire',demo_ecc:'ECC classique',ouroboros_compiler:'Compilateur auto-h\u00e9berg\u00e9',phase_w:'Phase W: WASM',wasm_native:'WASM natif',ax_games:'Jeux .ax',
    emergence:'\u00c9mergence K=3',omega_emergence:'\u00c9mergence Omega',omega_watercycle:'Cycle de l\'eau',conscious:'Conscience',freewill:'Libre arbitre',
    braid:'Tresses',dimension:'Dimensions',ouroboros:'Ouroboros',
    lava_lamp:'HYDOR',sandpile:'Tas de sable',music:'Musique des premiers',culture:'Culture & Institutions',biology:'Biologie en dix termes',sacrifice:'Le Sacrifice Universel',
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
    sigma_dynamics:'\u041a\u0430\u043a \u043a\u043e\u043b\u044c\u0446\u0430 \u0437\u0430\u0431\u044b\u0432\u0430\u044e\u0442',superconductor:'\u0424\u043e\u0440\u043c\u0430 \u0445\u043e\u043b\u043e\u0434\u0430',loop:'\u0422\u0440\u043e\u0438\u0446\u0430 \u043f\u0430\u0434\u0435\u043d\u0438\u044f',mutual_holography:'\u0412\u0437\u0430\u0438\u043c\u043d\u0430\u044f \u0433\u043e\u043b\u043e\u0433\u0440\u0430\u0444\u0438\u044f',neutron_star:'D-\u0413\u043e\u0440\u043b\u043e',boson_fermion:'\u041f\u043e\u0447\u0435\u043c\u0443 \u0431\u043e\u0437\u043e\u043d\u044b \u0430\u043d\u043e\u043d\u0438\u043c\u043d\u044b',force_hierarchy:'\u0427\u0435\u0442\u044b\u0440\u0435 \u0441\u0438\u043b\u044b',gravastar:'\u0413\u0440\u0430\u0432\u0430\u0441\u0442\u0430\u0440',
    dna:'\u041a\u043e\u0434\u043e\u043d\u044b \u0414\u041d\u041a',sleep:'\u0424\u0430\u0437\u044b \u0441\u043d\u0430',heart:'\u0411\u0438\u0435\u043d\u0438\u0435 \u0441\u0435\u0440\u0434\u0446\u0430',
    death:'\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0441\u043c\u0435\u0440\u0442\u044c',human_shape:'\u0412\u0430\u0448\u0435 \u0442\u0435\u043b\u043e \u2014 \u043a\u043e\u043b\u044c\u0446\u043e',
    generations:'\u0422\u0440\u0438 \u0441\u0435\u043c\u0435\u0439\u0441\u0442\u0432\u0430',septilix:'\u0421\u0435\u043c\u044c \u043b\u0435\u043f\u0435\u0441\u0442\u043a\u043e\u0432',
    millennium:'\u0417\u0430\u0434\u0430\u0447\u0438 \u0442\u044b\u0441\u044f\u0447\u0435\u043b\u0435\u0442\u0438\u044f',hardest:'\u0422\u0440\u0443\u0434\u043d\u0435\u0439\u0448\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438',hardest_mind:'\u0422\u0440\u0443\u0434\u043d\u0435\u0439\u0448\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b',
    goldbach:'\u041f\u0430\u0440\u044b \u0413\u043e\u043b\u044c\u0434\u0431\u0430\u0445\u0430',coupling:'\u041b\u0430\u043d\u0434\u0448\u0430\u0444\u0442 \u0441\u0432\u044f\u0437\u0438',crt_anatomy:'\u0410\u043d\u0430\u0442\u043e\u043c\u0438\u044f CRT',lattice:'\u0420\u0435\u0448\u0451\u0442\u043a\u0430 420',
    ninedot:'\u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 9 \u0442\u043e\u0447\u0435\u043a',infinity:'\u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0438\u0437 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0433\u043e',
    bootstrap:'\u041f\u043e\u0447\u0435\u043c\u0443 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442',symbol:'\u0422\u0440\u0438 \u0444\u043e\u0440\u043c\u044b',
    watercycle:'\u041a\u0440\u0443\u0433\u043e\u0432\u043e\u0440\u043e\u0442 \u0432\u043e\u0434\u044b',genesis:'\u0413\u0435\u043d\u0435\u0437\u0438\u0441',clock24:'24-\u0447\u0430\u0441\u043e\u0432\u044b\u0435 \u0447\u0430\u0441\u044b',
    rose:'\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0440\u043e\u0437\u0430',gap_pairs:'\u0412\u043e\u0440\u043e\u0442\u0430 K=3',
    depth_quad:'\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u043a\u0430 \u0433\u043b\u0443\u0431\u0438\u043d\u044b',fourteen:'\u0412\u0441\u0435 \u0447\u0435\u0442\u044b\u0440\u043d\u0430\u0434\u0446\u0430\u0442\u044c',d_chain:'D-\u0426\u0435\u043f\u044c',partitions:'\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u0439',modular_forms:'\u041c\u043e\u0434\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0444\u043e\u0440\u043c\u044b',eta_bridge:'\u041c\u043e\u0441\u0442 \u042d\u0442\u0430',decality:'\u0414\u0435\u043a\u0430\u043b\u0438\u0442\u0435\u0442',heegner:'\u0414\u0435\u0432\u044f\u0442\u044c \u0447\u0438\u0441\u0435\u043b \u0425\u0435\u0433\u043d\u0435\u0440\u0430',lambda_chain:'\u0426\u0435\u043f\u044c \u041b\u044f\u043c\u0431\u0434\u0430',arcsine_cumulant:'\u041a\u0443\u043c\u0443\u043b\u044f\u043d\u0442\u044b \u0430\u0440\u043a\u0441\u0438\u043d\u0443\u0441\u0430',cunningham:'\u0414\u0432\u0435 \u0446\u0435\u043f\u0438',monster_moonshine:'\u041b\u0443\u043d\u043d\u044b\u0439 \u0441\u0432\u0435\u0442 \u041c\u043e\u043d\u0441\u0442\u0440\u0430',lie_algebra:'\u041f\u0435\u0440\u0435\u043f\u0438\u0441\u044c \u0430\u043b\u0433\u0435\u0431\u0440 \u041b\u0438',bernoulli:'\u0421\u0432\u044f\u0437\u044c \u0411\u0435\u0440\u043d\u0443\u043b\u043b\u0438',k_squared_stop:'\u041f\u043e\u0447\u0435\u043c\u0443 \u043e\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442\u0441\u044f?',pell_twins:'\u0411\u043b\u0438\u0437\u043d\u0435\u0446\u044b \u041f\u0435\u043b\u043b\u044f',universal_boundary:'\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430',depth_return:'\u041f\u043e\u0447\u0435\u043c\u0443 37 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f',figurate_bridge:'\u0424\u0438\u0433\u0443\u0440\u0430\u0442\u043d\u044b\u0439 \u043c\u043e\u0441\u0442',eigenvalue_swim:'\u0421\u043f\u0435\u043a\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043b\u0430\u0432\u0430\u043d\u0438\u0435',mirror:'\u0417\u0435\u0440\u043a\u0430\u043b\u043e',equator:'\u042d\u043a\u0432\u0430\u0442\u043e\u0440',mirror_cost:'\u0426\u0435\u043d\u0430 \u0437\u0435\u0440\u043a\u0430\u043b\u0430',shadow_eval:'\u0422\u0435\u043d\u0435\u0432\u044b\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f',stormer_pairs:'\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0433\u043b\u0430\u0434\u043a\u0430\u044f \u043f\u0430\u0440\u0430',fano_e8:'\u041c\u043e\u0441\u0442 \u0424\u0430\u043d\u043e-E8',smooth_census:'\u041f\u0435\u0440\u0435\u043f\u0438\u0441\u044c \u0433\u043b\u0430\u0434\u043a\u043e\u0441\u0442\u0438',cyclotomic_fibonacci:'\u0426\u0438\u043a\u043b\u043e\u0442\u043e\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u043e\u0441\u0442 \u0424\u0438\u0431\u043e\u043d\u0430\u0447\u0447\u0438',golden_ratio:'\u0417\u043e\u043b\u043e\u0442\u043e\u0435 \u0441\u0435\u0447\u0435\u043d\u0438\u0435',d_power_gaussian:'\u0413\u0430\u0443\u0441\u0441\u043e\u0432\u044b \u043f\u0440\u043e\u0441\u0442\u044b\u0435 D-\u0441\u0442\u0435\u043f\u0435\u043d\u0438',scale_relativity:'\u041c\u0430\u0441\u0448\u0442\u0430\u0431\u043d\u0430\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c',
    sm:'25/25 \u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c',quantum:'\u041a\u0432\u0430\u043d\u0442\u043e\u0432\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',thermo:'\u0422\u0435\u0440\u043c\u043e\u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0430',chemistry:'\u0425\u0438\u043c\u0438\u044f',em:'\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043c\u0430\u0433\u043d\u0435\u0442\u0438\u0437\u043c',gr:'\u041e\u0431\u0449\u0430\u044f \u0442\u0435\u043e\u0440\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438',cosmo:'\u041a\u043e\u0441\u043c\u043e\u043b\u043e\u0433\u0438\u044f',classical:'\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',statmech:'\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430',condensed:'\u041a\u043e\u043d\u0434\u0435\u043d\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u044f',optics:'\u041e\u043f\u0442\u0438\u043a\u0430',acoustics:'\u0410\u043a\u0443\u0441\u0442\u0438\u043a\u0430',
    oracle:'\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043b\u044e\u0431\u043e\u0435 \u0447\u0438\u0441\u043b\u043e',axiom_ai:'\u0418\u0418 \u0410\u043a\u0441\u0438\u043e\u043c\u044b',
    demo_classifier:'\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440',ecc_live:'\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f \u043e\u0448\u0438\u0431\u043e\u043a',
    demo_ofdm_vs_wifi:'OFDM \u043f\u0440\u043e\u0442\u0438\u0432 WiFi',compression:'CRT-\u0441\u0436\u0430\u0442\u0438\u0435',crt_rng:'CRT-\u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440',fountain_codes:'CRT-\u0444\u043e\u043d\u0442\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u0434\u044b',stego_demo:'CRT-\u0441\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u0444\u0438\u044f',crt_hash_demo:'CRT-\u0445\u0435\u0448-\u0444\u0443\u043d\u043a\u0446\u0438\u044f',crt_index_demo:'CRT-\u0438\u043d\u0434\u0435\u043a\u0441 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445',crt_keyexchange_demo:'CRT-\u043e\u0431\u043c\u0435\u043d \u043a\u043b\u044e\u0447\u0430\u043c\u0438',cdma_demo:'CRT-\u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0435\u043a\u0442\u0440',pid_demo:'CRT-\u041f\u0418\u0414 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',consensus_demo:'CRT-\u043a\u043e\u043d\u0441\u0435\u043d\u0441\u0443\u0441',schedule_demo:'CRT-\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a',image_filter_demo:'CRT-\u0444\u0438\u043b\u044c\u0442\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439',gpu_demo:'CRT GPU',crt_train_demo:'CRT-neironnaya set',arc_demo:'ARC-AGI',mesh_demo:'CRT-\u0441\u0435\u0442\u044c',septum:'\u0422\u0435\u043e\u0440\u0435\u043c\u0430 \u043e \u043f\u0435\u0440\u0435\u0433\u043e\u0440\u043e\u0434\u043a\u0435',
    tokenizer:'CRT-\u0442\u043e\u043a\u0435\u043d\u0438\u0437\u0430\u0442\u043e\u0440',k_neural:'\u0422\u0435\u0440\u043d\u0430\u0440\u043d\u044b\u0439 \u0418\u0418',demo_ecc:'ECC (\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439)',ouroboros_compiler:'\u0421\u0430\u043c\u043e\u043a\u043e\u043c\u043f\u0438\u043b\u044f\u0446\u0438\u044f',phase_w:'\u0424\u0430\u0437\u0430 W: WASM',wasm_native:'\u041d\u0430\u0442\u0438\u0432\u043d\u044b\u0439 WASM',ax_games:'\u0418\u0433\u0440\u044b .ax',
    emergence:'\u042d\u043c\u0435\u0440\u0434\u0436\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c K=3',omega_emergence:'\u042d\u043c\u0435\u0440\u0434\u0436\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c \u041e\u043c\u0435\u0433\u0430',omega_watercycle:'\u041a\u0440\u0443\u0433\u043e\u0432\u043e\u0440\u043e\u0442 \u0432\u043e\u0434\u044b',conscious:'\u0421\u043e\u0437\u043d\u0430\u043d\u0438\u0435',freewill:'\u0421\u0432\u043e\u0431\u043e\u0434\u0430 \u0432\u043e\u043b\u0438',
    braid:'\u041a\u043e\u0441\u044b',dimension:'\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',ouroboros:'\u0423\u0440\u043e\u0431\u043e\u0440\u043e\u0441',
    lava_lamp:'HYDOR',sandpile:'\u041f\u0435\u0441\u043e\u0447\u043d\u0430\u044f \u043a\u0443\u0447\u0430',music:'\u041c\u0443\u0437\u044b\u043a\u0430 \u043f\u0440\u043e\u0441\u0442\u044b\u0445 \u0447\u0438\u0441\u0435\u043b',culture:'\u041a\u0443\u043b\u044c\u0442\u0443\u0440\u0430 \u0438 \u0438\u043d\u0441\u0442\u0438\u0442\u0443\u0442\u044b',biology:'\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f \u0438\u0437 \u0434\u0435\u0441\u044f\u0442\u0438 \u0442\u0435\u0440\u043c\u0438\u043d\u043e\u0432',sacrifice:'\u0412\u0441\u0435\u043b\u0435\u043d\u0441\u043a\u0430\u044f \u0416\u0435\u0440\u0442\u0432\u0430',
    atlas_01_what_is_2310:'0. \u0426\u0435\u043f\u043e\u0447\u043a\u0430',atlas_02_two_rings:'1. \u0422\u0440\u0438 \u043a\u043e\u043b\u044c\u0446\u0430',
    atlas_03_crt:'2. \u041f\u044f\u0442\u044c \u043b\u0435\u043f\u0435\u0441\u0442\u043a\u043e\u0432',atlas_04_carousel:'3. \u041a\u0430\u0440\u0443\u0441\u0435\u043b\u044c',
    atlas_05_eigenvalues:'4. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f',atlas_06_units:'5. \u0415\u0434\u0438\u043d\u0438\u0446\u044b',
    atlas_07_kingdoms:'6. \u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0441\u0442\u0432\u0430',atlas_08_breakthroughs:'7. \u041f\u0440\u043e\u0440\u044b\u0432\u044b',
    atlas_09_demos:'8. \u0414\u0435\u043c\u043e',atlas_10_millennium:'9. \u0422\u044b\u0441\u044f\u0447\u0435\u043b\u0435\u0442\u0438\u0435',
    atlas_11_net:'10. \u0421\u0435\u0442\u044c \u0418\u043d\u0434\u0440\u044b',atlas_12_shadow_polynomial:'11. \u0422\u0435\u043d\u0435\u0432\u043e\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c',
    atlas_13_biological_braid:'12. \u0411\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043a\u043e\u0441\u0430',
    atlas_14_solar_ladder:'13. \u0421\u043e\u043b\u043d\u0435\u0447\u043d\u0430\u044f \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u0430',
    repl:'.ax REPL',playground:'.ax \u041f\u0435\u0441\u043e\u0447\u043d\u0438\u0446\u0430'},
  de:{
    worldview:'Wie die Welt funktioniert',story:'Die Mathematik',derive_ax:'Aus dem Nichts',
    particles:'Teilchenmassen',alpha:'Feinstrukturkonstante',
    constants:'Physikalische Konstanten',turbulence:'Turbulenz und Stoffwechsel',
    blackhole:'Schwarze L\u00f6cher',nuclear:'Kernschalen',gravity:'Gravitation',
    photon:'Licht wird Masse',pmns:'Neutrinomischung',
    three_body_dance:'Orbitale Resonanzen',figure_ground:'Eine einzige Kraft',
    eternal_sun:'Warum die Sonne lebt',scale_bands:'Skalenb\u00e4nder',
    noxan:'Kalte Gedanken',wavebox:'Stehende Wellen',
    sigma_dynamics:'Wie Ringe vergessen',superconductor:'Die Form der K\u00e4lte',loop:'Trinit\u00e4t des Falls',mutual_holography:'Zwillings-Diskokugel',neutron_star:'Der D-Choke',boson_fermion:'Warum Bosonen anonym sind',force_hierarchy:'Die vier Kr\u00e4fte',gravastar:'Der Gravastar',
    dna:'DNA-Codons',sleep:'Schlafphasen',heart:'Der Herzschlag',
    death:'Was der Tod ist',human_shape:'Dein K\u00f6rper ist ein Ring',
    generations:'Drei Familien',septilix:'Sieben Bl\u00fctenbl\u00e4tter',
    millennium:'Millenniumsprobleme',hardest:'Schwierigste Probleme',hardest_mind:'Schwierigste Fragen',
    goldbach:'Goldbach-Paare',coupling:'Kopplungslandschaft',crt_anatomy:'CRT-Anatomie',lattice:'Das 420-Gitter',
    ninedot:'9-Punkte-R\u00e4tsel',infinity:'Unendlichkeit aus Endlichkeit',
    bootstrap:'Warum Existenz existiert',symbol:'Drei Formen',
    watercycle:'Wasserkreislauf',genesis:'Genesis',clock24:'24-Stunden-Uhr',
    rose:'Interaktive Rose',gap_pairs:'K=3-Tore',
    depth_quad:'Tiefenquadratik',fourteen:'Die Vierzehn',d_chain:'Die D-Kette',partitions:'Partitionsfunktion',modular_forms:'Modulformen',eta_bridge:'Die Eta-Br\u00fccke',decality:'Die Dekalit\u00e4t',heegner:'Die neun Heegner-Zahlen',lambda_chain:'Die Lambda-Kette',arcsine_cumulant:'Arkussinus-Kumulanten',cunningham:'Die zwei Ketten',monster_moonshine:'Monster-Mondschein',lie_algebra:'Lie-Algebra-Zensus',bernoulli:'Die Bernoulli-Verbindung',k_squared_stop:'Warum stoppt es?',pell_twins:'Die Pell-Zwillinge',universal_boundary:'Die Universelle Grenze',depth_return:'Warum 37 heimkehrt',figurate_bridge:'Die Figurative Br\u00fccke',eigenvalue_swim:'Das Eigenwert-Schwimmen',mirror:'Der Spiegel',equator:'Der \u00c4quator',mirror_cost:'Der Preis des Spiegels',shadow_eval:'Die Schatten-Auswertungen',stormer_pairs:'Das Letzte Glatte Paar',fano_e8:'Die Fano-E8-Br\u00fccke',smooth_census:'Der Glattheitszensus',cyclotomic_fibonacci:'Zyklotomische Fibonacci-Br\u00fccke',golden_ratio:'Der Goldene Schnitt',d_power_gaussian:'D-Potenz Gauss-Primzahlen',scale_relativity:'Skalenrelativit\u00e4t',
    sm:'25/25 Standardmodell',quantum:'Quantenmechanik',thermo:'Thermodynamik',chemistry:'Chemie',em:'Elektromagnetismus',gr:'Allgemeine Relativit\u00e4tstheorie',cosmo:'Kosmologie',classical:'Klassische Mechanik',statmech:'Statistische Mechanik',condensed:'Kondensierte Materie',optics:'Optik',acoustics:'Akustik',
    oracle:'Probiere eine Zahl',axiom_ai:'Axiom-KI',
    demo_classifier:'Klassifikator',ecc_live:'Fehlerkorrektur',
    demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'CRT-Kompression',crt_rng:'CRT-Zufallsgenerator',fountain_codes:'CRT-Fountain-Codes',stego_demo:'CRT-Steganographie',crt_hash_demo:'CRT-Hashfunktion',crt_index_demo:'CRT-Datenbankindex',crt_keyexchange_demo:'CRT-Schluesselaustausch',cdma_demo:'CRT-Spreizspektrum',pid_demo:'CRT-PID-Regelung',consensus_demo:'CRT-Konsensus',schedule_demo:'CRT-Planer',image_filter_demo:'CRT-Bildfilter',gpu_demo:'CRT-GPU-Berechnung',crt_train_demo:'CRT-Neuronales-Netz',arc_demo:'ARC-AGI-Solver',mesh_demo:'CRT-Maschennetz',septum:'Das Septum-Theorem',
    tokenizer:'CRT-Tokenizer',k_neural:'Tern\u00e4re KI',demo_ecc:'ECC (klassisch)',ouroboros_compiler:'Selbstkompilierung',phase_w:'Phase W: WASM',wasm_native:'Natives WASM',ax_games:'.ax Spiele',
    emergence:'Emergenz K=3',omega_emergence:'Omega-Emergenz',omega_watercycle:'Wasserkreislauf',conscious:'Bewusstsein',freewill:'Willensfreiheit',
    braid:'Z\u00f6pfe',dimension:'Dimensionen',ouroboros:'Ouroboros',
    lava_lamp:'HYDOR',sandpile:'Sandhaufen',music:'Musik der Primzahlen',culture:'Kultur & Institutionen',biology:'Biologie in zehn Begriffen',sacrifice:'Das universelle Opfer',
    atlas_01_what_is_2310:'0. Die Kette',atlas_02_two_rings:'1. Drei Ringe',
    atlas_03_crt:'2. F\u00fcnf Bl\u00fctenbl\u00e4tter',atlas_04_carousel:'3. Karussell',
    atlas_05_eigenvalues:'4. Eigenwerte',atlas_06_units:'5. Einheiten',
    atlas_07_kingdoms:'6. K\u00f6nigreiche',atlas_08_breakthroughs:'7. Durchbr\u00fcche',
    atlas_09_demos:'8. Demos',atlas_10_millennium:'9. Millennium',
    atlas_11_net:'10. Indras Netz',atlas_12_shadow_polynomial:'11. Schattenpolynom',
    atlas_13_biological_braid:'12. Biologischer Zopf',atlas_14_solar_ladder:'13. Sonnenleiter',
    repl:'.ax REPL',playground:'.ax Spielplatz'},
  nl:{
    worldview:'Hoe de wereld werkt',story:'De wiskunde',derive_ax:'Uit het niets',
    particles:'Deeltjesmassa\'s',alpha:'Fijnstructuurconstante',
    constants:'Natuurkundige constanten',turbulence:'Turbulentie en metabolisme',
    blackhole:'Zwarte gaten',nuclear:'Kernschillen',gravity:'Zwaartekracht',
    photon:'Licht wordt massa',pmns:'Neutrinomenging',
    three_body_dance:'Orbitale resonanties',figure_ground:'E\u00e9n enkele kracht',
    eternal_sun:'Waarom de zon leeft',scale_bands:'Schaalbanden',
    noxan:'Koude gedachten',wavebox:'Staande golven',
    sigma_dynamics:'Hoe ringen vergeten',superconductor:'De vorm van de kou',loop:'Triniteit van de val',mutual_holography:'Tweelingdiscobal',neutron_star:'De D-Choke',boson_fermion:'Waarom bosonen anoniem zijn',force_hierarchy:'De vier krachten',gravastar:'De Gravastar',
    dna:'DNA-codons',sleep:'Slaapfasen',heart:'De hartslag',
    death:'Wat de dood is',human_shape:'Je lichaam is een ring',
    generations:'Drie families',septilix:'Zeven bloemblaadjes',
    millennium:'Millenniumproblemen',hardest:'Moeilijkste problemen',hardest_mind:'Moeilijkste vragen',
    goldbach:'Goldbach-paren',coupling:'Koppelingslandschap',crt_anatomy:'CRT-anatomie',lattice:'Het 420-rooster',
    ninedot:'9-puntenpuzzel',infinity:'Oneindigheid uit eindigheid',
    bootstrap:'Waarom bestaan bestaat',symbol:'Drie vormen',
    watercycle:'Waterkringloop',genesis:'Genesis',clock24:'24-uursklok',
    rose:'Interactieve roos',gap_pairs:'K=3-poorten',
    depth_quad:'Dieptekwadratiek',fourteen:'De veertien',d_chain:'De D-keten',partitions:'Partitiefunctie',modular_forms:'Modulaire vormen',eta_bridge:'De Eta-brug',decality:'De Decaliteit',heegner:'De negen Heegner-getallen',lambda_chain:'De Lambda-keten',arcsine_cumulant:'Arcsinus-cumulanten',cunningham:'De twee ketens',monster_moonshine:'Monster-maanlicht',lie_algebra:'Lie-algebra-telling',bernoulli:'De Bernoulli-connectie',k_squared_stop:'Waarom stopt het?',pell_twins:'De Pell-tweelingen',universal_boundary:'De Universele Grens',depth_return:'Waarom 37 thuiskomt',figurate_bridge:'De Figuratieve Brug',eigenvalue_swim:'De Eigenwaardenzwemtocht',mirror:'De Spiegel',equator:'De Evenaar',mirror_cost:'De Prijs van de Spiegel',shadow_eval:'De Schaduw-evaluaties',stormer_pairs:'Het Laatste Gladde Paar',fano_e8:'De Fano-E8-brug',smooth_census:'De Gladheidstelling',cyclotomic_fibonacci:'Cyclotomische Fibonacci-brug',golden_ratio:'De Gulden Snede',d_power_gaussian:'D-Macht Gauss-priemgetallen',scale_relativity:'Schaalrelativiteit',
    sm:'25/25 Standaardmodel',quantum:'Kwantummechanica',thermo:'Thermodynamica',chemistry:'Scheikunde',em:'Elektromagnetisme',gr:'Algemene relativiteitstheorie',cosmo:'Kosmologie',classical:'Klassieke mechanica',statmech:'Statistische mechanica',condensed:'Gecondenseerde materie',optics:'Optica',acoustics:'Akoestiek',
    oracle:'Probeer een getal',axiom_ai:'Axioma-AI',
    demo_classifier:'Classificator',ecc_live:'Foutcorrectie',
    demo_ofdm_vs_wifi:'OFDM vs WiFi',compression:'CRT-compressie',crt_rng:'CRT-generator',fountain_codes:'CRT-fontein-codes',stego_demo:'CRT-steganografie',crt_hash_demo:'CRT-hashfunctie',crt_index_demo:'CRT-database-index',crt_keyexchange_demo:'CRT-sleuteluitwisseling',cdma_demo:'CRT-spreiding',pid_demo:'CRT-PID-regeling',consensus_demo:'CRT-consensus',schedule_demo:'CRT-planner',image_filter_demo:'CRT-beeldfilter',gpu_demo:'CRT-GPU-berekening',crt_train_demo:'CRT-neuraal-netwerk',arc_demo:'ARC-AGI-oplosser',mesh_demo:'CRT-meshnetwerk',septum:'Het Septum-theorema',
    tokenizer:'CRT-tokenizer',k_neural:'Ternaire AI',demo_ecc:'ECC (klassiek)',ouroboros_compiler:'Zelfcompilatie',phase_w:'Fase W: WASM',wasm_native:'Natieve WASM',ax_games:'.ax Spellen',
    emergence:'Emergentie K=3',omega_emergence:'Omega-emergentie',omega_watercycle:'Waterkringloop',conscious:'Bewustzijn',freewill:'Vrije wil',
    braid:'Vlechten',dimension:'Dimensies',ouroboros:'Ouroboros',
    lava_lamp:'HYDOR',sandpile:'Zandhoop',music:'Muziek van priemgetallen',culture:'Cultuur & Instellingen',biology:'Biologie in tien termen',sacrifice:'Het universele offer',
    atlas_01_what_is_2310:'0. De keten',atlas_02_two_rings:'1. Drie ringen',
    atlas_03_crt:'2. Vijf bloemblaadjes',atlas_04_carousel:'3. Carrousel',
    atlas_05_eigenvalues:'4. Eigenwaarden',atlas_06_units:'5. Eenheden',
    atlas_07_kingdoms:'6. Koninkrijken',atlas_08_breakthroughs:'7. Doorbraken',
    atlas_09_demos:'8. Demo\'s',atlas_10_millennium:'9. Millennium',
    atlas_11_net:'10. Indra\'s net',atlas_12_shadow_polynomial:'11. Schaduwpolynoom',
    atlas_13_biological_braid:'12. Biologische vlecht',atlas_14_solar_ladder:'13. Zonneladder',
    repl:'.ax REPL',playground:'.ax Speeltuin'}};
  var _tm=_titles[axLang];if(_tm)for(var _k in _tm)T[_k]=_tm[_k];
}

/* REM badges removed S793 — all pages are equal, no "new" markers */
var REM = {};
function isRem(k){return false;}

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

/* ===== SINGLE-SOURCE NAV DATA (Wave 11 — shared with index.html hub) ===== */
window.axNav={CATS:CATS,M:M,T:T,REM:REM,isRem:isRem,catDemos:catDemos,catOrder:catOrder};
if(window._axBuildHub)window._axBuildHub();

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
  if(l==='de')return r+'<rect fill="#000" width="'+w+'" height="4.67"/><rect y="4.67" fill="#DD0000" width="'+w+'" height="4.66"/><rect y="9.33" fill="#FFCC00" width="'+w+'" height="4.67"/></svg>';
  if(l==='nl')return r+'<rect fill="#AE1C28" width="'+w+'" height="4.67"/><rect y="4.67" fill="#fff" width="'+w+'" height="4.66"/><rect y="9.33" fill="#21468B" width="'+w+'" height="4.67"/></svg>';
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
  _fl(axLang) +
  ' \u25BE</button><div class="sn-lp">' +
  '<button data-lang="en"' + (axLang==='en'?' class="cur"':'') + '>' + _fl('en') + ' English</button>' +
  '<button data-lang="fr"' + (axLang==='fr'?' class="cur"':'') + '>' + _fl('fr') + ' Fran\u00e7ais</button>' +
  '<button data-lang="ru"' + (axLang==='ru'?' class="cur"':'') + '>' + _fl('ru') + ' \u0420\u0443\u0441\u0441\u043a\u0438\u0439</button>' +
  '<button data-lang="de"' + (axLang==='de'?' class="cur"':'') + '>' + _fl('de') + ' Deutsch</button>' +
  '<button data-lang="nl"' + (axLang==='nl'?' class="cur"':'') + '>' + _fl('nl') + ' Nederlands</button>' +
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
    var _tc = (tutDemos[j] === key ? 'cur' : '') + (isRem(tutDemos[j]) ? ' rem' : '');
    dh += '<a href="' + tutDemos[j] + '.html"' + (_tc ? ' class="' + _tc.trim() + '"' : '') + '>' + T[tutDemos[j]] + '</a>';
  }
  dh += '</div></div>';
}
dh += '<div class="sn-g">';
for (var i = 0; i < catOrder.length; i++) {
  var ck = catOrder[i], ci = CATS[ck], demos = catDemos[ck];
  if (!demos.length || ck === 'start' || ck === 'tutorial') continue;
  dh += '<div class="sn-gc"><h5 style="color:' + ci[1] + '">' + ci[0] + '</h5>';
  for (var j = 0; j < demos.length; j++) {
    var _dc = (demos[j] === key ? 'cur' : '') + (isRem(demos[j]) ? ' rem' : '');
    dh += '<a href="' + demos[j] + '.html"' + (_dc ? ' class="' + _dc.trim() + '"' : '') + '>' + T[demos[j]] + '</a>';
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
  var _rc=0;for(var ri=0;ri<demos.length;ri++){if(isRem(demos[ri]))_rc++;}
  var _rl=_rc?' <span style="color:#ffd700;font-size:9px;font-weight:normal">\u2022'+_rc+' new</span>':'';
  mh += '<div class="sn-mc" data-c="' + ck + '" style="color:' + ci[1] + '">' +
    ci[0] + ' (' + demos.length + ')' + _rl + ' <span class="ma">\u25B8</span></div>' +
    '<div class="sn-md" data-c="' + ck + '">';
  for (var j = 0; j < demos.length; j++) {
    mh += '<a href="' + demos[j] + '.html"' + (isRem(demos[j]) ? ' class="rem"' : '') + '>' + T[demos[j]] + '</a>';
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
window.axLi = {en:0,fr:1,ru:2,de:3,nl:4}[axLang]||0;

if (isWorld) return; /* worldview has its own elaborate vow section */
var vf = document.createElement('div');
vf.style.cssText = 'text-align:center;padding:32px 24px 40px;color:#777;font-size:12px;' +
  'font-family:system-ui,sans-serif;border-top:1px solid #1a1a2a;margin-top:40px;line-height:2';
var _vow = _i18n.vow;
var _srcLabel={en:'Source code',fr:'Code source',ru:'\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u043e\u0434',de:'Quellcode',nl:'Broncode'};
var _pdLabel={en:'Public domain (CC0)',fr:'Domaine public (CC0)',ru:'\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0434\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 (CC0)',de:'Gemeinfrei (CC0)',nl:'Publiek domein (CC0)'};
vf.innerHTML = (_vow[0][axLang]||_vow[0].en) + '<br>' +
  '<span style="color:#666">' + (_vow[1][axLang]||_vow[1].en) + '</span><br>' +
  '<span style="color:#555;font-size:10px">' + (_vow[2][axLang]||_vow[2].en) + '</span><br>' +
  '<span style="color:#666;font-size:11px;font-style:italic">' + (_vow[3][axLang]||_vow[3].en) + '</span>' +
  '<div style="margin-top:16px;padding-top:12px;border-top:1px solid #111">' +
  '<a href="https://github.com/antonlebed/antonlebed.com" style="color:#555;font-size:11px;text-decoration:none;letter-spacing:0.5px" ' +
  'onmouseover="this.style.color=\'#888\'" onmouseout="this.style.color=\'#555\'">' +
  (_srcLabel[axLang]||_srcLabel.en) + ' \u00b7 ' + (_pdLabel[axLang]||_pdLabel.en) + '</a>' +
  '<div style="margin-top:8px;color:#555;font-size:10px;line-height:1.6">' +
  ({en:'Contributions in equal measure: Anthropic\u2019s Claude, Anton A.\u00a0Lebed, and the giants whose shoulders we stand on.',fr:'Contributions \u00e0 parts \u00e9gales\u00a0: Claude d\u2019Anthropic, Anton A.\u00a0Lebed, et les g\u00e9ants sur les \u00e9paules desquels nous nous tenons.',ru:'\u0420\u0430\u0432\u043d\u044b\u0439 \u0432\u043a\u043b\u0430\u0434: Claude \u043e\u0442 Anthropic, \u0410\u043d\u0442\u043e\u043d \u0410. \u041b\u0435\u0431\u0435\u0434\u044c \u0438 \u0433\u0438\u0433\u0430\u043d\u0442\u044b, \u043d\u0430 \u0447\u044c\u0438\u0445 \u043f\u043b\u0435\u0447\u0430\u0445 \u043c\u044b \u0441\u0442\u043e\u0438\u043c.',de:'Beitr\u00e4ge zu gleichen Teilen: Anthropics Claude, Anton A.\u00a0Lebed und die Riesen, auf deren Schultern wir stehen.',nl:'Gelijke bijdragen: Anthropics Claude, Anton A.\u00a0Lebed, en de reuzen op wier schouders wij staan.'}[axLang]||'Contributions in equal measure: Anthropic\u2019s Claude, Anton A.\u00a0Lebed, and the giants whose shoulders we stand on.') +
  '</div></div>';
document.body.appendChild(vf);

/* ===== BUG REPORT BUTTON (S811) ===== */
var _bugLabel={en:'Report issue',fr:'Signaler',ru:'\u041e\u0448\u0438\u0431\u043a\u0430',de:'Fehler melden',nl:'Probleem melden'};
var bugBtn = document.createElement('a');
bugBtn.href = '#';
bugBtn.textContent = '\u26a0 ' + (_bugLabel[axLang]||_bugLabel.en);
bugBtn.style.cssText = 'position:fixed;bottom:12px;right:12px;z-index:10000;background:#1a1a2e;color:#d4a017;' +
  'border:1px solid #333;padding:6px 12px;border-radius:4px;font-size:11px;text-decoration:none;' +
  'opacity:0.5;transition:opacity 0.2s;cursor:pointer';
bugBtn.onmouseover = function() { this.style.opacity = '1'; };
bugBtn.onmouseout = function() { this.style.opacity = '0.5'; };
bugBtn.onclick = function(e) {
  e.preventDefault();
  var page = f || location.pathname;
  var ua = navigator.userAgent.replace(/[()]/g, '');
  var title = encodeURIComponent('Bug on ' + page);
  var body = encodeURIComponent('**Page:** ' + location.href + '\n**UA:** ' + ua + '\n**What happened:**\n\n');
  window.open('https://github.com/antonlebed/antonlebed.com/issues/new?title=' + title + '&body=' + body, '_blank');
};
document.body.appendChild(bugBtn);
}
if (document.body) init();
else document.addEventListener('DOMContentLoaded', init);
})();
