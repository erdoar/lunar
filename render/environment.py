"""Polar environment: a crater-rim site (Shackleton-like), graded pad, craters, boulders, distant massifs,
lunar curvature, the Sun ~1.5 deg above the horizon, Earth low in the sky and a faint star field.
"""
import os
from math import cos, sin, radians, pi, tan
import numpy as np
import bpy
from mathutils import Vector
from meshes import MB, fast_grid_object
import params as P
from materials import TEX

R_MOON = 1737.4e3
rng = np.random.default_rng(7)

# big crater: rim crest 150 m from the rig, towards CRATER_AZ
CRATER_AZ, CRATER_R, CREST = radians(185), 10500.0, 170.0
MASSIFS = [  # (azimuth deg, distance m, height m, sigma m)
    (200, 38e3, 3200, 7e3), (95, 30e3, 2200, 6e3), (160, 52e3, 4200, 9e3), (250, 26e3, 1400, 4e3),
    (20, 45e3, 2600, 8e3), (305, 60e3, 3800, 10e3),
]


def _spectral(n, beta, seed, kmax=12):
    """Band-limited tile: wavelengths from the tile size down to 1/kmax of it."""
    r = np.random.default_rng(seed)
    k = np.sqrt(np.fft.fftfreq(n)[:, None] ** 2 + np.fft.fftfreq(n)[None, :] ** 2) * n
    amp = np.where((k < 1e-9) | (k > kmax), 0, 1 / np.maximum(k, 1) ** beta)
    f = np.real(np.fft.ifft2(amp * np.exp(2j * np.pi * r.uniform(0, 1, (n, n)))))
    return (f - f.mean()) / f.std()


NOISE = [(_spectral(256, 1.6, s, kmax), L, a) for s, L, a, kmax in
         ((1, 8000.0, 15.0, 4), (2, 1500.0, 3.0, 6), (3, 200.0, 0.5, 8), (4, 25.0, 0.06, 12))]


def _sample(tile, L, x, y):
    n = tile.shape[0]
    u, v = (x / L * n) % n, (y / L * n) % n
    i0, j0 = np.floor(u).astype(int), np.floor(v).astype(int)
    fu, fv = u - i0, v - j0
    i0, j0 = i0 % n, j0 % n
    i1, j1 = (i0 + 1) % n, (j0 + 1) % n
    return (tile[j0, i0] * (1 - fu) * (1 - fv) + tile[j0, i1] * fu * (1 - fv)
            + tile[j1, i0] * (1 - fu) * fv + tile[j1, i1] * fu * fv)


def _sp(x, w):
    return w * np.logaddexp(0, x / w)


def _crater_field():
    out = []
    for _ in range(500):                                          # far field, 30 to 900 m
        r = 400 + rng.uniform(0, 1) ** 0.7 * 9000
        a = rng.uniform(0, 2 * pi)
        out.append((r * cos(a), r * sin(a), 30 * (1 + rng.pareto(1.8)) if rng.uniform() < 0.9 else rng.uniform(200, 900)))
    for _ in range(420):                                          # near field, 1.5 to 40 m
        r = rng.uniform(60, 480)
        a = rng.uniform(0, 2 * pi)
        out.append((r * cos(a), r * sin(a), min(40, 1.5 * (1 + rng.pareto(1.5)))))
    return np.array(out)


CRATERS = _crater_field()


def height(x, y, curvature=True, pad=True):
    x, y = np.asarray(x, float), np.asarray(y, float)
    cx, cy = (CRATER_R + CREST) * cos(CRATER_AZ), (CRATER_R + CREST) * sin(CRATER_AZ)
    t = np.hypot(x - cx, y - cy) - CRATER_R                     # >0 outside the crater
    z = -(0.035 * _sp(t, 60) + 0.58 * _sp(-t, 60))           # crest ~170 m out, inner wall ~30 deg
    floor = -3600
    z = np.where(z < floor + 200, floor + 200 * np.exp((z - floor - 200) / 200), z)
    for az, d, h, s in MASSIFS:
        mx, my = d * cos(radians(az)), d * sin(radians(az))
        rr = np.hypot(x - mx, y - my) / s
        z = z + h * np.exp(-rr ** 2) * (1 + 0.25 * _sample(NOISE[0][0], 9000, x + az, y))
    for tile, L, a in NOISE:
        z = z + a * _sample(tile, L, x, y)
    z = z + 30 * np.exp(-(np.hypot(x, y) / 650) ** 2)        # the site is a knoll: a peak of near-eternal light
    for (ccx, ccy, D) in CRATERS:
        Rr = D / 2
        near = (np.abs(x - ccx) < 2 * Rr) & (np.abs(y - ccy) < 2 * Rr)
        if not near.any():
            continue
        r = np.hypot(x[near] - ccx, y[near] - ccy) / Rr
        dz = np.where(r < 1, 0.2 * D * (r ** 2 - 1) + 0.035 * D, 0.035 * D * np.exp(-((r - 1) / 0.35) ** 2))
        z[near] += dz
    rr = np.hypot(x, y)
    if pad:
        z0 = _z0()
        w = np.clip((rr - 48) / 30, 0, 1)
        w = w * w * (3 - 2 * w)
        z = z0 + (z - z0) * w - z0                  # flat graded pad at z = 0, blending out to 78 m
    if curvature:
        z = z - rr ** 2 / (2 * R_MOON)
    return z


