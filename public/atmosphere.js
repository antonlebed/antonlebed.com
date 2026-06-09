// atmosphere.js -- starfield on a single canvas.
// Three depth layers drift slowly DOWNWARD (the page feels like it is rising);
// scrolling adds parallax per layer. Glows are pre-rendered sprites (no
// per-frame shadowBlur), the loop is capped at 30fps and pauses in hidden
// tabs. prefers-reduced-motion gets a single static frame.
// The black sun is pure CSS (style.css #atmo-sun). Stars are an enhancement:
// without JS the page is simply dark.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  // [color, glowAlpha, radius(px), drift(px/s), parallax, twinkle(s), density(per Mpx)]
  var LAYERS = [
    ['#1A4D3E', 0.20, 2.5,  4, 0.02, 7, 16],
    ['#2D8B6F', 0.40, 3.5,  8, 0.05, 5, 14],
    ['#7FFFD4', 0.60, 4.5, 14, 0.10, 3, 12]
  ];
  var GLOW = '74,255,160';
  var reduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var canvas = document.createElement('canvas');
  canvas.id = 'atmo-stars';
  document.body.appendChild(canvas);
  var ctx = canvas.getContext('2d');

  var W, H, stars, sprites;

  // One soft-glow sprite per layer: bright core + radial halo, baked once.
  function makeSprite(color, alpha, r) {
    var size = Math.ceil(r * 8);
    var c = document.createElement('canvas');
    c.width = c.height = size;
    var g = c.getContext('2d');
    var m = size / 2;
    var grad = g.createRadialGradient(m, m, 0, m, m, m);
    grad.addColorStop(0, color);
    grad.addColorStop(0.12, color);
    grad.addColorStop(0.3, 'rgba(' + GLOW + ',' + alpha + ')');
    grad.addColorStop(1, 'rgba(' + GLOW + ',0)');
    g.fillStyle = grad;
    g.fillRect(0, 0, size, size);
    return c;
  }

  function build() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
    sprites = [];
    stars = [];
    LAYERS.forEach(function(L, li) {
      sprites.push(makeSprite(L[0], L[1], L[2]));
      var count = Math.max(8, Math.round(W * H * L[6] / 1e6));
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
    var scroll = window.scrollY || 0;
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      var L = LAYERS[s.layer];
      var sp = sprites[s.layer];
      // drift down + scroll parallax (deeper layers move less)
      var y = (s.y + t * L[3] / 1000 - scroll * L[4]) % H;
      if (y < 0) y += H;
      // twinkle: ease between 35% and 100% of base opacity
      var tw = reduced ? 1 :
        0.675 + 0.325 * Math.sin(s.phase + t * 2 * Math.PI / (L[5] * 1000));
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
