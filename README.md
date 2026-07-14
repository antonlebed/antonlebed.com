# antonlebed.com

The deployed site for [antonlebed.com](https://antonlebed.com) — working
notes on the primorial tower: the rings Z/p_k# built from the first k
primes. Static HTML/CSS, zero client JS, math prerendered to MathML at
build time, served via Cloudflare Workers.

- `public/` — the site (8 pages), plus `public/files/` — the verifier
  scripts the claims cite, downloadable and runnable
- `worker.js` — Cloudflare Worker: static assets, bare-path routing,
  301 redirects for every URL that ever shipped

This repo is the deploy target; the source of truth lives in a private
research repo. Found a problem?
[Open an issue](https://github.com/antonlebed/antonlebed.com/issues).

Content: public domain (CC0).