_Z0 = None


def _z0():
    global _Z0
    if _Z0 is None:
        a = np.linspace(0, 2 * pi, 64, endpoint=False)
        _Z0 = float(np.mean(height(48 * np.cos(a), 48 * np.sin(a), curvature=False, pad=False)))
    return _Z0


def terrain(mats):
    _z0()
    col = bpy.context.scene.collection
    # near field: 960 m square at 2 m
    n = 481
    g = np.linspace(-480, 480, n)
    X, Y = np.meshgrid(g, g)
    Z = height(X, Y)
    near = fast_grid_object('terrain_near', X, Y, Z, mats['regolith'], 1.0, col)
    # far field: polar, 470 m to 90 km, pushed down inside the near square to avoid overlap
    rad = np.geomspace(440, 90e3, 190)
    ang = np.linspace(2 * pi, 0, 1201)            # clockwise so the faces point up
    A, Rr = np.meshgrid(ang, rad)
    XF, YF = Rr * np.cos(A), Rr * np.sin(A)
    ZF = height(XF, YF)
    inside = (np.abs(XF) < 482) & (np.abs(YF) < 482)
    ZF = np.where(inside, ZF - 0.6, ZF)
    far = fast_grid_object('terrain_far', XF, YF, ZF, mats['regolith'], 1.0, col)
    return near, far


def rocks(mats):
    mb = MB()
    shapes = []
    for s in range(6):
        r2 = np.random.default_rng(100 + s)
        n = 10
        verts = []
        for i in range(n // 2 + 1):
            th = pi * i / (n // 2)
            for j in range(n):
                ph = 2 * pi * j / n
                verts.append([sin(th) * cos(ph), sin(th) * sin(ph), cos(th)])
        verts = np.array(verts) * r2.uniform(0.7, 1.25, (len(verts), 1)) * np.array([1, r2.uniform(0.6, 1), r2.uniform(0.45, 0.8)])
        faces, uvs = [], []
        for i in range(n // 2):
            for j in range(n):
                a, b = i * n + j, i * n + (j + 1) % n
                faces.append((a, a + n, b + n, b))
                uvs.append(((j, i), (j, i + 1), (j + 1, i + 1), (j + 1, i)))
        shapes.append((verts, faces, uvs))
    pts = []
    for _ in range(2600):
        r = 50 + rng.uniform(0, 1) ** 0.8 * 430
        a = rng.uniform(0, 2 * pi)
        size = min(2.2, 0.08 * (1 + rng.pareto(1.7)))
        pts.append((r * cos(a), r * sin(a), size))
    for _ in range(140):                                          # a few small stones on the pad
        r = rng.uniform(5, 48); a = rng.uniform(0, 2 * pi)
        pts.append((r * cos(a), r * sin(a), rng.uniform(0.03, 0.1)))
    pts = np.array(pts)
    zs = height(pts[:, 0], pts[:, 1])
    for (x, y, s), z in zip(pts, zs):
        v, f, u = shapes[rng.integers(0, 6)]
        rot = rng.uniform(0, 2 * pi)
        Rm = np.array([[cos(rot), -sin(rot), 0], [sin(rot), cos(rot), 0], [0, 0, 1]])
        mb.add((v * s) @ Rm.T + (x, y, z - 0.25 * s), f, [tuple((a * s, b * s) for a, b in q) for q in u], 0, True)
    return mb.build('boulders', [mats['regolith']])


def sky(mats):
    sc = bpy.context.scene
    w = bpy.data.worlds.new('space')
    sc.world = w
    nt = w.node_tree
    bg = nt.nodes['Background']
    env = nt.nodes.new('ShaderNodeTexEnvironment')
    env.image = bpy.data.images.load(os.path.join(TEX, 'stars.png'))
    env.image.colorspace_settings.name = 'Non-Color'
    nt.links.new(env.outputs['Color'], bg.inputs['Color'])
    bg.inputs['Strength'].default_value = 0.35
    # Sun
    d = Vector((cos(P.SUN_EL) * cos(P.SUN_AZ), cos(P.SUN_EL) * sin(P.SUN_AZ), sin(P.SUN_EL)))
    light = bpy.data.lights.new('Sun', 'SUN')
    light.energy = 5.0
    light.angle = radians(0.53)
    sun = bpy.data.objects.new('Sun', light)
    sun.rotation_euler = (-d).to_track_quat('-Z', 'Y').to_euler()
    sc.collection.objects.link(sun)
    # Earth: 1.9 deg across, lit by the same Sun (gibbous from here)
    D = 150e3
    e = Vector((cos(P.EARTH_EL) * cos(P.EARTH_AZ), cos(P.EARTH_EL) * sin(P.EARTH_AZ), sin(P.EARTH_EL))) * D
    bpy.ops.mesh.primitive_uv_sphere_add(radius=D * tan(radians(0.95)), segments=64, ring_count=32, location=e)
    earth = bpy.context.object
    earth.name = 'Earth'
    earth.rotation_euler = (radians(23), 0, radians(40))
    earth.data.materials.append(mats['earth'])
    bpy.ops.object.shade_smooth()
    return sun, earth
