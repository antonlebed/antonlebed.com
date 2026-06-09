// atmosphere.js -- starfield on a single canvas, ANCHORED TO THE PAGE.
// Stars live in DOCUMENT coordinates and are drawn at (x, y - scrollY) on a
// viewport-sized fixed canvas: page-anchored look (stars scroll away with
// content), zero horizontal overflow, small memory, and devicePixelRatio-
// sharp rendering. Their only own motion is a slow downward drift -- the
// page feels like it is rising.
// Look: solid crisp cores with a TIGHT, steeply-fading glow; 28 stars per
// layer per viewport-height; drift one viewport in 80/50/30s; twinkle 7/5/3s
// between base opacity (0.4/0.65/0.9) and 35% of it (matches the original
// box-shadow starfield in git history, pages/atmosphere.js).
// Engine: pre-rendered sprites, 30fps drift cap (immediate redraw on scroll),
// pause in hidden tabs, prefers-reduced-motion = static frame.
// The black sun is pure CSS (style.css #atmo-sun). Stars are an enhancement:
// without JS the page is simply deep space.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  // [color, glowAlpha, coreRadius(px), haloRadius(px), driftSecsPerViewport,
  //  twinkleSecs, baseOpacity]
  var LAYERS = [
    ['#1A4D3E', 0.25, 0.6, 2.5, 80, 7, 0.4 ],
    ['#2D8B6F', 0.40, 1.0, 4.5, 50, 5, 0.65],
    ['#7FFFD4', 0.55, 1.5, 7.0, 30, 3, 0.9 ]
  ];
  var PER_VIEWPORT = 28;          // stars per layer per viewport-height
  var GLOW = '74,255,160';
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  var reduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var canvas = document.createElement('canvas');
  canvas.id = 'atmo-stars';
  document.body.appendChild(canvas);
  var ctx = canvas.getContext('2d');

  var viewW, viewH, docH, stars, sprites;

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

  function build() {
    viewW = document.documentElement.clientWidth;   // EXCLUDES scrollbar
    viewH = window.innerHeight;
    docH = Math.max(document.documentElement.scrollHeight, viewH);
    canvas.style.width = viewW + 'px';
    canvas.style.height = viewH + 'px';
    canvas.width = Math.ceil(viewW * DPR);
    canvas.height = Math.ceil(viewH * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    sprites = [];
    stars = [];
    LAYERS.forEach(function(L, li) {
      sprites.push(makeSprite(L[0], L[1], L[2], L[3]));
      var count = Math.min(150, Math.round(PER_VIEWPORT * docH / viewH));
      for (var i = 0; i < count; i++) {
        stars.push({
          layer: li,
          x: Math.random() * viewW,
          y: Math.random() * docH,     // document coordinates
          phase: Math.random() * Math.PI * 2
        });
      }
    });
  }

  function draw(t, scroll) {
    ctx.clearRect(0, 0, viewW, viewH);
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      var L = LAYERS[s.layer];
      var sp = sprites[s.layer];
      // drift down: one viewport-height every L[4] seconds, wrap on page height
      var yDoc = (s.y + t * viewH / (L[4] * 1000)) % docH;
      var y = yDoc - scroll;           // page-anchored: scrolls away with content
      var half = sp._cssSize / 2;
      if (y < -half || y > viewH + half) continue;
      // twinkle: base opacity down to 35% of it and back
      var tw = reduced ? L[6] :
        L[6] * (0.675 + 0.325 * Math.sin(s.phase + t * 2 * Math.PI / (L[5] * 1000)));
      ctx.globalAlpha = tw;
      ctx.drawImage(sp, s.x - half, y - half, sp._cssSize, sp._cssSize);
    }
    ctx.globalAlpha = 1;
  }

  var last = 0;
  var lastScroll = -1;
  function loop(t) {
    var scroll = window.scrollY || 0;
    if (!document.hidden && (t - last >= 33 || scroll !== lastScroll)) {
      last = t;
      lastScroll = scroll;
      draw(t, scroll);
    }
    requestAnimationFrame(loop);
  }

  build();
  if (reduced) {
    draw(0, window.scrollY || 0);
  } else {
    requestAnimationFrame(loop);
  }

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      build();
      draw(last, window.scrollY || 0);
    }, 250);
  });
})();
