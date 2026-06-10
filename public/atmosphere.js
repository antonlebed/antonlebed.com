// atmosphere.js -- starfield on a single canvas, ANCHORED TO THE VIEWPORT.
// Stars live in viewport coordinates and ignore scroll entirely: the field
// follows the reader down the page. (The black sun is the one page-anchored
// element -- CSS-absolute in style.css #atmo-sun -- so you scroll away from
// it while the stars stay with you.) Their only own motion is a slow
// downward drift -- the page feels like it is rising.
// Look: solid crisp cores with a TIGHT, steeply-fading glow; 28 stars per
// layer; drift one viewport in 80/50/30s; twinkle 7/5/3s between base
// opacity (0.5/0.7/0.9) and 35% of it (matches the original box-shadow
// starfield in git history, pages/atmosphere.js).
// MOBILE URL-BAR IMMUNITY: the bar appearing/disappearing fires resize with
// a ~100px innerHeight change on every scroll. The canvas band is therefore
// sized 100vh -- on mobile that is the LARGE viewport (bar hidden) no matter
// the bar state -- and simply clips under the bar when it shows: geometry
// never changes, so stars never jump. Drift is accumulated incrementally
// per frame (never derived from t * height, which would teleport the field
// on any height change). Only rotation or a real window resize re-sizes the
// band, and even then the same stars rescale via their fractional
// positions -- the field is never re-randomized.
// Engine: pre-rendered sprites, 30fps cap, pause in hidden tabs,
// prefers-reduced-motion = static frame. Stars are an enhancement: without
// JS the page is simply deep space.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  // [color, glowAlpha, coreRadius(px), haloRadius(px), driftSecsPerViewport,
  //  twinkleSecs, baseOpacity]
  var LAYERS = [
    ['#1A4D3E', 0.30, 1.0, 3.5, 80, 7, 0.5 ],
    ['#2D8B6F', 0.45, 1.5, 6.0, 50, 5, 0.7 ],
    ['#7FFFD4', 0.60, 2.2, 9.0, 30, 3, 0.9 ]
  ];
  var PER_LAYER = 28;             // stars per layer
  var GLOW = '74,255,160';
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  var reduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var canvas = document.createElement('canvas');
  canvas.id = 'atmo-stars';
  document.body.appendChild(canvas);
  var ctx = canvas.getContext('2d');

  var viewW, viewH, stars, sprites;
  var drift = [0, 0, 0];          // accumulated px of downward drift per layer

  // Sprite per layer: steep-falloff halo (bright tight, fades fast),
  // solid core on top. Rendered at DPR for crisp small stars.
  function makeSprite(color, alpha, coreR, haloR) {
    var size = Math.ceil(haloR * 2) + 2;
    var c = document.createElement('canvas');
    c.width = c.height = Math.ceil(size * DPR);
    var g = c.getContext('2d');
    g.scale(DPR, DPR);
    var m = size / 2;
    var grad = g.createRadialGradient(m, m, coreR * 0.5, m, m, haloR);
    grad.addColorStop(0,    'rgba(' + GLOW + ',' + alpha + ')');
    grad.addColorStop(0.25, 'rgba(' + GLOW + ',' + (alpha * 0.35).toFixed(3) + ')');
    grad.addColorStop(0.6,  'rgba(' + GLOW + ',' + (alpha * 0.08).toFixed(3) + ')');
    grad.addColorStop(1,    'rgba(' + GLOW + ',0)');
    g.fillStyle = grad;
    g.fillRect(0, 0, size, size);
    g.fillStyle = color;
    g.beginPath();
    g.arc(m, m, coreR, 0, Math.PI * 2);
    g.fill();
    c._cssSize = size;
    return c;
  }

  // Built ONCE: positions are band fractions, so any later re-size just
  // rescales the field instead of rolling new stars.
  function buildStars() {
    sprites = [];
    stars = [];
    LAYERS.forEach(function(L, li) {
      sprites.push(makeSprite(L[0], L[1], L[2], L[3]));
      for (var i = 0; i < PER_LAYER; i++) {
        stars.push({
          layer: li,
          x: Math.random(),          // fraction of band width
          y: Math.random(),          // fraction of the drift wrap-band
          phase: Math.random() * Math.PI * 2
        });
      }
    });
  }

  // The band: full width, 100vh tall. On mobile, 100vh is the LARGE viewport
  // (URL bar hidden) regardless of bar state, so the band is bar-immune from
  // the first frame; with the bar shown it just clips underneath. CSS owns
  // the element size; this reads it back to match the backing store.
  function size() {
    viewW = document.documentElement.clientWidth;   // EXCLUDES scrollbar
    canvas.style.width = viewW + 'px';
    canvas.style.height = '100vh';
    viewH = canvas.clientHeight;
    canvas.width = Math.ceil(viewW * DPR);
    canvas.height = Math.ceil(viewH * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  function draw(t, dt) {
    ctx.clearRect(0, 0, viewW, viewH);
    for (var li = 0; li < LAYERS.length; li++) {
      // drift down one band-height every L[4] seconds, accumulated
      // incrementally so a band re-size never teleports the field
      drift[li] = (drift[li] + dt * viewH / (LAYERS[li][4] * 1000)) %
                  (viewH + sprites[li]._cssSize);
    }
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      var L = LAYERS[s.layer];
      var sp = sprites[s.layer];
      var half = sp._cssSize / 2;
      // wrap on a band one sprite taller than the canvas so stars enter
      // and leave fully offscreen instead of popping at the edges
      var wrapH = viewH + sp._cssSize;
      var y = (s.y * wrapH + drift[s.layer]) % wrapH - half;
      // twinkle: base opacity down to 35% of it and back
      var tw = reduced ? L[6] :
        L[6] * (0.675 + 0.325 * Math.sin(s.phase + t * 2 * Math.PI / (L[5] * 1000)));
      ctx.globalAlpha = tw;
      ctx.drawImage(sp, s.x * viewW - half, y - half, sp._cssSize, sp._cssSize);
    }
    ctx.globalAlpha = 1;
  }

  var last = 0;
  function loop(t) {
    if (!document.hidden && t - last >= 33) {
      // cap dt so a hidden-tab stall reads as a pause, not a drift jump
      var dt = Math.min(t - last, 100);
      last = t;
      draw(t, dt);
    }
    requestAnimationFrame(loop);
  }

  buildStars();
  size();
  if (reduced) {
    draw(0, 0);
  } else {
    requestAnimationFrame(loop);
  }

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      // mobile URL-bar toggles fire resize but leave 100vh unchanged --
      // only rotation or a real window resize moves these
      var w = document.documentElement.clientWidth;
      var h = canvas.clientHeight;
      if (w === viewW && h === viewH) return;
      size();
      draw(last, 0);
    }, 150);
  });
})();
