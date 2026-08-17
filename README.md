# antonlebed.com

The deployed site for [antonlebed.com](https://antonlebed.com) — working
notes on the primorial tower: the rings Z/p_k# built from the first k
primes, and the mathematics found around them. Static HTML/CSS, zero
client JS, math prerendered to MathML at build time, served via
Cloudflare Workers.

- `public/` — the site: sections of claim-block pages, each section with
  a generated claims index listing every claim, its tier and its verifier
- `public/files/` — every verifier script the claims cite, downloadable
  and runnable (Python; a few need numpy/scipy, the rest are stdlib)
- `worker.js` — Cloudflare Worker: static assets, bare-path routing,
  301 redirects for every URL that ever shipped

This repo is the deploy target; the source of truth lives in a private
research repo. Found a problem?
[Open an issue](https://github.com/antonlebed/antonlebed.com/issues).

Content: public domain (CC0).
