"""Procedural texture maps for the render materials (numpy -> PNG). Deterministic: same seed, same files.

Run: python3 textures.py   (writes render/textures/*.png)
"""
import os
import numpy as np
from PIL import Image

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'textures')
rng = np.random.default_rng(33)


def save(name, a, mode=None):
    a = np.clip(a, 0, 1)
    img = Image.fromarray((a * 255).astype(np.uint8), mode)
    img.save(os.path.join(OUT, name), optimize=True)
    print('wrote', name, img.size)


def fbm(h, w, octaves=6, base=4, seed=0):
    """Tileable isotropic fractal noise by spectral synthesis (1/f^beta filtered white noise).

    `base` sets the lowest feature frequency (cycles per tile); `octaves` sets how far the detail extends.
    """
    r = np.random.default_rng(seed)
    ky = np.fft.fftfreq(h)[:, None] * h
    kx = np.fft.fftfreq(w)[None, :] * w
    k = np.sqrt(kx * kx + ky * ky)
    beta = 1.0 + 4.0 / octaves                     # fewer octaves -> steeper spectrum, smoother
    amp = np.where(k < 1e-9, 0, 1 / np.maximum(k, base * 0.5) ** beta)
    amp[k > base * 2 ** octaves] = 0
    spec = amp * np.exp(2j * np.pi * r.uniform(0, 1, (h, w)))
    out = np.real(np.fft.ifft2(spec))
    out -= out.min()
    return out / out.max()


