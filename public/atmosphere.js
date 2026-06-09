// atmosphere.js -- starfield on a single canvas, ANCHORED TO THE PAGE.
// The canvas is absolute-positioned and document-sized: stars belong to the
// page and scroll away with it (no viewport-following). Their only own
// motion is a slow downward drift -- the page feels like it is rising.
// Visual parameters match the original box-shadow starfield (git history,
// pages/atmosphere.js): 28 stars per layer per viewport-height, crisp
// 1/2/3px cores with a soft glow halo, drift of one viewport in 80/50/30s,
// twinkle 7/5/3s between base opacity and 35% of it.
// Canvas engine wins kept: pre-rendered sprites (no per-frame shadowBlur),
// 30fps cap, pause in hidden tabs, prefers-reduced-motion = static frame.
// The black sun is pure CSS (style.css #atmo-sun). Stars are an enhancement:
// without JS the page is simply deep space.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  // [color, glowAlpha, coreRadius(px), haloRadius(px), driftSecsPerViewport,
  //  twinkleSecs, baseOpacity]
  var LAYERS = [
    ['#1A4D3E', 0.20, 0.7,  5, 80, 7, 0.4 ],
    ['#2D8B6F', 0.40, 1.0,  9, 50, 5, 0.65],
    ['#7FFFD4', 0.65, 1.5, 13, 30, 3, 0.9 ]
  ];
  var PER_VIEWPORT = 28;          // stars per layer per viewport-height
  var GLOW = '74,255,160';
  var reduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var canvas = document.createElement('canvas');
  canvas.id = 'atmo-stars';
  document.body.appendChild(canvas);
  var ctx = canvas.getContext('2d');

  var W, H, viewH, stars, sprites;

  // Sprite per layer: soft halo gradient underneath, crisp solid core on top.
  function makeSprite(color, alpha, coreR, haloR) {
    var size = Math.ceil(haloR * 2) + 2;
    var c = document.createElement('canvas');
    c.width = c.height = size;
    var g = c.getContext('2d');
    var m = size / 2;
    var grad = g.createRadialGradient(m, m, coreR, m, m, haloR);
    grad.addColorStop(0, 'rgba(' + GLOW + ',' + alpha + ')');
    grad.addColorStop(1, 'rgba(' + GLOW + ',0)');
    g.fillStyle = grad;
    g.fillRect(0, 0, size, size);
    g.fillStyle = color;
    g.beginPath();
    g.arc(m, m, coreR, 0, Math.PI * 2);
    g.fill();
    return c;
  }

  function build() {
    viewH = window.innerHeight;
    W = canvas.width = window.innerWidth;
    H = canvas.height = document.documentElement.scrollHeight;
    sprites = [];
    stars = [];
    LAYERS.forEach(function(L, li) {
      sprites.push(makeSprite(L[0], L[1], L[2], L[3]));
      var count = Math.min(150, Math.round(PER_VIEWPORT * H / viewH));
      for (var i = 0; i < count; i++) {
        stars.push({
          layer: li,
          x: Math.random() * W,
          y: Math.random() * H,
          phase: Math.random() * Math.PI * 2
        });
      }
    });
  }

  function draw(t) {
    ctx.clearRect(0, 0, W, H);
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      var L = LAYERS[s.layer];
      var sp = sprites[s.layer];
      // drift down: one viewport-height every L[4] seconds, wrap on page height
      var y = (s.y + t * viewH / (L[4] * 1000)) % H;
      // twinkle: base opacity down to 35% of it and back
      var tw = reduced ? L[6] :
        L[6] * (0.675 + 0.325 * Math.sin(s.phase + t * 2 * Math.PI / (L[5] * 1000)));
      ctx.globalAlpha = tw;
      ctx.drawImage(sp, s.x - sp.width / 2, y - sp.height / 2);
    }
    ctx.globalAlpha = 1;
  }

  var last = 0;
  function loop(t) {
    if (!document.hidden && t - last >= 33) {   // ~30fps cap
      last = t;
      draw(t);
    }
    requestAnimationFrame(loop);
  }

  build();
  if (reduced) {
    draw(0);
  } else {
    requestAnimationFrame(loop);
  }

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() { build(); draw(last); }, 250);
  });
})();