def solar_cell():
    """One 2 m x 1 m panel: 16 x 8 cells of 0.125 m, 3 mm gaps, 2 busbars per cell, fine fingers."""
    W, H = 2048, 1024
    px = W / 2.0                                   # px per metre
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    cell = 0.125 * px
    u, v = (xx % cell) / cell, (yy % cell) / cell
    gap = 0.003 * px / cell
    edge = 0.02 * px / cell                         # panel border frame
    rgb = np.zeros((H, W, 3))
    base = np.array([0.035, 0.05, 0.12])
    mott = fbm(H, W, 5, 6, 1)[..., None]
    ci, cj = (xx // cell).astype(int), (yy // cell).astype(int)
    tone = rng.uniform(0.85, 1.15, (int(H / cell) + 1, int(W / cell) + 1))[cj, ci][..., None]
    rgb[:] = base * tone * (0.85 + 0.3 * mott)
    finger = (np.abs(((u * 48) % 1) - 0.5) < 0.06)
    rgb[finger] = rgb[finger] * 1.25 + 0.006
    for b in (0.3, 0.7):
        bus = np.abs(v - b) < 0.012
        rgb[bus] = [0.32, 0.33, 0.34]
    gaps = (u < gap) | (u > 1 - gap) | (v < gap) | (v > 1 - gap)
    rgb[gaps] = [0.22, 0.22, 0.21]
    border = (xx < edge * cell) | (xx > W - edge * cell) | (yy < edge * cell) | (yy > H - edge * cell)
    rgb[border] = [0.08, 0.08, 0.09]
    save('solar_cell.png', rgb, 'RGB')


def cfrp_twill():
    """2/2 twill weave, tileable, 512 px = 0.1 m."""
    N, tows = 512, 16
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    t = N / tows
    i, j = (xx // t).astype(int), (yy // t).astype(int)
    warp_up = ((i + j) // 2) % 2 == 0
    u, v = (xx % t) / t, (yy % t) / t
    shade_w = 0.5 + 0.5 * np.sin(np.pi * v)          # warp tow rounds across its width
    shade_f = 0.5 + 0.5 * np.sin(np.pi * u)
    s = np.where(warp_up, shade_w, shade_f)
    fib = 0.08 * np.sin(np.where(warp_up, u, v) * 2 * np.pi * 30)
    g = 0.035 + 0.05 * s + 0.01 * fib
    save('cfrp_twill.png', np.dstack([g, g, g * 1.04]), 'RGB')
    save('cfrp_twill_bump.png', s * 0.9 + 0.1 * fib, 'L')


def grating():
    """Bar grating alpha: load bars every 30 mm, cross bars every 100 mm (512 px = 0.3 m)."""
    N = 512
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    p = N / 0.3
    load = ((xx % (0.03 * p)) < 0.004 * p)
    cross = ((yy % (0.10 * p)) < 0.006 * p)
    save('grating_alpha.png', (load | cross).astype(float), 'L')


def mli_crinkle():
    """Crinkled multilayer insulation height map (tileable)."""
    N = 1024
    h = fbm(N, N, 7, 8, 5)
    ridges = 1 - np.abs(2 * fbm(N, N, 5, 6, 6) - 1)
    save('mli_bump.png', 0.6 * h + 0.4 * ridges ** 3, 'L')


def regolith():
    """Albedo variation and small-scale bump for regolith (tileable, 1024 px = 8 m)."""
    N = 1024
    a = 0.75 * fbm(N, N, 7, 3, 7) + 0.25 * fbm(N, N, 4, 24, 8)
    save('regolith_albedo.png', 0.35 + 0.65 * a, 'L')
    pits = np.zeros((N, N))
    yy, xx = np.mgrid[0:N, 0:N].astype(float)
    for _ in range(140):                            # small fresh craters 0.1 to 1 m
        cx, cy = rng.uniform(0, N, 2)
        r = rng.pareto(2.2) * 8 + 6
        dx = (xx - cx + N / 2) % N - N / 2
        dy = (yy - cy + N / 2) % N - N / 2
        d = np.sqrt(dx * dx + dy * dy) / r
        pits += np.where(d < 1, d ** 2 - 1, 0.25 * np.exp(-((d - 1.05) / 0.25) ** 2))
    b = 0.5 * fbm(N, N, 8, 6, 9) + 0.12 * pits
    b -= b.min()
    save('regolith_bump.png', b / b.max(), 'L')


def earth():
    """Equirectangular Earth: oceans, continents, ice caps and clouds (stylised)."""
    W, H = 1024, 512
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    lat = (0.5 - yy / H) * np.pi
    land = fbm(H, W, 6, 2, 11) > 0.56
    rgb = np.zeros((H, W, 3))
    rgb[:] = [0.02, 0.07, 0.22]
    tone = fbm(H, W, 5, 6, 12)[..., None]
    green = np.array([0.12, 0.22, 0.08]) * (0.7 + 0.6 * tone)
    desert = np.array([0.45, 0.36, 0.22]) * (0.8 + 0.4 * tone)
    dry = (np.abs(lat) > 0.25) & (np.abs(lat) < 0.6)
    rgb[land] = np.where(dry[land][:, None], desert[land], green[land])
    ice = np.abs(lat) > 1.2
    rgb[ice] = [0.9, 0.92, 0.95]
    cl = fbm(H, W, 7, 4, 13)
    cl = np.clip((cl - 0.5) * 3.5, 0, 1)[..., None]
    rgb = rgb * (1 - cl * 0.9) + cl * 0.92
    save('earth.png', rgb, 'RGB')


def stars():
    """Equirectangular star field, sparse and faint (artistic: real exposures for a sunlit scene show none)."""
    W, H = 4096, 2048
    img = np.zeros((H, W))
    n = 5000
    u = rng.uniform(0, 1, n)
    v = np.arccos(rng.uniform(-1, 1, n)) / np.pi    # uniform on the sphere
    mag = rng.pareto(1.6, n)
    x, y = (u * W).astype(int), (v * H).astype(int)
    img[y, x] = np.clip(0.08 + 0.12 * mag, 0, 1)
    save('stars.png', img, 'L')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    solar_cell(); cfrp_twill(); grating(); mli_crinkle(); regolith(); earth(); stars()
